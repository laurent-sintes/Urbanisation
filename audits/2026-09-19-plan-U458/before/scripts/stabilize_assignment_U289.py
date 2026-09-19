"""Stabilize terminology and correct the U287 interpretation without rewriting history."""
from pathlib import Path
from copy import deepcopy
from scripts.structured_io import read,dumps
from scripts.apply_planning_U269 import append

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-17-vocabulaire-affectation'
def main():
    if OUT.exists():raise SystemExit('U289 already recorded.')
    OUT.mkdir()
    for name in ['glossary','refactoring-target']:
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    definition='Affecter les ressources Supply présentes ou futures aux commandes identifiées, selon les priorités, les engagements et les contraintes applicables, afin d’en assurer la meilleure satisfaction possible.'
    plan='Ensemble cohérent d’affectations proposées ou retenues précisant les ressources, quantités et dates destinées aux commandes d’un périmètre, avec les hypothèses et contraintes applicables.'
    source_rows=[
      dict(id='T1',vendor='SAP',title='Explaining Supply Assignment',url='https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-supply-assignment_af05618d-4954-4f22-9857-3dd12e3940c4',edition='Cours S/4HANA Fashion évolutif sans édition unique',passage='Supply Assignment: Basics ; Supply Assignment (ARun)',finding='ARun affecte les ressources aux besoins de commandes en pénurie ; stocks présents et futurs sont distingués.',limit='SAP conserve le nom ARun et le vocabulaire allocated ; pas un algorithme optimal universel ni un catalogue de capacités FLOW.'),
      dict(id='T2',vendor='SAP',title='Explaining aATP Product Allocation (PAL)',url='https://learning.sap.com/courses/exploring-fashion-functions-and-business-processes-in-sap-s-4hana-for-fashion-and-vertical-business/explaining-aatp-product-allocation-pal-_dd30c229-d63f-4aba-a950-a174280c4a58',edition='Cours évolutif sans édition unique',passage='PAL Concept ; Advanced ATP and Supply Assignment',finding='PAL limite la consommation de groupes de demandes ; disponibilité et ARun respectent ces limites.',limit='PAL ne signifie pas le même résultat que Supply Assignment.'),
      dict(id='T3',vendor='Microsoft',title='Inventory Visibility inventory allocation',url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation',edition='Page évolutive',passage='Business background ; Allocation definition',finding='Enveloppes affectées à des groupes avant les commandes, avec protection et contrôle de surconsommation.',limit='Pas synonyme de l’affectation à des commandes identifiées.'),
      dict(id='T4',vendor='Oracle',title='Retail Allocation Cloud Service / Allocation Overview',url='https://docs.oracle.com/en/industries/retail/retail-allocation-cloud/latest/ralim/allocation-overview.htm',edition='latest, édition de la page non figée',passage='Allocation Overview ; Item Sources ; Calculation Parameters',finding='Allocation au niveau des lieux selon leurs besoins, pouvant utiliser stock entrepôt ou apports attendus.',limit='Autre acception d’allocation ; ne pas la confondre avec affectation à des commandes déjà identifiées.') ]
    for x in source_rows:x.update(consulted_at='2026-09-17',evidence='Source primaire ouverte ou texte indexé détaillé consulté',relation='appui lexical et fonctionnel ; convention FLOW distincte')
    convention=dict(id='TERMINOLOGY-U289',source_refs=['U275','U289','CMP096'],state='working_convention_under_user_mandate',authority='Demande de stabilisation U289 ; Assignment déjà retenu U275. Formulations détaillées éditoriales non déclarées validées par Laurent.',
      canonical=dict(en='Supply Assignment',fr='Affectation des ressources aux commandes',definition=definition),
      plan=dict(en='Supply Assignment Plan',fr='Plan d’affectation des ressources aux commandes',definition=plan),
      rules=[
        'Employer Supply Assignment / affectation pour les ressources destinées aux commandes ; pas Allocation comme synonyme dans les libellés FLOW.',
        'Employer plan d’affectation, sans alterner avec plan d’allocation.',
        'Pour les droits de groupes : enveloppes de protection, droits d’usage ou plafonds de consommation selon le résultat.',
        'Répartition et distribution sont des verbes descriptifs ; toujours préciser entre quoi et quoi, pas de concepts concurrents.',
        'Allocation reste un terme éditeur ou historique qualifié : SAP PAL, Microsoft Inventory Allocation, Oracle Retail Allocation, ancien Order Allocation Run.',
        'Optimiser la satisfaction des commandes est la finalité ; l’objectif exact dépend de priorités, service, coûts et engagements, pas du seul volume confirmé.',
      ],
      boundaries=dict(protection='Configure les droits et contraintes des groupes ; ne choisit pas la ressource de chaque Order.',assignment='Matérialise et maintient le lien ressources ↔ commandes ; mobilise les arbitrages spécialisés selon le modèle.',reservation='Effet d’engagement sur les usages concurrents ; peut être porté par la même affectation, articulation toujours à arbitrer sans double déduction.',promising='Établit les possibilités et gouverne les engagements quantité/date ; affecté, réservé et promis restent distincts.',order_management='Applique les changements d’Orders autorisés issus du plan ; ne devient pas implicitement propriétaire du lien d’affectation.',execution='Réalise et suit les prestations ; affectation ne prouve pas mouvement physique.'),
      sources=source_rows,remaining_scope='Le périmètre historique Supply Assignment couvre aussi d’autres besoins identifiés, dont prévisionnels. Aucune suppression implicite de cette extension ; finalité et cas commandes stabilisés ici.',
      name_cleanup=dict(id='D05.d',before='Stock Allocation Decision',proposed='Group Protection Decision',reason='La définition actuelle porte quantités protégées et limites par groupe ; supprimer une ambiguïté avec l’affectation aux commandes.',status='target_rename_proposed_live_adopted_name_preserved'))
    (ROOT/'modeles/backlog/assignment-terminology.yaml').write_text(dumps(convention),encoding='utf-8')
    p=ROOT/'modeles/backlog/glossary.yaml';g=read(p);g['source_refs']+=['U275','U289','CMP096']
    for t in g['terms']:
        if t['id']=='TER017':
            t['notes']+=' U289 : notion résultat associée à Supply Assignment (affectation des ressources aux commandes). Ne pas employer Allocation seul comme synonyme. Un lien peut porter sur une ressource future ; il ne prouve ni promesse confirmée ni mouvement physique. Convention : modeles/backlog/assignment-terminology.yaml.'
            t['context']='Ressources et commandes ou autres besoins identifiés ; choix lexical Assignment confirmé U275, stabilisé U289.'
            t['source_refs']+=['U275','U289','CMP096']
        elif t['id']=='TER018':
            t['context']='Terme historique / rapprochement éditeur. Dans le texte FLOW courant, employer enveloppe de protection ou droit d’usage par groupe.'
            t['notes']+=' U289 : Allocation n’est pas un synonyme de Supply Assignment. Cette entrée historique reste résoluble ; le mot seul est écarté des nouveaux libellés FLOW.'
            t['source_refs']+=['U289','CMP096']
    assert not any(t['id']=='TER078' for t in g['terms'])
    g['terms'].append(dict(id='TER078',name='Supply Assignment Plan',short_description='Plan d’affectation des ressources aux commandes.',definition=plan,
      context='Objet métier descriptif de résultat, pas un niveau supplémentaire de comportement ; convention de vocabulaire U289.',
      notes='Préciser statut proposé/retenu/appliqué, périmètre, version et hypothèses. Exemple fictif : ressource de 100 pièces affectée à deux commandes pour 60 et 40 selon les règles. Il ne s’agit ni d’une enveloppe par canal ni nécessairement d’un transfert entre sites. Décider les affectations, les enregistrer, confirmer la promesse et modifier les Orders ont des effets distincts.',
      source_refs=['U289','CMP096'],source_locator=dict(path='marche/assignment-allocation-convention.md',anchor='convention-flow'),
      review=dict(state='proposed',note='Définition éditoriale sous mandat U289 ; aucune validation détaillée auto-attribuée.')))
    p.write_text(dumps(g),encoding='utf-8')
    p=ROOT/'modeles/backlog/refactoring-target.yaml';d=read(p);d['source_refs']+=['U289','CMP096'];d['terminology_convention']='modeles/backlog/assignment-terminology.yaml'
    old=deepcopy(d['order_plan_application_U287'])
    d['historical_interpretation_U287_before_U289']=old
    app=d['order_plan_application_U287']
    app.update(state='domain_direction_adopted_meaning_corrected_U289_parent_pending',proposed_name='Plan-driven Order Application',
      proposed_definition='Appliquer aux Orders les conséquences autorisées d’un scénario ou d’un plan d’affectation des ressources aux commandes, avec origine, portée et résultat de prise en compte.',
      example='Un plan affecte 100 pièces disponibles à deux commandes pour 60 et 40. Supply Assignment tient ces affectations ; D04 applique les évolutions d’Orders nécessaires et autorisées, qui peuvent être nulles si les Orders ne changent pas.',
      targeted_benefit='Assurer la cohérence des Orders avec les choix retenus sans confondre leur modification avec la tenue des liens ressources-commandes.',
      parent_arbitration='Choisir le porteur de l’application sur les Orders après distinction entre décisions, affectations et mutations d’Orders. Si le plan ne change que les liens ressources-commandes, Supply Assignment reste le responsable courant ; aucune capacité D04 supplémentaire ne se déduit de ce cas.',
      count_note='Principe U287 conservé, interprétation corrigée U289 ; ne plus justifier une nouvelle capacité par un exemple de répartition magasin.')
    app['source_refs'].append('U289')
    app['boundaries']['D03']='Supply Assignment conserve les liens ressources-commandes ; décisions et Promise Management conservent la promesse. Le besoin de décision collective d’affectation reste à instruire sans déplacer silencieusement les responsabilités.'
    app['boundaries']['D04']='Applique seulement les évolutions d’Orders issues du plan ; ne remplace pas Supply Assignment pour la tenue des affectations.'
    app['boundaries']['D05']='Planifie le stock souhaitable ; un plan d’affectation aux commandes n’est pas automatiquement un scénario Inventory Planning.'
    app['functions_to_describe'][1]='Appliquer les évolutions autorisées des Orders, si le plan en exige ; pas de création automatique d’un transfert.'
    app['non_assumptions'].append('Pas d’assimilation du plan d’affectation à une répartition entre magasins')
    for c in d['capabilities']:
        if c['id']=='D02.e':
            c['target']['definition']=definition+' Le périmètre historique des autres besoins explicitement identifiés reste à qualifier, sans retrait implicite.'
            c['target']['definition_status']='wording_proposed_under_U289'
            c['target']['boundary']='Affectations aux commandes identifiées ; autres besoins historiques conservés à préciser. Décisions spécialisées, engagement de réservation, promesse et modification des Orders restent distincts.'
            c['target']['scope']=c['target']['boundary']+'\n\nExemple : '+app['example']
            c['justification']='Terme Supply Assignment cohérent avec SAP ARun et déjà retenu U275 ; convention U289 écarte Allocation seul.'
        if c['id']=='D05.d':
            c['target']['name']='Group Protection Decision';c['target']['name_status']='proposed_rename_under_U289'
            c['justification']='Déterminer quantités protégées et plafonds par groupe ; nom proposé pour éviter de confondre avec Supply Assignment. Portée métier conservée.'
        if 'order_plan_application_note' in c:
            c['order_plan_application_note']='U289 corrige le plan : affectation ressources-commandes. D04 applique ses conséquences sur les Orders ; les liens d’affectation restent Supply Assignment. Parent D04 précis à instruire.'
    for a in d['arbitrations']:
        if a['id']=='A8':
            a['recommendation']='Appliquer les conséquences du plan d’affectation aux Orders, sans transférer le lien ressources-commandes de Supply Assignment vers D04.'
            a['choice']='Déterminer si une responsabilité D04 transverse est nécessaire après clarification U289 ; ne pas inventer des transferts magasin.'
    for case in d['scenario_tests']:
        if case['id']=='CASE5':
            case.update(case='100 pièces affectées pour 60 et 40 à deux commandes ; une évolution d’Order requise par le plan est refusée.',test='Supply Assignment tient les affectations ; D04 explicite la modification prise en compte ou refusée ; la cohérence du plan est réexaminée.',capabilities=['D02.e','D04.o','D04.i','D03.b'],expected='Aucune assimilation affectation/promesse/modification Order ; pas de transfert physique automatique.')
    p.write_text(dumps(d),encoding='utf-8')
    p=ROOT/'AGENTS.md';s=p.read_text(encoding='utf-8')
    start=s.index('- **Application de plan (U287)**');end=s.index('\n',start)
    s=s[:start]+'- **Application de plan (U287/U289)** : le plan évoqué par Laurent est un plan d’affectation de ressources à des commandes, pas une répartition magasin. D04 porte le principe d’application sur les Orders ; son parent précis reste à arbitrer. Supply Assignment conserve le lien ressources-commandes ; ni création de transfert ni transfert de responsabilité implicite.'+s[end:]
    marker='- Noms en anglais, définitions en français'
    s=s.replace(marker,'- **Vocabulaire stabilisé U275/U289** : Supply Assignment = affectation des ressources aux commandes ; Supply Assignment Plan = plan d’affectation. Allocation seul est réservé aux citations/termes éditeurs ou historiques qualifiés. Pour les groupes, employer enveloppes de protection, droits d’usage ou plafonds. Répartition/distribution sont des verbes à complément explicite. Convention : modeles/backlog/assignment-terminology.yaml.\n'+marker)
    p.write_text(s,encoding='utf-8')
    append('connaissance/04-corrections.md', '''## C93

**id**

C93

**sources**

U275, U287, U289

**constat**

Codex a interprété le plan d’allocation mentionné U287 comme une répartition de quantités vers deux magasins et a étendu cet exemple à une application de plan créant des transferts. Laurent précise U289 qu’il parlait de ressources contraintes affectées aux commandes pour améliorer leur satisfaction.

**correction**

Supply Assignment / affectation des ressources aux commandes est le terme courant, déjà retenu U275. Supply Assignment Plan / plan d’affectation désigne l’ensemble cohérent de ces choix. L’exemple magasin est retiré de la cible courante et conservé dans sa section historique. D04 applique les conséquences autorisées sur les Orders ; Supply Assignment garde les liens ressources-commandes. Allocation reste qualifié et rattaché à son sens éditeur/historique, sans ambiguïté avec les protections par groupe. Portée detailed des responsabilités à instruire ; pas de mutation silencieuse du catalogue.''')
    append('marche/elements.md','''### ELM189

- Objet : vocabulaire Assignment/Allocation, U289. Sources T1–T4 dans modeles/backlog/assignment-terminology.yaml : SAP Supply Assignment et PAL (MKT13), Microsoft Inventory Visibility allocation (MKT14), Oracle Retail Allocation.
- Libellés, URL, éditions, passages, synthèses et limites sont distingués dans l’annexe. Oracle Retail Allocation est ici un produit documenté, pas le modèle Oracle Retail RBA ni Merchandising. Consultation 17 septembre 2026.
- Nature : concepts et fonctions produits ; aucun terme universel de marché revendiqué. Supply Assignment est le rapprochement le plus précis du sens donné par Laurent.
- Réutilisation : liens et synthèses sélectives ; pas d’import de catalogue ou de preuve de déploiement.''')
    append('marche/comparaisons.md','''## CMP096

- Objet : Supply Assignment D02.e, protections D02.b, décision de droits D05.d et plan U287 corrigé U289.
- Sources : ELM189, T1–T4 dans assignment-terminology.yaml, effectivement consultées le 17 septembre 2026.
- Résultat : Supply Assignment / affectation des ressources aux commandes est le terme de travail FLOW, cohérent avec SAP ARun et U275. Allocation est polysémique : PAL SAP, enveloppes Microsoft, distribution aux lieux Oracle Retail.
- Convention : nommer le résultat Supply Assignment Plan / plan d’affectation. Groupes : enveloppes de protection et limites d’usage. Proposer Group Protection Decision en cible pour le nom ambigu Stock Allocation Decision, sans renommer le nœud adopté actif à ce stade.
- Correction : l’exemple magasin ajouté U287 par Codex était une mauvaise interprétation ; l’application d’affectations ne se confond pas avec modifier ou créer des Orders. Frontières exactes encore à instruire.
- Statut/auteur/date : Codex, 17 septembre 2026, convention de travail fixée sous mandat U289, appui lexical partiel. Aucune équivalence normative ni validation détaillée de définitions auto-attribuée.''')
    append('JOURNAL.md','''## 2026-09-17 — U289 : terminologie Assignment fixée et interprétation corrigée

Recherche primaire SAP, Microsoft, Oracle. Convention de travail Supply Assignment / affectation et Supply Assignment Plan / plan d’affectation ; aucune alternance avec Allocation seul. Glossaire métier précisé, TER078 ajouté comme formulation proposée, AGENTS et cible U286 corrigés. Ancienne interprétation magasin préservée dans l’historique de la cible ; C93 documente la correction. D05.d : Group Protection Decision proposé en cible, nom actif conservé. Aucun modèle publié modifié.''')

if __name__=='__main__':main()
