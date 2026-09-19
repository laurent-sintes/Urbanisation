# Stock et Orders — mise à jour U219–U223

**État courant U235 :** le découpage D05 est désormais appliqué ; voir [les cinq capacités et descriptions actuelles](31-inventory-optimization.md). Les propositions et descriptions antérieures ci-dessous restent historiques. D01 et D03 conservent leurs fiches.

15 septembre 2026. Restitution des champs du backlog au moment de la mise à jour ; autorité : [model.yaml](../modeles/backlog/model.yaml). La release v005 reste inchangée.

Les finalités des domaines sont adoptées U219 ; Inventory Optimization est le nom retenu U220. La définition de D05 est adoptée U223 ; les autres nouvelles définitions, les précisions opérationnelles et les deux noms de capacités restent proposés. Le réapprovisionnement automatique est une piste de périmètre U221 ; sa granularité et ses règles restent à instruire. Les capacités D03 et D01 conservent leurs définitions.

## D01 — Inventory Management

**Finalité :** Connaître et fiabiliser le stock, enregistrer ses mouvements, le protéger et le réserver.

Connaître les stocks et les ressources attendues, expliquer leurs variations, fiabiliser les quantités et préserver les usages par les protections et réservations. Le stock futur est connu ici et mobilisé par Order Promising.

Stocks physiques, états logiques et connaissance des ressources futures ; disponibilité virtuelle pour la promesse dans Order Promising. Suivi du stock, enregistrement des mouvements, visibilité, inventaire, protection et réservation conservent leurs responsabilités dans D01.

[Inventory Optimization](../modeles/backlog/model.yaml) décide du stock souhaitable et des ajustements à viser ; [Order Promising](../modeles/backlog/model.yaml) cherche comment satisfaire les Orders. D01 fournit une connaissance fiable et applique les protections et réservations de son périmètre ; il ne se réduit pas à une observation passive. Un objectif de stock n’est pas une quantité réservée ou protégée. Les règles détaillées de décision, de consommation des ressources et de révision des protections restent à instruire.

## D03 — Order Promising

**Finalité :** Décider comment satisfaire les Orders avec les ressources disponibles ou adaptables.

Chercher comment satisfaire les [Supply Orders](../modeles/backlog/glossary.yaml) : établir les possibilités de couverture en ressources et en dates, arbitrer les solutions et établir puis maintenir les promesses. Les solutions peuvent mobiliser les ressources présentes ou attendues et proposer des adaptations lorsque la situation de référence ne suffit pas.

La satisfaction des Orders est la finalité du domaine. ATP apprécie une solution dans les ressources et engagements admissibles ; CTP peut proposer leur adaptation ; PTP compare les scénarios économiquement. Priorités, affectations et échéanciers concourent à la proposition, à la confirmation et à la révision des promesses. Cette lecture ne limite pas D03 à une commande isolée : les arbitrages peuvent porter sur plusieurs commandes et leurs engagements.

Exemple fictif : déplacer 50 pièces pour satisfaire une commande précise. Le résultat recherché est sa satisfaction, en tenant compte des dates, protections et conséquences sur les autres engagements. [Inventory Optimization](../modeles/backlog/model.yaml) peut envisager un transfert semblable pour corriger la répartition du stock : la ressemblance de l’opération n’efface pas la différence de finalité.

D01 conserve la connaissance du stock, les mouvements, protections et réservations ; D04 gère les Orders et leur progression ; D07 et Services portent prestations, engagements et faits d’exécution. Proposer un scénario CTP ne crée ni n’affermit automatiquement un Order et ne réalise pas un mouvement. Supply Assignment conserve sa définition actuelle, incluant les besoins prévisionnels : leur articulation détaillée avec les besoins de stock de D05 reste à éprouver, sans réduction implicite de cette portée.

## D05 — Inventory Optimization

**Finalité :** Décider du stock souhaitable et des ajustements nécessaires.

**Définition adoptée U223 :** Optimiser le stock consiste à choisir un compromis entre disponibilité, immobilisation et risque, puis à décider des ajustements nécessaires.

**Précision opérationnelle proposée :** Déterminer le stock souhaitable et les ajustements nécessaires de ses niveaux et de sa répartition : fixer les objectifs de couverture, établir les manques ou excédents nets et décider des redistributions utiles, en tenant compte du stock connu et des ressources attendues.

