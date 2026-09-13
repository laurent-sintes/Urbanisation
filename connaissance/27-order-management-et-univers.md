# Univers Supply / Case et Order Management

Application du Go U141, 13 septembre 2026. Autorité du modèle : [backlog JSON](../modeles/backlog/model.json). Cette note explique les changements ; elle ne remplace pas le JSON. C78 conserve la correction et CMP066 les correspondances.

## Portée de l’accord

Les univers Supply et Case sont explicites. Le premier accueille l’exploration transactionnelle courante ; le second réserve le modèle processus, encore à construire. Un univers regroupe ici une perspective cohérente d’urbanisation ; les domaines restent des espaces de problèmes métier. Business References demeure un groupe de présentation sous Supply, pas une capacité mère ni un univers concurrent.

Le Go porte sur le plan présenté et les quatre noms et descriptions courtes de capacités. Les finalités et périmètres ajoutés par Codex restent proposés. La création des identifiants, les liens détaillés et les répartitions internes n’étendent pas cet accord. Aucune publication.

## D04 — Order Management

Finalité du domaine, proposée : disposer d’une représentation cohérente des Orders à satisfaire, distincte des Cases, des conditions contractuelles reçues, des promesses et des prestations d’exécution.

| ID | Nom validé | Description courte validée |
| --- | --- | --- |
| D04.e | Order Registration | Reconnaître et enregistrer une commande Supply et son origine. |
| D04.f | Order Revision | Intégrer ses évolutions autorisées, avec leur historique. |
| D04.g | Order Visibility | Restituer son contenu applicable et sa situation. |
| D04.h | Order Reconciliation | Établir ce qui reste à satisfaire en rapprochant commande, modifications et réalisations. |

Ces aptitudes couvrent commandes d’achat, vente, transfert et retour, sans spécialisation B2B/B2C de domaine. Recevoir et reconnaître un Order n’est pas négocier la commande commerciale. Réviser son état selon une modification autorisée n’accorde pas le droit commercial de décider cette modification. Aucun endpoint, workflow ou moteur n’est une capacité supplémentaire par défaut.

Les anciens D04.a–d avaient des responsabilités différentes ou plus larges : ils sont conservés avec leurs relations dans [l’état antérieur complet](../modeles/backlog/history/pre-U141.json). D04.e/f/h reprennent les sujets de création/révision/rapprochement avec un résultat recentré ; D04.g rend la visibilité explicite. D04.d Return and Replacement Decision est retirée du domaine actif : son besoin de décision commerciale reste à instruire dans Case ; les Orders de retour sont couverts par les quatre capacités communes. Aucun lien de remplacement exact n’est affirmé entre D04.d et Order Visibility.

## Frontière avec D07

| D04 | D07 |
| --- | --- |
| Quelle commande est actuellement autorisée et applicable ? | Quelles prestations sont nécessaires pour la réaliser ? |
| Quelles modifications autorisées doivent être intégrées ? | Quels engagements de prise en charge changent en conséquence ? |
| Que reste-t-il à satisfaire sur la commande ? | Quels faits et écarts sont imputables aux prestations attendues ? |

D07.a exprime le besoin de prestation ; D07.b suit la prise en charge des exécutants ; D07.c rapproche leurs faits des prestations attendues ; D07.d qualifie les ressources futures attendues. Le domaine ne recrée pas une commande commerciale ni un contrat de référence. La logistique reste en adhérence, hors développement FLOW. Les définitions précisées de D07 sont des reformulations proposées, sans nouvelle validation individuelle.

Le lien caractérisé D07.c vers D04.h exprime que les faits et écarts rapprochés alimentent le calcul du reliquat de commande. Il ne prescrit ni appel synchrone, ni copie de tous les états, ni double autorité. Hypothèse illustrative : Order de 100, prestation de 60 acceptée, 40 réalisées. Le reliquat Order peut être 60, tandis que la prestation acceptée a encore 20 à réaliser ; les 40 non pris en charge ne disparaissent pas. Annulations, tolérances et imputations peuvent modifier ce calcul ; aucune formule universelle adoptée.

## Agreement et référentiels

Agreement reçoit le contrat complet : cadre, conditions particulières, périodes, engagements en quantité ou valeur et liens Party/Catalog. Cela ne suppose pas trois contrats ou trois objets distincts. Les ingestions maintiennent les projections externes ; les consommateurs consultent ces données. La visibilité reste autorisée selon U134, sans ajouter automatiquement les cinq capacités Visibility suggérées lors de l’audit initial, qui n’étaient pas dans la liste soumise au Go U141.

La consommation d’un Agreement, le reliquat d’un Order et le reliquat d’une prestation sont distincts. L’autorité sur les compteurs contractuels reste ouverte Q072. D04 ne modifie pas le contrat maître.

## Objets et variantes à approfondir

La feuille de route JSON prévoit explicitement le rattachement caractérisé Case/Order : noms et perspectives acquis, cardinalités et relation détaillée différées. Aucun objet Case ou Order supplémentaire n’est instancié à ce stade ; les illustrations existantes restent des illustrations et ne deviennent pas un inventaire validé.

Q077 suit les points encore ouverts : annulation, suspension, fractionnement, liens entre Orders, transitions autorisées, grain de rapprochement avec D07, unités et conditionnements, échéanciers, volumes et limites des réalisations. DMN concerne les décisions et complète les workflows ; il ne remplace pas les invariants ou le modèle métier. Les différences B2B/B2C se décrivent par les contraintes et résultats requis, sans présumer leur couverture complète par quatre capacités.

## Traçabilité et contrôles

U141, C78, CMP066 ; principes antérieurs U134/U140 conservés. Aucun changement du panorama As Is et aucune extension de périmètre logistique. Les états de release sont immuables. Le versionnement des éléments sera recalculé par le workflow de publication ; les portées lifecycle conservent les valeurs expressément approuvées.
