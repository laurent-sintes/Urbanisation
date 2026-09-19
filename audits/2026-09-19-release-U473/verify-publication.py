"""Contrôler la publication servie et les octets des historiques antérieurs."""
from pathlib import Path
from hashlib import sha256
from urllib.request import urlopen
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read

folder = Path(__file__).resolve().parent
version = '2026-09-19.6'


def api(path):
    with urlopen('http://127.0.0.1:8765'+path, timeout=10) as response:
        return json.load(response)


status = api('/api/status')
assert status['appName'] == 'FLOW Atlas' and status['space'] == 'release'
assert Path(status['repositoryRoot']).resolve() == ROOT.resolve()
index = read(ROOT/'modeles/release/index.json')
descriptor = read(ROOT/'modeles/release'/index['current'])
assert descriptor['version'] == version and descriptor['revision'] == 13
frozen = read(ROOT/'modeles/release'/descriptor['path'])
model = api('/api/model')
assert model['version'] == version
assert model['sourcePath'] == 'modeles/release/'+descriptor['path']
for key, value in frozen.items():
    assert model[key] == value, key
assert api('/api/releases')['current_version'] == version
guide = api('/api/modeling-guide?version='+version)
assert guide['status'] == 'available' and guide['guide']['version'] == '2026-09-19.2'
old = api('/api/model?version=2026-09-19.5')
assert old['version'] == '2026-09-19.5'
assert any(node['id'] == 'universe-case' for node in old['nodes'])
assert not any(node['id'] == 'universe-case' for node in model['nodes'])
assert any(term['id'] == 'TER067' for term in old['glossary']['terms'])
assert not any(term['id'] == 'TER067' for term in model['glossary']['terms'])
assert model['information_catalog'] == old['information_catalog']
assert len(model['nodes']) == 137 and len(model['relations']) == 338
assert len(model['glossary']['terms']) == 110
assert sum(node['kind'] == 'capability' for node in model['nodes']) == 47
assert sum(node['kind'] == 'behavior' for node in model['nodes']) == 76
market_counts = {}
for item in [*model['nodes'], *model['glossary']['terms']]:
    entries = item.get('fields', item).get('market_comparisons', [])
    if entries:
        urls = {entry['source_url'].split('#')[0].rstrip('/') for entry in entries}
        assert len(urls) >= 2, (item['id'], urls)
        market_counts[item['id']] = len(urls)
protected = read(folder/'protected-files.json')
changed = [path for path, digest in protected.items()
           if sha256((ROOT/path).read_bytes()).hexdigest() != digest]
assert not changed, changed
old_index = read(folder/'before/modeles/release/index.json')
assert all(publication in index['publications'] for publication in old_index['publications'])
old_guide = read(folder/'before/modeles/modeling-guides/index.yaml')
new_guide = read(ROOT/'modeles/modeling-guides/index.yaml')
assert old_guide['guides'] == new_guide['guides']
assert all(association in new_guide['associations'] for association in old_guide['associations'])
for name in ('model', 'glossary'):
    path = f'modeles/backlog/{name}.yaml'
    assert (folder/'before'/path).read_bytes() == (ROOT/path).read_bytes()
result = dict(status='passed', version=version, revision=descriptor['revision'],
    published_at=descriptor['published_at'], descriptor=index['current'], sourcePath=model['sourcePath'],
    model_equals_frozen_snapshot=True, nodes=len(model['nodes']), relations=len(model['relations']),
    capabilities=47, behaviors=76, glossary_terms=110, market_fiches_with_two_or_more_sources=len(market_counts),
    unchanged_information=len(model['information_catalog']['items']),
    unchanged_information_links=len(model['information_catalog']['links']), guide=guide['guide']['version'],
    historical_files_unchanged=len(protected), backlog_model_and_glossary_unchanged=True, server_pid=status['pid'])
(folder/'api-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=True))
