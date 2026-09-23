"""Measure a real editorial publication on disposable Git repositories."""
import json
from pathlib import Path
import platform
import shutil
import sys
from time import perf_counter
from unittest.mock import patch

from . import release, git_history, parsed_cache, structured_io
from .test_publish_release import isolated_project


def benchmark(root):
    root = Path(root).resolve()
    rows = []
    with isolated_project() as scratch:
        cache = scratch / 'cache'
        for mode in ('cold', 'warm'):
            with isolated_project() as sandbox:
                shutil.copytree(root / 'modeles', sandbox / 'modeles',
                                ignore=shutil.ignore_patterns('staging', '.decision-intents.lock'))
                (sandbox / '.gitattributes').write_text('* -text\n', encoding='utf-8')
                git_history.git(sandbox, 'init', '-q')
                git_history.git(sandbox, 'add', 'modeles')
                git_history.git(sandbox, '-c', 'user.name=Benchmark', '-c', 'user.email=benchmark@example.invalid',
                                'commit', '-qm', 'Isolated baseline')
                source = sandbox / 'modeles/backlog/model.yaml'
                model = structured_io.read(source)
                model['nodes'][0]['review']['note'] += ' Isolated performance fixture; no business change.'
                source.write_text(structured_io.dumps(model), encoding='utf-8')
                structured_io.clear_read_cache()
                with patch.object(parsed_cache, 'DIRECTORY', cache):
                    start = perf_counter()
                    result = release.run(sandbox, '2099-09-23.1', ['U627'], activate=True, verify_site=False)
                    seconds = perf_counter() - start
                row = {'mode': mode, 'seconds': round(seconds, 3), 'status': result['status'],
                       'validation_errors': result.get('checks', {}).get('validation_errors')}
                rows.append(row)
                print(json.dumps(row), flush=True)
                if result['status'] != 'published':
                    raise ValueError(str(result))
    return {'python': sys.version, 'platform': platform.platform(),
            'scenario': 'One editorial change, isolated full publication; empty then populated parser cache; HTTP excluded',
            'runs': rows}


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    result = benchmark(root)
    target = root / '.runtime/lean-release-performance.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
