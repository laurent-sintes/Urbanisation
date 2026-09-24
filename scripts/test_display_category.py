"""Keep display metadata optional and reject incomplete category captions."""
from pathlib import Path
import unittest
from scripts.structured_io import read
from scripts.json_contract import validate


class DisplayCategoryTests(unittest.TestCase):
    def test_category_contract(self):
        schema = read(Path(__file__).resolve().parents[1] / 'modeles/schemas/urbanism.schema.json')
        fields = schema['$defs']['node']['properties']['fields']
        self.assertNotIn('category', fields.get('required', []))
        category = fields['properties']['category']
        self.assertFalse(validate({'id': 'transport', 'display_name': 'Transport', 'order': 20}, category))
        for invalid in ({'id': 'transport'}, {'id': 'transport', 'display_name': '  '},
                        {'id': 'transport', 'display_name': 'Transport', 'order': '20'},
                        {'id': 'transport', 'display_name': 'Transport', 'parent_id': 'sd'}):
            with self.subTest(invalid=invalid):
                self.assertTrue(validate(invalid, category))


if __name__ == '__main__':
    unittest.main()
