# Glossaire et infobulles dans Atlas — U203

Demande du 14 septembre 2026 : disposer d’une page Glossaire, lire la description courte d’une cible au survol du lien, puis ouvrir sa page ou son ancre au clic.

## Résultat

L’entrée **Glossaire** est séparée de l’arbre métier. Elle propose recherche par nom, description ou définition, liste de notions et fiche détaillée. Les descriptions courtes apparaissent au survol et au focus clavier. L’infobulle reste accessible sous le pointeur ; Échap la ferme. Le clic et Entrée ouvrent la fiche, avec sa publication et sa section dans l’URL. Les liens existants de rattachement, d’exploration et d’extrémité de relation utilisent ce même aperçu. Sans description courte dédiée pour un élément, sa finalité puis sa définition servent d’aperçu.

Les textes reconnaissent seulement les liens explicites `[libellé](glossary:TER059)` et `[libellé](model:D01.f#definition)`. Le texte affiché reste libre. Aucun HTML n’est exécuté ; aucune liaison par simple égalité de mots, aucun nouveau rattachement métier. Une cible absente est signalée dans l’interface et bloque la validation du modèle à publier. Les liens connus peuvent être ouverts dans un nouvel onglet ; leur URL conserve la version.

## Catalogue et publication

Le catalogue de travail est `modeles/backlog/glossary.yaml` : **93 termes**, dont 81 repères TER/VER issus des tableaux historiques et douze repères TER057–TER068 pour les notions discutées récemment. Le registre Markdown reste la provenance narrative ; les modifications courantes se font dans le YAML. TER004 conserve son ancien sens d’Article ; le rôle Article possède TER060. ATP, CTP, Agreement et Product Reference reprennent les précisions récentes, avec leur ancienne définition conservée. Les descriptions courtes dérivées et formulations consolidées ne constituent pas une validation supplémentaire ; les portées des accords restent dans les sources.

Une préparation incorpore le glossaire au snapshot. Les termes, le catalogue et le modèle global sont versionnés automatiquement ; le modèle publié contient le catalogue figé. La publication refuse une modification de ce fichier depuis la préparation. Le rapport et la note de release décrivent les changements ; les références directes ou indirectes à une définition modifiée sont signalées pour examen sémantique. Le contrôle ne valide pas automatiquement le nouveau sens d’une capacité dont le texte est inchangé.

**La publication réelle reste v003 / 2026-09-13.5, sans glossaire structuré.** Sa page indique cet état ; le backlog n’est jamais injecté dans cette publication. Aucune nouvelle release métier, aucun commit ni push n’a été effectué. L’ajout systématique de liens dans les formulations du modèle sera réalisé lors de leur instruction ; aucun remplacement global du vocabulaire n’a été appliqué ici. Les points de reprise des validations déjà signalés par l’audit U202 restent à traiter avant une prochaine publication métier.

## Vérifications

- Modèle : validation du projet sans erreur ; tests Python des modèles, plus intégrité des cibles, versionnement du glossaire, impacts lexicaux, gel des entrées et publication dans un projet isolé.
- Application : compilation TypeScript/Vite ; 33 tests JavaScript ; 22 tests Python HTTP/données dont deux ignorés pour contraintes de plateforme.
- Navigateur : parcours existants, hiérarchie, sources, historiques fixes et rafraîchissement automatique ; puis tests spécifiques glossaire sur ordinateur et mobile, ancres après rechargement, survol/focus/Échap/Entrée, recherche et absence de débordement. Aucun incident JavaScript observé.
- Les versions publiées, révisions figées et décisions historiques ne sont pas modifiées. Le serveur local est relancé et `/api/model` vérifié sur v003.

`browser-checks.json` distingue les tests sur la publication réelle des données injectées uniquement dans le navigateur de test. `publication-v003.png` montre l’état réel. `fixture-desktop.png` et `fixture-mobile.png` montrent un exemple technique avec deux termes **non publiés** ; ils ne constituent pas une vue métier de v003.
