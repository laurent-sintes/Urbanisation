import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { createModel, createPanoramaModel } from './model.js';

const read = async relative => JSON.parse(await readFile(new URL(relative, import.meta.url), 'utf8'));
const backlog = await read('../modeles/backlog/model.json');
const pointer = await read('../modeles/release/current.json');
const release = await read('../modeles/release/' + pointer.path);
const config = await read('./exploration.json');
const clone = value => structuredClone(value);

test('le backlog conserve les identifiants déplacés et les 36 capacités', () => {
  const model = createModel(backlog, config);
  assert.equal([...model.nodes.values()].filter(n => n.kind === 'capability').length, 36);
  assert.equal(model.nodes.get('D02.b').parentId, 'D01');
  assert.equal(model.nodes.get('D02.c').parentId, 'D01');
  assert.equal(model.nodes.get('D02.e').parentId, 'D03');
  assert.equal(model.nodes.get('D03').children.length, 9);
  assert.equal(model.nodes.get('business-references').children.length, 5);
});

test('la release publie 36 capacités avec statuts explicites et sans compléter depuis le backlog', () => {
  const poisoned = clone(config);
  poisoned.nodes = [{id:'D08', name:'INVENTED'}, {id:'NEW', name:'Invented'}];
  poisoned.relations = [{from:'D01',to:'D03',type:'fake'}];
  const model = createModel(release, poisoned);
  const capabilities=[...model.nodes.values()].filter(n=>n.kind==='capability');
  assert.equal(capabilities.length,36);
  assert.equal(capabilities.filter(n=>n.status==='validated').length,9);
  assert.equal(model.nodes.get('D08').name,release.nodes.find(n=>n.id==='D08').fields.name);
  assert.equal(model.nodes.get('D08').aliases,'');
  assert.equal(model.nodes.has('NEW'),false);
  assert.equal(model.nodes.get('D04.a').status,'review');
  assert.equal(model.nodes.has('ILL-OBJ-01'),false);
  assert.equal(model.steps.length,0);
  assert.equal(model.related('D01').length,0);
  assert.equal(model.nodes.get('D02.c').parentRelation.review.state,'under_review');
  assert.ok(model.nodes.get('D02.c').parentRelation.adoption_ids.length);
  const partial=clone(release);delete partial.nodes.find(n=>n.id==='D08').fields.name;
  assert.equal(createModel(partial,poisoned).nodes.get('D08').name,'D08 · Libellé à valider');
});

test('objet, document et événement restent séparés des capacités', () => {
  const model = createModel(backlog, config);
  assert.deepEqual(model.nodes.get('D03.b').children, []);
  assert.equal(model.related('D03.b').length, 3);
  for (const [id, kind] of [['ILL-OBJ-01','object'],['ILL-DOC-01','document'],['ILL-EVT-01','event']]) {
    assert.equal(model.nodes.get(id).kind, kind);
    assert.equal(model.nodes.get(id).parentId, undefined);
    assert.equal(model.modelOf(id), 'transactional');
  }
  assert.equal(model.modelOf('ILL-OBJ-02'), 'process');
  assert.equal(model.steps.length, 4);
});

test('les relations inverses conservent le sens, le statut et la provenance', () => {
  const model = createModel(backlog, config);
  const relation = model.related('ILL-OBJ-01').find(e => e.from === 'D03.b');
  assert.equal(relation.label, 'est confirmé par');
  assert.equal(relation.direction, 'incoming');
  assert.deepEqual(relation.sources, ['P80']);
  assert.equal(relation.status, 'illustration');
});

test('aucune profondeur fixe, cycles de hiérarchie refusés et relations métier cycliques permises', () => {
  const value = clone(backlog);
  for (let i=1;i<=4;i++) {
    value.nodes.push({id:`group-${i}`,kind:'group',layer:'transactional',fields:{name:`Group ${i}`},review:{state:'proposed'},source_refs:['TEST']});
    value.relations.push({id:`edge-${i}`,type:'contains',source_id:i===1?'D03':`group-${i-1}`,target_id:`group-${i}`,source_refs:['TEST'],review:{state:'proposed'}});
  }
  value.relations.find(r=>r.target_id==='D03.b'&&r.type==='contains').source_id='group-4';
  assert.equal(createModel(value,config).lineage('D03.b').length, 8);
  value.relations.push({id:'cycle',type:'contains',source_id:'group-4',target_id:'D03',source_refs:['TEST'],review:{state:'proposed'}});
  assert.throws(()=>createModel(value,config),/Cycle de hiérarchie/);
  value.relations.at(-1).type='business-cycle';
  assert.doesNotThrow(()=>createModel(value,config));
});

test('identifiants dupliqués, cibles absentes et illustrations en release sont refusés', () => {
  const duplicate=clone(backlog);duplicate.nodes.push(duplicate.nodes[0]);
  assert.throws(()=>createModel(duplicate,config),/Identifiant dupliqué/);
  const dangling=clone(backlog);dangling.relations[0].target_id='unknown';
  assert.throws(()=>createModel(dangling,config),/Cible de relation inconnue/);
  const proposed=clone(release);proposed.nodes[0].review.state='illustration';
  assert.throws(()=>createModel(proposed,config),/non publiable/);
});

test('les modèles et la configuration ne sont jamais mutés par la navigation', () => {
  const before=clone(backlog), beforeConfig=clone(config);
  const model=createModel(backlog,config);
  model.nodes.get('D03').children.length=0;
  model.related('D03.b')[0].sources.push('TEMP');
  model.steps[0].text='TEMP';
  assert.deepEqual(backlog,before);assert.deepEqual(config,beforeConfig);
  assert.deepEqual(model.related('D03.b')[0].sources,['P80']);
});

test('panorama séparé : trois SI, contexte partagé et Sarenza non traité', async () => {
  const panorama=await read('../modeles/panorama-as-is/current.json');
  for(const entry of panorama.panoramas) entry.data=await read('../'+entry.path);
  panorama.shared.data=await read('../'+panorama.shared.path);
  const model=createPanoramaModel(panorama,config);
  assert.equal(model.nodes.get('panorama').children.length,4);
  assert.equal(model.nodes.get('sarenza-si').status,'not_assessed');
  assert.equal(model.nodes.get('sarenza-si').children.length,0);
  assert.equal(model.nodes.get('APP-STR').modelId,'panorama');
  assert.equal(model.nodes.has('D03'),false);
  assert.equal([...model.nodes.values()].some(n=>n.kind==='capability'),false);
  assert.equal(model.related('APP-STR').length,0);
});