Le stock à obtenir et à maintenir guide le domaine. Les objectifs et ajustements portent sur les périmètres et horizons opérationnels considérés ; leur détail reste à préciser. Les besoins peuvent prendre en compte des prévisions ou des Orders connus : la frontière avec D03 dépend de la finalité, pas de l’absence de commandes ni d’un partage global/individuel. La planification de saison demeure hors de ce périmètre.

Exemple fictif : déplacer 50 pièces pour corriger un surstock sur un site et un manque sur un autre. Le résultat recherché est une répartition de stock adaptée. [Order Promising](../modeles/backlog/model.yaml) peut envisager la même opération pour satisfaire une commande précise, avec une autre question de décision. D05.c est conservée ; partager des données ou des moyens de calcul ne suffit pas à la déclarer redondante avec le CTP.

[Inventory Management](../modeles/backlog/model.yaml) connaît et fiabilise le stock, enregistre ses mouvements, protège et réserve ; D05 détermine ce que le stock devrait devenir. Un objectif ou une redistribution décidée ne modifie pas à lui seul la position de stock et ne constitue pas une promesse. Le dossier Demande de réassort relève du modèle processus. Les Orders éventuellement mobilisés sont gérés dans D04 ; leurs possibilités de satisfaction et promesses dans D03 ; les prestations et mouvements physiques relèvent de D07 et des exécutants. Aucun type d’Order, cycle obligatoire ou transfert de responsabilité logistique à FLOW n’est déduit.

Piste U221 — réapprovisionnement automatique : déterminer le complément de stock puis déclencher une demande de [réapprovisionnement](../modeles/backlog/glossary.yaml) selon des règles et autorisations définies. Exemple fictif : cible de 100 pièces, 30 disponibles et 20 déjà attendues ; envisager un complément de 50, sous réserve des règles de calcul. Une nouvelle évaluation tient compte de ce qui a déjà été demandé ou commandé pour éviter de déclencher plusieurs fois le même complément.

Les règles peuvent conduire à une demande de réassort ou à des Orders, selon les autorités et parcours à définir. D04 gère les Orders correspondants ; D03 cherche à les satisfaire ; les exécutants réalisent les mouvements, dont D01 restitue les effets. Automatique qualifie le déclenchement selon les règles : cela ne vaut ni confirmation automatique d’une promesse, ni affermissement systématique, ni capacité autonome déjà adoptée. La granularité de cette aptitude et ses conditions restent à instruire.

## D05.a — Coverage Target Decision

**Finalité :** Définir le stock souhaitable auquel comparer la situation connue ou attendue.

Décider des niveaux et seuils de stock à viser pour le périmètre et l’horizon opérationnels considérés, afin de disposer d’une référence explicite pour le renouvellement et le rééquilibrage du stock.

Préciser le stock visé, son périmètre, son horizon et les conditions d’application de l’objectif. Exemple fictif : viser 100 pièces d’une référence sur un site pour l’horizon retenu. La nature des seuils, leurs modes de calcul et leurs autorités restent à instruire ; aucune formule de stock de sécurité ni règle universelle n’est adoptée.

Un objectif de couverture n’est ni une promesse à un client, ni une réservation pour un Order, ni une protection de ressources. Les protections et réservations restent dans D01 ; les promesses dans D03. La décision d’objectif ne constate pas une quantité physique et ne réalise pas un réassort.

## D05.b — Net Requirements Calculation

**Finalité :** Quantifier un ajustement de stock justifié, sans ignorer les ressources déjà attendues ni compter deux fois un même besoin.

Calculer les manques ou excédents nets de stock par rapport aux objectifs et besoins applicables, à partir des positions de stock et des approvisionnements attendus pertinents pour le périmètre et l’horizon considérés.

Comparer la situation de stock pertinente avec le stock souhaité. Exemple fictif simplifié : cible de 100 pièces, 30 prises en compte dans le stock et 20 supplémentaires attendues sur le même horizon ; le complément est de 50, si aucun autre besoin, mouvement ou restriction ne doit être pris en compte. Si la cible intègre déjà certaines demandes, elles ne sont pas ajoutées une seconde fois. Les règles d’admissibilité et le traitement des engagements restent à préciser.

