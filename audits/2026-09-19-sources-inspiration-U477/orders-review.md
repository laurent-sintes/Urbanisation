# Revue croisée Orders — U477

Les choix, synthèses et exemples des 65 profils ont été relus. Avis favorable après huit précisions ciblées dans `orders-output.yaml` ; aucun builder ni fichier d’autorité modifié.

- **BHV036** : affermir ne prouve pas à lui seul accord fournisseur, réservation ou autorisation de lancement.
- **BHV051** : le contrôle final renseigne l’état du bien ; Return Disposition Decision garde le choix de son devenir.
- **TER033** : le sens Oracle est précisé comme accord engageant l’achat à long terme, ensuite décliné en commandes. La réserve sur le document MAP reste entière.
- **TER038** : l’exemple distingue approbation interne et quantités reçues/restantes, sans présenter cette approbation comme accord fournisseur.
- **TER064 / TER069** : historique du retrait de Business Services et portée des accords lexicaux conservés en notes internes, retirés de la synthèse publique.
- **VER001** : distinguer définition et application d’une règle n’impose pas deux capacités.
- **VER017** : un réexamen peut confirmer l’existant ; une modification n’est pas obligatoire pour parler de révision au sens de la définition d’entrée.

Les frontières consignation/achat, crédit/remplacement/réparation, commande/document/fait, gel/suspension/lancement sont cohérentes. Les intentions des transferts restent distinctes de la décision des quantités et de la réalisation physique. Les illustrations construites sont attribuées à FLOW.

Relectures documentaires ciblées le 19 septembre 2026 : [Oracle Purchasing — Planned Purchase Orders et Scheduled Releases](https://docs.oracle.com/cd/E26401_01/doc.122/e48931/T446883T443953.htm), [Oracle Consigned Inventory](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faims/consigned-inventory.html), [Microsoft — approbation et confirmation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-approval-confirmation), [Oracle — back-to-back et retour du produit inutilisé](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/how-orchestration-processes-back-to-back-flows.html). Les autres consultations restent celles du relevé initial ; cette revue ne prétend pas les répéter exhaustivement.

Contrôles réellement exécutés sur l’état corrigé : `scripts.market_comparison.validate_comparisons` et `validate_inspiration`, égalité des identifiants avec l’entrée, deux documents distincts minimum, deux ou trois paragraphes de synthèse et exemples complets. Résultat : **42 nœuds, 23 termes, 137 comparaisons, 65 exemples, zéro erreur**.

Ne pas régénérer cet output avec le builder antérieur sans reporter ces précisions.
