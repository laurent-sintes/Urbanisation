# FLOW — instructions de travail

## 1. Priorités et autorités

Échanger en français et tutoyer Laurent. Lire les éléments concernés avant modification. Les instructions courantes sont ici ; les accords et leurs portées sont dans les sources et le modèle. Un historique ne réactive pas une règle remplacée.

| Besoin | Autorité |
| --- | --- |
| Construire ou discuter le modèle, par défaut | `modeles/backlog/model.yaml` ; annexes YAML pour les propositions et arbitrages |
| Consulter le modèle publié / Atlas | `modeles/release/index.json` → descripteur → snapshot ; aucun choix par tri ni complément depuis le backlog |
| Vocabulaire métier | `modeles/backlog/glossary.yaml` |
| Vocabulaire méthodologique | `modeles/backlog/modeling-glossary.yaml` ; distinct du glossaire métier |
| Connaissance de l’existant | `modeles/panorama-as-is/current.json` ; trois SI et contexte partagé |
| Preuves et corrections | `connaissance/01-contributions-utilisateur.md`, `connaissance/04-corrections.md`, décisions et provenance |
| Schémas, validation, publication | [guide des modèles](modeles/README.md), `modeles/schemas/`, `scripts/validate_models.py` |

Le YAML fait autorité pour le backlog et les nouvelles publications métier. Utiliser `scripts/structured_io.py` ; ne pas créer un modèle JSON concurrent. Index et fichiers techniques JSON restent légitimes. Le Markdown explique et restitue, sans devenir un deuxième catalogue.

## 2. Modélisation : sens avant découpage

- Une capacité décrit **ce que sait faire durablement l’entreprise, indépendamment de son organisation et de ses outils**. Distinguer résultat, finalité, périmètre et nature. Une opération, une fonctionnalité de produit ou un composant logiciel ne suffit pas à définir une capacité.
- Un domaine est un espace cohérent de problèmes métier, pas automatiquement une application ou un bounded context. Les capacités d’action gardent une maille large ; les décisions peuvent être plus fines.
- **Capacité → Comportement** est la décomposition descriptive terminale (U262). Un comportement appartient explicitement à une seule capacité de même couche ; aucun sous-comportement. Plusieurs comportements peuvent se combiner sans former une séquence.
- **Toute décomposition doit être justifiée par une complexité OU un bénéfice ciblé (U265).** Consigner cette justification sur la capacité dans `fields.decomposition_rationale`. Ne pas décomposer systématiquement ni créer un comportement pour chaque bouton, interface ou paramètre. L’exigence est adoptée ; chaque justification éditoriale garde sa propre portée de validation. L’audit [U265/U266](audits/2026-09-17-audit-comportements/rapport.md) propose les critères et refontes à instruire.
- **Maille des comportements (U282/U283)** : Mécanisme, Politique, Variante ou bénéfice sont les critères différenciants. Décrire une façon d’agir et son effet métier ; les opérations sur un concept restent matière de conception produit. Pour Planning, expliciter les impacts sur les pratiques humaines et les processus. Ne pas créer quatre niveaux ni décomposer systématiquement. Supply Protection : ancien découpage par opérations en réexamen. ATP inchangé à ce stade.
- Objets métier, documents et événements restent distincts ; ils ne sont pas des niveaux inférieurs de comportement. Leurs liens ne présument ni possession exclusive, ni cardinalité, ni ordre d’exécution.
- Déduire l’arbre uniquement des relations explicites. `contains`, `presents` et les liens métier transversaux ont des sens différents. Business References est un groupe de présentation ; Universe est un niveau d’urbanisme. Un lien « a besoin de » n’est pas une décomposition.
- Conserver les identifiants, y compris ceux dont le préfixe est historique. Ne pas renuméroter ni réutiliser un identifiant retiré. Qualifier `relates-to` par `qualification.meaning`, avec conditions, effets et sources lorsqu’ils sont connus.
- **Vocabulaire stabilisé U275/U289** : Supply Assignment = affectation des ressources aux commandes ; Supply Assignment Plan = plan d’affectation. Allocation seul est réservé aux citations/termes éditeurs ou historiques qualifiés. Pour les groupes, employer enveloppes de protection, droits d’usage ou plafonds. Répartition/distribution sont des verbes à complément explicite. Convention : modeles/backlog/assignment-terminology.yaml.
- Noms en anglais, définitions en français ; décrire factuellement, sans niveaux promotionnels comme Advanced ATP. Garder aATP comme appellation SAP dans la comparaison marché. Préférer un résultat explicite à « tenir » ou « fonction » sans qualificatif ; aucun renommage automatique de noms adoptés.

