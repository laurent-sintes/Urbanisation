# Audit avant release — U625

22 septembre 2026 — glossaire, métamodèle, Domain et Purpose. Auteur : Codex. Audit du backlog, sans publication ni modification de ses fiches.

**Avis : ne pas publier cet état comme la consolidation des décisions récentes.** Le cadre métier est largement clarifié ; sa transcription dans le catalogue reste partielle. Quatre écarts majeurs concernent les responsabilités et leurs frontières, auxquels s'ajoutent quatre lots de cohérence documentaire et de contrôle. Le nombre actuel de Purposes n'est pas en soi une anomalie : U584 proposait une structure, sans adopter globalement toutes les fiches et tous les déplacements.

## Périmètre et méthode

Lecture du modèle canonique, des 112 termes métier, des 14 termes méthodologiques et du guide ; revue des 9 fiches de niveau Domain/Purpose et des annexes de décisions concernées. Les 55 capacités ont été utilisées pour vérifier le rattachement et la couverture des finalités, sans rouvrir l'audit historique des comportements U431. Le dossier marché combine revue des correspondances locales et relectures externes ciblées, décrites dans [marche.md](marche.md).

Les empreintes initiales sont dans [inputs.json](inputs.json), l'extrait de travail dans [scope-extract.json](scope-extract.json). Ces pièces sont des preuves datées d'audit, pas des sources concurrentes du YAML. La matrice [revue-detaillee.md](revue-detaillee.md) suit chaque fiche et chaque terme. Les sources d'autorité restent celles d'AGENTS.md.

| Contrôle | Résultat |
| --- | --- |
| Structure observée | 1 Domain, 8 Purposes codés `area`, 7 référentiels, 55 capacités |
| Rattachement des capacités | 55/55 avec exactement un Purpose ancêtre : 41 directement, 14 via les référentiels ; aucune orpheline |
| Finalités de Domain/Purpose | 9/9 renseignées ; présence ne vaut pas qualité ni cohérence avec les descendants |
| Liens Markdown internes examinés | 418 ; aucun identifiant cible absent |
| Libellés de liens différents du canonique | 19 ; 9 occurrences « Customer Return » sont périmées, les autres incluent des abréviations ou précisions légitimes |
| Marché Domain/Purpose | 35 rapprochements, deux URL documentaires distinctes au minimum par fiche |
| Marché glossaire métier | 226 rapprochements sur 112 termes ; même minimum atteint |
| Métadonnées marché | Aucun manque sur les dix champs contrôlés : organisme, titre, URL, édition, passage, date, limites, similitudes, différences, position FLOW |
| Validation technique et intégrité | `validate_models.py` : **0 erreur** ; les dix entrées empreintées sont inchangées. Preuves dans [verification.json](verification.json) et [validation.log](validation.log) ; ce résultat reste distinct de l'avis sémantique présent |

Les URL ont été normalisées pour les ancres et paramètres de suivi ; il ne s'agit pas d'une comparaison exhaustive du contenu de tous les documents externes. Les preuves détaillées sont dans [structural-checks.json](structural-checks.json) et [market-metadata-checks.json](market-metadata-checks.json).

## Écarts majeurs

### A01 — Responsabilités adoptées encore dispersées dans l'ancien découpage

**Constat.** D04 `Service Requests` délègue la promesse à D15 `Order Promising`. `business-references` reste décrit par ses sept projections et vues, sans porter la finalité commune avec les policies. Aucun Purpose courant n'explicite à lui seul la responsabilité proposée de connaissance et suivi des apports attendus ; cette matière est notamment présente dans D01 et les Orders. Les politiques de protection des demandes et de recours aux prestataires restent surtout documentées dans l'annexe.

**Autorité.** U595 attribue à Demand besoins, exigences et promesse ; U618 maintient référentiels et policies dans un seul regroupement ; U585/U587/U590 cadrent les protections et Service Provider Policy. La gouvernance U613–U615 est déjà appliquée à certaines fiches et n'est pas à recommencer.

