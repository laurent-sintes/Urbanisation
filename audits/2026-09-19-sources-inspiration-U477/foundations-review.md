# Revue indépendante Foundations — U477

Les 13 termes ont été relus face à `foundations-input.yaml`. Avis favorable après les corrections ci-dessous. Aucun nom, définition, responsabilité ou accord n’a été modifié.

- Les 13 synthèses ont été converties de chaînes en listes de deux paragraphes, comme l’exige le contrat `market_inspiration`.
- TER023 : la protection du stock par une règle DOM est désormais conditionnée au maintien de cette règle. Le caractère impératif ou relâchable reste explicite. « Juridiction » a été remplacé par une formulation plus simple sur la portée des règles.
- TER039 : le résumé CloudEvents porte sur le fait capté et son contexte, sans faire des destinataires un élément du format ni confondre représentation technique et sens métier.

Les distinctions capacité/processus/opération/fonction restent cohérentes. Les rapprochements DDD ne fixent aucune frontière logicielle FLOW. Pour TER036/TER037, le lien obligatoire fait–document est correctement présenté comme choix FLOW ; les sources illustrent ce lien sans établir son universalité. Le document structuré, le fait reconnu et la notification restent distincts. Aucune immutabilité générale n’est déduite des exemples.

Vérifications documentaires ciblées refaites le 19 septembre 2026 : [GEA-NZ, principe « What and why »](https://dns.govt.nz/standards-and-guidance/technology-and-architecture/government-enterprise-architecture/gea-nz-framework/business-capabilities), [Fowler, Domain Model](https://martinfowler.com/eaaCatalog/domainModel.html), [Fowler, Bounded Context](https://martinfowler.com/bliki/BoundedContext.html), [réception Microsoft, cinq commandées et quatre reçues](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order), [règles DOM](https://learn.microsoft.com/en-us/dynamics365/commerce/dom-rules), [CloudEvents 1.0.2, Terminology](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md). Les autres appuis restent ceux du relevé de consultation initial ; cette revue n’en constitue pas une seconde consultation exhaustive.

Contrôles ciblés réussis : mêmes 13 identifiants, 26 comparaisons, deux documents distincts par terme, 13 exemples complets, contrats des comparaisons et de l’inspiration sans erreur.

Le fichier corrigé est `foundations-output.yaml`. Ne pas le régénérer avec le builder antérieur sans reporter ces corrections.
