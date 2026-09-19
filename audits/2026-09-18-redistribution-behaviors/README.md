# Redistribution — accord U318 intégré

Deux comportements sont ajoutés directement sous **Stock Redistribution Decision (D05.c)** :

| Identifiant | Mécanisme adopté | Nom anglais éditorial | Définition adoptée |
| --- | --- | --- | --- |
| BHV024 | Rééquilibrage entre sites | Inventory Rebalancing | Déplacer du stock vers les lieux qui en ont davantage besoin, en préservant les besoins des donneurs. |
| BHV025 | Consolidation de stocks dispersés | Stock Consolidation | Regrouper des quantités fragmentées pour leur redonner une utilité ou libérer des sites. |

La consolidation couvre les deux cas soumis à Laurent : **reconstituer des assortiments de tailles** dans certains magasins et **regrouper les reliquats** vers des lieux adaptés. Ces cas restent dans un seul comportement ; aucun niveau supplémentaire. Le bénéfice est confronté aux coûts et risques ; pénurie constatée et excédent ne sont pas des préconditions universelles.

Les noms anglais n’avaient pas été présentés dans la proposition validée : ils sont enregistrés comme formulations éditoriales, pas comme noms adoptés. La nouvelle définition de synthèse du parent et la justification rédigée sont également proposées ; l’ancienne définition et son empreinte restent dans la capture pré-U318.

Les comparaisons Oracle, Nextail et SAP sont conservées sur le parent et les comportements concernés, avec leurs limites. Stock Consolidation SAP EWM est interne à l’entrepôt ; FLOW décrit ici une décision intersites. D04 gère les Orders, D03 leur satisfaction et D06 les prestations ; la décision ne réalise pas le transfert physique.

L’audit marque P06/P07 comme intégrés dans leur périmètre révisé. P01–P03 sur le réassort et les autres sujets restent ouverts. [implementation.yaml](implementation.yaml) conserve les portées et empreintes ; les captures `*-before.yaml` préservent l’état précédent.

Backlog : **40 capacités, 16 comportements**. Aucune release déclenchée : Atlas continue à présenter la publication sélectionnée.
