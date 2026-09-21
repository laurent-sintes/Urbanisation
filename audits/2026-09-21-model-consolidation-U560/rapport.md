# Consolidation autonome du modèle — U560

21 septembre 2026. Réalisation du [plan U559](../2026-09-21-model-coherence-U557/plan-refacto-U559.md), hors référentiels. [Manifest détaillé](../../modeles/backlog/model-consolidation-U560.yaml).

**Le refacto est appliqué au backlog : neuf constats sont résolus dans le modèle de travail ; le dixième est clarifié avec une réserve métier conservée.** Les choix de travail de Codex sont tracés ; l’instruction d’autonomie n’a pas été transformée en accord de Laurent sur tous les nouveaux champs.

## Responsabilités et coopérations

- **Demand Planning** est reliée aux demandes de vente connues et à la consommation de sa demande publiée par Inventory Optimization Planning. La publication n’impose ni recalcul ni application du plan consommateur.
- **Les propositions planifiées** sont prises en charge selon leur nature par Purchase Order ou Transfer Order. Order Lifecycle Management gouverne les transitions. Leur révision ou retrait est rapproché des suites déjà engagées ; le plan amont n’est pas reconstruit.
- **Les politiques de réservation** sont déterminées par Reservation Policy Decision, configurées et rendues applicables par Supply Protection, puis utilisées par Reservation pour les engagements individuels. Les liens distinguent recommandation et politique active.
- **Les décisions de satisfaction** conservent leurs résultats propres. Lorsqu’un scénario collectif est construit, Fulfillment Plan Decision en porte la compatibilité et fait réexaminer les résultats incompatibles. Fulfillment Commitment conserve les propositions et engagements autorisés. Un plan collectif n’est pas obligatoire pour toute promesse.
- **Supply Assignment** porte les commandes identifiées, y compris les intentions planifiées prises en charge selon leur type et leurs conditions. Les besoins sans commande sont distingués selon leur finalité ; aucun forecast n’est transformé automatiquement en Order.

Les descriptions obsolètes de Supply Planning, du nombre de capacités de Fulfillment Optimization, de Supply Reassignment et de la redistribution ont été corrigées. Les 154 nœuds, leurs noms, leurs identifiants et leur décomposition sont conservés. Le lot modifie 26 fiches, qualifie six relations existantes et ajoute quatre coopérations : le modèle contient désormais 365 relations.

## Inspirations

Les quatorze occurrences documentaires portées par les sept comportements regroupés sont tracées vers leurs successeurs. Supply Assignment retrouve notamment les exemples de complément d’une affectation et de réaffectation ; Optimization Request Management retrouve les illustrations de sollicitation et de suivi des suites.

Les deux synthèses manquantes d’Inventory Plan Application et de Demand Plan Publication sont complétées. Demand Planning distingue désormais les approches Oracle/SAP de l’adaptation FLOW. Les éditions répétées sont regroupées au premier plan, avec conservation des preuves antérieures ; les colonnes Périmètre et Approche sont différenciées.

Les 128 fiches du périmètre audité disposent d’une synthèse illustrée et d’au moins deux documents de comparaison distincts. Leurs correspondances restent qualifiées selon leur apport réel ; ce contrôle documentaire ne transforme pas les choix FLOW en consensus du marché.

Microsoft Firm planned orders et commercetools Inventory overview ont été directement reconsultés ; les lectures ciblées des audits et du plan sont conservées. Les portails SAP Reassignment, EDQA, Supply Assignment et Workflow using Apps n’ont pas fourni de texte exploitable lors des contrôles d’accès : leurs passages et exemples antérieurement documentés sont repris avec leur date et leur limite, sans inventer une nouvelle vérification.

## Réserve maintenue

**AUD557-05 reste partiellement résolu.** La frontière de Supply Assignment est explicite, mais certains besoins prévisionnels historiques ne sont pas identifiés par des cas métier assez précis. Leurs mentions sont conservées ; une affectation exhaustive à Demand Planning, Inventory Optimization Planning, Supply Protection ou à une famille d’Orders ne peut pas être affirmée sans inventer leur sens.

Cette réserve n’empêche pas la consolidation appliquée. Elle ne réouvre pas l’audit des comportements clos U431 et n’introduit pas une capacité générique supplémentaire.

## Vérification

- [Validation du projet](validation.json) : zéro erreur.
- [Contrôles, tests et intégrité](verification.yaml) : 30 tests réussis sur inspirations, comparaisons, pluralité des références, comportements et relations ; restitution backlog régénérée.
- [Revue des 15 parcours](scenario-review.yaml) : responsabilités et frontières relues, avec la réserve historique isolée.
- Référentiels et leurs relations incidentes, catalogue Information, glossaires, principes et hiérarchie préservés ; aucune publication historique modifiée.

La [baseline complète](model-before.yaml) conserve l’état avant intervention. Le statut de chaque constat, les champs touchés, les références reprises et les éditions consolidées restent dans le manifest. Aucune release, opération serveur, commit ou push n’a été effectué.
