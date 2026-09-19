"""Repeat the original workloads with cold parse caches; retain baseline files."""
from pathlib import Path
import importlib.util
import json
import statistics
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'app'))


def main():
    spec = importlib.util.spec_from_file_location('perf_measure', HERE/'measure.py')
    measure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(measure)
    measure.OUT = HERE/'after'
    measure.OUT.mkdir(exist_ok=True)
    from scripts import structured_io as sio
    original_task = measure.run_task
    def cold_task(name, fn):
        sio.clear_read_cache()
        original_task(name, fn)
    measure.run_task = cold_task
    measure.main()
    # Restore instrumentation before independent runtime measurements.
    sio.read, sio.loads = measure.original_read, measure.original_loads
    from scripts import release_catalog, prepare_release
    import atlas_data
    samples = {}
    for name, callback in [('catalog', lambda: release_catalog.catalog(ROOT/'modeles/release')),
                           ('get_revision', lambda: atlas_data.get_revision(ROOT, 'release')),
                           ('load_model', lambda: atlas_data.load_model(ROOT, 'release'))]:
        sio.clear_read_cache()
        start = time.perf_counter(); callback(); cold = time.perf_counter()-start
        warm = []
        for _ in range(3):
            start = time.perf_counter(); callback(); warm.append(time.perf_counter()-start)
        samples[name] = {'cold_seconds': cold, 'warm_seconds': warm,
                         'median_seconds': statistics.median(warm)}
    report = prepare_release.build_candidate()['report']
    summary = prepare_release.summarize_report(report)
    result = {'atlas_functions': samples, 'validation_error_count': len(report['validation_errors']),
              'compact_report_bytes': len(json.dumps(summary, ensure_ascii=False, indent=2).encode('utf-8')),
              'full_report_bytes': len(json.dumps(report, ensure_ascii=False, indent=2).encode('utf-8'))}
    (measure.OUT/'runtime.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
