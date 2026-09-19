"""Capture previous publications and index bytes before U452 publication."""
from pathlib import Path
from hashlib import sha256
import json
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
protected = {}
for folder in ('release', 'revisions', 'decisions', 'provenance', 'modeling-guides/versions'):
    for path in (ROOT / 'modeles' / folder).rglob('*'):
        if path.is_file() and path not in (ROOT / 'modeles/release/index.json', ROOT / 'modeles/provenance/source-records.json'):
            protected[path.relative_to(ROOT).as_posix()] = sha256(path.read_bytes()).hexdigest()
with (OUT / 'protected-before.json').open('x', encoding='utf-8') as stream:
    json.dump(protected, stream, ensure_ascii=False, indent=2)
for relative, name in [('modeles/release/index.json', 'release-index-before.json'), ('modeles/modeling-guides/index.yaml', 'guide-index-before.yaml')]:
    with (OUT / name).open('xb') as stream:
        stream.write((ROOT / relative).read_bytes())
print(f'{len(protected)} fichiers historiques protégés ; deux index capturés séparément.')