**Risque.** Publier des responsables différents de ceux retenus dans la discussion ; confondre Order, apport attendu, position de stock et règle de protection. Aucune lacune de capacité n'est déduite de la seule absence d'un titre Supply Management.

**Correction attendue.** Construire une table de correspondance des responsabilités existantes vers les Purposes cibles, conserver les identifiants et expliciter les coopérations. Appliquer les frontières déjà acquises ; qualifier séparément les noms, finalités et déplacements encore proposés. Ne pas reclasser automatiquement toutes les capacités `management` en `policy`.

**Clôture.** Promesse portée par Demand dans les définitions et renvois ; références et policies réunies sous une finalité commune ; responsabilité des apports attendus explicite sans double tenue des Orders. Appuis et limites : dossier marché M02, M06–M11 et étude U584.

### A02 — D17 décrit deux périmètres incompatibles

**Constat.** Le Domain attribue à D17 le plan d'ensemble régulièrement actualisé. La définition de D17 vise la demande à couvrir et son seul enfant est `Demand Planning` D17.a. Son périmètre laisse au plan amont la détermination des apports. Les premières comparaisons Oracle/SAP limitent ce qui est reconstruit, tandis que les comparaisons Microsoft/SAP suivantes décrivent un plan intégré de satisfaction et d'apports.

**Risque.** Une même fiche peut être comprise comme prévision des besoins, plan global ou simple réception d'un plan externe. C'est une incohérence interne, indépendamment du nom final des Purposes.

**Correction attendue.** Établir une seule responsabilité cible à partir du cadrage retenu de l'arbitrage et de la demande ; réaligner définition, finalité, scope, descendants et `flow_position` des quatre comparaisons. Le renommage seul ne résout pas le problème.

**Clôture.** Le lecteur sait qui construit la demande prévisionnelle, qui construit le plan de couverture et qui porte les apports attendus ; les renvois du Domain donnent la même réponse. Appuis M11–M12 ; ils ne prescrivent pas la hiérarchie FLOW.

### A03 — Task et Service Order ne sont pas transcrits avec leur rôle actuel

**Constat.** TER066 s'appelle encore `Backing Service Order` et définit une demande suivie dans sa prise en charge. D04 l'utilise comme moyen général de sollicitation. D06 conserve la convention antérieure où les Tasks expriment des contributions ; son scope ne décrit pas leur gouvernance précisée U617. Aucun terme autonome Task ne permet de retrouver cette distinction dans le glossaire.

**Autorité.** U616 : la Task encapsule la sollicitation et peut produire un document Service Order ; U617 : activation immédiate, différée ou événementielle, suivi, relance, recours de secours et vérification de fin.

**Risque.** Confondre le besoin initial, l'objet de pilotage, la prestation et son document de commande. Une API terminée pourrait être prise pour une prestation terminée.

**Correction attendue.** Aligner TER066 et les scopes D04/D06 ; définir Task au niveau du vocabulaire utile, sans créer un nouveau niveau de la hiérarchie ni étendre le catalogue Informations masqué. Conserver l'optionnalité du document, la différence avec Purchase Order, et le périmètre de services physiques, humains et numériques déjà porté par TER075.

**Clôture.** Un exemple de production documentaire sans Order formalisé et un exemple logistique avec Order rendent la chaîne Demande → Task → Service / document éventuel compréhensible. Les comparaisons CMMN/Camunda précisent leurs différences : M13–M15.

### A04 — Le début d'exécution n'est pas inscrit comme frontière commune

**Constat.** D03, D15 et D06 distribuent optimisation, engagement et adaptation selon leurs anciens scopes. Ils n'explicitent pas ensemble la règle U592 : possibilité de modifier le contenu d'une demande, même ferme, tant qu'elle n'est pas en cours d'exécution. L'adaptation par re-sourcing dans Fulfillment et le suivi de la demande initiale ne sont pas restitués avec le nouveau vocabulaire Task/Service Order.

