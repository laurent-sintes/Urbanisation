import test from 'node:test';
import assert from 'node:assert/strict';
import { roleOf, roleOptions, matchesRole } from './src/subdomainRoles.ts';
const node = (id, role, kind = 'area') => ({ id, kind, fields: { dominant_role: role } });
const role = { id: 'data-state', display_name: 'Données et état' };
test('legacy publications have no inferred roles', () => {
  assert.equal(roleOf(node('Master Data')), undefined);
  assert.equal(roleOf(node('cap', role, 'capability')), undefined);
  assert.equal(roleOf(node('bad', { id: 'data-state' })), undefined);
});
test('roles filter the view without changing its nodes or hierarchy', () => {
  const nodes = [node('data', role), node('other', { id: 'policies', display_name: 'Politiques' }), node('legacy')];
  assert.equal(roleOptions(nodes).length, 2);
  assert.deepEqual(nodes.filter(n => matchesRole(n, 'data-state')).map(n => n.id), ['data']);
  assert.equal(nodes.filter(n => matchesRole(n, '')).length, 3);
  assert.equal(nodes.length, 3);
});
