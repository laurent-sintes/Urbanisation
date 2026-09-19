# Supply Protection — étude des comportements

> **Réorientation U282 — 17 septembre 2026.** La liste de 17 opérations ci-dessous est remise en question comme décomposition en comportements. Elle reste une matière fonctionnelle documentée pour la conception produit. La cible doit être reconstruite à partir des mécanismes de protection : risque, principe, conditions et effet métier. Les cinq comportements existants sont en réexamen ; aucun nouveau catalogue de mécanismes n’est encore adopté.

Étude du 17 septembre 2026, U279–U281. **Proposition, sans ajout au catalogue actif.**

Le panel couvre Microsoft, SAP, Oracle (Fusion et Retail), IBM, Blue Yonder, Kinaxis, RELEX, Slimstock et o9. La liste recherche une couverture complète des mécanismes utiles au périmètre FLOW ; elle ne prétend pas épuiser toutes les offres du marché.

La proposition détaillée et les sources font autorité dans [l’annexe YAML](../modeles/backlog/supply-protection-review.yaml). Les sections ci-dessous restituent cette annexe ; les familles de lecture ne sont pas des niveaux du modèle.

## Lecture marché

Les ERP documentent précisément les opérations et la vie des paramètres. Les spécialistes complètent la couverture des risques (cycle produit, place, obsolescence, multi-échelon) mais leurs pages publiques donnent moins de preuves sur les opérations transactionnelles. Ces deux niveaux de preuve restent distincts.

Trois résultats structurent la recommandation : des seuils sans méthode de réassort sont insuffisants ; une configuration préparée ne prouve pas son application ; prévenir les futurs excédents ne résorbe pas à lui seul le surstock déjà présent.

## Mécanismes couverts

| Mécanisme | Candidats | Appuis consultés | Bénéfice |
| --- | --- | --- | --- |
| Droits par groupe et limites de consommation | P01–P06, P09 | SAP / Microsoft | Pénurie et concurrence entre usages |
| Sécurité, seuil de réassort, cible et limite haute | P07 | Microsoft / SAP / Oracle | Pénurie et surstock |
| Unités ou jours de couverture, niveaux variables dans le temps | P07, P11 | Microsoft / Oracle | Éviter des seuils fixes devenus inadéquats |
| Méthode Min/Max, point de commande, cycle périodique et lots | P08 | Microsoft / Oracle | Encadrer les apports et le risque d’excédent |
| Minimum de présentation, place disponible et stock de démonstration | P07, P08, P10 | Oracle Retail / RELEX | Tenir compte des contraintes magasin sans concevoir les rayons |
| Fin de vie, arrêt progressif, dates de début/fin du réassort | P08, P11, P13 | RELEX / Oracle Retail / Slimstock | Limiter le stock résiduel ; dates de saison reçues en entrée |
| Durée de vie résiduelle / péremption | P08, P09, P17 | RELEX / Microsoft | Cas conditionnel selon produits ; règle reçue, pas gestion qualité |
| Segments, exceptions article-lieu, règles héritées | P10, P14, P16 | Oracle / IBM / Blue Yonder | Éviter ambiguïtés de portée et décisions locales invisibles |
| Activation, arrêt, application collective et lecture de l’effectif | P11–P16 | SAP / Oracle / Microsoft | Distinguer préparation et application |
| Détection d’écarts bas/haut et réexamen | P17 | IBM / RELEX / Kinaxis | Maîtriser les règles dans la durée, rattachement à arbitrer |

## Liste candidate et justification

Cinq comportements existants ; dix nouveaux candidats de cœur de périmètre ; deux candidats conditionnels. Tous seraient directement sous Supply Protection. Aucun sous-comportement.

