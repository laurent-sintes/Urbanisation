# FLOW — kit de revue V0

Préparé pour U434, le 19 septembre 2026. **Support proposé pour un atelier de revue ; aucune validation des réponses ni publication déduite.** Les noms et responsabilités viennent du backlog audité. Les situations chiffrées ci-dessous sont fictives et ne décrivent pas un déploiement Beaumanoir.

Mise à jour U435/U436 : corrections prioritaires appliquées et **blocage des usages concurrents réservé à Reservation**. Le [rapport des modifications](modifications.md) distingue les corrections faites et les contrats restant à instruire. Les cas ci-dessous restent des épreuves métier à discuter, pas des tests fonctionnels réussis d’une solution.

## Le message à présenter

FLOW Supply décrit les aptitudes nécessaires pour connaître les ressources, prendre en charge les demandes, décider de leur satisfaction, préparer le stock et coordonner les prestations. La carte distingue cinq domaines, six projections de référence, 47 capacités et 74 comportements. Les comportements décrivent des variantes ou mécanismes métier ; ils ne constituent pas un enchaînement d’écrans ni un découpage en applications.

Cette V0 est une base d’alignement des responsabilités et des interactions. Les attributions aux produits, les contrats détaillés et la couverture des SI existants ont leur propre instruction. Business Services est un univers distinct dont le détail reste à construire. L’autonomie des exécutants, notamment C-Log, est conservée. Sarenza reste non évalué.

## Lecture par public

| Public | Ce qu’il doit pouvoir expliquer après la revue | Preuve à obtenir |
| --- | --- | --- |
| PO | Résultat attendu, variantes utiles, périmètre, dépendances et critères de succès | Une situation métier et un contre-exemple pour chaque capacité du périmètre du PO ; ne pas déduire un produit par capacité |
| Domain expert | Sens des quantités, états, engagements, exceptions et règles d’arbitrage | Deux cas contradictoires résolus sans confusion entre demande, promesse, réservation et réalisé |
| Architecte solution | Qui décide, qui applique, quel résultat est échangé, avec quelle identité et validité | Un contrat minimal par interaction critique et une réaction explicite à l’échec, au retard ou au fait corrigé |

## Carte de lecture des responsabilités

| Ensemble | Question métier | Résultat principal | Limite à rappeler |
| --- | --- | --- | --- |
| D01 Inventory Management | Quelles ressources connaît-on et quels usages autorise-t-on ? | État de stock, mouvements tracés, protections et réservations | Stock futur distinct du physique ; réservation distincte de l’affectation |
| D03 Order Backlog Management | Comment satisfaire le carnet avec les ressources et contraintes ? | Possibilités, choix de satisfaction, affectations, promesses et scénarios | Décision de plan distincte de son application et de l’exécution |
| D04 Order Management | Quelle demande porte-t-on et quelles évolutions sont autorisées ? | Orders par intention et progression de leurs engagements | Types d’Order distincts ; pas de cycle universel ; Structuring et Archiving sont dans D03 |
| D05 Inventory Optimization | Quels objectifs et ajustements améliorent disponibilité, immobilisation et risque ? | Cibles, apports, redistribution, politiques et devenir des retours | Prévision et assortiment sont des entrées à qualifier ; aucune pondération universelle |
| D06 Process Management | Quelles prestations réaliser et comment coordonner/adopter une variation ? | Besoins et demandes de services, coordination, suivi et rapprochement | Opérations internes des exécutants et promesse Supply restent distinctes |
| D08/D09/D11/D12/D13/D14 | Quelles références externes rendent ces décisions possibles ? | Projections Product, Party/Role, Agreement, Catalog, Network, Service Catalog | Ingestion n’attribue pas la maîtrise des données à Supply |

## Seize cas d’épreuve

Il s’agit d’un programme de revue documentaire et métier, pas de tests d’une solution implémentée. « Appui existant » signifie responsabilité décrite dans le modèle, pas démonstration fonctionnelle ni accord sur toutes les valeurs.

