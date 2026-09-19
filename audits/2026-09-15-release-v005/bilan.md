# Publication v005 — U216

Publication `2026-09-15.1`, activée le 15 septembre 2026 à `14:42:23.827866Z` : [descripteur](../../modeles/release/urbanisation-v005-2026-09-15-144223.yaml), [note de release](../../modeles/release/2026-09-15.1/release-notes.md).

## Contenu et portée

51 nœuds, 37 capacités, 54 relations, 98 termes de glossaire. D04.i–o remplacent D04.e–h ; cinq contributions proposées de D07.c alimentent le rapprochement par type d’ordre. Les cinq nouveaux termes TER069–TER073 et les descriptions concrètes U215 sont publiés comme proposés. Alternatives, illustrations et annexes sont figées comme contexte, sans intégration silencieuse dans la carte.

La comparaison identifie uniquement D04 comme nœud existant modifié, sept capacités et douze relations ajoutées, quatre capacités et cinq relations retirées, ainsi que cinq nouveaux termes lexicaux. Les principes sont inchangés. Les cinq alertes de sens concernent les nouvelles capacités et leurs liens vers les nouveaux termes de même type ; examen cohérent avec les descriptions proposées, sans validation des définitions déduite de la publication.

63 décisions : 48 reprises compatibles et 15 transcriptions sourcées. Quatorze transcrivent U214 sur les sept noms et les sept rattachements ; la dernière reprend seulement le nom inchangé Order Management sur la nouvelle révision de D04, avec examen explicite de sa portée. Les descriptions nouvelles ne sont pas approuvées par ces décisions. ADOPT-049 reste historique sur l’ancienne révision de D04 ; ADOPT-050–053 restent attachées aux quatre capacités retirées. Aucun transfert de validation vers une nouvelle identité.

Le [rapport initial](initial-report.json) signale les décisions manquantes avant transcription. Les [décisions nouvelles](new-decisions.json) corrigent ces lacunes de preuve sans changer le modèle ni inventer de validation. Le candidat préparé ne comporte aucune erreur. Le rapport définitif est figé dans la publication.

## Vérification

- Préparation et publication réalisées par `prepare_release.py`, activation de l’index en dernier.
- `validate_models.py` : zéro erreur ; 1089 sources, 63 décisions.
- `render_models.py` : restitutions régénérées.
- `app/server.py --check` : release correcte et frontend prêt ; aucun redémarrage nécessaire pour ces données.
- [Réponses API vérifiées](atlas-api.json) : FLOW Atlas, racine du projet, PID 19836, espace release ; version `2026-09-15.1` et `sourcePath: modeles/release/2026-09-15.1/model.yaml`. Identités, sept rattachements D04, compteurs et tous les champs des nœuds servis correspondent au fichier publié. Catalogue courant aligné sur la nouvelle publication.
- Empreintes des 60 fichiers historiques release/révisions/décisions inchangées par rapport au contrôle avant refonte ; seul l’index existant est modifié pour activer v005.
- Navigateur Atlas : v005 visible en publication courante ; arbre et carte Supply affichent les sept capacités D04 et leurs liens directs.
- Clic sur Order Lifecycle Management : fiche D04.o dans v005, opérations Firm/Release/Start, Hold/Resume, Postpone/Advance, Cancel/Close et exemple 100/60/40 présents. Le statut montre uniquement le libellé adopté, avec Définition/Finalité/Nature/Périmètre à valider.
- Page Glossaire : 98 termes, dont Sales Order, Purchase Order, Transfer Order, Customer Return Order et Supplier Return Order ; version v005 conservée.

Un ancien onglet du navigateur affichait une erreur de connexion antérieure ; un chargement neuf de la même adresse a abouti. L’API était disponible et aucun changement serveur n’a été nécessaire.

Atlas est disponible sur [127.0.0.1:8765](http://127.0.0.1:8765/). Les versions antérieures restent sélectionnables. Aucun commit ni push.