Le résultat est un manque ou excédent à traiter. Il ne choisit pas à lui seul la source qui le couvrira, ne crée pas un Order et ne promet pas une date. ATP/CTP cherchent des solutions pour satisfaire les Orders ; des calculs de couverture communs peuvent être mobilisés, sans imposer un moteur commun ou distinct.

## D05.c — Stock Redistribution Decision

**Finalité :** Obtenir une répartition du stock mieux adaptée aux besoins des périmètres concernés.

Décider des quantités de stock à redistribuer et des destinations à privilégier pour corriger des déséquilibres de répartition, selon les objectifs de stock et les contraintes applicables.

Examiner où le stock est excédentaire ou insuffisant, puis retenir un ajustement de quantités et de destinations. Exemple fictif : déplacer 50 pièces d’un site excédentaire vers un site en manque pour rééquilibrer leurs stocks. Les critères, tolérances, autorisations, contraintes d’acheminement et effets sur les engagements restent à instruire.

La finalité de rééquilibrage justifie cette responsabilité même si [Order Promising](../modeles/backlog/model.yaml) envisage aussi des transferts. Le CTP cherche une solution pour satisfaire les Orders ; cette capacité cherche une meilleure répartition du stock. Supply Assignment affecte ou réaffecte des ressources à des besoins ou engagements : cette affectation n’est pas, à elle seule, une redistribution physique.

Une décision de redistribution peut nécessiter des Orders, dont le type et la responsabilité de création ne sont pas présumés. D04 en gère la structure et la progression ; D03 en examine la satisfaction et les promesses ; D07 et Services portent les prestations et leurs réalisations. Aucun mouvement effectif, arrêt d’exécution, calcul logistique installé ou réalisation FLOW n’est déduit de cette décision.

## Portée et correspondances

Identifiants et rattachements conservés. [Registre de frontière et historique](../modeles/backlog/stock-order-boundary.yaml). Les rapprochements partiels U222 sont documentés dans [l’étude marché](../marche/inventory-optimization-comparaison.md). U223 adopte la définition du domaine, sans valider ces correspondances ni la candidate Replenishment Decision. Aucun déploiement SI revendiqué.


## Clarification U224 — optimisation et application

D05 est le domaine analytique qui calcule le compromis et les ajustements recommandés. L'application opérationnelle met en vigueur les paramètres, déclenche les Orders et organise le réapprovisionnement. Cette orientation de Laurent remplace l'attribution proposée du déclenchement directement à D05 dans les paragraphes U221 ci-dessus, conservés comme état de rédaction antérieur. La définition U223 demeure adoptée ; les fiches de capacités doivent être revues.

Proposition à instruire : Stock Policy Optimization (objectifs, seuils, allocations recommandés), Replenishment Optimization (compléments et dates recommandés), Stock Redistribution Optimization (transferts de rééquilibrage recommandés). Le calcul net est un moyen potentiellement partagé ; son rang de capacité reste ouvert. Ces noms ne sont pas adoptés et aucun identifiant n'est supprimé ou créé.

Exemple fictif : calculer une allocation canal de 200 et un seuil de réassort de 40 relève de l'optimisation ; activer ces règles relève de leur application. Calculer un complément de 60 vers un magasin ne crée pas encore son Order et ne réalise pas le transport. Allocation de canal, réservation pour un Order et seuil de déclenchement ont des effets distincts. L'exécution peut être automatique : aucune validation humaine systématique ou découpe logicielle imposée. Stock Protection est le terme utilisateur U224 ; Supply Protection reste le nom courant de D02.b tant que son nom et son périmètre détaillé ne sont pas retravaillés.


## Proposition U227 — 16 septembre 2026, non appliquée

D05 pourrait être ramené à deux capacités : **Stock Protection Planning** (objectifs, seuils et allocations recommandés) et **Replenishment Planning** (compléments et redistributions recommandés, quantités et dates). Les calculs nets sont mobilisés par la seconde ; la redistribution reste couverte dans la même décision de planification. Aucune sous-capacité analytique par type de paramètre de protection.

