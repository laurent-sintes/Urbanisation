# FLOW — audit approfondi de préparation V0

**Demande U434 · 19 septembre 2026 · conclusions et recommandations proposées**

**Mise à jour U435/U436 : les corrections évidentes ont ensuite été appliquées.** Le [rapport des modifications](modifications.md) est le point d’entrée pour l’état final ; les mesures et constats ci-dessous décrivent l’état initial et restent conservés comme preuve. La frontière réservation/affectation a été tranchée par Laurent en U436.

**Le socle de capacités est solide, mais le modèle a encore besoin d’une remise en cohérence éditoriale et d’interactions plus explicites avant d’être présenté comme une V0 stabilisée.** L’audit ne démontre pas de grand domaine fonctionnel manquant dans le périmètre Supply retenu. Il établit plusieurs contradictions de lecture, des liens utiles absents du graphe et des sujets dont la responsabilité ou le contrat restent ouverts. Les références consultées confortent largement les responsabilités existantes ; elles révèlent surtout où les rendre plus précises.

Une revue de travail avec les PO, experts et architectes est possible avec les réserves du [kit de revue](kit-revue-v0.md). Pour une présentation annonçant une base stabilisée, traiter d’abord les lots 1 à 4 ci-dessous. Une V0 de cartographie n’exige pas que tous les contrats de réalisation soient finalisés : les décisions ouvertes doivent être identifiées et correctement délimitées.

## Périmètre, méthode et limites

L’autorité auditée est `modeles/backlog/model.yaml`, empreinte SHA-256 `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`. Les descriptions courantes, les deux glossaires, les annexes de décision utiles, les conventions, le panorama et les contrats de restitution ont été examinés. Trois analyses indépendantes couvrent cohérence, relations et éditeurs ; leur consolidation distingue preuve, interprétation et recommandation.

Le contrôle est exhaustif pour les identités et relations du graphe, le recensement des champs et la revue des 47 capacités. L’épreuve sémantique s’appuie sur les fiches et les scénarios détaillés dans les annexes. **La comparaison marché est large, pas exhaustive de toutes les fonctions de toutes les éditions des produits.** Aucun score global de couverture n’est calculé : processus, capacités, fonctionnalités et standards de données n’ont pas le même dénominateur.

La release affichée par Atlas a été résolue par son index, son descripteur puis son snapshot : `2026-09-19.1`, révision 8. Elle comporte 135 nœuds et 323 relations. Les champs des nœuds communs sont identiques au backlog ; quatre illustrations et leurs huit relations sont volontairement exclues. Leur absence dans Atlas n’est pas une perte de couverture.

U431 reste une clôture historique valide. Ses quatre travaux futurs sont repris comme questions ouvertes, sans recréer P04/P10/P12 ni annuler les accords. U434 autorise un nouvel audit, pas une adoption globale des propositions. Cette phase initiale conserve catalogue et publications ; U435 autorise ensuite les corrections décrites dans le rapport de modifications. Les publications restent inchangées.

## Résultats mesurables

| Contrôle | Résultat | Ce que cela établit |
| --- | --- | --- |
| Inventaire courant | 139 nœuds, 331 relations, 47 capacités, 74 comportements, 110 termes métier | Base exacte de l’analyse, illustrations comprises |
| Structure | Aucun lien vers un nœud absent, aucun cycle structurel, aucun double parent structurel détecté | Arbre exploitable ; ne prouve pas la pertinence de chaque frontière |
| Comportements | 22 capacités décomposées, justification présente pour chacune ; 74 comportements à parent unique de même couche, sans enfant | Convention terminale respectée ; 25 capacités sans comportement ne constituent pas 25 manques |
| Liens textuels du modèle | 216 références `model:` ; aucune cible cassée détectée | Navigation interne cohérente ; une référence textuelle ne crée pas une relation métier |
| Liens métier du backlog / publiés | 198 / 190 ; les 190 publiés ont un sens renseigné | L’absence de qualification des huit illustrations ne concerne pas la V0 publiée |
| Qualification des liens | 177 `needs`, aucun libellé/verbe propre ; 115 conditions et 130 effets réduits à une formule générique répétée | Information présente mais souvent trop peu discriminante pour expliquer un passage métier |
| Comparaisons en fiche | 24/47 capacités et 61/74 comportements avec `market_comparisons` ; 223 entrées, toutes `proposed` | Rapprochements nombreux mais inégalement exposés ; absence du champ ≠ absence d’étude documentaire |
| Portée des accords | 38/47 capacités portent `urbanist_validated`, mais 20/47 portent explicitement `definition` dans `lifecycle.validated_fields` | Le badge d’un élément ne valide pas toute sa description ; les autres preuves doivent rester examinées à leur portée |
| Applicabilité structurée | 4 contextes, 0 évaluation | Aucune heatmap de couverture installée ne peut être déduite de ce registre |
| Validation du dépôt | `python scripts/validate_models.py` : 0 erreur | Intégrité et contrats contrôlés ; les défauts sémantiques et de lisibilité ci-dessous restent réels |

