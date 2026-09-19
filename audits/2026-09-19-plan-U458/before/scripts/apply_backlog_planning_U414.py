"""Add Order Backlog Planning and move the existing Order Release behavior."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/backlog-planning-U414'
REFS = ['U414', 'ELM247', 'CMP158']
NAME = 'Order Backlog Planning'
DEFINITION = 'Construire, comparer et maintenir les scénarios de satisfaction du carnet d’Orders, en mobilisant les décisions spécialisées, puis préparer et autoriser la prise en charge de la part retenue par les processus.'


def main():
    assert not OUT.exists()
    mp = ROOT/'modeles/backlog/model.yaml'; before = read(mp); model = deepcopy(before)
    assert not any(n['id']=='D03.p' for n in model['nodes'])
    assert '## U414\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U414

**id**

U414

**date**

2026-09-19

**titre**

Créer Order Backlog Planning et y rattacher Order Release

**texte**

Go

**contexte et portée**

Accord sur la capacité Order Backlog Planning dans D03 et sa définition présentée : construire, comparer et maintenir les scénarios, mobiliser les décisions spécialisées, préparer et autoriser la prise en charge retenue. Déplacement du comportement existant Order Release BHV039 sous cette capacité, sans duplication ni changement de son identifiant ou de sa définition U410. Split et Structuring restent en D04 pour un arbitrage ultérieur. Planning ne remplace ni Fulfillment Plan Decision, ni Supply Assignment, ni Promise Management, ni Process Orchestration ; la release ne crée pas automatiquement une réservation et ne constate pas un démarrage physique. Aucun autre comportement Planning créé par généralisation. Description développée, justification éditoriale et comparaisons qualifiées séparément ; pas de release du modèle.''')
    OUT.mkdir()
    for path, name in [('modeles/backlog/model.yaml','model-before.yaml'),('modeles/backlog/behavior-gap-audit.yaml','audit-before.yaml'),('modeles/backlog/order-backlog-review.yaml','review-before.yaml'),('modeles/backlog/order-lifecycle-behaviors.yaml','lifecycle-before.yaml')]:
        (OUT/name).write_bytes((ROOT/path).read_bytes())
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def life(values, fields):
        return dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U414'],validated_fields=fields,value_sha256={f:value_hash(values[f]) for f in fields},note='U414 : seuls les champs indiqués et rattachements présentés sont adoptés. Descriptions développées et comparaisons éditoriales.')
    review = read(ROOT/'modeles/backlog/order-backlog-review.yaml')
    comparisons = deepcopy(review['market_comparisons'][:2])
    for comp in comparisons:
        comp['flow_position']='Order Backlog Planning travaille les scénarios en mobilisant les décisions ; Order Release en est un comportement. Oracle release ses résultats vers Order Management ; FLOW distingue cette opération produit de son autorisation de prise en charge vers les processus.'
        comp['source_refs']=REFS
    comparisons.append(dict(vendor='Microsoft',product='Dynamics 365 Supply Chain Management',element_name='Planned orders simplified',element_type='Fonction produit',relationship='Recouvrement partiel',similarities='Revue, approbation et affermissement des propositions issues de la planification ; split disponible dans la page standard.',differences='Propositions d’approvisionnement, pas tous les Orders FLOW. La liste d’opérations produit ne devient pas une décomposition automatique en comportements.',flow_position='Appui à une capacité de travail sur les propositions alimentée par la planification ; aucune équivalence de firming avec Order Release.',source_title='Planned orders simplified',source_url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-orders-simplified',source_version='Page mise à jour le 3 octobre 2025',source_locator='View, manage, and firm planned orders',consulted_on='2026-09-19',evidence_limits='Source primaire ouverte lors de la proposition ; aucune preuve installée Beaumanoir.',status='proposed',source_refs=REFS))
    rationale='La complexité du carnet exige de travailler plusieurs hypothèses de satisfaction et leurs impacts avant engagement. Order Release rend explicite le passage d’une satisfaction envisagée à une prise en charge autorisée, avec conditions individuelles et collectives ; son bénéfice est la maîtrise de cet engagement. Il reste le seul comportement directement rattaché à ce stade : aucun comportement ajouté pour chaque opération, ni reprise automatique des comportements d’Inventory Planning.'
    fields=dict(name=NAME,definition=DEFINITION,nature='planning',finality='Transformer les scénarios de satisfaction du carnet en une préparation cohérente de leur prise en charge, en conservant la maîtrise des engagements.',scope='''Travailler les hypothèses, comparer leurs effets, maintenir le scénario retenu et préparer sa mise en action. Planning peut être humain, automatisé ou mixte. Il mobilise Fulfillment Plan Decision pour déterminer les scénarios cohérents, et les décisions spécialisées pour leurs contributions ; il ne crée pas un deuxième moteur d’ATP, de CTP, de priorité ou d’arbitrage économique.

Exemple fictif : préparer une hypothèse privilégiant les ouvertures de magasins et une autre préservant davantage les dates promises. Les décisions produisent les scénarios correspondants ; Planning permet d’en examiner les impacts et de préparer celui qui sera engagé, sans présumer une validation humaine obligatoire ou une pondération unique de valeur.

Pour une demande de 100 pièces, le scénario peut retenir 60 maintenant et 40 plus tard. Order Release autorise les 60 selon les conditions individuelles et collectives. Supply Assignment conserve l’application des affectations de ressources ; Promise Management gère les engagements de promesse ; Process Orchestration coordonne les services pour la part autorisée. Une release ne crée pas automatiquement une réservation, ne lève pas les protections et ne signifie pas que les opérations physiques ont commencé.

Maintenir le scénario à partir des faits et des écarts reste distinct de Process Adaptation Decision, qui choisit les adaptations des processus opérationnels. D04 conserve le sens de la demande, ses mutations applicables et sa composition. Order Splitting et Order Structuring restent à leur place en attendant leur réexamen ciblé : fractionner la satisfaction ne présume pas créer deux commandes.

U414 rattache uniquement le comportement existant Order Release à cette capacité. Construction, comparaison, maintien et préparation font partie de son mandat ; aucune liste de comportements additionnels n’est adoptée par analogie avec Inventory Planning.''',decomposition_rationale=rationale,market_comparisons=comparisons)
    newcap=dict(id='D03.p',revision=1,kind='capability',layer='transactional',fields=fields,source_refs=REFS,source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u414'),review=dict(state='partial',note='Nom, définition, nature Planning et parent D03 présentés et adoptés ; scope, finalité, justification développée et comparaisons éditoriaux.'),adoption_ids=[],lifecycle=life(fields,['name','definition','nature']))
    model['nodes'].append(newcap)
    nodes={n['id']:n for n in model['nodes']}
    release=nodes['BHV039']; oldparent=nodes['D04.o']; domain=nodes['D03']
    assert all('scope' not in n['lifecycle']['validated_fields'] for n in [release,oldparent,domain])
    release['fields']['scope']='\n\n'.join(p for p in release['fields']['scope'].split('\n\n') if not p.startswith('U413 :'))
    release['fields']['scope']+='\n\nU414 : Order Release est rattaché à Order Backlog Planning dans D03. Son identifiant et sa définition U410 sont conservés ; D04 garde les autres mutations de l’Order. Autorisation et réalisation physique restent distinctes.'
    for comp in release['fields'].get('market_comparisons',[]):
        comp['flow_position']='U414 : Order Release est un comportement d’Order Backlog Planning. Il autorise la prise en charge selon les conditions individuelles et collectives, distinctement de l’affectation et de Process Orchestration. Comparaison produit partielle ; rattachement U363 sous Lifecycle remplacé.'
    oldparent['fields']['scope']='\n\n'.join(p for p in oldparent['fields']['scope'].split('\n\n') if not p.startswith(('U410 :','U413 :')))
    oldparent['fields']['scope']=oldparent['fields']['scope'].replace('Les neuf comportements décrivent des mécanismes combinables, pas neuf états obligatoires : Drafting, Firming, Freezing, Release, Hold & Resume, Rescheduling, Cancellation, Closure et Splitting.','Les huit comportements décrivent des mécanismes combinables, pas huit états obligatoires : Drafting, Firming, Freezing, Hold & Resume, Rescheduling, Cancellation, Closure et Splitting.')
    oldparent['fields']['scope']+='\n\nU414 : Order Release BHV039 relève désormais d’Order Backlog Planning D03.p ; Lifecycle conserve les autres mutations. Split et Structuring restent inchangés jusqu’au prochain arbitrage. Les effets autorisés sur les Orders restent distincts de la coordination des services.'
    oldparent['fields']['decomposition_rationale']=oldparent['fields']['decomposition_rationale'].replace(', autorisation,', ',')
    domain['fields']['scope']='\n\n'.join(p for p in domain['fields']['scope'].split('\n\n') if not p.startswith('État de transition U413 :'))
    domain['fields']['scope']+='\n\nU414 : Order Backlog Planning D03.p porte le travail des scénarios et accueille Order Release BHV039, déplacé depuis Lifecycle avec son identité et sa définition conservées. Split et Structuring restent en D04 pour le réexamen de leur finalité ; aucun déplacement en bloc ni autre comportement Planning créé.'
    for n in [release,oldparent,domain]:
        n['revision']+=1;n['source_refs']=list(dict.fromkeys(n['source_refs']+REFS))
    moved=next(r for r in model['relations'] if r['id']=='REL-BEHAVIOR-BHV039')
    moved.update(source_id='D03.p',revision=moved['revision']+1,source_refs=list(dict.fromkeys(moved['source_refs']+['U414'])))
    moved['lifecycle']=life(moved,['type','source_id','target_id'])
    moved['review']=dict(state='accepted',note='U414 : déplacement explicite depuis D04.o vers D03.p ; identité et définition du comportement conservées, ancien rattachement capturé.')
    member=dict(id='REL-MEMBER-D03.p',revision=1,type='contains',source_id='D03',target_id='D03.p',source_refs=REFS,review=dict(state='accepted',note='U414 : capacité explicitement créée dans D03.'))
    member['lifecycle']=life(member,['type','source_id','target_id']);model['relations'].append(member)
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),adopted_capability=dict(id='D03.p',name=NAME,definition=DEFINITION,parent_id='D03'),moved_behavior=dict(id='BHV039',previous_parent='D04.o',parent_id='D03.p',relation_id=moved['id']),behaviors=[],delta={})
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in model[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},removed=sorted(old.keys()-new.keys()),changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]})
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['implementation_U414']=migration;audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest();audit['source_refs']=list(dict.fromkeys(audit['source_refs']+REFS))
    source_ids=[]
    next_id=max(int(s['id'][1:]) for s in audit['sources'])+1
    for comp in [comparisons[0],comparisons[1],comparisons[2]]:
        sid=f'S{next_id:02d}';next_id+=1;source_ids.append(sid)
        audit['sources'].append(dict(id=sid,vendor=comp['vendor'],native_label=comp['element_name'],native_id=None,url=comp['source_url'],edition=comp['source_version'],consulted_on='2026-09-19',locator=comp['source_locator'],nature='documentation',access='Source primaire consultée lors de la proposition U414.',observed_fact=comp['similarities'],limits=comp['differences'],reuse='Synthèse sélective et lien ; aucune importation substantielle.'))
    assessment=next(x for x in audit['assessments'] if x['capability_id']=='D04.o')
    assessment['existing_behaviors'].remove('BHV039');assessment['candidate_ids'].remove('P11')
    assessment.update(verdict='huit comportements après déplacement U414',diagnosis=oldparent['fields']['decomposition_rationale'],recommendation='U414 déplace Order Release vers Order Backlog Planning ; Split et Structuring restent à arbitrer sans transfert en bloc.')
    audit['assessments'].append(dict(capability_id='D03.p',name=NAME,existing_behaviors=['BHV039'],verdict='capacité et rattachement intégrés U414',diagnosis=rationale,recommendation='Aucun comportement additionnel adopté ; décisions spécialisées, affectation, promesse et orchestration conservent leurs responsabilités.',market_sources=source_ids,candidate_ids=['P11']))
    proposal=next(x for x in audit['candidates'] if x['id']=='P11')
    proposal.update(parent_id='D03.p',review_note='Intégré à BHV039 U410 ; comportement déplacé sous D03.p U414, sans duplication ni modification de sa définition.',source_refs=list(dict.fromkeys(proposal['source_refs']+['U414'])))
    existing=next(x for x in audit['existing_behavior_review'] if x['behavior_id']=='BHV039')
    existing.update(status='reparented_U414',recommendation='Nom/définition U410 conservés ; rattachement explicite à Order Backlog Planning D03.p adopté U414.')
    audit['order_backlog_U413'].update(status='planning_parent_integrated_U414_split_structuring_pending',note='D03.p créé et BHV039 déplacé U414 ; P11 demeure résolu. Split et Structuring restent en D04 à arbitrer.')
    save('modeles/backlog/behavior-gap-audit.yaml',audit)
    review['planning_U414']=dict(status='integrated',source_refs=REFS,capability_id='D03.p',adopted_name=NAME,adopted_definition=DEFINITION,parent_id='D03',behavior_id='BHV039',previous_behavior_parent='D04.o',decomposition_rationale=rationale,market_comparisons=comparisons,implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    review['status']='planning_integrated_split_structuring_pending'
    review['model_state']='138 nœuds, 47 capacités, 73 comportements. D03.p ajouté ; BHV039 déplacé sans duplication.'
    review['next_arbitration']='Distinguer découper la demande et organiser sa satisfaction : Order Splitting et Order Structuring restent en D04 avant cet arbitrage.'
    review['scope']='U413 : nom et direction adoptés. U414 : capacité D03.p et parent de BHV039 adoptés ; autres déplacements non décidés. Audit existant conservé.'
    for item in review['targeted_review']:
        if item['ids']==['BHV039']:
            item.update(status='integrated_U414',recommendation='Order Release déplacé vers D03.p Order Backlog Planning avec identité et définition conservées.',open_point='Rattachement résolu U414 ; seuils détaillés restent des règles de gestion.')
    review['source_refs']=list(dict.fromkeys(review['source_refs']+REFS));save('modeles/backlog/order-backlog-review.yaml',review)
    lifecycle=read(ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml')
    lifecycle['release_placement_U414']=dict(status='integrated',source_refs=REFS,behavior_id='BHV039',previous_parent='D04.o',parent_id='D03.p',definition_unchanged=True,note='Les accords U363/U410 restent historiques. Lifecycle conserve huit comportements ; Split et Structuring restent inchangés.')
    save('modeles/backlog/order-lifecycle-behaviors.yaml',lifecycle)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8')
    text=text.replace('Réexamen ciblé Lifecycle/Structuring : aucun déplacement en bloc ni parent précis adopté ; BHV039 reste sous D04.o en attendant cet arbitrage.', 'U414 crée Order Backlog Planning D03.p et y déplace Order Release BHV039, identité et définition conservées. Lifecycle garde huit comportements ; Split et Structuring restent en D04 à arbitrer.')
    text=text.replace('**Order Release (U410)**', '**Order Release (U410/U414)**')
    text=text.replace('P11 intégré au comportement existant, sans comportement autonome.', 'P11 intégré au comportement existant, désormais sous Order Backlog Planning D03.p (U414). Planning mobilise les décisions et prépare l’engagement ; il ne reprend ni affectation, ni promesse, ni orchestration. Aucun autre comportement Planning créé par analogie.')
    agents.write_text(text,encoding='utf-8')
    append('marche/elements.md','### ELM247\n\nOracle Backlog Planning 26B / Key Actions on Orders 25D et Microsoft Planned Orders simplified (mise à jour 3 octobre 2025), pages primaires consultées le 19 septembre 2026. URL et passages dans modeles/backlog/order-backlog-review.yaml, planning_U414.market_comparisons. Travail sur les scénarios et propositions distinct de leur calcul ; aucune taxonomie universelle ni preuve installée Beaumanoir.')
    append('marche/comparaisons.md','### CMP158\n\nU414 — Order Backlog Planning D03.p mobilise les décisions pour travailler les scénarios et préparer la part engagée. Appui lexical Oracle Backlog Planning, appui pratique Microsoft sur les Planned Orders. Oracle transmet des résultats à Order Management ; FLOW rattache son autorisation de prise en charge Order Release à Planning sans assimiler les deux opérations. Le comportement BHV039 est déplacé, pas dupliqué ; sa définition U410 reste inchangée. Supply Assignment applique les affectations, Promise Management gère les engagements, Process Orchestration coordonne les services. Aucun transfert automatique de Split ou Structuring, ni liste de comportements Planning déduite du produit.')
    append('JOURNAL.md','## 2026-09-19 — U414 : Order Backlog Planning et Order Release\n\nD03.p créé avec nom/définition présentés ; parent D03 adopté. BHV039 déplacé depuis D04.o en conservant son identifiant et sa définition. Lifecycle garde huit comportements ; Split et Structuring inchangés. Justification de décomposition, comparaisons Oracle/Microsoft ELM247/CMP158, audit existant et AGENTS actualisés. Aucune release.')
    (OUT/'README.md').write_text('# U414 — Order Backlog Planning\n\nD03.p créé ; BHV039 déplacé sous cette capacité, identité et définition conservées. Captures et empreintes dans implementation.yaml. Split et Structuring restent en D04 ; aucune release.\n',encoding='utf-8')
    print('U414 integrated: D03.p created; existing BHV039 moved; 47 capabilities / 73 behaviors.')


if __name__=='__main__':
    main()