## 3. Décision, Planning, Management

- **Decision** détermine une réponse métier et intègre ses calculs. Ne pas recréer une maille Calculation pour le seul calcul.
- **Planning mobilise les décisions**, qui restent distinctes. U283/U284 retiennent comme comportements la construction de scénarios alternatifs, Simulation & analyse (un seul comportement) et l’adaptation de l’exécution d’un scénario. L’analyse des impacts est intégrée à Simulation & analyse ; évaluation, validation et application restent des fonctions utiles, sans comportement autonome justifié à ce stade. Le découpage U269/U271 en six comportements est historique et en réexamen. Noms, définitions et migration du catalogue à préciser ; aucun transfert implicite de l’adaptation opérationnelle de D06 vers D05.
- **Promise Management (U288)** : regroupement de Promise Proposal, Promise Confirmation et Promise Revision adopté, avec ces trois responsabilités comme comportements. Ne plus les qualifier de simples fonctions dans la cible. Préserver leurs effets distincts et les frontières ATP/CTP/PTP, affectation et réservation ; détails de migration et formulations nouvelles restent proposés.
- **Application de plan (U287/U289)** : le plan évoqué par Laurent est un plan d’affectation de ressources à des commandes, pas une répartition magasin. D04 porte le principe d’application sur les Orders ; son parent précis reste à arbitrer. Supply Assignment conserve le lien ressources-commandes ; ni création de transfert ni transfert de responsabilité implicite.
- Stock Protection relève de la gouvernance/management. Appliquer signifie mettre à jour transactionnellement les données : unité, groupe ou masse ; écran, batch, flux ou streaming. Ces modalités ne créent pas à elles seules de nouvelles capacités ; leurs comportements éventuels doivent être utiles et justifiés.
- Distinguer décision, mise à jour transactionnelle, déclenchement et réalisation physique, sans imposer une organisation humaine, un découpage logiciel, l’atomicité d’un lot ou un contrôle manuel. L’automatisation est possible.
- Conserver les décisions spécialisées plutôt qu’un agrégat Stock Protection Decision. Ne pas renommer implicitement **Supply Protection** en Stock Protection ou Inventory Policy Management. La généralisation de Management hors du cas discuté reste proposée (MOD003).
- Couverture : distinguer possibilités, affectation, réservation, promesse et réalisation. MOD005 porte la convention méthodologique ; TER022/TER077 portent les sens métier. La convention détaillée reste proposée.

## 4. Frontières métier à préserver

| Périmètre | Responsabilité |
| --- | --- |
| D01 Inventory Management | Connaître et fiabiliser le stock, enregistrer les mouvements, protéger et réserver ; distinguer état, mouvement et ressources futures. |
| D03 Order Promising | Décider comment satisfaire les Orders. Conserver ATP/CTP/PTP à la maille retenue, priorités et échéancier. ATP établit les possibilités de référence ; CTP examine leur faisabilité sous adaptation en mobilisant les décisions spécialisées ; PTP arbitre économiquement. |
| D04 Order Management | Un type d’Order par capacité de gestion : vente, achat, transfert, retour client, retour fournisseur. Structuring et Lifecycle sont transverses, pas copiés sous chaque type. Conserver les exemples split, spread, affermissement, lancement, attente/reprise, report, annulation, clôture. |
| D05 Inventory Optimization | « Optimiser le stock consiste à choisir un compromis entre disponibilité, immobilisation et risque, puis à décider des ajustements nécessaires. » Quatre décisions (Coverage Target, Stock Allocation, Replenishment, Stock Redistribution) et Inventory Planning. |
| D06 Execution Management | Huit capacités ; orchestration et décision d’adaptation séparées. Capacité opérationnelle contextualisée, prestations requises, choix de services, gestion des Service Orders, tracking et rapprochement. D07 retiré comme domaine ; ses capacités gardent leurs identifiants sous D06. |
| Référentiels Supply | Projections de maîtres externes : au moins ingestion, lecture/recherche possibles. Aucune administration de données maîtresses introduite implicitement. |

