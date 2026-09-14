# Atlas Exploration — essai React Flow / LikeC4

Prototype local issu de l’[étude U143](../../marche/etudes/2026-09-14-exploration-atlas/etude.md), destiné à comparer deux moteurs sur le même parcours métier : arbre gauche, fiche centrale, carte et relations. **Laurent a validé React Flow avec interface sur mesure en [U150](../../connaissance/01-contributions-utilisateur.md#u150)** ; la comparaison est conservée comme historique. Cette application est séparée de FLOW Atlas et ne modifie aucun modèle publié.

Réalisation autorisée par **U146**. Voir le [bilan de l’essai et les captures](bilan.md) : 15 tests de données et 12 familles de contrôles navigateur réussis.

**Parcours à essayer :** Supply → Order Management → Order Reconciliation, puis Relations → Execution Reconciliation. Passer de React Flow à LikeC4 conserve la sélection. La recherche se concentre sur les textes et identifiants publiés. Les statuts et leurs portées restent visibles ; les agrégats graphiques LikeC4 sont signalés comme résumés des relations sources.

## Construire et lancer

Prérequis : Node.js 24 ou supérieur, pnpm et le Python utilisé par le lanceur FLOW Atlas. Les versions npm sont fixées dans `package.json` et `pnpm-lock.yaml`. Depuis ce dossier :

```powershell
pnpm install --frozen-lockfile
node scripts/generate-likec4.mjs
pnpm run build
.\Lancer-Atlas-Exploration.ps1
```

Le prototype se consulte sur [http://127.0.0.1:8767/](http://127.0.0.1:8767/). Le lanceur démarre la prévisualisation locale des fichiers construits dans `dist/`, en arrière-plan et sans fenêtre de navigateur. `-Browser` ouvre explicitement le navigateur ; `-NoBrowser` permet aussi d’exprimer ce choix dans un script. Le lanceur ne télécharge ni ne construit automatiquement les dépendances.

Les requêtes `/api` sont transmises à FLOW Atlas sur **127.0.0.1:8765**. Si nécessaire, le lanceur réutilise `../../Lancer-FLOW-Atlas.ps1 -Port 8765 -NoBrowser` pour démarrer cette API après contrôle d’identité. Le prototype vérifie également son identité propre via `/__atlas_experiment` : nom d’application, racine du dépôt et PID.

Un nouveau lancement réutilise le prototype déjà identifié. Pour arrêter uniquement son processus suivi :

```powershell
.\Lancer-Atlas-Exploration.ps1 -Stop
```

L’arrêt exige une correspondance entre l’identité HTTP, le dépôt, le PID et sa date de démarrage. Un ancien PID ou un service non identifié n’est pas arrêté. L’API FLOW Atlas reste disponible. Le suivi et les journaux sont dans `.runtime/preview-8767.*`. Fermer le navigateur laisse les serveurs fonctionner. Après modification de Vite ou reconstruction, arrêter puis relancer le prototype.

Pour développer au premier plan, démarrer l’API Atlas puis utiliser `pnpm run dev` ; `Ctrl+C` termine ce serveur. La prévisualisation Vite est destinée à cet essai local, sans déploiement Internet.

## Une publication commune aux deux moteurs

`scripts/load-publication.mjs` lit l’index officiel → le descripteur désigné → le modèle publié et vérifie leurs empreintes. Aucune sélection par tri des fichiers, aucun complément depuis le backlog. `src/model.ts` conserve les identifiants, sources, qualifications complètes des relations et portées de validation.

La génération LikeC4 produit une projection dérivée dans `.generated/`, avec une correspondance bijective des identifiants et un manifeste indiquant la publication. Les deux moteurs demandent ensuite **cette même publication** à `/api/model?version=…`. L’essai reste donc fixe pour permettre une comparaison ; il ne suit pas automatiquement la publication courante comme Atlas.

Pour comparer une autre publication existante, régénérer puis reconstruire :

```powershell
node scripts/generate-likec4.mjs --version=2026-09-13.5
pnpm run build
```

Sans `--version`, le générateur suit le pointeur courant de l’index. Ne pas éditer `.generated/` à la main. `contains` et `presents` restent distincts ; Business References reste un groupe de présentation. Les voisins métier ne sont jamais transformés en enfants par déduction. Les types objet, document et événement sont supportés par la projection, sans inventer d’instances dans la publication.

## Vérifier

```powershell
node --test --test-isolation=none scripts/test*.mjs
pnpm run build
node scripts/verify-browser.mjs
```

Les tests couvrent notamment les données réelles de v003, une version historique, les parents explicites, les qualifications, la recherche et une fixture synthétique de profondeur supplémentaire. Cette fixture reste limitée aux tests. La revue dans le navigateur complète ces contrôles pour le placement, la lisibilité et la navigation au clavier.

`src/types.ts` et `src/model.ts` constituent le contrat commun ; les moteurs graphiques ont leurs propres composants. Les dépendances, les projections générées, les fichiers construits et les journaux sont exclus de Git. Seules les sources du prototype et le fichier de verrouillage sont destinés au suivi de version.
