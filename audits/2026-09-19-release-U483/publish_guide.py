"""Associer le guide U482/U479 à v015 après la publication U483 du modèle.

Ce script ne publie pas le modèle. Il préserve chaque ancienne association et
chaque octet des éditions précédentes. Une reprise identique est sans effet.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, loads, dumps
from scripts.release_catalog import resolve_release
from scripts.prepare_release import context_source_references
from app.modeling_guide import _validate_guide, load_modeling_guide

PUBLICATION = '2026-09-19.8'
BASE_PUBLICATION = '2026-09-19.7'
GUIDE_VERSION = '2026-09-19.3'
EXPECTED_SHA256 = '278fb78a61ee4030ce6b566cc2579ae69e9856b0a3c0a7150f727b28e0a9d520'
AUDIT = Path(__file__).resolve().parent
FOLDER = ROOT / 'modeles/modeling-guides'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_protected(proof):
    for relative, expected in proof['protected_guides'].items():
        path = FOLDER / relative
        require(path.resolve() == path, 'Chemin de guide historique non conforme')
        require(sha256(path.read_bytes()).hexdigest() == expected,
                f'Guide historique modifié : {relative}')


def main():
    proof = read(AUDIT / 'guide-candidate-proof.yaml')
    content = (AUDIT / 'guide-candidate.yaml').read_bytes()
    require(sha256(content).hexdigest() == EXPECTED_SHA256 == proof['candidate_sha256'],
            'Empreinte du candidat de guide incorrecte')
    require(proof['publication_version'] == PUBLICATION and proof['guide_version'] == GUIDE_VERSION,
            'Versions différentes de la préparation U483')
    guide = loads(content.decode('utf-8'), '.yaml')
    _validate_guide(guide, GUIDE_VERSION)
    references = context_source_references(guide)
    known_sources = {item['id'] for item in read(ROOT / 'modeles/provenance/source-records.json')['records']}
    require(references <= known_sources, 'Source racine du guide absente du registre')
    require({'U479', 'U482', 'U483'} <= references, 'Portée U479/U482/U483 manquante')
    require(resolve_release(ROOT / 'modeles/release')['version'] == PUBLICATION,
            'Publier et activer le modèle 2026-09-19.8 avant son guide')

    before = proof['before_index']
    require(all(item['version'] != GUIDE_VERSION for item in before['guides']),
            'Version du guide déjà présente dans l’état antérieur')
    require(all(item['publication_version'] != PUBLICATION for item in before['associations']),
            'Publication déjà associée dans l’état antérieur')
    base = [item for item in before['associations'] if item['publication_version'] == BASE_PUBLICATION]
    require(len(base) == 1 and base[0]['guide_version'] == '2026-09-19.2',
            'Association de base inattendue')
    verify_protected(proof)

    carried = deepcopy(base[0])
    carried.update(publication_version=PUBLICATION, scope='carried_frozen_methodology',
                   note=f'Édition méthodologique figée reprise explicitement depuis {BASE_PUBLICATION} ; aucune lecture du backlog.')
    expected_carried = deepcopy(before)
    expected_carried['associations'].append(carried)
    final = deepcopy(expected_carried)
    final['guides'].append(dict(version=GUIDE_VERSION, path=f'versions/{GUIDE_VERSION}.yaml', sha256=EXPECTED_SHA256))
    final['associations'][-1].update(guide_version=GUIDE_VERSION, scope='explicit_methodology_U483',
        note='Édition publiée avec U483 : Domain → Area → Capability → Behavior et Authoritative Data adoptés U482 ; autorité locale des références U479. Les formulations pédagogiques proposées gardent leur portée ; aucune validation globale ni fusion des référentiels.')

    index_path = FOLDER / 'index.yaml'
    index_bytes = index_path.read_bytes()
    current = loads(index_bytes.decode('utf-8-sig'), '.yaml')
    require(current in (expected_carried, final),
            'L’index a changé hors du report attendu ; aucune association modifiée')
    target = FOLDER / 'versions' / f'{GUIDE_VERSION}.yaml'
    if target.exists():
        require(target.read_bytes() == content, 'Une édition différente occupe la version cible')
    else:
        require(current == expected_carried, 'L’index final pointe vers une édition absente')
        with target.open('xb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())

    if current != final:
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='\n',
                                             dir=FOLDER, suffix='.tmp', delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(dumps(final))
                stream.flush()
                os.fsync(stream.fileno())
            require(index_path.read_bytes() == index_bytes, 'Index modifié pendant la publication du guide')
            os.replace(temporary, index_path)
        finally:
            if temporary is not None and temporary.exists():
                temporary.unlink()

    verify_protected(proof)
    require(read(index_path) == final, 'Index final inattendu')
    result = load_modeling_guide(ROOT, PUBLICATION)
    require(result['status'] == 'available' and result['guide']['version'] == GUIDE_VERSION,
            'Le nouveau guide n’est pas disponible')
    old = load_modeling_guide(ROOT, BASE_PUBLICATION)
    require(old['status'] == 'available' and old['guide']['version'] == '2026-09-19.2',
            'Association historique de v014 altérée')
    names = {term['id']: term['name'] for term in result['guide']['glossary']['terms']}
    require(names['MOD008'] == 'Domain' and names['MOD013'] == 'Area', 'Niveaux méthodologiques incorrects')
    print(json.dumps(dict(publication=PUBLICATION, guide=GUIDE_VERSION, sha256=EXPECTED_SHA256,
                          terms=len(names), protected_guides=len(proof['protected_guides']),
                          historical_associations_preserved=len(before['associations']),
                          already_published=current == final), ensure_ascii=False))


if __name__ == '__main__':
    main()