| Cas | Situation fictive et question décisive | Appui existant | Point à rendre visible / résultat de revue attendu |
| --- | --- | --- | --- |
| V0-S01 Stock reçu puis corrigé | Réception de 100 reçue deux fois, corrigée ensuite à 80. Quelle quantité devient utilisable et quand ? | D01.g/f/c, D07.c/d | Identité du fait, correction traçable, absence de double compte, effet sur les promesses ; ne pas assimiler retrait d’un message et annulation physique |
| V0-S02 Protection et engagements concurrents | 100 pièces, protection de 30 pour un groupe, deux demandes simultanées de 60. Qui peut engager quoi ? | D02.b/c/e, D05.d/h, D03.i/n/o | Séparer droit d’usage, choix d’affectation, réservation opposable et confirmation ; prolongement A01/A07 U431, aucune solution d’atomicité présumée |
| V0-S03 B2B, priorités et coût | Ressource insuffisante pour trois clients, l’un plus rentable, un autre prioritaire contractuellement. Qui tranche ? | D03.m/k/o, D11, D03.p | Contraintes dures, préférences, critères de valeur et trace de dérogation ; PTP ne décide pas implicitement à la place de toutes les décisions |
| V0-S04 Échéancier et split | 100 demandées, 60 vendredi, 40 lundi. Est-ce une ou deux commandes ? | D03.l, D04.n/BHV044, D03.n, D04.o | Ne pas déduire deux Orders des deux échéances ; indiquer le résultat transmis, puis l’autorité de modification |
| V0-S05 Promesse sous calendrier | Stock suffisant vendredi à 17 h 05, collecte fermée à 17 h et jour férié lundi. Quelle date peut être promise ? | D03.i/BHV003, D03.l, D06.b, D13/D14 | Provenance, version et fuseau des calendriers, date de coupure, fraîcheur des délais ; préciser l’entrée avant de créer une nouvelle capacité |
| V0-S06 Confirmation fournisseur | 100 attendues, fournisseur confirme 80 plus tard. Que changent stock futur, échéancier et promesse client ? | D04.j/BHV078, D01.f, D07.d, D03.n | Donner un lien explicite de fait/résultat et ses consommateurs ; confirmation fournisseur distincte de réception |
| V0-S07 Livraison directe | Le fournisseur livre le client, la marchandise ne passe pas par un entrepôt du groupe. Qui porte demande, engagement et preuve de livraison ? | D04.i/j et leurs variantes, D03, D06, D07.c/d | Relier les intentions vente/achat sans identité ni cardinalité imposée entre Orders ; qualifier propriété et détenteur |
| V0-S08 Consignation et fin de saison | Stock détenu mais fournisseur propriétaire ; une partie vendue, une partie invendue. Qui décide acquisition, maintien ou retour ? | D04.r, D01.h, D11, D05, D04.j/m | Lier apport, régime de stock, choix du devenir et mise en œuvre ; responsabilité de décision après saison encore à instruire, sans ranger tous les invendus sous Customer Return |
| V0-S09 Implantation puis réassort | Cible initiale 100, 30 présentes, 50 engagées, retard de 20 puis besoin accru. Quels apports nouveaux ? | D05.a/g/e, BHV083–085, D05.f, D04 | Ne pas recréer les 50 engagées ; finalité implantation distincte du réassort, même si les dates se recouvrent |
| V0-S10 Redistribution et tailles | Deux magasins ont des tailles dispersées ; un transfert reconstitue un assortiment mais prive le donneur. Quel compromis ? | D05.c, D05.a, D05.e, D04.k, D02.e | Préserver besoin du donneur, coûts et risque ; coordonner transfert de redistribution et apport de réassort pour éviter le doublon |
| V0-S11 Retour client multissue | Retour autorisé, produit à inspecter, puis remise en stock ou réparation ou rebut. Le remboursement est-il automatique ? | D04.l, D05.i, D06, D01 | Séparer autorisation commerciale, inspection, décision logistique et résultat financier externe ; aucun remboursement déduit du mouvement |
| V0-S12 Retour fournisseur | Renvoi pour avoir, remplacement ou réparation du même bien. Quand considérer la suite terminée ? | D04.m, D04.j, D01, D06 | Préserver différences d’identité et de résultat attendu ; rapprochement de prestation distinct du reliquat de l’Order |
| V0-S13 Release puis échec | Order libéré ; prestataire refuse ou n’accuse pas réception. Que reste-t-il autorisé et engagé ? | D04.o/BHV039, D06.d, D07.b/d, D06.f | Contrat de prise en charge, refus et reprise ; ne pas lire « release » comme exécution réussie |
| V0-S14 Changement après expédition | Une quantité est annulée après expédition partielle. Que peut-on encore changer ? | D04.o, D06.f/d, D07.b/c, D01.g | Distinguer annulation logique, demande de compensation et fait irréversible ; réévaluer promesse et engagement sans rollback physique imaginaire |
| V0-S15 Référence externe devenue invalide | Accord expiré ou produit bloqué après réception d’un Order. Quelles données font foi pour la suite ? | D11/D08, capacités d’ingestion, D04.o, D03, D01 | Conserver version applicable, temporalité et identité ; ne pas supposer le nom du maître installé ; définir alerte/rejet et autorité de dérogation |
| V0-S16 Prestation et résultat numérique | Commande d’une prestation ; appel technique réussi mais document métier non produit. Le service est-il terminé ? | D04.j, D07.b, D07.d/BHV082, D07.c, D14 | Distinguer achat éventuel, demande de service, appel, résultat métier et achèvement du processus ; réception technique insuffisante |

