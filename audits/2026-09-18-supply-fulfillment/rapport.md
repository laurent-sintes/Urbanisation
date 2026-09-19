# Audit local — Supply, Supply Chain et Fulfillment

18 septembre 2026 · Demandes U366/U367, réexamens U368/U369 · Comparaisons CMP136–138.

**État U369 :** les noms **Fulfillment Optimization** (D03) et **Supply Network** (D13) sont adoptés ; leur application au catalogue reste à réaliser. Le nom **Supply Chain Management** pour l’univers est recommandé et encore proposé. Les analyses de portée et les descriptions détaillées ci-dessous ne sont pas validées globalement par ces accords de nommage.

**Réexamen U370 :** les achats et l’approvisionnement des entrepôts sont inclus. Les maîtres et la planification globale sont externes par choix de périmètre. La recommandation courante devient **Supply Chain Orchestration**, encore proposée ; SCM reste le cadre plus large. Inventory Planning et les décisions opérationnelles sont conservés. Voir `universe_review_U370` dans l’analyse structurée et C100.

**Accord U373 : Supply Chain Orchestration est adopté et appliqué au nom de l’univers dans le backlog.** Identifiant et périmètre conservés ; les passages U369/U370 ci-dessus retracent les propositions antérieures. Les noms D03/D13 restent à appliquer séparément. [Contrôle du changement](../2026-09-18-universe-U373/implementation.yaml).

**Application U378 :** D03 porte désormais le nom adopté **Fulfillment Optimization** et accueille **Fulfillment Plan Decision** (D03.o). D13 Supply Network reste adopté en attente d’application. Le choix du seul cadre U365/U376 est dépassé par la décision de plan précisée U377 et adoptée U378. [Intégration](../2026-09-18-fulfillment-plan-U378/README.md).

## Résultat

**Fulfillment exprime une finalité utile pour FLOW, mais ne remplace pas Supply partout.** Dans les références consultées, Supply peut désigner les ressources qui répondent à la demande ; Supply Chain désigne le système étendu ; Fulfillment porte la satisfaction des commandes. FLOW utilise en plus Supply comme nom d’un périmètre fonctionnel local. C’est cette polysémie qui crée une part de l’ambiguïté.

Le candidat de renommage le plus intéressant est **D03 Order Promising → Fulfillment Optimization**. Il ne comporte pourtant pas Supply dans son nom : le bénéfice vient de la meilleure expression de sa finalité. Ce changement reste un arbitrage de modèle, avec des frontières à préciser. À l’inverse, remplacer Supply Assignment ou Future Supply Projection changerait ou brouillerait le résultat décrit.

Le glossaire métier a été enrichi selon U367. Aucun domaine, capacité ou comportement n’a été renommé. Les publications et le glossaire méthodologique sont inchangés.

**Réexamen U368 : Supply Network est désormais recommandé pour D13**, avec Supply Network Ingestion pour D13.a. Le référentiel représente la structure partagée du réseau, indépendamment d’un plan de satisfaction. Cette recommandation remplace le maintien de Fulfillment Network initialement proposé ; [l’état précédent est conservé](network-finding-before-U368.yaml).

## Périmètre et méthode

L’autorité examinée est le backlog courant : **99 éléments, 38 capacités et 43 comportements**. L’inventaire parcourt toutes les chaînes du modèle, de ses relations et des deux glossaires. Il sépare le texte métier courant, les comparaisons marché, les identifiants et les preuves historiques. Les conventions Assignment, la proposition U365 et les frontières d’AGENTS.md ont également été relues. Une recherche ciblée couvre les libellés du code Atlas.

Résultat de l’inventaire avant ajout des nouvelles définitions : **8 noms de modèle contenant Supply, 2 contenant Fulfillment** ; **37 éléments** comportent l’un de ces termes dans leurs champs métier. Les deux glossaires et les relations portent aussi des usages qui demandent une lecture contextuelle. Le nombre brut de chaînes contenant un terme ne constitue pas un nombre de renommages : un nom SAP, une URL et une référence historique n’ont pas le même statut qu’un libellé FLOW.

[Inventaire détaillé et empreintes](inventory.yaml) · [Analyse structurée par élément](../../modeles/backlog/supply-fulfillment-audit.yaml) · [Contrôles](checks.json).

Cette étude est locale et ciblée. Elle ne prétend pas établir un consensus de tous les éditeurs ou un audit complet de leur couverture fonctionnelle. Les constats de documentation, interprétations et recommandations FLOW sont distingués ci-dessous.

## Les trois notions, et la convention locale