Un transfert peut servir la satisfaction d’un Order ou l’optimisation du stock : l’opération commune ne fusionne pas D03 et D05. Après U283/U284, la mise en action reste une fonction d’Inventory Planning : déclencher les actions retenues et connaître leur prise en compte **via les capacités opérationnelles responsables** (Supply Protection, D04 et D06), sans comportement autonome Scenario Application. Leurs responsabilités restent distinctes ; validation du scénario, application transactionnelle et réalisation physique ne se confondent pas. Le calcul des besoins nets appartient à Replenishment Decision (D05.b retirée).

D14 décrit l’offre des services exécutants, leurs accès et SLA globaux configurés, y compris services documentaires. D06 rend visible leur capacité opérationnelle dans le contexte ; D03 en a besoin pour la promesse Supply. D06 orchestre les prestations et réagit aux échecs ; il ne crée pas une seconde promesse Supply. Conserver SLA configuré, engagement individuel, estimation et résultat distincts. La latitude d’adaptation est à préciser séparément, sans bloquer le catalogue (U243). Fusion Execution Service Decision et détails éditoriaux restent proposés selon leurs portées.

Les couches transactionnelle Supply et processus Business Services gardent leurs modèles et contrats. Toutes deux peuvent porter décision et orchestration ; Case Management est l’approche de réalisation de la couche processus. Ne pas inventer ses domaines à partir d’un portail, ni un Order ou cycle universel. Les exécutants gardent leurs opérations internes ; logistique en adhérence, C-Log autonome. Finance, contrôle de gestion, conformité, design produit et planification de saison sont exclus comme domaines ; leurs interfaces utiles restent documentables.

Party / Role, Agreement et Catalog restent distincts et contigus dans leur présentation. Agreement reçoit les références Party/Catalog et conditions utiles ; commande et Agreement ne se confondent pas. Product/Variant, rôles Article/Container et Product Unit restent distincts. Ne pas déduire un maître externe précis sans preuve ni étendre cette règle aux données transactionnelles.

## 5. Validation, provenance et marché

Publier ne vaut pas valider. Un Go s’applique au contenu présenté et à sa portée : champs, valeurs et rattachements explicites. Ne pas étendre un accord aux compléments éditoriaux, descendants ou nouvelles valeurs. Conserver empreintes et accords historiques ; `lifecycle`, `review` et décisions `ADOPT-*` ne remplacent pas la qualification champ par champ.

Enregistrer d’abord les apports métier de Laurent dans les contributions, puis interpréter. Préserver verbatims, archives ChatGPT, sources et réserves. Employer les noms canoniques dans le texte rédigé, notamment Boardriders ; préserver les identifiants et citations d’origine.

Distinguer proposition cible, applicabilité, couverture documentée et preuve de réalisation installée. Sarenza reste non évalué tant qu’aucune étude ne le documente ; absence de ligne ou de donnée ≠ absence de couverture. Ne pas inventer les extrémités de flux, dates d’observation ou maîtres d’information. Une pertinence FLOW ne présume pas un développement interne.

Suivre [la méthode marché](marche/methode.md) et actualiser les correspondances quand un périmètre change, ou les marquer à instruire. Identifier source primaire, édition, date, passage, nature de l’élément, rapprochement et limites. Une fonctionnalité produit, un processus, un composant ou une API n’est pas automatiquement une capacité ; les niveaux éditeurs ne s’alignent pas numéro pour numéro. Préférence Microsoft pour le nommage de l’optimisation et intérêt pour la séparation SAP planification/mise en action : aucun catalogue complet adopté. Une documentation éditeur ne prouve aucun déploiement Beaumanoir.

