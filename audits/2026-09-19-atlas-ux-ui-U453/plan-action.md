# Atlas — plan d’action proposé pour une V0 de référence métier

19 septembre 2026. Plan proposé à Laurent ; il ne vaut ni lancement des lots ni demande de publication.

## Résultat visé

Un lecteur comprend ce que fait chaque domaine, ses limites et ses interactions. Un PO retrouve les règles de périmètre. Un expert métier peut expliquer les informations, documents, engagements et faits nécessaires. Un architecte utilise cette référence pour concevoir une solution dans un dossier distinct.

Atlas reste strictement métier. Univers → Domaine → Capacité organise la navigation ; les comportements précisent les capacités. Les interactions relient les responsabilités. Les objets et leurs structures métier constituent une vue transversale. Les couches transactionnelle/processus, applications, produits logiciels et contrats techniques ne structurent pas Atlas.

## Point de départ

- Publication examinée : v010 / 2026-09-19.3, 47 capacités, 76 comportements et 202 relations métier qualifiées.
- Les décisions U455/U456 sont enregistrées dans les principes et conventions. La migration technique de `layer`, les formulations héritées et les parcours éditeurs de l’application restent à traiter.
- L’audit documente les défauts de lecture, recherche, relations et contraste. La maquette illustre une proposition ; elle n’est pas l’application.
- Les deux glossaires, le guide versionné, les types et icônes, l’ordre des décisions et les liens de publication sont des acquis à préserver.
- L’audit des comportements U431 reste clos. Le plan n’ouvre pas un nouvel audit exhaustif et ne valide pas globalement les contenus existants.

Sources de travail : [audit UX/UI](rapport.md), [décisions U455/U456](../../modeles/backlog/domain-interactions-U455-U456.yaml), [suivi V0 existant](../../modeles/backlog/v0-readiness.yaml), [maquette](proposition.html). Les éléments datés du suivi V0, notamment les anciens comptages, devront être contextualisés plutôt que repris comme l’état courant.

## Séquence et dépendances

**Lot 1 : cohérence du socle → Lot 2 : consultation → Jalon A : Atlas lisible.**

**Lot 3 : cas métier pilotes → Lot 4 : informations et interactions → Jalon B : référence métier éprouvée.**

**Lots 1 à 4 → Lot 5 : généralisation → Lot 6 : recette et préparation de publication → V0 présentable.**

Les lots 2 et 3 peuvent avancer en parallèle une fois leurs conventions communes stabilisées. Les corrections de contraste et de classement de recherche sont indépendantes des arbitrages sur les données. La généralisation du schéma attend les cas pilotes ; les parties non ambiguës des fiches peuvent être améliorées auparavant. Cet ordre n’impose aucune délégation à des agents.

## Lot 1 — aligner le socle sur les décisions prises

**Priorité : immédiate.** Appliquer U455/U456 sans changer les responsabilités métier par déduction.

Actions :

- Retirer `layer` du modèle courant et des règles qui en font un critère d’appartenance. Adapter les lecteurs et contrôles pour conserver les anciennes publications ; préserver leurs octets et accords.
- Corriger les six périmètres et qualifications héritées identifiés dans l’annexe U455/U456. Préparer un nouveau guide du méta modèle pour une publication future.
- Séparer explicitement contenu métier destiné à Atlas et matériau de travail interne. Sortir des parcours publics les comparaisons produits, réserves, validations et sources du backlog ; conserver leur provenance interne.
- Consolider les actions et questions encore ouvertes dans le suivi V0 existant, en distinguant réalisé, proposé, à arbitrer et hors périmètre. Les critères de recette de ce plan ne constituent pas des validations de contenu.

**Livrable :** socle cohérent, compatible avec l’historique, et liste unique des travaux restant pour la V0.

**Critères de sortie :** aucun raisonnement métier courant fondé sur une couche ; anciens snapshots et liens consultables ; aucun changement implicite de nom ou de parent ; contrôles de modèle et parcours touchés réussis.

## Lot 2 — rendre la consultation simple et directe

**Priorité : immédiate.** Corriger UX01–04, UX07 et les principaux défauts de navigation avant une refonte graphique étendue.

Actions :