| Terme | Sens retenu pour la clarification | Exemple fictif | Limite essentielle |
| --- | --- | --- | --- |
| **Supply** — TER083 | Ressources présentes ou attendues qui peuvent répondre à une demande. | 80 pièces en stock et un apport attendu de 40. | Exister ou être attendu ne signifie pas être libre, admissible ou disponible à la bonne date. |
| **Supply Chain** — TER084 | Réseau de parties, activités et flux reliant les sources d’approvisionnement aux destinataires. | Fournisseurs, entrepôts, transporteurs, magasins et clients, avec leurs relations et flux. | Le périmètre dépasse le modèle FLOW ; Supply Chain Management désigne sa gestion. |
| **Fulfillment** — TER085 | Activités organisant et réalisant la satisfaction d’une commande selon les quantités, délais et conditions retenus. | Mobiliser les ressources, préparer puis mettre les pièces à disposition du destinataire. | Un plan calculé, une promesse ou une affectation ne prouve pas la réalisation. |
| **Supply — sens fonctionnel du projet** — TER035 | Convention FLOW historique : couche transactionnelle de contrôle, d’orchestration et d’optimisation de la logistique. | Le périmètre actuellement présenté sous l’univers Supply. | Ce sens local ne doit pas être présenté comme la définition générale de Supply. |

Microsoft Business Central oppose explicitement le côté ressources au côté demande dans la planification. Cette lecture justifie de distinguer Supply de la fonction locale du projet. [Microsoft — Balancing supply and demand](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-balancing-demand-and-supply).