| Repère / nom | Résultat | Exemple fictif | Complexité ou bénéfice justifiant la maille | Appui / statut |
| --- | --- | --- | --- | --- |
| P01 **Allocation** | Attribuer une enveloppe initiale à un groupe. | Le web reçoit 300 pièces. | Créer des droits utilisables distincts de ressources affectées à une commande. | S01 ; existant U278/U279 |
| P02 **Reallocation** | Transférer des droits disponibles entre groupes. | 50 pièces de droits web passent aux magasins. | Conserver un total partagé tout en changeant de bénéficiaire. | S01 ; existant U278/U279 |
| P03 **Allocation Release** | Restituer les droits inutilisés au disponible commun. | 20 pièces non utilisées cessent d’être protégées. | Différencier restitution et changement de bénéficiaire. | S01 ; existant U278/U279 |
| P04 **Allocation Consumption** | Imputer un usage à une enveloppe. | 80 pièces de droits sont consommées. | Maintenir un solde sans confondre consommation de droits et sortie physique. | S01 ; existant U278/U279 |
| P05 **Allocation Visibility** | Consulter les droits alloués, consommés et restants. | Le canal consulte son solde et les mouvements qui l’expliquent. | Lire la disponibilité des droits, distincte de celle du stock. | S01 ; existant U278/U279 |
| P06 **Allocation Consumption Reversal** | Corriger ou annuler une imputation de consommation et rétablir les droits selon les règles applicables. | Une annulation de commande rend 10 droits à une enveloppe encore valide. | La libération de droits inutilisés ne corrige pas un usage déjà enregistré. | S05 ; proposé |
| P07 **Coverage Threshold Setting** | Enregistrer et réviser les niveaux de sécurité, déclencheurs, cibles et limites hautes retenus, avec leurs unités et leurs effets. | Pour un magasin : sécurité 40, réassort sous 60, cible 100 ; préciser séparément un éventuel plafond strict. | Distinguer les sémantiques de seuils pour éviter pénurie ou apports excessifs. | S02, S03, S06, S07 ; proposé |
| P08 **Replenishment Rule Setting** | Configurer la méthode de réassort, les contraintes et conditions de renouvellement à appliquer. | Révision chaque lundi, complément jusqu’à la cible, multiples de colis et arrêt à la date de retrait. | Un même seuil donne des résultats différents selon méthode, fréquence et contraintes. | S02, S07, S08, S10 ; proposé |
| P09 **Consumption Rule Setting** | Configurer qui peut utiliser les protections et selon quelles restrictions ou priorités de groupes. | Un groupe prioritaire peut utiliser une ressource sous conditions ; un autre reste plafonné. | Distinguer minimum protégé, plafond et priorité, sans arbitrer les commandes individuellement. | S01, S05 ; proposé |
| P10 **Protection Scope Assignment** | Rattacher une politique de protection à des produits, lieux ou groupes, avec les règles de priorité des rattachements. | Une règle commune couvre un groupe de magasins ; une exception identifie un article-lieu. | Maîtriser les héritages et éviter qu’une règle s’applique au mauvais périmètre. | S07, S08, S16 ; proposé |
| P11 **Protection Scheduling** | Programmer les valeurs et changements de règles sur leurs périodes de validité. | La cible passe de 100 à 60 après la promotion puis revient à 40. | Préparer des changements futurs sans altérer la règle applicable aujourd’hui. | S03, S05, S09 ; proposé |
| P12 **Protection Activation** | Rendre une configuration applicable à son périmètre. | Les nouveaux seuils deviennent effectifs à la date retenue. | Distinguer donnée préparée et règle utilisée ; automatisation possible. | S05, S08, S09 ; proposé |
| P13 **Protection Deactivation** | Suspendre ou arrêter l’application d’une configuration pour son périmètre. | Arrêter le réassort automatique d’un article en retrait, tout en conservant d’autres protections. | Un arrêt de règle diffère d’une suppression de données ou d’une libération de droits. | S05, S08, S09 ; proposé |
| P14 **Protection Override** | Appliquer une dérogation explicite à une règle, avec périmètre, priorité et durée maîtrisés. | Un magasin conserve temporairement une cible différente du groupe. | Préserver la règle commune tout en rendant l’exception visible et réversible. | S07 ; proposé |
| P15 **Protection Mass Update** | Appliquer une modification à un ensemble de protections et rendre compte de ce qui a été appliqué ou rejeté. | Modifier 2 000 couples article-lieu et traiter les exceptions identifiées. | La maîtrise des résultats partiels justifie le comportement ; le nombre de lignes ou l’interface ne suffit pas. | S04, S08 ; à arbitrer |
| P16 **Protection Visibility** | Consulter la configuration effectivement applicable, sa validité et les dérogations qui l’expliquent. | Expliquer pourquoi le magasin utilise une cible de 80 alors que la règle commune indique 100. | Différencier règle, valeur proposée et état effectif ; ne pas doubler Allocation Visibility pour les soldes. | S03, S07, S09 ; proposé |
| P17 **Protection Monitoring** | Détecter et signaler les écarts aux règles de protection et les situations requérant un réexamen. | Stock projeté au-dessus de la limite ou quota presque épuisé. | Passer de la consultation à la détection d’exception ; rattachement à arbitrer avec Inventory Visibility. | S11, S13, S17 ; à arbitrer |

## Points de modélisation à préserver

