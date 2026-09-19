# Audit FLOW : capacités et comportements

17 septembre 2026 — U265/U266. Backlog après U264, puis corrections documentaires de cet audit. Conclusions et refontes proposées par Codex ; aucune adoption implicite. [Comparaison marché et sources primaires](marche.md) · [Matrice exhaustive](matrice.md) · [Propositions structurées](../../modeles/backlog/behavior-audit.yaml).

## Conclusion

**Le niveau Comportement est suffisant pour les besoins examinés. Je ne recommande pas de niveau supplémentaire.** Il permet de conserver des capacités d’action larges tout en précisant simulation, traitements collectifs, cycle de vie et réaction aux aléas. Les détails restants peuvent être des conditions, informations, règles, exemples et résultats d’un comportement ; les objets, documents, événements et parcours conservent leurs modèles propres.

Cette conclusion porte sur la maille descriptive, pas sur la complétude du métier. Le test a porté sur les 41 capacités Supply/référentiels, les quatre comportements ATP et les familles de cas ci-dessous. Business Services reste peu développé : pas d’affirmation d’exhaustivité de cet univers. Les comportements ne corrigent pas seuls les frontières Reservation/Assignment, la nature de Lifecycle, les relations manquantes ou la disposition des retours.

Le marché confirme surtout une difficulté de **nature des éléments comparés** : Microsoft va jusqu’aux configurations et tests, SAP distingue métier et solution, TM Forum relie processus, informations et API. Ajouter notre niveau ne justifie pas de reproduire leurs profondeurs. La correspondance doit être plusieurs-à-plusieurs, explicitée par résultat et périmètre, à la capacité ou au comportement selon le cas. Voir [la comparaison sourcée](marche.md).

## Règle d’arrêt et justification

U265 adopte l’exigence : **complexité OU bénéfice ciblé**. Elle figure désormais comme principe du modèle et dans MOD006 ; `fields.decomposition_rationale` la documente sur une capacité décomposée. ATP possède une justification proposée. Le contrôleur exige un texte non vide lorsqu’une capacité a des comportements dans un modèle appliquant ce principe ; il ne prétend pas juger automatiquement sa pertinence métier. Les anciennes publications gardent leur contrat.

Grille proposée pour instruire chaque ajout :

1. **Différence utile** : quelle situation, règle ou conséquence ne peut pas être expliquée clairement au seul niveau de la capacité ?
2. **Résultat observable** : que doit-on pouvoir comprendre, comparer ou vérifier ?
3. **Responsabilité unique** : le comportement reste-t-il dans une capacité, sans masquer une décision appartenant à une autre ?
4. **Coût maîtrisé** : apporte-t-il davantage qu’un exemple ou une condition dans la fiche ?

Pas de quota de comportements ni d’obligation de décomposer toutes les capacités. Le motif « le logiciel possède un écran/API/batch » ne suffit pas. Simulation et masse ne sont pas des capacités génériques à dupliquer partout.

| Cas éprouvé | Représentation suffisante | Bénéfice ou complexité ciblée |
| --- | --- | --- |
| ATP : stock protégé, différents lieux, mobilisation lente, arrivage futur | Quatre comportements existants, combinables | Expliquer disponibilité et date de promesse sans quadrupler les capacités |
| Planning : changer une hypothèse, comparer deux répartitions, retenir un scénario | Trois comportements proposés de D05.f | Distinguer exploration et scénario retenu ; les quatre décisions restent sollicitées |
| Mettre à jour 2 000 seuils avec exceptions | Comportement proposé d’application collective de Supply Protection | Expliquer périmètre, effets partiels, erreurs et reprise ; écran/batch/flux restent des modalités |
| Suspendre 40 pièces d’un transfert de 100, puis les reporter | Comportements proposés de Lifecycle + dépendances Structuring/Promising | Ne pas confondre échéance, blocage et promesse ; pas un sous-comportement par statut |
| Préparation partielle puis transport impossible | Adaptation Decision, Orchestration, Service Order Management et leurs comportements | Distinguer choix de variation, propagation et acceptation par l’exécutant |
| Événement reçu deux fois ou correction tardive | Règle/condition du comportement d’intégration ou rapprochement | Résultat compté une seule fois ; aucun niveau « opération technique » |

## Ce que je propose de refactorer

