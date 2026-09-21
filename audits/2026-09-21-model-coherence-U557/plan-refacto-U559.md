# Proposition de refacto — U559

Consolider le modèle Supply hors référentiels en quatre lots. Les dix constats U557/U558 sont rattachés à un lot dans [le plan structuré](../../modeles/backlog/model-consolidation-plan-U559.yaml). Cette proposition n’exécute pas le refacto et n’adopte aucun arbitrage.

## 1. Consolider les acquis et reprendre les inspirations regroupées

Corriger les noms, comptes et formulations devenus obsolètes. Reprendre sur Supply Assignment, Optimization Request Management ou Order Backlog Planning les apports utiles des anciens comportements : conservation et complément des affectations, réaffectation, impondérables, sollicitation périodique ou explicite, suivi des suites.

Pour chaque source, conserver une issue traçable : reprise dans la fiche, remplacement justifié ou maintien historique motivé. Les exemples doivent suivre les responsabilités ; le cas « conserver 70 et compléter 30 » doit notamment redevenir lisible. Une source momentanément inaccessible conserve sa limite d’accès.

**Résultat attendu :** aucun appui particulier perdu sans explication, descriptions alignées sur l’arbre courant. Aucune modification de périmètre dans ce lot.

## 2. Achever les interfaces de planification

Relier explicitement Demand Planning aux demandes connues de Sales Order et aux consommateurs de la demande publiée, notamment Inventory Optimization Planning. Qualifier ce qui est fourni, dans quelles conditions et avec quel effet ; ne pas déduire un flux installé ou un recalcul automatique.

Proposition pour les Planned Orders : Purchase Order et Transfer Order prennent en charge les demandes selon leur nature ; Order Lifecycle Management porte les mécanismes transverses, dont l’affermissement. Préciser la prise en charge d’une proposition, de ses révisions et de son retrait avant ou après création d’engagements. Le plan amont conserve sa maîtrise et n’est pas reconstruit dans FLOW.

En même temps, compléter les synthèses illustrées de Inventory Plan Application et Demand Plan Publication, puis réécrire les inspirations de Demand Planning pour couvrir toute la capacité et distinguer constat éditeur et choix FLOW.

**Résultat attendu :** Demand Planning intégrée au graphe ; continuité compréhensible entre demande planifiée et Order géré ; inspirations complètes. La répartition avant affermissement est une clarification métier proposée, pas encore adoptée.

## 3. Arbitrer trois frontières précises

| Sujet | Recommandation | Limite à conserver |
| --- | --- | --- |
| Politique de réservation | Reservation Policy Decision détermine les conditions ; **Supply Protection les configure, les maintient et les rend applicables** ; Reservation les applique aux engagements individuels. | Configuration extérieure aux Plannings. Aucun nouveau comportement par paramètre ; protection de groupe et réservation restent distinctes. |
| Décisions de satisfaction | PTP conserve le choix économique, Delivery Schedule Decision le choix d’échéancier. **Lorsqu’un plan collectif est construit, Fulfillment Plan Decision porte sa compatibilité d’ensemble** et fait réexaminer les résultats incompatibles. | Aucun passage obligatoire par un plan collectif pour chaque promesse ; aucune fusion des décisions ni pondération universelle. Fulfillment Commitment conserve propositions et engagements autorisés. |
| Besoins sans commande | **Confirmer Supply Assignment sur les commandes identifiées**, puis qualifier chaque besoin prévisionnel historique : anticipation de demande, ajustement de stock, protection d’accès ou demande déjà gérée. | Aucun forecast transformé automatiquement en Order. Un cas insuffisamment décrit reste ouvert ; il n’est ni supprimé ni affecté artificiellement. |

Les descriptions, relations et inspirations sont alignées ensemble après les arbitrages retenus. Le bénéfice attendu est un porteur explicite pour chaque résultat, sans recréer des capacités.

Les sources ne dictent pas ces propriétaires : [Microsoft — Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities) étaye la distinction politique configurée/réservation ; [Oracle — Backlog Management Processes](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faubm/overview-of-backlog-management-processes.html) distingue travail du scénario et transmission des résultats ; [Oracle — Manually Release Plan Recommendations](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faupc/manually-release-plan-recommendations.html) décrit les suites des recommandations nouvelles ou révisées. Les rapprochements complémentaires de CMP231/CMP232 restent conservés. Ces attributions sont des recommandations de cohérence FLOW, sans consensus ou innovation revendiqué.

## 4. Harmoniser et vérifier

Alléger les doublons d’éditions sans effacer la provenance et différencier les colonnes Périmètre et Approche. Vérifier, pour chaque élément modifié, la continuité entre responsabilité, successeur, justification marché et exemple.

Reprendre les 15 parcours de l’audit avec priorité aux cas touchés, contrôler hiérarchie et relations, rendre le backlog et exécuter les validations et tests concernés une fois sur l’état final. Clôturer chaque constat avec sa preuve, ou conserver explicitement ce qui reste ouvert.

**Livrable :** modèle consolidé, inspirations cohérentes, bilan avant/après et liste des décisions effectivement adoptées. Les identifiants et publications historiques sont préservés ; aucune nouvelle capacité n’est nécessaire dans cette proposition. Release, commit et push restent des opérations distinctes.

Le lot 1 peut avancer indépendamment des trois arbitrages du lot 3. Les inspirations accompagnent chaque changement métier ; le dernier lot vérifie leur cohérence d’ensemble.