Sources reproductibles : [métriques générales](metrics.yaml), [métriques des liens](metrics-liens.yaml), [inventaire complet des liens](inventaire-liens.md), scripts [baseline](audit_baseline.py) et [graphe](audit_links.py). Les compteurs sont des observations de champs, pas des scores de maturité. En particulier, `release_complete_capability_count: 0` utilise le statut technique `review=accepted` ; il ne signifie pas que les 47 capacités sont sans valeur ni sans accord.

## Les points qui tiennent bien

**La séparation des responsabilités est robuste.** Stock, demande, décision de satisfaction, promesse, application et orchestration ne sont pas confondus. D03 et D05 partagent des moyens possibles mais gardent des finalités différentes. Les mouvements n’effacent pas la distinction entre propriétaire, détenteur et localisation. Les référentiels restent des projections de maîtres externes.

**Les variantes majeures sont déjà présentes.** Les types d’Orders, les retours selon leur résultat, la consignation, la livraison directe, le lancement et le réassort, la redistribution et les trois échelles de cibles de stock sont représentés. L’audit n’établit pas un besoin de recommencer la décomposition des comportements.

**L’exécution garde sa place.** Orchestration, choix d’adaptation, demandes de services, suivi et rapprochement sont distingués. Une réussite technique ne vaut pas réalisation métier. Les opérations internes du WMS, du transport et du magasin ne deviennent pas automatiquement des capacités à développer dans FLOW.

## Les constats prioritaires

Les priorités ci-dessous portent sur la préparation du support V0. Elles sont distinctes d’une criticité d’exploitation. « Avant conception » signifie que le catalogue peut être discuté avec une question ouverte clairement affichée.

| ID | Constat et preuve | Risque pour le lecteur | Traitement recommandé |
| --- | --- | --- | --- |
| V0-F01 | Textes restés à une structure antérieure : D01 cite encore Order Promising ; BHV045–047 renvoient la structure des Orders à D04 alors que D04.n est dans D03 ; alternatives et limitations conservent des sujets déjà remplacés | Les lecteurs reconstituent plusieurs modèles différents à partir des mêmes fiches | **Avant présentation** : corriger les textes courants à partir des relations actuelles, conserver les décisions antérieures dans leur historique |
| V0-F02 | Formulation Intercompany / modes de satisfaction copiée dans D01.h/BHV063–065, sans pertinence pour ces comportements de consignation | Doute sur la fiabilité éditoriale et la différence entre variants | **Avant présentation** : supprimer ou remplacer la phrase hors sujet ; ne pas élargir l’accord métier |
| V0-F03 | 177 dépendances `needs` ; conditions/effets souvent génériques ; Atlas force le libellé « A besoin de » pour cette famille | Les relations sont visibles mais leur apport métier reste difficile à comprendre | **Avant présentation** : qualifier d’abord les interactions critiques ; adapter leur restitution si Atlas est le support retenu. Ajouter des labels seuls au YAML ne suffit pas |
| V0-F04 | Liens décrits par le texte mais absents du graphe, notamment D03.p → D03.o, orchestration → autorisations Lifecycle, promesse → confirmation fournisseur et fil de consignation | Le graphe ne permet pas de reconstruire les cas pourtant couverts par les fiches | **Avant présentation** : instruire les liens proposés avec résultat, orientation et limites, sans convertir toute mention textuelle en flèche |
| V0-F05 | D03.k PTP, D03.l échéancier et D03.m priorités ont une précision inégale ; calendriers/coupures/fuseaux peu explicites dans les descriptions opérationnelles | Les responsabilités existent mais leurs entrées, arbitrages et résultats sont difficiles à confronter au réel | **Avant présentation** : enrichir la fiche de décision et un cas concret ; la réalisation des règles temporelles appartient à la conception |
| V0-F06 | Réservation opposable, effet d’application d’un plan, capacité engageable et interfaces externes restent ouverts U431 | Un architecte peut prendre une possibilité décrite pour une garantie de contrat | **Afficher avant présentation**, trancher avant engagement de réalisation ; ne pas rouvrir le catalogue pour résoudre toute règle |
| V0-F07 | Le choix du devenir d’un stock consigné après saison et le porteur de gestion des politiques de réservation restent explicitement à instruire dans les annexes | Une décision ou une application peut rester sans responsable clair | **Question métier ciblée** : choisir responsabilité existante ou extension justifiée ; aucune nouvelle capacité automatique |
| V0-F08 | Comparaisons en fiche absentes de 23 capacités, alors que plusieurs études et nouveaux rapprochements existent | Les PO ne voient pas l’argumentation ou lisent une position marché antérieure au périmètre courant | **Avant présentation** sur les fiches prioritaires : reporter les rapprochements vérifiés avec statut proposé, différences et limites ; élargir ensuite par lot |
| V0-F09 | Portées de validation partielles, vocabulaire historique et méthodologique présent parmi les termes métier | « Publié » ou « validé » peut être compris comme accord global ; bruit lexical à l’atelier | **Avant présentation** : légende des statuts et vocabulaire de lecture resserré, sans effacer identifiants ni preuves |
| V0-F10 | Peu de contrats explicites sur données tardives/corrigées, origine des prévisions/assortiments et versions de références | Solutions plausibles mais non vérifiées sur les exceptions et temporalités | **Avant conception** : contrats minimaux pour les scénarios concernés, sans créer une capacité par problème technique |
| V0-F11 | Aucun objet/document/événement métier de production dans le graphe publié ; Business Services reste non décomposé | La carte peut être prise pour une architecture métier et de solution complète | **Avant présentation** : annoncer la portée et joindre un petit jeu d’objets échangés/scénarios ; pas d’inventaire exhaustif imposé |
| V0-F12 | Panorama partiel et applicabilité non renseignée ; Sarenza non évalué | Une cible générique peut être présentée à tort comme couverture réelle des trois SI | **Avant présentation** : distinguer cible, pertinence, couverture documentée et réalisation installée ; étude As Is séparée |

