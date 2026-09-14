import test from 'node:test';
import assert from 'node:assert/strict';
import { LikeC4 } from 'likec4';
import { loadPublication } from './load-publication.mjs';
import { projectLikeC4 } from './project-likec4.mjs';

const publication = await loadPublication({ version: '2026-09-13.5' });
const { dsl, manifest } = projectLikeC4(publication.raw, publication.descriptor);

test('LikeC4 identifiers round-trip, including non-prefix parents', () => {
  for (const node of publication.raw.nodes) assert.equal(manifest.likeC4ToAtlas[manifest.atlasToLikeC4[node.id]], node.id);
  assert.equal(Object.keys(manifest.atlasToLikeC4).length, publication.raw.nodes.length);
  assert.ok(manifest.atlasToLikeC4['D02.b'].startsWith(`${manifest.atlasToLikeC4.D01}.`));
  assert.ok(manifest.atlasToLikeC4['D02.e'].startsWith(`${manifest.atlasToLikeC4.D03}.`));
  const special = projectLikeC4({ nodes: ['a.b', 'a_b', 'a-b'].map(id => ({ id, kind: 'capability', fields: { name: id } })), relations: [] }, publication.descriptor);
  assert.equal(new Set(Object.values(special.manifest.atlasToLikeC4)).size, 3);
});

test('Every published relationship keeps its identity and its own type', () => {
  const projected = new Map([...manifest.structuralRelations, ...manifest.transverseRelations].map(relation => [relation.id, relation]));
  assert.equal(projected.size, publication.raw.relations.length);
  for (const relation of publication.raw.relations) assert.deepEqual(projected.get(relation.id), { id: relation.id, type: relation.type, sourceId: relation.source_id, targetId: relation.target_id });
});

test('Official LikeC4 parser preserves node provenance and transverse meaning', async () => {
  const engine = await LikeC4.fromSource(dsl);
  const parsed = await engine.computedModel();
  assert.equal([...parsed.elements()].length, publication.raw.nodes.length);
  assert.equal([...parsed.relationships()].length, manifest.transverseRelations.length);
  for (const relation of parsed.relationships()) {
    const original = publication.raw.relations.find(candidate => candidate.id === relation.getMetadata('atlasRelationId'));
    assert.ok(original);
    assert.deepEqual(JSON.parse(relation.getMetadata('qualification')), original.qualification ?? {});
    assert.equal(relation.getMetadata('reviewState'), original.review.state);
  }
  const referenceGroup = parsed.element(manifest.atlasToLikeC4['business-references']);
  assert.equal(referenceGroup.kind, 'presentation');
  assert.equal(parsed.element(manifest.atlasToLikeC4.D04).getMetadata('parentRelationType'), 'presents');
  assert.equal(parsed.element(manifest.atlasToLikeC4['D04.h']).getMetadata('parentRelationType'), 'contains');
  const realRelation = [...parsed.relationships()].find(relation => relation.getMetadata('atlasRelationId') === 'REL-EXECUTION-FACTS-ORDER-RECONCILIATION');
  if (realRelation) {
    const supplyEdge = parsed.view(manifest.mapViewByAtlasId['universe-supply']).$view.edges.find(edge => edge.relations.includes(realRelation.id));
    assert.ok(supplyEdge, 'LikeC4 should retain the source relation behind its grouped edge');
    assert.equal(manifest.likeC4ToAtlas[supplyEdge.source], 'D07');
    assert.equal(manifest.likeC4ToAtlas[supplyEdge.target], 'D04');
    const detailEdge = parsed.view(manifest.relationViewByAtlasId['D04.h']).$view.edges.find(edge => edge.relations.includes(realRelation.id));
    assert.equal(manifest.likeC4ToAtlas[detailEdge.source], 'D07.c');
    assert.equal(manifest.likeC4ToAtlas[detailEdge.target], 'D04.h');
  }
  await engine.dispose();
});
