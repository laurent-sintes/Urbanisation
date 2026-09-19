# Capacités, variantes et niveaux — U261

17 septembre 2026. Étude de modélisation à partir des précisions ATP de Laurent. Catalogue de capacités et schéma inchangés. Les propositions de vocabulaire ci-dessous ne sont pas adoptées.

## Ce que distinguent les références

| Référence | Notions documentées | Portée utile pour FLOW |
| --- | --- | --- |
| BIZBOK 15.0 | Capability Level : profondeur de décomposition ; Capability Behavior : comportement selon les circonstances ; Capability Instance : réalisation dans un contexte donné | Décomposer, caractériser le comportement et contextualiser une réalisation sont trois opérations différentes. |
| SAP LeanIX | Hiérarchie de capacités ; recommandation de limiter la profondeur, généralement deux ou trois niveaux | Un niveau inférieur reste une capacité. Changer le libellé en « niveau » ne change pas sa nature. |
| Ardoq | Séparation d’une capacité abstraite et de ses instances réalisées ; analyse distincte des coûts, maturités et moyens | Des différences entre réalisations ne justifient pas nécessairement des capacités métier différentes. |
| Microsoft Inventory Visibility | Mesure ATP configurable, dimensions de regroupement et changements de stock prévus | Illustration produit d’un calcul unique décrit par ses données et paramètres ; pas un métamodèle de capacités. |

Sources primaires et passages :

- **S1 / MKT03 / ELM052 reconsulté** : [glossaire BIZBOK 15.0](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf), ©2026, pages imprimées 456–457 (PDF 3–4), entrées Capability Behavior, Instance, Level. Extrait public lu ; guide intégral non consulté.
- **S2 / MKT25 / ELM163** : [SAP LeanIX, Best Practices to Define Business Capability Maps](https://www.leanix.net/en/wiki/ea/best-practices-to-define-business-capabilities), sections 5–6, page évolutive sans édition affichée. Recommandation d’éditeur, pas nombre de niveaux obligatoire.
- **S3 / MKT26 / ELM164** : [Ardoq, Patterns for Large Enterprise Modeling](https://help.ardoq.com/en/articles/96374-patterns-for-large-enterprise-modeling), sections Atomic and Instance Capabilities et Shared Capabilities. Documentation évolutive sans édition affichée ; ne pas importer sa duplication de composants dans FLOW par défaut.
- **S4 / MKT14 / ELM165** : [Microsoft, Inventory Visibility on-hand change schedules and ATP](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise), sections configuration et fonctionnement des changements prévus/ATP. Documentation évolutive ; distinction de la fonctionnalité ATP de SCM étudiée en U260. Pas de compatibilité avec un horizon FLOW précis déduite.

Consultation le 17 septembre 2026. Synthèses sélectives sans reproduction substantielle. Les chapitres normatifs TOGAF/ArchiMate ouverts ont renvoyé une erreur ; aucune nouvelle assertion normative fondée sur ces pages. La page Ardoq Foundation a été repérée mais non lisible à l’ouverture ; non retenue comme preuve détaillée.

## Lecture des exemples de Laurent

Les quatre exemples décrivent des dimensions combinables de la même aptitude. Ils ne constituent ni quatre paliers ordonnés, ni quatre capacités distinctes par eux-mêmes.

| Dimension proposée | Question ATP | Exemple U261 |
| --- | --- | --- |
| Admissibilité des quantités | Quelle part peut soutenir ces engagements compte tenu des droits et engagements existants ? | Stock physique alloué/réservé, part libre pour le besoin considéré |
| Périmètre spatial | Quelles sources de stock peut-on mobiliser ? | Entrepôt, magasin, darkstore, tout lieu admissible |
| Disponibilité opérationnelle | À partir de quand la quantité est-elle mobilisable pour la prestation attendue ? | Réserve profonde versus emplacement proche de l’expédition |
| Disponibilité future | Quelles ressources attendues et consommations concurrentes compter à chaque date ? | Arrivage J+7 pouvant soutenir une promesse J+60 |

Ces formulations sont des analyses proposées. Ne pas définir une formule « stock moins allocation moins réservation » : les données peuvent se recouvrir, une protection de groupe peut rester admissible à un membre du groupe et la comptabilisation exacte reste à instruire. Un arrivage J+7 doit encore être compatible avec les consommations et contraintes jusqu’à J+60. Pour un ensemble de promesses, une même quantité ne peut soutenir plusieurs engagements incompatibles.

L’ATP consomme une disponibilité opérationnelle contextualisée. L’exemple RFID illustre des moyens ; il ne prescrit pas cette technologie, ni le pilotage du rangement/prélèvement par D03. D01 renseigne le stock et ses droits/engagements ; D06 et les exécutants contribuent aux délais et possibilités opérationnelles. Les contrats de données restent à préciser.

## Proposition pour FLOW

Conserver **ATP comme capacité** et ajouter, si retenu, une description structurée de ses **dimensions de prise en compte**. Des **variantes**, ou **profils de capacité**, combineraient ces dimensions pour des contextes identifiés. « Profil » est ici une proposition locale, pas un terme normatif commun aux références.

Une variante décrit la même aptitude et le même type de résultat sous un périmètre ou des règles spécifiques. Une réalisation décrit où et avec quels moyens l’aptitude existe. Une décomposition décrit des aptitudes contributrices distinctes. Ces trois liens ne sont pas interchangeables.

Exemples illustratifs de variantes :

- **ATP pour retrait magasin** : stock admissible dans le magasin, engagements concurrents, délai local de mise à disposition, horizon adapté au retrait.
- **ATP pour engagements à terme** : ressources admissibles présentes et futures, plusieurs sites possibles, échéances et engagements concurrents, délais de mobilisation.

Les mêmes dimensions existent dans les deux exemples ; leur configuration et précision diffèrent. Ni liste exhaustive ni catalogue de variantes adopté. Une variante à court terme n’est pas nécessairement moins mature. La qualité des données ou la sophistication du moteur ne se déduit pas du seul horizon.

Pour l’exploration future, une fiche ATP pourrait présenter ses dimensions puis ses variantes en détail. Les variantes resteraient distinguées de l’arbre des capacités ; aucune implémentation d’Atlas ni nouveau niveau sémantique n’est autorisé par la seule demande d’étude.

**Critère de choix proposé :** résultat métier distinct → envisager une capacité à un niveau plus fin ; même résultat sous d’autres conditions → variante ; caractéristique combinable du raisonnement → dimension ; progression évaluée selon des critères explicites → niveau de maturité ou de sophistication. Ne pas utiliser « niveau » seul pour ces quatre sens.

La correspondance CMP088 est un appui méthodologique proposé, pas une équivalence ATP/BIZBOK/LeanIX/Ardoq ni une adoption de métamodèle.


## Suite U262 — décision locale du 17 septembre 2026

Laurent retient **Comportement** comme niveau complémentaire terminal sous la capacité. La recommandation de variantes/profils ci-dessus reste l’état historique U261 et n’est pas le choix retenu. MOD006 et modeling-roadmap.yaml consignent la convention ; les exemples ATP restent proposés. BIZBOK éclaire le terme, sans imposer cette convention de profondeur à FLOW.
