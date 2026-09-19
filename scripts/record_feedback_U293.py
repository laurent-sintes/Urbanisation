"""Record scoped feedback on the U292 proposals; no catalogue changes."""
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.apply_refactoring_U290 import append

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'modeles/backlog/behavior-gap-audit.yaml'
a=read(p)
if 'feedback_U293' in a:
    raise SystemExit('Feedback already recorded.')
history=ROOT/'audits/2026-09-17-comportements-manquants/history'
history.mkdir(exist_ok=True)
(history/'audit-before-U293.yaml').write_bytes(p.read_bytes())

records=[
('S29','SAP','SAP Business Network Global Track and Trace','https://www.sap.com/products/business-network/global-track-and-trace.html','Page produit évolutive, édition non indiquée','FAQ: logistics visibility / solution scope','Visibilité des expéditions : localisation, progression, statut et arrivée estimée, avec contexte commande ; alertes en cas de perturbation.','Présentation produit primaire, pas garantie universelle de précision ou de temps réel.'),
('S30','Microsoft','Landed cost module overview','https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview','D365 SCM, page évolutive','Goods in transit / tracking','Le module documente les marchandises en transit et le suivi de leurs dates de livraison.','Périmètre produit spécifique ; pas équivalence intégrale avec le tracking multi-services FLOW, ni télémétrie continue démontrée.'),
('S31','Microsoft','Approve and confirm purchase orders','https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation','D365 SCM ; mise à jour affichée 2026-09-08','Approval / Changing / Canceling purchase orders','Le guide distingue statuts de commande, approbation, modification et annulation du reliquat non réalisé. Le workflow d’approbation organise les activités permettant certains changements.','Pas de cycle universel à copier ; clôture financière hors périmètre de notre exemple.'),
('S32','Camunda','Compensation','https://docs.camunda.io/docs/components/modeler/bpmn/compensation-handler/','Version affichée 8.9','Compensation handlers','Les gestionnaires de compensation traitent les effets d’activités achevées.','Document de réalisation BPMN, pas modèle métier ; ne prouve pas que toute compensation implique Case Management ni qu’un Order est toujours un case.'),
('S33','Camunda','Workflow patterns','https://docs.camunda.io/docs/components/concepts/workflow-patterns/','Version affichée 8.9','Interrupting events / compensation','Les événements peuvent interrompre un traitement en cours ; la compensation est un mécanisme distinct de gestion des effets.','Interrompre un processus ne garantit pas l’arrêt d’un exécutant externe. Aucun moteur ni redémarrage global imposé.')]
for i,v,t,u,e,l,f,limit in records:
    a['sources'].append(dict(id=i,vendor=v,native_label=t,native_id=None,url=u,edition=e,consulted_on='2026-09-17',locator=l,nature='présentation produit' if i=='S29' else 'documentation',access='Texte primaire consulté',observed_fact=f,limits=limit,reuse='Synthèse sélective et lien ; aucune importation substantielle.'))

