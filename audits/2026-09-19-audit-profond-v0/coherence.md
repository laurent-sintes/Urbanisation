# Audit de cohérence sémantique et de préparation de la V0

Date : 19 septembre 2026. Périmètre : backlog courant, sans modification du catalogue ni publication. Cet audit répond à la nouvelle demande explicite de Laurent ; il ne réouvre pas l'audit des comportements clos U431.

**Décisions postérieures à l'instantané audité.** U435 autorise la prise en charge des corrections évidentes ; leur préparation est décrite dans `coherence-fix-plan-U435.md`. U436 précise que seule la réservation bloque les usages concurrents et qu'une affectation seule ne les bloque pas. Le constat COH-04 décrit l'ouverture à l'instantané initial ; ce principe est désormais tranché, tandis que les contrats détaillés d'application restent à préciser. Les mises à jour consolidées sont réalisées et rapportées séparément par le coordinateur.

## Conclusion

Le découpage des responsabilités Supply est solide : les cinq domaines distinguent correctement connaissance et gestion du stock, travail collectif du carnet, demandes par intention, optimisation du stock et orchestration des prestations. Les 47 capacités et 74 comportements ne présentent pas de défaut de rattachement ni de décomposition terminale. La densité supérieure des comportements dans D04 répond à la règle de lisibilité par Order ; elle ne justifie pas de décomposer artificiellement les autres domaines.

Une V0 de discussion avec les PO et experts est atteignable par clarification, sans reconstruction de l'arbre. En revanche, qualifier ce catalogue de modèle de solution complet serait prématuré : les engagements opposables, l'application croisée des changements, certaines autorités de politique et les contrats d'information restent ouverts. Plusieurs sont explicitement différés par U431 et ne constituent pas des capacités manquantes.

Les défauts certains concernent surtout la cohérence du texte courant après des évolutions adoptées : anciennes responsabilités de D03, vieux placements de Structuring, limitations et alternative encore ouvertes, exemples méthodologiques datés, phrases recopiées hors contexte. Ces défauts peuvent induire une erreur de lecture malgré un arbre correct. Les corrections éditoriales proposées doivent préserver les empreintes d'accord et leur portée : une formulation corrigée n'acquiert pas automatiquement l'accord de la précédente.

## Méthode, preuves et limites

Autorité lue : `modeles/backlog/model.yaml`, SHA-256 `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`. Lecture par `scripts.structured_io.read`, avec contrôles en mémoire et sans réécriture. Lecture des définitions et périmètres des cinq domaines, des 47 capacités, des 74 comportements, des six référentiels et des quatre illustrations ; lecture des définitions des 110 entrées du glossaire métier et du glossaire méthodologique. Contrôle des principes, limitations et alternatives du modèle.

Sources de cadrage : `AGENTS.md`, sections métier de `CONVENTIONS-MODELE.md`, `marche/methode.md`. Annexes déterminantes : `behavior-gap-audit.yaml` / `closure_U431`, `consignment-inventory-review.yaml`, `consignment-sales-transfer-review.yaml`, `return-disposition-review.yaml`, `reservation-policy-review.yaml`, `modeling-roadmap.yaml`, `applicability.yaml`. Les règles de clôture et limites y sont traitées comme des informations courantes, sans réactiver leurs propositions historiques remplacées.

Cet axe justifie ses recommandations par la cohérence interne. Il ne revendique aucune équivalence marché nouvelle ni aucun taux de couverture marché ; la recherche externe est instruite dans l'autre axe du présent audit. Une absence de champ, de nœud ou de preuve est qualifiée avant de devenir un défaut. Les scénarios ci-dessous sont des tests de lecture fictifs, pas des observations Beaumanoir.

### Contrôles structurels exécutés

| Contrôle | Résultat |
| --- | --- |
| 74 comportements rattachés à une capacité unique | Conforme |
| Même couche parent/enfant | Conforme |
| Aucun enfant sous un comportement | Conforme |
| Justification sur chaque capacité décomposée | 22 sur 22 |
| Capacités sans comportement | 25 ; absence non assimilée à un manque |
| Domaines / référentiels | 5 domaines ; 6 référentiels et leurs 6 ingestions |
| Objets, documents, événements | 4 illustrations explicites, dont 1 dans Business Services |
| Homonymes de comportements | 5 paires intentionnelles à contextualiser |
| `fields.nature` sur les capacités | 37 renseignées sur 47 ; 10 absences éditoriales |

Ces contrôles complètent l'audit sémantique ; ils ne remplacent ni les validations de schéma effectuées dans l'axe technique, ni la qualification des accords champ par champ.

## Matrice exhaustive du catalogue

La matrice est une vue d'audit de l'instantané désigné ci-dessus, pas un second catalogue d'autorité. Les identifiants historiques sont conservés ; les parents proviennent des relations `contains`.

