"""Publish the U450 methodology repair; never modify a business snapshot."""
from pathlib import Path
from hashlib import sha256
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'app'))
from scripts.structured_io import read, dumps
from modeling_guide import _validate_guide, load_modeling_guide

audit = Path(__file__).parent
folder = ROOT / 'modeles/modeling-guides'
version = '2026-09-19.1'
publication = '2026-09-19.2'
candidate = audit / 'guide-candidate.yaml'
_validate_guide(read(candidate), version)
index_path = folder / 'index.yaml'
assert index_path.read_bytes() == (audit / 'guide-index-before.yaml').read_bytes()
index = read(index_path)
assert not any(item['publication_version'] == publication for item in index['associations'])
target = folder / 'versions' / (version + '.yaml')
content = candidate.read_bytes()
with target.open('xb') as stream:
    stream.write(content)
index['guides'].append({'version': version, 'path': 'versions/' + version + '.yaml', 'sha256': sha256(content).hexdigest()})
index['associations'].append({'publication_version': publication, 'guide_version': version,
    'scope': 'explicit_methodology_U450_U451',
    'note': 'Réparation U450 : guide et glossaire du méta modèle figés, associés explicitement à v009 ; grille des comportements U451. Aucun changement des octets ni des validations de la publication métier.'})
index_path.write_text(dumps(index), encoding='utf-8', newline='\n')
result = load_modeling_guide(ROOT, publication)
assert result['status'] == 'available'
print(f"Guide {version} : {len(result['guide']['lessons'])} repères, {len(result['guide']['glossary']['terms'])} termes méthodologiques ; publication {publication}.")
