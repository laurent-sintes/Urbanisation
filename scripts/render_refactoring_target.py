"""Validate and render the U286 proposal from its authoritative YAML."""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import json
from scripts.structured_io import read

ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'modeles/backlog/refactoring-target.yaml'
OUT=ROOT/'audits/2026-09-17-refonte-modele'

def cell(value):
    return str(value).replace('|',' / ').replace('\n',' ')

def main():
    d=read(TARGET); model=read(ROOT/d['baseline']['path'])
    assert sha256((ROOT/d['baseline']['path']).read_bytes()).hexdigest()==d['baseline']['sha256']
    nodes={n['id']:n for n in model['nodes']}
    caps={c['id']:c for c in d['capabilities']}
    behaviors={b['key']:b for b in d['behaviors']}
    sources={s['id']:s for s in d['sources']}
    assert len(caps)==len(d['capabilities'])==41
    assert set(caps)=={n['id'] for n in model['nodes'] if n['kind']=='capability'}
    assert len(behaviors)==len(d['behaviors'])
    assert {x['id'] for x in d['behavior_migration']}=={n['id'] for n in model['nodes'] if n['kind']=='behavior'}
    assert len(d['behavior_migration'])==15
    assert {r['id'] for r in d['existing_relation_review']}=={r['id'] for r in model['relations']}
    assert len(d['existing_relation_review'])==len(model['relations'])
    for c in caps.values():
        assert c['before']==nodes[c['id']]['fields']
        assert c['current_adoption']==nodes[c['id']].get('lifecycle',{})
        assert c['target']['definition'] and c['target']['example'] and c['target']['boundary'] and c['target']['scope']
        assert c['decomposition_rationale'] and set(c['market_sources'])<=set(sources)
        assert set(c['needs_providers'])<=set(caps)
        assert set(c['behavior_keys'])<=set(behaviors)
    merge=d['merge_proposal']
    parent_names={cid:c['before']['name'] for cid,c in caps.items()}
    parent_names[merge['key']]=merge['name']
    referenced=list(merge['behavior_keys'])
    for c in caps.values(): referenced+=c['behavior_keys']
    assert Counter(referenced)==Counter({key:1 for key in behaviors})
    for b in behaviors.values():
        assert b['parent_id'] in parent_names
        assert b['key'] in (merge['behavior_keys'] if b['parent_id']==merge['key'] else caps[b['parent_id']]['behavior_keys'])
        assert b['targeted_benefit'] and b['differentiator'] and b['definition']
        assert set(b['market_sources'])<=set(sources)
    for m in d['behavior_migration']:
        assert m['target'] in set(caps)|set(behaviors)
    keys=[x['key'] for x in d['dependencies']]
    assert len(keys)==len(set(keys))
    for r in d['dependencies']:
        assert r['consumer'] in caps and r['provider'] in caps and r['consumer']!=r['provider']
        assert r['result'] and r['condition'] and r['effect']
        assert set(r['existing_edges_between'])<={x['id'] for x in model['relations']}
    merge=d['merge_proposal']
    assert set(merge['source_ids'])<=set(caps)
    target_count=len(caps)-len(merge['source_ids'])+1
    def refs(ids):
        return ', '.join(f"[{sid} — {sources[sid]['vendor']}]({sources[sid]['url']})" for sid in ids) or 'Justification FLOW ; pas de nouvelle équivalence marché établie.'
    count_core=sum(b['status']!='conditional_arbitration' for b in behaviors.values())
    implemented=d.get('implementation')
    report=[
      '# Refonte du modèle FLOW — cible complète U286','',
      ('17 septembre 2026. **Cible de référence préparée U286–U289, socle appliqué U290.** Cette page conserve les propositions telles que présentées avant migration ; les statuts courants et écarts sont dans le [bilan de mise en œuvre](../2026-09-17-refonte-appliquee/rapport.md). Les mentions de catalogue inchangé et arbitrages à venir ci-dessous décrivent cette revue antérieure.' if implemented else '17 septembre 2026. Proposition préparée à la demande de Laurent. **Le catalogue actif reste inchangé pendant cette revue.**'),
      '',
      f"**41 capacités examinées, 15 comportements actuels traités et {len(model['relations'])} relations existantes revues.** Cible recommandée : {target_count} capacités après le regroupement adopté Promise Management, hors éventuelle capacité supplémentaire pour U287 ; {count_core} comportements de cœur, plus 4 conditionnels. Un mécanisme supplémentaire d’application de plan est retenu dans D04 (U287), avec capacité parente à préciser. Ces nombres sont un résultat du découpage proposé, pas un quota.",
      '',
      'Le niveau Capacité → Comportement reste suffisant pour les cas examinés. La refonte porte sur le sens, les frontières, les descriptions et les dépendances. Case/Business Services et les réalisations des trois SI ne sont pas audités ici.',
      '',
      'Autorité de cette proposition : [annexe YAML](../../modeles/backlog/refactoring-target.yaml). Le modèle actif reste [model.yaml](../../modeles/backlog/model.yaml). Ce document et les fiches sont dérivés de l’annexe.',
      '',
      '- [Matrice avant/après et 41 fiches](capacites.md)',
      '- [Comportements proposés et migration des 15 existants](comportements.md)',
      '- [Dépendances et revue de toutes les relations](relations.md)',
      '- [Sources primaires et limites](sources.md)',
      '',
      '**Précision U289 :** Supply Assignment = affectation des ressources aux commandes ; Supply Assignment Plan = plan d’affectation. Allocation seul est écarté des libellés FLOW. [Étude et convention](../../marche/assignment-allocation-convention.md). L’interprétation du plan U287 comme répartition magasin est corrigée.','',
      '## Ce que change la cible','',
      '| Ensemble | Proposition concrète | Portée |','| --- | --- | --- |',
      '| Inventory Planning | Construction de scénarios alternatifs ; Simulation & analyse ; adaptation du scénario en cours | Directions adoptées U283/U284 ; noms anglais et synthèses proposés |',
      '| Supply Protection | Group Supply Protection ; Consumption Capping ; Safety Stock Policy ; Replenishment Regulation | Liste, définitions et articulation proposées |',
      '| Order Management | Application des conséquences du scénario / plan d’affectation sur les Orders | U287 précisé U289 ; liens ressources-commandes conservés par Supply Assignment ; A8 à instruire |',
      '| ATP | Conserver ses quatre comportements | Définitions adoptées conservées ; justification enrichie proposée |',
      '| Promise Proposal / Confirmation / Revision | Promise Management avec trois comportements Proposal, Confirmation et Revision | Regroupement et décomposition adoptés U288 ; 41 → 39 hors U287 |',
      '| Reservation / Supply Assignment | Maintenir en attendant une frontière démontrée | Arbitrage A3 ; pas de fusion automatique |',
      '| Order Lifecycle Management | Nature management, autorisation et application des transitions | Arbitrage A4 |',
      '| Stock Allocation Decision | Nom cible Group Protection Decision, même décision de droits par groupe | Clarification lexicale proposée U289 ; nom actif conservé |',
      '| Replenishment Decision | Décider aussi les ajustements des apports futurs excessifs | Arbitrage A5 ; application par D04 |',
      '| Stocktaking / Execution Orchestration | Deux mécanismes candidats chacun | A6 ; option conditionnelle, pas nécessaire au cœur |',
      '',
      'Le bénéfice du refacto ne se mesure pas à la réduction du nombre de nœuds. Les opérations restent expliquées ; elles quittent la hiérarchie lorsqu’elles ne différencient pas une manière d’agir.',
      '',
      '## 1 — Changements déductibles des accords','']
    report += ['- '+x for x in d['work_packages']['from_existing_agreements']]
    report += ['','**Déjà réalisé dans cette passe :** cible exhaustive, table de migration, preuves marché, nettoyage des consignes actives et signalement de l’ancien audit comme historique depuis AGENTS. Ses fichiers historiques sont conservés. Les mutations du catalogue sont préparées dans la proposition ; aucune nouvelle valeur n’est présentée comme adoptée par ce seul travail.',
      '',
      '## 2 — Arbitrages conjoints','',
      '| Repère | Sujet | Recommandation | Décision attendue |','| --- | --- | --- | --- |']
    for a in d['arbitrations']: report.append('| '+' | '.join(cell(a[k]) for k in ['id','topic','recommendation','choice'])+' |')
    report += ['','**Ordre conseillé : A1 Protection et A8 application de plan, A3 engagement, A4/A5 cycle et apports ; A2 est résolu par U288, A6 reste optionnel.** A7 accompagne chaque cas. La mise en cohérence Planning est déjà cadrée par nos accords ; les détails éditoriaux proposés sont regroupés dans ses fiches.',
      '',
      '## Protection : couverture et limites','',
      '| Préoccupation | Destination proposée | Limite |','| --- | --- | --- |']
    for x in d['protection_coverage']: report.append('| '+cell(x['concern'])+' | '+cell(', '.join(x['covered_by']))+' | '+cell(x['limit'])+' |')
    application=d['order_plan_application_U287']
    report += ['','## Application de scénario ou plan dans Order Management — U287','', application['proposed_definition'],'','**Bénéfice :** '+application['targeted_benefit'],'','**Exemple :** '+application['example'],'','**Rattachement :** '+application['parent_arbitration'],'','**Marché :** '+refs(application['market_sources']),'']
    report += ['**Frontières :**'] + ['- '+key+' : '+value for key,value in application['boundaries'].items()]
    report += ['','Les quatre mécanismes de Protection se combinent. Le stock de sécurité exprime le rôle de tampon ; la régulation indique quand et comment renouveler. Une même valeur peut intervenir dans les deux, sans être comptée deux fois. La protection d’un groupe préserve son accès ; le plafond limite sa consommation. La fin de vie est d’abord un contexte de ces politiques, sans comportement additionnel automatique.',
      '',
      '## Cas pour éprouver les frontières','']
    for x in d['scenario_tests']:
        report += [f"**{x['id']} — {x['case']}**",x['test'],f"Résultat attendu : {x['expected']}",'']
    report += ['## Manques à instruire','']
    for x in d['known_gaps']: report += [f"- **{x['topic']}** : {x['recommendation']} {x['decision_needed']}"]
    report += ['','## Migration et contrôles','']+['- '+x for x in d['work_packages']['technical_migration']]
    report += ['','Les relations proposées sont orientées « consommateur a besoin du fournisseur ». Les liens historiques conservent leur sens natif ; aucune inversion mécanique. Les liens d’information et d’application peuvent être réciproques selon la phase, sans imposer un appel récursif ni une séquence logicielle.',
      '',
      'Le contrôle de couverture vérifie chaque capacité, ancien comportement et relation, les références et les rattachements uniques. Il ne remplace pas les arbitrages métier. Rapport technique : [checks.json](checks.json).',
      '',
      'Régénération : python -m scripts.render_refactoring_target. Les publications, accords historiques et valeurs du catalogue actif restent préservés.']
    (OUT/'rapport.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    names={'maintain':'Conserver','conditional_behaviors':'Décomposer sous condition','rebuild_behaviors':'Refondre comportements','boundary_arbitration':'Frontière à arbitrer','merge_candidate':'Regroupement proposé','merge_adopted_behaviors':'Regroupement et comportements adoptés U288','retain_behaviors':'Conserver comportements','maintain_with_gap':'Conserver + manque à localiser','nature_arbitration':'Nature à arbitrer','scope_extension_arbitration':'Périmètre à étendre','maintain_pending_prior_arbitration':'Conserver proposition non adoptée'}
    doc=['# Les 41 capacités — avant/après','',
      '[Synthèse](rapport.md) · [Comportements](comportements.md) · [Dépendances](relations.md)','',
      'Toutes les nouvelles descriptions et illustrations restent proposées. Le maintien d’une valeur conserve son statut actuel. Les fonctions contenues dans les anciens scopes restent matière utile : aucune perte par retrait de la hiérarchie.',
      '',
      '| ID | Capacité | Destination |','| --- | --- | --- |']
    for c in caps.values(): doc.append(f"| {c['id']} | {cell(c['before']['name'])} | {names[c['recommendation']]} |")
    for c in caps.values():
        t=c['target']
        doc += ['',f"## {c['id']} — {c['before']['name']}",'',f"**Recommandation : {names[c['recommendation']]}** — {c['justification']}",'',
          '**Nom cible :** '+t['name']+' (nom courant : '+c['before']['name']+').','',
          '**Avant :** '+c['before']['definition'],'',
          '**Cible proposée / valeur conservée :** '+t['definition'],'',
          f"**Nature :** {t['nature'] or 'non établie — ne pas déduire automatiquement'} ({t['nature_status']}).",
          '**Frontière :** '+t['boundary'],'',
          '**Fonctions conservées :** '+t['supporting_functions'],'',
          '**Exemple fictif :** '+t['example'],'',
          '**Comportements :** '+(', '.join(behaviors[k]['name'] for k in c['behavior_keys']) or 'Aucune décomposition recommandée à ce stade.'),
          '**Justification de décomposition :** '+c['decomposition_rationale'],'',
          '**A besoin de — proposition :** '+(', '.join(f"{x} {caps[x]['before']['name']}" for x in c['needs_providers']) or 'Source maîtresse externe ; pas de fournisseur interne imposé.'),
          '**Marché / justification :** '+refs(c['market_sources']),'',
          '**Entrées externes :** '+c['external_inputs_to_qualify'],'',
          '**Accords conservés :** '+(', '.join(c['current_adoption'].get('validated_fields',[])) or 'Aucun champ adopté dans le lifecycle ; autres preuves historiques conservées dans le modèle.')+'. Aucun accord étendu aux nouveaux textes.']
        if c['recommendation'] in ('merge_candidate','merge_adopted_behaviors'): doc += ['','**Destination commune adoptée U288 : Promise Management ; définition détaillée proposée.** '+merge['definition']+' '+merge['identity_plan']]
    (OUT/'capacites.md').write_text('\n'.join(doc)+'\n',encoding='utf-8')
    doc=['# Comportements et migration','', '[Synthèse](rapport.md)','',
      'Clés PLAN/PROTECT/COUNT/ORCH : repères de proposition, pas IDs de nouveaux nœuds. Un parent explicite, même couche ; pas de sous-comportement. Les quatre comportements COUNT/ORCH sont conditionnels.']
    for b in behaviors.values():
        doc += ['',f"## {b['key']} — {b['name']}",'',f"Parent : {b['parent_id']} — {parent_names[b['parent_id']]}. Statut : {b['status']}.",'',
          b['definition'],'',f"**Critère :** {b['differentiator']}. **Bénéfice :** {b['targeted_benefit']}",'',
          '**Exemple fictif :** '+b['example'],'','**Frontière :** '+b['boundary'],'','**Appui :** '+refs(b['market_sources'])]
    doc += ['','## Destination de chaque comportement existant','',
      '| Ancien ID | Nom | Traitement proposé | Destination | Conservation du besoin |','| --- | --- | --- | --- | --- |']
    for m in d['behavior_migration']: doc.append('| '+' | '.join(cell(x) for x in [m['id'],m['before']['name'],m['action'],m['target'],m['reason']])+' |')
    doc += ['','Les noms et valeurs adoptés sont conservés dans la capture et l’annexe. À la migration, BHV006 conserve son identité avec révision de contenu, BHV010 est absorbé et retiré. BHV009 ne devient pas adaptation : un nouvel identifiant sera créé. Les cinq comportements d’allocation sont retirés comme nœuds, avec leurs fonctions replacées dans Protection. Aucune de ces mutations n’est encore exécutée.']
    (OUT/'comportements.md').write_text('\n'.join(doc)+'\n',encoding='utf-8')
    doc=['# Dépendances proposées et relations existantes','',
      '[Synthèse](rapport.md)','',
      'Propositions de contrats métier issues des descriptions ; elles ne sont pas toutes adoptées. Consommateur → fournisseur, avec résultat et condition. Les paires historiques sont des repères de recherche, pas des équivalences certifiées. Les références d’ingestion désignent les informations projetées ; elles n’imposent pas d’appeler le processus d’ingestion à chaque décision.',
      '',
      '| Consommateur | Fournisseur | Résultat requis | Condition | Repères existants |','| --- | --- | --- | --- | --- |']
    for r in d['dependencies']: doc.append('| '+' | '.join(cell(x) for x in [r['consumer'],r['provider'],r['result'],r['condition'],', '.join(r['existing_edges_between']) or 'À créer/qualifier'])+' |')
    doc += ['','Le regroupement Promise Management adopté U288 conduit à remplacer D03.a/b/c par la clé proposée PROMISE-MANAGEMENT. Les dépendances devenant internes ne créent pas de boucle ; les autres contrats sont conservés et dédoublonnés seulement après examen. La projection figure dans le YAML.','','## Revue exhaustive des liens courants','',
      '| ID | Relation actuelle | Traitement | Motif |','| --- | --- | --- | --- |']
    for r in d['existing_relation_review']: doc.append('| '+' | '.join(cell(x) for x in [r['id'],f"{r['source']} → {r['target']} ({r['type']})",r['action'],r['reason']])+' |')
    (OUT/'relations.md').write_text('\n'.join(doc)+'\n',encoding='utf-8')
    doc=['# Marché — preuves et limites','',
      'Consultation le 17 septembre 2026. Sources primaires ciblées ; pas d’étude exhaustive de tous les éditeurs ni de preuve de déploiement. Chaque rapprochement est proposé ; les choix de maille restent FLOW.','']
    for s in sources.values(): doc += [f"## {s['id']} — {s['vendor']} : {s['title']}",'',f"[Source primaire]({s['url']}) — {s['edition']}. Passage : {s['passage']}.",s['finding'],'Limite : '+s['limit'],'']
    (OUT/'sources.md').write_text('\n'.join(doc)+'\n',encoding='utf-8')
    if implemented:
        for filename in ['capacites.md','comportements.md','relations.md']:
            path=OUT/filename
            heading, body=path.read_text(encoding='utf-8').split('\n',1)
            notice='\n\n> Revue de référence U286–U289 avant migration. Le socle a été appliqué U290 ; les mentions de proposition ou de migration à venir ci-dessous décrivent cet état antérieur. Voir le [bilan courant](../2026-09-17-refonte-appliquee/rapport.md).\n'
            path.write_text(heading+notice+body,encoding='utf-8')
    active_unchanged=sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest()==d['baseline']['sha256']
    assert active_unchanged or implemented, 'Live model changed without a migration record.'
    if implemented:
        migration=read(ROOT/implemented['registry'])
        assert migration['state']=='core_implemented'
        assert sha256((ROOT/migration['baseline']).read_bytes()).hexdigest()==d['baseline']['sha256']
    integrity=read(OUT/'integrity.json')
    assert all(sha256((ROOT/path).read_bytes()).hexdigest()==h for path,h in integrity['protected_files'].items())
    checks=dict(capabilities_reviewed=len(caps),behaviors_mapped=len(d['behavior_migration']),relations_reviewed=len(d['existing_relation_review']),
        dependency_contracts_proposed=len(d['dependencies']),recommended_core_behaviors=count_core,conditional_behaviors=4,additional_domain_direction_pending_parent='U287',
        target_capabilities_before_U287_parent_choice=target_count,live_model_unchanged=active_unchanged,reference_checks='passed',scope='Structural coverage, not business acceptance')
    (OUT/'checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
    print(json.dumps(checks))

if __name__=='__main__': main()
