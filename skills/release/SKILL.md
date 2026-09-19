---
name: release
description: Évaluer le backlog Beaumanoir / FLOW, produire la release et la publier dans FLOW Atlas sous Urbanisation, avec actualisation des données. Utiliser pour une release du modèle ou une comparaison backlog/release ; ni release logicielle, ni push Git, ni déploiement distant.
---

# Release du modèle Beaumanoir / FLOW

Explorer et construire se fait dans le **backlog**. Une invocation de `$release`, même sans autre précision, autorise l’évaluation, la production de la release et sa publication locale dans **FLOW Atlas / Urbanisation**, avec actualisation des données selon U119. Ne pas ajouter une confirmation systématique. Une demande expressément limitée à comparer, auditer ou préparer ne modifie pas la release. Si aucun changement publiable ne subsiste, conserver la version existante sauf demande de republication explicite, puis vérifier sa disponibilité dans Atlas.

Situer le projet courant par `AGENTS.md`, `modeles/backlog/model.yaml` et `scripts/prepare_release.py` ; à défaut, utiliser `C:/Dev/Beaumanoir Cartographie`. Les chemins ci-dessous sont relatifs à cette racine, et non au dossier personnel du skill. Lire les règles de `AGENTS.md`, `modeles/README.md` et les corrections pertinentes de `connaissance/04-corrections.md`.

## Évaluer les évolutions

Enregistrer d’abord les nouveaux apports utilisateur selon les règles du projet. Si nécessaire, actualiser uniquement l’index courant des sources :

```powershell
python scripts/refresh_sources.py
```

Employer le Python du projet ou le runtime Python disponible, sans imposer une installation globale. Le lecteur nécessite PyYAML, épinglé dans `requirements.txt` ; installer au besoin avec `python -m pip install --target .tools/yaml-runtime -r requirements.txt`. Comparer le **backlog vivant** à la release désignée par `modeles/release/index.json` et son descripteur versionné :

```powershell
python scripts/prepare_release.py report
```

Cette commande est en lecture seule. Examiner les ajouts, retraits, champs avant/après, rattachements, qualifications de relations, changements de statut, décisions conservées ou suspendues et erreurs d’intégrité. La version suggérée est une disponibilité technique, pas une validation. Ne pas compter comme nouvel apport le simple changement d’enveloppe backlog/release.

Compléter le rapport automatique par une lecture métier ciblée : cohérence avec les arbitrages, définitions de capacités, conséquences sur les domaines, objets et relations, provenance et limites des correspondances marché. Distinguer une proposition cohérente non validée d’une erreur structurelle. Les capacités non validées restent publiables avec leur statut, conformément à U111.

Les alternatives, illustrations et fichiers annexes du backlog sont recensés et figés comme contexte ; ils ne deviennent pas silencieusement des éléments de release. La feuille de route et l’applicabilité ne constituent pas des résultats de couverture. Le panorama As Is ne fait pas partie de cette publication du modèle commun. Si la demande exige l’intégration d’un de ces éléments différés, traiter explicitement son périmètre et son contrat avant de le publier.

## Versions et métadonnées — U120 à U123

Le candidat calcule automatiquement les révisions entières et `last_modified` pour le modèle global, les nœuds, les relations et les principes : nouvel élément = 1, modifié = précédent + 1, inchangé = mêmes valeurs. Les révisions saisies dans le backlog ne pilotent pas le compteur. Le contenu comprend aussi les informations de provenance et de statut saisies. Une empreinte interne évite les incréments artificiels dus aux annotations calculées de publication. La première date enregistrée ne reconstitue pas un historique inconnu.

Chaque publication produit une courte `release-notes.md` et un descripteur immuable **`urbanisation-v<NNN>-<YYYY>-<MM>-<DD>-<HHMMSS>.yaml`**, selon U123 : au moins trois chiffres pour la version entière du modèle, heure UTC. Le descripteur porte `revision`, `version` (identifiant technique de publication), `published_at`, `last_modified`, les chemins et empreintes du modèle et de la note. L’index technique désigne le descripteur courant et recense les publications sélectionnables dans Atlas. Les descripteurs et modèles JSON historiques restent inchangés ; le manifeste technique et l’index restent JSON. Les anciens modèles conservent leur absence d’horodatage précis, sans date inventée.

