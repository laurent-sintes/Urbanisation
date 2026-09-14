import test from 'node:test';
import assert from 'node:assert/strict';
import { readRoute, routeHash } from './src/navigation.ts';

test('a shared link preserves its fixed publication, selection, source and literal characters', () => {
  const route = {
    ...readRoute(''), node: 'OBJ/été&1', scope: '@root', version: '2026-09-13.5', view: 'relations',
    query: 'ordre & événement', type: 'object', status: 'partial', relation: 'REL-1',
    source: 'connaissance/fichier avec espaces.md', anchor: 'référence-1', sourceId: 'U153',
  };
  assert.deepEqual(readRoute(routeHash(route)), route);
});
test('old space links use the published model and preserve actual node identities', () => {
  const route = readRoute('#space=backlog&node=D02.b&view=links');
  assert.equal(route.node, 'D02.b');
  assert.equal(route.view, 'relations');
  assert.equal(route.version, '');
  assert.ok(!routeHash(route).includes('space='));
  for (const id of ['atlas', 'transactional', 'process']) assert.equal(readRoute(`#node=${id}`).node, '');
});
test('a direct capability URL leaves view selection to its published structure', () => {
  assert.equal(readRoute('#node=D04.e').view, undefined);
  assert.equal(readRoute('#node=D04.e&view=unknown').view, undefined);
  assert.equal(routeHash(readRoute('')), '/');
});
