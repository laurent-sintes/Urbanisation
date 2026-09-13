/** Build navigation from exactly one authoritative JSON space.
 * UI shells are navigational only. No Markdown, prototype or backlog completion.
 */
export function createModel(data, exploration = {}) {
  if (!data || !Array.isArray(data.nodes) || !Array.isArray(data.relations)) throw new Error('Le modèle JSON doit fournir nodes et relations.');
  const snapshot = structuredClone(data);
  const config = structuredClone(exploration);
  const nodes = new Map();
  const labels = { ...config.labels, model: 'Vue de navigation', domain: 'Domaine', group: 'Groupe de présentation' };
  const icons = config.icons || {};
  const fail = message => { throw new Error(message); };
  const statusMap = { accepted: 'validated', partial: 'partial', under_review: 'review', proposed: 'proposed', illustration: 'illustration' };
  const add = node => {
    if (!node.id || nodes.has(node.id)) fail(`Identifiant dupliqué ou absent : ${node.id}.`);
    nodes.set(node.id, { sources: [], sourceLinks: [], purpose: '', definition: '', aliases: '', ...node, children: [] });
  };
  add({ id: 'atlas', kind: 'model', name: 'Le modèle business', status: 'navigation', purpose: 'Navigation dans l’espace sélectionné.' });
  add({ id: 'transactional', kind: 'model', name: 'Socle transactionnel', parentId: 'atlas', status: 'navigation', purpose: snapshot.space === 'release' ? 'Dernier modèle publié ; validations, propositions et réexamens restent explicitement distingués.' : 'Modèle en réflexion et conception ; statuts propres à chaque élément.' });
  add({ id: 'process', kind: 'model', name: 'Modèle processus', parentId: 'atlas', status: 'navigation', purpose: 'Modèle distinct de la couche transactionnelle, à développer.' });
  for (const raw of snapshot.nodes) {
    if (!labels[raw.kind]) fail(`Type de nœud inconnu : ${raw.kind}.`);
    if (snapshot.space === 'release' && !['accepted', 'partial', 'proposed', 'under_review'].includes(raw.review?.state)) fail(`Statut non publiable dans la release : ${raw.id}.`);
    const fields = raw.fields || {};
    const locator = raw.source_locator || {};
    const sources = raw.source_refs || [];
    add({
      id: raw.id, revision: raw.revision, kind: raw.kind,
      name: fields.name || `${raw.id} · Libellé à valider`,
      nameMissing: !fields.name,
      purpose: fields.finality || '', definition: fields.definition || '',
      approvedFields: raw.approved_fields || [], proposedFields: raw.proposed_fields || [], missingFields: raw.missing_fields || [], adoptionIds: raw.adoption_ids || [],
      scope: fields.scope, nature: fields.nature, fieldStatus: raw.field_status || raw.field_review || {},
      displayOrder: raw.id === 'business-references' ? 100 : 0,
      status: statusMap[raw.review?.state] || 'review', statusNote: raw.review?.note || '',
      modelId: raw.layer === 'process' ? 'process' : 'transactional',
      sources, sourcePath: locator.path, sourceAnchor: locator.anchor, sourceLine: locator.line,
      modelPath: snapshot.sourcePath, sourceLinks: sources.map(id => snapshot.sourceReferences?.[id]).filter(Boolean),
      aliases: snapshot.space === 'backlog' ? (config.aliases?.[raw.id] || '') : '',
    });
  }
  const relationLabels = {
    confirms: ['confirme', 'est confirmé par'],
    'associated-document': ['a pour document associé', 'est associé à'],
    'observed-result': ['a pour résultat constaté', 'constate le résultat de'],
    represents: ['représente les engagements de', 'est représenté dans'],
    records: ['porte la confirmation associée à', 'a pour document associé'],
    'provides-knowledge': ['fournit la connaissance des stocks à', 's’appuie sur les stocks connus dans'],
    'provides-conditions': ['fournit les conditions à appliquer à', 'applique les conditions reçues de'],
    'describes-network': ['décrit le réseau utilisé par', 'utilise les références du réseau de'],
  };
  const relationIndex = new Map();
  const relationIds = new Set();
  for (const raw of snapshot.relations) {
    if (!raw.id || relationIds.has(raw.id)) fail(`Identifiant de relation dupliqué ou absent : ${raw.id}.`);
    relationIds.add(raw.id);
    if (!nodes.has(raw.source_id) || !nodes.has(raw.target_id)) fail(`Cible de relation inconnue : ${raw.id}.`);
    if (snapshot.space === 'release' && !['accepted', 'partial', 'proposed', 'under_review'].includes(raw.review?.state)) fail(`Relation non publiable dans la release : ${raw.id}.`);
    if (['contains', 'presents'].includes(raw.type)) {
      const node = nodes.get(raw.target_id);
      if (node.parentId) fail(`Plusieurs parents de présentation : ${node.id}.`);
      node.parentId = raw.source_id;
      node.parentRelation = raw;
      continue;
    }
    const fields = raw.fields || {};
    const sources = raw.source_refs || [];
    const edge = {
      id: raw.id, from: raw.source_id, to: raw.target_id, type: raw.type,
      verb: fields.verb || raw.verb || fields.label || relationLabels[raw.type]?.[0] || raw.type,
      inverse: fields.inverse || raw.inverse || relationLabels[raw.type]?.[1] || `relation entrante : ${raw.type}`,
      status: statusMap[raw.review?.state] || 'review', statusNote: raw.review?.note || '',
      sources, sourcePath: raw.source_locator?.path,
      sourceLinks: sources.map(id => snapshot.sourceReferences?.[id]).filter(Boolean),
    };
    for (const [id, target, label, direction] of [[edge.from, edge.to, edge.verb, 'outgoing'], [edge.to, edge.from, edge.inverse, 'incoming']]) {
      if (!relationIndex.has(id)) relationIndex.set(id, []);
      relationIndex.get(id).push({ ...edge, target, label, direction });
    }
  }
  for (const node of nodes.values()) {
    if (node.kind !== 'model' && !node.parentId && !['object', 'document', 'event'].includes(node.kind)) {
      // A root placement is UI navigation, not an inferred business ownership.
      node.parentId = node.modelId;
      node.navigationParent = true;
    }
  }
  const completed = new Set();
  for (const start of nodes.values()) {
    const pending = new Set();
    let node = start;
    while (node && !completed.has(node.id)) {
      if (pending.has(node.id)) fail(`Cycle de hiérarchie détecté : ${[...pending, node.id].join(' → ')}.`);
      pending.add(node.id);
      node = nodes.get(node.parentId);
    }
    pending.forEach(id => completed.add(id));
  }
  for (const node of nodes.values()) {
    if (node.parentId) nodes.get(node.parentId).children.push(node.id);
  }
  for (const node of nodes.values()) node.children.sort((a, b) => (nodes.get(a).displayOrder || 0) - (nodes.get(b).displayOrder || 0));
  // The guided story is illustrative and available only in backlog, and only
  // when every target is part of that JSON model. UI config cannot add objects.
  const steps = snapshot.space === 'backlog' && (config.steps || []).every(step => nodes.has(step.id)) ? (config.steps || []) : [];
  const confirmation = nodes.has(config.confirmation) ? config.confirmation : undefined;
  const getNode = nodeOrId => typeof nodeOrId === 'string' ? nodes.get(nodeOrId) : nodes.get(nodeOrId?.id);
  function lineage(nodeOrId) {
    const path = [];
    let node = getNode(nodeOrId);
    while (node) {
      path.unshift(node);
      node = nodes.get(node.parentId);
    }
    return path;
  }
  function modelOf(nodeOrId) {
    const node = getNode(nodeOrId);
    if (!node) return undefined;
    if (node.modelId) return node.modelId;
    return lineage(node).reverse().find(ancestor => ancestor.kind === 'model')?.id;
  }
  function related(id) {
    return structuredClone(relationIndex.get(id) || []);
  }
  return { nodes, related, lineage, modelOf, labels, icons, steps, confirmation };
}


