"""Read-only workload measurements; generated writes are intercepted in memory.

Run from the repository root. No production module is modified. Timings are
single warm-filesystem samples, not statistically significant benchmarks.
"""
from pathlib import Path
import contextlib
import importlib
import io
import json
import sys
import time
from collections import defaultdict
from hashlib import sha256
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts import structured_io as sio

OUT = Path(__file__).resolve().parent
original_read = sio.read
original_loads = sio.loads
reads = defaultdict(lambda: {'calls': 0, 'seconds': 0.0, 'bytes': 0})
load_stats = defaultdict(lambda: {'calls': 0, 'seconds': 0.0})
writes = []


def timed_loads(text, suffix='.yaml'):
    start = time.perf_counter()
    try:
        return original_loads(text, suffix)
    finally:
        load_stats[suffix]['calls'] += 1
        load_stats[suffix]['seconds'] += time.perf_counter() - start


def timed_read(path):
    path = Path(path).resolve()
    start = time.perf_counter()
    try:
        return original_read(path)
    finally:
        key = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        reads[key]['calls'] += 1
        reads[key]['seconds'] += time.perf_counter() - start
        reads[key]['bytes'] = path.stat().st_size


def discard_text(path, text, *args, **kwargs):
    writes.append({'path': str(path), 'bytes': len(text.encode('utf-8'))})
    return len(text)


def run_task(name, fn):
    reads.clear(); load_stats.clear(); writes.clear()
    captured = io.StringIO()
    start = time.perf_counter()
    with patch.object(Path, 'write_text', discard_text), contextlib.redirect_stdout(captured):
        result = fn()
    elapsed = time.perf_counter()-start
    record = {'task': name, 'seconds': elapsed, 'structured_loads': dict(load_stats),
              'read_calls': sum(x['calls'] for x in reads.values()), 'unique_files': len(reads),
              'read_bytes_with_repeats': sum(x['calls']*x['bytes'] for x in reads.values()),
              'slowest_reads': sorted(({'path': p, **v} for p,v in reads.items()), key=lambda x:x['seconds'], reverse=True)[:12],
              'repeated_reads': [{'path': p, **v} for p,v in reads.items() if v['calls']>1],
              'suppressed_write_count': len(writes), 'suppressed_write_bytes': sum(w['bytes'] for w in writes),
              'stdout_bytes': len(captured.getvalue().encode('utf-8'))}
    if name == 'report':
        r = result['report']
        start = time.perf_counter()
        serialized = json.dumps(r, ensure_ascii=False, indent=2)
        record.update(report_json_bytes=len(serialized.encode('utf-8')), report_serialization_seconds=time.perf_counter()-start,
                      validation_error_count=len(r['validation_errors']), deferred_artifacts=len(r['deferred_artifacts']),
                      compact_summary_bytes=len(json.dumps({'version':r['candidate_version'],'validation_errors':len(r['validation_errors'])})))
    if name == 'validate':
        record['result'] = result
    (OUT / (name+'.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'task':name,'seconds':round(elapsed,3),'reads':record['read_calls'],
                      'load_seconds':round(sum(v['seconds'] for v in load_stats.values()),3)}, ensure_ascii=False), flush=True)


def main():
    tracked = [ROOT/'modeles/backlog/model.yaml', ROOT/'modeles/release/index.json', ROOT/'AGENTS.md', ROOT/'modeles/provenance/source-records.json']
    before = {str(p):sha256(p.read_bytes()).hexdigest() for p in tracked}
    sio.read = timed_read
    sio.loads = timed_loads
    from scripts import validate_models, render_models, prepare_release, render_behavior_gap_audit, refresh_sources
    # This callback bypasses the atomic source-index writer, retaining computation.
    def refresh():
        with patch.object(refresh_sources, 'activate_pointer', lambda path, data: writes.append({'path':str(path),'bytes':len(json.dumps(data,ensure_ascii=False).encode('utf-8'))})):
            return refresh_sources.main()
    tasks = {'refresh': refresh, 'validate': validate_models.validate_project,
             'render': render_models.main, 'report': prepare_release.build_candidate,
             'audit': render_behavior_gap_audit.main}
    for task in (sys.argv[1:] or tasks.keys()):
        run_task(task, tasks[task])
    after = {str(p):sha256(p.read_bytes()).hexdigest() for p in tracked}
    assert before == after, 'Observed input changed during measurement'
    (OUT/'inputs.json').write_text(json.dumps({'before':before,'after':after,'preserved':True,'python':sys.version,
         'yaml':sio.yaml.__version__,'libyaml':getattr(sio.yaml,'__with_libyaml__',False)},indent=2),encoding='utf-8')


if __name__ == '__main__':
    main()