| Ensemble courant | Recommandation | Pourquoi / arbitrage requis |
| --- | --- | --- |
| Promise Proposal, Confirmation, Revision | **Candidat principal : Promise Management**, avec comportements proposer, confirmer, réviser | Trois actions d’un même objet/cycle, aujourd’hui plus fines que Sales Order Management. À valider : autonomie réelle de ces résultats et effet sur les responsabilités adoptées. |
| Inventory Planning | Conserver et décomposer : reconfiguration, simulation/comparaison, validation du scénario | Le sens est déjà adopté ; les fiches détaillées et leurs résultats sont à instruire. **Ne pas y descendre les quatre décisions D05.** |
| Supply Protection | Conserver ; préciser gestion de validité et application collective des protections | Gouvernance et application, décisions de niveaux/quotas ailleurs. Ne pas créer Stock Protection Decision ni renommer le parent. |
| Supply Assignment / Reservation | **Clarifier avant toute fusion** | Si Reservation n’est que l’enregistrement de l’affectation, elle pourrait devenir un comportement ; si elle porte un engagement autonome, la conserver. La différence groupe/besoin identifié ne suffit pas à résoudre Assignment/Reservation. |
| Order Lifecycle Management | Conserver la responsabilité transverse ; clarifier sa nature `decision` malgré son nom Management | Séparer dans la description autorisation métier et application de transition. Ne pas choisir automatiquement action, décision ou deux capacités. |
| Order Structuring | Conserver transverse ; comportements scission, regroupement, répartition si utiles | Traçabilité et conservation des quantités sont partagées entre types d’Orders. Ne pas répéter ces comportements sous cinq parents. |
| Cinq gestions d’Orders par type | Conserver ; ajouter seulement les particularités utiles | Choix utilisateur explicite. Le CRUD générique ne justifie pas cinq arbres identiques. |
| ATP / CTP / PTP, priorités, échéancier | Conserver les décisions ; décomposer CTP seulement après test de cas | Résultats autonomes. Les modifications de politiques ou choix de services ne deviennent pas des comportements CTP. |
| Inventory Tracking / Record Inventory Movements | Conserver la distinction adoptée | État et faits/mouvements ont des résultats distincts ; nommer des opérations ne suffit pas à justifier une rétrogradation. |
| Les huit capacités D06 | Conserver ; décomposer d’abord Orchestration et Service Order Management | L’utilisateur a demandé orchestration et adaptation séparées. Tracking, rapprochement et visibilité ont des résultats distincts. |
| Six ingestions de référentiels | Conserver leurs périmètres ; partager un gabarit documentaire | Maîtres et contrats différents. Chargement complet/incrémental ou correction seulement si leur distinction est métier ; aucune capacité générique d’intégration ajoutée. |

Le regroupement des trois actions de promesse ramènerait, **à lui seul**, le catalogue de 41 à 39 capacités et introduirait trois comportements sous une nouvelle capacité. C’est un calcul de scénario, pas une cible quantitative. Une éventuelle fusion Reservation/Assignment est indépendante ; elle ne doit pas être cumulée avant clarification.

Pour une migration adoptée : figer les anciens nœuds et liens, créer des identités adaptées à leur nouveau sens, enregistrer les correspondances ancien/nouveau, requalifier les relations incidentes et reprendre seulement les validations compatibles. Aucun changement global de `kind` ni transfert automatique d’approbation. Les propositions sont isolées dans l’annexe, hors catalogue actif.

## Relations et descriptions : les vrais points faibles restants

Le backlog comporte **63 nœuds et 92 relations**, dont quatre nœuds et huit liens illustratifs historiques. Hors illustrations : **59 nœuds, 41 capacités, 4 comportements, 84 relations**. Parmi les relations, 57 sont structurelles, 27 transverses ; 24 relient des capacités. **18 capacités n’ont aucun lien transverse explicite**, dont les six ingestions. Cela mesure un manque de formalisation, pas un manque démontré de dépendances métier.

**ATP est encore isolé dans le graphe transverse**, alors que sa description consomme les stocks, protections, engagements et délais opérationnels. Son arbre de quatre comportements ne remplace pas ces liens. Les cinq capacités D04 décrivent Structuring/Lifecycle dans leurs textes mais ne disposent pas des liens correspondants. Les relations D14→D03 et D06→D03 restent au domaine ; elles ne démontrent pas toutes les dépendances fines.

Propositions prioritaires, à qualifier avant intégration :

| Consommateur → résultat requis | Contenu à expliciter |
| --- | --- |
| ATP → Inventory Visibility | Quantités admissibles présentes/futures, dimensions et fraîcheur |
| ATP → Supply Protection / Reservation / Supply Assignment | Droits et engagements pertinents sans double décompte ; fournisseur exact à arbitrer |
| ATP → Execution Capacity Visibility | Délais/capacités contextuels ; ne pas assimiler capacité de préparation et disponibilité d’un article |
| PTP / Delivery Schedule Decision → ATP | Possibilités de référence, en complément des liens CTP existants |
| Promise Proposal / Confirmation / Revision → décisions de promesse | Possibilités, arbitrages retenus, autorisations et effets d’engagement |
| Cinq gestions D04 → Structuring / Lifecycle | Transformation demandée, autorisation, application et suivi de reliquat |
| D05 Stock Allocation / Coverage Target → Supply Protection | Recommandation puis mise à jour applicable ; propriétaire de chaque seuil à confirmer |
| D05 Replenishment / Redistribution → Orders concernés | Quantités/dates proposées puis déclenchement et état de réalisation, sans attribuer leur exécution à D05 |

La direction des liens actuels mélange fournisseur→consommateur et consommateur→décision mobilisée. **Ne pas inverser les flèches automatiquement.** Proposer une lecture « a besoin de » fondée sur rôle/qualification, en préservant les échanges de résultats. Chaque dépendance a besoin d’un résultat fourni, de conditions et d’une portée ; une flèche de causalité n’est pas une séquence obligatoire.