Côté opérationnel, proposition de renommer et préciser D02.b Supply Protection en **Stock Protection**, avec maintien des règles actives, et d'ajouter **Replenishment Management** dans D01 pour leur mise en action par les Orders. Cela étendrait explicitement le périmètre de D01 au réapprovisionnement ; cette extension n'est pas déjà validée. D04 gère les Orders, D03 leur satisfaction et les exécutants les prestations physiques.

Noms locaux proposés, pas intitulés officiels d'un catalogue Microsoft. Proposition et limites complètes dans stock-order-boundary.yaml, capability_proposal_U227. Aucun changement de capacité ou publication à ce stade.


## Correction U229 — Decision nourrit Planning

Laurent préfère Decision aux intitulés Calculation. Planning désigne reconfigurer, simuler et valider, en mobilisant les capacités de décision. Les deux noms Planning proposés U227 pour désigner directement les responsabilités de décision sont donc à corriger. Codex propose Stock Protection Decision et Replenishment Decision ; leur granularité, l'absorption de D05.b/c et le placement de Planning restent non adoptés.

Lecture proposée : la décision détermine une réponse sous hypothèses et contraintes ; Planning fait varier les hypothèses, mobilise les décisions et valide un ensemble cohérent ; l'application donne effet aux paramètres et engage les Orders. Une dépendance fonctionnelle ne constitue pas une décomposition en sous-capacités ni un nouveau domaine. Aucun changement des nœuds à cette étape.


## Correction U230 — gouvernance et décisions spécialisées

Laurent qualifie Stock Protection comme gouvernance/management et juge Stock Protection Decision trop agrégée. La proposition d'un pendant analytique unique est abandonnée. Codex propose quatre décisions dans D05 : Coverage Target Decision (niveaux et seuils), Stock Allocation Decision (canaux/groupes), Replenishment Decision (apports à prévoir) et Stock Redistribution Decision (rééquilibrage du stock existant). La fusion de redistribution et réapprovisionnement n'est plus la recommandation courante.

Ce découpage reste proposé. La gouvernance peut s'appuyer sur plusieurs décisions ; Planning les mobilise pour reconfigurer, simuler et valider. Ce sont des responsabilités distinctes, pas une hiérarchie métier adoptée. La granularité du calcul net et les frontières détaillées sont à préciser ; aucune capacité active modifiée.


## Précision U231 — application transactionnelle

Dans Stock Protection, « application » signifie mettre à jour transactionnellement les données unitairement, en groupe ou en masse. Les interfaces possibles comprennent écrans, batch, flux et streaming. Cette responsabilité de management comprend donc la tenue concrète des données. Ces modalités ne deviennent pas des capacités supplémentaires et ne présument pas de technologie particulière. La mise à jour reste distincte de la décision sur les valeurs et de leur usage par les autres capacités.


## Glossaire de modélisation séparé — U232

Decision, Planning, Management et application transactionnelle relèvent du [glossaire de modélisation](../modeles/backlog/modeling-glossary.yaml), en support à la définition des objets du modèle. Leurs sens courants sont maintenus dans ce registre séparé du glossaire métier ; les paragraphes précédents conservent la trace de leur discussion. Aucun ajout de ces notions au glossaire métier publié.


## Proposition de domaine U233 — non appliquée

D05 Inventory Optimization conserverait sa définition U223 et comporterait quatre décisions spécialisées : Coverage Target Decision, Stock Allocation Decision, Replenishment Decision et Stock Redistribution Decision. Une cinquième capacité **Inventory Planning**, proposée dans D05, les mobiliserait pour reconfigurer, simuler et valider un scénario cohérent. Il ne s'agit pas de les placer sous Planning dans une hiérarchie de décomposition.

Résultats : cibles/seuils ; allocations/protections par groupe ; apports recommandés ; redistributions recommandées ; scénario retenu. Calcul net intégré aux décisions plutôt que capacité autonome. Stock Protection gère transactionnellement les données ; la mise en action engage les Orders. Réapprovisionnement et redistribution tiennent compte de leurs effets mutuels. Les horizons restent opérationnels ; les prévisions sont des entrées, sans import de la planification de saison.

La proposition structurée `domain_proposal_U233` dans stock-order-boundary.yaml fait foi de cette proposition, pas d'une modification du graphe actif. Les notions transversales sont définies séparément dans modeling-glossary.yaml. Aucun nom ou nouveau rattachement adopté par la demande de proposition.
