# Commandes et prévisions dans un même Planning — Microsoft, U565/U566

Microsoft documente cette combinaison dans ses produits de planification ERP. Le périmètre des fonctions OMS consultées reste différent.

| Produit / document | Cas couvert | Conséquence pour FLOW |
| --- | --- | --- |
| Dynamics 365 Supply Chain Management — Master planning with demand forecasts | Un master plan peut inclure commandes et prévisions, avec consommation paramétrable de la prévision par la demande réelle. | Appui au plan commun ; le produit génère aussi des Planned Orders, au-delà du plan d’affectation FLOW. |
| Dynamics 365 Business Central — Balancing supply and demand | Les commandes et la prévision restante entrent dans le profil de demande du planning. | Confirme la combinaison et la nécessité de distinguer demande totale et restante. Le document écarte des prévisions les liens contraignants order-to-order : pas équivalence automatique avec une affectation appliquée. |
| Intelligent Order Management — Intelligent Fulfillment Optimization | Des commandes reçues sont optimisées ensemble ; un fulfillment plan donne des résultats par ligne. | Appui au scénario du carnet. L’optimisation conjointe de forecasts dans ce moteur n’est pas démontrée par la documentation consultée. |

Exemple fictif : 600 ventes au total sont attendues et 300 sont déjà commandées. Si ces commandes appartiennent à la prévision considérée, la demande à couvrir comprend 300 commandées et 300 encore prévues, pas 900. Un arrivage de 500 laisse 100 sans couverture. U565 retient un même Planning pour comparer les scénarios de partage ; aucune priorité ou répartition chiffrée n’est adoptée.

Demand Planning rapproche la demande attendue et les commandes connues ; D03.p prépare et actualise les scénarios d’affectation communs, Fulfillment Plan Decision en détermine le résultat avec les décisions spécialisées, Supply Assignment matérialise les liens. Reservation conserve l’engagement bloquant les usages concurrents. La couverture amont qui produit les Planned Orders n’est pas reconstruite.

Le mécanisme général de plan commun est documenté sur le marché. La hiérarchie FLOW et la séparation de ses responsabilités restent un choix de modèle ; ni préférence universelle d’éditeur ni innovation de principe n’est démontrée. Le nom Order Backlog Planning est désormais plus étroit que le périmètre U565 et reste à qualifier.

Sources primaires consultées le 21 septembre 2026 : [Microsoft SCM, Master planning with demand forecasts](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/demand-forecast) (mise à jour affichée 27 juillet 2026), [Microsoft Business Central, Balancing supply and demand](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-balancing-demand-and-supply) (documentation évolutive), [Microsoft IFO architecture](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) (mise à jour affichée 30 janvier 2026). ELM573, ELM574, ELM403 et CMP236 conservent les passages et limites.
