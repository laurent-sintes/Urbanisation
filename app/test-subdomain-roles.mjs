import test from 'node:test';
import assert from 'node:assert/strict';
import { roleOf } from './src/subdomainRoles.ts';
const node = (id, role, kind = 'area') => ({ id, kind, fields: { dominant_role: role } });
const role = { id: 'data-state', display_name: 'Données et état' };
test('legacy publications have no inferred roles', () => {
  assert.equal(roleOf(node('Master Data')), undefined);
  assert.equal(roleOf(node('cap', role, 'capability')), undefined);
  assert.equal(roleOf(node('bad', { id: 'data-state' })), undefined);
});
