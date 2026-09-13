# Order Promising — noms, nature et couverture des capacités

Comparaison du 11 septembre 2026, demandée par Laurent en U89. État comparé : [P83](../connaissance/05-propositions.md#p83), quatre capacités proposées pour D03 dans [la carte de travail](../connaissance/25-domaines-coeur-et-epreuve-recits.md#proposition-de-présentation-u87u88). Analyse Codex, non validée ; ELM078–ELM081 et CMP047. Les noms, le nombre et les frontières restent proposés.

## Résultat

**Les quatre aptitudes ont des appuis de marché, mais leur découpage ne reproduit aucun des modèles examinés et leur couverture détaillée reste insuffisamment démontrée.** P83 distingue surtout les résultats possibles, confirmés, affectés et révisés. SAP RBA rend davantage visibles les problèmes particuliers à résoudre pour promettre : disponibilité, allocations, alternatives et nouvel approvisionnement.

Microsoft apporte aussi des alternatives de fourniture ; il ne faut donc pas le réduire au seul calcul ATP. Oracle Global Order Promising confirme l’intérêt d’examiner plusieurs solutions de fourniture. Ces descriptions de produits éclairent des aptitudes métier, sans fournir à elles seules une hiérarchie native de Business Capabilities.

## 1. Noms et nature des quatre propositions

« Nature » est examinée sous deux angles : aptitude métier ou autre objet dans la source ; type de contribution dans notre modèle. Les qualifications ci-dessous sont proposées, sans valider une nouvelle taxonomie à la place de [P72](../connaissance/19-glossaire-metier.md#hypothèse-sur-les-natures-de-capacité). Adapter n’est pertinent que lorsqu’un engagement ou un objet existe déjà ; toute confirmation initiale n’est pas une adaptation.

| Proposition locale | Nature de contribution envisagée | Noms et comportements de marché rapprochés | Appréciation du nom et de la maille |
| --- | --- | --- | --- |
| **Supply Feasibility** — D03.a | Évaluer ou déterminer une possibilité de fourniture, sans engager par cette seule évaluation. | SAP **Product Availability Check** ; Microsoft **ATP**, **CTP** ; Oracle **available-to-promise**, **capable-to-promise**. | Aptitude crédible, nom local large. **Product Availability Check** est mieux attesté pour le contrôle des ressources existantes/attendues ; il ne désigne pas à lui seul toute la recherche d’alternatives. Le nom actuel risque de masquer plusieurs problèmes. |
| **Confirmation** — D03.b | Décider et établir un engagement de quantité/date ; Adapter lors de ses modifications. | La confirmation est un résultat de PAC chez SAP ; Microsoft **Order promising** ; Oracle **Global Order Promising**. | Résultat métier pertinent, mais pas feuille autonome de même nom démontrée dans les catalogues consultés. **Promise Confirmation** serait plus explicite hors contexte ; option lexicale locale seulement. Sa séparation d’avec calcul et révision demande une justification métier. |
| **Supply Assignment** — repère historique D02.e, rattaché à D03 | Décider de la couverture d’une demande par des ressources ; Adapter lors d’une réaffectation ou libération. | SAP **Supply Assignment** ; Microsoft **Reservation** pour une partie du lien ressource/demande. Oracle : rapprochement à approfondir, sans équivalence exacte établie ici. | Le nom a un appui SAP direct et exprime bien une aptitude indépendante du moteur Allocation Run. La réservation Microsoft peut recouvrir une partie de cette aptitude : frontière avec D01 à préciser. |
| **Promise Revision** — D03.c | Réévaluer, puis éventuellement Adapter les engagements selon les règles autorisées. | SAP **Backorder Processing** ; Microsoft recalcul de promesse dans certaines modifications de commande ; Oracle réexamen de solutions de fourniture. | Nom local clair sur l’objet et l’effet. **Backorder Processing** est plus reconnaissable chez SAP, mais ne signifie pas seulement traiter les demandes sans couverture. La page Microsoft ne prouve pas un arbitrage global entre commandes équivalent au besoin Boardriders. |

Sources : [SAP PAC et BOP](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/using-advanced-available-to-promise-aatp-in-sap-s-4hana_ef38afd2-4730-433f-854a-613b8e4afec5), [Microsoft Order promising](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-dates-available-promise-calculations), [Oracle GOP 26B](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fascp/overview-of-global-order-promising.html) ; réservation et affectation déjà qualifiées en ELM071/ELM072. Relations de recouvrement partiel et appuis sémantiques ; aucune équivalence complète déduite du nom.

Les quatre définitions peuvent respecter notre définition de capacité. En revanche, énumérer les étapes « calculer, confirmer, affecter, réviser » ne suffit pas à démontrer quatre périmètres autonomes. Il faut éprouver leurs règles propres, leurs résultats et leurs relations, sans imposer une séquence de traitement.

## 2. Ce que l’on peut compter

| Référence et périmètre effectivement observé | Nombre observé | Nature de ce qui est compté | Conclusion permise |
| --- | --- | --- | --- |
| P83, Order Promising local | **4** | Capacités candidates, rattachées au domaine local D03. | Point de départ de cette comparaison, pas couverture validée. |
| SAP RBA, colonne Order Promising du schéma pédagogique | **5** | Éléments présentés au rang **Business Capability**, sous une **Business Area**. | Comparaison de maille pertinente, mais extrait pédagogique sans édition ni exhaustivité du catalogue établies. |
| Microsoft, page Order promising | **5** | Méthodes de contrôle des dates : Sales lead time, ATP, ATP + Issue margin, CTP et CTP for Planning Optimization. | Variantes de calcul et de réalisation ; ce ne sont pas cinq capacités. D’autres comportements sont décrits dans Delivery alternatives. |
| Oracle GOP 26B, section Principles of Promising | **7** | Principes de choix de fourniture, pas sept capacités. | Source de critères de couverture ; aucun nombre natif comparable établi. |
| TM Forum et Business Architecture Guild, corpus consulté | **Non établi** | Composants/API publics TM Forum et exemples méthodologiques Guild ; catalogue détaillé pertinent non consulté. | Ni zéro capacité ni preuve d’absence. Pas de comparaison numérique défendable pour Order Promising. |

Le schéma SAP a été **relu visuellement le 11 septembre 2026**. Chemin natif : Enterprise Domain **Supply - Fulfill Demand** → Business Domain **Supply Chain Execution** → Business Area **Order Promising**. Le tableau suivant transcrit les cinq libellés, avec retours à la ligne normalisés. [Cours et schéma officiels](https://learning.sap.com/courses/sap-enterprise-architecture-framework-foundation-introduction/discovering-the-reference-architecture-content).

| Capacité SAP RBA visible | Accueil dans P83 et la carte locale | Couverture et frontière à préciser |
| --- | --- | --- |
| **Product Availability Check** | Supply Feasibility, avec Confirmation pour le résultat engagé. | Principe explicite ; équivalence de toutes les règles non établie. |
| **Product Allocation Check** | Faisabilité/confirmation, en lien avec Supply Protection de D01. | Partiel : administrer une protection et vérifier les droits d’une demande à consommer une allocation sont deux contributions à distinguer. PAL n’est pas automatiquement identique à SUP. |
| **Product Substitution** | Pas de résultat explicite dans P83 ; propriétés produit en D08 comme appui possible. | Lacune documentaire : connaître des produits ne signifie pas savoir décider d’une substitution admissible pour une demande. |
| **Fulfillment Location Determination** | Supply Feasibility et D06.c, options d’exécution admissibles. | Partiel à l’échelle de la carte ; le problème a déjà un accueil. Il faut définir qui évalue, choisit et promet, sans dupliquer D06 ni reprendre les autorités C-Log. |
| **Supply Creation Based Confirmation** | Faisabilité/confirmation, avec D04/D07 pour l’approvisionnement. | Partiel : le futur déjà attendu est décrit ; provoquer une nouvelle fourniture pour rendre la promesse possible ne l’est pas explicitement. |

**Cinq contre quatre ne mesure pas un déficit d’une capacité.** Les découpages se croisent. Supply Assignment et Promise Revision ne sont pas visibles dans cette colonne SAP, mais sont éclairés par d’autres documentations SAP ; on ne peut pas conclure à leur absence chez l’éditeur.

## 3. Couverture éprouvée sur dix critères explicites

Cette grille est une **construction d’analyse locale**, établie à partir des sources ci-dessous et des distinctions déjà travaillées. Ses dix lignes ne sont ni dix capacités recommandées ni l’ensemble des capacités du marché. « Explicite » signifie que le résultat figure dans P83 au niveau du principe ; cela ne démontre ni ses règles détaillées ni une réalisation installée.

| Critère de couverture | Appui de marché | État local actuel | Conséquence pour l’étude |
| --- | --- | --- | --- |
| 1. Évaluer quantité/date à partir des ressources présentes et futures admissibles | SAP PAC, Microsoft ATP, Oracle ATP | **Explicite** — Supply Feasibility, avec contraintes amont/aval U80. | Préciser règles de calcul et degré de certitude du futur. |
| 2. Établir ce qui est promis à une demande | SAP confirmation ; Microsoft et Oracle promising | **Explicite** — Confirmation. | Préciser la portée engageante et distinguer une simple réponse de simulation. |
| 3. Couvrir une demande avec des ressources déterminées | SAP Supply Assignment ; recouvrement partiel des réservations Microsoft | **Explicite** — Supply Assignment. | Définir les effets communs avec Reservation, sans compter deux fois un engagement. |
| 4. Réexaminer les promesses, notamment après changement de priorité | SAP BOP ; Microsoft réexamen plus limité dans la page consultée | **Explicite** — Promise Revision, besoin Boardriders U30/U31. | Définir les engagements révisables et les règles de préemption. |
| 5. Vérifier la part allouée que la demande peut consommer | SAP Product Allocation Check ; règles d’allocation Oracle | **Partiel** — protection D01 connue ; contrôle par demande non isolé dans P83. | Décrire la décision et son lien avec les protections, avant de créer une capacité. |
| 6. Choisir une origine de fourniture admissible | SAP lieu de fourniture ; Microsoft Delivery alternatives ; Oracle sourcing | **Partiel** — D06.c propose déjà les options. | Éprouver la frontière D03/D06 et l’autorité C-Log. |
| 7. Déterminer une substitution de produit acceptable | SAP Product Substitution ; variantes Microsoft ; substitution Oracle | **Non décrit explicitement** dans P83. | Capacité ou contribution à explorer ; besoin local à confirmer, variantes et substitutions générales non équivalentes. |
| 8. Promettre en mobilisant une fourniture à créer | SAP SBC ; Microsoft CTP/alternatives d’achat ; Oracle CTP | **Partiel** — potentiel fournisseur U79, mais lien causal demande → nouvelle fourniture non défini. | Séparer consommation de futur existant et création de futur ; ne pas importer Manufacturing ou la planification de saison. |
| 9. Construire une réponse partielle ou répartie dans le temps/entre origines | SAP ABC ; Microsoft Delivery alternatives ; Oracle fractionnement | **Partiel** — variante évoquée dans l’audit, définition et règles absentes de P83. | Peut enrichir la définition d’une capacité existante ; pas nécessairement une nouvelle capacité. |
| 10. Arbitrer entre solutions faisables selon leur coût de fourniture | Oracle profitable-to-promise ; comparaison des transports Microsoft | **Non décrit explicitement** dans P83. | Suggestion de marché, pas besoin local déclaré. Critère possible de décision ; « optimiser » reste une Finalité. |

**Bilan sur ces dix critères : quatre explicites, quatre partiels, deux non décrits.** Ce bilan porte sur la précision de notre définition et ses points d’accueil, pas sur un pourcentage de conformité au marché. Les critères 7 et 10 ne deviennent pas des besoins Beaumanoir par leur seule présence dans les produits. Les critères 5, 6 et 8 méritent un examen de frontière avant toute augmentation du nombre.

Appuis détaillés : [Microsoft Delivery alternatives](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-alternatives), [SAP création de fourniture pour confirmation](https://learning.sap.com/courses/performing-the-availability-check/acquiring-a-basic-understanding-of-available-to-promise-atp-_ae470c8e-1483-46ce-b5cc-e80647e8a32b), [Oracle règles d’allocation 26B](https://docs.oracle.com/en/cloud/saas/readiness/scm/26b/order26b/26B-order-mgmt-wn-f42969.htm). SAP ABC et Oracle GOP sont dans les sources de la section 1.

## 4. Conclusion pour la prochaine itération

Conserver les quatre propositions comme hypothèse de départ, sans conclure qu’elles suffisent. Examiner d’abord **allocation consommable, alternatives de lieu, substitution et création d’approvisionnement** ; décider ensuite si chacun nécessite une capacité autonome, une définition enrichie ou un lien vers un autre domaine. Le nom Supply Feasibility mérite le premier réexamen parce qu’il rassemble potentiellement ces problèmes. Supply Assignment dispose du meilleur appui lexical direct parmi les quatre titres.

Les récits du périmètre historique de Beaumanoir et de Boardriders justifient le noyau présent/futur, affectation et réexamen prioritaire. Ils ne démontrent pas toutes les règles d’alternatives proposées par les éditeurs. Cette comparaison élargit donc l’épreuve de l’[audit précédent](../audits/2026-09-11-order-promising.md), sans invalider ses distinctions ni adopter des capacités supplémentaires.

## 5. Périmètre des preuves et limites

- **SAP RBA — ELM078, MKT04 :** schéma public de cours, rangs et cinq libellés visibles ; définitions détaillées des cinq feuilles indisponibles dans l’image, édition inconnue. Les comportements sont éclairés séparément par le produit, sans identité de version présumée.
- **SAP S/4HANA — ELM079, MKT13 :** cours aATP, sections PAC, PAL, BOP, ABC et Release for Delivery ; cours ATP, passage SBC consulté dans un extrait indexé détaillé. Vérification le 11 septembre 2026, sans édition globale. SBC décrit le recours à PP/DS en édition privée/on-premise ; pas de généralisation à toutes les offres SAP. Release for Delivery éclaire aussi la frontière D07/processus, sans entrer dans les dix critères retenus.
- **Microsoft — ELM080, MKT14 :** Order promising, mise à jour affichée du 21 avril 2026 ; Delivery alternatives, 29 septembre 2021. Textes publics lus, cinq méthodes dans la première page et options dans la seconde. Pas de version produit homogène établie ni de catalogue natif de capacités extrait. Les limites des moteurs CTP restent propres aux produits.
- **Oracle — ELM081, MKT20 :** documentation Fusion Cloud 26B, GOP et règles d’allocation partagées avec Backlog Management. Ce corpus est distinct d’Oracle Retail Reference Model MKT05. Le cycle complet d’affectation et le réexamen global du backlog ne sont pas établis par les passages retenus. Le PDF de présentation Backlog Management identifié n’a pas pu être ouvert ; aucune assertion détaillée n’en est tirée.
- **TM Forum/Guild :** limites déjà consignées en ELM065 et dans l’étude initiale ; pas de consultation nouvelle des catalogues membres. La qualification de service TM Forum est un rapprochement partiel, pas une identité avec la promesse commerce.

Sources publiques synthétisées sélectivement et liées ; aucun catalogue intégral importé. Aucun fonctionnement du déploiement Beaumanoir ni choix de produit cible démontré. Application de la [méthode](methode.md), maintien des archives, identifiants et validations antérieurs.

## Suite de la discussion — U90

Le 11 septembre 2026, Laurent propose **Promise Verification** et **Promise Confirmation**, et apprécie **Supply Assignment** et **Promise Revision**. La comparaison ci-dessus conserve les noms historiques qu’elle examinait en U89. La [vue courante P83](../connaissance/25-domaines-coeur-et-epreuve-recits.md#proposition-de-présentation-u87u88) intègre les candidats U90 ; [CMP048](comparaisons.md#cmp048) précise l’appui métier ATP et les distinctions. Les dix critères de couverture et leurs réserves restent applicables : un changement de nom ne résout pas les points partiels ou non décrits.

**Suite U91/U92 :** ajout des aptitudes de décision dans la [vue courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md#capacités-de-décision-ajoutées-à-lexploration-u91), avec propriétaires proposés. Promise Verification est rejeté ; Promise Formulation devient le candidat assistant pour faire naître une promesse. CMP049. La grille U89 reste le diagnostic de son état comparé, pas une évaluation réactualisée de couverture après ces ajouts.

**Suite U93 :** l’acheminement est rendu explicite par le candidat Fulfillment Route Decision, au-delà du choix de source. [CMP050](comparaisons.md#cmp050) examine SAP Transportation Management, Microsoft et Oracle et distingue la promesse du plan de transport détaillé. Promise Proposal est le nouveau candidat après rejet de Promise Formulation ; [vue courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md#capacités-de-décision-ajoutées-à-lexploration-u91). La grille U89 demeure le diagnostic de l’état antérieur.

## ATP et CTP chez Microsoft — U94

Complément du 11 septembre 2026, ELM084/CMP051. **ATP comprend déjà les approvisionnements futurs planifiés.** La distinction pertinente porte sur les ressources disponibles ou attendues, puis sur les possibilités supplémentaires de fourniture, pas sur présent contre futur.

| Notion | Question métier — reformulation | Appui Microsoft |
| --- | --- | --- |
| Available-to-Promise — ATP | Quelle quantité non engagée pouvons-nous promettre, à quelle date, sur la base des ressources présentes et des réceptions prévues ? | Supply Chain Management et Business Central. |
| Capable-to-Promise — CTP | Que pouvons-nous rendre disponible pour couvrir la demande, compte tenu des moyens et délais nécessaires ? | Supply Chain Management explicite composants et capacités de fabrication ; Business Central décrit le scénario de production, achat ou transfert pour la quantité manquante. |

**Exemple construit pour le modèle local :** une demande porte sur 100 articles, 30 sont libres maintenant et 40 libres attendus vendredi. Le raisonnement ATP peut fonder une réponse sur ces 70, sous réserve des dates et règles. Pour les 30 manquants, un raisonnement CTP examine une fourniture supplémentaire et ses contraintes. Il ne garantit pas qu’une solution sera trouvée ; une proposition peut rester partielle ou plus tardive. Exemple indépendant des formules ou paramètres Microsoft, sans description de configuration Beaumanoir.

Pour P83, les deux raisonnements peuvent contribuer à Promise Proposal ; CTP éclaire notamment Supply Creation Decision. Les domaines amont fournissent la faisabilité utile. Cette lecture ne crée pas deux capacités supplémentaires et n’importe pas Manufacturing ou la planification de saison dans FLOW. Un droit contractuel d’achat ne garantit pas une date ou une capacité fournisseur.

**Précision documentaire :** la liste Microsoft de cinq méthodes relevée dans la section 2 est conservée comme état de la page générale. La page détaillée CTP expose aussi Near real-time CTP et Batch CTP, avec conditions de version/configuration ; C62. Ce sont des modalités techniques distinctes du contraste métier ATP/CTP. Sources exactes, sections et limites en [ELM084](elements.md#elm084).

**Décision U95 — 11 septembre 2026, Laurent :** les quatre capacités d’action et cinq capacités de décision d’Order Promising sont validées. [Vue courante](../connaissance/25-domaines-coeur-et-epreuve-recits.md#d03-promesse-de-fourniture), CMP052. ATP est associé à la promesse ; CTP reste au glossaire mais son placement est différé, la piste analytique n’étant pas adoptée. Supply Creation Decision demeure validée. Les analyses U89/U94 ci-dessus sont conservées comme preuves et hypothèses datées ; elles n’imposent plus une contribution CTP au modèle local.