- Coverage Target Decision détermine les valeurs ; Coverage Threshold Setting configure les valeurs retenues. Stock Allocation Decision reste distincte des opérations sur enveloppes.
- Replenishment Decision détermine les apports nécessaires. Configurer une méthode ou un plafond ne crée ni ne lance un Order. D04 et D06 conservent leurs responsabilités.
- Supply Assignment lie les ressources aux besoins ; Reservation engage une quantité. Le fait consommant les droits et les corrections doivent prévenir les doubles déductions.
- Protection Scheduling programme une applicabilité ; Inventory Planning construit et éprouve des scénarios. Aucune simulation, analyse d’impact ou validation de scénario copiée sous Protection.
- Allocation Release restitue des droits encore inutilisés ; Consumption Reversal corrige des droits consommés ; Protection Deactivation arrête une règle. Aucun effet automatique sur un engagement existant présumé.
- Replenishment Rule Setting configure les contraintes déjà connues ; les maîtres Product, Agreement et Network restent externes. Les décisions de fournisseur, substitution ou service ne sont pas absorbées.
- Les plafonds de stock souhaitables, les cibles Min/Max, les plafonds de consommation et les capacités physiques sont différents. Une cible haute peut être dépassée par des contraintes de lots ; un plafond strict doit être explicitement qualifié.
- La configuration d’une limite de place ne mesure pas la capacité opérationnelle : D06 fournit le contexte exécutant pertinent. La conception du planogramme ou de l’assortiment ne devient pas une responsabilité Supply Protection.
- La surveillance de seuils peut utiliser Inventory Visibility et des projections ; elle ne recalcule pas une optimisation. Le rattachement exact de P17 reste un arbitrage.
- Un surstock existant peut nécessiter redistribution, retour, report/annulation d’apport ou écoulement. Les règles orientent ces réponses mais ne les exécutent pas. La décision de réduire ou reporter des apports reste à vérifier dans D05 ; ne pas la prétendre couverte par la seule définition actuelle de Replenishment Decision.
- Finance, démarque commerciale, disposition/destruction, conformité, planification de saison et création de prévision ne sont pas intégrées implicitement à cette capacité. Leurs contraintes utiles peuvent être reçues.

Les contrôles de cohérence (unités, dates, valeurs incompatibles), la traçabilité et les modalités écran/batch/flux/streaming sont des exigences des comportements concernés. Un comportement supplémentaire ne sera justifié que par un résultat ou une complexité métier propre.

P15 est justifié seulement si la prise en charge des résultats partiels et des exceptions constitue un besoin métier ; Oracle atteste la modification collective, pas notre contrat de reprise proposé. P17 reste à arbitrer avec Inventory Visibility ; les calculs d’optimisation et l’analyse d’impact de scénario restent en D05.

## Priorités de revue

1. P07 Coverage Threshold Setting : sécurité, déclencheur, cible, plafond
2. P08 Replenishment Rule Setting et P09 Consumption Rule Setting
3. P06 correction de consommation et frontière Reservation
4. P10–P14 et P16 : portée et vie des règles
5. P15 et P17 : utilité et rattachement à arbitrer

## Sources primaires et limites

