"""Isolated proof-of-concept: reject YAML aliases during its only parse.

This does not change production code. Run after measure.py, not concurrently.
"""
from pathlib import Path
import importlib.util
import json
import sys
import time
from copy import deepcopy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts import structured_io as sio

OUT = Path(__file__).resolve().parent
baseline_loads = sio.loads


class SinglePassLoader(sio.ModelLoader):
    def compose_node(self, parent, index):
        if self.check_event(sio.yaml.AliasEvent):
            raise ValueError('YAML aliases are not supported in models')
        return super().compose_node(parent, index)


def single_pass(text, suffix='.yaml'):
    if suffix.lower() not in ('.yaml', '.yml'):
        return baseline_loads(text, suffix)
    try:
        value = sio.yaml.load(text, Loader=SinglePassLoader)
        sio.check_values(value)
        return value
    except sio.yaml.YAMLError as exc:
        raise ValueError('Invalid model YAML: '+str(exc)) from exc


def outcome(loader, text):
    try:
        return ('ok', loader(text))
    except Exception as exc:
        return ('error', type(exc).__name__)


def main():
    cases = ['a: 1\na: 2', 'a: &x [1, 2]\nb: *x', 'a: &x [*x]',
             '1: invalid-key', '? [a,b]\n: value', 'a: yes\nb: no\nc: on\nd: off',
             'a: 2026-09-19\nb: 01\nc: 0x12\nd: true\ne: false\nf: null',
             'a: 1.5\nb: 3e2\nc: -4\nd: .inf\ne: .nan', 'a: !!float .inf',
             'a: !!python/object:foo {}', 'a: &x [1, 2]', 'a: [1, 2',
             'a: 1\n---\na: 2', 'a: {b: 1, b: 2}', 'true: 1', 'a: !!timestamp 2026-09-19',
             'a: null\nb: ~\nc: ""\nd: |\n  texte\n', 'a: !!binary YQ==']
    results=[]
    for text in cases:
        old, new = outcome(baseline_loads,text), outcome(single_pass,text)
        assert old == new, (text, old, new)
        results.append({'input':text,'outcome':old[0]})
    samples=[]
    for name in ['modeles/backlog/model.yaml','modeles/backlog/behavior-gap-audit.yaml','modeles/backlog/glossary.yaml']:
        text=(ROOT/name).read_text(encoding='utf-8-sig')
        start=time.perf_counter(); old=baseline_loads(text); baseline=time.perf_counter()-start
        start=time.perf_counter(); new=single_pass(text); trial=time.perf_counter()-start
        assert old == new
        samples.append({'path':name,'baseline_seconds':baseline,'single_pass_seconds':trial,'same_value':True})
    (OUT/'parser-experiment.json').write_text(json.dumps({'edge_cases':results,'samples':samples,'production_modified':False},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(samples),flush=True)
    spec=importlib.util.spec_from_file_location('perf_measure',OUT/'measure.py')
    measure=importlib.util.module_from_spec(spec);spec.loader.exec_module(measure)
    measure.OUT=OUT/'singlepass';measure.OUT.mkdir(exist_ok=True)
    measure.original_loads=single_pass
    sys.argv=[sys.argv[0],'validate','render','report']
    measure.main()


if __name__=='__main__':
    main()