| Périmètre | Capacités | Comportements | Lecture |
| --- | ---: | ---: | --- |
| D01 Inventory Management | 7 | 10 | Responsabilités cohérentes ; réserves détaillées ci-dessous |
| D03 Order Backlog Management | 11 | 14 | Responsabilités cohérentes ; réserves détaillées ci-dessous |
| D04 Order Management | 7 | 29 | Responsabilités cohérentes ; réserves détaillées ci-dessous |
| D05 Inventory Optimization | 8 | 17 | Responsabilités cohérentes ; réserves détaillées ci-dessous |
| D06 Process Management | 8 | 4 | Responsabilités cohérentes ; réserves détaillées ci-dessous |
| Business References | 6 | 0 | Projections de maîtres externes, pas six domaines opérationnels |

### D01 — Inventory Management

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D01.f Inventory Tracking | Aucun ; ne vaut pas manque | État reconnu et ressources futures distincts ; connaissance des attendus à contractualiser (A07). |
| D01.g Record Inventory Movements | Aucun ; ne vaut pas manque | Journal des faits et justifications, y compris changement de propriété sans déplacement ; cohérent. |
| D01.c Inventory Visibility | Aucun ; ne vaut pas manque | Lecture transverse, provenance et fraîcheur ; distincte des faits suivis par D06. |
| D01.d Stocktaking | BHV029, BHV030, BHV031 | Trois politiques utiles ; rapprochement commun ; exécution physique externe ; cohérent. |
| D02.b Supply Protection | BHV017, BHV018, BHV019, BHV020 | Quatre mécanismes distincts ; application des décisions D05 ; cohérent. |
| D02.c Reservation | Aucun ; ne vaut pas manque | Engagement individuel distinct de lien d’affectation ; effet opposable ouvert A01 (COH-04). |
| D01.h Consigned Inventory Management | BHV063, BHV064, BHV065 | Régime de propriété et obligations distincts de l’apport ; choix du devenir ouvert (COH-06), phrase copiée (COH-02). |

### D03 — Order Backlog Management

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D02.e Supply Assignment | BHV045, BHV046, BHV047 | Application des affectations et trois mécanismes utiles ; responsabilité de structure périmée (COH-01), effets ouverts A01/A03. |
| D03.i Available-to-Promise (ATP) | BHV001, BHV002, BHV003, BHV004 | Faisabilité dans la référence, quatre dimensions justifiées ; aucune réservation implicite. |
| D03.j Capable-to-Promise (CTP) | BHV075, BHV076, BHV077 | Faisabilité sous adaptation ; trois leviers, responsabilités spécialisées conservées ; cohérent. |
| D03.k Profitable-to-Promise (PTP) | Aucun ; ne vaut pas manque | Arbitrage économique distinct de faisabilité ; articulation au choix collectif à illustrer (COH-11). |
| D03.l Delivery Schedule Decision | Aucun ; ne vaut pas manque | Échéancier retenu distinct des dates possibles et du changement de date demandée ; cohérent. |
| D03.m Order Prioritization | Aucun ; ne vaut pas manque | Priorités relatives distinctes de droits de groupe ; définition seule peu explicative (COH-07/11). |
| D04.n Order Structuring | BHV044 | Split et composition persistante ; seul Split décomposé avec justification ; rattachement D03 correct. |
| D03.n Promise Management | BHV021, BHV022, BHV023 | Proposition, confirmation et révision explicitement distinctes ; effets de garantie ouverts A01/A07. |
| D04.q Order Archiving | Aucun ; ne vaut pas manque | Historique distinct de clôture et purge ; rattachement D03 correct ; pas de durée légale inventée. |
| D03.o Fulfillment Plan Decision | Aucun ; ne vaut pas manque | Scénario collectif cohérent, distinct de stratégie et application ; articulation des choix (COH-11). |
| D03.p Order Backlog Planning | Aucun ; ne vaut pas manque | Préparation/maintien des scénarios ; aucun comportement requis par symétrie à D05.f. |

### D04 — Order Management

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D04.i Sales Order | BHV066, BHV067, BHV068, BHV069 | Quatre variantes combinables ; client, document et capacité distingués ; ancien nom D03 (COH-01). |
| D04.j Purchase Order | BHV058, BHV059, BHV060, BHV078 | Biens, service et engagement fournisseur explicites ; pas d’achat obligatoire pour chaque service. |
| D04.k Transfer Order | BHV070, BHV071, BHV072, BHV073, BHV074 | Cinq intentions de transfert ; distinctes de la décision D05 ; résidus éditoriaux (COH-01/02). |
| D04.l Customer Return | BHV050, BHV051, BHV052, BHV053, BHV054 | Cinq suites logistiques ; devenir, remboursement et exécution distincts ; interface commerciale A04. |
| D04.m Supplier Return | BHV055, BHV056, BHV057 | Avoir, remplacement et même bien réparé distingués ; pas de double compte des remplacements. |
| D04.o Order Lifecycle Management | BHV036, BHV037, BHV038, BHV039, BHV040, BHV043 | Six dimensions combinables ; pas de statut universel ; changement de contenu et réalisations acquis distingués. |
| D04.r Consignment Replenishment Order | BHV061, BHV062 | Apport sans achat ; implantation et continu rendus lisibles ; prise en charge fournisseur à éprouver selon contexte. |