| Source | Produit / passage | Édition et accès | Portée / limite |
| --- | --- | --- | --- |
| S01 [Inventory Visibility inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation) | Microsoft ; Business background; Use the allocation APIs; Consume as a soft reservation | Page évolutive ; mise à jour affichée 2025-08-13 ; ouvert et lu | Enveloppes par groupe, opérations et soldes. Ne couvre pas toute la protection FLOW. |
| S02 [Replenishment methods and quantity modification](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification) | Microsoft ; Coverage codes; Impact of the order quantity; Min/Max examples | Page évolutive ; mise à jour affichée 2026-07-01 ; ouvert et lu | Méthodes, seuils et contraintes de lots. Le maximum Min/Max peut être dépassé dans certains cas de multiples. |
| S03 [Safety stock fulfillment for items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment) | Microsoft ; Set safety stock; Minimum key; Min/max; FEFO; safety stock constraint | Page évolutive ; édition non spécifiée ; ouvert et lu | Niveaux par lieu, dates et variations temporelles ; distinguer sécurité, disponibilité et commande. |
| S04 [Use the safety stock journal to update minimum coverage for items](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal) | Microsoft ; Overview; Calculate minimum coverage based on historical usage | Page évolutive ; édition non spécifiée ; ouvert et lu | Propositions de valeurs, analyse d’impact et mise à jour effective sont distinguées. |
| S05 [Outlining aATP with Supply Protection (SuP)](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-) | SAP ; Activation; Core/Prioritized Protection; Time Buckets; Consuming Supply Protection | Cours S/4HANA ; édition précise non indiquée ; ouvert et lu | Groupes, priorités, temporalité, consommation et annulation. Le périmètre SAP SuP est plus étroit que FLOW. |
| S06 [Executing Demand-Driven Replenishment in SAP S/4HANA](https://learning.sap.com/courses/exploring-production-planning-in-sap-s-4hana/executing-demand-driven-replenishment-in-sap-s-4hana) | SAP ; Buffer Profiles; Buffer Level Calculation; Manage Buffer Levels; Schedule MRP Runs | Cours S/4HANA ; édition précise non indiquée ; ouvert et lu | Buffers : sécurité, point de commande et maximum ; propositions puis utilisation des paramètres. DDMRP est une méthode, pas un niveau FLOW. |
| S07 [Policy Assignment Sets](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html) | Oracle ; Policy Parameters; Default Policy Values; Policy Overrides; Hierarchy | Fusion Cloud 26B ; ouvert et lu | Politiques par segment, dérogations article-lieu et ordre de priorité. Ne pas importer les contraintes techniques de volumétrie. |
| S08 [Activating Items on Replenishment](https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmpug/activating-items-replenishment.htm) | Oracle ; Creating Attributes; Managing Attributes at Item List Level; Replenishment Attributes Window | Pointeur latest ; numéro de version non affiché dans la page lue ; ouvert et lu | Périmètres article-lieu, mises à jour collectives, présentation et activation/désactivation. Aucune maîtrise de référentiel FLOW déduite. |
| S09 [Manage Scheduled Updates](https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmpug/manage-scheduled-updates.htm) | Oracle ; Create a Scheduled Update; Manage Scheduled Updates | Pointeur latest ; numéro de version non affiché dans la page lue ; ouvert et lu | Changements datés de paramètres et de statut ; ce n’est pas une simulation de scénario. |
| S10 [Replenishment and allocation](https://www.relexsolutions.com/solutions/automatic-replenishment-system/) | RELEX ; Key features; store space; seasonal items; new product introductions and ramp-downs | Page produit évolutive ; version non indiquée ; ouvert et lu | Espace, durée de vie et retrait progressif. Appui de cas métier ; opérations détaillées non établies par cette page. |
| S11 [Inventory Planning Software](https://www.relexsolutions.com/solutions/inventory-planning-software/) | RELEX ; Inventory policies, thresholds and exceptions | Page produit évolutive ; version non indiquée ; ouvert et lu | Seuils et écarts ; aucune preuve d’une interface transactionnelle précise. |
| S12 [Inventory Optimization](https://blueyonder.com/solutions/supply-chain-planning/inventory-optimization) | Blue Yonder ; Features & Capabilities; Dynamic Segmentation; Multi-echelon Optimization | Page produit évolutive ; version non indiquée ; ouvert et lu | Segmentation et optimisation ; surtout appui des frontières D05, sans détail suffisant de cycle de règle. |
| S13 [What is Inventory Optimization](https://www.kinaxis.com/en/inventory-optimization) | Kinaxis ; Techniques; Key inventory optimization activities | Article évolutif ; version logicielle non indiquée ; ouvert et lu | Cibles, politiques, visibilité et exceptions ; pas catalogue contractuel des fonctions installées. |
| S14 [Inventory Management Software — Slim4](https://www.slimstock.com/solutions/inventory-management-software/) | Slimstock ; Key features: stocking policies; stock parameters; network balancing | Page produit évolutive ; version non indiquée ; ouvert et lu | Politiques de stockage liées au cycle produit ; optimisation et rééquilibrage dépassent Protection. |
| S15 [Allocation & Replenishment](https://o9solutions.com/solutions/merchandise-planning/allocation-replenishment) | o9 ; Core Building Blocks; Advanced Building Blocks | Page produit évolutive ; version non indiquée ; ouvert et lu | Distingue moteur, règles, visibilité et transmission des Orders ; allocation peut signifier distribution vers les lieux. |
| S16 [Safety stock rules](https://www.ibm.com/docs/en/sip?topic=inventory-managing-safety-stock-rules) | IBM ; Safety stock rules; Network level; Node level | Sterling Inventory Visibility / SIP ; version non précisée ; texte indexé lu ; ouverture directe en erreur | Règles par réseau/nœud, mode de livraison et article. Comparaison limitée au passage indexé. |
| S17 [Inventory monitor](https://www.ibm.com/docs/en/order-management-sw/9.5.0?topic=monitors-inventory-monitor) | IBM ; Introduction; inventory availability above/below configured quantities | Sterling Order Management 9.5.0 ; référence historique ; texte indexé lu ; ouverture directe en erreur | Appui historique de surveillance de seuils ; ne prouve pas la couverture de l’édition courante. |

Les sources sont consultées le 17 septembre 2026. Les extraits de recherche non retenus (notamment pages Oracle 26D et anciens guides PDF) ne fondent aucune recommandation. Aucune documentation éditeur ne prouve un déploiement Beaumanoir.
