# Complément TM Forum — U249

Consultation officielle le 16 septembre 2026. Comparaison ciblée des services d'exécution, pas du retail. Les éléments ELM129/131/132 sont revérifiés ; aucune conformité TM Forum ni équivalence globale de capacités n'est affirmée.

| Clé | Source, version et passage effectivement lu | Observation et limite |
| --- | --- | --- |
| TM01 | [TMF633 Service Catalog Management v4.0](https://www.tmforum.org/open-digital-architecture/open-apis/service-catalog-management-api-TMF633/v4.0), Overview et version affichée | L'API porte le cycle des éléments de catalogue. D14 est une **projection** de catalogue : sa seule ingestion ne couvre donc pas toute l'administration TMF633. C'est un choix de frontière, pas une lacune à combler localement. Schéma détaillé non audité. |
| TM02 | [TMF641 Service Ordering Management v4.2](https://www.tmforum.org/open-digital-architecture/open-apis/service-ordering-management-api-TMF641/v4.2), Overview et historique de version ; stable affichée au 14 août 2026 | Demandes de service, évolution, consultation et notifications : appui partiel à D07.b. La page ne démontre ni un cycle universel achat/vente/prestation, ni toutes les modalités d'annulation physique. Schéma détaillé non audité. |
| TM03 | [TMFC007 Service Order Management v1.2.1](https://oda-production.s3.eu-west-2.amazonaws.com/v1.0.0/TMFC007_Service_Order_Management_v1.2.1.pdf), approuvé 2 juillet 2024 ; p. 5 et 9–11, fonctions 571 et 598 | Ce composant ODA regroupe choix de solution technique, coordination et délégation. La fonction 598 décrit les dépendances entre items de Service Order ; 571 mobilise capacité/charge pour une date de prestation. Cela soutient les contrats D06 et D03. Le composant est plus large que notre capacité Service Order Management ; sa maille ne doit pas imposer une fusion locale. Contexte télécom et ressources techniques, pas promesse retail. |

**Interprétation d'audit :** conserver catalogue, gestion des demandes, coordination, suivi et adaptation comme responsabilités distinctes est défendable. Le manque prioritaire est l'explicitation des résultats échangés : besoin de prestation, service retenu, demande prise en charge, résultat attendu, estimation, fait et écart. Ce sont des candidats à documenter comme objets/événements ; ils ne créent pas automatiquement sept capacités.

La séparation D06.d Orchestration / D06.f Adaptation Decision répond à la règle locale de modélisation. Les sources consultées ne prouvent pas un découpage natif identique ; ce choix reste une adaptation FLOW. La latitude d'adaptation relève des règles opérationnelles et ne bloque pas le catalogue (U243).

Accès : pages HTML et texte du PDF ouverts ; passages cités localisés. TMF633/641 affichent Apache 2.0 sauf mention contraire et guides RAND ; TMFC007 indique RAND. Liens et synthèses sélectives uniquement, sans redistribution des modèles ou spécifications.