## Préparer un contenu contrôlable

Corriger les incohérences établies dans le backlog, avec leurs sources ; les révisions sont calculées automatiquement. Regrouper les corrections, puis passer à la préparation finale si aucun réexamen intermédiaire n’est nécessaire : elle fournit son rapport complet et sa synthèse sans appel préalable supplémentaire à `report`. Après suspension d’une validation, vérifier aussi les notes narratives : un ancien commentaire « validé » doit être présenté comme historique et ne pas qualifier la nouvelle révision. Ne pas inventer de décision métier pour faire réussir un contrôle.

Une validation antérieure est conservée automatiquement uniquement pour une même identité, une même révision et des valeurs approuvées inchangées. Un changement de révision ou de valeur suspend la reprise automatique ; l’accord historique reste conservé. Le rapport rend cette suspension visible. Une nouvelle validation exige une décision sourcée conforme au schéma, avec un nouvel identifiant, la version préparée et la portée réellement adoptée. Une décision sur un nom n’adopte pas la définition ni le rattachement. Les contenus qui restent proposés peuvent néanmoins être publiés.

Choisir une version neuve `YYYY-MM-DD.N`, en utilisant la disponibilité indiquée par le rapport. Remplacer `VERSION` et `SOURCE` ci-dessous par les valeurs réelles ; `SOURCE` désigne la contribution autorisant cette publication, pas simplement la demande de création du skill :

```powershell
python scripts/prepare_release.py prepare --version VERSION --source SOURCE
```

Répéter `--source` si nécessaire. Ajouter `--decisions chemin.json` seulement pour des décisions nouvelles réellement sourcées ; ne pas recopier tout l’ancien catalogue. Les décisions antérieures compatibles sont reprises automatiquement.

Si des accords sont suspendus, utiliser le dossier maintenu dès le diagnostic, sans script ponctuel :

```powershell
python scripts/prepare_release.py report --version VERSION --source SOURCE --review-output .runtime/review-VERSION
python scripts/prepare_release.py inspect .runtime/review-VERSION --section review --id IDENTIFIANT --full
```

Examiner les valeurs approuvées, leurs empreintes, les changements de fiche, de relations et du glossaire dans `review.json`, avec `inspect DOSSIER --section review-context` pour les changements globaux et `report.json` pour les autres éléments. Ces fichiers restent intacts. Compléter uniquement `assessment.yaml` : auteur du réexamen dans `reviewer`, puis `retain` ou `defer` et une justification de portée pour chaque entrée. Les choix commencent à `pending` ; l’éligibilité calculée ne vaut pas confirmation du sens. Ce réexamen peut être effectué par l’agent dans la portée déjà autorisée, comme pour les transcriptions antérieures ; une décision métier nouvelle ou complexe reste à arbitrer selon les instructions de Laurent. Aucun accord élargi par automatisation.

`prepare --version VERSION --source SOURCE --review .runtime/review-VERSION` construit le candidat final une seule fois et vérifie le dossier contre les entrées, le contrat, le code et la publication de départ. Une valeur approuvée modifiée ou retirée ne peut pas être transcrite. Les reprises conservent auteur, date, sources et champs de l’accord historique, sous de nouveaux identifiants ; les preuves sont figées avec la préparation puis archivées lors de la publication. Tout dossier périmé doit être régénéré après correction, sans retoucher ses empreintes.

Après préparation, lire `prepare_release.py inspect modeles/staging/VERSION` pour la synthèse et ajouter `--id IDENTIFIANT`, `--section errors`, `--section decisions` ou `--section context` pour les détails paginés. Ces lectures ne reconstruisent pas le candidat. Pour les preuves de réexamen préparées : `inspect modeles/staging/VERSION/decision-review --section review`. Ne pas relancer `report` uniquement pour relire les résultats déjà figés.

