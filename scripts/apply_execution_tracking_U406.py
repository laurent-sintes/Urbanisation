"""Integrate the approved execution visibility behaviors and process tracking."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT=ROOT/'modeles/backlog/history/execution-tracking-U406'
REFS=['U305','U308','U404','U405','U406','ELM243','CMP154']


def main():
    assert not OUT.exists()
    mp=ROOT/'modeles/backlog/model.yaml'; before=read(mp); model=deepcopy(before)
    ap='modeles/backlog/behavior-gap-audit.yaml'; audit=read(ROOT/ap)
    ids=['BHV079','BHV080','BHV081','BHV082']
    assert not set(ids)&{n['id'] for n in model['nodes']}
    parent=next(n for n in model['nodes'] if n['id']=='D07.d')
    assert not any(r['type']=='contains' and r['source_id']==parent['id'] for r in model['relations'])
    assert not set(['scope','decomposition_rationale','market_comparisons'])&set(parent['lifecycle']['validated_fields'])
    contributions=[('U404','Préférer Business Process Tracking','Je pense Business Process Tracking est bien meilleur.',
        'Préférence explicite pour le nom de marché Microsoft, en remplacement du candidat Digital Service Visibility. La réponse propose un point de vue transversal sur les processus d’exécution Supply, complémentaire des trois visibilités physiques ; pas un élargissement au pilotage global Business Services.'),
        ('U405','Relier le suivi des Tasks aux appels de services sous-jacents',"Le tracking de Task implique le tracking des appels de service sous jacents. Donc c'est encore mieux",
        'La Task métier devient un point d’entrée du suivi, reliée aux appels et prestations qui contribuent à sa réalisation. Ne pas confondre appel accepté, résultat métier acquis, Task terminée et processus complet. Les Tasks et appels sont des objets suivis, pas des niveaux de décomposition supplémentaires.'),
        ('U406','Adopter Business Process Tracking avec suivi des Tasks et appels','Go',
        'Accord sur Business Process Tracking, la définition présentée intégrant processus, Tasks métier, prestations et appels sous-jacents, les exemples et le rattachement direct à Execution Tracking. La réussite technique n’implique pas le résultat métier ni la fin du processus. Périmètre processus d’exécution Supply ; orchestration et adaptation distinctes. Les trois visibilités physiques déjà adoptées U305/U308 sont à matérialiser au même niveau, sans Logistics Visibility intermédiaire. Digital Service Visibility demeure une ancienne proposition remplacée ; aucun comportement autonome supplémentaire ni objet Task créé par extension. Comparaisons et compléments rédactionnels qualifiés séparément, aucune release.')]
    for ident,title,verbatim,scope in contributions:
        assert f'## {ident}\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        append('connaissance/01-contributions-utilisateur.md',f'## {ident}\n\n**id**\n\n{ident}\n\n**date**\n\n2026-09-19\n\n**titre**\n\n{title}\n\n**texte**\n\n{verbatim}\n\n**contexte et portée**\n\n{scope}')
    OUT.mkdir()
    rp='modeles/backlog/execution-services-review.yaml'
    for path,name in [(mp,'model-before.yaml'),(ROOT/ap,'behavior-gap-audit-before.yaml'),(ROOT/rp,'execution-review-before.yaml')]:
        (OUT/name).write_bytes(path.read_bytes())
    historical=audit['adoption_U305']['values']['behaviors']
    bpt_definition='Suivre l’avancement des processus d’exécution Supply et de leurs Tasks métier, en reliant chaque Task aux prestations et appels de services qui contribuent à sa réalisation, pour rendre explicites les résultats acquis, les attentes, les échecs et leurs conséquences sur la progression.'
    common='Les quatre comportements sont directement rattachés à Execution Tracking. Les visibilités physiques et le suivi du processus sont des perspectives complémentaires et peuvent utiliser les mêmes faits. Logistics Visibility reste une notion englobante, sans niveau supplémentaire. Les faits, estimations et engagements restent distincts, avec origine et fraîcheur. Le suivi porte aussi sur la progression normale, pas seulement les exceptions. Une information manquante ne prouve pas qu’une opération n’a pas eu lieu. Les exécutants gardent leurs opérations internes ; Inventory Management enregistre les effets sur le stock. Orchestration coordonne la suite et Execution Adaptation Decision détermine les adaptations ; le tracking ne les décide pas. Aucun temps réel uniforme ni architecture d’instrumentation imposés.'
    entries=[
        dict(id=ids[0],name='Warehouse Visibility',definition=historical[0]['scope'],approved_by=['U305'],sources=['S44'],
            finality='Comprendre la situation des marchandises et l’avancement de leur traitement dans les entrepôts et plateformes.',
            scope='Suivre réception, manutention, rangement, préparation et expédition à partir des faits communiqués par l’exécutant. Relier biens ou unités logistiques, opérations et prestations concernées. Les traces numériques d’une opération physique peuvent alimenter cette vue sans transformer l’opération en prestation numérique.\n\nExemple fictif : sur 100 pièces attendues, 80 sont préparées et 20 restent à traiter ; la préparation partielle ne signifie pas que les 80 pièces ont déjà quitté le site. Les retards et anomalies sont visibles avec la progression normale.'),
        dict(id=ids[1],name='Transportation Visibility',definition=historical[1]['scope'],approved_by=['U305'],sources=['S35'],
            finality='Connaître la progression des acheminements et les arrivées attendues, en distinguant estimation et remise constatée.',
            scope='Suivre départs, étapes d’acheminement, localisation connue, retards, estimations d’arrivée et remise au destinataire. Conserver la continuité entre segments utiles, sans présumer une localisation continue ou une précision uniforme.\n\nExemple fictif : un camion est en route avec une arrivée estimée à 14 h ; cette estimation n’est ni une preuve de livraison ni une réception magasin réalisée. La suite des opérations au magasin est visible dans Store Visibility.'),
        dict(id=ids[2],name='Store Visibility',definition=audit['adoption_U308']['values']['scope'],approved_by=['U305','U308'],sources=['S46'],
            finality='Distinguer marchandise livrée, reçue, en réserve et rendue accessible au client, afin d’expliquer les attentes de mise en rayon.',
            scope='Rendre visibles réception magasin, passage en réserve, mise en rayon et réassort de la surface de vente. Le périmètre adopté ne s’étend pas à toutes les ventes ou à l’ensemble de l’activité du magasin.\n\nExemple fictif : 100 pièces sont reçues, 60 restent en réserve et 40 sont mises en rayon. Livré au magasin ne signifie pas accessible au client ; une rupture en rayon peut coexister avec du stock en réserve. La vue décrit les opérations et leur progression, sans remplacer Inventory Visibility ni décider les seuils de réassort.'),
        dict(id=ids[3],name='Business Process Tracking',definition=bpt_definition,approved_by=['U406'],sources=['S49','S48','S50'],
            finality='Comprendre où en est un traitement métier, les résultats acquis et ce qui conditionne sa progression, jusqu’aux appels de services associés aux Tasks.',
            scope='''**Point d’entrée métier.** Suivre le processus d’exécution Supply et ses Tasks métier, en les reliant aux commandes, documents et prestations concernés. Une Task peut mobiliser plusieurs services ; la corrélation ne suppose ni un appel unique ni une correspondance un pour un. Les actions humaines peuvent contribuer au résultat de la Task sans être assimilées à des appels informatiques.

**Exemple : produire les documents d’expédition.** La Task mobilise des services pour récupérer les données, produire le document, le déposer et notifier sa disponibilité. Le tracking relie sollicitations, prises en charge connues, réponses, résultats et tentatives à cette Task. Si la production du document a abouti mais que son dépôt reste en attente, il devient possible de comprendre ce qui manque au résultat attendu, selon les conditions de fin définies pour la Task. Cet exemple ne prescrit pas un workflow universel.

**Trois distinctions essentielles.** Un appel accepté ne signifie pas que la prestation est terminée. Des appels techniquement réussis ne garantissent pas le résultat métier attendu. Une Task terminée ne signifie pas que le processus complet est terminé. Une nouvelle tentative reste reliée à la demande d’origine ; absence de réponse ne vaut pas refus. Le suivi expose les faits et les résultats connus, sans inventer l’état d’un service externe.

**Exemple : contrôle antifraude.** Le contrôle a répondu avec une suspicion : la prestation numérique peut être terminée alors que la commande reste en attente d’une décision. Le tracking rend explicite cette différence ; il ne décide pas d’accepter le risque. De même, la vérification d’identité ou de code-barres et la production documentaire restent visibles dans leur contexte métier, sans comportement autonome par service.

**Lecture transversale.** Pour une commande, on peut constater le contrôle terminé, une décision attendue, le document non encore produit et la préparation physique terminée. Les vues Warehouse, Transportation et Store éclairent les opérations physiques ; Business Process Tracking explique leur articulation avec les Tasks et conditions connues de progression. Les faits peuvent être partagés sans duplication de responsabilité.

**Frontières de modèle.** Les Tasks, prestations et appels de services sont des objets suivis ; ils ne créent aucun niveau sous Comportement. Aucun nouvel objet de catalogue, cardinalité ou relation de possession n’est imposé par cette description. Le périmètre est celui des processus d’exécution Supply ; le pilotage global des processus Business Services reste distinct. Le nom Digital Service Visibility est remplacé : son besoin de visibilité explicite demeure inclus ici, sans conserver un cinquième comportement. Les exemples sont fictifs et ne prouvent aucun existant Beaumanoir.''')]
    sources=[]
    for sid in ['S44','S35','S46','S49','S48','S50']:
        source=deepcopy(next(s for s in audit['sources'] if s['id']==sid))
        source['consulted_on']='2026-09-19';source['access']='Texte primaire ouvert et consulté ; synthèse sélective.'
        if sid=='S35':source['edition']='Article éditeur du 22 août 2023 ; édition logicielle non indiquée'
        if sid=='S46':source['limits']='Présentation produit : réception et disponibilité en rayon documentées ; Store Visibility est le nom FLOW adopté par cohérence, pas une taxonomie éditeur démontrée.'
        if sid=='S49':
            source['edition']='Azure Business Process Tracking ; page mise à jour 2025-09-11'
            source['limits']='Le produit documenté mappe des étapes métier sur les opérations des workflows Standard stateful Logic Apps. FLOW retient le concept de suivi métier ; le lien Task/appels est sa convention, sans équivalence un pour un ni obligation Azure.'
        if sid=='S50':source['limits']='Présentation commerciale de Process Observability, incluant des moyens d’intervention et d’analyse plus larges que le tracking FLOW. Ne prouve pas une collecte exhaustive de tout service externe.'
        sources.append(source)
    def comparison(sid):
        s=next(s for s in sources if s['id']==sid)
        return dict(vendor=s['vendor'],product=s['edition'],element_name=s['native_label'],element_type=s['nature'],relationship='Recouvrement partiel',
            similarities=s['observed_fact'],differences=s['limits'],flow_position='Quatre perspectives de tracking complémentaires sous Execution Tracking ; visibilité physique et suivi métier jusqu’aux appels des Tasks. Suivre reste distinct de décider et d’orchestrer.',
            source_title=s['native_label'],source_url=s['url'],source_version=s['edition'],source_locator=s['locator'],consulted_on=s['consulted_on'],
            evidence_limits=s['access']+' Aucune couverture installée Beaumanoir déduite.',status='proposed',source_refs=REFS)
    stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def life(values,fields,approvals):
        return dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=approvals,validated_fields=fields,
            value_sha256={f:value_hash(values[f]) for f in fields},note='Intégration U406. Les définitions physiques reprennent exactement les périmètres adoptés U305/U308 ; nom et définition Business Process Tracking adoptés U406. Descriptions développées et comparaisons éditoriales.')
    adoptions=[]
    for e in entries:
        fields=dict(name=e['name'],definition=e['definition'],finality=e['finality'],scope=e['scope']+'\n\n'+common,market_comparisons=[comparison(s) for s in e['sources']])
        node=dict(id=e['id'],revision=1,kind='behavior',layer=parent['layer'],fields=fields,source_refs=REFS,adoption_ids=[],
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor=e['approved_by'][-1].lower()),
            review=dict(state='partial',note='Nom, responsabilité présentée et parent adoptés ; détails éditoriaux distincts.'),lifecycle=life(fields,['name','definition'],e['approved_by']))
        rel=dict(id='REL-BEHAVIOR-'+e['id'],revision=1,type='contains',source_id=parent['id'],target_id=e['id'],source_refs=REFS,
            review=dict(state='accepted',note='Rattachement direct adopté, sans niveau intermédiaire.'))
        rel['lifecycle']=life(rel,['type','source_id','target_id'],e['approved_by'])
        model['nodes'].append(node);model['relations'].append(rel)
        adoptions.append(dict(node_id=e['id'],parent_id=parent['id'],adopted_fields=['name','definition'],value_sha256=node['lifecycle']['value_sha256'],approved_by=e['approved_by']))
    rationale='Les trois périmètres physiques rendent lisibles les situations et opérations propres à l’entrepôt, au transport et au magasin ; livré ne signifie pas mis en rayon. Le suivi transversal des processus explique les résultats, attentes et blocages métier en reliant Tasks et appels sous-jacents. Ce sont des perspectives combinables aux bénéfices distincts, sans sous-comportements ni découpage par bouton, interface ou fournisseur.'
    parent['fields']['decomposition_rationale']=rationale
    parent['fields']['scope']+='\n\nU406 : '+', '.join('['+e['name']+'](model:'+e['id']+')' for e in entries)+'. '+common+' Business Process Tracking conserve la visibilité explicite des prestations numériques, de leurs résultats et de leurs contributions aux Tasks.'
    parent['fields']['market_comparisons']=[comparison(s['id']) for s in sources]
    parent['revision']+=1;parent['source_refs']=list(dict.fromkeys(parent['source_refs']+REFS));parent['review']['note']+=' U406 : quatre comportements intégrés, portées U305/U308 et U406 distinguées.'
    new={n['id']:n for n in model['nodes']}
    for old in before['nodes']:
        for f in old.get('lifecycle',{}).get('validated_fields',[]):assert new[old['id']]['fields'][f]==old['fields'][f]
    assert model['relations'][:-4]==before['relations']
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},adopted_behaviors=adoptions,behaviors=[])
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in model[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},removed=sorted(old.keys()-new.keys()))
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit['source_refs']=list(dict.fromkeys(audit['source_refs']+REFS));audit['implementation_U406']=migration;audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(a for a in audit['assessments'] if a['capability_id']==parent['id'])
    assessment.update(existing_behaviors=ids,verdict='quatre comportements intégrés U406',diagnosis=rationale,recommendation='Trois perspectives physiques et Business Process Tracking jusqu’aux Tasks/appels ; pas de cinquième Digital Service Visibility ni de doublon pour les exceptions. P10 reste à réexaminer sans présomption de création.')
    for e in entries:audit['existing_behavior_review'].append(dict(behavior_id=e['id'],status='integrated_U406',market_sources=e['sources'],recommendation='Nom, périmètre et parent intégrés selon les accords ; compléments éditoriaux et comparaisons ELM243/CMP154 dans la fiche.'))
    for key in ['adoption_U305','adoption_U308']:
        audit[key]['implementation_status']='Nœuds BHV079–081 intégrés U406 ; valeurs et empreintes de l’accord historique préservées. Aucune publication.'
    audit['feedback_U306']['status']='superseded_by_Business_Process_Tracking_U406'
    audit['feedback_U306']['superseded_by']=dict(node_id='BHV082',source_refs=['U404','U405','U406'],note='Le besoin numérique est conservé dans le suivi des processus, Tasks et appels ; ancien nom proposé conservé pour provenance.')
    save(ap,audit)
    review=read(ROOT/rp);review['source_refs']=list(dict.fromkeys(review['source_refs']+REFS))
    review['tracking_U406']=dict(status='integrated',source_refs=REFS,parent_id=parent['id'],entries=entries,common_boundaries=common,decomposition_rationale=rationale,sources=sources,
        interpretation='Tasks et appels sont des objets suivis, sans nouveau niveau descriptif ni ajout automatique d’objets de catalogue. Les trois accords physiques sont matérialisés ; le candidat Digital Service Visibility est remplacé.',
        implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    save(rp,review)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8');marker='D14 décrit l’offre des services exécutants'
    assert marker in text
    text=text.replace(marker,'**Execution Tracking (U305/U308/U406)** : Warehouse Visibility, Transportation Visibility, Store Visibility et Business Process Tracking sont quatre comportements directs. Le dernier relie processus d’exécution Supply, Tasks et appels de services ; ceux-ci sont des objets suivis, pas de nouveaux niveaux. Appel accepté, réussite technique, résultat métier, fin de Task et fin de processus restent distincts. Digital Service Visibility est remplacé ; son besoin demeure inclus. Portées et comparaison : `modeles/backlog/execution-services-review.yaml`, `tracking_U406`.\n\n'+marker,1)
    agents.write_text(text,encoding='utf-8')
    append('marche/elements.md','''### ELM243

19 septembre 2026 — sources primaires consultées : Microsoft Azure Business Process Tracking (conception, identifiant métier et mapping d’étapes), Logic Apps Run History (statuts/actions/résultats), Camunda Process Observability (instances et contexte métier). Relecture ciblée SAP EWM (flux entrants, internes, sortants et monitor), project44 (article du 22 août 2023, Transportation Visibility et ETA multimodal) et Blue Yonder Store Execution (réception directe en rayon et disponibilité).

URL, éditions, passages, constats et limites dans modeles/backlog/execution-services-review.yaml, tracking_U406.sources. Documentation ou présentation éditeur, sans preuve Beaumanoir. Microsoft apporte le nom et un mécanisme de corrélation ; FLOW explicite Task/appels sans correspondance un pour un ni contrainte Azure. Les pages commerciales n’établissent pas une collecte exhaustive. Synthèse sélective, pas de reproduction intégrale.''')
    append('marche/comparaisons.md','''### CMP154

U404–U406 — Codex, 19 septembre 2026. ELM243 comparé à Execution Tracking D07.d et BHV079–082. Trois visibilités physiques déjà adoptées U305/U308 matérialisées ; Business Process Tracking adopté sous le même parent. Appui Microsoft au nom et à la corrélation d’étapes métier ; extension explicite FLOW jusqu’aux prestations et appels contribuant aux Tasks, sans imposer de cardinalité. Camunda Process Observability a un périmètre produit plus large, incluant intervention et analyse ; FLOW conserve suivi, orchestration et adaptation distincts.

SAP EWM étaye le périmètre entrepôt ; project44 le vocabulaire et périmètre Transportation Visibility ; Blue Yonder les opérations magasin et le bénéfice de disponibilité en rayon. Les visibilités sont des perspectives combinables, pas une taxonomie éditeur reprise intégralement. Logistics Visibility ne crée pas de niveau intermédiaire. Digital Service Visibility reste une proposition historique remplacée, dont le besoin est conservé. Noms et périmètres adoptés selon leurs accords ; descriptions développées et rapprochements restent qualifiés séparément.''')
    append('JOURNAL.md','''## 2026-09-19 — U404–U406 : visibilité physique et Business Process Tracking

Préférence de nom, précision Task/appels et accord enregistrés. BHV079–082 intégrés sous Execution Tracking : trois visibilités physiques selon U305/U308, Business Process Tracking selon U406. Description des résultats, attentes, tentatives, réussite technique et fin de Task/processus ; pas de nouveau niveau ni objet de catalogue. Sources Microsoft/Camunda et relecture ciblée SAP/project44/Blue Yonder consignées ELM243/CMP154. Audit existant et AGENTS actualisés ; anciens champs validés, relations métier et preuves historiques conservés. Aucune release.''')
    (OUT/'README.md').write_text('# U406 — intégration Execution Tracking\n\nQuatre comportements directs BHV079–082. Accords physiques U305/U308 conservés ; Business Process Tracking U406, avec Tasks et appels comme objets suivis. Capture et empreintes dans implementation.yaml ; aucune nouvelle étude d’audit ni publication.\n',encoding='utf-8')
    print('U406 integrated: four direct behaviors; earlier adoptions and relations preserved.')


if __name__=='__main__':main()
