# Pilotage et orchestration de l’exécution — U247

Catalogue courant du backlog après U247, le 16 septembre 2026. Autorité : `modeles/backlog/model.yaml`. D06 regroupe huit capacités ; D05, D03 et les références restent inchangés. La release et Atlas conservent leur publication.

Service Order Management remplace le nom abstrait Execution Commitment Management. Capacity Visibility est retenu U246. Les noms et responsabilités courtes du dernier tableau sont repris dans leur portée ; la fusion qualification/options en Execution Service Decision reste proposée. Les descriptions détaillées et exemples sont des compléments proposés.

| Identifiant | Capacité | Responsabilité |
| --- | --- | --- |
| D07.a | Execution Requirements Decision | Déterminer les prestations nécessaires. |
| D06.e | Execution Service Decision | Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes. |
| D06.b | Execution Capacity Visibility | Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply. |
| D07.b | Service Order Management | Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service. |
| D06.d | Execution Orchestration | Coordonner les prestations et leurs dépendances. |
| D07.d | Execution Tracking | Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation. |
| D07.c | Execution Reconciliation | Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs. |
| D06.f | Execution Adaptation Decision | Déterminer les variations du plan. |

<a id="d06"></a>
## D06 — Execution Management

Orchestrer l’exécution Supply en coordonnant les prestations, en suivant leur réalisation et en adaptant le plan aux aléas, en articulation avec la promesse Supply.

Connaître les services admissibles et la capacité logistique contextualisée ; exprimer les prestations, gérer leurs engagements, coordonner leurs dépendances, suivre leur avancement et adapter le plan aux aléas. Les services couvrent entrepôt, transport et prestations telles que la production de documents.

Un SLA configuré compatible ne garantit pas la réussite opérationnelle. Exemple : la préparation prend du retard et menace la collecte ; rechercher une autre collecte, un autre service ou une réalisation partielle selon les contraintes, puis mobiliser D03 si la promesse doit être réexaminée.

Le référentiel D14 décrit l’offre et les SLA globaux ; D06 traite le contexte opérationnel. D03 conserve la décision de promesse Supply, D04 les Orders et leurs reliquats, D01 la représentation du stock et de ses mouvements. Les exécutants conservent leurs opérations internes. La latitude d’adaptation est une règle de fonctionnement, sans effet sur le catalogue des capacités.

<a id="d07-a"></a>
## D07.a — Execution Requirements Decision

Déterminer les prestations nécessaires.

Déterminer, à partir du besoin Supply et de ses contraintes, les prestations et résultats requis : préparation, réception, transport ou production de documents. Préciser biens ou documents concernés, quantités, destinataires, lieux et échéances utiles.

Exemple : réaliser la livraison requiert une préparation, un document et un transport. La décision explicite ces besoins ; Service Order Management tient ensuite les demandes adressées aux exécutants et leurs évolutions. La décision de service choisit les moyens de service pour y répondre.

La capacité ne se limite plus à formuler un message ou à exprimer un Service Order. Elle ne recrée ni l’autorisation de la commande D04, ni sa promesse D03, ni un Agreement ou un Case. D07.a conserve son identité pour la responsabilité de détermination des prestations, précisée par U245/U247.

<a id="d06-e"></a>
## D06.e — Execution Service Decision

Déterminer les services et exécutants à mobiliser pour les prestations nécessaires, en tenant compte de leur admissibilité et des contraintes.

Regrouper les responsabilités d’admissibilité et de comparaison d’options auparavant portées par D06.a et D06.c. Exploiter le catalogue des services, les lieux et relations du réseau, les conditions applicables et la visibilité sur la capacité. Déterminer les services utilisables, puis les moyens à mobiliser.

Exemple : identifier les transporteurs desservant une destination, compatibles avec les marchandises et les horaires, puis déterminer le service à solliciter. La qualification désignait ce contrôle d’admissibilité ; elle n’est plus une capacité distincte dans cette proposition.

La décision reste dans le besoin Supply et les contraintes portés par D03. Elle ne reprend pas la décision de couverture de l’Order ou la révision de sa promesse. Elle peut être mobilisée pour le plan initial ou par Adaptation Decision. Le regroupement et cette formulation sont appliqués comme proposition ; aucune validation antérieure de D06.a/c n’est transférée.

<a id="d06-b"></a>
## D06.b — Execution Capacity Visibility

Rendre visible la capacité opérationnelle communiquée par les exécutants, avec son contexte, sa période et sa fraîcheur, pour alimenter les décisions Supply.