- Recherche : nom exact et identifiant en premier, puis variantes lexicales documentées ; extraits expliquant le résultat ; index limité au contenu destiné au lecteur. « Bon de commande » doit mener à la bonne notion et à ses capacités liées, sans fusionner document et capacité.
- Fiche : finalité, inclus/exclus et responsabilités voisines en tête ; détail des comportements et texte développé accessibles à la demande. Conserver une lecture complète et partageable.
- Relations : noms lisibles et dépendances directes par défaut ; sens « a besoin de / est utilisé par » explicite ; liens entre voisins et profondeur avancée à la demande. Ne pas présenter une dépendance comme un flux d’informations.
- Présentation : contrastes corrigés, typographie hiérarchisée, recherche proche de l’arbre, aides secondaires accessibles. Appliquer la palette proposée B, avec accents limités et libellés explicites.
- Vérifier clavier, focus, zoom, petit écran et consultation des glossaires ; conserver les icônes spécifiques des références et les décisions en fin de domaine avec séparation légère.

**Livrable :** une consultation cohérente utilisant le contenu disponible ; les nouvelles rubriques n’inventent pas de synthèse métier absente.

**Critères de sortie :** le nom exact remonte en premier ; les annotations internes ne déclenchent plus les résultats ; résultat, périmètre et voisins sont accessibles sans parcourir plusieurs écrans ; graphe d’entrée compréhensible sans mémoriser les IDs ; parcours essentiels accessibles au clavier et lisibles à 200 %.

**Jalon A : Atlas lisible.** Ce jalon améliore la consultation ; il ne suffit pas à déclarer la V0 métier complète.

## Lot 3 — éprouver la fiche métier sur cinq capacités

**Priorité : avant généralisation des nouvelles structures.** Utiliser Purchase Order, Product Reference et le triptyque Fulfillment Commitment / Supply Assignment / Reservation.

Pour chaque cas, préparer une fiche courte : résultat, responsabilités, limites, voisins, informations nécessaires ou produites, états/effets essentiels et exemple concret. Réutiliser les définitions du glossaire ; différencier la capacité et l’objet lorsqu’ils portent le même nom.

Sur Product Reference, expliciter la projection et les rôles d’autorité/alimentation, sans nommer une application supposée. Sur Purchase Order, explorer ligne, attente, confirmation et fait de réception, sans adopter de cardinalité par analogie avec un ERP. Sur le triptyque, conserver la règle : seule Reservation bloque les usages concurrents.

Éprouver ces fiches avec un scénario d’interaction Commerce–Supply–logistique. Les retours, refus et écarts comptent autant que la progression nominale. Le scénario ne crée pas automatiquement trois domaines ou univers et ne remplace pas les responsabilités existantes.

**Livrable :** cinq fiches pilotes et quelques exemples d’objets, documents et faits, chacun qualifié selon sa portée réelle d’accord.

**Critère de sortie :** un PO et un expert savent expliquer qui peut décider, s’engager, demander une prestation et constater sa réalisation ; les questions ouvertes sont précises et rattachées à un exemple.

## Lot 4 — ajouter les informations et interactions métier utiles

**Dépendance : lot 3.** Choisir le minimum de structure qui résout les ambiguïtés observées.

Actions :

- Définir les fiches d’information : sens, identité et maille métier, informations essentielles, relations, états et règles utiles. Ne pas importer des structures de tables ou d’API.
- Qualifier les liens entre capacités et informations : consulter, établir, modifier, recevoir, communiquer, selon des responsabilités effectivement justifiées. Ne pas transformer automatiquement les dépendances existantes en flux.
- Pour les projections, distinguer autorité métier, source d’alimentation, contexte, fraîcheur utile, validité et traitement d’une information absente ou contradictoire.
- Clarifier la convention fait/document à partir des exemples pilotes ; préserver l’historique. Une fiche autonome se justifie par un besoin de compréhension ou une responsabilité, pas par chaque champ ou message possible.
- Étendre le contrat de données d’Atlas, les validations et la publication pour ces informations métier ; rendre leurs liens navigables dans « Informations et échanges ». Ce travail technique sert l’outil Atlas, sans ajouter une vue de solutions au contenu présenté.

**Livrable :** vue métier transverse, cohérente avec le glossaire et le snapshot sélectionné.

