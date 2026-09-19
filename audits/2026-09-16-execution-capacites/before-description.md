# Pilotage et orchestration de l’exécution — U244

Mise à jour du backlog le 16 septembre 2026. Autorité : `modeles/backlog/model.yaml`. D05 conservé ; D06 regroupe les responsabilités de D06/D07. D07 est retiré comme domaine, ses capacités gardent leurs identifiants. La release reste inchangée.

Les principes U240/U242/U243 et la définition de domaine présentée avant U244 sont adoptés dans leurs portées. Les nouveaux noms anglais, le détail des capacités, les exemples et qualifications de relations restent proposés. La latitude d’adaptation ne conditionne pas le catalogue.

| Identifiant | Capacité du domaine D06 | Responsabilité |
| --- | --- | --- |
| D06.a | Execution Service Qualification | Qualifier les lieux et services admissibles pour une prestation dans son contexte opérationnel. |
| D06.b | Execution Capacity Assessment | Décrire et apprécier la capacité opérationnelle des exécutants dans le contexte d’une prestation et d’une période. |
| D06.c | Execution Option Assessment | Établir et comparer les variantes de réalisation compatibles avec le résultat attendu et la situation opérationnelle. |
| D07.a | Execution Requirement Definition | Exprimer les prestations nécessaires à la réalisation des Orders Supply sous forme de Service Orders compréhensibles par les exécutants. |
| D07.b | Execution Commitment Management | Gérer la prise en charge et les engagements des exécutants, leur portée, leur validité et leurs évolutions. |
| D07.d | Execution Tracking | Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation. |
| D07.c | Execution Reconciliation | Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs. |
| D06.d | Execution Orchestration | Coordonner les prestations et leurs dépendances, puis adapter le plan d’exécution en réponse aux faits et aux aléas. |

<a id="d06"></a>
## D06 — Execution Management

Orchestrer l’exécution Supply en coordonnant les prestations, en suivant leur réalisation et en adaptant le plan aux aléas, en articulation avec la promesse Supply.

Connaître les services admissibles et la capacité logistique contextualisée ; exprimer les prestations, gérer leurs engagements, coordonner leurs dépendances, suivre leur avancement et adapter le plan aux aléas. Les services couvrent entrepôt, transport et prestations telles que la production de documents.

Un SLA configuré compatible ne garantit pas la réussite opérationnelle. Exemple : la préparation prend du retard et menace la collecte ; rechercher une autre collecte, un autre service ou une réalisation partielle selon les contraintes, puis mobiliser D03 si la promesse doit être réexaminée.

Le référentiel D14 décrit l’offre et les SLA globaux ; D06 traite le contexte opérationnel. D03 conserve la décision de promesse Supply, D04 les Orders et leurs reliquats, D01 la représentation du stock et de ses mouvements. Les exécutants conservent leurs opérations internes. La latitude d’adaptation est une règle de fonctionnement, sans effet sur le catalogue des capacités.

<a id="d06-a"></a>
## D06.a — Execution Service Qualification

Qualifier les lieux et services admissibles pour une prestation dans son contexte opérationnel.

Mobiliser les lieux et relations de Fulfillment Network ainsi que les services, conditions et SLA du catalogue d’exécution. Examiner leur applicabilité au besoin : origine, destination, nature des biens ou documents, horaires et restrictions.

Exemple : un service de préparation existe au catalogue, mais le site concerné ne prend pas en charge cette catégorie de marchandises. Qualifier cette inadmissibilité sans administrer le référentiel. La capacité quantitative est évaluée par Execution Capacity Assessment ; la comparaison des solutions relève d’Execution Option Assessment.

<a id="d06-b"></a>
## D06.b — Execution Capacity Assessment

Décrire et apprécier la capacité opérationnelle des exécutants dans le contexte d’une prestation et d’une période.

Décrire notamment le nombre maximal de préparations dans un contexte donné, comme précisé en U240. D03 utilise cette connaissance pour sa promesse Supply.

Exemple illustratif : un entrepôt annonce un plafond de préparation pour le créneau considéré. Les unités, horizons, charge déjà engagée, ressources partagées et fraîcheur permettent d’interpréter ce chiffre ; leur détail demeure proposé. Un maximum ne constitue pas à lui seul une formule de capacité résiduelle.

Cette capacité évalue la réalisation possible ; elle ne confirme pas une promesse Supply. La mesure et la consommation de capacité restent à préciser comme règles, sans imposer un algorithme ou une réservation à chaque simulation.

<a id="d06-c"></a>
## D06.c — Execution Option Assessment

Établir et comparer les variantes de réalisation compatibles avec le résultat attendu et la situation opérationnelle.

Comparer les origines, prestations, combinaisons ou séquences possibles à partir des services qualifiés, capacités contextuelles et engagements. Conserver cette responsabilité utile aussi avant une promesse.

Exemple : après un retard de préparation, examiner une collecte ultérieure ou un autre service de transport. Une variante peut préserver le résultat attendu ou nécessiter le réexamen de la promesse par D03. L’évaluation ne vaut ni engagement de l’exécutant ni modification de la promesse ; l’orchestration coordonne la mise en œuvre de la variante selon les règles applicables.

<a id="d07-a"></a>
## D07.a — Execution Requirement Definition

Exprimer les prestations nécessaires à la réalisation des Orders Supply sous forme de Service Orders compréhensibles par les exécutants.

