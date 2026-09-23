"""Measure agreement writes on a disposable copy; never register a real approval."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
from time import perf_counter
import uuid

try:
    from . import record_decision as recorder
    from . import parsed_cache
    from . import decision_registry
    from .structured_io import read, loads, load_for_sequence_append
except ImportError:
    import record_decision as recorder
    import parsed_cache
    import decision_registry
    from structured_io import read, loads, load_for_sequence_append


def benchmark(root, target, source, runs=3):
    if runs < 2:
        raise ValueError('Use at least two runs to compare cold and warm writes')
    root = Path(root).resolve()
    base = root / '.runtime/decision-benchmark'
    folder = base / uuid.uuid4().hex
    folder.mkdir(parents=True)
    relatives = [recorder.REGISTRY_PATH, 'modeles/backlog/model.yaml',
                 'modeles/backlog/glossary.yaml', 'modeles/provenance/source-records.json']
    original_hashes = {}
    for relative in relatives:
        origin = root / relative
        destination = folder / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origin, destination)
        original_hashes[relative] = sha256(origin.read_bytes()).hexdigest()
    shards = root / 'modeles/backlog/decision-intents'
    if shards.exists():
        shutil.copytree(shards, folder / 'modeles/backlog/decision-intents')
        for origin in shards.rglob('*.yaml'):
            original_hashes[origin.relative_to(root).as_posix()] = sha256(origin.read_bytes()).hexdigest()
    cache_before = parsed_cache.DIRECTORY
    parsed_cache.DIRECTORY = folder / 'cache'
    try:
        registry = folder / recorder.REGISTRY_PATH
        original_bytes = registry.read_bytes()
        timings = []
        params = dict(collection='nodes', target_id=target, fields=['name'],
                      source_refs=[source], author='Synthetic benchmark',
                      decided_at='2026-09-22', interpretation='explicit',
                      note='Synthetic performance fixture, never a real approval.', reviewer='Benchmark')
        for index in range(runs):
            start = perf_counter()
            recorder.record_intent(folder, intent_id=f'BENCHMARK-{index}', **params)
            elapsed = perf_counter() - start
            timings.append(elapsed)
            print(json.dumps({'run': index, 'seconds': round(elapsed, 3)}), flush=True)
        start = perf_counter()
        result = recorder.record_intent(folder, intent_id=f'BENCHMARK-{runs - 1}', **params)
        idempotent_seconds = perf_counter() - start
        assert not result['recorded']

        original, offset = load_for_sequence_append(original_bytes, 'intents')
        sharded = decision_registry.is_index(original)
        if sharded:
            original = {'schema_version': '1.0.0',
                        'intents': [decision_registry.load_entry(registry, e) for e in original['entries']],
                        'suspensions': original['suspensions']}
        final_bytes = registry.read_bytes()
        # Independent strict parse: do not trust the cache seeded by the writer.
        start = perf_counter()
        if sharded:
            index = loads(final_bytes.decode('utf-8-sig'))
            decision_registry.verify_index(registry, index)
            final = {'schema_version': '1.0.0',
                     'intents': [loads(decision_registry.shard_path(registry, e).read_text(encoding='utf-8'))[0] for e in index['entries']],
                     'suspensions': index['suspensions']}
        else:
            final = loads(final_bytes.decode('utf-8-sig'))
        independent_parse_seconds = perf_counter() - start
        recorder.validate_document(final, read(folder / 'modeles/provenance/source-records.json'))
        assert final['intents'][:-runs] == original['intents']
        assert final.get('suspensions') == original.get('suspensions')
        if offset is not None:
            text = original_bytes.decode('utf-8-sig')
            prefix, suffix = text[:offset].encode(), text[offset:].encode()
            if original_bytes.startswith(b'\xef\xbb\xbf'):
                prefix = b'\xef\xbb\xbf' + prefix
            assert final_bytes.startswith(prefix) and final_bytes.endswith(suffix)
        for relative, digest in original_hashes.items():
            assert sha256((root / relative).read_bytes()).hexdigest() == digest, relative
        report = dict(source_bytes=len(original_bytes), existing_intents=len(original['intents']),
                      record_seconds=timings, idempotent_seconds=idempotent_seconds,
                      independent_parse_seconds=independent_parse_seconds,
                      historical_values_unchanged=True, source_files_unchanged=True,
                      historical_bytes_preserved=offset is not None or sharded, sharded=sharded)
        (base / 'latest.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        return report
    finally:
        parsed_cache.DIRECTORY = cache_before
        # Delete only the uniquely created fixture within the intended workspace.
        resolved = folder.resolve()
        if resolved.parent != base.resolve() or resolved.name != folder.name or len(resolved.name) != 32:
            raise ValueError('Unsafe benchmark cleanup path')
        shutil.rmtree(resolved)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--target', required=True)
    parser.add_argument('--source', required=True)
    parser.add_argument('--runs', type=int, default=3)
    arguments = vars(parser.parse_args())
    print(json.dumps(benchmark(**arguments), indent=2))
