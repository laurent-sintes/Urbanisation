---
name: release
description: Évaluer les évolutions du backlog du modèle Beaumanoir / FLOW, préparer puis publier une nouvelle release locale avec ses statuts et preuves. Utiliser pour une demande de release du modèle ou de comparaison backlog/release ; ne concerne pas les releases logicielles, Git ou un déploiement distant.
---

# Release du modèle Beaumanoir / FLOW

Explorer et construire se fait dans le **backlog**. Ce skill organise le passage vers une publication locale distincte. Une demande de release autorise l’évaluation, la préparation et la publication ; ne pas ajouter une confirmation systématique. Une demande limitée à comparer, auditer ou préparer ne modifie pas la release. Si aucun changement publiable ne subsiste, donner le bilan et conserver la version existante, sauf demande de republication explicite.

Situer le projet courant par `AGENTS.md`, `modeles/backlog/model.json` et `scripts/prepare_release.py` ; à défaut, utiliser `C:/Dev/Beaumanoir Cartographie`. Les chemins ci-dessous sont relatifs à cette racine, et non au dossier personnel du skill. Lire les règles de `AGENTS.md`, `modeles/README.md` et les corrections pertinentes de `connaissance/04-corrections.md`.

## Évaluer les évolutions

Enregistrer d’abord les nouveaux apports utilisateur selon les règles du projet. Si nécessaire, actualiser uniquement l’index courant des sources :

```powershell
python scripts/refresh_sources.py
```

Employer le Python du projet ou le runtime Python disponible, sans imposer une installation globale. Comparer le **backlog vivant** à la release désignée par `modeles/release/current.json` :

```powershell
python scripts/prepare_release.py report
```

Cette commande est en lecture seule. Examiner les ajouts, retraits, champs avant/après, rattachements, qualifications de relations, changements de statut, décisions conservées ou suspendues et erreurs d’intégrité. La version suggérée est une disponibilité technique, pas une validation. Ne pas compter comme nouvel apport le simple changement d’enveloppe backlog/release.

Compléter le rapport automatique par une lecture métier ciblée : cohérence avec les arbitrages, définitions de capacités, conséquences sur les domaines, objets et relations, provenance et limites des correspondances marché. Distinguer une proposition cohérente non validée d’une erreur structurelle. Les capacités non validées restent publiables avec leur statut, conformément à U111.

Les alternatives, illustrations et fichiers annexes du backlog sont recensés et figés comme contexte ; ils ne deviennent pas silencieusement des éléments de release. La feuille de route et l’applicabilité ne constituent pas des résultats de couverture. Le panorama As Is ne fait pas partie de cette publication du modèle commun. Si la demande exige l’intégration d’un de ces éléments différés, traiter explicitement son périmètre et son contrat avant de le publier.

## Préparer un contenu contrôlable

Corriger les incohérences établies dans le backlog, avec sources et révisions adaptées, puis refaire le rapport. Après suspension d’une validation, vérifier aussi les notes narratives : un ancien commentaire « validé » doit être présenté comme historique et ne pas qualifier la nouvelle révision. Ne pas inventer de décision métier pour faire réussir un contrôle.

Une validation antérieure est conservée automatiquement uniquement pour une même identité, une même révision et des valeurs approuvées inchangées. Un changement de révision ou de valeur suspend la reprise automatique ; l’accord historique reste conservé. Le rapport rend cette suspension visible. Une nouvelle validation exige une décision sourcée conforme au schéma, avec un nouvel identifiant, la version préparée et la portée réellement adoptée. Une décision sur un nom n’adopte pas la définition ni le rattachement. Les contenus qui restent proposés peuvent néanmoins être publiés.

Choisir une version neuve `YYYY-MM-DD.N`, en utilisant la disponibilité indiquée par le rapport. Remplacer `VERSION` et `SOURCE` ci-dessous par les valeurs réelles ; `SOURCE` désigne la contribution autorisant cette publication, pas simplement la demande de création du skill :

```powershell
python scripts/prepare_release.py prepare --version VERSION --source SOURCE
```

Répéter `--source` si nécessaire. Ajouter `--decisions chemin.json` seulement pour des décisions nouvelles réellement sourcées ; ne pas recopier tout l’ancien catalogue. Les décisions antérieures compatibles sont reprises automatiquement.

La préparation écrit uniquement `modeles/staging/<version>/` : `report.json`, `candidate.json`, manifeste, backlog, décisions et preuves figés. Examiner les différences et les éventuelles validations suspendues avant publication, puis présenter un bilan concis à Laurent en poursuivant l’opération déjà demandée. Une erreur d’intégrité empêche de publier ; un statut non validé n’est pas une erreur.

## Publier la version préparée

Si la demande couvre la publication, exécuter :

```powershell
python scripts/prepare_release.py publish --version VERSION --activate
python scripts/validate_models.py
python scripts/render_models.py
python app/server.py --check
```

Le workflow vérifie les empreintes, le contrat, la release de départ et l’absence de changement du backlog depuis la préparation. Il copie les entrées figées vers l’historique permanent et actualise `current.json` en dernier. Il refuse une version existante ; ne pas modifier une release gelée ni contourner un refus en réécrivant ses empreintes. Si le backlog ou la release de départ a changé, réévaluer et préparer une nouvelle version. En cas d’interruption, examiner les artefacts réellement écrits et le pointeur avant toute reprise ; ne pas répéter aveuglément une publication.

Le script historique `publish_release.py --from-manifest` sert à republier un ancien instantané ; il ne remplace pas ce workflow pour intégrer le backlog courant.

Actualiser le journal et les liens documentaires devenus obsolètes ; signaler la version publiée, les évolutions utiles, les validations conservées ou à reprendre et ce qui reste dans le backlog. Le backlog reste l’espace de travail par défaut après publication. Une nouvelle donnée JSON demande une actualisation de FLOW Atlas, sans redémarrage du serveur tant que son code Python n’a pas changé.