Préciser résultats attendus, biens ou documents concernés, lieux, destinataires, quantités et échéances utiles. Distinguer une demande, son acceptation et sa réalisation ; aucune cardinalité Order/Service Order ni séquence technique universelle n’est imposée.

Exemple : exprimer les prestations de préparation, de production documentaire et de transport nécessaires à une commande. Le Service Order reste propre au contexte des prestations ; il ne recrée ni l’autorisation commerciale, ni l’Agreement, ni le Case. Le canal de sollicitation est décrit par les accès du service.

<a id="d07-b"></a>
## D07.b — Execution Commitment Management

Gérer la prise en charge et les engagements des exécutants, leur portée, leur validité et leurs évolutions.

Tenir les acceptations, refus, retraits, modifications et engagements de réalisation ; traiter les sollicitations de suspension, annulation ou reprise selon les possibilités propres au service et à son état. Distinguer SLA configuré, engagement pris pour une prestation, estimation actualisée et résultat constaté.

Exemple : un transporteur accepte une collecte à 16 h ; un retard impose de réviser cet engagement. L’estimation d’arrivée mise à jour n’est pas à elle seule une nouvelle acceptation. Un acquittement informatique ne prouve pas la réussite physique.

Les règles éventuelles de consommation/libération de capacité restent à définir ; leur détail ne crée pas une nouvelle capacité. Les exécutants conservent leurs opérations internes et D03 la promesse Supply.

<a id="d07-d"></a>
## D07.d — Execution Tracking

Suivre les faits, jalons, estimations et résultats encore attendus des prestations pendant leur réalisation.

Conserver la responsabilité d’Expected Supply Tracking : quantités, dates, provenance et fermeté des ressources encore attendues. Étendre explicitement le suivi aux opérations et résultats des services, y compris documentaires, sans créer un cycle identique pour tous.

Exemple : préparation commencée, retard annoncé, expédition partielle, transport en cours ou document en échec. Identifier le fait, la prestation et sa fraîcheur ; distinguer estimation, engagement et constat. Le feedback continu signifie un suivi pendant la prestation, sans télémétrie temps réel uniforme imposée.

Le tracking alimente l’orchestration et le réexamen de promesse lorsque nécessaire. Il ne décide pas seul d’une variante et ne tient pas le stock à la place de D01.

<a id="d07-c"></a>
## D07.c — Execution Reconciliation

Rapprocher les résultats constatés des prestations attendues, qualifier les écarts et fournir les faits utiles aux domaines consommateurs.

Rapprocher production, préparation, expédition, réception, consommation et résultats documentaires des prestations demandées et engagées. Les quantités manquantes, écarts et résultats partiels sont qualifiés à la maille pertinente.

Exemple : 80 unités sont reçues sur les 100 attendues ; qualifier l’écart de prestation et en transmettre les faits à la commande concernée. D04 conserve le reliquat de l’Order et D01 la représentation des mouvements de stock. Les cinq contributions existantes vers les capacités par type d’Order sont conservées, avec leur statut proposé. Le tracking rend visible l’avancement ; le rapprochement explique le réalisé au regard de l’attendu.

<a id="d06-d"></a>
## D06.d — Execution Orchestration

Coordonner les prestations et leurs dépendances, puis adapter le plan d’exécution en réponse aux faits et aux aléas.

Coordonner les prestations entre exécutants à partir des demandes, engagements, évaluations et faits. Rechercher une variation du plan lorsque le réel contredit les conditions prévues ; mobiliser l’évaluation des options et la gestion des engagements pour la rendre exécutable.

Exemple : un SLA prévoit une préparation compatible avec la collecte, mais une panne retarde le départ. Exploiter le tracking, comparer les variantes et coordonner les prestations concernées, notamment transport et document. D03 réexamine la promesse Supply lorsque celle-ci est remise en cause.

Cette orchestration porte l’exécution Supply et respecte les opérations internes des exécutants. Les conditions d’autonomie, coûts et autorisations relèvent des règles de fonctionnement et ne conditionnent pas le catalogue. Aucun contrôle humain obligatoire, technologie de workflow, objet Plan formalisé ou rollback physique universel n’est imposé.

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

## Vocabulaire

TER075 Execution Service et TER076 Service Level Agreement sont ajoutés comme propositions au glossaire métier. TER066 Service Order conserve son sens. Le glossaire de modélisation reste distinct et inchangé.

## Frontières et continuité

Les cinq liens D07.c vers D04.i–m sont conservés à l’identique. D01/D03/D04/D05 et les cinq référentiels existants conservent leurs nœuds. D06.a continue la qualification des lieux/services ; D07.d conserve les ressources encore attendues et étend son tracking aux prestations. Aucun préfixe d’identifiant ne détermine le parent.

La nouvelle définition de D06 rend l’adaptation explicite. Les règles d’autonomie, mesures et contrats d’échange restent des questions de fonctionnement. La réalisation interne des exécutants et la promesse Supply D03 restent distinctes.

## Marché

CMP078 actualise la projection locale de CMP077 sur les nœuds appliqués. Les études U239/U241 restent les preuves consultées ; aucune nouvelle vérification éditeur réalisée dans cette application. Appuis partiels TM Forum au catalogue/qualification/orchestration et Microsoft/SAP à la contribution de capacité vers la promesse ; aucune équivalence globale ou couverture installée démontrée.
