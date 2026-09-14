# Ressource, stock et mouvement

14 septembre 2026 — U175. Première question du point 5 : ce qui est stocké et ce qui est transporté doivent-ils être des objets différents ? Propositions en instruction, sans création d’objets actifs.

## Proposition

Le bien ne change pas de nature parce qu’il quitte un entrepôt. La position de stock représente ses quantités et qualifications ; l’expédition ou la livraison représente une opération, un regroupement ou un document à préciser selon le contexte. Ce sont des responsabilités différentes. Stocké et en transit ne forment pas nécessairement une alternative exclusive : la notion de stock en transit existe.

La continuité métier ne prescrit pas un objet logiciel unique partagé entre Supply et Services. Les vues doivent pouvoir être rapprochées ; une identité par pièce n’est pas exigée pour des biens fongibles, suivis éventuellement par quantités, lots ou unités logistiques. L’existence, la localisation, la propriété, la détention et la disponibilité ne doivent pas être fusionnées.

Exemple sans perte ni transformation : 100 pièces en A, puis départ de 40 vers B ; 60 restent en A et 40 sont en transit. Les 40 attendues par B sont une vue des mêmes biens, pas un stock physique supplémentaire. Le périmètre de propriété reste une hypothèse de l’exemple, sans règle de transfert comptable implicite.

## Appuis de marché

- [GS1 — SSCC](https://www.gs1.org/standards/id-keys/sscc) : extrait officiel consulté le 14 septembre 2026 ; une unité logistique peut être constituée pour le stockage et/ou le transport. Une identité logistique n’est donc pas réservée à un seul de ces états. Cela ne décide pas notre grain d’objet.
- [SAP ERP — Stock Transport Order with Delivery via Shipping](https://help.sap.com/docs/SAP_ERP/00b86df2555f4c83b47b97a5c1223904/ed7dc1536ca9b54ce10000000a174cb4.html) : extrait officiel consulté le 14 septembre 2026, version détaillée non établie ; suivi de quantité en transit et réception dans un processus avec livraison. Appui pour distinguer stock suivi et document/opération de livraison, sans universaliser la configuration.

## Sens de Resource

Laurent apprécie sa généricité et souligne qu’un magasin peut aussi être une ressource du point de vue Fulfillment Network. La définition U174 limitée aux biens est donc seulement une spécialisation candidate. Aucun méta-objet Resource englobant sans distinction magasins, biens et moyens n’est créé. Le choix du mot et le choix de frontières d’objets sont deux décisions distinctes.

Voir `resource_vocabulary_review.stock_transit_review` dans [l’annexe JSON](../modeles/backlog/vocabulary-review.json). Le point 6 reste clos.
