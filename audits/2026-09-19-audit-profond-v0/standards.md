# Standards et cadres transverses — audit U434

État consulté le 19 septembre 2026. Analyse proposée, appliquée au backlog dont l’empreinte figure dans [metrics.yaml](metrics.yaml). Les identifiants STD-V0 sont locaux à cet audit. Ils ne créent aucun élément adopté dans le modèle.

## Ce que les références permettent de conclure

La comparaison porte sur des objets différents : capacités, processus, événements et relations d’architecture. Les faire coïncider en une seule hiérarchie produirait une fausse complétude. FLOW présente une bonne séparation entre demande, décisions, engagement, orchestration et opérations physiques. La faiblesse pour une V0 commune aux trois publics se situe dans les passages entre ces responsabilités : objet transmis, autorisation, date d’effet, résultat et réaction à un écart.

### STD-V0-01 — BIZBOK, capacité et réalisation

**Source effectivement lue :** [Glossaire BIZBOK 15.0](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), ©2026, pages imprimées 456–457, entrées Capability, Capability Behavior et Capability Instance. Extrait public officiel ; guide complet et modèles sectoriels membres non consultés. Synthèse seulement, sans redistribution du document.

**Constat sourcé :** la capacité, sa façon d’agir selon le contexte et sa réalisation particulière sont des notions distinctes. **Interprétation FLOW :** cela soutient la distinction modèle cible / applicabilité / réalisation installée et l’étude des comportements. La règle de parent unique et de niveau terminal reste une convention FLOW, pas une conformité BIZBOK démontrée. **Recommandation :** conserver les 47 capacités ; expliquer leur nature avant de discuter les applications ou équipes qui les réaliseront. Aucun découpage logiciel n’en découle.

### STD-V0-02 — Business Architecture Metamodel, vues croisées

**Source effectivement lue :** [Business Architecture Metamodel Guide](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf), version 3.0, septembre 2024, §4.2–4.3, page PDF 10. Document public officiel ; droits réservés, synthèse et lien uniquement.

**Constat sourcé :** le socle proposé articule capacités, flux de valeur et information ; les scénarios donnent un usage aux vues croisées. **Point commun :** FLOW distingue déjà catalogue et récits. **Différence :** la publication FLOW n’embarque aucun objet/document/événement métier de production, uniquement les capacités, comportements, regroupements et référentiels ; les quatre illustrations sont exclues. **Recommandation :** préparer pour la V0 une fiche de quelques objets échangés et des scénarios, sans construire prématurément un schéma de données exhaustif ni changer la hiérarchie. Le mot « domaine » de ce métamodèle n’équivaut pas automatiquement à D01–D06.

### STD-V0-03 — SCOR Digital Standard

