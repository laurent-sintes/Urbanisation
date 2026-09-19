# Modèle business et réalisations techniques — U322

Date de consultation : 18 septembre 2026. Cette note prépare la première clé pédagogique du guide Atlas. Elle ne modifie aucun découpage métier et ne documente aucun déploiement Beaumanoir.

## Principe et portée

L’apport de Laurent est enregistré dans [U322](../../connaissance/01-contributions-utilisateur.md#u322). Le modèle business décrit des responsabilités métier indépendamment de leur réalisation. Il ne prescrit ni une application par domaine, ni un composant par capacité, ni un microservice par comportement. Une brique dédiée est possible ; des solutions peuvent également mutualiser plusieurs responsabilités ou distribuer la réalisation d’une même capacité entre plusieurs services. Les choix et contraintes techniques ont leur propre justification.

Cette indépendance du modèle n’efface pas les correspondances avec les solutions : elles peuvent être documentées explicitement, sans devenir des relations de décomposition métier et sans cardinalité présumée.

## Comparaison avec les références primaires consultées

| Source | Passage et édition | Constat sourcé | Rapprochement et limite pour FLOW |
| --- | --- | --- | --- |
| Microsoft, [Design a microservice domain model](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/microservice-domain-model) | *Define one rich domain model for each business microservice or Bounded Context*, page mise à jour le 13 avril 2022 ; extrait du guide .NET Microservices | Un contexte délimité ou microservice métier peut être composé de plusieurs services physiques partageant le même modèle. | Confirme que frontière logique et service physique ne sont pas nécessairement en correspondance un pour un. Le modèle DDD décrit ici sert la conception logicielle ; ce n’est pas le catalogue des capacités FLOW. |
| Microsoft, [Data sovereignty per microservice](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice) | *The relationship between microservices and the Bounded Context pattern*, page mise à jour le 13 avril 2022 ; extrait du même guide | Un contexte délimité peut être une frontière logique au sein d’un monolithe. Le point de départ « un service par contexte » n’est pas une obligation ; plusieurs services physiques peuvent réaliser ce contexte. | Appuie la diversité des réalisations. La source porte sur DDD et l’architecture microservices, sans démontrer une règle universelle de correspondance avec les capacités métier. |
| Microsoft Azure Architecture Center, [Use domain analysis to model microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) | Introduction, *Analyze the domain*, *Define bounded contexts* ; page mise à jour le 25 février 2026 | L’analyse métier précède les choix techniques. Les frontières de services nécessitent un arbitrage tenant compte du métier, des exigences et des caractéristiques d’architecture. La source recommande cohésion fonctionnelle et faible couplage ; elle définit le contexte délimité comme le périmètre où s’applique un modèle particulier. | Cohérent avec une description métier indépendante des solutions. Cette approche propose de guider les services par les capacités ; elle ne justifie ni une bijection ni l’assimilation automatique des domaines FLOW aux contextes DDD. |

La page officielle The Open Group [Business Capabilities](https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html) a été recherchée, mais sa consultation a été redirigée vers l’authentification. Elle n’est donc pas utilisée comme preuve de contenu dans cette note ; aucun miroir ou résumé secondaire n’est substitué à sa consultation.

## Distinctions conservées

- **Domaine FLOW** : espace cohérent de problèmes métier.
- **Capacité FLOW** : ce que l’entreprise sait faire durablement, indépendamment de son organisation et de ses outils.
- **Contexte délimité DDD** : frontière d’application et de cohérence d’un modèle de conception ; aucune équivalence automatique avec un domaine ou une capacité FLOW.
- **Service physique / composant** : élément de réalisation logicielle, soumis à des choix de déploiement, d’exploitation et d’intégration.

Ces définitions n’imposent aucune cardinalité entre les quatre notions. La mutualisation et la généricité citées par Laurent ne sont pas assimilées aux « generic subdomains » du DDD : une proximité de vocabulaire ne prouve pas une équivalence.

## Application pédagogique proposée

Garder visuellement le même ensemble de responsabilités métier pendant que le lecteur choisit entre trois réalisations illustratives : **Brique dédiée**, **Mutualisation**, **Services distribués**. Le changement doit affecter seulement les blocs logiciels et leur explication. Aucun scénario n’est présenté comme supérieur, comme architecture cible adoptée ou comme situation installée.

Le bénéfice est de rendre l’indépendance immédiatement observable. Le compromis est une simplification assumée : quelques blocs illustrent des possibilités sans prétendre couvrir les architectures réelles. Les arbitrages de cohésion, couplage, autonomie, coûts et contraintes se discutent à partir d’un contexte de solution explicite, sans redessiner automatiquement les responsabilités métier.
