# Release U502 — Urbanisation v017

Publication **2026-09-19.10**, activée le 19 septembre 2026 à 16:45:21 UTC. [Descripteur](../../modeles/release/urbanisation-v017-2026-09-19-164521.yaml) ; [note figée](../../modeles/release/2026-09-19.10/release-notes.md).

## Contenu publié

- **Service Requests** remplace Order Management et explicite les demandes externes ou internes qui sollicitent le Domain.
- **Backing Service Orders**, **Backing Service** et **Service Catalog** distinguent demandes, prestations exécutantes et catalogue de l’offre mobilisable.
- **Order Backlog Optimization Request** et ses six comportements sont publiés sous Service Requests. Déclenchement et Activité sont deux angles de lecture au même niveau terminal.
- Origine **Backoffice** pour la demande d’optimisation ; **Frontoffice et Backoffice** pour Transfer Order. Aucun classement implicite des autres capacités.
- Trois coopérations avec Order Backlog Planning, Fulfillment Plan Decision et Supply Assignment ; sept rattachements explicites. Les sept nouvelles fiches disposent chacune de deux documents primaires et d’une illustration FLOW.
- Le rendu partagé **Périmètre** présente le résumé en encart coloré puis le détail directement visible. Le frontend U501 construit avant publication est servi par Atlas.
- Guide méthodologique **2026-09-19.4** associé à cette seule publication : Service Requests, origine des demandes et angles de lecture des comportements. Les associations historiques restent inchangées.

Le snapshot contient **144 objets, 48 capacités, 82 comportements, 348 relations et 110 termes métier**. Les illustrations de travail restent exclues de la publication. Le catalogue Information est conservé sans extension et reste masqué.

## Accords et intégrité

232 décisions conservées automatiquement. Les 13 décisions suspendues ont fait l’objet du [réexamen maintenu](../../modeles/revisions/2026-09-19.10/decision-review/assessment.yaml) : dix sont reprises sur leurs valeurs et leur sens inchangés. Trois décisions composites ne sont pas reprises intégralement : ancien nom D04, ancien ensemble nom/définition D07.b et ancien ensemble nom/définition D14.

Les [22 décisions complémentaires](new-decisions.json) comprennent vingt accords nouveaux explicitement fondés sur U496/U497/U501 et deux portées historiques réduites : le nom Service Catalog et la définition inchangée de D07.b. Ces deux portées conservent auteur, date et sources des accords historiques ; elles ne sont pas réattribuées à la demande de publication. Les champs modifiés exclus ne sont pas réadoptés implicitement.

Les 264 décisions actives ne valident pas globalement les fiches. Les cinq traductions anglaises nouvelles, développements, natures, exemples, qualifications détaillées et inspirations gardent leur portée éditoriale. Le glossaire conserve sa qualification propre ; le contrat ADOPT n’est pas étendu aux termes.

## Vérifications

Préparation, publication et validation finale : **zéro erreur**. Restitutions générées et contrôle serveur réussi. Les 46 tests Python, 14 tests frontend et build U501 restent applicables au code inchangé.

L’API Atlas sert exactement les champs du snapshot publié, ses relations et son glossaire, depuis `modeles/release/2026-09-19.10/model.yaml`. Les métadonnées d’origine, les six angles de comportements et les noms sont vérifiés. Le catalogue désigne v017, le guide courant .4 est disponible et v016 conserve son guide .3. Le HTML et les assets servis correspondent au build local.

**700 fichiers historiques** contrôlés par empreinte : aucun changement. Les index courants sont actualisés. [Preuve de vérification](verification.yaml) ; [candidat du guide et empreinte](guide-candidate-proof.yaml).

Serveur existant conservé, aucun redémarrage requis. Une page déjà ouverte doit être rechargée pour installer le nouveau code frontend. Aucun navigateur ouvert, commit ou push effectué.
