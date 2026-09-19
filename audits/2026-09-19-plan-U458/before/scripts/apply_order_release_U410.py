"""Enrich existing Order Release with collective launch conditions."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/order-release-U410'
REFS = ['U410', 'ELM245', 'CMP156']
DEFINITION = 'Autoriser la prise en charge de tout ou partie d’un Order, ou d’un ensemble d’Orders liés, lorsque les conditions de lancement individuelles et collectives sont satisfaites.'


def main():
    assert not OUT.exists(), 'Preserve previous evidence.'
    path = ROOT / 'modeles/backlog/model.yaml'
    before = read(path); model = deepcopy(before)
    audit = read(ROOT / 'modeles/backlog/behavior-gap-audit.yaml')
    assert '## U410\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U410

**id**

U410

**date**

2026-09-19

**titre**

Intégrer le lancement collectif dans Order Release

**texte**

Go

**contexte et portée**

Accord sur l’enrichissement d’Order Release BHV039, sous Order Lifecycle Management D04.o, sans comportement supplémentaire. La définition présentée autorise tout ou partie d’un Order ou un ensemble d’Orders liés selon des conditions individuelles et collectives. Complétude, éléments indispensables et traitement partiel sont explicités ; seuils et règles précises restent à définir. Affectation des ressources, autorisation de prise en charge et coordination des services restent distinctes. Autoriser ensemble ne présume pas un démarrage simultané. P11 est résolu par intégration au comportement existant. Les comparaisons et compléments rédactionnels gardent leur portée éditoriale ; aucun nouveau niveau, audit ou release.''')
    OUT.mkdir()
    for rel, name in [('modeles/backlog/model.yaml', 'model-before.yaml'), ('modeles/backlog/behavior-gap-audit.yaml', 'audit-before.yaml'), ('modeles/backlog/order-lifecycle-behaviors.yaml', 'lifecycle-before.yaml')]:
        (OUT / name).write_bytes((ROOT / rel).read_bytes())
    node = next(n for n in model['nodes'] if n['id'] == 'BHV039')
    parent = next(n for n in model['nodes'] if n['id'] == 'D04.o')
    assert 'scope' not in node['lifecycle']['validated_fields']
    assert 'scope' not in parent['lifecycle']['validated_fields']
    node['fields']['definition'] = DEFINITION
    node['fields']['scope'] = '''Autoriser la prise en charge selon les conditions applicables à un Order, une ligne, une quantité ou un ensemble d’Orders liés. Les conditions collectives peuvent porter sur la complétude requise, la présence d’éléments indispensables et l’acceptation éventuelle d’un traitement partiel. Les valeurs, seuils, autorités et dérogations éventuelles sont des règles de gestion à préciser ; aucun seuil universel n’est prescrit.

Exemple fictif individuel : un transfert de 100 pièces devient ferme ; seules 60 sont autorisées à partir, les 40 autres attendent. Affermir ne libère pas automatiquement et affecter des ressources ne suffit pas à autoriser la prise en charge.

Exemple fictif collectif : une implantation magasin comprend vêtements et accessoires. Les vêtements sont disponibles, mais certains accessoires indispensables manquent. Selon la politique retenue, autoriser un départ partiel ou attendre un ensemble cohérent. L’intérêt est d’éviter que des Orders individuellement prêts produisent un résultat d’ensemble inutilisable. Aucun cas installé Beaumanoir n’est déduit de cet exemple.

Order Release autorise la prise en charge ; Process Orchestration coordonne ensuite les services nécessaires à la réalisation autorisée. Autoriser plusieurs Orders ensemble n’impose ni un démarrage simultané de leurs services ni une transaction technique atomique. Le début physique est un fait observé par Operations Tracking, pas un effet présumé de l’autorisation.

Order Structuring conserve la composition persistante de l’ensemble lorsqu’elle existe ; aucun Order chapeau obligatoire n’est introduit par le lancement collectif. Les décisions de satisfaction et Supply Assignment conservent leurs responsabilités sur les ressources, les échéances et leurs affectations. Hold & Resume reste distinct ; une autorisation n’efface pas silencieusement les autres blocages applicables.

P11 Coordinated Order Release est intégré à ce comportement existant (U410), sans comportement autonome ni sous-comportement. Les modalités écran, batch, API ou flux ne constituent pas des comportements supplémentaires.'''
    comparisons = []
    for sid, similar, different in [
        ('S04', 'SAP distingue affectation et release check : les quantités affectées sont confrontées aux besoins pour autoriser la création de livraison, selon les règles de satisfaction.', 'ARun et ITA sont des mécanismes produit mêlant des responsabilités séparées dans FLOW. Le statut SAP ou le contrôle de livraison ne définit pas un cycle universel pour tous les Orders.'),
        ('S18', 'Oracle documente les shipment sets pour des lignes destinées à être expédiées ensemble, avec des contraintes collectives de progression et de mise en attente.', 'Un shipment set de lignes ne prouve pas une composition persistante de plusieurs Orders ni une capacité autonome. Ses contraintes produit ne sont pas imposées au modèle FLOW.')]:
        source = next(s for s in audit['sources'] if s['id'] == sid)
        comparisons.append(dict(vendor=source['vendor'], product=source['edition'], element_name=source['native_label'], element_type='Mécanisme produit', relationship='Recouvrement partiel', similarities=similar, differences=different,
            flow_position='Le besoin de cohérence collective enrichit Order Release existant. Affectation, autorisation et orchestration restent distinctes ; aucun comportement Coordinated Order Release supplémentaire.',
            source_title=source['native_label'], source_url=source['url'], source_version=source['edition'], source_locator=source['locator'], consulted_on='2026-09-19', evidence_limits='Source primaire ouverte et consultée lors de la proposition ; aucune preuve installée Beaumanoir. Oracle 26A explicitement consulté, sans affirmation de dernière version.', status='proposed', source_refs=REFS))
    node['fields'].setdefault('market_comparisons', []).extend(comparisons)
    life = node['lifecycle']
    life['validated_fields'] = list(dict.fromkeys(life['validated_fields'] + ['definition']))
    life['value_sha256']['definition'] = value_hash(DEFINITION)
    life['source_refs'] = list(dict.fromkeys(life['source_refs'] + ['U410']))
    life['recorded_at'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    life['note'] += ' U410 adopte la définition élargie et les principes du lancement collectif ; scope développé et comparaisons restent éditoriaux.'
    node['review'] = dict(state='partial', note='U410 : nom antérieur préservé, nouvelle définition adoptée ; descriptions et rapprochements éditoriaux. P11 intégré sans nouveau comportement.')
    parent['fields']['scope'] += '\n\nU410 : Order Release couvre aussi les conditions collectives d’un ensemble d’Orders liés : complétude, éléments indispensables et acceptation du partiel. Il autorise la prise en charge ; Process Orchestration coordonne les services. L’autorisation collective ne présume pas un démarrage simultané. P11 est intégré à BHV039 sans dixième comportement.'
    for entry in (node, parent):
        entry['revision'] += 1
        entry['source_refs'] = list(dict.fromkeys(entry['source_refs'] + REFS))
    assert model['relations'] == before['relations']
    save('modeles/backlog/model.yaml', model)
    migration = dict(source_refs=REFS, model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(), model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), adopted_definition=DEFINITION, definition_sha256=value_hash(DEFINITION), behaviors=[], delta={})
    for key in ('nodes', 'relations'):
        old = {v['id']: v for v in before[key]}; new = {v['id']: v for v in model[key]}
        assert old.keys() == new.keys()
        migration['delta'][key] = dict(added={}, removed=[], changed={i: value_hash(new[i]) for i in sorted(new) if new[i] != old[i]})
    save((OUT / 'implementation.yaml').relative_to(ROOT), migration)
    audit['implementation_U410'] = migration
    audit['baseline']['sha256'] = sha256(path.read_bytes()).hexdigest()
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + REFS))
    candidate = next(p for p in audit['candidates'] if p['id'] == 'P11')
    candidate.update(status='implemented_U410', implemented_as='BHV039', review_note='U410 : besoin de lancement collectif intégré à Order Release existant. Pas de comportement autonome ; règles précises à instruire sans bloquer le catalogue.', source_refs=list(dict.fromkeys(candidate['source_refs'] + REFS)))
    synth = audit['current_synthesis_U298']
    synth['reassess_candidate_ids'].remove('P11')
    synth['implemented_candidate_ids'].append('P11')
    assessment = next(x for x in audit['assessments'] if x['capability_id'] == 'D04.o')
    assessment['recommendation'] = 'U410 : lancement individuel et collectif décrits dans Order Release BHV039 ; P11 résolu sans comportement supplémentaire. Conditions détaillées par type et ensemble à préciser.'
    assessment['market_sources'] = list(dict.fromkeys(assessment['market_sources'] + ['S04', 'S18']))
    existing = next(x for x in audit['existing_behavior_review'] if x['behavior_id'] == 'BHV039')
    existing.update(status='enriched_U410', recommendation='Définition élargie adoptée ; autorisation individuelle ou collective distincte de l’affectation et de la coordination des services.', market_sources=['S04', 'S18'])
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    review = read(ROOT / 'modeles/backlog/order-lifecycle-behaviors.yaml')
    review['order_release_U410'] = dict(status='integrated', source_refs=REFS, behavior_id='BHV039', parent_id='D04.o', adopted_definition=DEFINITION, value_sha256=value_hash(DEFINITION), principles=['Conditions individuelles et collectives de lancement.', 'Complétude, éléments indispensables et traitement partiel ; seuils précis non prescrits.', 'Autoriser ensemble ne signifie pas démarrer simultanément.', 'P11 intégré au comportement existant ; pas de niveau supplémentaire.'], editorial_scope=node['fields']['scope'], market_comparisons=comparisons, implementation_ref=(OUT / 'implementation.yaml').relative_to(ROOT).as_posix())
    save('modeles/backlog/order-lifecycle-behaviors.yaml', review)
    agents = ROOT / 'AGENTS.md'
    text = agents.read_text(encoding='utf-8')
    marker = '- Stock Protection relève de la gouvernance/management.'
    assert marker in text
    text = text.replace(marker, '- **Order Release (U410)** : BHV039 autorise tout ou partie d’un Order ou un ensemble d’Orders liés selon des conditions individuelles et collectives. Complétude, éléments indispensables et partiel restent explicités ; seuils et règles détaillées à préciser. Affectation, autorisation et Process Orchestration distinctes ; autoriser ensemble ne présume pas un démarrage simultané. P11 intégré au comportement existant, sans comportement autonome. Voir `modeles/backlog/order-lifecycle-behaviors.yaml`, `order_release_U410`.\n'+marker, 1)
    agents.write_text(text, encoding='utf-8')
    append('marche/elements.md', '### ELM245\n\nSAP S/4HANA Fashion, Supply Assignment / Release checks ; Oracle Fusion Cloud SCM 26A, Guidelines for Managing Shipment Sets. Sources primaires ouvertes le 19 septembre 2026, URL, passages, éditions et limites dans modeles/backlog/order-lifecycle-behaviors.yaml, order_release_U410.market_comparisons. SAP distingue affectation et autorisation de livraison ; Oracle documente les contraintes collectives des shipment sets. Pas de preuve installée Beaumanoir.')
    append('marche/comparaisons.md', '### CMP156\n\nU410 — P11 rapproché du comportement Order Release BHV039. Le marché documente la cohérence collective préalable au lancement, mais ne justifie pas à lui seul une capacité ou un comportement autonome. FLOW enrichit le comportement existant : complétude, éléments indispensables et traitement partiel. SAP Release Check et Oracle Shipment Sets constituent des recouvrements partiels, pas des équivalences à tous les types d’Orders FLOW. L’affectation prépare les ressources ; Order Release autorise ; Process Orchestration coordonne les services. Autorisation collective distincte de simultanéité physique et d’atomicité technique. Définition adoptée, comparaisons éditoriales.')
    append('JOURNAL.md', '## 2026-09-19 — U410 : lancement collectif dans Order Release\n\nBHV039 enrichi avec une définition adoptée et des explications individuelles/collectives. P11 clôturé par intégration au comportement existant ; neuf comportements Lifecycle conservés. Comparaison SAP/Oracle consignée ELM245/CMP156. Audit existant et AGENTS actualisés, historique et relations préservés. Aucune release.')
    (OUT / 'README.md').write_text('# U410 — Order Release\n\nP11 intégré à BHV039 existant : conditions de lancement individuelles et collectives. Définition adoptée ; descriptions et comparaisons éditoriales. Aucun ajout de nœud ou relation.\n', encoding='utf-8')
    print('U410 integrated: P11 resolved in existing Order Release, unchanged graph.')


if __name__ == '__main__':
    main()