La préparation écrit uniquement `modeles/staging/<version>/` : `report.json`, `candidate.yaml`, manifeste, backlog, décisions et preuves figés. Examiner les différences et les éventuelles validations suspendues avant publication, puis présenter un bilan concis à Laurent en poursuivant l’opération déjà demandée. Une erreur d’intégrité empêche de publier ; un statut non validé n’est pas une erreur.

## Publier la version préparée

Le glossaire courant `modeles/backlog/glossary.yaml` est une entrée publiée : le workflow l’intègre au snapshot, le fige et versionne ses termes. Examiner `glossary_changes` et `glossary_reference_impacts` : une définition modifiée peut affecter le sens d’un champ lié pourtant inchangé. Ces alertes demandent un examen de portée, sans créer une validation. Toute modification du glossaire après préparation exige de préparer à nouveau ; aucune ancienne release ne reçoit le glossaire vivant. Vérifier aussi la page Glossaire d’Atlas après publication lorsqu’il contient des termes.

Si la demande couvre la publication, exécuter :

```powershell
python scripts/prepare_release.py publish --version VERSION --activate
python scripts/validate_models.py
python scripts/render_models.py
python app/server.py --check
```

Le workflow vérifie les empreintes, le contrat, la release de départ et l’absence de changement du backlog depuis la préparation. Il copie les entrées figées vers l’historique permanent et active `index.json` en dernier. Il refuse une version existante ; ne pas modifier une release gelée ni contourner un refus en réécrivant ses empreintes. Si le backlog ou la release de départ a changé, réévaluer et préparer une nouvelle version. En cas d’interruption, examiner les artefacts réellement écrits et le pointeur avant toute reprise ; ne pas répéter aveuglément une publication.

Le script historique `publish_release.py --from-manifest` sert à republier un ancien instantané ; il ne remplace pas ce workflow pour intégrer le backlog courant.

## Rendre la publication disponible dans Atlas

Atlas n’a pas de copie de référence : son serveur lit directement `modeles/release/index.json` et son descripteur versionné et le YAML versionné désigné (ou JSON pour les publications historiques). L’interface affiche uniquement des releases, sous le nom **Urbanisation** ; par défaut la dernière, ou une version historique choisie dans la liste décroissante. Ne pas copier le modèle vers `app/` ni exposer le backlog pour simuler une publication.

Après activation, utiliser le port suivi du projet (8765 par défaut). Lire `/api/status` avec un délai borné et vérifier `appName`, `repositoryRoot` et l’espace `release`, puis lire `/api/model` et `/api/releases`. Contrôler que `version`, `sourcePath` et les nœuds/relations servis correspondent à la version activée. Une réussite de publication disque seule ne suffit pas à annoncer la disponibilité dans Atlas.

Si Atlas ne tourne pas, démarrer le serveur avec le skill `server-admin`, sans ouvrir de fenêtre sauf demande. S’il tourne, l’interface vérifie la révision toutes les cinq secondes lorsqu’elle est visible, ainsi qu’à son retour au premier plan, et recharge automatiquement les données en conservant la navigation lorsque l’élément existe encore. Une ancienne version sélectionnée reste fixe ; la publication n’impose pas de quitter cette consultation. Pour un changement de données YAML/JSON seul, le redémarrage n’est pas nécessaire. Si le serveur exécute un ancien code Python ou sert un état incohérent, suivre `server-admin` pour l’arrêter puis le relancer au même port et vérifier l’API à nouveau. Si le code de l’interface a aussi changé, recharger la page ouverte pour installer ce code ; le redémarrage du serveur seul ne recharge pas le JavaScript déjà ouvert.

En cas d’échec serveur, préserver la release publiée et indiquer séparément « release produite » et « Atlas indisponible », avec la cause constatée. Ne pas republier une nouvelle version pour contourner une panne serveur et ne pas interrompre un autre service occupant le port.

Actualiser le journal et les liens documentaires devenus obsolètes ; signaler la version, les changements, les validations conservées ou à reprendre et l’état vérifié d’Atlas. Le backlog reste l’espace de travail du projet hors de l’interface. Ce cycle n’inclut aucun commit ou push Git.
