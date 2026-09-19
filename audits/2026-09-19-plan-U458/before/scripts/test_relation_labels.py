"""Business relation labels remain typed, versioned and frozen with their evidence."""
from copy import deepcopy
from pathlib import Path
import unittest

from scripts.json_contract import validate
from scripts.lifecycle import validate_lifecycle, value_hash
from scripts.prepare_release import revision_errors
from scripts.publish_release import compile_snapshot
from scripts.structured_io import read
from scripts.validate_models import validate_release


ROOT = Path(__file__).resolve().parents[1]


class RelationLabelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = read(ROOT / 'modeles/schemas/urbanism.schema.json')
        cls.backlog = read(ROOT / 'modeles/backlog/model.yaml')

    def test_optional_labels_are_strings_in_a_closed_fields_object(self):
        for fields in ({'label': 'Consomme le résultat'}, {'verb': 'Fournit les faits'}, {}):
            model = deepcopy(self.backlog)
            model['relations'][0]['fields'] = fields
            self.assertEqual(validate(model, self.schema), [])
        for fields in ({'label': ''}, {'verb': 3}, {'unknown': 'invented'}):
            model = deepcopy(self.backlog)
            model['relations'][0]['fields'] = fields
            self.assertTrue(validate(model, self.schema))

    def test_label_does_not_hide_endpoint_approval_or_grant_label_approval(self):
        relation = {'id': 'R', 'source_id': 'A', 'target_id': 'B',
                    'fields': {'label': 'Consomme le résultat'},
                    'lifecycle': {'state': 'urbanist_validated', 'recorded_at': '2026-09-19T00:00:00Z',
                                  'validated_fields': ['source_id'], 'value_sha256': {'source_id': value_hash('A')}}}
        self.assertEqual(validate_lifecycle(relation), [])
        relation['fields']['label'] = 'Autre libellé éditorial'
        self.assertEqual(validate_lifecycle(relation), [])
        relation['source_id'] = 'Forged'
        self.assertTrue(any('approved value changed' in error for error in validate_lifecycle(relation)))

    def test_label_change_requires_a_new_relation_revision(self):
        before = {'nodes': [], 'relations': [{'id': 'R', 'revision': 1, 'type': 'relates-to',
                                             'source_id': 'A', 'target_id': 'B'}]}
        after = deepcopy(before)
        after['relations'][0]['fields'] = {'label': 'Consomme le résultat'}
        self.assertTrue(any('requires a new revision' in error for error in revision_errors(before, after)))
        after['relations'][0]['revision'] = 2
        self.assertEqual(revision_errors(before, after), [])

    def test_compiled_label_is_preserved_and_cannot_be_changed_after_freezing(self):
        snapshot = read(ROOT / 'modeles/revisions/2026-09-13.1/backlog.json')
        decisions = read(ROOT / 'modeles/decisions/2026-09-13.1.json')
        sources = {record['id']: record for record in read(ROOT / 'modeles/provenance/source-records.json')['records']}
        relation = next(item for item in snapshot['relations'] if item['review']['state'] != 'illustration')
        relation['fields'] = {'label': 'Expression métier proposée'}
        release = compile_snapshot(snapshot, decisions, '2026-09-19.99', ['U131'])
        published = next(item for item in release['relations'] if item['id'] == relation['id'])
        self.assertEqual(published['fields'], relation['fields'])
        self.assertEqual(validate_release(release, decisions, snapshot, sources, self.schema), [])
        published['fields']['label'] = 'Modification après gel'
        self.assertTrue(any('published fields differ from frozen input' in error
                            for error in validate_release(release, decisions, snapshot, sources, self.schema)))


if __name__ == '__main__':
    unittest.main()