La distinction entre système étendu et activités de fulfillment s’appuie sur les périmètres professionnels de CSCMP et d’ASCM. La définition française du glossaire est une synthèse éditoriale, pas une citation normative. [CSCMP — définitions SCM](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx), [ASCM — Supply chain logistics](https://www.ascm.org/topics/logistics/).

Microsoft emploie Fulfillment pour l’optimisation des choix, mais aussi pour les opérations de magasin. Il faut donc conserver le qualificatif Optimization quand on veut parler de la recherche d’une solution plutôt que de tout son accomplissement. [Microsoft — Intelligent Fulfillment Optimization](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch), [Microsoft — Store order fulfillment](https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview).

**Point de vigilance :** les sources parlent fréquemment de commandes clients. Pour FLOW, l’usage de Fulfillment à propos d’un transfert, d’un achat, d’un retour ou d’une prestation numérique devra préciser le destinataire, le résultat attendu et le point de vue. L’extension n’est pas interdite ; elle ne découle simplement pas d’une équivalence de vocabulaire démontrée. Un retour peut alimenter la Supply du receveur tout en constituant une commande à réaliser : les notions décrivent des dimensions différentes.

## Recommandations par élément

| Élément courant | Recommandation | Motif et limite |
| --- | --- | --- |
| **Supply** — universe-supply | Conserver provisoirement le nom local et expliciter sa définition. | L’univers couvre aussi stock, préparation des apports, achats, retours et références. Le rebaptiser Fulfillment pourrait faire lire tout le modèle comme la seule satisfaction de commandes. Sa définition actuelle est circulaire et mérite une reformulation. |
| **Order Promising** — D03 | **Examiner Fulfillment Optimization en priorité.** | La finalité actuelle est déjà de décider comment satisfaire les Orders. Le domaine comprend aussi priorités, choix économiques, échéancier et affectation : il dépasse la seule émission d’une promesse. Le rapprochement Microsoft est partiel, à adapter à FLOW. |
| **Supply Assignment** — D02.e | Conserver. | Supply désigne les ressources affectées ; Assignment décrit les liens aux commandes. Renommer en Fulfillment Optimization ferait confondre l’application et l’optimisation. Aucun consensus établi ici pour Fulfillment Assignment. |
| **Supply Assignment Plan Application**, **Incremental Supply Assignment**, **Supply Reassignment** — BHV045–047 | Conserver leurs libellés dans cet audit. | Les mécanismes validés distinguent application de plan, stabilité et révision des liens. Ils restent une décomposition de l’affectation. |
| **Supply Protection**, **Group Supply Protection** — D02.b, BHV017 | Conserver ; maintenir les différences marché dans la comparaison. | L’objet protégé est l’accès aux ressources, y compris avant les commandes. FLOW couvre davantage que les seules enveloppes de groupes SAP. Fulfillment Protection suggérerait à tort une garantie de résultat. |
| **Future Supply Projection** — BHV004 | Conserver. | Le comportement prend en compte des ressources futures. Future Fulfillment Projection déplacerait le sens vers un résultat futur de satisfaction. |
| **Fulfillment Network**, **Fulfillment Network Ingestion** — D13, D13.a | **Supply Network / Supply Network Ingestion recommandés U368.** | La représentation de référence des lieux et liaisons sert plusieurs finalités. Le nouveau nom décrit mieux cette structure partagée ; l’ingestion reste une projection externe, sans nouveau maître ni routage calculé. |
| **Supply Order** — TER065 | **Réexaminer ; préférer Order qualifié par son type dans un contexte explicite.** | Le sens générique local diverge de l’usage Microsoft supply order pour les apports. Un remplacement par Fulfillment Order risquerait une autre ambiguïté avec les ordres de réalisation. |
| **Supply Assignment Plan** — TER078 | Conserver ; expliciter « plan d’affectation des ressources aux commandes ». | Il ne décrit pas à lui seul toutes les tâches, prestations et engagements d’un plan de fulfillment. |
| **Inventory Management**, **Inventory Optimization**, **Order Management**, **Execution Management** — D01/D05/D04/D06 | Conserver les noms et frontières. | Contribuer au fulfillment ne transforme pas toutes les responsabilités en une capacité de fulfillment. Les besoins de stock et la satisfaction des Orders restent deux finalités distinctes. |

Les comparaisons sont enregistrées par identifiant dans l’annexe structurée, avec source, passage, version connue et limites. Appuis spécifiques : [SAP — affectation dans BOP](https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html), [SAP — Supply Protection](https://help.sap.com/docs/PRODUCT_ID/32da8359c8ee4e8b8e8c5e15cacba5aa/c4b704762cbd4611a3ee2dc00c7a7277.html?locale=en-US&state=PRODUCTION&version=2602.500), [Microsoft — Inventory allocation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation).

Les noms apparus uniquement dans le code d’icônes, comme Supply Creation Decision ou Expected Supply Tracking, ne sont pas des capacités courantes de ce backlog. Ils ne doivent pas gonfler artificiellement la liste des éléments à renommer.

## Réexamen du référentiel réseau — U368

La définition actuelle de D13 porte les points, caractéristiques et relations du réseau ; elle n’est pas limitée à la recherche d’une source pour une commande. **Supply Network** est donc plus précis pour nommer ce référentiel partagé. Fulfillment désigne la finalité pour laquelle le réseau peut être mobilisé ; il ne faut pas créer deux référentiels concurrents.

SAP F&R 7.0 EHP4 documente explicitement un Supply Network formé de liaisons entre lieux, avec sources internes et fournisseurs externes. C’est un appui direct au vocabulaire, provenant d’une référence historique ; cela ne prouve pas que toutes les caractéristiques envisagées dans FLOW sont couvertes à l’identique. [SAP — Supply Network](https://help.sap.com/docs/SAP_SUPPLY_CHAIN_MANAGEMENT/35d41850ef1d4618a0ce6ffa921e8d6d/01b4c7ac10a64d7791560ac37235fe46.html?locale=en-US&state=PRODUCTION&version=7.0.4).

La page Microsoft utilise elle-même supply network pour le contexte d’ensemble et fulfillment sources pour les lieux mobilisables. Ces sources incluent des fournisseurs en dropship : la différence ne se réduit donc pas à « Supply amont / Fulfillment aval ». [Microsoft — Fulfillment sources](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch).

Définition de référence proposée : **« Représentation de référence des lieux, de leurs caractéristiques et de leurs relations logistiques, décrivant les possibilités d’approvisionnement, de stockage, de transfert, de distribution et de retour des marchandises. »** Les flux et attributs détaillés restent à préciser selon Q076 ; le nom ne crée pas de nouvelles données.

Party décrit les acteurs, D13 les lieux et relations, D14 les services. Stocks, charge effective et parcours retenus restent dans leurs domaines. D13.a reçoit les références de maîtres externes ; aucun droit d’administration du réseau n’est ajouté. D13, D13.a et TER054 restent inchangés tant que le renommage n’est pas adopté.

## Arbitrage prioritaire : D03

**Fulfillment Optimization est une bonne piste de nommage pour D03 ; ce n’est pas un simple remplacement lexical.**

Le domaine comporte actuellement sept capacités : Supply Assignment, ATP, CTP, PTP, Delivery Schedule Decision, Order Prioritization et Promise Management. Supply Assignment est déjà rattachée à D03 malgré son identifiant historique D02.e. Ce rattachement réel doit guider l’analyse, plutôt que le préfixe de l’identifiant.

Proposition de finalité à discuter : **« Rechercher la meilleure satisfaction d’un ensemble d’Orders selon les objectifs, engagements et contraintes applicables. »** La finalité actuelle adoptée reste inchangée pendant cet audit.

Conditions du renommage proposé :

1. Garder ATP, CTP, PTP et les autres décisions spécialisés ; le domaine n’est pas un unique algorithme.
2. Conserver la proposition, la confirmation et la révision des promesses ; Optimization ne doit pas faire disparaître leur gestion.
3. Conserver l’application des affectations comme capacité d’action distincte, sans déplacer tacitement D02.e.
4. Laisser à D05 le stock souhaitable et ses ajustements, à D04 les Orders, à D06 l’orchestration et l’adaptation d’exécution, et aux exécutants les opérations internes.
5. Rendre explicites les objectifs et contraintes ; une règle séquentielle ou proportionnelle ne démontre pas un optimum global de valeur.

Le compromis est un nom plus parlant sur la finalité, mais plus exigeant sur l’explication de son périmètre. Il pourrait sinon laisser croire que le domaine réalise aussi les opérations logistiques ou qu’il garantit une optimisation universelle.

**Fulfillment Strategy Decision demeure une proposition U365**, pas une huitième capacité déjà créée. Son résultat envisagé est le cadre applicable ; il ne faut pas la confondre avec le domaine, le calcul ATP ou l’application du plan.

## Formulations à clarifier ensuite

Il est souvent plus utile de préciser le complément français que de remplacer un mot anglais :

| Formulation rencontrée | Reformulation candidate selon le contexte |
| --- | --- |
| ressources Supply | stocks présents, réceptions attendues ou ressources admissibles, selon ce qui est réellement visé |
| promesse Supply | promesse de satisfaction de l’Order, avec quantités, dates et conditions |
| exécution Supply | exécution des prestations nécessaires à la réalisation des Orders |
| référentiels Supply | référentiels utilisés par le périmètre FLOW concerné ; leur maîtrise externe reste inchangée |
| couche transactionnelle Supply | conserver la convention locale et pointer vers TER035 |

Ces formulations sont des propositions à appliquer champ par champ. Les citations éditeurs, les termes historiques et les libellés approuvés ne sont pas remplacés mécaniquement. La réalisation physique, les services numériques et la traçabilité de D06 restent explicitement couverts.

## Changements réalisés et plan d’action

**Réalisé dans le périmètre demandé :**

- Inventaire complet des occurrences dans les trois YAML courants, classement sémantique et revue des dix noms concernés du modèle.
- Ajout de **TER083 Supply**, **TER084 Supply Chain**, **TER085 Fulfillment**, avec exemples, différences et comparaisons marché.
- Clarification de TER035 par le contexte et les renvois ; son nom, sa définition historique et sa description courte restent identiques.
- Enregistrement des recommandations et de leurs impacts. Les nouvelles formulations restent proposées ; une demande de documentation ne vaut pas validation de chaque définition.

**À travailler ensemble, dans cet ordre :**

1. Appliquer les noms acquis U369 : **D03 → Fulfillment Optimization** et **D13 → Supply Network**, en qualifiant séparément les descriptions et les déclinaisons de nommage.
2. Examiner **Supply Chain Management** pour l’univers, avec une portée FLOW explicite, puis clarifier le devenir de **Supply Order**.
3. Reprendre **Fulfillment Strategy Decision** : responsabilité précise et résultat, avant création éventuelle.
4. Appliquer les décisions aux formulations concernées, aux comparaisons, aux accords de champs et aux restitutions.

Un renommage validé conserve les IDs, notamment universe-supply et D02.e. Il faut actualiser les correspondances d’icônes par nom dans `app/src/icons.tsx` et les tests concernés ; les icônes génériques servent déjà de repli. Les libellés historiques, URLs et snapshots restent figés. Atlas ne reçoit ces évolutions qu’au travers d’une nouvelle publication ; cet audit n’en déclenche aucune.

### Proposition d’univers — U369

**Supply Chain Management** exprime la nature de pilotage du niveau univers et évite le double sens du mot Supply isolé. Le CSCMP lui donne un périmètre étendu de planification et de coordination. Le produit Microsoft porte lui aussi un ensemble plus vaste que notre catalogue courant ; son nom ne commande pas l’importation de ses modules. [CSCMP](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx), [Microsoft](https://learn.microsoft.com/en-us/dynamics365/supply-chain/supply-chain-management-welcome).

Description FLOW proposée : « Piloter et coordonner les ressources, les stocks, les commandes et leur réalisation au sein du réseau, afin de satisfaire les besoins selon les objectifs de service, de coût et de risque. » C’est une description du périmètre cartographié, pas une définition exhaustive du SCM professionnel. Les exclusions actuelles et les responsabilités des exécutants restent explicites. Aucune extension ou complétude du catalogue n’est déduite du nom de l’univers.

## Validation

Les contrôles d’intégrité vérifient l’absence de modification du catalogue, du glossaire méthodologique et de l’index publié, ainsi que la conservation de 125 fichiers publiés ou preuves figées. Ils vérifient aussi que seul TER035 a été enrichi parmi les anciens termes et que ses trois champs historiques principaux sont inchangés. Les résultats de validation du modèle et des tests sont consignés dans `checks.json`.
