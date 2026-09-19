"""Additional isolated measurements: hashes, per-run cache, Atlas read paths."""
from pathlib import Path
import importlib.util
import json
import statistics
import sys
import time
from copy import deepcopy
from hashlib import sha256

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT/'app'))


def import_file(name, path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def main():
    audit=json.loads((OUT/'audit.json').read_text())
    # Audit measurement contains all 45 inputs in the traced reads only for top
    # entries; explicitly take the immutable protected inventory for this test.
    protected=json.loads((ROOT/'audits/2026-09-17-refonte-appliquee/protected.json').read_text())
    start=time.perf_counter()
    for p,expected in protected.items():
        assert sha256((ROOT/p).read_bytes()).hexdigest()==expected
    hash_seconds=time.perf_counter()-start
    from scripts import release_catalog
    import atlas_data
    samples={}
    for name,callback in [('catalog',lambda:release_catalog.catalog(ROOT/'modeles/release')),
                          ('get_revision',lambda:atlas_data.get_revision(ROOT,'release')),
                          ('load_model',lambda:atlas_data.load_model(ROOT,'release'))]:
        times=[]
        for _ in range(3):
            start=time.perf_counter();callback();times.append(time.perf_counter()-start)
        samples[name]={'seconds':times,'median_seconds':statistics.median(times)}
        print(name,samples[name],flush=True)
    (OUT/'runtime.json').write_text(json.dumps({'atlas_functions':samples,'protected_hash_seconds':hash_seconds,'protected_files':len(protected),'method':'Current in-process backend code; no HTTP or browser/GPU measurement.'},indent=2),encoding='utf-8')
    # Cache only within one invocation; key is actual content, values are copied.
    exp=import_file('perf_experiments',OUT/'experiments.py')
    measure=import_file('perf_measure',OUT/'measure.py')
    cache={};hits=0
    def cached(text,suffix='.yaml'):
        nonlocal hits
        key=(suffix,text)
        if key not in cache: cache[key]=exp.single_pass(text,suffix)
        else: hits+=1
        return deepcopy(cache[key])
    original={'a':[1]}
    first=cached('a: [1]');first['a'].append(2)
    assert cached('a: [1]')==original
    assert cached('a: [2]')=={'a':[2]}
    cache.clear();hits=0
    measure.OUT=OUT/'singlepass-cache';measure.OUT.mkdir(exist_ok=True)
    measure.original_loads=cached
    sys.argv=[sys.argv[0],'report']
    measure.main()
    (OUT/'cache-experiment.json').write_text(json.dumps({'entries':len(cache),'hits':hits,'copy_isolation':True,'content_change_detected':True,'persistent_cache':False,'production_modified':False},indent=2),encoding='utf-8')


if __name__=='__main__':main()
