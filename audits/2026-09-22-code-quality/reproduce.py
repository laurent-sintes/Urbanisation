"""Read-only audit probes: mutations are restricted to disposable test fixtures."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.test_decision_registry import ShardedRegistryTests
from scripts.structured_io import dumps, read
from scripts import decision_registry, record_decision

results = {}
case = ShardedRegistryTests()
case.setUp()
try:
    index = case.split()
    frozen = case.root/'modeles/revisions/2026-09-22.1/deferred/decision-intents.yaml'
    frozen.parent.mkdir(parents=True)
    frozen.write_text(dumps(case.document()), encoding='utf-8')
    index['entries'] = []
    case.path.write_text(dumps(index), encoding='utf-8')
    before = case.check_project()[0]
    frozen.unlink()
    after, counts = case.check_project()
    results['missing_frozen_registry'] = {'before': before, 'after_removing_frozen_file': after, 'counts': counts}
finally:
    case.doCleanups()

case = ShardedRegistryTests()
case.setUp()
try:
    index = case.split()
    # Desynchronise the index's summary without touching the immutable capture.
    index['entries'][0]['target']['approved_fields'].append('scope')
    case.path.write_text(dumps(index), encoding='utf-8')
    result = case.record(intent_id='AUDIT-REPLACEMENT', fields=['scope'], supersedes=case.params['intent_id'])
    errors, _ = case.check_project()
    results['replacement_using_unverified_summary'] = {'recorded': result['recorded'], 'validation_errors': errors}
finally:
    case.doCleanups()

print(json.dumps(results, ensure_ascii=False, indent=2))