**Critères de sortie :** aucune information issue silencieusement du backlog dans une version publiée ; aucun lien orphelin ; origine métier et effets compréhensibles ; informations internes conservées hors affichage ; absence d’autorité connue non remplacée par une supposition.

**Jalon B : référence métier éprouvée sur les pilotes.** La généralisation repose sur des cas relus, pas sur un schéma théorique imposé à toutes les capacités.

## Lot 5 — généraliser à la couverture V0 convenue

Appliquer le format de lecture aux 47 capacités, avec une profondeur proportionnée. Décrire les six projections et leurs informations utiles ; seules les notions justifiant une fiche autonome sont créées. Rendre explicites les limites de couverture de l’univers Business Services sans inventer son catalogue.

Contrôler surtout les contradictions, doublons sémantiques, exclusions mal visibles, relations ambiguës et renvois de glossaire. Conserver les sujets déjà clos et ne pas relancer l’audit des comportements. Les questions du suivi V0 antérieur sont triées : bloquantes pour comprendre une frontière, utiles ultérieurement, ou hors Atlas parce que purement techniques.

**Livrable :** catalogue V0 homogène et fiche de couverture interne montrant précisément ce qui a été relu et ce qui reste à préciser.

**Critère de sortie :** aucun manque connu ne conduit le lecteur à attribuer une responsabilité, une autorité ou un effet non établi. Une lacune locale peut rester ouverte si elle ne fausse pas l’usage présenté ; elle n’est ni masquée par une valeur inventée ni transformée en validation globale.

## Lot 6 — éprouver la V0 et préparer sa publication

Organiser un essai qualitatif avec 6 à 8 personnes couvrant direction, métier, PO et architecture/développement. Mesurer la réussite des tâches, les hésitations et les termes employés, sans prétendre à une représentativité statistique.

Tâches : comprendre Promising/Optimization ; retrouver un achat en vocabulaire courant ; distinguer capacité, objet et document ; expliquer Assignment/Reservation ; identifier l’autorité d’un référentiel ; expliquer une coopération entre domaines ; retrouver une information et sa règle ; naviguer au clavier et revenir du glossaire.

Corriger les difficultés observées. Exécuter les vérifications proportionnées sur l’état final : modèles, contrats et publications, tests frontend concernés, compilation, intégrité des historiques et parcours réels. Préparer la note de release et le dossier de revue : contenu précis, accords, limites connues et preuves de recette. La publication suit une demande de release distincte ; le plan n’autorise pas une publication automatique.

**Critères de V0 présentable :** compréhension correcte des frontières essentielles ; recherche et navigation opérationnelles ; périmètre métier respecté ; aucune source/autorité inventée ; version de référence identifiable ; limitations utiles connues de l’équipe de préparation ; contrôles réussis. Publication ne vaut pas validation de tous les contenus.

## Répartition de l’autonomie et des arbitrages

| Prise en charge autonome après lancement | Cas concrets à soumettre à Laurent et aux experts |
| --- | --- |
| Migration technique des principes adoptés et compatibilité historique | Création, suppression, fusion ou rattachement de domaines/univers |
| Corrections de recherche, contraste, navigation et icônes | Autorités métier et sources d’alimentation réelles |
| Mise en forme et reformulations sans changement de sens, avec traçabilité | Structure/cardinalité qui modifie un engagement ou son identité |
| Liens explicites fondés sur une définition déjà établie | Relation fait/document, correction et irréversibilité métier |
| Contrôles, preuves et préparation de release | Nouveaux effets, droits de décision et tolérances métier à une information différée |

Les arbitrages ne sont pas regroupés dans un questionnaire abstrait préalable. Chacun est présenté avec le cas concerné, les options, la recommandation, les conséquences et les sources utiles. Le travail indépendant continue pendant leur instruction.

## Modalités de pilotage proposées

Pour chaque lot : un livrable inspectable, un bilan des modifications, les vérifications effectuées et les points restant ouverts. Le suivi courant reste celui de V0 ; ce document donne la trajectoire et ne devient pas un second catalogue métier. Les évolutions restent locales tant qu’aucune release, aucun commit ou push n’est demandé.

Les charges ne sont pas encore estimées : la migration et les cinq fiches pilotes permettront de distinguer le temps de réalisation du temps d’obtention des arbitrages métier. Les lots 1 et 2 constituent le premier ensemble concret recommandé pour démarrer.
