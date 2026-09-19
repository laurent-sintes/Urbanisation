"""Targeted U450 presentation changes; never strip metadata from source models."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def edit(relative, replacements, patterns=()):
    path = ROOT / relative
    text = path.read_text(encoding='utf-8')
    for old, new in replacements:
        assert old in text, (relative, old[:100])
        text = text.replace(old, new)
    for pattern, replacement in patterns:
        text, count = re.subn(pattern, replacement, text, flags=re.S)
        assert count == 1, (relative, pattern, count)
    path.write_text(text, encoding='utf-8')

edit('app/src/components/BusinessSheet.tsx', [
    ('  const extraFields =', '  const extraFields ='),
    ('    <ValidationSummary item={node}/>\n', ''),
    ('          <span className={`pill ${behavior.status}`}>{statusLabel(behavior)}</span>\n', ''),
    ('      <Reservations item={node}/>\n', ''),
    ('      <Provenance model={model} item={node} onOpenSource={onOpenSource}/>\n', ''),
    ('<span className={`pill ${relation.status}`}>{statusLabel(relation)}</span>{relation.review.note && <p>{relation.review.note}</p>}{relation.lifecycle?.note && relation.lifecycle.note !== relation.review.note && <p>{relation.lifecycle.note}</p>}<Provenance model={model} item={relation} onOpenSource={onOpenSource}/>', ''),
    ('    <ValidationSummary item={relation}/>\n', ''),
    ('    <Reservations item={relation}/><Provenance model={model} item={relation} onOpenSource={onOpenSource}/>\n', ''),
    ('{ model, node, onOpenSource }: { model: PublishedModel; node: AtlasNode; onOpenSource: OpenSource }', '{ model, node }: { model: PublishedModel; node: AtlasNode }'),
    ('{ model, relation, onOpenSource }: { model: PublishedModel; relation: AtlasRelation; onOpenSource: OpenSource }', '{ model, relation }: { model: PublishedModel; relation: AtlasRelation }'),
], [(r'function SourceButtons\(.*?\nexport function BusinessSheet', 'export function BusinessSheet')])

edit('app/src/App.tsx', [
    ("import { SourceDialog } from './components/SourceDialog';\n", ''),
    ("  const [perspective, setPerspective] = useState('');\n", ''),
    ("{headingNode && <span className={`pill ${headingNode.status}`}>{statusLabel(headingNode)}</span>}", ''),
    (' onOpenSource={openSource}', ''),
    ('perspective={perspective}', 'perspective=""'),
    ('{kindLabel(selected)} · {statusLabel(selected)}', '{kindLabel(selected)}'),
    (' · Modèle en cours de construction', ''),
    ('    {model && <SourceDialog model={model} source={source} onClose={closeSource} />}\n', ''),
    ('Les clés du modèle', 'Comprendre le méta modèle'),
    ('Ouverture des clés du modèle…', 'Ouverture du méta modèle…'),
    ('COMPRENDRE LA MODÉLISATION', 'LE MÉTA MODÈLE'),
], [
    (r'  const openSource = useCallback\(.*?\n  const links =', '  const links ='),
    (r'\s*<select aria-label="Mettre en évidence un statut".*?</select>', ''),
])

edit('app/src/components/Sidebar.tsx', [
    ('Boolean(route.query || route.type || route.status)', 'Boolean(route.query || route.type)'),
    (" && (!route.status || n.status === route.status || n.lifecycle?.state === route.status)", ''),
    ('<br /><small>Publier ne vaut pas valider.</small>', ''),
    ('Les clés du modèle', 'Comprendre le méta modèle'),
], [(r'\s*<select id="fa-status".*?</select>', '')])

edit('app/src/ReactFlowPane.tsx', [
    ('<span className={`status-dot ${data.item.status}`} title={statusLabel(data.item)}/>', ''),
    ('{data.count ? `${data.count} éléments` : statusLabel(data.item)}', "{data.count ? `${data.count} éléments` : kindLabel(data.item)}"),
])

edit('app/src/DependenciesPane.tsx', [
    ('  onOpenSource: (id: string, locator?: SourceLocator) => void;\n', ''),
    (', onRead, onOpenSource }: Props', ', onRead }: Props'),
    (' onOpenSource={onOpenSource}', ''),
])

edit('app/src/components/MarketComparisons.tsx', [
    ('<span className="market-status">{statuses[entry.status]}</span>', ''),
    ('    <p className="market-intro">Repères pour discuter du vocabulaire et des périmètres. Une proximité avec un produit ne prouve pas sa mise en œuvre chez Beaumanoir.</p>\n', ''),
    ('        <div className="market-choice"><dt>Choix retenu ou proposé pour FLOW</dt><dd><ModelText text={entry.flow_position}/></dd></div>\n', ''),
    ('        <p><strong>Limite de preuve :</strong> {entry.evidence_limits}</p>\n', ''),
    ('        <p className="market-refs">Références : {entry.source_refs.join(\' · \')}</p>\n', ''),
])

edit('app/src/components/ModelingGuidePage.tsx', [
    ('Critères, frontières et sources', 'Critères et frontières'),
    ('Chargement des clés du modèle pour', 'Chargement du méta modèle pour'),
], [
    (r'\s*<section className="guide-scope">.*?</section>', ''),
    (r'\s*<details className="guide-sources">.*?</details>', ''),
    (r'\s*<div className="guide-edition">.*?</div>', ''),
])
