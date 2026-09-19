"""Shared validation for market comparisons on nodes and business glossary terms."""
from datetime import date
from functools import lru_cache
import json
from pathlib import Path

try:
    from .json_contract import validate
except ImportError:
    from json_contract import validate

@lru_cache(maxsize=1)
def contract():
    path = Path(__file__).resolve().parents[1] / 'modeles/schemas/urbanism.schema.json'
    return json.loads(path.read_text(encoding='utf-8'))['$defs']['marketComparisons']

def validate_comparisons(value, label):
    errors = [label + ': ' + error for error in validate(value, contract())]
    if errors:
        return errors
    for index, entry in enumerate(value):
        try:
            date.fromisoformat(entry['consulted_on'])
        except ValueError:
            errors.append(f'{label}/{index}: invalid consultation date')
    return errors
