"""Prepare U286 target; no live catalog migration."""
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-17-refonte-modele'
TARGET=ROOT/'modeles/backlog/refactoring-target.yaml'

def main():
    if TARGET.exists() or OUT.exists(): raise SystemExit('Already prepared; edit target YAML.')
    OUT.mkdir()
    mp=ROOT/'modeles/backlog/model.yaml'
    model=read(mp)
    (OUT/'model-before.yaml').write_bytes(mp.read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    protected={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for folder in ('release','revisions','decisions') for p in (ROOT/'modeles'/folder).rglob('*') if p.is_file()}
    nodes={n['id']:n for n in model['nodes']}
    parents={r['target_id']:r['source_id'] for r in model['relations'] if r['type']=='contains'}
    d=dict(id='REFACTORING-U286',as_of='2026-09-17',state='complete_proposal_pending_arbitrations',
        source_refs=['U286','U285','U282','U283','U284','U265','CMP095'],
        purpose='Cible complète proposée ; annexe de travail, pas second catalogue actif ni publication.',
        scope='Supply et référentiels existants ; Case/Business Services non inventorié.',
        baseline=dict(path='audits/2026-09-17-refonte-modele/model-before.yaml',sha256=sha256(mp.read_bytes()).hexdigest(),capabilities=41,behaviors=15),
        reading_rule='Maintenir conserve la portée actuelle des accords, sans valider tous les champs. Formulations nouvelles, exemples et liens détaillés restent proposés.',
        behavior_rule=dict(differentiators=['mécanisme','politique','variante','bénéfice concret'],test='Décrire différence de façon d’agir, circonstances et effet métier. Justifier complexité OU bénéfice ciblé. Une opération produit, interface ou paramètre ne suffit pas.',terminal=True,single_parent=True),
        sources=[],capabilities=[],behaviors=[],behavior_migration=[],dependencies=[],existing_relation_review=[])
    for line in SOURCES.strip().splitlines():
        sid,vendor,mkt,title,url,edition,passage,finding,limit=line.split('|')
        d['sources'].append(dict(id=sid,vendor=vendor,market_ref=mkt,title=title,url=url,edition=edition,passage=passage,finding=finding,limit=limit,consulted_at='2026-09-17',evidence='Source primaire consultée ; S10 extrait officiel indexé, autres pages ouvertes ou texte indexé détaillé.',relation='appui partiel ; pas équivalence normative',reuse='Synthèses et liens, sans import substantiel.'))
    for line in CAPABILITIES.strip().splitlines():
        cid,action,why,example,boundary,deps,srcs=line.split('|')
        n=nodes[cid]
        d['capabilities'].append(dict(id=cid,parent_id=parents[cid],before=deepcopy(n['fields']),current_adoption=deepcopy(n.get('lifecycle',{})),
            recommendation=action,justification=why,
            target=dict(name=n['fields']['name'],definition=DEFINITIONS.get(cid,n['fields']['definition']),definition_status='new_wording_proposed' if cid in DEFINITIONS else 'unchanged_preserve_existing_scope',
                nature='management' if cid=='D04.o' else n['fields'].get('nature'),nature_status='proposed_change' if cid=='D04.o' else 'unchanged_or_not_established',boundary=boundary,example=example,example_status='illustration_proposed'),
            behavior_keys=[],decomposition_rationale='Pas de décomposition sans différence métier établie ; fonctions et règles restent en description.',
            needs_providers=deps.split(),market_sources=srcs.split(),comparison_limit='Appui partiel ; maille FLOW.' if srcs else 'Justification FLOW ; nouvelle équivalence marché non établie.',
            source_refs=list(dict.fromkeys(n.get('source_refs',[])+['U286'])),decision_status='proposal_not_adoption'))
    assert len(d['capabilities'])==41 and {c['id'] for c in d['capabilities']}=={n['id'] for n in model['nodes'] if n['kind']=='capability'}
    caps={c['id']:c for c in d['capabilities']}
    for line in BEHAVIORS.strip().splitlines():
        key,parent,name,definition,criterion,benefit,example,boundary,sources,status,existing=line.split('|')
        if existing.startswith('BHV00') and key==existing:
            name=nodes[existing]['fields']['name']; definition=nodes[existing]['fields']['definition']
        d['behaviors'].append(dict(key=key,parent_id=parent,name=name,definition=definition,differentiator=criterion,targeted_benefit=benefit,example=example,boundary=boundary,market_sources=sources.split(),status=status,existing_id=existing or None))
        caps[parent]['behavior_keys'].append(key)
    for cid,why in RATIONALES.items(): caps[cid]['decomposition_rationale']=why
    for n in model['nodes']:
        if n['kind']!='behavior': continue
        bid=n['id']
        if bid in MIGRATION: action,target,reason=MIGRATION[bid]
        elif bid in ('BHV001','BHV002','BHV003','BHV004'): action,target,reason='retain',bid,'Définition conservée ; justification rééprouvée selon U283.'
        else: action,target,reason='demote_to_description','D02.b','Conserver les opérations sur les enveloppes comme fonctions des mécanismes concernés ; pas de comportement par opération.'
        d['behavior_migration'].append(dict(id=bid,before=deepcopy(n['fields']),current_adoption=deepcopy(n.get('lifecycle',{})),action=action,target=target,reason=reason,status='migration_proposed_not_executed'))
    for c in d['capabilities']:
        for provider in c['needs_providers']:
            consumer=c['id']; condition='Si pertinent dans le cas ; pas d’appel systématique ni de séquence universelle.'
            if consumer=='D03.j' and provider in ('D05.a','D05.d'): condition='Uniquement si l’option nécessite une évolution de politique ; aucune application par CTP.'
            if provider in ('D02.c','D02.e'): condition='Selon arbitrage Reservation/Assignment ; ne pas déduire plusieurs fois un même engagement.'
            if consumer=='D05.f' and provider in ('D02.b','D04.j','D04.k','D06.d'): condition='Pour la mise en action des choix autorisés et le suivi de leur prise en compte ; aucune réalisation physique par Planning.'
            result=RESULTS.get(provider,nodes[provider]['fields']['definition'])
            matches=[r['id'] for r in model['relations'] if r['type'] not in ('contains','presents') and {r['source_id'],r['target_id']}=={consumer,provider}]
            d['dependencies'].append(dict(key=f'NEEDS-{consumer}-{provider}',consumer=consumer,provider=provider,result=result,condition=condition,
                effect='Résultat consommé sans transfert de responsabilité du fournisseur.',status='boundary_pending' if provider in ('D02.c','D02.e') else 'proposed_detailed_contract',existing_edges_between=matches,
                provenance='Lecture des définitions et périmètres ; même paire ne signifie pas équivalence de lien.',source_refs=['U286']))
    migration={x['id']:x for x in d['behavior_migration']}
    for r in model['relations']:
        s,t=r['source_id'],r['target_id']
        if r['type']=='contains' and t in migration: action,reason='migrate_with_behavior',migration[t]['reason']
        elif s in ('D03.a','D03.b','D03.c') or t in ('D03.a','D03.b','D03.c'): action,reason='conditional_redirect','Si fusion retenue, préserver sens et portée, y compris objets/document/événement illustratifs.'
        elif r['type'] in ('contains','presents'): action,reason='retain','Hiérarchie explicite conservée ; aucun parent déduit du préfixe.'
        elif r['id'].startswith('REL-INVENTORY-PLANNING'): action,reason='update_wording_only','Mobilisation conservée ; actualiser le vocabulaire de Planning.'
        else: action,reason='retain_and_qualify','Conserver le lien et compléter résultat/conditions si nécessaire ; pas d’inversion automatique.'
        d['existing_relation_review'].append(dict(id=r['id'],source=s,target=t,type=r['type'],action=action,reason=reason,current_review=deepcopy(r.get('review',{}))))
    d.update(EXTRA)
    TARGET.write_text(dumps(d),encoding='utf-8')
    finish(d,mp,protected)

SOURCES="""
S01|Microsoft|MKT14|Inventory Visibility inventory allocation|https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation|Page évolutive|Business background ; allocation APIs|Protection des groupes et contrôle de surconsommation distincts des opérations API.|Ne tranche pas Reservation/Assignment FLOW.
S02|SAP|MKT13|Outlining aATP with Supply Protection|https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-|Cours sans édition unique|Core ; Prioritized ; Time Buckets|Protection mutuelle ou priorisée ; validité et consommation contextualisées.|SuP ne couvre pas toute la prévention du surstock FLOW.
S03|Microsoft|MKT14|Replenishment methods and quantity modification|https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification|Page évolutive|Period ; Min/Max ; quantity modification|Méthodes de réassort et contraintes de quantité ont des effets distincts.|Une cible maximum n’est pas toujours un plafond dur.
S04|Microsoft|MKT14|Safety stock fulfillment for items|https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment|Page évolutive|Min/Max ; variations temporelles|Sécurité et niveaux de réassort alimentent la planification.|Tampon ne signifie pas interdiction universelle de consommer.
S05|Oracle|MKT20|Policy Assignment Sets|https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html|26B|Policy types ; overrides|Méthodes et paramètres affectables aux segments et articles-lieux.|Configuration produit, pas catalogue de capacités.
S06|RELEX|MKT29|Replenishment and allocation|https://www.relexsolutions.com/solutions/automatic-replenishment-system/|Page commerciale évolutive|Store space ; shelf-life ; ramp-downs|Espace, durée de vie et arrêt progressif influencent les apports.|Pas de contrat détaillé ; markdown et planification de saison hors FLOW.
S07|Kinaxis|MKT28|Sales and operations planning|https://www.kinaxis.com/en/solutions/sales-and-operations-planning|Page commerciale évolutive|Advanced scenarios ; Real-time agility|Simulation, impacts et ajustements sont associés à la coordination.|Ne prescrit pas les trois comportements FLOW.
S08|Microsoft|MKT14|Cycle counting|https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting|Page évolutive ; Warehouse management|Automatically create work ; Spot cycle counting|Plans récurrents et contrôles déclenchés selon la situation sont distingués.|Périmètre WMS ; réalisation des comptages chez les exécutants.
S09|Microsoft|MKT14|Action messages|https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages|Page datée 2026-03-26|Types of action messages|Recommandations d’avancement, report et réduction d’apports.|Recommandation différente de l’autorisation de modifier une commande ferme.
S10|SAP|MKT13|Backorder Processing (CA-ATP-BOP)|https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/73a1a457ef816b10e10000000a441470.html|Édition non établie ; extrait indexé|Présentation BOP|Une évolution offre/demande motive le réexamen des confirmations.|Appui à la révision ; ne démontre pas le regroupement Promise Management.
S11|Oracle|MKT20|Managing Change During Order Fulfillment|https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faiom/overview-of-managing-change-that-occurs-during-order-fulfillment.html|25C, historique explicite|Compensation ; fulfillment changes|Un changement peut nécessiter des ajustements aux tâches engagées.|Aucun rollback physique universel ni reproduction du moteur Oracle.
S12|Microsoft|MKT14|Inventory Visibility reservations|https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations|Page évolutive|Soft reservations ; offsets|Réservation logique et décompte demandent une articulation explicite.|N’impose pas une fusion Reservation/Assignment.
"""
DEFINITIONS={
'D02.b':'Configurer et maintenir les politiques, règles et quantités qui encadrent l’usage et le renouvellement des ressources pour maîtriser pénurie, surstock et déséquilibre.',
'D04.o':'Gouverner et appliquer les évolutions autorisées du cycle de vie des Orders Supply, avec leur portée, leurs conditions et leurs effets sur le reste à satisfaire.',
'D05.e':'Déterminer les apports futurs et leurs ajustements en quantité et en date pour atteindre le stock souhaitable, en tenant compte du disponible, des besoins, des apports engagés et des contraintes de modification.',
'D05.f':'Construire des scénarios alternatifs de stock, simuler et analyser leurs conséquences, puis adapter le scénario en cours à partir des faits, en mobilisant les décisions spécialisées et les capacités responsables de sa mise en action.'}
CAPABILITIES="""
D01.f|maintain|État courant et attendu distinct des faits qui l’expliquent.|100 présentes moins 30 sorties reconnues : 70 présentes ; 50 attendues restent futures.|Corrections tardives et dimensions sont des règles, pas un comportement par événement.|D01.g D07.d|
D01.g|maintain|Responsabilité durable de preuve des mouvements malgré un nom formulé comme opération.|Tracer -5 justifié par comptage sans effacer le mouvement initial.|Enregistrer et corriger sont opérations du même résultat.|D01.d D07.c|
D01.c|maintain|Vue exploitable distincte de la tenue de l’état et du contrôle ATP.|Afficher 70 présentes et 50 attendues à J+7 avec leur fraîcheur.|Filtrer, consulter, agréger sont fonctions ; multi-site est un périmètre.|D01.f|
D01.d|conditional_behaviors|Contrôle récurrent et contrôle déclenché peuvent changer les pratiques de fiabilisation.|Comparer comptage régulier des articles sensibles et recomptage après écart de préparation.|Les exécutants comptent ; mandat du déclenchement à arbitrer.|D01.c|S08
D02.b|rebuild_behaviors|Quatre mécanismes de configuration pour consommation et renouvellement.|Protéger 200 web, plafonner un groupe à 500, sécurité 40 et réassort sous 60 vers 100.|D05 décide les valeurs ; D02.b les applique transactionnellement ; les consommateurs les respectent.|D05.a D05.d|S01 S02 S03 S04 S05 S06
D02.c|boundary_arbitration|Conserver si engagement opposable distinct de l’affectation explicative.|Un droit exclusif sur 40 peut précéder l’affectation du lot précis.|Tester réservation sans affectation détaillée et affectation candidate sans réservation ; hypothèse à valider.|D01.c D02.b|S12
D03.a|merge_candidate|Regrouper actions sur la promesse avec Confirmation et Revision.|Proposer 60 vendredi et 40 lundi sans les présenter comme confirmées.|ATP/CTP produisent la faisabilité ; proposer n’est pas comportement par défaut.|D03.i D03.j D03.k D03.l|S10
D03.b|merge_candidate|Même objet d’engagement ; maille plus fine que les gestions d’Orders.|Confirmer 60 et laisser 40 non confirmées.|Confirmation ne prouve ni réservation ni acceptation d’un Service Order.|D03.a D02.c D02.e|S12
D03.c|merge_candidate|Maintenance d’un même engagement, besoin de révision conservé.|Retard de 2 jours : examiner une nouvelle promesse en conservant la précédente.|Les décisions restent spécialisées et les modifications autorisées.|D03.i D03.j D03.m D07.d D06.f|S10
D02.e|boundary_arbitration|Affectation des ressources aux besoins identifiés ; frontière engagement à trancher.|Affecter 40 d’un arrivage à une commande puis changer leur provenance admissible.|Ni redistribution physique ni enveloppe de groupe ; éviter double décompte des droits.|D01.c D02.b D02.c D03.m|S01 S12
D03.i|retain_behaviors|Quatre comportements différencient admissibilité, réseau, mobilisation et projection.|Arrivage J+7 couvrant J+60 après engagements concurrents.|Aucune politique modifiée ou réservation ; consommer les délais des exécutants.|D01.c D02.b D02.c D02.e D06.b D13.a|
D03.j|maintain|Faisabilité sous adaptation distincte des arbitrages mobilisés.|100 demandées, 60 admissibles : établir les conditions pour les 40 manquantes.|Aucun enfant par décision appelée ; apport pour Order ne dépend pas nécessairement de D05.e.|D03.i D03.m D06.e D05.a D05.d|
D03.k|maintain|Arbitrage économique autonome ; calcul du coût inclus.|Comparer transport accéléré et deux livraisons compatibles avec le service.|Ne décide pas seul de faisabilité ou des conditions contractuelles.|D03.i D03.j D11.a|
D03.l|maintain|Répartition temporelle distincte de la faisabilité et de sa matérialisation.|Retenir 60 vendredi et 40 lundi parmi les options autorisées.|Une ou plusieurs échéances sont cas à décrire, pas deux comportements obligatoires.|D03.i D03.j D03.k D11.a|
D03.m|maintain|Priorité des Orders différente des droits de groupes.|Arbitrer deux commandes concurrentes sur 80 pièces.|Pas un comportement par critère de classement ; ne modifie pas les quotas.|D11.a|
D04.i|maintain|Un type d’Order par capacité reste cohérent avec l’accord.|100 demandées, 60 livrées, 40 à servir ; retour distinct.|Pas de comportements CRUD ; promesse et progression gardent leurs responsables.|D04.n D04.o D07.c D03.b D08.d D09.d D11.a D12.a|
D04.j|maintain|Engagement fournisseur avec dates et reliquat propres.|60 reçues sur 100 ; report proposé des 40 à instruire.|Aucune négociation de contrat ou exécution fournisseur absorbée.|D04.n D04.o D07.c D08.d D09.d D11.a|
D04.k|maintain|Origine/destination et départ/arrivée distincts.|60 expédiées sur 100 ne signifient pas 60 reçues.|Même type pour réassort ou redistribution ; finalités de décision distinctes.|D04.n D04.o D07.c D13.a D08.d|
D04.l|maintain_with_gap|Gestion du retour conservée ; choix du sort du bien non démontré couvert.|6 reçues sur 10 ; identifier séparément qui décide réintégration ou rebut.|Autorisation commerciale, remboursement et disposition ne sont pas implicitement absorbés.|D04.n D04.o D07.c D04.i D08.d|
D04.m|maintain|Renvoi fournisseur distinct de l’achat et du transport.|Sur 10 à retourner, suivre les 4 encore à expédier.|Avoir financier et accord commercial hors de cette responsabilité.|D04.n D04.o D07.c D04.j D09.d D11.a|
D04.n|maintain|Transformation transverse avec conservation des quantités et liens.|Scinder 100 en 60 et 40 sans doubler la demande.|Split/merge/spread restent opérations ; choix de l’échéancier D03.l.|D03.l|
D04.o|nature_arbitration|Contenu mêlant gouvernance/application, nature courante decision à revoir.|Reporter 40 bloquées à lundi ne lève pas leur attente.|Recommander management ; autorisations incluses, décisions spécialisées distinctes.|D03.b D07.d|
D05.a|maintain|Décision des niveaux/seuils ; aucun enfant par paramètre.|Sécurité 40, déclenchement 60, cible 100 : trois effets différents.|Cible haute différente d’un plafond de groupe ou d’une capacité physique.|D01.c D13.a D08.d|S03 S04 S05
D05.d|maintain|Décide droits et limites, distinct de la configuration active.|Proposer 200 web et plafond 500 wholesale pour une période.|Ne pas renommer car allocation a un autre sens chez un éditeur.|D01.c D02.b D05.a|S01 S02
D05.e|scope_extension_arbitration|Apports positifs seuls insuffisants pour maîtriser un excès futur.|30 présentes et 80 attendues pour cible 100 : examiner réduction/report de 10.|Extension aux apports futurs ; D04 autorise/applique les changements de commandes.|D01.c D02.b D05.a D07.d D04.j D04.k|S09
D05.c|maintain|Rééquilibrage existant distinct de l’ajustement des apports.|Transférer 50 d’un site excédentaire en préservant ses engagements.|Coordonner Replenishment sans corriger deux fois le manque ; aucun transport réalisé ici.|D01.c D02.b D13.a D05.e|
D05.f|rebuild_behaviors|Trois comportements retenus ; fonctions d’autorisation et application préservées.|Explorer deux couvertures, analyser, puis adapter après retard d’arrivage.|D05 mobilise ses décisions ; D04/D02.b appliquent et D06 garde son adaptation opérationnelle.|D05.a D05.d D05.e D05.c D01.c D07.d D02.b D04.j D04.k D06.d|S07
D06.b|maintain|Capacité contextuelle communiquée, différente du SLA configuré.|1 000 préparations annoncées ne signifient pas 1 000 encore disponibles.|Aucun comportement par canal de feedback ; contrat de disponible à préciser.|D14.a|
D07.a|maintain|Résultat de décision spécifique : prestations nécessaires.|Livrer requiert préparation, document et transport.|Ne choisit pas encore l’exécutant et ne pilote pas ses opérations internes.|D14.a D13.a D04.i|
D06.e|maintain_pending_prior_arbitration|Conserver la proposition de choix des services ; fusion historique non validée par ce refacto.|Choisir un service compatible destination, marchandises et créneau.|Admissibilité/comparaison sont opérations de décision, pas comportements par filtre.|D07.a D14.a D13.a D06.b|
D06.f|maintain|Décide la variation opérationnelle, distincte de sa coordination.|Panne de préparation : retenir autre créneau ou réalisation partielle.|Remonter effet promesse à D03 ; D05 peut revoir son scénario sans décider le transporteur.|D07.d D07.b D06.e D06.b|S11
D06.d|conditional_behaviors|Prérequis du plan et compensation d’un plan engagé : deux mécanismes candidats.|Changer de transporteur décidé : révoquer ce qui reste annulable et coordonner la nouvelle collecte.|Décision D06.f séparée ; pas de rollback physique ni seconde promesse.|D07.a D06.e D06.f D07.b D07.d|S11
D07.b|maintain|Demande, acceptation et réalisation distinctes ; gestion large.|100 demandées avant 16 h, 80 acceptées pour 17 h.|Émettre/accepter/modifier/clôturer sont fonctions, pas comportements par statut.|D07.a D06.e D14.a|
D07.d|maintain|Connaissance des faits et estimations, sans décider ou tenir le stock.|60 préparées, 40 retardées, estimation de collecte révisée.|Batch/streaming sont modalités ; distinguer faits et estimations.|D07.b|
D07.c|maintain|Résultat rapproché de l’attendu, autonome par rapport à l’avancement.|80 reçues sur 100 : qualifier l’écart et informer l’Order.|Reliquat prestation différent du reliquat Order ; aucun rapprochement financier.|D07.b D07.d|
D09.d|maintain|Projection externe des parties/rôles.|Recevoir un rôle destinataire avec identifiant et provenance du partenaire.|Lecture/recherche incluse ; ni maître local ni comportement par interface.||
D11.a|maintain|Projection des conditions utiles, contiguë à Party/Catalog.|Recevoir validité et conditions de livraison applicables.|Aucune négociation locale de l’Agreement.|D09.d D12.a|
D08.d|maintain|Produit indépendant des catalogues ; rôles et variantes distincts.|Recevoir taille/couleur avant intégration dans une offre.|Product/Container sont objets et rôles, pas comportements d’ingestion.||
D12.a|maintain|Projection d’offre externe, différente du maître produit.|Recevoir offre et zone d’application avec références produit.|Aucune gouvernance locale du prix ou du catalogue.|D08.d|
D13.a|maintain|Projection des lieux/liens, différente de capacité et offre de service.|Recevoir darkstore et liens de desserte.|Ne décide pas implantation du réseau ni charge opérationnelle.|D09.d|
D14.a|maintain|Projection de services/SLA/accès, différente du suivi.|Recevoir service documentaire et accès sollicitation/feedback.|SLA, engagement individuel, estimation et résultat distincts ; pas de maître local.|D09.d D13.a|
"""

BEHAVIORS="""
BHV001|D03.i|||politique|Respecter les droits sans promettre deux fois la même quantité.|100 présentes dont 30 engagées ne donnent pas 100 libres.|Situation de référence ; aucune réservation par ATP.||existing_adopted_rationale_proposed|BHV001
BHV002|D03.i|||variante|Élargir les possibilités au réseau admissible.|Un magasin autorisé contribue lorsque l’entrepôt est vide.|Pas de comportement par type de lieu.||existing_adopted_rationale_proposed|BHV002
BHV003|D03.i|||mécanisme|Convertir présence en disponibilité utilisable à temps.|Réserve mobilisable dans 2 jours versus rack disponible aujourd’hui.|Consomme les délais opérationnels ; ne réorganise pas le prélèvement.||existing_adopted_rationale_proposed|BHV003
BHV004|D03.i|||mécanisme|Permettre engagement futur sans exiger le stock aujourd’hui.|Arrivage J+7 contribuant à J+60 après autres engagements.|Pas de création d’approvisionnement par ATP.||existing_adopted_rationale_proposed|BHV004
PLAN-CONSTRUCT|D05.f|Scenario Construction|Construire plusieurs réponses possibles en explicitant leurs hypothèses, objectifs et contraintes.|variante|Explorer des alternatives avant engagement.|Couvertures à 10 ou 15 jours pour les mêmes demandes.|Copier est une fonction ; décisions spécialisées distinctes.|S07|direction_adopted_wording_proposed|BHV005
PLAN-SIMULATE|D05.f|Simulation & Analysis|Projeter les conséquences d’un scénario et analyser leurs impacts sur les indicateurs métier et les processus pour éclairer les choix.|mécanisme|Comprendre compromis et effets locaux.|Service 94 à 97 %, stock +120 k€ ; identifier les magasins perdants.|BHV006 et BHV010 réunis ; comparer reste une fonction, aucun recalcul imposé.|S07|combined_behavior_adopted_wording_proposed|BHV006
PLAN-ADAPT|D05.f|Scenario Execution Adaptation|Adapter le scénario de stock en cours aux écarts observés, compte tenu des actions engagées et des décisions spécialisées.|mécanisme|Maintenir une trajectoire cohérente malgré les aléas.|Réviser apports et transferts après report fournisseur sans oublier les quantités expédiées.|D06 décide la variation opérationnelle ; D04/D02.b appliquent leurs changements.|S07|direction_adopted_wording_proposed|
PROTECT-GROUP|D02.b|Group Supply Protection|Configurer les droits préservant l’accès d’un groupe à des ressources face aux usages concurrents.|politique|Éviter qu’une demande précoce épuise les ressources d’un autre groupe.|Préserver 200 pièces pour le web avant sa demande.|Protection mutuelle ou priorisée décrites ensemble ; D05.d décide les quantités.|S01 S02|proposed|
PROTECT-CAP|D02.b|Consumption Capping|Configurer les limites de consommation d’un groupe sur le périmètre et la période retenus.|politique|Empêcher la surconsommation même si du stock reste accessible.|Un groupe ne dépasse pas 500 malgré un stock supérieur.|Préserver un minimum et limiter un maximum diffèrent ; imputation et correction sont fonctions.|S01|proposed|
PROTECT-BUFFER|D02.b|Safety Stock Policy|Configurer le stock tampon et ses conditions d’utilisation pour absorber les incertitudes.|mécanisme|Expliciter le rôle de sécurité sans le confondre avec réservation ou déclenchement.|Sécurité 40 pour absorber retard fournisseur ; préciser quand elle peut être consommée.|D05.a décide le niveau ; ne pas additionner deux fois le tampon et le minimum de réassort.|S04 S05|proposed|
PROTECT-REPLENISH|D02.b|Replenishment Regulation|Configurer les règles de déclenchement et de limitation du réassort qui encadrent le renouvellement du stock.|mécanisme|Prévenir manque et excès par des règles cohérentes de renouvellement.|Sous 60 viser 100 ; appliquer la baisse de cible décidée en fin de vie.|Min/Max et revue périodique décrites comme modalités, sans sous-comportements ; D05.e décide et D04 gère les apports.|S03 S05 S06|proposed|
COUNT-RECUR|D01.d|Recurring Stock Verification|Fiabiliser le stock par un programme récurrent de constats et de rapprochements ciblés.|politique|Organiser une fiabilisation régulière selon les risques.|Contrôles réguliers des références sensibles puis corrections justifiées.|Réalisation du comptage chez l’exécutant ; mandat du programme à préciser.|S08|conditional_arbitration|
COUNT-TRIGGER|D01.d|Triggered Stock Verification|Fiabiliser une situation de stock par une vérification ciblée face à un signal.|mécanisme|Traiter une incertitude locale sans attendre le cycle régulier.|Recomptage après écart de préparation.|Seuil ou anomalie sont déclencheurs ; pas un comportement par motif.|S08|conditional_arbitration|
ORCH-DEPEND|D06.d|Dependency-driven Execution|Coordonner les prestations selon leurs prérequis et les résultats observés du plan retenu.|mécanisme|Éviter des sollicitations dont les prérequis métier ne sont pas satisfaits.|Collecte conditionnée aux colis prêts et au document requis.|Pas de workflow universel ; D06.f décide les variations.|S11|conditional_arbitration|
ORCH-COMPENSATE|D06.d|Execution Compensation|Coordonner les ajustements des prestations engagées pour appliquer une variation retenue en respectant les effets irréversibles.|mécanisme|Éviter doublons et annulations impossibles lors d’un changement.|Changer de collecte après préparation ; révoquer seulement ce qui reste annulable.|Pas de rollback physique ; décision D06.f et gestion D07.b distinctes.|S11|conditional_arbitration|
"""
RATIONALES={
'D03.i':'Quatre différences combinables modifient les possibilités : droits engagés, réseau, mobilisation et ressources futures ; aucun comportement par lieu ou technologie.',
'D05.f':'Explorer des alternatives, comprendre leurs conséquences et adapter un scénario engagé changent les pratiques de planification et leur articulation avec l’exécution.',
'D02.b':'Préserver un accès, limiter une consommation, absorber l’incertitude et réguler les apports répondent à des risques différents ; mécanismes combinables, pas étapes d’un cycle.',
'D01.d':'Sous réserve du mandat, contrôle récurrent et contrôle déclenché organisent différemment la fiabilisation ; compter/comparer/corriger restent fonctions.',
'D06.d':'Faire progresser un plan et transformer un plan engagé posent des contraintes de coordination différentes, notamment les effets irréversibles.'}
MIGRATION={
'BHV005':('revise_definition','PLAN-CONSTRUCT','Préciser la construction d’alternatives ; conserver l’identité.'),
'BHV006':('broaden_and_rename','PLAN-SIMULATE','Conserver l’identité de simulation en intégrant l’analyse.'),
'BHV010':('absorb_then_retire','PLAN-SIMULATE','Préserver indicateurs et explications dans le comportement combiné et archiver les accords U271.'),
'BHV007':('demote_to_description','D05.f','Conserver comparaison/appréciation sans nœud autonome.'),
'BHV008':('demote_to_description','D05.f','Conserver autorisation, conditions et réserves sans nœud autonome.'),
'BHV009':('demote_to_description','D05.f','Conserver application et prise en compte ; ne pas réutiliser cet ID pour adaptation.')}
RESULTS={
'D01.g':'Faits de stock qualifiés et corrections tracées','D01.d':'Constats et corrections de comptage justifiés','D01.f':'État courant et ressources futures séparés','D01.c':'Quantités et états avec provenance et fraîcheur',
'D02.b':'Protections applicables, droits et limites par période','D02.c':'Engagements opposables selon frontière à arbitrer','D02.e':'Affectations aux besoins identifiés',
'D03.a':'Propositions de promesse','D03.b':'Engagements confirmés et part non confirmée','D03.i':'Possibilités quantité/date de référence','D03.j':'Possibilités sous adaptation et conditions',
'D03.k':'Arbitrage économique','D03.l':'Échéancier retenu','D03.m':'Priorités relatives des Orders',
'D04.n':'Structure transformée et liens à l’origine','D04.o':'Progression autorisée et restrictions','D04.i':'Demande client et conditions',
'D04.j':'Apports fournisseur attendus et possibilités de modification','D04.k':'Transferts attendus et possibilités de modification',
'D05.a':'Cibles et seuils proposés ou retenus','D05.d':'Droits de groupes et limites proposés ou retenus','D05.e':'Apports et ajustements recommandés selon arbitrage','D05.c':'Rééquilibrage recommandé du stock existant',
'D06.b':'Capacité contextuelle communiquée et datée','D07.a':'Prestations nécessaires','D06.e':'Services/exécutants compatibles retenus','D06.f':'Variation opérationnelle retenue et impacts Supply',
'D06.d':'Coordination du plan et prise en compte','D07.b':'Demandes et réponses de prise en charge','D07.d':'Faits, jalons et estimations','D07.c':'Résultats rapprochés et écarts qualifiés',
'D08.d':'Produits/variantes et caractéristiques utiles','D09.d':'Parties et rôles externes','D11.a':'Conditions contractuelles et validité','D12.a':'Offre commerciale externe','D13.a':'Lieux et liens du réseau','D14.a':'Services, SLA et accès configurés'}
EXTRA={
'merge_proposal':{
 'key':'PROMISE-MANAGEMENT','source_ids':['D03.a','D03.b','D03.c'],'name':'Promise Management',
 'definition':'Gérer les propositions et engagements de promesse Supply, leurs confirmations et leurs révisions autorisées, avec quantités, dates, conditions et historique.',
 'status':'joint_arbitration','recommended':True,'behavior_keys':[],
 'why':'Même engagement durable, maille d’action cohérente avec les autres gestions ; trois verbes conservés comme fonctions.',
 'identity_plan':'Identifiant neuf si fusion retenue ; trois IDs retirés avec correspondance et redirection explicites. Aucun ancien accord transféré automatiquement.',
 'alternative':'Conserver si l’autonomie des responsabilités est démontrée ; ne pas transformer automatiquement les trois en comportements.',
 'counterexample_test':'Si confirmer relève d’un mandat autonome irréductible à la gouvernance de la promesse, expliciter cette frontière avant fusion.',
 'market_limit':'BOP prouve le besoin de révision, pas la fusion ; recommandation fondée sur la cohérence FLOW.'},
'protection_coverage':[
 {'concern':'Accès concurrent / surconsommation','covered_by':['PROTECT-GROUP','PROTECT-CAP'],'limit':'Fait consommant les droits et correction à définir ; pas de double décompte avec réservation.'},
 {'concern':'Pénurie / incertitude','covered_by':['PROTECT-BUFFER','PROTECT-REPLENISH'],'limit':'Sécurité, seuil et cible se combinent sans addition automatique.'},
 {'concern':'Surstock futur / fin de vie','covered_by':['PROTECT-REPLENISH','D05.e'],'limit':'Limiter nouveaux apports ; ajustement des commandes fermes soumis à arbitrage puis D04.'},
 {'concern':'Surstock existant','covered_by':['D05.c'],'limit':'Protection ne réalise ni redistribution, ni retour, ni markdown ou destruction.'},
 {'concern':'Présentation / espace / péremption / lots','covered_by':['PROTECT-REPLENISH','D05.a','D05.e'],'limit':'Contraintes selon le cas ; aucun comportement par paramètre ni nouvelle maîtrise des données externes.'},
 {'concern':'Validité / activation / dérogation / masse / suivi','covered_by':['D02.b'],'limit':'Propriétés et fonctions de gouvernance ; dérogation explicite avec portée et durée.'}],
'arbitrations':[
 {'id':'A1','topic':'Supply Protection','recommendation':'Quatre mécanismes proposés ; fonctions d’allocation conservées.','affected':['D02.b'],'choice':'Retenir ou ajuster les quatre résultats, noms et frontières.'},
 {'id':'A2','topic':'Promise Management','recommendation':'Fusion des trois actions sans recréer trois comportements fonctionnels.','affected':['D03.a','D03.b','D03.c'],'choice':'Confirmer responsabilité commune ou démontrer autonomie.'},
 {'id':'A3','topic':'Reservation / Assignment','recommendation':'Maintenir provisoirement les deux ; tester engagement opposable versus affectation.','affected':['D02.c','D02.e'],'choice':'Propriété du droit, décompte, rattachement et cas discriminants.'},
 {'id':'A4','topic':'Order Lifecycle Management','recommendation':'Nature management couvrant gouvernance et application des transitions.','affected':['D04.o'],'choice':'Valider ce périmètre ou démontrer un résultat de décision autonome.'},
 {'id':'A5','topic':'Replenishment et surstock','recommendation':'Étendre D05.e aux ajustements des apports futurs, mise en action D04.','affected':['D05.e'],'choice':'Valider le périmètre sur apports déjà fermes sous contraintes.'},
 {'id':'A6','topic':'Décompositions complémentaires','recommendation':'Deux mécanismes Stocktaking et deux Orchestration, conditionnels.','affected':['D01.d','D06.d'],'choice':'Confirmer bénéfice et mandat avant création.'},
 {'id':'A7','topic':'Dépendances et données','recommendation':'Valider résultats et producteurs sur cas concrets, surtout engagement/disponibilité.','affected':['D03.i','D05.f','D06.b'],'choice':'Contrats métier et conditions ; pas graphe d’appels logiciel.'}],
'known_gaps':[
 {'topic':'Disposition des retours','recommendation':'Localiser la décision réintégration/réparation/rebut/renvoi avant nouveau nœud.','decision_needed':'Supply, Case ou exécutant ? Comparaison nouvelle non réalisée dans cette passe.'},
 {'topic':'Données de décision','recommendation':'Décrire demande future, coûts, risques, délais, règles et fraîcheur en entrées.','decision_needed':'Producteurs et contrats inconnus pour certains cas ; aucun maître inventé.'},
 {'topic':'Capacité disponible / mobilisation','recommendation':'Consommer connaissance contextuelle D06.b et délai effectif article/lieu.','decision_needed':'Responsable du délai et sémantique de capacité restante avec les exécutants.'}],
'work_packages':{
 'from_existing_agreements':['Conserver domaines, décisions spécialisées et niveau terminal.','Préparer les trois comportements Planning, dont Simulation & analyse.','Sortir les opérations d’allocation de la cible de comportements, garder les détails.','Balisage des recommandations obsolètes et correction des consignes actives.','Conserver les quatre comportements ATP ; justifications enrichies proposées.'],
 'joint_decisions':['A1','A2','A3','A4','A5','A6','A7'],
 'technical_migration':['Figer remplacements et attribuer des IDs neufs sans réemploi.','Migrer valeurs, scopes et relations en conservant les anciennes valeurs et accords.','N’adopter que les champs/valeurs effectivement validés.','Vérifier chaque ancien nœud/lien, les liens model: et les vues dérivées.','Atlas : contrôler arbre, recherche et fiches lors d’une publication demandée ; aucune réécriture du moteur justifiée.'],
 'performed_this_turn':['Cible exhaustive et migration préparées','Comparaison ciblée actualisée','Consignes obsolètes corrigées','Couverture et non-modification du catalogue vérifiées']},
'scenario_tests':[
 {'id':'CASE1','case':'100 présentes, 30 réservées, enveloppe web 40 dont 10 consommées ; demande web 20.','test':'Préciser les recouvrements avant calcul ; éviter stock moins réservation moins enveloppe sans contrat.','capabilities':['D02.b','D02.c','D02.e','D03.i'],'expected':'Décompte expliqué ; aucune valeur imposée sans les données manquantes.'},
 {'id':'CASE2','case':'Cible 100, présentes 30, arrivage ferme 80, demande en baisse.','test':'D05.e recommande ; D04 examine réduction/report des 10 excédentaires.','capabilities':['D05.e','D04.j','D04.o'],'expected':'Si non modifiable, excès explicité ; aucune modification silencieuse.'},
 {'id':'CASE3','case':'100 à livrer, 60 préparées, collecte impossible.','test':'D06.f choisit, D06.d coordonne, D03 révise si nécessaire ; D05 adapte son scénario de stock.','capabilities':['D06.f','D06.d','D07.b','D07.d','D03.c','D05.f'],'expected':'Ni deuxième autorité sur transporteur/promesse, ni oubli des faits irréversibles.'},
 {'id':'CASE4','case':'Deux scénarios de stock aux effets service/coûts différents.','test':'Construction des hypothèses ; Simulation & analyse des conséquences ; validation et application décrites.','capabilities':['D05.f'],'expected':'Trois comportements sans perte d’analyse des impacts ou de gouvernance.'}]
}

def finish(d,mp,protected):
    p=ROOT/'AGENTS.md'; text=p.read_text(encoding='utf-8')
    old='U269 attribue explicitement à Scenario Application sous Inventory Planning le déclenchement des actions retenues et la connaissance de leur prise en compte **via les capacités opérationnelles responsables** : Supply Protection pour les protections, D04 pour les Orders et D06 pour les prestations.'
    new='Après U283/U284, la mise en action reste une fonction d’Inventory Planning : déclencher les actions retenues et connaître leur prise en compte **via les capacités opérationnelles responsables** (Supply Protection, D04 et D06), sans comportement autonome Scenario Application.'
    assert old in text
    text=text.replace(old,new).replace('- Plan d’amélioration et arbitrages : [audit U265/U266](audits/2026-09-17-audit-comportements/rapport.md), [propositions structurées](modeles/backlog/behavior-audit.yaml).',
        '- Refonte courante U286 : [cible complète et arbitrages](audits/2026-09-17-refonte-modele/rapport.md), annexe proposée faisant autorité pour cette étude : modeles/backlog/refactoring-target.yaml. L’audit U265/U266 reste historique ; ses découpages par opérations ne sont plus des recommandations courantes.')
    p.write_text(text,encoding='utf-8')
    p=ROOT/'modeles/backlog/behavior-audit.yaml'; a=read(p)
    a['source_refs'].append('U286')
    a['current_target_U286']=dict(path='modeles/backlog/refactoring-target.yaml',report='audits/2026-09-17-refonte-modele/rapport.md',state='proposed',scope='Cible exhaustive ; remplace les recommandations obsolètes, pas les accords historiques.')
    p.write_text(dumps(a),encoding='utf-8')
    append('marche/elements.md','''### ELM188

- Ensemble documentaire U286 : sources S01–S12 distinguées dans modeles/backlog/refactoring-target.yaml ; Microsoft MKT14, SAP MKT13, Oracle MKT20, Kinaxis MKT28, RELEX MKT29.
- Éléments natifs : politiques d’allocation/réassort, comptages, recommandations, réservation, BOP, compensation et scénarios. Nature : fonctions, politiques ou processus de produits ; pas automatiquement des capacités.
- URL, édition, passage, synthèse et limite sont conservés source par source dans l’annexe ; consultation 17 septembre 2026. S10 extrait officiel indexé ; autres pages ouvertes ou passages indexés détaillés. Oracle 25C historique explicite.
- Appui à la différenciation des mécanismes et effets ; pas de preuve de déploiement Beaumanoir. Synthèses sélectives sans import substantiel ni droit de republication intégrale présumé.''')
    append('marche/comparaisons.md','''## CMP095

- Objet : U286, 41 capacités et 15 comportements de la capture audits/2026-09-17-refonte-modele/model-before.yaml ; empreinte dans l’annexe cible.
- Sources : ELM188 et S01–S12 de modeles/backlog/refactoring-target.yaml ; reprend et précise aussi ELM176–179, ELM183 et ELM187.
- Relation : appuis fonctionnels/méthodologiques partiels. Chaque recommandation est justifiée par le marché consulté ou explicitement par la cohérence FLOW.
- Cible proposée : quatre mécanismes Protection ; trois Planning selon accords ; quatre ATP conservés ; fusion candidate Promise Management sans comportements CRUD ; ajustements des apports D05.e ; Stocktaking/Orchestration conditionnels.
- Écarts : Supply Protection FLOW dépasse SAP SuP ; les produits combinent décisions et application que FLOW distingue. Les anciennes listes d’opérations sont matière fonctionnelle.
- Limites : pas de copie des niveaux éditeurs, de complétude Case, ni de preuve d’installation. Fusion et frontières restent des arbitrages FLOW.
- Statut/auteur/date : proposition Codex, 17 septembre 2026. U286 autorise la préparation ; les valeurs nouvelles ne sont pas automatiquement adoptées.''')
    append('JOURNAL.md','''## 2026-09-17 — U286 : cible complète préparée

Revue des 41 capacités, migration des 15 comportements et inventaire de toutes les relations. Proposition de quatre mécanismes Protection, trois Planning et maintien des quatre ATP ; Stocktaking et Orchestration conditionnels. Sept arbitrages regroupés. Consignes obsolètes corrigées, catalogue actif et accords inchangés. Comparaison CMP095. Aucune publication ou administration serveur.''')
    assert sha256(mp.read_bytes()).hexdigest()==d['baseline']['sha256']
    assert all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in protected.items())
    (OUT/'integrity.json').write_text(json.dumps(dict(active_model_unchanged=True,active_model_sha256=d['baseline']['sha256'],protected_files=protected),indent=2),encoding='utf-8')
    print('Complete target prepared; live catalog unchanged.')

if __name__=='__main__': main()
