import test from 'node:test';
import assert from 'node:assert/strict';
import { adaptPublication } from './src/model.ts';
import { searchPublication } from './src/search.ts';
import { businessFields, businessQualification } from './src/businessContent.ts';
import { marketText, marketSearchText } from './src/marketContent.ts';

const raw = () => ({ space: 'release', version: 'reader-fixture', nodes: [
  { id: 'OTHER', kind: 'capability', fields: { name: 'Sales Order', definition: 'Mobiliser Purchase Order selon le besoin.', market_comparisons: [{ vendor: 'VendorExemple', status: 'proposé', similarities: 'appuipublic', source_refs: ['motsecret'] }] } },
  { id: 'PO', kind: 'capability', fields: { name: 'Purchase Order', definition: 'Prendre en charge les achats.', scope: 'Préserver les engagements.' } },
], relations: [], glossary: { terms: [{ id: 'DOC', name: 'Bon de commande', definition: 'Document exprimant une demande d’achat.', short_description: 'Une expression de la commande.', notes: 'noteinterne', source_refs: [], review: { state: 'proposed' } }] } });

test('exact names and IDs precede prose matches; editorial fields are not searchable', () => {
  const model = adaptPublication(raw());
  assert.equal(searchPublication(model, 'purchase order')[0].id, 'PO');
  assert.equal(searchPublication(model, 'po')[0].id, 'PO');
  for (const query of ['motsecret', 'proposé', 'noteinterne', 'réserver']) assert.deepEqual(searchPublication(model, query), [], query);
  assert.equal(searchPublication(model, 'VendorExemple appuipublic')[0].id, 'OTHER');
});
test('market position retains its meaning without exposing adoption metadata or inferring innovation', () => {
  const text = 'U438 : Frontière adoptée U395. Achat et stocks restent distincts. Comparaison proposée au titre de U435, sans validation ni réalisation installée déduites.';
  assert.equal(marketText(text), 'Achat et stocks restent distincts.');
  assert.equal(marketText('Recouvrement partiel'), 'Recouvrement partiel');
  assert.equal(marketSearchText(), '');
  assert.equal(marketText('Sous réserve de disponibilité. Une date proposée reste une proposition.'), 'Sous réserve de disponibilité. Une date proposée reste une proposition.');
});
test('published glossary terms have their own search result, without a fabricated capability alias', () => {
  const model = adaptPublication(raw());
  const result = searchPublication(model, 'bon de commande');
  assert.equal(result[0].id, 'DOC');
  assert.equal(result[0].kind, 'glossary');
  assert.equal(result.some(item => item.id === 'PO'), false);
  assert.match(result[0].excerpt, /commande/);
});
test('reader fields and relation qualifications reject unknown metadata without mutating the input', () => {
  const fields = { definition: 'Métier', market_comparisons: [{ product: 'Logiciel' }], review: 'privé', new_internal_field: 'secret' };
  assert.deepEqual(businessFields(fields), { definition: 'Métier' });
  assert.deepEqual(businessQualification({ meaning: 'Raison', conditions: ['Condition'], source_refs: ['U1'], review: 'secret' }), { meaning: 'Raison', conditions: ['Condition'] });
  assert.equal(fields.new_internal_field, 'secret');
});
test('a definition starting with the searched phrase precedes scattered word matches', () => {
  const input = raw();
  input.nodes[0].fields.definition = 'Une commande mobilise des possibilités ; un achat peut les compléter.';
  input.glossary.terms[0].definition = 'Commande d’achat portant les biens attendus.';
  input.glossary.terms[0].short_description = input.glossary.terms[0].definition;
  assert.equal(searchPublication(adaptPublication(input), 'commande d’achat')[0].id, 'DOC');
});
test('retired layer metadata is ignored by the reader; explicit parent relationships remain authoritative', () => {
  const input = raw();
  input.nodes[0].layer = 'process';
  input.nodes.push({ id: 'B', kind: 'behavior', layer: 'transactional', fields: { name: 'Behavior', definition: 'Comportement' } });
  input.relations.push({ id: 'P', type: 'contains', source_id: 'OTHER', target_id: 'B' });
  const model = adaptPublication(input);
  assert.equal('layer' in model.nodeById.get('B'), false);
  assert.equal(model.raw.nodes.at(-1).layer, 'transactional');
});
