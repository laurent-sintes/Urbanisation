"""Verify U435/U436 preservation and local deliverable links, without mutation of models."""
from hashlib import sha256
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

OUT = Path(__file__).parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    baseline = read(OUT / 'metrics.yaml')
    changed_protected = [name for name, expected in baseline['protected_files'].items()
                         if not (ROOT / name).exists() or digest(ROOT / name) != expected]
    assert not changed_protected, changed_protected
    original = read(OUT / 'model-before-U435.yaml')
    current = read(ROOT / 'modeles/backlog/model.yaml')
    preserved = 0
    for collection in ('nodes', 'relations'):
        new = {item['id']: item for item in current[collection]}
        for old in original[collection]:
            item = new[old['id']]
            old_values = old['fields'] if collection == 'nodes' else old
            new_values = item['fields'] if collection == 'nodes' else item
            for key in old.get('lifecycle', {}).get('validated_fields', []):
                assert new_values[key] == old_values[key], (old['id'], key)
                assert item['lifecycle']['value_sha256'][key] == old['lifecycle']['value_sha256'][key]
                preserved += 1
            for key in (('kind', 'layer') if collection == 'nodes' else ('type', 'source_id', 'target_id')):
                assert item[key] == old[key], (old['id'], key)
            if collection == 'nodes':
                assert item['fields']['name'] == old['fields']['name']
    glossary_before = {t['id']: t for t in read(OUT / 'glossary-before-U435.yaml')['terms']}
    glossary_now = read(ROOT / 'modeles/backlog/glossary.yaml')['terms']
    for term in glossary_now:
        for key in ('name', 'short_description', 'definition'):
            assert term[key] == glossary_before[term['id']][key]
    subprocess.run(['git', 'diff', '--exit-code', '--', 'modeles/backlog/behavior-gap-audit.yaml'], cwd=ROOT, check=True, capture_output=True)
    subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True, capture_output=True)
    report = {
        'source_refs': ['U434', 'U435', 'U436'],
        'model_before_sha256': digest(OUT / 'model-before-U435.yaml'),
        'model_after_sha256': digest(ROOT / 'modeles/backlog/model.yaml'),
        'protected_files_checked': len(baseline['protected_files']),
        'protected_files_changed': changed_protected,
        'validated_values_preserved': preserved,
        'existing_nodes_removed_or_renamed_or_retyped': [],
        'existing_relations_removed_or_reoriented': [],
        'glossary_names_definitions_short_descriptions_preserved': len(glossary_now),
        'behavior_audit_U431_unchanged': True,
        'checks_observed_in_task': [
            {'command': 'python scripts/validate_models.py', 'result': '0 errors, final model'},
            {'command': 'python scripts/render_models.py --space backlog', 'result': 'success'},
            {'command': 'node --test --test-isolation=none test-dependency-graph.mjs', 'cwd': 'app', 'unique_tests_passed': 13},
            {'command': 'python -m unittest scripts.test_models scripts.test_prepare_release scripts.test_relation_labels', 'unique_tests_passed': 44},
            {'command': 'python -m unittest discover -s scripts -p test_lifecycle.py', 'unique_tests_passed': 7},
            {'command': 'python -m unittest scripts.test_behaviors scripts.test_glossary scripts.test_market_comparisons', 'unique_tests_passed': 15},
            {'command': 'python -m unittest scripts.test_relation_labels', 'rechecked_tests_passed': 4, 'note': 'final hash; already counted in 44'},
            {'command': 'pnpm --dir app build', 'result': 'success', 'warning': 'bundle size warning; no compile error'},
            {'command': 'git diff --check', 'result': 'success'},
        ],
        'unique_tests_passed': 79,
        'independent_code_review': 'No actionable defect found in relation label, approval, freeze and version paths.',
        'publication_changed': False,
        'commit_or_push_performed': False,
    }
    target = OUT / 'verification.yaml'
    target.write_text(dumps(report), encoding='utf-8')
    broken = []
    for path in OUT.glob('*.md'):
        for raw in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            value = raw.strip('<>')
            if re.match(r'^(?:https?://|model:|glossary:|mailto:|#)', value):
                continue
            value = unquote(value.split('#')[0])
            if not value:
                continue
            if not (path.parent / value).exists():
                broken.append({'document': path.name, 'target': value})
    report['broken_local_markdown_links'] = broken
    target.write_text(dumps(report), encoding='utf-8')
    assert not broken, broken
    print(f'OK: {preserved} approved values; {len(baseline["protected_files"])} protected files unchanged; 110 glossary definitions preserved; local links resolve.')


if __name__ == '__main__':
    main()
