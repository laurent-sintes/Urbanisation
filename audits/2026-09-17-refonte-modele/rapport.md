# Refonte du modèle FLOW — cible complète U286

17 septembre 2026. **Cible de référence préparée U286–U289, socle appliqué U290.** Cette page conserve les propositions telles que présentées avant migration ; les statuts courants et écarts sont dans le [bilan de mise en œuvre](../2026-09-17-refonte-appliquee/rapport.md). Les mentions de catalogue inchangé et arbitrages à venir ci-dessous décrivent cette revue antérieure.

**41 capacités examinées, 15 comportements actuels traités et 103 relations existantes revues.** Cible recommandée : 39 capacités après le regroupement adopté Promise Management, hors éventuelle capacité supplémentaire pour U287 ; 14 comportements de cœur, plus 4 conditionnels. Un mécanisme supplémentaire d’application de plan est retenu dans D04 (U287), avec capacité parente à préciser. Ces nombres sont un résultat du découpage proposé, pas un quota.

Le niveau Capacité → Comportement reste suffisant pour les cas examinés. La refonte porte sur le sens, les frontières, les descriptions et les dépendances. Case/Business Services et les réalisations des trois SI ne sont pas audités ici.

Autorité de cette proposition : [annexe YAML](../../modeles/backlog/refactoring-target.yaml). Le modèle actif reste [model.yaml](../../modeles/backlog/model.yaml). Ce document et les fiches sont dérivés de l’annexe.

- [Matrice avant/après et 41 fiches](capacites.md)
- [Comportements proposés et migration des 15 existants](comportements.md)
- [Dépendances et revue de toutes les relations](relations.md)
- [Sources primaires et limites](sources.md)

**Précision U289 :** Supply Assignment = affectation des ressources aux commandes ; Supply Assignment Plan = plan d’affectation. Allocation seul est écarté des libellés FLOW. [Étude et convention](../../marche/assignment-allocation-convention.md). L’interprétation du plan U287 comme répartition magasin est corrigée.

## Ce que change la cible

| Ensemble | Proposition concrète | Portée |
| --- | --- | --- |
| Inventory Planning | Construction de scénarios alternatifs ; Simulation & analyse ; adaptation du scénario en cours | Directions adoptées U283/U284 ; noms anglais et synthèses proposés |
| Supply Protection | Group Supply Protection ; Consumption Capping ; Safety Stock Policy ; Replenishment Regulation | Liste, définitions et articulation proposées |
| Order Management | Application des conséquences du scénario / plan d’affectation sur les Orders | U287 précisé U289 ; liens ressources-commandes conservés par Supply Assignment ; A8 à instruire |
| ATP | Conserver ses quatre comportements | Définitions adoptées conservées ; justification enrichie proposée |
| Promise Proposal / Confirmation / Revision | Promise Management avec trois comportements Proposal, Confirmation et Revision | Regroupement et décomposition adoptés U288 ; 41 → 39 hors U287 |
| Reservation / Supply Assignment | Maintenir en attendant une frontière démontrée | Arbitrage A3 ; pas de fusion automatique |
| Order Lifecycle Management | Nature management, autorisation et application des transitions | Arbitrage A4 |
| Stock Allocation Decision | Nom cible Group Protection Decision, même décision de droits par groupe | Clarification lexicale proposée U289 ; nom actif conservé |
| Replenishment Decision | Décider aussi les ajustements des apports futurs excessifs | Arbitrage A5 ; application par D04 |
| Stocktaking / Execution Orchestration | Deux mécanismes candidats chacun | A6 ; option conditionnelle, pas nécessaire au cœur |

Le bénéfice du refacto ne se mesure pas à la réduction du nombre de nœuds. Les opérations restent expliquées ; elles quittent la hiérarchie lorsqu’elles ne différencient pas une manière d’agir.

## 1 — Changements déductibles des accords

- Conserver domaines, décisions spécialisées et niveau terminal.
- Préparer les trois comportements Planning, dont Simulation & analyse.
- Sortir les opérations d’allocation de la cible de comportements, garder les détails.
- Balisage des recommandations obsolètes et correction des consignes actives.
- Conserver les quatre comportements ATP ; justifications enrichies proposées.
- Intégrer U287 : mécanisme d’application d’un scénario/plan dans D04 ; capacité parente et détails à préciser.
- U288 : regrouper les trois capacités de promesse sous Promise Management avec trois comportements, en conservant historique et dépendances.