**Sources :** [présentation officielle ASCM](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/) consultée via le contenu textuel indexé ; ouverture directe refusée 403. [Quick Reference Guide hébergé par le chapitre ASCM San Diego](https://sandiego.ascm.org/images/downloads/Eco_Sustainability/scor_qrg_digital_book_5_pager_digital.pdf), PDF de cinq pages effectivement ouvert, édition exacte non affichée dans les passages lus. Pages PDF 2–4 : facilitateurs, processus, mesures. Le fichier central ASCM et l’introduction 2025 ont échoué à l’ouverture ; leur texte indexé ne sert pas à prétendre une revue exhaustive du standard courant. Réutilisation limitée à la synthèse et aux liens.

**Constat sourcé :** SCOR distingue Orchestrate, Plan, Order, Source, Transform, Fulfill et Return. Il couvre un périmètre d’entreprise plus large que FLOW Supply. Sa catégorie Orchestrate inclut des responsabilités stratégiques et de gouvernance : elle n’est pas équivalente à D06 Process Orchestration.

**Correspondances proposées, à maille de processus :**

| Élément natif | Cibles FLOW examinées | Relation et limite |
| --- | --- | --- |
| Plan | D03.p, D03.o, D05.f et décisions D05 | Mobilise ; pas d’équivalence entre processus SCOR et capacité FLOW |
| Order | D04.i/k, D03.i/l/n, D04.o | Recouvrement partiel ; paiement reste externe |
| Source | D04.j/r/m, D06, D01 | Recouvrement partiel ; sourcing fournisseur et négociation des accords restent externes |
| Transform | D06, D07.b, D07.d | Adhérence via prestations ; production interne non démontrée comme périmètre FLOW |
| Fulfill | D03, D04.o, D06 et exécutants | Contribution ; opérations entrepôt/transport et facture ne deviennent pas des capacités FLOW |
| Return | D04.l/m, D05.i, D01, D06 | Recouvrement ; droits commerciaux distincts du devenir logistique |
| Orchestrate | principes, politiques, projections de référence | Appui méthodologique ; ne justifie pas un domaine Supply absorbant Finance, RH ou conformité |

Le guide distingue aussi préparation de réponse, communication des résultats et mesures de performance. **Inférence locale :** une V0 doit rendre visibles les résultats échangés et proposer des critères de succès, sans importer tous les processus ou indicateurs SCOR. Les mesures proposées dans le kit V0 sont locales et n’utilisent aucun identifiant SCOR prétendument équivalent.

### STD-V0-04 — GS1 EPCIS / CBV

**Source effectivement lue :** [EPCIS and CBV Implementation Guideline 2.0](https://ref.gs1.org/guidelines/epcis-cbv/2.0.0/), ratifiée mars 2023 ; introduction, dimensions de visibilité, §5.9 sur événements erronés et corrections. Document public officiel, synthèse seulement.

**Constat sourcé :** identité, date, lieu et contexte donnent leur sens aux événements ; une correction peut porter sur un fait antérieur sans effacer sa trace. **Points communs :** D01.f/g/c et D07.d parlent de provenance, fraîcheur, absence de double compte et faits distincts des estimations. **Écart de précision :** la correction des faits tardifs et son effet sur stock disponible, promesse et rapprochement ne forment pas encore un contrat traversant les fiches. **Recommandation :** scénario de réception reçue deux fois puis corrigée, avec un résultat attendu par responsabilité. Ce rapprochement ne prescrit ni EPCIS comme technologie, ni suivi unitaire de tous les articles, ni nouvelle capacité « Event Management ».

### STD-V0-05 — ArchiMate, sens des relations

**Source effectivement lue :** [ArchiMate 101, Relationships between systems](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/), tutoriel évolutif de la communauté The Open Group, sans édition normative revendiquée ; sections Sharing information, Temporal or causal relationship, Dependencies between systems. Synthèse et lien.

**Constat sourcé :** échange, causalité et fourniture d’un service sont des relations distinctes ; leurs flèches ne vont pas nécessairement dans le même sens. **Application FLOW proposée :** écrire une expression lisible de la source vers la cible et distinguer résultat transmis, besoin, autorisation et réalisation. Ne pas convertir automatiquement `needs` en déclenchement, ni tirer un workflow de la simple connexité du graphe. Cette référence confirme l’intérêt de la règle U398/U399 ; elle ne valide pas les liens proposés dans [liens.md](liens.md).

### STD-V0-06 — APQC Retail PCF : limite explicite

**Sources effectivement lues :** notices [Retail PCF 6.1.1](https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-retail-pdf-version-611) et [Retail PCF 7.2.1](https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-retail-pdf-version-721). Le lien « latest » de la première conduit à la seconde. Le téléchargement affiche un formulaire nominatif et CAPTCHA ; aucun formulaire soumis, aucun contenu détaillé récupéré.

La nature « classification de processus retail » est établie, mais **aucune couverture détaillée APQC n’est affirmée**. Aucun code natif de processus n’est inventé. Cette piste reste non comparée au niveau élémentaire ; elle ne figure pas au dénominateur d’un score de complétude et ne bloque pas les comparaisons documentées ailleurs.

## Conséquences pour la préparation de la V0

Ces rapprochements renforcent trois choix : conserver la carte de capacités, ajouter des vues de scénarios transverses et expliciter les informations/engagements échangés. Ils ne démontrent pas la complétude de tout le retail ni d’une architecture de solution. L’absence de prévision, de prix, de facturation ou d’exécution WMS comme domaines internes doit être appréciée contre les frontières décidées, et les entrées/sorties correspondantes doivent être identifiées.

L’applicabilité aux SI reste un travail séparé : `modeles/backlog/applicability.yaml` a quatre contextes et zéro évaluation ; Sarenza est explicitement non évalué. Une présentation peut exposer cette situation, mais ne peut pas la transformer en carte de couverture installée.