**Règle de discussion U268 :** comparer chaque proposition de Laurent aux références pertinentes du marché, avec sources effectivement consultées, points communs, écarts et limites. Justifier chaque proposition de Codex par le marché ou par la cohérence avec notre modèle, en explicitant le bénéfice, les frontières et le compromis. Ne pas simplement approuver ni invoquer « le marché » sans preuve ; distinguer constat sourcé, interprétation et recommandation. Si la comparaison n’est pas établie, le signaler sans inventer d’équivalence. Cette règle ne vaut pas validation des propositions discutées.

## 6. Exécution du travail et Atlas

1. Lire modèle, annexes et corrections utiles. Préserver le travail existant ; séparer corrections sans changement de sens et arbitrages à valider.
2. Modifier le backlog et ses explications. Actualiser l’index courant avec `python scripts/refresh_sources.py`, contrôler avec `python scripts/validate_models.py`, puis dériver les vues avec `python scripts/render_models.py`. Exécuter les tests pertinents ; ne pas réimporter le Markdown historique via les scripts de migration.
3. Release, commit, push et administration serveur sont distincts ; utiliser leurs skills pour les demandes correspondantes. Pas de déclenchement implicite, ni de confirmation systématique pour une action déjà demandée. `push` cible Urbanisation ; `flow-push` concerne FLOW-Program. Ne pas changer l’identité Git globale.
4. Préserver les octets des publications, révisions, preuves et archives ; `.gitattributes` interdit leur normalisation implicite. Une correction publiée exige une nouvelle version. La release se construit depuis une préparation figée contrôlée, jamais un ancien snapshot ignorant le backlog courant.
5. Atlas présente exclusivement les publications sous Urbanisation ; historique sélectionné fixe, courant suivi automatiquement. Glossaire et liens résolus dans le même snapshot ; aucun repli backlog. Ne pas publier le glossaire méthodologique comme glossaire métier.
6. Frontend React / TypeScript / React Flow, arbre gauche, fiche centrale, recherche, comportements et liens directs. Aucun historique de visites. Identité : [app/BRANDING.md](app/BRANDING.md). Compiler avec `pnpm --dir app build` puis recharger la page ; Python sert `app/dist/`, sans Node permanent.
7. Serveur local en lecture seule, port 8765 par défaut, lanceur `Lancer-FLOW-Atlas.ps1` et skill server-admin. Vérifier l’identité avant arrêt/redémarrage ; redémarrer après changement Python si nécessaire, pas pour un simple changement de données. Aucun navigateur lancé sans demande.

## 7. Lecture ciblée et historique

Consulter seulement les dossiers utiles au travail, sans charger tout l’historique dans les instructions :

- Stock, D03–D05 : `stock-order-boundary.yaml`, `d03-review.yaml`, `d04-refactoring.yaml`, `d05-refactoring.yaml` dans `modeles/backlog/`.
- D06/D14 : `modeles/backlog/execution-services-review.yaml` ; ATP : [comportements](connaissance/34-comportements-atp.md).
- Inventory Planning : [historique et réexamen U283](connaissance/35-comportements-inventory-planning.md) ; direction courante dans `modeles/backlog/d05-refactoring.yaml`, section `planning_mechanisms_U283`. Accords U269/U271 conservés avec leurs empreintes.
- Extensions et applicabilité : `modeles/backlog/modeling-roadmap.yaml`, `modeles/backlog/applicability.yaml` ; trois contextes As Is et FLOW cible, sans assimilation.
- Refonte courante U286 : [cible complète et arbitrages](audits/2026-09-17-refonte-modele/rapport.md), annexe proposée faisant autorité pour cette étude : modeles/backlog/refactoring-target.yaml. L’audit U265/U266 reste historique ; ses découpages par opérations ne sont plus des recommandations courantes.
- Versions et processus détaillés : [modeles/README.md](modeles/README.md), [app/README.md](app/README.md), sources des skills dans `skills/` (répercuter leurs évolutions dans les copies personnelles sans écraser de skill tiers).

Consolidation U265/U266, 17 septembre 2026. L’intégralité du précédent AGENTS.md est conservée dans [la capture historique](audits/2026-09-17-audit-comportements/AGENTS-before.md), avec ses états successifs et chemins relatifs à la racine du dépôt. Elle sert à retrouver une provenance, pas de deuxième jeu d’instructions courantes. Les nombres et versions courants se lisent dans les modèles et index, pas dans des paragraphes datés.