Preuves et nuances : [cohérence](coherence.md), [liens](liens.md), [marché éditeurs](marche-editeurs.md), [standards](standards.md). Les registres détaillés portent les identifiants locaux, les éléments touchés et les recommandations ; cette synthèse les regroupe sans créer de nouveaux éléments métier.

## Ce que la comparaison marché apporte

L’étude éditeurs croise SAP, Microsoft, Oracle, IBM Sterling, Manhattan, Blue Yonder, RELEX et o9. Leurs sources n’ont pas toutes la même force : documentation de fonction, formation officielle, présentation de produit ou seulement texte officiel indexé lorsque l’ouverture échoue. Les limites sont conservées source par source dans [le registre marché](marche-editeurs.yaml). Aucun déploiement Beaumanoir n’est déduit d’une capacité produit.

Le résultat principal est un **recouvrement fonctionnel large, avec une maille différente** : les suites regroupent souvent décision, calcul, orchestration et application dans un même module ; FLOW les distingue. Le nom d’un module n’impose pas un domaine et un autre vocabulaire ne prouve pas un manque. Les termes Allocation, Backlog, CTP et Release doivent conserver leurs précisions de sens.

Trois exemples de différences qui justifient du travail concret : les calendriers de source de fulfillment rendent explicites les jours travaillés et délais ; la réservation de visibilité distingue l’engagement souple de sa consommation ; le changement d’une commande orchestrée nécessite des actions de compensation selon son avancement. Ce sont des appuis pour préciser les contrats FLOW, pas une invitation à recopier les mécanismes produits. Sources officielles : [Microsoft — calendriers](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/setup-fulfillment-source-calendar), [Microsoft — réservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations), [Oracle — compensation](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faiom/compensate-sales-orders-that-change.html).

Les cadres transverses complètent ces comparaisons : BIZBOK pour capacité/comportement/réalisation, SCOR pour éprouver les passages entre activités, GS1 pour le sens et la correction des faits, ArchiMate pour les relations. APQC Retail a été localisé, mais son détail est resté derrière un formulaire ; il n’a pas été utilisé comme preuve de couverture élémentaire. Voir [sources et correspondances](standards.md).

## Manques réels, interfaces et fausses alertes

**Manques constatés :** actualisation de certains textes, exposition de relations déjà soutenues par les fiches, qualification utile des liens, homogénéité des fiches de décision et visibilité des questions ouvertes. Le modèle doit mieux montrer qui reçoit quel résultat et ce qui change à la suite de celui-ci.

