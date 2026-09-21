# Un plan Supply commun — vérification U567

La combinaison est documentée chez Microsoft : le master planning peut affecter une ressource existante et proposer un nouvel achat, tandis que Batch CTP calcule les dates à partir du plan dynamique. SAP fournit aussi des mécanismes de création d’apports et d’optimisation intégrée, mais leur attribution à ARun seul serait incorrecte.

| Mécanisme | Ce qui est documenté | Limite |
| --- | --- | --- |
| Microsoft Master Planning + Batch CTP | Plan dynamique, dates des commandes, emploi d’apports existants et propositions d’achats. | CTP n’est pas nécessaire pour toute proposition d’achat ; aucune garantie d’optimum global. |
| SAP ARun via Backorder Processing | Affectation/réaffectation du stock et des réceptions futures, avec prise en compte des protections configurées. | La présence d’apports planifiés ne signifie pas leur création ; le recalcul des seuils n’est pas démontré. |
| SAP SBC / PP/DS | Création de planned orders, purchase requisitions et stock transfer requisitions pour un manque. | La matrice SAP 2025 FPS01 précise que BOP ne déclenche pas cette création. |
| SAP IBP Supply Planning Optimizer | Optimisation conjointe des achats, de la production, des mouvements et du stock. | Planification par périodes, distincte d’ARun et de l’application transactionnelle aux commandes. |

Le principe formulé par Laurent est donc étayé dans sa faisabilité : un plan Supply retenu peut coordonner la satisfaction des demandes et les ajustements de ressources. Son unicité est un choix FLOW de cohérence. Plusieurs scénarios, itérations et calculs spécialisés peuvent y contribuer ; ils doivent partager les contraintes et ne pas appliquer des conclusions finales incompatibles. Un calcul batch ne suffit pas à garantir la cohérence ni l’optimalité hors du modèle de contraintes considéré.

Exemple fictif : 600 ventes attendues, dont 300 commandées ; un arrivage de 500 dont 100 sont retardées ; une cible de stock final distincte de 50. À l’échéance, 400 sont disponibles pour 650 de besoin total dans cet exemple : 250 restent à couvrir. Un scénario peut combiner achat, transfert, révision d’échéance ou proposition de changement de cible. La faisabilité, les coûts, les engagements et les conséquences sur les autres demandes décident du résultat. Une proposition d’achat de 250 ne devient pas un achat ferme par son seul calcul.

La frontière U555 doit être revue : ne pas refaire un plan déjà produit reste pertinent ; exclure sa responsabilité métier au motif qu’un outil la réalise ne l’est pas. La refonte doit conserver décisions spécialisées, configuration, autorisation des engagements et application distinctes. Les hypothèses concernant le fonctionnement installé chez Beaumanoir restent des apports utilisateur, sans flux ou réalisation supplémentaires déduits.

Sources : [Microsoft Batch CTP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp), [Microsoft exemple d’affectation et nouvel achat](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/dynamic-positive-days), [SAP restriction SBC/BOP](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f132c385e0234fe68ae9ff35b2da178c/95cbb18b60da470cac8d340f0c6f5251.html), [SAP SBC dans PP/DS](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f899ce30af9044299d573ea30b533f1c/4c56297de7c33a0de10000000a42189c.html), [SAP IBP Supply Planning Optimizer](https://help.sap.com/docs/SAP_INTEGRATED_BUSINESS_PLANNING/c1fb60cb1e9c49d99ada277ae57e9e6c/deb28978d5ba4c64bad78edcab913228.html).

Les pages SAP retenues ont été consultées via leur texte primaire indexé ; les ouvertures directes n’ont pas fourni de texte exploitable. Titres, éditions, passages et limites des neuf documents sont conservés dans [l’annexe structurée](../../modeles/backlog/integrated-supply-plan-U567.yaml), CMP237.