**Déjà réalisé dans cette passe :** cible exhaustive, table de migration, preuves marché, nettoyage des consignes actives et signalement de l’ancien audit comme historique depuis AGENTS. Ses fichiers historiques sont conservés. Les mutations du catalogue sont préparées dans la proposition ; aucune nouvelle valeur n’est présentée comme adoptée par ce seul travail.

## 2 — Arbitrages conjoints

| Repère | Sujet | Recommandation | Décision attendue |
| --- | --- | --- | --- |
| A1 | Supply Protection | Quatre mécanismes proposés ; fonctions d’allocation conservées. | Retenir ou ajuster les quatre résultats, noms et frontières. |
| A2 | Promise Management | Promise Management avec Promise Proposal, Promise Confirmation et Promise Revision comme comportements. | Regroupement et décomposition adoptés U288 ; préciser formulations et identités lors de la migration. |
| A3 | Reservation / Assignment | Maintenir provisoirement les deux ; tester engagement opposable versus affectation. | Propriété du droit, décompte, rattachement et cas discriminants. |
| A4 | Order Lifecycle Management | Nature management couvrant gouvernance et application des transitions. | Valider ce périmètre ou démontrer un résultat de décision autonome. |
| A5 | Replenishment et surstock | Étendre D05.e aux ajustements des apports futurs, mise en action D04. | Valider le périmètre sur apports déjà fermes sous contraintes. |
| A6 | Décompositions complémentaires | Deux mécanismes Stocktaking et deux Orchestration, conditionnels. | Confirmer bénéfice et mandat avant création. |
| A7 | Dépendances et données | Valider résultats et producteurs sur cas concrets, surtout engagement/disponibilité. | Contrats métier et conditions ; pas graphe d’appels logiciel. |
| A8 | Application de plan dans Order Management | Appliquer les conséquences du plan d’affectation aux Orders, sans transférer le lien ressources-commandes de Supply Assignment vers D04. | Déterminer si une responsabilité D04 transverse est nécessaire après clarification U289 ; ne pas inventer des transferts magasin. |

**Ordre conseillé : A1 Protection et A8 application de plan, A3 engagement, A4/A5 cycle et apports ; A2 est résolu par U288, A6 reste optionnel.** A7 accompagne chaque cas. La mise en cohérence Planning est déjà cadrée par nos accords ; les détails éditoriaux proposés sont regroupés dans ses fiches.

## Protection : couverture et limites

| Préoccupation | Destination proposée | Limite |
| --- | --- | --- |
| Accès concurrent / surconsommation | PROTECT-GROUP, PROTECT-CAP | Fait consommant les droits et correction à définir ; pas de double décompte avec réservation. |
| Pénurie / incertitude | PROTECT-BUFFER, PROTECT-REPLENISH | Sécurité, seuil et cible se combinent sans addition automatique. |
| Surstock futur / fin de vie | PROTECT-REPLENISH, D05.e | Limiter nouveaux apports ; ajustement des commandes fermes soumis à arbitrage puis D04. |
| Surstock existant | D05.c | Protection ne réalise ni redistribution, ni retour, ni markdown ou destruction. |
| Présentation / espace / péremption / lots | PROTECT-REPLENISH, D05.a, D05.e | Contraintes selon le cas ; aucun comportement par paramètre ni nouvelle maîtrise des données externes. |
| Validité / activation / dérogation / masse / suivi | D02.b | Propriétés et fonctions de gouvernance ; dérogation explicite avec portée et durée. |

## Application de scénario ou plan dans Order Management — U287

Appliquer aux Orders les conséquences autorisées d’un scénario ou d’un plan d’affectation des ressources aux commandes, avec origine, portée et résultat de prise en compte.

**Bénéfice :** Assurer la cohérence des Orders avec les choix retenus sans confondre leur modification avec la tenue des liens ressources-commandes.

**Exemple :** Un plan affecte 100 pièces disponibles à deux commandes pour 60 et 40. Supply Assignment tient ces affectations ; D04 applique les évolutions d’Orders nécessaires et autorisées, qui peuvent être nulles si les Orders ne changent pas.

**Rattachement :** Choisir le porteur de l’application sur les Orders après distinction entre décisions, affectations et mutations d’Orders. Si le plan ne change que les liens ressources-commandes, Supply Assignment reste le responsable courant ; aucune capacité D04 supplémentaire ne se déduit de ce cas.

