"""Build static Atlas data from verified, explicitly indexed publications only."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.atlas_lock import atlas_lock
from scripts.export_publication import export
from scripts.release_catalog import catalog
from app.modeling_guide import load_modeling_guide


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False) + '\n').encode('utf-8')


def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() == content:
        return
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        temporary.write_bytes(content)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def export_atlas(root=ROOT, destinations=None):
    root = Path(root).resolve()
    with atlas_lock(root):
        return _export_atlas(root, destinations)


def _export_atlas(root, destinations):
    # Refuse the legacy directory-scanning fallback: the index is authoritative.
    index_path = root / 'modeles/release/index.json'
    before = index_path.read_bytes()
    result = catalog(index_path.parent)
    files = {}
    for entry in result['versions']:
        version = entry['version']
        if not isinstance(version, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}\.[1-9]\d*', version):
            raise ValueError('Invalid static publication version')
        model = export(root, version)['raw']
        guide = load_modeling_guide(root, version)
        for name, value in (('model', model), ('guide', guide)):
            payload = encoded(value)
            relative = f'{version}/{name}.json'
            files[relative] = payload
            entry[name + '_sha256'] = hashlib.sha256(payload).hexdigest()
    if index_path.read_bytes() != before:
        raise ValueError('Publication index changed during static export; retry.')
    destinations = destinations if destinations is not None else [root / 'app/public/data'] + (
        [root / 'app/dist/data'] if (root / 'app/dist/index.html').is_file() else [])
    # Build everything before touching the served catalog. Keep older files for
    # readers whose catalog request preceded a release.
    for destination in destinations:
        destination = Path(destination)
        for relative, payload in files.items():
            atomic_write(destination / relative, payload)
        if index_path.read_bytes() != before:
            raise ValueError('Publication index changed before static activation; retry.')
        atomic_write(destination / 'index.json', encoded(result))
    return {'current_version': result['current_version'], 'publications': len(result['versions']),
            'files': len(files) + 1, 'bytes': sum(map(len, files.values())),
            'destinations': [str(path) for path in destinations]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path, action='append')
    args = parser.parse_args()
    print(json.dumps(export_atlas(args.root, args.output), ensure_ascii=False))


if __name__ == '__main__':
    main()