**Risque.** Prendre la fermeté pour une interdiction de réviser, ou attribuer à l'arbitrage une modification de demande déjà en exécution sans contrat de coopération.

**Correction attendue.** Écrire la frontière acquise dans les Purposes concernés et illustrer la reprise du seul article manquant. Faire apparaître comme détails restant à préciser le signal du début d'exécution et la maille d'une demande partiellement exécutée. Le modèle de capacités n'a pas besoin d'un automate exhaustif pour être publiable.

**Clôture.** Les trois cas de U592 ont une responsabilité lisible : demande non exécutée, ferme non exécutée, réalisation en cours avec manque. Les détails non arbitrés restent signalés ; aucune réouverture du principe. Preuves existantes : U592/CMP254, Fluent Source Order Items et Oracle Split or Substitute Fulfillment Lines, avec leurs limites consignées dans U584.

## Compléments de cohérence

### A05 — Purpose adopté, restitution méthodologique incomplète

MOD013 et la règle principale d'AGENTS.md portent U624. Le guide U458 enseigne encore `Domain → Area → Capability → Behavior`, et son exemple structuré D05.f reste nommé Inventory Planning. Le frontend expose encore `Area` et `Areas et référentiels` dans `presentation.ts` et `dependencyGraph.ts`.

Mettre en cohérence le guide et la présentation des **nouvelles** publications, sans réécrire les anciennes ni renommer massivement les identifiants. Le code `kind: area` est volontairement compatible : sa conservation n'est pas un échec de validation. Une évolution du libellé visible doit respecter le vocabulaire du snapshot sélectionné. Distinguer aussi le niveau Purpose du champ `finality`, présent à plusieurs niveaux.

La comparaison de MOD013 reste principalement rattachée à CMP195 SAP/DDD ; relier la synthèse élargie U620–U624 et ses appuis BMM/Guild. Purpose est une convention locale adoptée, pas un standard marché découvert.

### A06 — Glossaire à synchroniser et à compléter sur les distinctions structurantes

- TER072 conserve `Customer Return Order` alors que D04.l est devenu `Return Order` U612. Ne pas réintroduire l'ancienne décomposition Customer Return / Consignment Return abandonnée ; neuf liens Markdown gardent aussi l'ancien libellé.
- TER071 décrit un déplacement de marchandises très large : préciser sa distinction avec mise en consignation, reprise et retour selon l'intention. Le sens plus large de Transfer Order chez certains éditeurs peut rester dans la comparaison.
- Les notions Task, consignation et ses deux sens, Fill-up, Pick-up et Consignment Issue ne disposent pas d'entrées autonomes dans le glossaire. Leur couverture doit être ajoutée ou reliée explicitement, en conservant Issue comme comportement de Sales Order. Un terme utile ne crée pas une capacité supplémentaire.
- Clarifier les renvois entre Service Catalog, Service Provider et Service Provider Policy ; ne pas exiger une entrée par capacité ni une règle de gestion par contrat.
- TER001 et TER026–TER030 sont essentiellement méthodologiques, alors que le glossaire méthodologique n'a pas d'entrée autonome Capability. Prévoir une autorité et des renvois clairs, avec conservation des identifiants et liens historiques ; pas de suppression aveugle.
- TER007/TER055 et TER004/TER060 demandent des alias ou distinctions mieux visibles. Ce sont des sujets de lecture, pas des contradictions prouvées.

Ne pas corriger des écarts assumés : TER056 garde explicitement Inventory Ledger Management comme candidat non adopté ; TER080 expose le sens local de Réassort ; ATP/CTP/PTP peuvent rester des repères de glossaire même si le découpage des capacités évolue.

### A07 — Dossier marché abondant, mais pas encore aligné avec chaque Purpose

Tous les minima quantitatifs passent. La faiblesse tient surtout à la portée : D04 utilise des preuves de demandes de services pour un périmètre plus large ; D17 présente des positions incompatibles ; le Purpose références/policies et la gouvernance des Tasks sont mieux argumentés en annexe que dans leurs fiches.

