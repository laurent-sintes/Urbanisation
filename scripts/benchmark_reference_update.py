"""Compare repeated builds and the maintained review workflow in disposable copies.

Never publish, activate, modify live inputs or grant a real agreement. Automatic
assessments below belong only to the explicitly synthetic benchmark fixture.
"""
import argparse
from contextlib import contextmanager
import json
from pathlib import Path
import shutil
import sys
from statistics import median
from time import perf_counter
import uuid
from unittest.mock import patch

try:
    from . import prepare_release as workflow
    from .structured_io import dumps, read, working_path
except ImportError:
    import prepare_release as workflow
    from structured_io import dumps, read, working_path


def source_files(root):
    models, pointer, _, _, manifest_path = workflow.load_current(root)
    manifest = read(manifest_path)
    files = {models / p for p in ('release/index.json', 'provenance/source-records.json')}
    for folder in ('backlog', 'schemas'):
        files.update(p for p in (models / folder).iterdir()
                     if p.is_file() and p.suffix in ('.json', '.yaml', '.yml'))
    index = read(models / 'release/index.json')
    files.update(workflow.checked_path(models / 'release', e['descriptor']) for e in index['publications'])
    files.update((models / 'release' / pointer['path'], manifest_path))
    if pointer.get('release_notes'):
        files.add(workflow.checked_path(models / 'release', pointer['release_notes']))
    for key in ('input_revision', 'decisions', 'provenance'):
        path = (manifest_path.parent / manifest[key + '_path']).resolve()
        if not path.is_relative_to(models):
            raise ValueError('Frozen input outside model directory')
        files.add(path)
    deferred = models / 'revisions' / pointer['version'] / 'deferred'
    if deferred.exists():
        files.update(p for p in deferred.iterdir() if p.is_file())
    guide_index = models / 'modeling-guides/index.yaml'
    if guide_index.exists():
        files.add(guide_index)
        files.update(workflow.checked_path(guide_index.parent, e['path']) for e in read(guide_index)['guides'])
    return sorted(files)


@contextmanager
def isolated_copy(root, files):
    base = (root / '.runtime/reference-benchmark').resolve()
    base.mkdir(parents=True, exist_ok=True)
    folder = base / uuid.uuid4().hex
    folder.mkdir()
    try:
        for path in files:
            destination = folder / path.relative_to(root)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        yield folder
    finally:
        resolved = folder.resolve()
        if resolved.parent != base or len(resolved.name) != 32:
            raise ValueError('Unsafe benchmark cleanup target')
        shutil.rmtree(resolved)


def simulate_assessment(folder):
    path = folder / 'assessment.yaml'
    review = read(folder / 'review.json')
    eligible = {e['decision_id'] for e in review['items'] if e['eligible_for_reassessment']}
    assessment = read(path)
    assessment['reviewer'] = 'Synthetic benchmark only'
    for entry in assessment['items']:
        entry.update(action='retain' if entry['decision_id'] in eligible else 'defer',
                     rationale='Simulation isolée : précision de note éditoriale, aucune valeur approuvée modifiée. Aucun accord réel.')
    path.write_text(dumps(assessment), encoding='utf-8')


def stable_candidate(value):
    if isinstance(value, dict):
        return {k: stable_candidate(v) for k, v in value.items() if k != 'last_modified'}
    if isinstance(value, list):
        return [stable_candidate(v) for v in value]
    return value


def run_path(root, mode, identifier):
    version = '2099-09-19.1'
    model_path = working_path(root / 'modeles/backlog')
    model = read(model_path)
    node = next((n for n in model['nodes'] if n['id'] == identifier), None)
    if node is None:
        raise ValueError('Unknown benchmark target: ' + identifier)
    node['review']['note'] += ' Simulation isolée de précision éditoriale pour mesure du workflow.'
    model_path.write_text(dumps(model, model_path.suffix), encoding='utf-8')
    _, _, previous, _, _ = workflow.load_current(root)
    sources = previous['publication']['source_refs']
    timings = {}
    def measure(label, operation):
        start = perf_counter()
        result = operation()
        timings[label] = round(perf_counter() - start, 4)
        return result
    start = perf_counter()
    with patch.object(workflow, 'build_candidate', wraps=workflow.build_candidate) as builds:
        bundle = measure('diagnostic', lambda: workflow.build_candidate(root, version, sources, include_review=mode == 'maintained'))
        if mode == 'repeated':
            bundle = measure('repeated_review_build', lambda: workflow.build_candidate(root, version, sources, include_review=True))
        folder = root / 'review'
        measure('dossier', lambda: workflow.decision_review.save_review(folder, bundle['review'], bundle['report']))
        simulate_assessment(folder)
        if mode == 'repeated':
            measure('repeated_final_build', lambda: workflow.build_candidate(root, version, sources, review_path=folder))
        else:
            measure('inspect_saved', lambda: workflow.inspect_artifact(folder, 'review', identifier))
        result = measure('prepare', lambda: workflow.prepare(root, version, sources, review_path=folder))
        count = builds.call_count
    elapsed = round(perf_counter() - start, 4)
    if result['summary']['validation_error_count']:
        raise ValueError('Invalid benchmark preparation')
    candidate = read(result['candidate'])
    return {'seconds': elapsed, 'steps': timings, 'candidate_builds': count,
            'suspended_decisions_examined': len(bundle['review']['items']),
            'candidate_sha256_without_timestamps': workflow.canonical_sha256(stable_candidate(candidate))}


def benchmark(root, identifier='D04.j', iterations=3):
    root = Path(root).resolve()
    files = source_files(root)
    before = {p: workflow.digest(p) for p in files}
    samples = {'repeated': [], 'maintained': []}
    for iteration in range(iterations):
        # Alternate order to avoid assigning every first/cold run to the same path.
        modes = ('repeated', 'maintained') if iteration % 2 == 0 else ('maintained', 'repeated')
        for mode in modes:
            with isolated_copy(root, files) as fixture:
                samples[mode].append(run_path(fixture, mode, identifier))
            print(f"Iteration {iteration + 1}/{iterations}: {mode}, {samples[mode][-1]['seconds']:.3f}s", file=sys.stderr, flush=True)
        if samples['repeated'][-1]['candidate_sha256_without_timestamps'] != samples['maintained'][-1]['candidate_sha256_without_timestamps']:
            raise ValueError('Workflow candidates differ beyond generation timestamps')
    if before != {p: workflow.digest(p) for p in files}:
        raise ValueError('Live inputs changed during benchmark')
    medians = {mode: round(median(s['seconds'] for s in values), 4) for mode, values in samples.items()}
    return {'scenario': 'One editorial note changed; historical approved values unchanged',
            'target': identifier, 'iterations': iterations, 'median_seconds': medians,
            'reduction_percent': round(100 * (1 - medians['maintained'] / medians['repeated']), 1),
            'copied_files_per_fixture': len(files), 'copied_bytes_per_fixture': sum(p.stat().st_size for p in files),
            'live_inputs_unchanged': True, 'publication_performed': False,
            'limits': 'Local Python workflow only; excludes copying, LLM generation and real semantic reassessment. Caches are reused.',
            'samples': samples}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=workflow.ROOT)
    parser.add_argument('--id', default='D04.j', dest='identifier')
    parser.add_argument('--iterations', type=int, choices=range(1, 11), default=3)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error('Output must be a new file')
    result = benchmark(args.root, args.identifier, args.iterations)
    if args.output:
        workflow.write(args.output, result)
    print(json.dumps({k: v for k, v in result.items() if k != 'samples'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