### D05 — Inventory Optimization

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D05.a Inventory Target Decision | BHV026, BHV027, BHV028 | Cibles magasin, distribution et réseau distinctes ; pas de hiérarchie forcée ; P12 couvert U431. |
| D05.d Group Protection Decision | Aucun ; ne vaut pas manque | Droits de groupe et plafond distincts d’affectation ; mise en vigueur D02.b identifiée. |
| D05.e Replenishment Decision | BHV083, BHV084, BHV085 | Deux politiques + ajustement combinable ; recommandations distinctes d’Orders ; cohérent. |
| D05.c Stock Redistribution Decision | BHV024, BHV025 | Rééquilibrage et concentration, contraintes donneurs ; définitions courtes à contextualiser (COH-07/08). |
| D05.f Inventory Planning | BHV005, BHV006, BHV016 | Construction, simulation/analyse et adaptation de scénario ; application via responsables distincts. |
| D05.g Initial Stocking Decision | Aucun ; ne vaut pas manque | Apports de lancement distincts de cible et réassort ; assortiment externe ; périmètre magasin explicite. |
| D05.h Reservation Policy Decision | BHV032, BHV033, BHV034, BHV035 | Quatre politiques/mécanismes justifiés ; porteur de mise en vigueur ouvert (COH-05). |
| D05.i Return Disposition Decision | BHV048, BHV049 | Devenir du retourné, deux stratégies ; ne couvre pas automatiquement tous les excédents (COH-06). |

### D06 — Process Management

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D06.b Service Capacity Visibility | Aucun ; ne vaut pas manque | Capacité contextualisée, fraîcheur ; plafond ≠ disponible ; contrat A07. |
| D07.a Service Requirements Decision | Aucun ; ne vaut pas manque | Besoin de prestations distinct du choix du service ; définition courte (COH-07). |
| D07.b Service Order Management | Aucun ; ne vaut pas manque | Demande, acceptation et engagement de prestation ; distinct de Purchase Order et résultat réalisé. |
| D07.c Service Reconciliation | Aucun ; ne vaut pas manque | Rapprochement prestation distinct du reliquat Order et du rapprochement financier ; cohérent. |
| D07.d Operations Tracking | BHV079, BHV080, BHV081, BHV082 | Trois perspectives physiques et suivi du processus ; exception P10 déjà couverte U431. |
| D06.d Process Orchestration | Aucun ; ne vaut pas manque | Coordination et dépendances ; adaptation distincte ; P04 couvert sans nouveau comportement. |
| D06.e Service Selection Decision | Aucun ; ne vaut pas manque | Choix de service/exécutant distinct de promesse ; fusion reste proposée, ne pas reprendre l’accord des anciens éléments. |
| D06.f Process Adaptation Decision | Aucun ; ne vaut pas manque | Variation opérationnelle distincte du scénario D05 et de la promesse D03 ; définition courte (COH-07). |

### D09 — Party / Role

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D09.d Party / Role Ingestion | Aucun ; ne vaut pas manque | Projection externe ; Party, Role et habilitation distingués ; pas de maître précis présumé. |

### D11 — Agreement

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D11.a Agreement Ingestion | Aucun ; ne vaut pas manque | Accords externes, engagements et périodes ; commande distincte de contrat. |

### D08 — Product Reference

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D08.d Product Reference Ingestion | Aucun ; ne vaut pas manque | Product/Variant distincts de Product Unit ; Article/Container rôles ; SKU/conditionnements à préciser. |

### D12 — Catalog

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D12.a Catalog Ingestion | Aucun ; ne vaut pas manque | Offre commerciale projetée, produit indépendant ; pas de gouvernance prix locale. |

### D13 — Fulfillment Network

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D13.a Fulfillment Network Ingestion | Aucun ; ne vaut pas manque | Lieux et relations distincts des parties et capacités actuelles ; maître externe à identifier. |

### D14 — Service Catalog

| Capacité | Comportements directs | Appréciation |
| --- | --- | --- |
| D14.a Service Catalog Ingestion | Aucun ; ne vaut pas manque | Offre, SLA et accès distincts de charge, engagement et résultat ; maître et articulation Agreement ouverts. |

## Constats détaillés

### COH-01 — Le texte courant garde des responsabilités et états remplacés