**Qualité documentaire :** 11 capacités n’ont pas de nature renseignée, 13 n’ont pas de périmètre explicite. Il s’agit surtout de D01, des premières actions D03 et de cinq ingestions. À l’inverse, D04 et CTP ont des périmètres longs ; enlever les répétitions exige de conserver leurs frontières et exemples. Les courtes définitions D06 sont lisibles seulement avec leurs périmètres : ne pas conclure qu’elles sont vides après lecture du seul libellé.

Gabarit proposé : résultat/finalité → limites → comportements utiles → un cas concret avec quantités, échéance, exception et effet attendu → dépendances. Les noms anglais, natures et définitions détaillées non adoptés restent signalés. « Simulation » doit préciser ce qui change et ce qui est comparé ; « masse » doit préciser sélection, échecs partiels et résultat, sans architecture technique imposée.

## Manques à instruire, sans gonfler le catalogue

- **Engagements et protections :** qui transforme une affectation candidate en engagement opposable, qui le libère, et comment éviter un double décompte ? À traiter avant de déplacer Reservation.
- **Décision vers mise en action :** seuils, allocations et Orders recommandés doivent avoir un propriétaire d’application explicite, une trace de résultat et un traitement des échecs/reprises. Le nom D05 ne règle pas cette frontière.
- **Disponibilité opérationnelle :** clarifier qui connaît le délai article/emplacement et qui fournit la capacité de préparation. BHV003 explique la prise en compte, pas la production de l’information.
- **Disposition des retours :** responsabilité de réintégrer, remettre en état, rebuter ou remplacer ; le marché signale un cas à évaluer, pas l’obligation de tout internaliser dans Supply.
- **Données de décision :** demande future, incertitude, coûts, calendriers, priorités et péremption des hypothèses. D’abord leurs sources et consommateurs, ensuite seulement une capacité supplémentaire si un résultat autonome manque.
- **Objets/événements/contrats :** ils restent principalement illustratifs ; documenter progressivement promesse, affectation, protection, scénario et faits d’exécution aidera plus qu’un sous-comportement supplémentaire.

## Plan d’actions — partie 1 : autonome, sans arbitrage métier

| Priorité | Action | État / critère de résultat |
| --- | --- | --- |
| A1 | Réordonner AGENTS.md, retirer les récits datés du corps actif et conserver une capture complète | Appliqué ; autorités, règles, frontières, preuves, exécution, puis liens ciblés |
| A2 | Enregistrer U265/U266 et le principe de justification ; ajouter champ et contrôle | Appliqué ; justification ATP explicitement proposée, portées adoptées intactes |
| A3 | Corriger les six références textuelles au domaine D07 devenu D06 | Appliqué dans les scopes proposés ; identifiants D07.* conservés |
| A4 | Alléger les limitations du modèle en renvoyant l’historique à sa capture | Appliqué ; pas de catalogue ou de définition métier réécrit |
| A5 | Produire la matrice des 41 capacités, les correspondances marché et les propositions isolées | Livré ; chaque décomposition candidate porte son bénéfice/sa complexité |
| A6 | Contrôler schéma, validations existantes et immutabilité des publications ; rendre la justification lisible dans Atlas | Contrôles consignés dans le bilan ; aucune release implicite |

Les prochaines corrections purement éditoriales pourront suivre le même critère : identités, responsabilité et portées de validation inchangées. Renseigner une nature manquante, fusionner une définition ou créer une relation supposée n’entre pas automatiquement dans cette catégorie.

## Plan d’actions — partie 2 : travail conjoint et validation

| Ordre | Atelier / décision attendue | Livrable de Codex | Validation de Laurent |
| --- | --- | --- | --- |
| B1 | Éprouver la règle de décomposition sur Inventory Planning et Supply Protection | Fiches de 3 comportements Planning et 2–3 Protection, avec cas simulation/masse et justification | Résultats, limites, utilité et niveau de détail |
| B2 | Trancher Promise Management et Reservation / Supply Assignment | Deux scénarios comparés sur commande partielle, arrivage futur et réaffectation | Fusion ou maintien ; propriétaires des engagements ; migration des validations |
| B3 | Préciser Lifecycle et Structuring | Cas 100 pièces dont 40 bloquées/reportées ; transitions et effets séparés | Nature de la capacité et responsabilités ; comportements à retenir |
| B4 | Compléter les dépendances et la mise en action de D05 | Graphe caractérisé, données fournies, conditions, cas d’échec | Sens des liens, propriétaires et limites d’automatisation métier |
| B5 | Détailler D06 et examiner les manques | Cas de préparation partielle/transport défaillant ; tableau retours/données/contrats | Variations attendues, frontières avec exécutants et besoins nouveaux éventuels |
| B6 | Appliquer uniquement les arbitrages adoptés et relire la carte | Migration traçable, descriptions cohérentes, vérifications Atlas | Relecture métier ; release sur demande distincte |

**Point de départ recommandé : B1.** Il montre rapidement l’apport du nouveau niveau sans commencer par une fusion de capacités déjà adoptées. B2 vient ensuite avec une maille de comportement concrètement éprouvée.
