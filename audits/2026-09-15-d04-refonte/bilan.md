# Refonte D04 — bilan U214/U215

15 septembre 2026. Demande U212, remplacement discuté U213, accord U214, descriptions concrètes demandées U215.

## Résultat

Le backlog contient sept capacités D04.i–o à la place de D04.e–h : Sales Order Management, Purchase Order Management, Transfer Order Management, Customer Return Management, Supplier Return Management, Order Structuring et Order Lifecycle Management. Les sept rattachements directs à D04 et les noms sont adoptés. Les responsabilités courtes présentées avant l’accord sont conservées dans [le registre de refonte](../../modeles/backlog/d04-refactoring.yaml).

Les définitions détaillées, finalités, natures et périmètres rédigés ensuite sont proposés, avec exemples par type et opérations concrètes. Les fiches expliquent les différences entre split, regroupement et spread ; firm, release et start ; hold et report ; annulation et retour ; clôture opérationnelle et financière. D03 conserve les priorités, la couverture et les promesses. La frontière Supply/Services demeure explicite, sans cycle uniforme ni réalisation physique absorbée.

Les anciennes aptitudes d’enregistrement, révision, visibilité et rapprochement sont redistribuées. Le lien D07.c → D04.h est retiré avec sa cible ; cinq nouvelles contributions vers D04.i–m sont proposées pour le rapprochement par type, avec identifiants nouveaux et sans validation héritée.

Le glossaire ajoute cinq sens de travail TER069–TER073, proposés. Aucun objet métier n’est instancié dans la carte. Q077 reste ouverte sur les règles détaillées ; C91, les études historiques, le registre des candidats et la feuille de route signalent la nouvelle orientation. Les sept nouvelles définitions sont marquées non comparées individuellement au marché ; les appuis produit U210/U211 ne prouvent aucune équivalence native ni couverture des SI.

## Conservation et vérifications

- [Snapshot complet avant modification](../../modeles/backlog/history/pre-U214.yaml), copié à l’identique ; son empreinte figure dans le registre de refonte.
- Annexes avant modification conservées ici : glossaire, candidats D03/D04 et feuille de route.
- [Vérification structurée](verification.json) : seuls D04 et ses quatre anciennes capacités sont affectés parmi les nœuds précédents. Tous les autres nœuds, relations conservées, principes, alternatives et 93 termes de glossaire préexistants sont identiques.
- Sept nouveaux rattachements, aucun lien vers une capacité retirée ; les anciennes identités et validations ne sont pas transférées. Cinq relations métier nouvelles restent proposées.
- [Empreintes avant modification](frozen-before.json) : les 61 fichiers de release, révisions et décisions contrôlés sont inchangés, sans ajout ni retrait. La release v004 / 2026-09-14.1 reste courante.
- Backlog : 52 → 55 nœuds, 34 → 37 capacités, 55 → 62 relations ; glossaire : 93 → 98 termes.
- `python scripts/refresh_sources.py` : 1088 sources courantes.
- `python scripts/validate_models.py` : zéro erreur ; release toujours à 48 nœuds et 34 capacités.
- Tests existants : 7 tests de lifecycle et 4 tests de glossaire réussis via `unittest discover -s scripts`. Le premier appel sous forme de modules échouait à importer `lifecycle` ; le mode de découverte documenté résout le chemin d’import, sans modification du code de test.
- `python scripts/render_models.py` : restitutions régénérées ; backlog dérivé du YAML courant. Aucun code Atlas modifié.

Les [descriptions lisibles](../../connaissance/29-order-management-refonte.md) restituent les champs du backlog à la date de cette opération. Elles ne constituent pas une seconde autorité métier.

Aucune publication, aucun commit et aucun push. Atlas continue donc d’afficher le découpage publié v004 jusqu’à une nouvelle release.
