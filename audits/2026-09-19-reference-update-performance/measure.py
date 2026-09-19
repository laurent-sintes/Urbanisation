"""Measure real commands sequentially; never publish or edit business inputs."""
from pathlib import Path
from time import perf_counter
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('phase')
args = parser.parse_args()
out = Path(__file__).parent / (args.phase + '.json')
assert not out.exists(), out
commands = {
    'targeted_read': ['-c', "from scripts.structured_io import read; m=read('modeles/backlog/model.yaml'); print(next(n['fields']['name'] for n in m['nodes'] if n['id']=='D04.j'))"],
    'validation': ['scripts/validate_models.py'],
    'render_backlog': ['scripts/render_models.py', '--space', 'backlog'],
    'release_report': ['scripts/prepare_release.py', 'report'],
}
result = {}
for label, command in commands.items():
    start = perf_counter()
    proc = subprocess.run([sys.executable, '-X', 'utf8', *command], cwd=ROOT, capture_output=True)
    result[label] = dict(seconds=round(perf_counter()-start, 3), returncode=proc.returncode,
                         stdout_bytes=len(proc.stdout), stderr_bytes=len(proc.stderr))
    if proc.returncode:
        print(proc.stderr.decode('utf-8'), file=sys.stderr)
        raise SystemExit(proc.returncode)
    print(label, result[label], flush=True)
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