**Nature : défaut de cohérence éditoriale avéré. Priorité : corriger avant la V0 présentée.**

Preuves :

- D01 `fields.definition` / `scope`, D04.i / D04.k `scope`, D05 `scope` et D05.c `scope` parlent encore d'`Order Promising` comme nom ou périmètre de D03. Trois liens explicites `[Order Promising](model:D03)` affichent ce nom ancien ; D03 est désormais Order Backlog Management et son mandat est plus large.
- BHV045, BHV046 et BHV047 disent que modifier le contenu, l'état **ou la structure** d'un Order mobilise les responsabilités D04. Le placement courant U417/U420 affecte Structuring D04.n à D03, Lifecycle D04.o à D04. L'arbre est correct, mais cette phrase attribue incorrectement la structure.
- `alternatives[D03-BACKLOG-DOMAIN-U158].state` reste `proposed` avec Backlog Management, alors qu'U413 adopte Order Backlog Management et sa frontière.
- `limitations[-1]` présente encore Stocktaking / Orchestration comme décompositions conditionnelles et le rattachement du comportement transverse D04 comme à instruire. Stocktaking porte déjà trois comportements U334 ; P04 est couvert sans nouveau comportement par U431 ; Lifecycle / Split sont explicitement placés.
- `PRINCIPLE-SUPPLY-DOCUMENTS` garde « Supply générique orientée documents d'autorisation » U100. Ce texte doit être contextualisé avec l'approche par intention U393/U394 : les documents ERP ne dictent plus le découpage. Ce n'est pas une invitation à supprimer la notion de document ou le principe de séparation des couches.
- BHV060 parle encore d'une « définition actuelle centrée sur les biens », alors que Purchase Order inclut explicitement biens et prestations U391. D02.e renvoie encore la « décision collective » à A02, alors que Fulfillment Plan Decision D03.o existe ; les contrats détaillés demeurent, eux, ouverts.

**Impact :** un PO ou un architecte peut tirer deux frontières différentes selon la fiche consultée, ou croire qu'un arbitrage déjà traité reste ouvert.

**Action proposée :** préparer un lot éditorial ciblé avec chaque formulation remplacée, sa référence courante et sa portée. Conserver l'alternative U158 et les textes antérieurs dans l'historique ; qualifier leur succession dans les données courantes. Ne pas remplacer tous les noms historiques dans les preuves, citations marché ou archives.

**Critère de sortie :** aucune fiche courante n'attribue la structure à D04 ; les statuts ouverts désignent un vrai arbitrage restant et chaque nom de domaine courant pointe sur le bon mandat.

### COH-02 — Une explication de la vente a été copiée dans la consignation et les transferts

**Nature : défaut éditorial avéré. Priorité : V0.**

La phrase « Intercompany est un axe de relation commerciale ; les autres parcours décrivent principalement le mode de satisfaction » figure dans 15 périmètres. Elle est pertinente sous Sales Order et ses quatre comportements. Elle est hors contexte dans **10 fiches** : D01.h, D04.k, BHV063–065 et BHV070–074. Les comportements de la consignation différencient des effets de propriété / sortie ; les comportements de transfert distinguent l'intention d'apport ou de déplacement. Ils ne sont pas un ensemble « Intercompany versus modes de satisfaction ».

**Impact :** les critères de décomposition, pourtant valables, deviennent difficiles à expliquer aux experts. Cette phrase peut faire supposer un comportement Intercompany absent sous le transfert, alors que la distinction vente intersociétés / déplacement de lieu est voulue.

**Action proposée :** remplacer uniquement la phrase hors contexte par la justification propre à chaque capacité. Le rappel de non-exclusivité et de non-double-compte peut rester s'il est formulé dans le contexte de la fiche. Aucun changement de nom, de parent ou de comportement n'est requis.

### COH-03 — Les exemples méthodologiques ne reflètent plus le catalogue courant

**Nature : dette de cohérence des instructions de lecture. Priorité : V0.**

`modeling-glossary.yaml` / MOD006 conserve :

- une note U282 affirmant que la nouvelle décomposition Supply Protection reste à proposer, alors que BHV017–020 sont intégrés ;
- une note et l'exemple `business_scope` présentant Warehouse / Transportation / Store Visibility comme non intégrés, alors que BHV079–081 existent ;
- l'exemple `business_effect` qui situe Drafting, Rescheduling, Cancellation, Closure et Splitting BHV036–044 sous Lifecycle. U424 a remplacé cette présentation par six dimensions ; BHV041 et BHV042 sont retirés et Split BHV044 est sous Structuring depuis U417.

**Impact :** la source pédagogique prescrite pour créer les prochaines propositions peut reproduire une structure retirée. Les formulations datées dans une analyse historique sont légitimes ; dans la liste d'exemples actifs de MOD006, leur statut historique doit être explicite.