Rendre accessible la capacité logistique dans son contexte, par exemple le nombre maximal de préparations communiqué pour un site et un créneau. Expliciter le service, l’unité, la période, l’origine et la fraîcheur des informations disponibles.

Exemple : l’entrepôt annonce un plafond de 1 000 préparations sur un créneau ; si une charge ou un disponible sont également communiqués, les présenter avec leur sens et leur date de connaissance. Ne pas transformer sans règle connue ce plafond en capacité encore disponible.

Cette visibilité ne décide pas d’augmenter les ressources de l’exécutant, ne calcule pas implicitement un disponible à partir d’une formule non convenue et ne réserve pas la capacité. D03 l’utilise pour sa promesse Supply ; Service Decision et Adaptation Decision peuvent la mobiliser. Le nom est adopté U246 ; les détails de représentation et contrats restent proposés.

<a id="d07-b"></a>
## D07.b — Service Order Management

Gérer les demandes de prestation adressées aux exécutants et leur cycle de vie : émission, acceptation ou refus, modification, annulation et clôture, selon le service.

Tenir ce qui est demandé à un exécutant, ce qu’il accepte de réaliser et les évolutions de cette prise en charge. L’émission d’une demande, son acceptation et sa réalisation restent distinctes. Les opérations possibles dépendent du service et de son état ; aucun cycle universel ni acceptation systématiquement différée n’est imposé.

Exemple : demander à l’entrepôt de préparer 100 colis avant 16 h ; enregistrer l’acceptation, le refus ou une autre échéance proposée ; tenir ensuite une demande de modification ou d’annulation et la réponse correspondante. Le tracking renseigne en parallèle la préparation commencée, les 60 colis prêts ou le retard annoncé.

Requirements Decision détermine les prestations nécessaires ; Orchestration coordonne les prestations et leurs dépendances ; Adaptation Decision détermine la variation du plan. Cette gestion met à jour transactionnellement les demandes et leurs états, unitairement ou en groupe selon les interfaces disponibles ; ces modalités ne créent pas de capacités supplémentaires.

Conserver la distinction entre SLA configuré, engagement individuel, estimation et résultat. Les exécutants gardent leurs opérations internes et D03 la promesse Supply. D07.b conserve la gestion des prises en charge et engagements, désormais explicitée dans le cycle du Service Order.

<a id="d06-d"></a>
## D06.d — Execution Orchestration

Coordonner les prestations et leurs dépendances.

Coordonner le déclenchement et l’enchaînement des prestations du plan retenu, en tenant compte de leurs dépendances, des prises en charge et des faits d’exécution. Mobiliser Service Order Management pour tenir les demandes et leurs évolutions.

Exemple : coordonner la préparation, la disponibilité du document et la collecte. Si la décision d’adaptation retient un autre transporteur, coordonner la modification des prestations concernées et leur nouvel enchaînement.

La détermination de la variation du plan appartient à Execution Adaptation Decision. L’orchestration peut lui transmettre un aléa, mais ne porte plus cette décision dans sa propre définition. Les exécutants conservent l’organisation de leurs opérations internes. Aucun moteur de workflow, contrôle humain systématique ou rollback physique universel n’est présumé.

<a id="d07-d"></a>
## D07.d — Execution Tracking

Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation.

Conserver la responsabilité d’Expected Supply Tracking : quantités, dates, provenance et fermeté des ressources encore attendues. Étendre explicitement le suivi aux opérations et résultats des services, y compris documentaires, sans créer un cycle identique pour tous.

Exemple : préparation commencée, retard annoncé, expédition partielle, transport en cours ou document en échec. Identifier le fait, la prestation et sa fraîcheur ; distinguer estimation, engagement et constat. Le feedback continu signifie un suivi pendant la prestation, sans télémétrie temps réel uniforme imposée.

Le tracking alimente l’orchestration pour la coordination des prestations et Adaptation Decision pour la recherche d’une variation du plan ; D03 conserve le réexamen de la promesse lorsque nécessaire. Il ne décide pas seul d’une variante et ne tient pas le stock à la place de D01.

<a id="d07-c"></a>
## D07.c — Execution Reconciliation

Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs.

Rapprocher production, préparation, expédition, réception, consommation et résultats documentaires des prestations demandées et engagées. Les quantités manquantes, écarts et résultats partiels sont qualifiés à la maille pertinente.

