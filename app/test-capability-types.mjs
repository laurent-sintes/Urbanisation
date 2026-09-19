import test from 'node:test';
import assert from 'node:assert/strict';
import { capabilityNature, capabilityTypeLabel, capabilityTypes, decisionsLast, startsDecisionSection } from './src/capabilityTypes.ts';
import { adaptPublication, childrenOf } from './src/model.ts';

const node = (id, nature, kind = 'capability') => ({ id, name: id, kind, fields: { nature } });
test('explicit types drive labels and six distinct icons; never names or IDs', () => {
  assert.equal(new Set(Object.values(capabilityTypes).map(type => type.icon)).size, 6);
  assert.equal(capabilityTypeLabel(node('ATP', 'decision')), 'Décision');
  assert.equal(capabilityNature(node('Decision by name only', undefined)), undefined);
  assert.equal(capabilityNature(node('D05.e', 'unsupported')), undefined);
  assert.equal(capabilityNature(node('toString', 'toString')), undefined);
  assert.equal(capabilityNature(node('behavior', 'decision', 'behavior')), undefined);
});
test('stable decision partition does not change the snapshot or reorder other types', () => {
  const input = Object.freeze([node('d1', 'decision'), node('a', 'action'), node('p', 'planning'), node('d2', 'decision'), node('old', undefined)]);
  const output = decisionsLast(input);
  assert.deepEqual(output.map(n => n.id), ['a', 'p', 'old', 'd1', 'd2']);
  assert.deepEqual(input.map(n => n.id), ['d1', 'a', 'p', 'd2', 'old']);
  assert.deepEqual(output.map((_, i) => startsDecisionSection(output, i)), [false, false, false, true, false]);
  for (const homogeneous of [[], [node('d', 'decision')], [node('d1', 'decision'), node('d2', 'decision')], [node('a', 'action')]]) {
    assert.equal(homogeneous.some((_, i) => startsDecisionSection(homogeneous, i)), false);
  }
});
test('only domain and reference children are sorted, behaviors and raw edges stay intact', () => {
  const raw = { space: 'release', version: 'fixture', nodes: [
    { id: 'domain', kind: 'domain' },
    { id: 'a', kind: 'capability', fields: { name: 'Renamed decision', nature: 'action' } },
    { id: 'd', kind: 'capability', fields: { name: 'ATP', nature: 'decision' } },
    { id: 'b2', kind: 'behavior', fields: { name: 'Second', nature: 'decision' } },
    { id: 'b1', kind: 'behavior', fields: { name: 'First', nature: 'action' } },
  ], relations: [
    { id: '1', type: 'contains', source_id: 'domain', target_id: 'd' },
    { id: '2', type: 'contains', source_id: 'domain', target_id: 'a' },
    { id: '3', type: 'contains', source_id: 'a', target_id: 'b2' },
    { id: '4', type: 'contains', source_id: 'a', target_id: 'b1' },
  ] };
  const model = adaptPublication(raw);
  assert.deepEqual(childrenOf(model, 'domain').map(n => n.id), ['a', 'd']);
  assert.deepEqual(childrenOf(model, 'a').map(n => n.id), ['b2', 'b1']);
  assert.deepEqual(model.raw, raw);
});