a['feedback_U293']=dict(source_refs=['U293','C94','ELM192','CMP099'],
    scope='Corrections de l’audit. Aucun changement du catalogue actif ; nouvelles formulations et décomposition Transit Visibility restent proposées.',
    points=[
        dict(topic='Execution Tracking',market_sources=['S29','S30'],
            conclusion='La visibilité de la marchandise en mouvement est un résultat à part entière ; la détection d’exception complète ce suivi normal.',
            proposal='Transit Visibility : rendre consultables la localisation connue ou estimée, l’étape du trajet, les quantités concernées, la destination et l’arrivée attendue, avec source et fraîcheur. Comportement candidat sous Execution Tracking, à discuter ; pas de renommage de toute la capacité.',
            boundary='Execution Tracking suit aussi les prestations non physiques. Inventory Visibility conserve les quantités et états de stock, y compris en transit selon le périmètre ; les deux vues partagent les faits sans ajouter deux fois la même ressource. Disponible à consulter à tout moment ne signifie pas mesure GPS permanente.'),
        dict(topic='Order Lifecycle Management',market_sources=['S31'],
            conclusion='Gérer les états métier de l’Order et appliquer leurs transitions autorisées, avec conditions, portée et effets sur le reste à satisfaire.',
            proposal='Exemple : 100 pièces, 60 expédiées, demande d’annulation des 40 restantes. Lifecycle enregistre le devenir autorisé du reliquat ; le processus traite les activités affectées ; l’orchestration coordonne les prestations nécessaires.',
            boundary='Coordinated Order Release P11 reste à clarifier, pas recommandé en l’état. Une condition de libération ne suffit pas à justifier un comportement distinct. La responsabilité des états ne commande pas directement les étapes de préparation ou de transport.'),
        dict(topic='Excédent',market_sources=['S12'],
            conclusion='Employer excédent dans les propositions courantes, selon la préférence U293.',
            proposal='Définition proposée : quantité de ressource dépassant le besoin ou la cible retenue pour un périmètre et un horizon donnés, après prise en compte des engagements pertinents.',
            boundary='Un excédent local peut être utile ailleurs ou plus tard ; il ne présume ni anomalie globale ni destruction. Les citations et archives restent intactes. Entrée de glossaire non créée dans cette discussion.'),
        dict(topic='Adaptabilité des processus / Case Management',market_sources=['S17','S32','S33'],
            conclusion='Retirer P05 Execution Compensation comme comportement métier Supply autonome. Dans le cas discuté, l’Order est le case ; changement d’état et de contenu peuvent nécessiter d’adapter son traitement.',
            proposal='L’adaptation du processus peut interrompre les travaux devenus inutiles, compenser les effets déjà produits lorsque nécessaire, puis poursuivre ou reprendre les parties affectées conformément à l’état actualisé de l’Order.',
            boundary='Compensation est un mécanisme de réalisation de l’adaptabilité ; elle existe aussi en BPMN. D06.f conserve le choix métier de la variation et D06.d la coordination des prestations. Aucun transfert global de l’orchestration vers Business Services ; aucune assimilation universelle Order/Case ni effacement d’un fait physique.')
    ],
    current_summary='P05 retiré ; P11 à clarifier ; P10 conservé comme complément, Transit Visibility proposé séparément dans ce feedback. Neuf candidats ciblés initiaux restent proposés, cinq options conditionnelles ; Transit Visibility n’est pas encore ajouté comme fiche P ni comme BHV.')

for c in a['candidates']:
    if c['id']=='P05':
        c['status']='withdrawn_U293'
        c['review_note']='Retiré comme comportement métier autonome ; mécanisme d’adaptabilité du processus/Case. Voir feedback U293.'
    if c['id']=='P11':
        c['status']='needs_clarification_U293'
        c['review_note']='Le bénéfice distinct d’une règle de transition reste à démontrer ; confusion avec orchestration à lever.'
    if c['id']=='P10':
        c['boundary']+=' U293 : ce comportement ne résume pas Execution Tracking ; la visibilité normale du transit reste essentielle.'
for x in a['assessments']:
    if x['capability_id']=='D06.d':
        x['diagnosis']='La compensation proposée U292 relève de l’adaptabilité du processus ; elle ne justifie pas un comportement Supply autonome.'
        x['recommendation']='P04 reste proposé. P05 retiré U293 ; conserver la distinction choix métier de variation / coordination / réalisation par processus.'
    if x['capability_id']=='D07.d':
        x['diagnosis']='Le suivi doit montrer la situation normale, dont la localisation des marchandises en transit, et les exceptions.'
        x['recommendation']='Transit Visibility proposé dans U293 ; P10 complémentaire. Ne pas réduire les prestations documentaires à la localisation physique.'
    if x['capability_id']=='D04.o':
        x['verdict']='clarifier avant décomposition'
        x['recommendation']='Expliciter les états métier et transitions autorisées ; P11 à clarifier, distinct de la coordination des prestations. Voir U293.'

# Only current proposal prose; the exact original is preserved above.
def terminology(value):
    if isinstance(value,str):
        return value.replace('Protection contre le surstock','Traitement d’un excédent').replace('du surstock','des excédents').replace('le surstock','les excédents')
    if isinstance(value,list): return [terminology(v) for v in value]
    if isinstance(value,dict): return {k:terminology(v) for k,v in value.items()}
    return value
a=terminology(a)
a['source_refs']+=['U293','CMP099']
a['findings']=[f for f in a['findings'] if not f.startswith('11 candidats')]
a['findings'].append(a['feedback_U293']['current_summary'])
a['methodology']['completeness']+=' U293 ajoute Camunda comme appui de réalisation des processus, pas comme huitième catalogue Supply.'
p.write_text(dumps(a),encoding='utf-8')

