"""Read a verified publication from disk and serialize it to JSON on stdout."""
import argparse
import json
from pathlib import Path
try:
    from .release_catalog import resolve_release, within
    from .structured_io import read
except ImportError:
    from release_catalog import resolve_release, within
    from structured_io import read


def export(root, version=None):
    root = Path(root).resolve()
    folder = root / 'modeles/release'
    descriptor = resolve_release(folder, version)
    source = within(folder, descriptor['path'])
    raw = read(source)
    source_path = source.relative_to(root).as_posix()
    return {'raw': {**raw, 'sourcePath': source_path}, 'descriptor': descriptor,
            'sourcePath': source_path,
            'descriptorPath': 'modeles/release/' + descriptor['descriptor'] if descriptor.get('descriptor') else None}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--version')
    args = parser.parse_args()
    print(json.dumps(export(args.root, args.version), ensure_ascii=True, allow_nan=False))
