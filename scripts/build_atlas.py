"""Serialize the complete static build with local publication and export."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.atlas_lock import atlas_lock
from scripts.export_atlas import export_atlas


def main():
    pnpm = shutil.which('pnpm')
    if not pnpm:
        raise ValueError('pnpm is required to build Atlas')
    with atlas_lock(ROOT):
        # A failed type check must not update the data served by the old build.
        subprocess.run([pnpm, 'exec', 'tsc', '--noEmit'], cwd=ROOT / 'app', check=True)
        export_atlas(ROOT, [ROOT / 'app/public/data'])
        subprocess.run([pnpm, 'exec', 'vite', 'build'], cwd=ROOT / 'app', check=True)


if __name__ == '__main__':
    main()
