# U463 — définition métier de Supply Chain Orchestration

La définition héritée « Univers du pilotage transactionnel de la Supply ; priorité de l’exploration courante » est remplacée dans le backlog par :

> Coordonner la satisfaction des demandes Supply : gérer les commandes et les stocks, établir les engagements de quantités et de dates, optimiser l’usage des ressources et piloter la réalisation avec les services exécutants.

Elle explique les responsabilités des six domaines existants. Le nom adopté reste **Supply Chain Orchestration** (`universe-supply`, révision 4). Les référentiels fournissent les informations utiles ; cette correction ne leur attribue pas l’administration de maîtres externes.

## Modifications

- Définition de l’univers recentrée sur le métier ; la priorité d’exploration, qui décrit le travail de modélisation, en est retirée.
- Deux comparaisons dans la fiche : appui méthodologique TOGAF et recouvrement partiel Microsoft, avec raisons de définition/vocabulaire, sources et limites.
- Exemple de coopération Commerce → Supply → logistique repris de U455. Il illustre les interactions, sans créer de domaines ni supposer un parcours universel.
- TER034, sens fonctionnel local d’OMS, ne le place plus au-dessus de la Supply ; TER035, sens fonctionnel local de Supply, ne la définit plus comme une couche. Renvois vers l’univers et distinction avec Supply au sens ressources conservés.
- Contribution U463 enregistrée, correction C108 et rapprochement CMP182 documentés. Instructions, conventions et suivi du plan alignés.

## Pourquoi cette rédaction

[TOGAF G189, Business Capabilities](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf), §2 et §2.1.2, étaye la distinction entre aptitudes métier et moyens de réalisation. Ce document primaire de 2018 a été consulté sur un miroir tiers ; il ne définit pas l’univers Supply de FLOW. Le portail officiel 9.2 demande une authentification : aucune vérification de la 10e édition n’est prétendue.

[Microsoft Intelligent Order Management](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview) illustre la coopération autour de l’orchestration des commandes, de la visibilité des stocks et de l’optimisation. Le rapprochement reste partiel : une documentation produit ne fixe pas les frontières de nos domaines.

Le retrait de la qualification transactionnelle découle de U455/U463. La nouvelle formulation est éditoriale, à périmètre constant ; l’accord sur le nom n’est pas étendu à cette rédaction. Cette correction ne prétend pas que SAP a inventé la notion de transaction, ni qu’un autre produit constitue une meilleure taxonomie universelle.

## Vérifications et publication

- Validation du modèle : **0 erreur** ; **11 tests ciblés réussis** sur les comparaisons, exemples, glossaire et compatibilité des publications historiques.
- Restitution backlog régénérée.
- Un seul nœud et deux termes modifiés ; **142 nœuds et 346 relations conservés**, noms et validations antérieures identiques.
- **303 fichiers de publication et de preuve inchangés**. [Résultat détaillé](verification.json), [manifest des empreintes](protected-files.json), captures avant modification dans `before/`.
- Atlas reste sur **v010**. La définition corrigée et ses compléments seront visibles après une nouvelle release ; aucune publication ou opération serveur n’a été lancée.

La correction vise les définitions de périmètre et la hiérarchie résiduelle OMS/Supply. Les verbatims historiques et le vocabulaire technique des sources restent conservés ; les distinctions entre décision, mise à jour des informations et réalisation physique demeurent utiles.
