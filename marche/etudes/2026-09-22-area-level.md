# Quel rôle pour le niveau Area ?

Étude du 22 septembre 2026 — U620/U621, Codex. Recommandation proposée, aucune migration du catalogue. Analyse structurée : [annexe YAML](../../modeles/backlog/area-level-market-study-U620.yaml).

## Résultat

Le niveau intermédiaire est utile, mais sa signification doit être choisie. Les sources distinguent une catégorie de présentation, une capacité plus large décomposée et un périmètre de responsabilités métier. FLOW utilise aujourd’hui la troisième lecture ; SAP apporte un précédent de hiérarchie, pas une définition universelle suffisante.

## Comparaison élargie

| Référence | Objet natif | Raisonnement et limite |
| --- | --- | --- |
| [SAP Reference Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture) — ELM633 | Business Domain → Business Area → Business Capability | Area regroupe les capacités ; chaque capacité appartient à une Area puis à un Domain. SAP fixe trois niveaux de granularité. La structure est explicite ; elle ne fournit pas un test universel pour décider où couper une Area. Le Business Process Segment est un objet différent, même si son nom peut coïncider. |
| [DDD — Nick Tune](https://nick-tune.me/blog/2020-11-25-domain-subdomain-bounded-context-problem-solution-space-in-d/) — ELM634 | Domain et Subdomain | Subdomain est relatif : un domaine est qualifié de sous-domaine par rapport à son parent. Plusieurs découpages restent possibles. Point de vue argumenté d’un praticien, pas norme DDD. L’auteur conteste lui-même la séparation trop simple entre espaces du problème et de la solution. |
| [Microsoft — analyse DDD](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) — ELM635 | Subdomain / Bounded Context | Identifier fonctions proches et dépendances pour dégager les sous-domaines. Le bounded context délimite l’application d’un modèle particulier. Guide orienté conception de microservices ; aucune obligation de convertir une Area FLOW en service logiciel. Core/supporting/generic qualifie l’importance stratégique, pas la profondeur. |
| [The Open Group — TOGAF](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf) — ELM636 | Stratification / Leveling | Sépare classement en catégories et décomposition des capacités. La profondeur répond aux besoins des lecteurs et des décisions. Guide V2 sur le site officiel inaccessible pendant cette étude. Aucun détail de 2018 attribué automatiquement à une édition actuelle ; aucune classe Area imposée par ces passages. |
| [Business Architecture Guild](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf) — ELM637 | Capability decomposes into capability | Décomposition récursive de capacités centrées sur un objet métier. Les enfants restent dans le périmètre de l’objet parent. Livre blanc public, pas lecture intégrale du BIZBOK. FLOW distingue déjà Area et Capability ; une Area réunissant plusieurs objets ne doit pas être déclarée équivalente à cette décomposition. |
| [BIAN / Van Haren](https://www.vanharen.net/wp-content/uploads/2026/02/syllabus-BIAN-Foundation-v3.8.pdf) — ELM638 | Business Area → Business Domain → Service Domain | Area et Domain organisent la présentation du Service Landscape. Le Service Domain porte une responsabilité fonctionnelle élémentaire. Ordre Area/Domain inverse de SAP ; cadre bancaire. La structure de présentation ne suffit pas à attribuer une responsabilité opérationnelle au regroupement. |
| [APQC](https://www.apqc.org/How-Can-Organizations-Classify-and-Organize-Their-Processes-Using-a-Common-Framework) — ELM639 | Category → Process group → Process → Activity → Task | La catégorie regroupe les processus au plus haut niveau ; le groupe de processus contribue à cette catégorie. Le détail sert pilotage, mesure et amélioration. Taxonomie de processus ; Process Group ne devient pas automatiquement une Area de capacités. La page générale ne constitue pas une lecture du catalogue Retail complet. |
| [IBM Component Business Model](https://public.dhe.ibm.com/software/emea/dk/frontlines/g510-6163-component-business-models.pdf) — ELM640 | Business Competency × Accountability Level | Les compétences regroupent l’activité ; un axe distinct distingue Direct, Control et Execute. Les composants coopèrent selon des niveaux de service convenus. Matrice de conception et réalisation métier ; pas une hiérarchie Domain/Area/Capability. N’impose pas de réintroduire des couches dans FLOW. |
| [SAP LeanIX](https://help.sap.com/docs/leanix/ea/business-capability-modeling-guidelines?locale=en-US) — ELM641 | Business Capability L1 / L2 / L3 | Hiérarchie de capacités ; recommande généralement trois niveaux au plus et une affectation non ambiguë des enfants. Distingue organisation, processus et technologie. Conseil d’usage produit, pas contrainte ontologique universelle. Même groupe SAP que RBA, donc pas une preuve indépendante de consensus. |
| [Ardoq](https://help.ardoq.com/en/articles/44050-business-capability-modeling-and-realization-metamodel) — ELM642 | Business Capability récursive | Un même type Business Capability se décline en hiérarchie à profondeur libre ; le niveau sert notamment aux vues et filtres. Métamodèle d’outil ; la flexibilité ne prouve pas la pertinence métier d’un découpage. Contenu conservé après intégration de l’ancien bundle dans Foundation. |

## Ce que le mot sous-domaine précise réellement

Chez Nick Tune, « sous-domaine » exprime une relation au parent, pas une catégorie de rang fixe. Microsoft propose de chercher des fonctions proches et leurs dépendances, puis de délimiter où un modèle particulier est applicable. L’intérêt pour FLOW est la cohérence des problèmes traités. En déduire une correspondance automatique Area = bounded context imposerait un choix que cette étude ne justifie pas. Le classement core/supporting/generic traite d’une autre dimension que la profondeur.

La recherche ne trouve donc pas une frontière mécanique produite par le seul terme sous-domaine. Les critères retenus, les exemples et les exclusions doivent rendre le découpage vérifiable. La position de Nick Tune est celle d’un praticien ; elle ne constitue pas une norme unique du DDD.

## Proposition pour FLOW

> Une Area est un périmètre cohérent de responsabilités métier à l’intérieur d’un Domain. Elle regroupe les capacités qui concourent à une même finalité et précise ce qu’elles prennent en charge ainsi que leurs échanges avec les autres Areas.

Cette proposition renforce la définition actuelle MOD013, déjà centrée sur les responsabilités. L’Area situe un ensemble de responsabilités ; la capacité précise ce que l’entreprise sait faire dans ce périmètre. Un simple dossier de navigation ne suffit pas à justifier une Area.

1. Finalité commune exprimable indépendamment de la liste des capacités.
2. Responsabilités incluses et exclues explicites, distinguables de celles des Areas voisines.
3. Cohérence des concepts, règles et décisions nécessaires à cette finalité ; un même objet peut être utilisé dans plusieurs Areas sous des responsabilités différentes.
4. Rattachement principal des capacités justifiable sans recopier les capacités transversales.
5. Interactions explicables par informations, demandes, résultats et engagements échangés.
6. Stabilité lorsque changent organisation, fournisseurs, applications et processus.

Une Area peut combiner action, décision, planning, orchestration et policy. Le partage d’un objet ne suffit pas à fusionner des Areas : la demande peut être tenue par Demand, prise en compte dans l’arbitrage et exécutée par Fulfillment, avec des responsabilités différentes. Les coopérations ne sont pas des chevauchements si leur rôle est explicite.

## Mise à l’épreuve sur FLOW

| Area | Finalité et test proposés |
| --- | --- |
| Demand Management | Porter les besoins, exigences et promesses de satisfaction des demandes. La cohérence vient de la responsabilité sur la demande, y compris achat et transfert, et non d’un type de client. |
| Inventory Management | Établir les états et mouvements du stock. Les demandes et décisions consomment ces informations sans absorber cette responsabilité. |
| Fulfillment Orchestration | Conduire l’exécution des demandes en gouvernant les sollicitations de services et leur suivi. Tâches, déclenchement, suivi et reprise relèvent de la même finalité ; la nature numérique ou physique du service ne suffit pas à scinder l’Area. |
| Référentiels et policies — nom détaillé non réarbitré | Fournir les références et le cadre de règles nécessaires au Domain. U618 maintient une seule Area ; il reste utile de formuler sa finalité commune. Les distinctions de type et gouvernance restent internes, sans réouvrir son regroupement. |

Le rapprochement avec la Guild présente une limite utile : sa décomposition par objet est plus prescriptive que notre regroupement de plusieurs référentiels et policies. Cette différence ne rend pas FLOW invalide ; elle empêche seulement de revendiquer une conformité exacte à cette méthode.

## Sources, accès et portée

Toutes les sources ci-dessus ont été consultées le 22 septembre 2026. Les synthèses sont sélectives et sans copie intégrale des documents. Aucun consensus, classement de fournisseurs ni réalisation Beaumanoir n’est inféré.

- **ELM633 / MKT04** — Cours évolutif ; consulté le 22 septembre 2026. Passage : Business Capability Model, niveaux 1–3 ; distinction avec Business Process Segment. Accès : Texte primaire ouvert.
- **ELM634 / MKT85** — Article du 25 novembre 2020. Passage : Subdomains ; Subdomains vs Bounded Contexts ; Problem Space vs Solution Space. Accès : Texte original de l’auteur ouvert.
- **ELM635 / MKT69** — Documentation évolutive. Passage : Analyze the domain ; Define bounded contexts. Accès : Texte primaire ouvert.
- **ELM636 / MKT01** — G189, juin 2018. Passage : §§3.2.1–3.2.2, pages imprimées 9–10. Accès : Document primaire historique ouvert sur hébergement tiers.
- **ELM637 / MKT03** — Metamodel Guide v3.0, septembre 2024. Passage : §5.2, pages imprimées 17–18 ; §6.3, page 45. Accès : PDF primaire ouvert.
- **ELM638 / MKT18** — Syllabus BIAN Foundation v3.8. Passage : Key terms and concepts, pages imprimées 24–26. Accès : Syllabus primaire de certification ouvert.
- **ELM639 / MKT07** — Page créée septembre 2026 ; PCF 8.0 cité. Passage : Common hierarchy ; paragraphes sur management, accountability, measurement et improvement. Accès : Texte primaire ouvert.
- **ELM640 / MKT06** — Publication historique, ©2005. Passage : The CBM framework ; figure 5, page imprimée 7. Accès : Passage primaire indexé consulté ; ouverture directe en échec 502.
- **ELM641 / MKT25** — Métamodèle v4 ; documentation évolutive. Passage : Guidelines and Best Practices ; Antipatterns. Accès : Texte primaire indexé détaillé ; ouverture directe vide.
- **ELM642 / MKT26** — Article du 19 novembre 2025. Passage : Business Capability Workspace ; Component Level. Accès : Texte primaire indexé détaillé ; ouverture directe 401.

Le guide TOGAF 2018 est une source primaire historique sur hébergement tiers ; le corps de la version actuelle n’a pas été vérifié. Les passages IBM, LeanIX et Ardoq ont été lus dans l’index primaire, avec les limites d’ouverture signalées. Le document Guild est son guide de métamodèle public, pas le BIZBOK intégral. SAP RBA et SAP LeanIX constituent deux approches d’une même entreprise.

## Décision à venir

Conserver Area comme périmètre de responsabilités est la recommandation. Sa définition et les critères ci-dessus restent à discuter avec Laurent avant application. Le nom Area et sa place avaient déjà été adoptés U482 ; U620/U621 n’annulent pas cet accord et n’adoptent pas les compléments proposés ici.
