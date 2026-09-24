import tempfile
from pathlib import Path
import unittest
from scripts.structured_io import dumps
from scripts.backlog_delivery import check_delivery


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root / 'modeles/backlog'
        self.folder.mkdir(parents=True)
        self.model = {'nodes': [{'id': 'packing', 'fields': {'name': 'Packing Order'}}],
                      'relations': [{'type': 'contains', 'source_id': 'services', 'target_id': 'packing'}]}

    def declare(self, state='applied'):
        (self.folder / 'study.yaml').write_text(dumps({'publication_delivery': {
            'state': state, 'summary': 'Packing replaces VAS',
            'required_nodes': [{'id': 'packing', 'fields': {'name': 'Packing Order'}, 'parent': 'services'}],
            'absent_nodes': ['vas']}}), encoding='utf-8')

    def test_complete_delivery(self):
        self.declare()
        rows, errors = check_delivery(self.root, self.model)
        self.assertFalse(errors)
        self.assertEqual(rows[0]['state'], 'applied')

    def test_missing_or_retired_node_blocks(self):
        self.declare()
        self.model['nodes'] = [{'id': 'vas', 'fields': {}}]
        self.assertEqual(len(check_delivery(self.root, self.model)[1]), 2)

    def test_wrong_name_or_parent_blocks(self):
        self.declare()
        self.model['nodes'][0]['fields']['name'] = 'Old'
        self.model['relations'] = []
        self.assertEqual(len(check_delivery(self.root, self.model)[1]), 2)

    def test_pending_is_visible_without_approval(self):
        self.declare('pending')
        self.model['nodes'] = []
        rows, errors = check_delivery(self.root, self.model)
        self.assertEqual(rows[0]['state'], 'pending')
        self.assertFalse(errors)

    def test_empty_applied_declaration_blocks(self):
        (self.folder / 'study.yaml').write_text(dumps({'publication_delivery': {'state': 'applied'}}), encoding='utf-8')
        self.assertTrue(check_delivery(self.root, self.model)[1])