**Action proposée :** actualiser les exemples actifs et conserver les exemples U389 comme photographie historique clairement datée. La liste des formes reste une aide non exclusive, pas une classification obligatoire des comportements. Cette maintenance ne réouvre pas l'audit U431.

### COH-04 — Les engagements et leurs effets concurrents restent à contractualiser

**Nature : décisions ouvertes déjà connues, non défaut du catalogue. Priorité : atelier de contrats avant conception de solution.**

La distinction ATP / CTP / affectation / réservation / promesse / firming / freezing / release est présente et utile. Elle ne suffit pas encore à exécuter des modifications cohérentes.

Preuves : `closure_U431.future_work` A01 (effet d'une affectation sur les usages concurrents), A03 (objets modifiés par le plan), A07 (états, unités, horizons, dates rendant une capacité engageable). D02.c Reservation a une définition et un exemple courts ; D03.i/BHV001 interdisent le double compte sans fixer les règles exactes. BHV045–047 appliquent un plan sans transaction atomique universelle, à raison ; le comportement en cas d'application partielle reste à contractualiser. D06.b ne transforme pas implicitement un plafond communiqué en disponible, également à raison.

**Questions minimales à poser aux experts et architectes :**

1. Quel fait empêche une même quantité ou capacité de soutenir deux engagements incompatibles ? Quelle autorité le constate ?
2. Quelle règle maintient ou remplace une réservation quand source, lot, date, promesse ou portée changent ?
3. Comment expose-t-on un plan accepté mais partiellement appliqué, et quelles décisions reprennent les écarts ?
4. Quelles informations rendent un stock futur crédible et une capacité de service réellement engageable, à quelle date et pour combien de temps ?
5. Comment traite-t-on une annulation pendant préparation : besoin retiré, réservation libérée, affectation révisée, service annulé et constat physique sont-ils tous explicités ?

**Action proposée :** produire des contrats métier courts sur des exemples quantifiés, avec entrées, résultat, préconditions, effets, motifs de refus et retour d'écart. Ne pas imposer une base de données, une atomicité globale ou un workflow universel. L'atelier peut accompagner la V0 ; sa conclusion n'est pas nécessaire pour considérer le catalogue clos.

### COH-05 — Le responsable de mise en vigueur des politiques de réservation est ouvert

**Nature : responsabilité à arbitrer déjà identifiée. Priorité : V0 visible, résolution avant réalisation.**

D05.h `scope` distingue la décision de politique de sa gouvernance et précise que le porteur de management est « à arbitrer ». `reservation-policy-review.yaml.open_questions` le confirme. Reservation applique et maintient les engagements individuels ; Supply Protection gouverne déjà des droits de groupe, tampons et règles de renouvellement. On ne peut attribuer automatiquement à l'un ou à l'autre la mise en vigueur d'un régime de réservation.

**Impact :** la chaîne « politique recommandée → version applicable → effet sur les futures réservations → sort des engagements déjà accordés » n'a pas encore de responsable complet explicite.

**Action proposée :** choisir le porteur, puis préciser version, portée, période d'effet, source d'autorité, exceptions et politique de repli. Une clarification de périmètre et une relation peuvent suffire ; aucune capacité supplémentaire n'est démontrée nécessaire. Préserver la règle selon laquelle un changement de politique ne retire pas silencieusement les garanties existantes.

### COH-06 — Le choix du devenir du stock consigné n'est pas attribué pour tous les cas

**Nature : lacune de responsabilité explicitement ouverte, distincte d'une absence de prise en charge. Priorité : V0 visible.**

D01.h et BHV065 Consignment Exit appliquent une issue autorisée ; ils ne choisissent pas la meilleure issue. D05.i définit le devenir d'un **produit retourné**. D05.c décide des transferts, sans absorber destruction, liquidation ou politique commerciale. `consignment-inventory-review.yaml.responsibility_boundaries` précise : « Articulation avec D05 à instruire ; Return Disposition Decision ne couvre pas automatiquement tous les excédents. »

**Cas révélateur :** un reliquat consigné toujours détenu doit aller au fournisseur, à une filière seconde main ou à une autre issue autorisée. Il n'est pas nécessairement issu d'un Customer Return ni déjà en Supplier Return. Les Orders et prestations peuvent porter l'issue ; l'autorité qui la retient n'est pas attribuée pour tout le périmètre.

**Action proposée :** arbitrer la frontière entre décision Supply sur le devenir logistique et décision commerciale externe. Éprouver d'abord une articulation avec les capacités existantes ; ne pas élargir silencieusement Return Disposition Decision ni créer un Inventory Disposition Decision par analogie. L'interface externe peut être la bonne réponse selon le cas.

**Limite :** ce point est déjà identifié dans l'annexe ; il ne prouve pas que la clôture U431 est invalide ni qu'un service nécessaire n'existe pas dans le SI.

### COH-07 — Des fiches courtes exposent mal la responsabilité lorsqu'elles sont lues seules

**Nature : dette de présentation, pas défaut systématique de maille. Priorité : V0.**

Quatre définitions de capacité comptent moins de dix mots : D03.m Order Prioritization ; D07.a Service Requirements Decision ; D06.d Process Orchestration ; D06.f Process Adaptation Decision. Les deux dernières parlent de « prestations » ou de « plan » sans contexte dans la définition ; leurs `scope` rétablissent le sens. D06.f pourrait désigner n'importe quelle adaptation de plan si une vue compacte n'affiche que nom et définition.

Les définitions de BHV024 et BHV025 emploient « Déplacer » / « Regrouper » alors qu'il s'agit de décisions ; le périmètre l'explique explicitement. Les définitions BHV075–077 sont formulées comme des résultats (« Les possibilités… »), et BHV079–081 comme des périmètres d'information. Ces différences sont compatibles avec MOD006 ; leur lecture nécessite le parent et la nature.

`fields.nature` est absent sur D01.f, D01.g, D01.c, D01.d, D02.c, D09.d, D11.a, D08.d, D12.a et D13.a. Il ne faut pas déduire leur nature d'un préfixe ou d'une fonction produit. La présence de `nature` dans 37 autres capacités rend néanmoins l'asymétrie visible.

**Action proposée :** compléter quelques définitions pour qu'elles précisent résultat et objet, avec une proposition de qualification de nature à valider. Afficher toujours le parent des comportements dans les supports PO. Ne pas fabriquer des comportements pour compenser une fiche courte.

### COH-08 — Les homonymes sont utiles, mais leur présentation doit montrer l'intention et le parent

**Nature : risque de lecture ; pas un doublon à fusionner. Priorité : V0.**

| Même nom | Contextes distincts | Distinction à afficher |
| --- | --- | --- |
| Direct Delivery | BHV059 achat / BHV068 vente | Engagement fournisseur / attendu client, une même livraison possible |
| Initial Stocking | BHV061 consignation / BHV070 transfert | Apport fournisseur sans achat / déplacement d'implantation |
| Continuous Replenishment | BHV062 consignation / BHV071 transfert | Demande fournisseur / transfert courant |
| Inventory Rebalancing | BHV024 décision D05.c / BHV072 Transfer Order | Choisir le transfert / gérer sa demande et sa satisfaction |
| Stock Consolidation | BHV025 décision D05.c / BHV073 Transfer Order | Choisir le regroupement / porter les transferts retenus |

L'usage de noms courts pour Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return est une convention U384 ; l'objet reste distinct de la capacité. Afficher leur nature et la phrase d'action évite de prendre la carte pour une liste de documents ERP.

**Action proposée :** montrer un fil « domaine → capacité → comportement », le résultat attendu et le lien qualifié vers l'autre perspective. Ne pas renommer ni fusionner automatiquement. Cette distinction constitue un bénéfice de la structure, lorsqu'elle est visible.

### COH-09 — La preuve d'applicabilité ne doit pas être confondue avec la couverture cible

**Nature : manque de preuve structurée, pas défaut fonctionnel. Priorité : V0 visible.**

`applicability.yaml.assessments` est vide ; Beaumanoir historique et Boardriders sont `to_structure`, Sarenza `not_assessed`, FLOW cible `to_structure`. De nombreux exemples des fiches sont explicitement fictifs. Certains constats rapportés sont précis, par exemple réassort magasin guidé par seuils et contexte des deux saisons ; ils ne valident pas toutes les variantes cibles décrites autour d'eux.

**Action proposée :** joindre à la V0 un cartouche distinct pour cible, pertinence métier, couverture documentée et réalisation installée. L'atelier peut commencer avec « non évalué » et un propriétaire de vérification. Aucun pourcentage de couverture Beaumanoir ou Sarenza ne peut être inféré de ce catalogue. L'existant doit être instruit depuis le panorama As Is et les sources concernées, sans reconstruire son autorité dans ce rapport.

### COH-10 — Le catalogue ne contient pas encore un modèle d'information ni les processus Business Services

**Nature : exclusion / travail différé volontaire. Priorité : cadrage de la présentation.**

Les seuls objets, document et événement instanciés sont ILL-OBJ-01 Engagement de fourniture, ILL-DOC-01 Confirmation de promesse, ILL-EVT-01 Promesse confirmée et ILL-OBJ-02 Demande de réassort. Ils sont explicitement illustratifs. Les domaines de Business Services sont différés. Les fiches parlent d'Order, version, ligne, quantité, promesse, ressource, prestation, Task, fait et état ; ces notions ne constituent pas encore un réseau complet d'objets avec invariants et autorités.

**Impact :** un architecte peut utiliser la V0 pour comprendre les responsabilités, mais pas en déduire directement les agrégats, services, flux, cardinalités, ownership ou séquences de traitement. Une capacité n'est pas automatiquement un bounded context.

**Action proposée :** présenter une carte de capacités accompagnée de quelques contrats et récits de bout en bout. Identifier séparément les objets et événements à instruire ; ne pas les ajouter sous les comportements ni inventer les domaines Business Services pour compléter visuellement la carte.

### COH-11 — La frontière entre hypothèses, choix spécialisés et arbitrage collectif mérite un exemple commun

**Nature : risque d'interprétation, pas doublon de capacité démontré. Priorité : atelier V0.**

D03.i établit les possibilités de référence ; D03.j établit les possibilités après adaptation ; D03.k compare et sélectionne selon les conséquences économiques ; D03.l choisit un échéancier ; D03.m établit les priorités ; D03.o retient le scénario collectif cohérent à valeur multidimensionnelle ; D02.e matérialise les affectations. D03.p prépare et maintient les scénarios avec les décisions. Cette finesse est voulue et utile, mais des formulations « choisir », « sélectionner » et « maximiser » à plusieurs endroits peuvent sembler prescrire plusieurs optimiseurs concurrents.

**Action proposée :** documenter un même cas où priorité, coût, risque et service conduisent à des préférences différentes : quels résultats chaque décision livre-t-elle, lesquels sont contraintes, propositions ou choix applicables, et qui renvoie une impossibilité ? D03.o garde la cohérence collective ; il ne doit pas être interprété comme autorisé à lever seul un gel, une réserve ou un accord. D02.e poursuit une finalité de valeur par application des choix, sans absorber l'arbitrage.

**Limite :** une formule de valeur, des pondérations fixes, un algorithme global et un appel systématique à toutes les décisions ne sont ni nécessaires à la V0 ni adoptés. L'absence de KPI formalisés limite l'évaluation des scénarios, pas l'existence des capacités.

### COH-12 — Le glossaire métier conserve des strates méthodologiques et historiques

**Nature : bruit de présentation et de recherche. Priorité : modérée.**

Le glossaire métier contient notamment Capacité métier TER001, Objet métier TER002, Processus TER024, Opération métier TER025, Réalisation d'une capacité TER026, Fonction TER027, Fonctionnalité de produit TER028, Regroupement de capacités TER029 et Domaine TER030, ainsi que des verbes. Le glossaire méthodologique MOD001–006 existe séparément et précise explicitement qu'aucune reclassification exhaustive des anciens termes n'a été réalisée.

**Action proposée :** organiser la lecture V0 et qualifier les entrées historiques sans migration automatique d'identifiants. Ne pas présenter le glossaire méthodologique comme glossaire métier, ni supprimer des termes cités dans les publications. L'enjeu est de retrouver facilement Stock, Ressource attendue, Engagement, Affectation, Réservation, Promesse, Order et Service dans le contexte approprié. Les synonymes historiques ne justifient pas un renommage automatique.

## Épreuve de complétude par parcours

Les parcours ci-dessous vérifient que les résultats essentiels disposent d'une responsabilité ou d'une frontière explicite. Ils ne démontrent pas des règles détaillées déjà adoptées ni une couverture installée. Une flèche décrit une dépendance de lecture, pas une séquence d'exécution universelle.

| Parcours fictif | Responsabilités retrouvées | Question ou limite restante |
| --- | --- | --- |
| Vente 100, ressource admissible 60 et arrivage 40 | D04.i ; D03.i/j/o/l/n ; D02.e/c ; D04.o ; D06 | Opposabilité de l'attendu et effets concurrents A01/A07 |
| Deux Orders se disputent les mêmes 100 unités | D03.m/k/o ; D02.b/c ; D02.e | Arbitrage collectif explicite, pas deux ATP isolés |
| Client web retire en magasin | BHV067 ; D03 ; D06 ; D01 | Prêt / retiré / non-retrait et preuve de remise, sans règle universelle de paiement |
| Fournisseur livre directement le client | BHV059 et BHV068 ; BHV078 ; D03 ; D06 | Cohérence des engagements et des faits sans dupliquer le stock |
| Vente intersociétés avec livraison directe | BHV069 combiné à BHV068 ; D04.j ; Agreement | Finance et fiscalité externes ; relation commerciale distincte du mouvement |
| Implantation saison en magasin | D05.a/g/f ; D04.k/BHV070 ou D04.r/BHV061 ; D03 ; D06 | Assortiment / saison en entrée ; manque résiduel explicite |
| Réassort puis réduction d'un apport engagé | D05.e/BHV083–085 ; D04/Lifecycle ; BHV078 ; D03 ; D06 | Refuser un report n'annule pas sa réalité ; contrats d'application |
| Rééquilibrage et regroupement de tailles | D05.c/BHV024–025 ; D04.k/BHV072–073 ; D06 | Préservation des besoins du donneur et comparaison bénéfice/coût |
| Comptage contredit le stock connu | D01.d/BHV029–031 ; D01.g/f/c ; exécutant | Politique d'acceptation / recomptage et justification de correction |
| Annulation après expédition partielle | D04.o/BHV043 ; D02.e/c ; D03.n ; D06 | Ce qui est réalisé reste acquis ; effets croisés à contractualiser |
| Retour client avec réparation puis restitution | D04.l/BHV051/053 ; D05.i ; D06 ; D01 | Autorisation commerciale externe ; même bien versus remplacement |
| Retour fournisseur pour remplacement ou réparation | D04.m/BHV056/057 ; D04.j si achat ; D06 ; D01 | Ne pas créer deux ressources futures pour le même remplacement |
| Consignation : apport, acquisition puis sortie de reliquat | D04.r ; D01.h/BHV063–065 ; D04.j/m/i/k selon issue | Le choix du devenir hors produit retourné reste à attribuer (COH-06) |
| Document produit mais dépôt en échec | D07.d/BHV082 ; D06.d/f ; D07.b/c | Réussite technique ≠ résultat métier ≠ Task terminée |
| Capacité entrepôt annoncée puis panne | D14 ; D06.b/e/f/d ; D03.j/n | SLA, plafond, disponible, engagement et constat restent distincts |
| Fin d'Order puis conservation historique | D04.o/BHV043 ; D04.q dans D03 | Clôture, archive, version restaurée et purge ne sont pas synonymes |

### Ce qui ne justifie pas une capacité manquante

- Absence de domaine WMS, TMS, atelier ou opérations magasin : les exécutants gardent leurs opérations internes ; le modèle peut orchestrer, connaître et rapprocher leurs prestations.
- Absence de Demand Planning, assortiment commercial ou planification de saison : les prévisions, objectifs et assortiments sont des entrées externes selon le périmètre courant. L'interface doit être décrite ; leur création ne doit pas être absorbée silencieusement.
- Absence de finance, paiement, négociation, conformité ou assurance comme domaines : frontières externes explicites. Leurs autorisations, faits et conditions utiles doivent être identifiables, conformément à A04.
- Absence de nouveau comportement pour exception transverse P10, orchestration P04 ou cible P12 : couverts U431 ; aucun nouvel écart démontré par leur absence comme boîtes autonomes.
- Absence de comportement pour chaque opération de modification, interface ou seuil : conforme à U265 et MOD006.
- Absence de capacités de CRUD des maîtres : les six référentiels sont des projections ; la qualité et l'acceptation d'une projection peuvent nécessiter un contrat sans transférer l'administration du maître.

### Points à éprouver sans les déclarer manquants

La définition D05.g vise les magasins alors que les capacités d'Orders peuvent porter des apports plus génériques ; la constitution initiale d'autres lieux relève d'une applicabilité à clarifier si le besoin existe. BHV071 parle d'une ressource « déjà présente ailleurs dans le réseau » : un transfert planifié sur arrivage futur mérite une clarification si ce scénario est requis, sans déduire une obligation de stock présent à partir de cet exemple. Supplier Confirmation est explicite sous Purchase Order ; le traitement des engagements d'apport consigné doit être éprouvé dans son propre contexte avant de proposer un comportement par simple symétrie. Ces questions ne sont pas des défauts certains ni des extensions adoptées.

## Proposition de paquet V0

1. Une carte des cinq domaines et six référentiels, montrant les frontières externes et les couches. Conserver les noms et identifiants adoptés.
2. Les 47 fiches en lecture homogène : question / responsabilité, résultat, frontière et exemple. Afficher la capacité parente pour les comportements, notamment les cinq paires d'homonymes.
3. Un lot de corrections éditoriales COH-01 à COH-03, puis des clarifications ciblées COH-07 / COH-12, avec qualification des champs changés.
4. Les parcours ci-dessus, en priorité vente concurrente, réassort ajusté, retour réparé et consignation, pour la revue métier.
5. Une page de décisions ouvertes : A01/A03/A04/A07, gouvernance de réservation, choix du devenir consigné et interfaces de données ; responsables d'atelier à désigner, sans inventer les détenteurs de données ou les logiciels.
6. Une qualification explicite « modèle de capacités cible pour revue » et « réalisation / applicabilité à vérifier ». La V0 n'est ni une cartographie de déploiement validée ni un modèle d'information exhaustif.

Le principal risque de la V0 n'est pas un manque massif de capacités. C'est l'écart entre la précision apparente des fiches et la maturité variable de leurs accords, formulations et contrats. Rendre cette maturité visible et retirer les contradictions datées apporte plus de valeur immédiate qu'une nouvelle couche de décomposition.