## Fiche minimale d’interaction à discuter

Pour chaque lien critique, renseigner le résultat observable, sans imposer de protocole d’API :

1. **Expression source → cible** : par exemple « transmet la confirmation fournisseur à prendre en compte », distinct de « dépend de ».
2. **Objet et identité** : Order, ligne/fraction, ressource, plan, prestation, fait ou référence concernée ; cardinalité connue ou explicitement ouverte.
3. **Situation de validité** : quantités/unités, dates/horizon, version, origine et fraîcheur ; statut proposé/autorisé/engagé/réalisé.
4. **Autorité et effet** : qui décide, qui applique, ce qui devient opposable et ce qui reste une recommandation.
5. **Écarts** : refus, délai dépassé, résultat partiel, données périmées ou contradictoires, doublon et correction.
6. **Limites et preuve** : frontière de responsabilité, source locale ou marché, proposition ou champ adopté, inconnus restant à instruire.

Le contrat V0 doit suffire à raconter un passage métier. Les schémas de messages, mécanismes de concurrence, transactions distribuées, stockage et SLA techniques appartiennent à la conception ultérieure.

## Six décisions à organiser

| Décision | Question à instruire | Position de départ | Statut de présentation |
| --- | --- | --- | --- |
| V0-A01 | Quels effets détaillés ont expiration, consommation, libération et automatisation de la réservation ? | U436 : seule Reservation bloque les usages concurrents ; Supply Assignment seul ne les bloque pas | Frontière tranchée ; règles détaillées et engagement technique encore ouverts |
| V0-A02 | Quels effets produit l’application d’un plan : liens d’affectation, structure, états ou plusieurs ? | A03 U431 ; distinguer choix et application | Ouvert ; montrer le passage retenu pour chaque scénario |
| V0-A03 | Quelle information de capacité est réellement engageable ? | A07 U431 ; plafond, charge et disponible ne sont pas synonymes | Ouvert ; pas de réservation de capacité inventée |
| V0-A04 | Qui fournit autorisations commerciales et financières et qui consomme les résultats Supply ? | A04 U431 et frontière U429 ; organisation externe non globalement tranchée | Exclusion explicite et interfaces identifiées |
| V0-A05 | Qui choisit le devenir d’un stock consigné après saison ? | Annexes U395 : articulation D05 à instruire ; D01 applique l’accord | Arbitrage métier ciblé ; pas de nouvelle capacité automatique |
| V0-A06 | Qui gouverne/applique la version des politiques de réservation ? | D05.h décide ; porteur de management encore ouvert dans l’annexe | Responsabilité à expliciter avant engagement de réalisation |

## Conditions pour qualifier la V0 de « propre à présenter »

- **Lecture cohérente :** aucun texte courant ne contredit un rattachement actuel ; les décisions remplacées restent dans l’historique.
- **Sens visible :** les six interactions prioritaires de [liens.md](liens.md) ont une expression orientée et une frontière, et sont lisibles dans le support de présentation choisi.
- **Trois exemples maîtrisés :** vente partielle sous contrainte, consignation et retour peuvent être expliqués du début au résultat avec leurs exceptions. Les autres scénarios sont disponibles pour l’atelier.
- **Qualification honnête :** champs adoptés, éditoriaux et ouverts sont distingués ; un badge d’élément ou une publication ne vaut pas validation globale.
- **Marché traçable :** rapprochements prioritaires des fiches cohérents avec leur périmètre actuel ; différences et limites visibles ; pas de pourcentage de couverture globale non démontré.
- **Périmètre explicite :** externes, Business Services différé et SI non évalués annoncés ; aucun maître ni déploiement imaginé.
- **Intégrité vérifiée après les corrections :** validation et contrôles ciblés réussis, sans modification des anciennes publications. Si une nouvelle version Atlas est demandée, elle suivra le workflow de release distinct.

Ces conditions sont proposées. Elles n’imposent ni validation de tous les contrats de réalisation avant l’atelier, ni complétude de tous les domaines de l’entreprise.

## Déroulé proposé de la revue — 90 minutes

10 minutes sur le périmètre et les cinq responsabilités ; 15 minutes sur le vocabulaire et les décisions distinctes ; 35 minutes sur les trois exemples prioritaires ; 20 minutes sur les interfaces et six questions ouvertes ; 10 minutes pour consigner les corrections et accords **champ par champ**. La durée est une proposition d’animation, pas une estimation du travail de remédiation.

Les décisions de revue doivent préciser contenu présenté, champ ou interaction concerné, réserves et auteur de l’accord. Une liste d’actions avec responsable et critère de clôture suffit ; aucun accord global sur tous les descendants.