**Périmètres voisins à relier :** prévision et assortiment, politique commerciale, autorisations de retour, paiement/facturation, sourcing et négociation, qualité/conformité et opérations physiques. Leur existence dans une suite de marché ne démontre pas qu’ils doivent devenir des domaines internes de Supply. Pour les prévisions, l’origine et le contrat d’entrée doivent notamment être clarifiés : l’absence de capacité dédiée n’est pas à elle seule un défaut établi.

**Sujets à vérifier selon les cas réels :** rappels/quarantaine, péremption, conditionnements complexes, multi-entités, nouvelles formes de livraison ou d’économie circulaire. Les mécanismes actuels peuvent contribuer à ces besoins, mais l’audit ne certifie ni leur couverture détaillée ni leur applicabilité aux trois SI. Un récit réel et une frontière précise sont nécessaires avant d’étendre le catalogue.

**Fausses alertes écartées :** identifiant D02/D04/D07 sous un autre domaine, absence de comportement sous chaque capacité, absence de lien métier sur chaque comportement, exclusion des illustrations de la release, absence de domaines Finance/WMS, statuts encore proposés et absence de scoring de maturité. Aucun de ces éléments n’est une anomalie par lui-même.

## Chemin recommandé vers une V0 propre

| Lot | Travail concret | Critère de sortie | Arbitrage nécessaire |
| --- | --- | --- | --- |
| 1 — Cohérence courante | Traiter F01/F02 ; nettoyer alternatives/limitations actives ; employer les noms et parents actuels | Aucun passage courant contradictoire avec le graphe ou les décisions applicables ; historique préservé | Un changement de sens reste proposé, une reprise éditoriale doit citer sa base |
| 2 — Interactions prioritaires | Traiter F03/F04 ; six familles de liens prioritaires avec sens, résultat, conditions et effets | Vente partielle, confirmation fournisseur, consignation et retour lisibles sans supposer de flèches cachées | Valider les interactions nouvelles à leur portée ; ne pas déduire causalité ou cardinalité |
| 3 — Fiches de décision | Traiter F05 et report marché F08 : ATP/CTP/PTP, échéancier/priorités, promesse/réservation, plan et exécution | Pour chaque fiche prioritaire : question, entrées, critères, résultat, application, cas contradictoire, comparaison | Pas de formule universelle ni décision produit imposée |
| 4 — Support et statut V0 | Traiter F09/F11/F12 et utiliser le kit ; préparer trois parcours et la légende d’accord | Un lecteur distingue immédiatement adopté, éditorial, ouvert, externe et non évalué | Accord sur le périmètre de présentation ; aucune validation globale de description |
| 5 — Contrats et responsabilités | Instruire F06/F07/F10 à partir des six décisions du kit | Responsable et résultat définis pour chaque interaction retenue ; inconnus de réalisation consignés | Ateliers experts/architectes ciblés ; ne bloque pas la carte si les limites sont visibles |
| 6 — Contrôle et publication éventuelle | Vérifier l’état corrigé et les champs modifiés ; produire une nouvelle publication lorsqu’elle sera demandée | Contrats/intégrité réussis, rendu cohérent, preuves et anciennes publications inchangées | Publication distincte de validation métier, commit et push distincts |

Je recommande de commencer par les lots 1 et 2 : ils corrigent les incohérences les plus visibles tout en conservant le socle. La décision la plus utile n’est pas de créer un domaine supplémentaire ; c’est de choisir et rendre explicites les responsabilités et interactions que la V0 doit permettre de discuter.

## Livrables et preuve de réalisation de l’audit

- [Cohérence et revue détaillée des capacités](coherence.md).
- [Audit des relations et propositions orientées](liens.md), [inventaire exhaustif](inventaire-liens.md).
- [Comparaison éditeurs](marche-editeurs.md) et [sources/correspondances structurées](marche-editeurs.yaml).
- [Standards et limites d’accès](standards.md).
- [Kit de revue : 16 cas, 6 décisions, critères de présentation](kit-revue-v0.md).
- [Métriques et empreintes](metrics.yaml), [résultat des vérifications](verification.yaml).

Les contrôles initiaux ont été exécutés sur l’état audité. Les sources ont été réindexées après enregistrement fidèle des demandes ; les changements U435/U436 ont ensuite fait l’objet de contrôles ciblés sur l’état corrigé. Les documents d’audit sont des analyses, distinctes des accords. Le report des rapprochements prioritaires vers `fields.market_comparisons` a été réalisé sous U435, avec statut proposé. L’état final et les limites restantes figurent dans [modifications.md](modifications.md).
