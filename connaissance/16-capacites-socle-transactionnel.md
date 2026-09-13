# Première vue des capacités du socle transactionnel

**Vue de travail courante après U75 (P81 version 0.4, D02 en réexamen) :** la [carte des domaines cœur éprouvée par les récits](25-domaines-coeur-et-epreuve-recits.md) propose dix domaines, 35 formulations de capacités et une matrice des cas. P81 prolonge cette étape ; ses frontières et capacités restent proposées. Les formulations ci-dessous conservent leur provenance historique.

Date : 9 septembre 2026. Priorité fixée par Laurent : [U21](01-contributions-utilisateur.md#u21), F111. Analyse Codex : A15/P63, à éprouver. Cette vue projette le [catalogue candidat](09-capacites-candidates.md) dans l’[orientation à deux couches](15-orientation-deux-couches.md). Les huit familles sont des regroupements d’exploration ; elles ne fixent ni niveaux d’urbanisme ni nouvelles capacités validées.

Portée réaffirmée en U50 : la capability map cible la couche transactionnelle ; un modèle fonctionnel distinct, orienté processus, décrira la couche processus. Le registre historique contient encore des candidats aux frontières des deux couches : les conserver avec leurs réserves ne vaut pas inclusion de tous ces candidats dans la carte du socle.

## Ce que le récit permet déjà

Le noyau le mieux décrit concerne stock, commandes et réassort chez GBM. Le récit distingue déjà des états métier, des décisions et leurs réalisations : Storeland tient le stock magasin, IRMA produit les seuils et en constitue la référence déclarée, Storeland déclenche le réassort, MAP calcule les protections marque/canal. La commande client persiste pendant les nouvelles tentatives d’exécution magasin. Sources : U03–U06, U10 ; INF01, INF04, INF05, INF10.

Ces descriptions permettent de proposer des capacités génériques sans reprendre les noms des applications. Le degré de détail varie : connaître un besoin de réservation ne signifie pas connaître son implantation ; stock présent dans UR ne signifie pas autorité de stock démontrée.

## Huit familles de travail

Dans le tableau, les verbes décrivent des responsabilités candidates, et les objets sont des repères d’analyse. Les champs du registre CAP conservent leur définition et leur statut ; les reformulations de cette vue n’en constituent pas une substitution.

| Famille proposée | Capacités du socle à explorer | Objets et résultats à préciser | Appui Beaumanoir et limite | Candidats d’origine |
| --- | --- | --- | --- | --- |
| Référentiels opérationnels | Recevoir Party / Role, Agreement et Catalog depuis leurs maîtres externes, U97/U98 | Partie/rôle, contrat de référence, catalogue ; liens par identifiants | Ingestion seule dans la plateforme. Les références articles restent utiles, articulation avec Catalog à préciser ; les lieux sont un sujet distinct en D06. Q010 partiellement répondue. | CAP001–CAP003 historiques corrigées ; P85, D09.d/D11.a/D12.a |
| Stock et disponibilité | Tenir les états et mouvements ; exposer une représentation ; déterminer une disponibilité utilisable | État de stock, mouvement, disponibilité, provenance/fraîcheur | Storeland tient les stocks magasin ; UR en reçoit des copies et contient une représentation entrepôt. Les calculs de disponibilité et l’autorité entrepôt restent inconnus. U03/U04/U10, INF01–INF03. | CAP004, CAP005, CAP006 |
| Protections et engagements de stock | Tenir et appliquer les protections ; réserver, confirmer ou libérer des quantités ; instruire les arbitrages admissibles | Protection marque/canal, quantité engagée, affectation | MAP calcule les protections et republie des données après aléa amont ; les objets remplacés et la tenue des protections applicables restent à préciser. U30 précise la réservation GBM au passage de commande ; implantation et cycle SFS à décrire. GBM sert en FIFO, sans repriorisation Gold. BRD doit couvrir les comportements cités, dont engagement futur et réaffectation prioritaire ; règles/ARun installé à explorer. U31/P69 propose la révision des promesses côté Order Promising. U02/U10/U30/U31, Q018, Q030–Q032, Q049/Q068. | CAP007, CAP008, CAP009, CAP010, CAP035 |
| Réassort opérationnel | Déterminer les paramètres ; tenir leur version applicable ; déclencher une demande d’approvisionnement | Stock optimal, seuil, paramètre applicable, demande de réassort | IRMA calcule et fait référence sur les seuils ; Storeland déclenche. Quantité demandée et publication des paramètres restent à préciser. Appui concret U06, INF04, DEC02–DEC03. | CAP011, CAP012, CAP013 |
| Commandes clients | Enregistrer la commande et tenir ses états et engagements commerciaux | Commande client, engagement commercial, états à définir | Saisie POS/web/Elastic décrite ; maintien de la commande pendant les tentatives magasin confirmé. Autorité, cycle détaillé et découpage en lignes à établir. U03–U05, Q022–Q023. | CAP014 |
| Possibilités et engagements d’exécution | Qualifier les services disponibles ; tenir charge et engagements ; déterminer les origines admissibles ; exprimer une prestation demandée ; enregistrer les résultats utiles au commerce | Service d’un lieu, quota, engagement d’exécution, demande de prestation, résultat | SFS : stock, participation et quota ; C-Log : demande EDI précisant articles, destinataire et prestations. Distinguer les responsabilités du socle, l’organisation du travail et la réalisation physique. Les retours d’état sont à documenter. U04–U07, Q015–Q019, Q040–Q043. | CAP015, CAP016, CAP017, CAP018, CAP020, CAP036 |
| Achats opérationnels | Émettre une demande fournisseur ; instruire sa transformation en engagement ferme ; tenir les faits et états opérationnels de sa réalisation | Demande d’achat, engagement fournisseur à qualifier, fait de fabrication/acheminement, état documentaire | MAP produit la demande ; CBS suit la fabrication et l’amont. U48 précise trois cas : fabrication complète fournisseur, produits finis sur catalogue et fabrication à façon avec achats séparés de composants. Dans le premier cas, MAP envoie des Planned Purchase Order. L’engagement ferme et les autorités ne sont pas établis. Séparer les faits du socle des dossiers, relances et coordinations. U03/U10, Q034–Q036. | CAP029, CAP030, CAP031, CAP032 |
| Retours et échanges | Déterminer les opérations commerciales admissibles ; autoriser un retour/échange ; enregistrer ses conséquences opérationnelles | Autorisation, retour, échange, effets sur engagements/stock à définir | SAV déclaré comme force de Sarenza, sans parcours détaillé. Les opérations proposées proviennent surtout de l’analyse initiale ; les dossiers SAV éclairent le besoin mais ne sont pas affectés globalement au socle. U01/U02, P25/P53, Q048. | CAP033, CAP034 |

## Frontières à préserver dans cette vue

Les 36 candidats ne sont pas 36 capacités du seul socle. Tous restent repérables : les huit familles mobilisent 27 candidats, dont plusieurs seulement pour une partie de leur contenu ; les neuf autres éclairent les frontières suivantes.

| Candidats | Traitement proposé pendant l’exploration du socle |
| --- | --- |
| CAP019 | Résolution de non-prise en charge : conserver la coordination humaine dans la vue processus ; expliciter les opérations du socle qu’elle sollicite. |
| CAP021, CAP022, CAP023, CAP024, CAP025 | Responsabilités du SI C-Log et de la logistique. Logistique hors développement de la plateforme FLOW, en adhérence (U58/F158) : décrire les contrats et faits échangés, en conservant l’autonomie de la filiale. CAP017 ne rapatrie pas le choix d’entrepôt dans l’ERP commercial. |
| CAP026, CAP027, CAP028 | Prévisions, anticipation de stockage, planification et lotissement des achats : documenter l’amont et ses interfaces. L’appartenance à MAP ne suffit pas à les inclure dans le socle. |

CAP007/CAP009 ont également une frontière planification/opération : examiner d’abord les protections applicables et leurs effets (CAP008), sans décider que leur calcul amont doit être internalisé. Le calcul opérationnel des seuils IRMA constitue une piste d’inclusion existante, à distinguer de la planification de saison exclue.

## Candidats dont le contenu traverse les deux couches

- CAP016 : distinguer la définition organisationnelle du quota, le paramètre applicable, la tenue de charge et le contrôle des engagements. La répartition reste ouverte (Q063).
- CAP018 : distinguer demande/engagement et transitions autorisées, puis distribution des tâches, échéances, nouvelles tentatives et escalades. La commande client conserve une identité distincte.
- CAP030–CAP032 : distinguer faits opérationnels et états opposables, d’une part, suivi de dossier et relances, d’autre part. Le suivi par CBS ne prouve pas qu’il fait autorité sur toutes les pièces.
- CAP033/CAP034 : distinguer le dossier de réclamation des autorisations et effets commerciaux qu’il mobilise ; le récit n’a pas encore fourni le détail de ces opérations.
- CAP036 : explorer l’enregistrement du résultat de préparation/expédition et ses effets opérationnels ; le travail physique en magasin et son organisation ne deviennent pas automatiquement des fonctions du socle.

Ces distinctions sont des propositions d’analyse. Aucun candidat du registre n’est déplacé, scindé ou promu comme validé par cette vue.

## Une première maille concrète pour le stock

Pour éprouver la généricité, les responsabilités suivantes donnent une première matière de définition :

| Responsabilité candidate | Résultat métier proposé | Ce qui est connu / ce qui manque |
| --- | --- | --- |
| Tenir le stock | Un état de référence et les changements qui l’expliquent, par article et périmètre | Tenue magasin déclarée ; détails des états et mouvements à décrire. Étendre le libellé au-delà du magasin est une proposition de vue, pas une modification de CAP004 ni une reprise d’autorité C-Log. |
| Exposer le stock | Une représentation consultable, avec origine et fraîcheur | Remontées batch connues ; fréquence et règles exactes à préciser (Q013). |
| Déterminer la disponibilité | Une quantité mobilisable dans un contexte et selon une politique explicites | Politique GBM de vente sur stock connue ; formule et composants à identifier (Q012/Q038). |
| Tenir les protections | Une politique applicable par marque/canal, identifiable dans le temps | Calcul MAP connu ; tenue et application à préciser (Q030). |
| Engager une quantité | Une réservation ou affectation dont les autres opérations tiennent compte | U30 précise le passage de commande comme déclencheur métier GBM ; application, événement technique et cycle SFS encore inconnus (Q018). Les liens avec les protections sont à définir. |

Cette grille évite d’assimiler quantité présente, copie de stock, disponibilité calculée, protection et engagement. Elle fournit une base pour les futurs objets et contrats, sans choisir maintenant leur découpage technique.

## Comparaison au marché

Les huit familles sont une construction d’exploration Codex à partir du récit ; aucune hiérarchie standard n’est revendiquée. Les [comparaisons existantes](../marche/comparaisons.md) restent des pistes : CMP003 pour les articles, CMP004 pour l’allocation, CMP005 pour le réassort, CMP006 pour les commandes, CMP007/CMP008 pour le service client et les retours. Elles ne valident ni le placement dans le socle ni la famille entière. La création de cette vue n’avait ajouté aucun contrôle externe. Le complément U22/U23 du même jour examine désormais le [stock chez SAP](../marche/sap-stock.md), avec CMP013–CMP017. P64/Q065 proposent notamment d’expliciter comptage, écarts et régularisation autour de CAP004 ; aucun candidat ni niveau de hiérarchie n’est adopté.

## Priorité de la prochaine exploration

Commencer par stock, disponibilité, protections, engagements et commande client : CAP004–CAP010, CAP014, partie opérationnelle de CAP018. Utiliser ensuite le réassort IRMA–Storeland (CAP011–CAP013) pour éprouver le même modèle sur un second besoin.

Pour chaque capacité, préciser résultat attendu, objets/états, décisions et règles, autorité actuelle, puis responsabilité cible et contrat. Les questions Q011/Q012/Q018/Q023/Q030 constituent déjà les principaux points d’entrée ; la priorité donnée au socle ne les résout pas. Aucun nouveau fait d’existant n’est déduit de cette proposition.

## Exploration du bloc stock après l’étude de marché

Les apports U26/U27 sont analysés dans [l’exploration du bloc stock](17-exploration-bloc-stock.md) : états/mouvements/visibilité, disponibilité par usage, allocations/protections/engagements. P66 propose de rattacher les opérations à l’objet modifié et de qualifier le stock virtuel/logique avant un bloc supplémentaire. Ces regroupements restent exploratoires ; la présente vue et les définitions CAP ne sont pas remplacées.

## Politiques et frontière de la promesse

Les [apports U30/U31](18-politiques-engagement-gbm-brd.md) précisent le besoin BRD et proposent de placer la révision des promesses dans Order Promising. Cette distinction affine les interactions étudiées dans la famille protections/engagements sans fixer une nouvelle hiérarchie. P68/P69, CMP022/CMP023.

## Première liste de domaines après U47

La [liste de domaines à éprouver](20-domaines-candidats.md) reprend les récits et les candidats de cette vue pour discuter des espaces de problèmes cohérents. Elle distingue un noyau déjà décrit et les zones à compléter. Les huit familles ci-dessus restent une vue exploratoire antérieure ; ni leur remplacement par une hiérarchie validée ni un déplacement de CAP ne sont effectués.

## Complément sur les achats après U48

Les [trois cas d’achat et la question de l’orchestration](21-achats-et-orchestration.md) enrichissent la matière achats. La fabrication à façon éprouve les liens entre achats, ressources confiées et prestations. Ces pistes ne créent pas trois capacités ni un domaine Orchestration ; Q034 reste ouverte, Q069 précise les inconnues. CAP029 reçoit un complément de réalisation sourcé et un rapprochement marché partiel en CMP030 ; ses intitulé, résultat et statut restent inchangés.

## Réexamen de la maille après U53–U57

Les [précisions OMS/Supply et le cas des transferts](23-reassort-transferts-et-promesse.md) remettent à l’étude la maille des familles Commandes, Réassort et Retours : les types de parcours commerciaux de l’OMS ne sont pas automatiquement des domaines transactionnels. La Supply possède aussi des décisions propres de rééquilibrage, prévision et gestion des impondérables. Identifier les aptitudes génériques et leurs règles ; les candidats historiques restent conservés sans reclassement automatique.

U58 précise le périmètre de réalisation : la logistique est hors développement FLOW, en adhérence. La présence d’une aptitude Supply dans l’analyse ne l’attribue pas à la plateforme. Les [interactions et responsabilités à la frontière](23-reassort-transferts-et-promesse.md#périmètre-flow-et-adhérence-logistique) restent à décrire ; aucun reclassement des candidats CAP n’en est déduit.

## Description des capacités et modèle métier après U61

La [grille objets, états, faits et documents](24-capacites-objets-et-faits.md) propose de préciser le résultat des aptitudes et les informations auxquelles elles donnent sens. Ces éléments restent dans des vues liées ; ce ne sont pas de nouvelles capacités par simple présence d’un objet ou d’un événement. P80 conserve la proposition ; les 36 fiches candidates restent inchangées.

U62/F164 confirme aussi des objets dans le modèle processus, avec Demande de réassort comme exemple. L’étude des objets à partir de cette vue des capacités vise ceux du socle et leurs relations aux objets du processus ; elle ne réserve pas l’expression objet métier au transactionnel. Voir les [deux modèles](24-capacites-objets-et-faits.md#des-objets-métier-dans-les-deux-couches).

**Actualisation U100 — 11 septembre 2026 :** [P81 version 0.7](25-domaines-coeur-et-epreuve-recits.md) distingue maintenant la réception de Product Reference (D08.d) et celle de Catalog (D12.a), aux côtés de Party / Role et Agreement. Les anciennes capacités D08.a–c restent retirées. La [Supply orientée documents d’autorisation](26-supply-documents-autorisations.md) réoriente la revue D04/D07 ; les variantes commerciales ne prescrivent pas des domaines transactionnels Achat/Vente séparés. Les regroupements historiques de cette note restent des pistes, pas la carte courante.
