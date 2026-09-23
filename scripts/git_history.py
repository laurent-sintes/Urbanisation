"""Read retired artifacts from exact Git commits; never restore a shadow tree."""
import json
from pathlib import Path
import re
import subprocess
from functools import lru_cache

INDEX = 'modeles/git-history.json'


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True)
    if result.returncode:
        raise ValueError('Git history unavailable: ' + result.stderr.decode('utf-8', 'replace').strip())
    return result.stdout


@lru_cache(maxsize=8)
def blob(root, commit, relative):
    if not re.fullmatch(r'[a-f0-9]{40,64}', commit):
        raise ValueError('History requires an exact Git commit')
    if relative.startswith('/') or any(p in ('', '.', '..') for p in relative.split('/')) or any(c in relative for c in ('\\', ':', '\0')):
        raise ValueError('Invalid Git artifact path')
    return git(root, 'show', commit + ':' + relative)


def read_bytes(path):
    path = Path(path).resolve()
    if path.is_file():
        return path.read_bytes()
    for root in path.parents:
        index = root / INDEX
        if index.is_file():
            relative = path.relative_to(root).as_posix()
            records = json.loads(index.read_text(encoding='utf-8'))['archives']
            matches = [r for r in records if relative == r['path'] or relative.startswith(r['path'].rstrip('/') + '/')]
            if not matches:
                break
            record = max(matches, key=lambda r: len(r['path']))
            return blob(str(root), record['commit'], relative)
    raise FileNotFoundError(path)


def enabled(root):
    return (Path(root) / INDEX).is_file()