Rapatrier les arguments utiles **après** stabilisation des scopes, avec points communs, différences et limite de preuve. Les 35 + 226 entrées ne représentent pas autant de documents uniques ni de validations indépendantes. Ne pas ajouter de liens génériques pour augmenter le total. Le [dossier marché](marche.md) fournit 15 relectures ciblées, les études réutilisables et une appréciation de chaque fiche.

### A08 — Les contrôles techniques ne prouvent pas la qualité d'un Purpose

Le schéma accepte `fields.finality` mais les champs du nœud ne sont pas tous obligatoires. Le validateur contrôle la structure et la présence des références, sans attester que finalité, définition, descendants et position marché donnent le même périmètre. Les sources peuvent être parfaitement renseignées tout en justifiant l'ancien modèle.

Proposer pour les futurs lots un contrôle opt-in compatible avec les historiques : nom/définition/finalité/scope non vides aux niveaux Domain/Purpose, couverture des capacités par un Purpose, cohérence des libellés canoniques avec alias autorisés, correspondances réexaminées lorsqu'un scope change. La pertinence des preuves et la finalité commune restent des contrôles éditoriaux ; aucun algorithme ne doit leur inventer une validation.

## Couverture métier à obtenir

Cette grille est une recommandation de rédaction pour la refonte ; elle n'adopte pas de nouveaux noms ou champs.

| Famille de finalité | Résultat durable à rendre explicite | Frontière à contrôler |
| --- | --- | --- |
| Références et policies | Disposer d'un contexte interprétable et d'un cadre de décision applicable | Vérité externe / CRUD local / vue ; catalogue d'offres / règles de recours |
| Demandes | Porter les besoins, leurs exigences et la promesse de satisfaction | Intention / effet juridique ; besoin / réservation ; demande / prestation |
| Apports attendus | Connaître les ressources à venir et leurs échéances | Order source / apport résultant ; proposition / engagement ; entrée attendue / réception |
| Stock | Connaître et fiabiliser les positions de stock dans le temps | Fait de mouvement / projection ; propriétaire / détenteur ; disponibilité / affectation |
| Arbitrage du plan | Organiser la couverture des besoins et les ajustements autorisés | Plan / décision spécialisée / application ; avant exécution / exécution commencée |
| Réalisation | Obtenir et suivre le résultat des prestations mobilisées | Task / Service / Service Order ; reprise / re-sourcing ; acquittement / achèvement |

Les exemples indispensables existent déjà dans la discussion : campagne eCommerce nécessitant de réviser une protection B2B ; transfert issu du plan ; vente de stock détenu en consignation ; retour avec réparation selon mandat ; exclusion d'un prestataire en difficulté ; article manquant repris depuis un autre entrepôt ; service numérique sans document de commande. Ils permettent de vérifier la complétude des frontières sans inventer de flux installés.

## Ordre de correction et sortie d'audit

1. Aligner les responsabilités et le plan d'ensemble (A01/A02), en séparant acquis et propositions de rattachement.
2. Transcrire le contrat Task/Service/Service Order et la frontière de début d'exécution (A03/A04).
3. Harmoniser métamodèle, guide, glossaire et noms affichés pour les nouvelles publications (A05/A06).
4. Actualiser les comparaisons à cette maille, puis vérifier l'état final et les accords champ par champ (A07/A08).

Les principaux acquis ne nécessitent pas un nouvel arbitrage : Purpose/Finalité, une seule famille références + policies, axes nature/gouvernance séparés, intention des demandes, Purchase Order comme achat, Consignment Issue comme comportement et règle avant/après début d'exécution. Les intitulés finaux de certains Purposes, les formulations détaillées et les rattachements non explicitement adoptés restent à qualifier. Le fait de demander cet audit ne les valide pas.

La release pourra présenter le modèle consolidé lorsque les quatre écarts majeurs seront clos et que les compléments affectant son contenu visible seront traités. Le présent audit ne vaut ni accord métier global ni autorisation implicite de publication.
