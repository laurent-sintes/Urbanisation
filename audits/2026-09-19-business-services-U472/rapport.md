# Retrait de Business Services — U472

19 septembre 2026 — modification du backlog, sans publication.

Business Services (`universe-case`) est supprimé. Cet univers ne contenait aucun domaine ni aucune capacité et ne participait à aucune relation. Supply Chain Orchestration est désormais le seul univers instancié ; Business References reste son groupe de présentation. Le commerce sera étudié après la Supply Chain, sans univers de remplacement anticipé.

## Modifications

- Suppression du nœud `universe-case` et du terme associé `TER067`.
- Terme Case (`TER064`) conservé comme dossier de traitement, sans rattachement à l’univers supprimé.
- Deux principes et le périmètre de Process Tracking (`BHV082`) corrigés pour retirer ce rattachement. Nom, définition, parent et accords de ce comportement conservés.
- Priorité Supply puis commerce consignée dans `PRINCIPLE-SUPPLY-FIRST`, la feuille de route, AGENTS.md et les conventions.
- Contribution U472, correction C109 et comparaison CMP187 enregistrées. La restitution du backlog est régénérée.

Les identifiants retirés ne seront pas réutilisés. U173 et les anciennes annexes restent des preuves historiques ; ils ne justifient plus le maintien de cet univers. Les états avant modification sont conservés dans [before/](before/).

## Appuis et limites

Le [tutoriel communautaire ArchiMate](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/) distingue un service exposé des processus et fonctions internes. Le [Case de Microsoft Customer Service](https://learn.microsoft.com/en-gb/dynamics365/customer-service/administer/overview-cases) est un dossier de traitement client. Ces deux concepts n’établissent pas à eux seuls la pertinence d’un univers transversal Business Services : cette conclusion est une interprétation locale, et son retrait relève du choix U472. Le tutoriel n’est pas une spécification normative ; le cas Microsoft n’épuise pas la notion générique de dossier. Passages, éditions et dates : ELM323/ELM324 et CMP187.

## Contrôles

- Validation des modèles : **zéro erreur**.
- Tests des glossaires et comportements : **12 réussis**.
- Retrait ciblé contrôlé : 142 → **141 nœuds**, 111 → **110 termes**.
- **47 capacités, 76 comportements et 346 relations du backlog conservés** ; aucun lien orphelin, aucune capacité déplacée. Les 338 relations de v012 appartiennent à la publication antérieure, distincte du backlog courant.
- Catalogue d’informations inchangé ; aucun développement du volet data.
- **519 fichiers** de publications, révisions, décisions et historique du backlog vérifiés par empreinte : identiques. Liste : [protected-files.yaml](protected-files.yaml).

Atlas continue de présenter v012 / `2026-09-19.5`. Une prochaine release rendra ce retrait visible ; aucune ancienne publication ni règle d’affichage n’est modifiée pour masquer artificiellement un nœud publié.