/** Separate As Is browser. No capability nodes or target-model relations enter it. */
export function createPanoramaModel(data, exploration = {}) {
  if (data?.space !== 'panorama-as-is' || !Array.isArray(data.panoramas)) throw new Error('Index panorama-as-is attendu.');
  const labels = { model: 'Vue de navigation', landscape: 'Panorama SI', category: 'Catégorie', component: 'Composant décrit', flow: 'Flux décrit', authority: 'Autorité d’information', responsibility: 'Responsabilité de décision' };
  const icons = { model: 'layers', landscape: 'database', category: 'library', component: 'box', flow: 'route', authority: 'file-text', responsibility: 'compass' };
  const nodes = new Map();
  const add = node => {
    if (nodes.has(node.id)) throw new Error(`Identifiant de panorama dupliqué : ${node.id}.`);
    nodes.set(node.id, { children: [], sources: [], sourceLinks: [], status: 'navigation', purpose: '', definition: '', aliases: '', ...node });
    if (node.parentId) nodes.get(node.parentId).children.push(node.id);
  };
  add({ id: 'atlas', name: 'Panorama As Is', kind: 'model', purpose: 'État de connaissance des SI actuels, distinct des modèles conçus et adoptés.' });
  add({ id: 'panorama', name: 'Panorama As Is', kind: 'model', parentId: 'atlas', purpose: 'Trois SI documentés séparément. La date de publication ne vaut pas observation des déploiements.', definition: (data.limitations || []).join(' ') });
  const entries = structuredClone(data.panoramas);
  if (data.shared?.data) entries.push({ model_id: 'shared-context', name: 'Contexte partagé · C-Log', data: data.shared.data, path: data.shared.path, contextOnly: true });
  for (const entry of entries) {
    const panorama = entry.data;
    const status = panorama.assessment_status === 'not_assessed' ? 'not_assessed' : 'documented';
    add({ id: entry.model_id, kind: 'landscape', name: entry.name, parentId: 'panorama', modelId: 'panorama', status,
      purpose: status === 'not_assessed' ? 'Non traité' : entry.contextOnly ? 'Contexte commun ; aucune interface n’est déduite de ce partage.' : 'Connaissances déclarées et réserves conservées.',
      definition: panorama.assessment_reason || (panorama.limitations || []).join(' '), modelPath: entry.path,
      statusNote: 'Les éléments déclarés ne constituent pas une preuve indépendante de déploiement.' });
    const categories = [['objects', 'Composants et organisations', 'component'], ['flows', 'Flux', 'flow'], ['information_authorities', 'Autorités d’information', 'authority'], ['decision_responsibilities', 'Responsabilités de décision', 'responsibility']];
    for (const [key, name, kind] of categories) {
      const records = panorama[key] || [];
      if (!records.length) continue;
      const parentId = `${entry.model_id}:${key}`;
      add({ id: parentId, name, kind: 'category', parentId: entry.model_id, modelId: 'panorama', purpose: `${records.length} éléments issus des récits et registres.`, status: 'navigation' });
      for (const record of records) {
        const loc = record.source_locator || {};
        const sources = record.source_refs || [];
        const details = [record.described_role, record.content, record.authority_or_producer && `Autorité ou producteur : ${record.authority_or_producer}`, record.other_contributions, record.described_realization && `Réalisation décrite : ${record.described_realization}`, record.modality && `Modalité : ${record.modality}`].filter(Boolean);
        add({ id: record.id, name: record.name || record.id, kind, parentId, modelId: 'panorama', status: record.evidence_status === 'observed' ? 'observed' : 'declared',
          purpose: details[0] || record.scope || '', definition: details.join(' '), scope: record.scope,
          statusNote: [...(record.limitations || []), ...((record.correction_context || []).map(c => c.text))].join(' '),
          sources, sourceLinks: sources.map(id => data.sourceReferences?.[id]).filter(Boolean), sourcePath: loc.path, sourceAnchor: loc.anchor, modelPath: entry.path,
          rawSource: record.source_fields, observedAt: record.observed_at,
        });
      }
    }
  }
  const get = value => nodes.get(typeof value === 'string' ? value : value?.id);
  const lineage = value => {
    const result = []; let node = get(value);
    while (node) { result.unshift(node); node = nodes.get(node.parentId); }
    return result;
  };
  return { nodes, labels, icons, lineage, modelOf: () => 'panorama', related: () => [], steps: [], confirmation: undefined };
}
