"""Associer l’édition préparée à v011, en préservant les associations antérieures."""
from pathlib import Path
from hashlib import sha256
import os
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.release_catalog import resolve_release
from app.modeling_guide import _validate_guide, load_modeling_guide

audit = Path(__file__).parent
folder = ROOT/'modeles/modeling-guides'
publication = '2026-09-19.4'
version = '2026-09-19.2'
candidate = audit/'guide-candidate.yaml'
content = candidate.read_bytes()
assert sha256(content).hexdigest() == '5c43053a82840a9f8a05105933f01263696f7cccf98862a1fda0422f5b7da18d'
_validate_guide(read(candidate), version)
assert resolve_release(ROOT/'modeles/release')['version'] == publication
before = read(audit/'before/modeles/modeling-guides/index.yaml')
index_path = folder/'index.yaml'; index = read(index_path)
assert index['guides'] == before['guides']
assert index['associations'][:-1] == before['associations']
association = index['associations'][-1]
assert association['publication_version'] == publication
assert association['scope'] == 'carried_frozen_methodology'
assert association['guide_version'] == '2026-09-19.1'

target = folder/'versions'/f'{version}.yaml'
with target.open('xb') as stream:
    stream.write(content); stream.flush(); os.fsync(stream.fileno())
index['guides'].append(dict(version=version, path=f'versions/{version}.yaml', sha256=sha256(content).hexdigest()))
association.update(guide_version=version, scope='explicit_methodology_U467',
    note='Édition publiée avec U467 : coopération sans couches, périmètre métier, Information et distinction proposition/engagement U466. Les rédactions proposées gardent leur portée ; les fiches pilotes ne deviennent pas des nœuds.')
temporary = folder/'.index-U467.tmp'
with temporary.open('x', encoding='utf-8', newline='\n') as stream:
    stream.write(dumps(index)); stream.flush(); os.fsync(stream.fileno())
os.replace(temporary, index_path)
result = load_modeling_guide(ROOT, publication)
assert result['status'] == 'available'
assert result['guide']['version'] == version
assert load_modeling_guide(ROOT, '2026-09-19.3')['guide']['version'] == '2026-09-19.1'
print(f'Guide {version} associé à {publication} : {len(result["guide"]["glossary"]["terms"])} termes ; ancien guide conservé pour v010.')