Exemple : 80 unités sont reçues sur les 100 attendues ; qualifier l’écart de prestation et en transmettre les faits à la commande concernée. D04 conserve le reliquat de l’Order et D01 la représentation des mouvements de stock. Les cinq contributions existantes vers les capacités par type d’Order sont conservées, avec leur statut proposé. Le tracking rend visible l’avancement ; le rapprochement explique le réalisé au regard de l’attendu.

<a id="d06-f"></a>
## D06.f — Execution Adaptation Decision

Déterminer les variations du plan.

Déterminer la variation à retenir lorsqu’un fait, un retard ou un échec remet en cause le plan d’exécution. Mobiliser les décisions de service, les capacités communiquées et les informations sur les demandes et réalisations.

Exemple : un SLA était compatible avec la collecte, mais une panne retarde la préparation. Déterminer une autre collecte, un autre transporteur ou une réalisation partielle selon les possibilités ; Orchestration coordonne ensuite les prestations du plan retenu.

Si la variation remet la promesse Supply en cause, fournir à D03 les faits et variantes utiles à son réexamen. Cette capacité ne décide pas seule d’une nouvelle promesse. La latitude d’adaptation relève des règles de fonctionnement et ne conditionne pas le catalogue.

Decision détermine une réponse métier ; Planning conserve le sens reconfigurer, simuler et valider en mobilisant des décisions. La séparation demandée n’ajoute pas automatiquement une capacité Planning ou un contrôle humain obligatoire.

<a id="d14"></a>
## D14 — Execution Service Catalog

Le référentiel contient la liste des services et leurs SLA globaux en configuration.

Offre de préparation, réception, transport et autres services tels que la production de documents. Décrire le résultat rendu, le prestataire, les conditions d’éligibilité et le SLA de réalisation applicable, ainsi que les accès informatiques de sollicitation et de feedback.

Exemple : un service de préparation à délai configuré, un transport et une génération de document ont des résultats et engagements différents. Le SLA exprime le service rendu, notamment lorsqu’il dépend du physique ; il reste distinct du temps de réponse informatique. L’identité métier d’un service est distincte de ses accès techniques ; un exécutant partiellement manuel peut être sollicité via une adaptation.

Charge actuelle, capacité contextuelle, demandes, engagements individuels, estimations et résultats relèvent de D06. Fulfillment Network décrit les lieux et relations, Party les parties, Agreement les accords maîtres et Catalog les offres commerciales. Aucun protocole ni endpoint unique imposé.

<a id="d14-a"></a>
## D14.a — Execution Service Catalog Ingestion

Recevoir l’offre des services exécutants, leurs SLA configurés, conditions et accès, ainsi que leurs évolutions depuis les sources maîtresses externes.

Ingestion du référentiel, dans la continuité du principe des projections Supply. Recevoir les évolutions des services et de leurs accès sans reprendre la maîtrise des données. Consultation et recherche restent en lecture seule pour les consommateurs.

L’ingestion du catalogue ne reçoit pas à sa place le tracking des opérations et ne transforme pas une évolution du SLA en révision automatique des engagements déjà pris. Maîtres et contrats d’échange seront définis dans les règles de fonctionnement.

## Continuité, vocabulaire et sources

D06.a/c et leurs rattachements sont conservés dans history/pre-U247.yaml ; la décision de service reçoit une nouvelle identité D06.e. L’adaptation reçoit D06.f ; D06.d garde la coordination. Les capacités D07.a–d gardent leurs identités et leur rattachement explicite à D06. Les cinq liens de rapprochement D07.c vers D04.i–m sont inchangés.

Les deux glossaires sont inchangés. Decision détermine une réponse métier ; Visibility restitue une connaissance ; Management tient les demandes et leurs évolutions. Planning reste reconfigurer, simuler et valider en mobilisant des décisions. La latitude d’adaptation n’impacte pas le catalogue.

CMP079 actualise les correspondances depuis les études U239/U241 et CMP078, sans nouvelle consultation de source éditeur. Les granularités et frontières locales ne sont pas des équivalences de marché.

État documentaire U244 conservé dans audits/2026-09-16-execution-capacites/before-description.md ; accords et application détaillés dans execution-services-review.yaml.


## Convention courante U409 — Process et Service

Le Process orchestre des Services. D06 devient Process Management ; les noms et portées courants sont dans modeles/backlog/execution-services-review.yaml, process_services_U409. Les sections précédentes conservent leur valeur historique. Operations Tracking porte Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking. Les noms changent sans ajouter de capacité ou déplacer de responsabilité ; les identifiants restent stables.
