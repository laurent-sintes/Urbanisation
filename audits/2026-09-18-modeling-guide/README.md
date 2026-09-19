# Les clés du modèle — contrôle de l’intégration Atlas

L’intégration autorisée par U321 comprend six principes, une lecture immédiate et une profondeur « Pour contribuer ». U322 précise l’indépendance du modèle business et de l’architecture de solution. Les capacités restent identiques pendant le changement de réalisation technique : brique dédiée, mutualisation ou services distribués.

La [comparaison avec les références primaires](business-solution.md) documente les points communs, les différences de portée et les limites de preuve. Les exemples du guide sont pédagogiques ; ils ne décrivent pas un déploiement installé.

## Vérification navigateur

Commande : `node app/verify-modeling-guide.mjs` ou `pnpm --dir app verify:principles` après compilation de l’application.

Le test utilise Microsoft Edge en mode headless et des routes interceptées sur `http://atlas.test`. Le modèle provient du lecteur de publication et le guide de son chargeur Python réel. Aucun serveur n’est démarré ; aucune publication métier ni donnée du serveur local n’est modifiée. Une référence inexistante est injectée uniquement dans une réponse du navigateur pour vérifier son filtrage.

Les contrôles couvrent :

- l’ouverture depuis une fiche, les six clés et les liens directs ;
- trois réalisations techniques pour le même modèle business ;
- chaque choix, son explication et l’accès direct à l’explication ;
- les critères, frontières, portées et extraits de sources figés ;
- les liens résolus dans la publication affichée et les références absentes ;
- le retour navigateur, l’usage au clavier et les écrans 390 px et 320 px ;
- l’indisponibilité explicite pour une publication historique sans association ;
- une réponse lente pendant un changement de publication, sans mélange des versions ;
- l’absence d’erreur JavaScript et de requête vers le backlog ou les sources vivantes.

Résultat détaillé et reproductible : [browser/checks.json](browser/checks.json). La publication contrôlée et la version du guide y sont enregistrées.

Captures : [bureau, modèle business et solution](browser/desktop-business-solution.png), [mobile 390 px](browser/mobile-390.png), [mobile 320 px](browser/mobile-320.png), [réalisations en 320 px](browser/mobile-320-business-solution.png), [publication historique](browser/historical-unavailable.png).

Les contrôles navigateur n’attestent pas un redémarrage ou une mise à jour du serveur local. Ils vérifient le build compilé et les réponses de lecture réelles dans un environnement de test isolé.

## Vérification finale du 18 septembre 2026

- Tests frontend : 40 réussis ; compilation TypeScript/Vite réussie.
- Chargeur et API du guide : 15 tests réussis et 1 ignoré, la création de liens symboliques nécessitant un privilège Windows indisponible. La protection contre une redirection de chemin est aussi contrôlée par simulation.
- Validation des modèles : aucune erreur ; provenance et restitutions dérivées actualisées.
- Non-régression de lecture des publications : 19 tests réussis et 2 ignorés lors du premier passage. Le dernier test a révélé une incohérence de fixture entre un modèle historique et le glossaire courant ; le glossaire de la fixture a été aligné sur le même état historique, puis ce test a réussi lors d’un passage ciblé. Cette correction concerne uniquement le répertoire temporaire du test.
- Navigateur : les 10 groupes de contrôles ont réussi, sans erreur JavaScript, après la compilation finale et la correction du retour à la ligne des numéros sur mobile.
- Les empreintes des 139 fichiers protégés contrôlés sont inchangées ; aucun nouveau fichier de publication, révision ou preuve figée n’a été ajouté.
- `git diff --check` est passé sur les fichiers de l’intégration et `python app/server.py --check` confirme la disponibilité du build et de la publication courante.

Le serveur local était arrêté et n’a pas été démarré. Aucun commit, push ou nouvelle release métier n’a été effectué.
