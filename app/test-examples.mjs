import test from 'node:test';
import assert from 'node:assert/strict';
import { businessExamples, exampleSearchText } from './src/examples.ts';
import { marketSearchText, marketComparisonsForReading } from './src/marketContent.ts';
import { adaptPublication } from './src/model.ts';
import { searchPublication } from './src/search.ts';

test('explicit examples preserve situation, result and lesson without exposing their provenance', () => {
  const fields = { examples: [{ title: 'Réception partielle', situation: '60 reçues sur 100.', outcome: '40 restantes.', lesson: 'Annonce et réception diffèrent.', source_refs: ['sourceprivee'], review: 'secret' }] };
  assert.deepEqual(businessExamples(fields), [{ title: 'Réception partielle', situation: '60 reçues sur 100.', outcome: '40 restantes.', lesson: 'Annonce et réception diffèrent.' }]);
  assert.doesNotMatch(exampleSearchText(fields), /sourceprivee|secret/);
});
test('old scopes expose only explicit example paragraphs and retain their business caveats', () => {
  const fields = { scope: 'Frontière. Exemple fictif : 60 puis 40. Sous réserve de capacité.\n\nUn accord ne vaut pas réception.\n\nExemple simplifié : A vers B.\n\nExemples fictifs : scinder ou regrouper.' };
  assert.deepEqual(businessExamples(fields).map(e => e.situation), ['60 puis 40. Sous réserve de capacité.', 'A vers B.', 'scinder ou regrouper.']);
});
test('definitions and editorial evidence do not invent examples; identical excerpts are not duplicated', () => {
  assert.deepEqual(businessExamples({ definition: 'Exemple : ne pas récupérer la définition.', review: 'Exemple : privé.' }), []);
  assert.equal(businessExamples({ scope: 'Exemple : 40 pièces.\n\nExemple : 40 pièces.' }).length, 1);
  assert.deepEqual(businessExamples({ scope: 'La définition emploie des exemples dans sa méthode.' }), []);
});
test('discussed and formatted historical examples remain visible without their editorial labels', () => {
  const scope = 'Exemple discuté : 60 autorisées et 40 en attente.\n\nExemple illustratif FLOW : contrôle ciblé.\n\n**Exemple métier fictif.** Une révision est préparée.\n\nExemple fictif textile : comparer revente et retour.';
  assert.deepEqual(businessExamples({scope}).map(e=>e.situation), ['60 autorisées et 40 en attente.','contrôle ciblé.','Une révision est préparée.','comparer revente et retour.']);
});
test('naming choices come first without rewriting or reclassifying the comparison records', () => {
  const a=Object.freeze({element_name:'A'}), b=Object.freeze({element_name:'B',term_choice:'Terme'}), c=Object.freeze({element_name:'C',definition_choice:'Définition'});
  const records=Object.freeze([a,b,c]);
  assert.deepEqual(marketComparisonsForReading(records),[b,c,a]);
  assert.deepEqual(records,[a,b,c]);
});
test('structured examples take precedence over their historic inline wording without mixing versions', () => {
  assert.equal(businessExamples({ examples: [{ title: 'Nouveau', situation: 'Publié ici.' }], scope: 'Exemple : Ancien.' })[0].situation, 'Publié ici.');
  assert.deepEqual(businessExamples({ examples: [] }), []);
});
test('example contents and naming reasons are searchable, internal sources are not', () => {
  const model = adaptPublication({ space: 'release', version: 'fixture', nodes: [{ id: 'C', kind: 'capability', fields: {
    name: 'Purchase Order', definition: 'Achats', examples: [{ title: 'Réception partielle', situation: 'Manquant illustratif', source_refs: ['ultrasecret'] }],
    market_comparisons: [{ term_choice: 'Choix lexical explicite', definition_choice: 'Frontière économique', source_refs: ['ultrasecret'] }],
  }}], relations: [] });
  assert.equal(searchPublication(model, 'manquant illustratif')[0].id, 'C');
  assert.equal(searchPublication(model, 'frontière économique')[0].id, 'C');
  assert.deepEqual(searchPublication(model, 'ultrasecret'), []);
  assert.match(marketSearchText(model.nodes[0].fields.market_comparisons), /Choix lexical explicite/);
});