append('connaissance/04-corrections.md','''## C94

**id**

C94

**sources**

U292, U293

**constat**

L’audit U292 mettait en avant la détection d’exceptions sans rendre aussi visible le suivi normal du transit. Sa proposition de libération coordonnée prêtait à confusion avec l’orchestration. Il proposait aussi Execution Compensation comme comportement métier autonome et utilisait surstock.

**correction**

U293 réaffirme la visibilité de la marchandise en mouvement ; Transit Visibility est une piste de comportement, pas un renommage adopté. Lifecycle porte états et transitions autorisées de l’Order ; le processus organise son traitement et D06 coordonne les prestations. P11 est à clarifier, P05 retiré comme comportement autonome : la compensation relève de l’adaptabilité du processus, avec l’Order comme case dans le contexte discuté. Interruption des activités en cours et compensation des effets produits sont distinguées. Employer excédent dans les propositions courantes ; définition contextuelle proposée, sans remplacement des archives ni mutation silencieuse du catalogue.''')
append('marche/catalogue.md','''## MKT36

- Référence : Camunda 8, documentation de réalisation BPMN ; distincte de la norme OMG.
- Sources : https://docs.camunda.io/docs/components/modeler/bpmn/compensation-handler/ et https://docs.camunda.io/docs/components/concepts/workflow-patterns/
- Version affichée 8.9, textes consultés le 17 septembre 2026 ; sections compensation et interruptions.
- Rôle et limites : éclairer réalisation de l’adaptabilité et distinction interruption/compensation ; aucun moteur, niveau métier ni équivalence Order/Case imposé. Synthèse sélective, pas de reproduction substantielle.

## MKT37

- Référence : SAP Business Network Global Track and Trace, présentation produit.
- Source : https://www.sap.com/products/business-network/global-track-and-trace.html ; FAQ logistics visibility et périmètre du produit.
- Édition logicielle non indiquée ; texte consulté le 17 septembre 2026.
- Rôle et limites : visibilité des marchandises en transit, étapes et ETA ; appui de périmètre, pas garantie détaillée de télémétrie ni preuve de déploiement. Synthèse sélective.''')
append('marche/elements.md','''### ELM192

- Éléments S29–S33 de modeles/backlog/behavior-gap-audit.yaml : SAP Global Track and Trace MKT37, Microsoft Landed Cost et états des achats MKT14, Camunda compensation/workflow patterns MKT36.
- Consultation : 17 septembre 2026 ; faits, URL, passages, éditions et limites source par source dans l’annexe. SAP : présentation produit ; Microsoft et Camunda : guides documentaires.
- Nature : visibilité logistique, règles de cycle de vie et mécanismes de processus ; aucune décomposition de capacités native ni adoption de moteur. CMP099 proposé.''')
append('marche/comparaisons.md','''## CMP099

- Objet : corrections U293 de l’audit U292, sur D07.d, D04.o, D06.d et vocabulaire des excédents.
- Appuis : ELM192, S29–S33 ; S12 pour les excédents et S17 pour la compensation produit. Baseline du catalogue U290 inchangée.
- Résultat : tracking normal et visibilité du transit, complétés par détection d’exceptions ; séparation état métier de l’Order / conduite du processus / coordination des prestations. Retrait de P05 comme comportement autonome ; P11 à clarifier. Proposition Transit Visibility sans création de BHV.
- Limites : compensation n’est pas spécifique au Case Management ; l’Order comme case est le choix du contexte discuté, pas un axiome général. Interruption, compensation et irréversibilité physique restent distinctes. Excédent dépend d’un besoin/cible, lieu et horizon.
- Statut/auteur/date : corrections reçues U293 ; définitions et rattachements supplémentaires proposés par Codex le 17 septembre 2026. Aucun nom de capacité ni domaine renommé.''')
append('JOURNAL.md','''## 2026-09-17 — U293 : précisions du feedback sur l’audit

Contribution enregistrée, C94 et CMP099. Audit U292 annoté : Transit Visibility proposé en complément des exceptions, Lifecycle distingué du processus et de l’orchestration, P11 à clarifier, P05 retiré comme mécanisme autonome au profit de l’adaptabilité du processus. Terme excédent dans les propositions courantes. État antérieur de l’annexe conservé dans history/audit-before-U293.yaml. Catalogue et publications inchangés.''')
print('Feedback U293 recorded; catalogue unchanged.')
