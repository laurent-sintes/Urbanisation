"""Apply the three CTP mechanisms approved by Laurent; continue the existing audit."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/ctp-behaviors-U402'
REFS = ['U402', 'ELM241', 'CMP152']


def main():
    assert not OUT.exists(), 'Preserve integration evidence.'
    mp = ROOT/'modeles/backlog/model.yaml'
    before = read(mp); model = deepcopy(before)
    ap = 'modeles/backlog/behavior-gap-audit.yaml'; audit = read(ROOT/ap)
    ids = ['BHV075', 'BHV076', 'BHV077']
    assert not set(ids) & {n['id'] for n in model['nodes']}
    assert '## U402\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    parent = next(n for n in model['nodes'] if n['id']=='D03.j')
    assert not any(r['type']=='contains' and r['source_id']==parent['id'] for r in model['relations'])
    assert not set(['scope','decomposition_rationale','market_comparisons']) & set(parent['lifecycle']['validated_fields'])
    append('connaissance/01-contributions-utilisateur.md', '''## U402

**id**

U402

**date**

2026-09-18

**titre**

Adopter les trois mécanismes de faisabilité sous adaptation de CTP

**texte**

Go

**contexte et portée**

Après « next », accord sur Additional Supply Feasibility, Fulfillment Alternative Feasibility et Commitment Rebalancing Feasibility, les responsabilités et exemples présentés, et leur rattachement à CTP. Trois leviers combinables : obtenir davantage de ressources, changer la solution de satisfaction, réexaminer des engagements existants. CTP établit possibilités et conséquences ; Fulfillment Plan Decision détermine le scénario collectif maximisant la valeur multidimensionnelle ; Supply Assignment applique les affectations et Promise Management les modifications autorisées de promesse. Une alternative déjà admissible dans la référence reste dans ATP ; aucun retrait implicite de garanties ou gel. Les intitulés sont des formulations FLOW appuyées par des mécanismes Microsoft/SAP, pas une taxonomie universelle CTP. L’accord ne valide pas globalement les compléments éditoriaux, paramètres, contrats de dépendance ou comparaisons marché. Poursuite de l’audit existant, aucune release.''')
    OUT.mkdir()
    for path, name in [(mp,'model-before.yaml'), (ROOT/ap,'behavior-gap-audit-before.yaml'),
                       (ROOT/'modeles/backlog/d03-review.yaml','d03-review-before.yaml')]:
        (OUT/name).write_bytes(path.read_bytes())
    boundary = ('[CTP](model:D03.j) établit les possibilités sous adaptation et leurs conséquences. '
        '[Fulfillment Plan Decision](model:D03.o) détermine le scénario collectif cohérent maximisant la valeur multidimensionnelle, '
        'en mobilisant les décisions spécialisées. [Supply Assignment](model:D02.e) applique les affectations retenues ; '
        '[Promise Management](model:D03.n) porte les modifications autorisées de promesse. '
        'Le résultat de faisabilité ne réserve pas, ne modifie pas un Order ou une politique et ne déclenche pas l’exécution. '
        'Les trois comportements peuvent se combiner sans séquence imposée.')
    rationale = ('Distinguer trois leviers métier : obtenir davantage de ressources, changer la solution de satisfaction, '
        'ou réexaminer des engagements existants. Les conditions, les parties concernées et les conséquences diffèrent réellement. '
        'La décomposition rend explicite ce qui doit changer pour rendre une commande satisfaisable, sans confondre faisabilité, '
        'choix collectif et application. Plusieurs leviers peuvent se combiner.')
    entries = [dict(id=ids[0], candidate='P14', source='S07', name='Additional Supply Feasibility',
        definition='Les possibilités de satisfaire la demande en obtenant des ressources supplémentaires, avec quantités, dates et conditions de disponibilité.',
        example='Il manque 40 pièces : un apport fournisseur supplémentaire pourrait les rendre disponibles vendredi.',
        finality='Expliciter les apports supplémentaires qui rendraient la commande satisfaisable et les conditions nécessaires avant engagement.',
        detail='Un arrivage déjà prévu et admissible dans la situation de référence reste pris en compte par ATP. Ici, l’apport supplémentaire est une hypothèse à rendre réalisable. La capacité ne crée pas l’achat ou la demande d’apport ; elle ne suppose pas une acquisition quand le régime est consigné. Le fournisseur ou l’exécutant concerné fournit les possibilités utiles. Replenishment Decision conserve l’objectif d’optimisation du stock ; tout apport pour satisfaire un Order ne passe pas nécessairement par cette décision.'),
        dict(id=ids[1], candidate='P15', source='S05', name='Fulfillment Alternative Feasibility',
        definition='Les possibilités obtenues en modifiant les modalités de satisfaction par rapport à la situation de référence.',
        example='La livraison standard ne permet pas de respecter la date ; une prestation express pourrait le permettre, sous réserve de sa disponibilité et de son autorisation.',
        finality='Rendre visibles les solutions de satisfaction nécessitant une adaptation, leurs conditions et leurs effets sur le service attendu.',
        detail='Un autre magasin déjà admissible dans la référence relève d’ATP : le caractère alternatif ne suffit pas à classer une option dans CTP. Une substitution de produit exige une équivalence autorisée ; proximité de taille, couleur ou apparence ne vaut pas acceptabilité. Execution Service Decision et Execution Capacity Visibility conservent respectivement choix de service et information de capacité contextualisée. CTP exploite leurs résultats sans créer une seconde décision de service. Un changement de date déjà possible dans la référence ne devient pas automatiquement CTP.'),
        dict(id=ids[2], candidate='P16', source='S06', name='Commitment Rebalancing Feasibility',
        definition='Les possibilités obtenues en révisant des engagements modifiables, en explicitant les conséquences sur les commandes concernées.',
        example='Une commande urgente pourrait être satisfaite si une autre accepte un décalage de deux jours ; les engagements gelés restent préservés.',
        finality='Rendre visibles les possibilités et conséquences croisées d’une révision d’engagements avant l’arbitrage collectif.',
        detail='CTP ne choisit pas seul quelle commande sacrifier. Il explicite les possibilités et impacts permettant à Fulfillment Plan Decision d’arbitrer, avec Order Prioritization, PTP et les autres décisions utiles. La modifiabilité est une condition à établir, non une autorisation déduite de l’urgence. Une même ressource ne peut soutenir des possibilités collectivement incompatibles. Réservation opposable et gel restent respectés ; aucune libération ou révision implicite. Promise Revision conserve la modification autorisée de l’engagement et Supply Reassignment l’application des liens révisés.')]
    evidence = {
        'S07': dict(product='Dynamics 365 Supply Chain Management / Planning Optimization',
            finding='CTP vérifie matières et capacités pour déterminer les dates réalisables, notamment pour assembler ou produire à la demande.',
            difference='Appui au mécanisme d’apport supplémentaire ; le CTP FLOW est plus large que ce cas de fabrication. Aucun processus de production interne FLOW ni équivalence de taxonomie déduit.',
            locator='How CTP compares to ATP ; exemple de fabrication de A à partir de B et C'),
        'S05': dict(product='SAP S/4HANA aATP',
            finding='Alternative-Based Confirmation examine des sites alternatifs et des produits de substitution selon des règles.',
            difference='SAP expose ABC sous aATP. FLOW distingue alternatives déjà admissibles (ATP) et adaptations de la référence (CTP). L’exemple express est une illustration FLOW ; cette page ne prouve pas un mécanisme ABC de choix de transport express.',
            locator='Advanced ATP Scenario: Alternative-Based Confirmation (ABC)'),
        'S06': dict(product='SAP S/4HANA Cloud Public Edition / Backorder Processing',
            finding='BOP réexamine les confirmations selon disponibilités et priorités, avec stratégies de préservation, amélioration et redistribution.',
            difference='Le processus SAP traverse plusieurs responsabilités FLOW : faisabilité CTP, décision collective, priorités, révision de promesse et application des affectations. BOP ne correspond pas à un comportement CTP unique ni à une autorité de CTP pour choisir les perdants.',
            locator='Backorder Processing Overview ; Confirmation Strategies'),
    }
    sources = []
    for sid in ['S07','S05','S06']:
        s = deepcopy(next(s for s in audit['sources'] if s['id']==sid))
        s['consulted_on']='2026-09-18'; s['access']='Texte primaire ouvert et consulté avant la proposition approuvée U402.'
        s['locator']=evidence[sid]['locator']; s['observed_fact']=evidence[sid]['finding']; s['limits']=evidence[sid]['difference']
        if sid=='S07': s['edition']='Documentation évolutive ; mise à jour affichée 2026-07-27'
        sources.append(s)
    def comparison(sid):
        s=next(s for s in sources if s['id']==sid); e=evidence[sid]
        return dict(vendor=s['vendor'],product=e['product'],element_name=s['native_label'],element_type='Mécanisme ou processus produit',
            relationship='Recouvrement partiel',similarities=e['finding'],differences=e['difference'],
            flow_position='Trois mécanismes combinables sous CTP, noms FLOW ; faisabilité distincte du scénario collectif et de sa mise en application.',
            source_title=s['native_label'],source_url=s['url'],source_version=s['edition'],source_locator=s['locator'],
            consulted_on=s['consulted_on'],evidence_limits='Texte primaire consulté ; aucune taxonomie universelle ni preuve de déploiement Beaumanoir.',
            status='proposed',source_refs=REFS)
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def lifecycle(values, fields):
        return dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U402'],
            validated_fields=fields,value_sha256={f:value_hash(values[f]) for f in fields},
            note='U402 : noms, responsabilités présentées et rattachements adoptés ; descriptions développées et comparaisons qualifiées séparément.')
    parent['fields']['decomposition_rationale']=rationale
    parent['fields']['scope']+='\n\nU402 : '+', '.join('['+e['name']+'](model:'+e['id']+')' for e in entries)+'. '+boundary
    parent['fields']['market_comparisons']=[comparison(sid) for sid in ['S07','S05','S06']]
    parent['revision']+=1; parent['source_refs']=list(dict.fromkeys(parent['source_refs']+REFS))
    parent['review']['note']+=' U402 : trois mécanismes adoptés, détails éditoriaux et correspondances marché distincts.'
    adoptions=[]
    for entry in entries:
        fields=dict(name=entry['name'],definition=entry['definition'],finality=entry['finality'],
            scope=entry['detail']+'\n\nExemple fictif : '+entry['example']+'\n\n'+boundary+' Aucune pratique installée chez Beaumanoir déduite de cet exemple.',
            market_comparisons=[comparison(entry['source'])])
        node=dict(id=entry['id'],revision=1,kind='behavior',layer=parent['layer'],fields=fields,source_refs=REFS,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u402'),adoption_ids=[],
            review=dict(state='partial',note='Nom, définition présentée et parent adoptés ; descriptions développées et comparaison éditoriales.'),
            lifecycle=lifecycle(fields,['name','definition']))
        relation=dict(id='REL-BEHAVIOR-'+entry['id'],revision=1,type='contains',source_id=parent['id'],target_id=entry['id'],
            source_refs=REFS,review=dict(state='accepted',note='Parent CTP adopté U402.'))
        relation['lifecycle']=lifecycle(relation,['type','source_id','target_id'])
        model['nodes'].append(node); model['relations'].append(relation)
        adoptions.append(dict(node_id=node['id'],parent_id=parent['id'],adopted_fields=['name','definition'],value_sha256=node['lifecycle']['value_sha256']))
    new={n['id']:n for n in model['nodes']}
    for old in before['nodes']:
        for field in old.get('lifecycle',{}).get('validated_fields',[]):
            assert new[old['id']]['fields'][field]==old['fields'][field]
    assert model['relations'][:len(before['relations'])]==before['relations']
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},adopted_behaviors=adoptions,behaviors=[])
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]}; new={x['id']:x for x in model[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(old.keys()&new.keys()) if old[i]!=new[i]},removed=sorted(old.keys()-new.keys()))
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit['source_refs'].extend(REFS); audit['implementation_U402']=migration
    audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    for entry in entries:
        p=next(p for p in audit['candidates'] if p['id']==entry['candidate'])
        p.update(status='implemented_U402',implemented_as=entry['id'],review_note='U402 : nom, responsabilité présentée et parent CTP adoptés ; formulation initiale conservée pour provenance. Frontière avec Fulfillment Plan Decision explicitée dans d03-review.yaml.')
        audit['existing_behavior_review'].append(dict(behavior_id=entry['id'],status='integrated_U402',market_sources=[entry['source']],
            recommendation='Mécanisme CTP adopté ; comparaison datée ELM241/CMP152 dans la fiche. Aucune modification transactionnelle implicite.'))
    assessment=next(x for x in audit['assessments'] if x['capability_id']=='D03.j')
    assessment.update(existing_behaviors=ids,verdict='mécanismes intégrés U402',diagnosis=rationale,
        recommendation='Trois mécanismes combinables de faisabilité ; Fulfillment Plan Decision choisit le scénario collectif. Paramètres et autorisations détaillés ne bloquent pas le catalogue adopté.')
    synthesis=audit['current_synthesis_U298']
    synthesis['conditional_candidate_ids']=[i for i in synthesis['conditional_candidate_ids'] if i not in ['P14','P15','P16']]
    synthesis['implemented_candidate_ids'].extend(['P14','P15','P16'])
    synthesis['source_refs'].append('U402')
    synthesis['next_step']='CTP P14–P16 intégré U402. Poursuivre les autres points de l’audit existant, notamment engagement fournisseur et exécution ; ne pas réactiver P01/P02 suspendus U324 ni ouvrir un nouvel audit.'
    for arbitration in audit['arbitrations']:
        if arbitration['id']=='A01':
            arbitration['limit']='Les règles et contrats de réservation restent à préciser. U402 adopte P16 sans libération implicite des garanties ; sa création n’est plus conditionnelle à ces règles détaillées.'
        if arbitration['id']=='A05':
            arbitration.update(status='catalogue_boundary_resolved_U402',recommendation='Référence ATP et adaptation CTP distinguées U402 ; BHV076 décrit la faisabilité sous adaptation. Les listes d’options, équivalences autorisées et paramètres relèvent des règles à préciser.',
                limit='La frontière de catalogue est adoptée ; aucune substitution de taille/couleur ni administration des équivalences attribuée implicitement au Product Reference.')
    save(ap,audit)
    path='modeles/backlog/d03-review.yaml'; d03=read(ROOT/path)
    d03['ctp_behaviors_U402']=dict(status='integrated',source_refs=REFS,parent_id=parent['id'],behavior_ids=ids,
        entries=entries,boundary=boundary,decomposition_rationale=rationale,sources=sources,
        adoption_scope='Noms, responsabilités présentées, exemples et parent adoptés. Finalités, descriptions développées et correspondances gardent leur qualification éditoriale.',
        implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    save(path,d03)
    append('marche/elements.md', '''### ELM241

18 septembre 2026 — relecture ciblée avant U402 de trois textes primaires : Microsoft Dynamics 365 SCM, Calculate sales order delivery dates using CTP (page mise à jour 2026-07-27, How CTP compares to ATP) ; SAP Learning S/4HANA, Using Advanced Available-To-Promise (aATP), section Alternative-Based Confirmation ; SAP Learning S/4HANA Cloud Public Edition, Exploring Backorder Processing, sections Overview et Confirmation Strategies. URL, éditions, constats, passages et limites dans modeles/backlog/d03-review.yaml, ctp_behaviors_U402.sources (S07, S05, S06).

Nature : mécanismes et processus produit. Appuis à la faisabilité par apports supplémentaires, alternatives de satisfaction et réexamen d’engagements. Les frontières éditeurs diffèrent de FLOW ; aucune taxonomie universelle de trois comportements CTP ni déploiement Beaumanoir démontré. Synthèses sélectives, aucune reproduction intégrale.''')
    append('marche/comparaisons.md', '''### CMP152

U402 — Codex, 18 septembre 2026. ELM241 comparé à D03.j et BHV075–077 du backlog. Noms et responsabilités présentées des trois comportements adoptés par Laurent ; correspondances marché éditoriales qualifiées séparément. Microsoft CTP apporte un appui partiel à la faisabilité de ressources supplémentaires, notamment fabrication ; FLOW couvre plus largement les adaptations supply. SAP ABC apporte un appui aux alternatives, mais une option déjà admissible reste dans ATP FLOW. SAP BOP traverse CTP, décision collective, priorités, révision de promesse et application des affectations ; ce n’est pas un synonyme du troisième comportement.

Le bénéfice est de rendre lisibles trois leviers combinables aux conditions et conséquences distinctes. CTP établit les possibilités et impacts, Fulfillment Plan Decision choisit le scénario collectif ; Supply Assignment et Promise Management appliquent leurs effets respectifs. Intitulés FLOW, pas labels de taxonomie CTP revendiqués au marché. L’exemple express est une illustration FLOW, non une fonctionnalité ABC établie par la source. Aucun engagement ou gel levé par hypothèse.''')
    append('JOURNAL.md', '''## 2026-09-18 — U402 : mécanismes CTP intégrés

Additional Supply Feasibility, Fulfillment Alternative Feasibility et Commitment Rebalancing Feasibility ajoutés sous CTP (BHV075–077), avec descriptions, exemples, justification et comparaisons Microsoft/SAP. Sources primaires reconsultées avant la proposition, tracées ELM241/CMP152. P14–P16 marqués intégrés dans l’audit existant ; frontière de catalogue A05 clarifiée, règles détaillées distinctes. Aucun changement des champs précédemment validés ni des relations métier existantes. Captures et empreintes dans modeles/backlog/history/ctp-behaviors-U402 ; aucune release.''')
    (OUT/'README.md').write_text('# U402 — preuve d’intégration\n\nTrois comportements CTP approuvés ; poursuite de l’audit existant. Capture antérieure et empreintes dans implementation.yaml. Noms, responsabilités et parents adoptés ; enrichissements éditoriaux qualifiés séparément.\n',encoding='utf-8')
    print('U402 integrated: 3 CTP behaviors; previous approved fields and relations preserved.')


if __name__=='__main__':
    main()