**Marché :** [S13 — Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming), [S14 — Oracle](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/release-plan.html)

**Frontières :**
- D05 : Planifie le stock souhaitable ; un plan d’affectation aux commandes n’est pas automatiquement un scénario Inventory Planning.
- D04 : Applique seulement les évolutions d’Orders issues du plan ; ne remplace pas Supply Assignment pour la tenue des affectations.
- D02.b : Applique les politiques, seuils et droits par groupes ; un plan d’enveloppes sans Orders ne devient pas une création de commandes.
- D03 : Supply Assignment conserve les liens ressources-commandes ; décisions et Promise Management conservent la promesse. Le besoin de décision collective d’affectation reste à instruire sans déplacer silencieusement les responsabilités.
- D06 : Coordonne les prestations et décide les variations opérationnelles ; matérialisation d’un plan d’Orders ne vaut pas exécution physique.

Les quatre mécanismes de Protection se combinent. Le stock de sécurité exprime le rôle de tampon ; la régulation indique quand et comment renouveler. Une même valeur peut intervenir dans les deux, sans être comptée deux fois. La protection d’un groupe préserve son accès ; le plafond limite sa consommation. La fin de vie est d’abord un contexte de ces politiques, sans comportement additionnel automatique.

## Cas pour éprouver les frontières

**CASE1 — 100 présentes, 30 réservées, enveloppe web 40 dont 10 consommées ; demande web 20.**
Préciser les recouvrements avant calcul ; éviter stock moins réservation moins enveloppe sans contrat.
Résultat attendu : Décompte expliqué ; aucune valeur imposée sans les données manquantes.

**CASE2 — Cible 100, présentes 30, arrivage ferme 80, demande en baisse.**
D05.e recommande ; D04 examine réduction/report des 10 excédentaires.
Résultat attendu : Si non modifiable, excès explicité ; aucune modification silencieuse.

**CASE3 — 100 à livrer, 60 préparées, collecte impossible.**
D06.f choisit, D06.d coordonne, D03 révise si nécessaire ; D05 adapte son scénario de stock.
Résultat attendu : Ni deuxième autorité sur transporteur/promesse, ni oubli des faits irréversibles.

**CASE4 — Deux scénarios de stock aux effets service/coûts différents.**
Construction des hypothèses ; Simulation & analyse des conséquences ; validation et application décrites.
Résultat attendu : Trois comportements sans perte d’analyse des impacts ou de gouvernance.

**CASE5 — 100 pièces affectées pour 60 et 40 à deux commandes ; une évolution d’Order requise par le plan est refusée.**
Supply Assignment tient les affectations ; D04 explicite la modification prise en compte ou refusée ; la cohérence du plan est réexaminée.
Résultat attendu : Aucune assimilation affectation/promesse/modification Order ; pas de transfert physique automatique.

## Manques à instruire

- **Disposition des retours** : Localiser la décision réintégration/réparation/rebut/renvoi avant nouveau nœud. Supply, Case ou exécutant ? Comparaison nouvelle non réalisée dans cette passe.
- **Données de décision** : Décrire demande future, coûts, risques, délais, règles et fraîcheur en entrées. Producteurs et contrats inconnus pour certains cas ; aucun maître inventé.
- **Capacité disponible / mobilisation** : Consommer connaissance contextuelle D06.b et délai effectif article/lieu. Responsable du délai et sémantique de capacité restante avec les exécutants.

## Migration et contrôles

- Figer remplacements et attribuer des IDs neufs sans réemploi.
- Migrer valeurs, scopes et relations en conservant les anciennes valeurs et accords.
- N’adopter que les champs/valeurs effectivement validés.
- Vérifier chaque ancien nœud/lien, les liens model: et les vues dérivées.
- Atlas : contrôler arbre, recherche et fiches lors d’une publication demandée ; aucune réécriture du moteur justifiée.

Les relations proposées sont orientées « consommateur a besoin du fournisseur ». Les liens historiques conservent leur sens natif ; aucune inversion mécanique. Les liens d’information et d’application peuvent être réciproques selon la phase, sans imposer un appel récursif ni une séquence logicielle.

Le contrôle de couverture vérifie chaque capacité, ancien comportement et relation, les références et les rattachements uniques. Il ne remplace pas les arbitrages métier. Rapport technique : [checks.json](checks.json).

Régénération : python -m scripts.render_refactoring_target. Les publications, accords historiques et valeurs du catalogue actif restent préservés.
