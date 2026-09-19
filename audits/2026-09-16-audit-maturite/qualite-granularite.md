# Qualité des descriptions et granularité des capacités — U249

Audit du 16 septembre 2026. Base : **v007, publication `2026-09-16.2`**, modèle publié [model.yaml](../../modeles/release/2026-09-16.2/model.yaml). Lecture des 41 capacités et de leurs champs publiés, complétée par les règles consolidées d’[AGENTS.md](../../AGENTS.md), le [glossaire de modélisation](../../modeles/backlog/modeling-glossary.yaml), la [revue D03](../../modeles/backlog/d03-review.yaml) et les [cas de stock unifié et de conditionnement](../../modeles/backlog/unified-inventory-packaging.yaml). Les compléments de contexte ne sont pas traités comme du texte déjà publié.

**Conclusion : le découpage est nettement plus mûr que son homogénéité documentaire.** Les définitions récentes D04–D06 permettent de comprendre un résultat, un exemple et ses limites. D01 et D03 demeurent majoritairement des descriptions courtes : leur lecteur doit reconstruire les échanges entre capacités et connaître les conversations antérieures. La priorité est de compléter ces contrats métier et d’arbitrer les ambiguïtés de type, avant d’ajouter ou de fusionner des capacités.

Cet audit ne modifie ni le modèle ni ses validations. Les formulations ci-dessous sont des **propositions**, y compris lorsqu’elles complètent une définition adoptée. Les exemples sont fictifs ; ils ne décrivent ni un déploiement ni une règle Beaumanoir. Les capacités sont retrouvées par leur identité et leur rattachement explicite : D02.b/D02.c appartiennent à D01, D02.e à D03 et les identifiants D07.* appartiennent à D06.

## Méthode et constats vérifiables

La grille distingue quatre questions, sans note globale ni pondération arbitraire :

1. **Résultat** : peut-on dire ce que la capacité produit ou tient à jour, et à quoi cela sert ?
2. **Contrat métier** : comprend-on les informations mobilisées, le résultat transmis, les frontières et les responsabilités voisines ? Il ne s’agit pas d’imposer des API ou un schéma d’objet.
3. **Exemple situé** : un cas présente-t-il une situation, l’intervention de la capacité et un résultat interprétable ? Une liste « réception, sortie, transfert » illustre un vocabulaire, mais ne constitue pas un cas d’application complet.
4. **Granularité par famille** : une décision répond-elle à une question métier identifiable ? Une action ou une gestion couvre-t-elle un résultat durable ou un cycle utile, sans devenir une simple commande d’écran ? Plusieurs calculs ou modalités techniques ne suffisent pas à créer plusieurs capacités.

Dans les tables, **P** signifie que le champ `scope` est présent et non vide ; **E** qu’un exemple situé est présent. Ces indicateurs constatent une présence, pas une qualité automatique. Un périmètre générique peut être insuffisant, et une définition courte peut déjà exprimer une frontière. La colonne finale apporte cette lecture qualitative.

| Constat sur les 41 capacités | Résultat reproductible | Portée du constat |
| --- | --- | --- |
| Nom, définition et finalité présents | **41/41** | Tous ont un résultat et un objectif au moins esquissés ; la présence n’atteste pas une précision égale. |
| Champ de périmètre `scope` présent | **26/41** | Les **15 absences** concernent exactement les 6 capacités D01 et les 9 D03. |
| Exemple situé présent dans les champs publiés | **20/41** | 7 D04, 5 D05, 8 D06. Les 15 D01/D03 et les 6 ingestions n’en ont pas. |
| Nature renseignée | **30/41** | Les **11 absences** concernent les 6 capacités D01 et les 5 ingestions antérieures à D14. |
| Natures déclarées | 13 `decision`, 12 `action`, 2 `knowledge`, 1 `planning`, 1 `management`, 1 `orchestration` | Cette distribution décrit les champs saisis ; elle n’est pas encore une classification homogène. |
| Périmètre des 5 ingestions historiques | Même phrase de **19 mots** | La frontière avec le maître est utile, mais ne décrit pas le résultat métier propre à chaque projection. |
| Ancien domaine D07 encore cité comme porteur de l’exécution | **6 capacités** : D04.i/j/k/l/m et D05.c | Ce sont des références textuelles devenues obsolètes après la fusion dans D06. Les identifiants D07.a/b/c/d conservés restent, eux, corrects. |
| Capacités entièrement `accepted` | **5/41** | Promise Confirmation, ATP, CTP, PTP et Delivery Schedule Decision. La qualité ou la publication des autres descriptions n’étend pas leur portée d’adoption. |

Les 20 exemples sont identifiables par `Exemple` dans `fields.scope`, puis ont été lus pour vérifier qu’ils décrivent une situation. Les autres champs ont été lus pour s’assurer que l’absence de ce mot ne masque pas un exemple situé. Recalcul des principales présences, avec le lecteur du dépôt :

```python
from collections import Counter
from scripts.structured_io import read
m = read('modeles/release/2026-09-16.2/model.yaml')
caps = [n for n in m['nodes'] if n['kind'] == 'capability']
assert len(caps) == 41
assert all(n['fields'].get(k) for n in caps
           for k in ('name', 'definition', 'finality'))
assert sum(bool(n['fields'].get('scope')) for n in caps) == 26
assert sum('Exemple' in n['fields'].get('scope', '') for n in caps) == 20
assert sum(bool(n['fields'].get('nature')) for n in caps) == 30
print(Counter(n['fields'].get('nature', 'absente') for n in caps))
```

## Grille exhaustive des 41 capacités

### D01 — Inventory Management : 6 capacités

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D01.f — Inventory Tracking** | Absente | Non / Non | Résultat clair : état du stock présent et ressources futures connues. Rendre concret le passage fait reconnu → nouvel état, et la différence avec Visibility. Exemple à ajouter : 24 pièces en A, 12 expédiées vers B ; distinguer stock en A, transit et attendu en B sans additionner trois fois les mêmes biens. Maille cohérente pour la tenue d’un état, pas une capacité par événement. |
| **D01.g — Record Inventory Movements** | Absente | Non / Non | La définition distingue déjà mouvement et déplacement physique ; bon point. Préciser ce qui rend un fait reconnu et la contribution à Tracking, sans imposer un système maître inconnu. Exemple : enregistrement d’un changement de propriétaire de 20 pièces qui restent au même endroit. Nature d’action à instruire ; pas une capacité distincte pour chaque type de mouvement. |
| **D01.c — Inventory Visibility** | Absente | Non / Non | Fraîcheur et non-double-compte sont explicites, mais la différence entre produire l’état et le rendre lisible reste implicite. Exemple : une vue réseau expose stock disponible, bloqué, en transit et attendu avec date de connaissance, sans transformer l’attendu en disponible. Nature de connaissance/visibilité candidate, distincte de la tenue transactionnelle. |
| **D01.d — Stocktaking** | Absente | Non / Non | Résultat durable et chaîne de responsabilité intelligibles. Ajouter un cas enregistré 100 / compté 97, puis écart expliqué et correction justifiée enregistrée via Movements. Distinguer proposition de correction, décision autorisée et écriture effective ; leur modalité humaine ou automatique n’est pas imposée. Conserver définition/finalité adoptées et la maille complète de l’inventaire. |
| **D02.b — Supply Protection** | Absente | Non / Non | **Écart prioritaire** : « établir et appliquer » ne restitue pas clairement U230/U231 ni la frontière avec Stock Allocation Decision. Décrire gouvernance, validité et tenue transactionnelle des protections/limites, puis les faire consommer par les décisions. Exemple : appliquer une protection web de 200 pièces pendant une période, sans déplacer ni réserver physiquement ces pièces. Nom conservé. |
| **D02.c — Reservation** | Absente | Non / Non | **Frontière encore ouverte** avec Supply Assignment. Dire ce qui devient opposable aux usages concurrents, à quelle maille, et comment l’engagement est révisé/libéré. Exemple : réserver 6 pièces pour un besoin identifié réduit la quantité mobilisable pour les autres besoins. La distinction avec l’affectation est à éprouver, pas présentée comme résolue ; aucun déplacement de domaine déduit. |

### D03 — Order Promising : 9 capacités

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D03.a — Promise Proposal** | Action | Non / Non | La formulation peut faire croire qu’elle refait les décisions ATP/CTP/PTP/échéancement. Décrire son résultat comme proposition composée, explicite et communicable, avec alternatives et conditions. Exemple : demander 100 pièces, proposer 60 vendredi et 40 lundi, avec une variante accélérée. Action plus fine que les gestions D04, mais résultat distinct ; tester la distinction plutôt que fusionner immédiatement. |
| **D03.b — Promise Confirmation** | Action | Non / Non | Définition adoptée concise et intelligible ; manque la frontière entre engagement, réservation et affectation. Exemple : confirmer 60 vendredi, laisser 40 non confirmées. L’engagement doit garder sa portée sans prétendre que toutes les ressources ont été réservées par la même opération. Compléter le périmètre, conserver les champs adoptés. |
| **D03.c — Promise Revision** | Action | Non / Non | « Réexaminer » et « établir » mêlent mobilisation des décisions et tenue de l’engagement modifié. Décrire demande de révision, solution examinée, modification autorisée et traçabilité de l’avant/après. Exemple : panne signalée, 40 pièces déplacées de vendredi à lundi après réexamen, sans report automatique de l’Order. Action adoptée : clarifier son contrat avant toute reclassification. |
| **D02.e — Supply Assignment** | Action | Non / Non | Affecter/réaffecter/libérer est une maille d’action cohérente. Préciser le résultat « lien de couverture » par rapport à Reservation et aux droits de groupe. Les besoins prévisionnels inclus dans le texte demandent une explication face à la finalité D03 centrée Orders. Exemple : couvrir deux commandes par un stock présent et une réception attendue, puis réaffecter une partie sans créer l’approvisionnement. |
| **D03.i — Available-to-Promise (ATP)** | Decision | Non / Non | Question identifiable et frontière « situation de référence inchangée » claire. Ajouter un exemple quantités/dates, protections, disponibilités admissibles et contraintes de prestation. Le cas de packing wholesale discuté doit être retrouvable : marchandises présentes ne signifie pas promesse conforme. Conserver cette maille et la définition adoptée ; pas de capacité autonome par contrôle ATP. |
| **D03.j — Capable-to-Promise (CTP)** | Decision | Non / Non | **Décision la plus large de D03** : achats supplémentaires, autres Orders/promesses, protections. Le choix local est explicite, donc ne pas le réduire silencieusement au CTP d’un produit. Donner le résultat « plan candidat + impacts + conditions » et distinguer ses propositions des actes D04/D01. Ajouter un scénario de manque de 40 pièces et son traitement alternatif. Maille à expliquer, pas défaut avéré à corriger par découpage. |
| **D03.k — Profitable-to-Promise (PTP)** | Decision | Non / Non | Résultat économique distinct ; risque de confusion avec sélection de service D06.e. Préciser le coût/effet évalué à la maille de la solution Supply, sans absorber comptabilité ou négociation contractuelle. Exemple : livraison unique lundi contre deux expéditions dont une urgente ; choisir parmi les solutions admissibles, pas rendre admissible une solution impossible. Définition adoptée conservée. |
| **D03.l — Delivery Schedule Decision** | Decision | Non / Non | Grain fin et résultat net : couples quantité/date retenus. Ajouter demande 100, solution 60 vendredi/40 lundi, puis distinguer le choix d’échéancier de sa matérialisation par Order Structuring et de la promesse confirmée. Aucune nécessité de créer deux Orders. Définition adoptée conservée. |
| **D03.m — Order Prioritization** | Decision | Non / Non | Question autonome claire mais définition très courte. Entrées et résultat à préciser : commandes en concurrence, critères applicables et priorité relative retenue. Exemple : stock insuffisant pour servir deux commandes à temps ; établir leur priorité, sans réserver ni promettre par cet acte. Ne pas inventer une règle « VIP d’abord » comme politique Beaumanoir. |

### D04 — Order Management : 7 capacités

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D04.i — Sales Order Management** | Action | Oui / Oui | Bonne maille d’objet et exemple 100/60/40 concret ; retour distinct et date demandée/promesse bien séparés. Corriger l’ancien domaine D07 en D06. Expliquer par un lien métier l’usage des deux capacités transversales ; leur citation textuelle seule ne prouve pas une dépendance modélisée. |
| **D04.j — Purchase Order Management** | Action | Oui / Oui | Bonne description du reçu/reste attendu, du report fournisseur et de l’affermissement. Rendre explicite la prise en compte d’une proposition de date fournisseur sans la transformer en promesse Supply acceptée. Corriger D07. L’administration de la commande est suffisamment large ; pas de capacité « report d’achat ». |
| **D04.k — Transfer Order Management** | Action | Oui / Oui | Cas 60 autorisées/40 en attente et départ ≠ arrivée très utiles. Bonne frontière avec le transport physique. Corriger D07 et relier les besoins en faits d’expédition/réception au rapprochement ; ne pas confondre état du transfert et représentation du stock en transit. |
| **D04.l — Customer Return Management** | Action | Oui / Oui | Le dossier de retour et ses quantités sont concrets. **Périmètre encore ouvert** : autorisation commerciale, disposition des biens, remplacement. Ce n’est pas la preuve qu’une capacité manque ; attribuer les responsabilités par cas. Exemple actuel 10/6/4 utile, à compléter ultérieurement par « reçu mais non remis en stock vendable ». Corriger D07. |
| **D04.m — Supplier Return Management** | Action | Oui / Oui | Envoi ≠ réception ≠ avoir financier explicite ; bonne maille de gestion. Distinguer dans les résultats attendus prise en charge du retour fournisseur et mouvement physique, selon les services. Corriger D07. Pas de capacité financière à ajouter au périmètre pour cet exemple. |
| **D04.n — Order Structuring** | Action | Oui / Oui | Décision d’échéancier et transformation de structure correctement séparées ; conservation des quantités et liens très utile. Maille transversale justifiée pour split/merge/spread. Le statut des transformations et leur réversibilité restent des règles à instruire, pas une raison de découper davantage. |
| **D04.o — Order Lifecycle Management** | **Decision** | Oui / Oui | **Ambiguïté de type et de maille à arbitrer** : gouverner la progression peut désigner des décisions d’autorisation de transition ; `decision` est alors défendable, avec tenue des états par les gestions d’Orders. Si la capacité tient elle-même tout le cycle transactionnel, une lecture gestion/action serait plus cohérente. Le texte doit préciser son résultat et son partage avec D04.i–m. Ni le nom Management ni le nombre de verbes ne démontrent une erreur ; aucun renommage ou découpage par transition n’est requis. |

### D05 — Inventory Optimization : 5 capacités

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D05.a — Coverage Target Decision** | Decision | Oui / Oui | Niveaux, seuils et exemple 40/60/100 rendent la réponse tangible. Bonne séparation choix/application. Préciser le consommateur opérationnel des paramètres selon leur sens : seuil de réassort et protection d’usage ne sont pas interchangeables. Ces familles de paramètres ne justifient pas à elles seules plusieurs capacités. |
| **D05.d — Stock Allocation Decision** | Decision | Oui / Oui | Question fine, distinction groupes/réservations/affectations explicite. L’exemple oppose protection minimale et plafond, sans les additionner comme stocks. Compléter le contrat du résultat transmis à Supply Protection et ses effets attendus ; la description actuelle est une bonne base. |
| **D05.e — Replenishment Decision** | Decision | Oui / Oui | Le besoin net, les apports engagés et l’arrondi 50 → 60 illustrent bien la décision. **Trou d’attribution explicite** du déclenchement opérationnel : déterminer qui transforme le résultat retenu en demandes/Orders. Ce trou ne prouve pas qu’il faut une nouvelle capacité ; D04 peut porter la création selon les règles. Garder la frontière achat/réassort/redistribution par finalité. |
| **D05.c — Stock Redistribution Decision** | Decision | Oui / Oui | Bonne finalité intersites et articulation D03/D05 ; distinguer optimisation du stock et couverture d’un Order évite un faux doublon. Corriger l’ancien D07 en D06. Préciser le résultat consommé par Transfer Order Management, sans en déduire une création automatique. |
| **D05.f — Inventory Planning** | Planning | Oui / Oui | Reconfigurer, simuler, valider et mobiliser quatre décisions est conforme au sens adopté. Exemple de scénarios et risque de double compte bien traités. La définition isolée « ces décisions » dépend du contexte : ajouter les noms ou un lien dans le périmètre accessible. Ne pas en faire leur parent ni imposer un contrôle humain. |

### D06 — Execution Management : 8 capacités

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D07.a — Execution Requirements Decision** | Decision | Oui / Oui | La définition courte est très générique, mais le périmètre montre préparation/document/transport. Question distincte : quelles prestations/résultats faut-il ? Ajouter un cas incluant destination, quantité et échéance pour rendre le résultat vérifiable. Ne pas absorber la sélection d’exécutant ni réduire la capacité à un message technique. |
| **D06.e — Execution Service Decision** | Decision | Oui / Oui | La fusion admissibilité/comparaison forme une réponse compréhensible : quel service et quel exécutant mobiliser ? Elle reste proposée. Affiner le résultat : service retenu, conditions de validité, solution non trouvée si nécessaire. Tester son interaction avec PTP : choix de prestation versus choix économique global de promesse. Aucun doublon démontré par le seul mot « choisir ». |
| **D06.b — Execution Capacity Visibility** | Knowledge | Oui / Oui | Très bon cas plafond 1 000 préparations et garde-fou plafond ≠ résiduel. La capacité est bien une connaissance exploitable, pas une décision d’accroissement. Qualifier disponibilité et période lorsque les exécutants les communiquent ; l’incertitude de mesure ne bloque pas le catalogue. |
| **D07.b — Service Order Management** | Management | Oui / Oui | Cycle concret et acceptation ≠ réalisation bien expliqués ; demande 100 colis/60 prêts lisible. Maille comparable à une gestion d’Order D04, bien que sa nature soit différente dans les champs. Conserver le sens propre à chaque contexte et traiter l’harmonisation de type séparément du cycle. |
| **D06.d — Execution Orchestration** | Orchestration | Oui / Oui | Coordination des prestations du plan retenu distincte de la recherche d’une variante. Exemple préparation/document/collecte pertinent. Décrire le résultat constatable : prestations déclenchées ou suspendues selon leurs dépendances, demandes et états cohérents. Ne pas confondre orchestration métier et choix d’un moteur logiciel. |
| **D07.d — Execution Tracking** | Knowledge | Oui / Oui | Bons exemples de jalons, échec documentaire et résultats attendus. Préciser la transmission des connaissances de ressource future à D01.f/c : suivre une prestation et représenter le stock attendu sont deux responsabilités. La duplication éventuelle d’une information n’implique pas deux autorités. |
| **D07.c — Execution Reconciliation** | Action | Oui / Oui | Résultat différent du Tracking : qualifier les écarts entre attendu et réalisé. Exemple 80/100 et conservation du reliquat D04 sont clairs. Compléter le chemin résultats réconciliés → faits de mouvement D01 sans supposer que toute preuve d’exécution modifie le stock. Bonne maille de rapprochement, pas une capacité par écart. |
| **D06.f — Execution Adaptation Decision** | Decision | Oui / Oui | Définition courte vague seule, périmètre et panne/collecte la rendent concrète. Résultat distinct : variante choisie et impact connu sur la promesse. Préciser ses entrées Service Order/Tracking et la sortie vers Orchestration ; D03 conserve la promesse. La latitude relève des règles, sans conditionner l’existence de la capacité. |

### Référentiels : 6 capacités d’ingestion

| Capacité | Nature publiée | P / E | Constat et correction proposée |
| --- | --- | --- | --- |
| **D09.d — Party / Role Ingestion** | Absente | Oui / Non | Maître externe et rôles correctement mentionnés ; le résultat « projection de référence mise à jour et identifiable » mérite d’être explicite. Exemple à ajouter : recevoir une évolution de rôle fournisseur et conserver son identité externe pour les Orders. Ne pas déduire la maîtrise locale du rôle. |
| **D11.a — Agreement Ingestion** | Absente | Oui / Non | Définition assez riche ; intégrer un exemple de nouvelle version de conditions de livraison d’un client wholesale, avec période applicable, sans négociation locale. Distinguer conditions reçues et engagements transactionnels déjà pris ; pas de révision automatique rétroactive. |
| **D08.d — Product Reference Ingestion** | Absente | Oui / Non | Bonne distinction référence produit/catalogues/exemplaires physiques. Ajouter un cas référence de chemise et variante taille/couleur, reçues avant toute entrée en stock. La capacité ne crée ni stock ni Product Unit ; pas une ingestion différente pour chaque type de référence. |
| **D12.a — Catalog Ingestion** | Absente | Oui / Non | Définition orientée données reçues, finalité « permettre de commander » trop indirecte. Décrire la disponibilité d’une offre commerciale identifiable, datée et applicable au contexte. Exemple : offre reçue pour une zone et une période, sans transformer le produit en nouveau produit ni le catalogue en service d’exécution. |
| **D13.a — Fulfillment Network Ingestion** | Absente | Oui / Non | Contenu réseau utile mais exemple absent. Cas entrepôt/magasin et relation de desserte avec provenance ; préciser que capacité dynamique et SLA de service ne sont pas automatiquement des attributs du lieu. Conserver la projection externe, sans administration du réseau. |
| **D14.a — Execution Service Catalog Ingestion** | Action | Oui / Non | Frontière configuration/tracking claire, mais finalité cite encore « qualification », responsabilité désormais intégrée à Service Decision. Reformuler par le consommateur courant et ajouter un exemple de service préparation/document, SLA configuré et accès reçu. Pas d’acceptation individuelle ou de capacité résiduelle dérivée de cette ingestion. |

## Granularité : ce qui mérite une correction et ce qu’il faut conserver

**Les quatre décisions D05 constituent une bonne référence de grain.** Elles répondent à des questions différentes : quel stock viser, quels droits d’usage répartir, quels apports obtenir et quels stocks existants redistribuer. Un résultat peut demander plusieurs calculs et plusieurs paramètres. Les séparer en calcul de seuil, calcul de besoin net, calcul d’arrondi ou mise à jour par interface dégraderait le catalogue métier.

**Les gestions par type D04 sont une référence utile pour les actions de plus grosse maille.** Enregistrer, modifier et suivre le restant d’un Order appartiennent à la même aptitude. Structuring et Lifecycle sont transversales parce qu’elles produisent un résultat réutilisable ; elles ne doivent pas être répétées sous chaque type. Service Order Management présente une maille de gestion comparable dans un autre contexte, sans imposer un Order universel.

Trois hétérogénéités demandent un arbitrage explicite :

- **Nature de Lifecycle.** Deux lectures restent possibles : elle décide des transitions admissibles, les gestions par type tenant les états ; ou elle gouverne et tient le cycle. La première soutient `decision`, la seconde une famille de gestion/action. Arbitrer ce partage et la maille des décisions d’autorisation est plus utile qu’un réétiquetage fondé sur le nom Management ou qu’une scission par transition. Aucune portée de nature n’est adoptée sur D04.o dans v007 ; son nom reste adopté.
- **Nature des gestions d’Orders et ingestions.** D04 utilise `action`, D07.b `management`, D14.a `action`, les cinq autres ingestions aucune nature. Définir une convention de familles et documenter son rapport aux sous-familles avant une normalisation globale. La généralisation de Management demeure proposée dans MOD003 ; on ne peut pas présenter un changement de nomenclature comme déjà acquis.
- **Trois actions de promesse versus une gestion de cycle.** Proposal/Confirmation/Revision sont plus fines que les gestions D04. Elles ont des résultats métier différenciés et des champs déjà adoptés : l’asymétrie n’est pas à elle seule une erreur. Le test utile est de vérifier qu’on peut expliquer leur contribution sans reproduire ATP/CTP/PTP. Si les cas d’usage ne permettent pas de les distinguer durablement, un regroupement pourrait être remis en discussion ; il n’est pas recommandé automatiquement par cet audit.

**CTP est volontairement une décision plus large que les autres décisions D03.** La réponse attendue est un plan candidat de satisfaction impliquant plusieurs adaptations. Son ampleur doit être rendue explicite, ainsi que la responsabilité de chaque mise en action. Le choix ATP/CTP/PTP est acquis ; un audit de granularité ne doit pas le défaire sous prétexte d’alignement éditorial.

**Orchestration et Adaptation restent distinctes.** L’une coordonne le plan retenu, l’autre détermine sa variation. Orchestration peut être une grosse maille d’action même si les décisions qu’elle mobilise sont fines. Ni le nombre de verbes ni la longueur d’une description ne suffisent à décider d’un découpage.

## Huit compléments de description proposés

Ces textes proposent des périmètres et exemples à discuter, sans renommer les capacités. Les définitions adoptées d’ATP, CTP et Promise Confirmation sont conservées ; compléter leur périmètre ne vaut pas adoption de ce complément.

### 1. D01.f — Inventory Tracking

**Résultat à rendre explicite.** Une représentation actualisée des quantités et états de stock reconnus, ainsi que des ressources futures connues, dans les dimensions pertinentes du contexte.

**Périmètre proposé.** À partir des faits de stock reconnus et des informations sur les ressources attendues, tenir les quantités par produit, lieu et état, et par détenteur ou propriétaire lorsque ces dimensions sont utiles. Garder la provenance et le moment de connaissance pour pouvoir expliquer une évolution. Les faits enregistrés sont apportés notamment par Record Inventory Movements ; les prestations encore attendues peuvent être éclairées par Execution Tracking. La façon dont une source fait autorité reste à préciser.

**Exemple fictif.** Vingt-quatre pièces sont présentes au site A. Douze sont expédiées vers B. Dans un périmètre incluant le transit, représenter 12 pièces en A et 12 en transit ; l’attendu de 12 en B indique leur destination et leur arrivée prévue, sans créer 12 pièces supplémentaires. Inventory Visibility permet ensuite de consulter cette situation. Tenir cet état ne réalise pas le transport et ne promet pas ces pièces à une commande.

### 2. D01.g — Record Inventory Movements

**Résultat à rendre explicite.** Des faits de mouvement identifiables et justifiés, permettant d’expliquer les évolutions du stock sans effacer leur histoire.

**Périmètre proposé.** Enregistrer les faits de réception, sortie, transfert, changement d’état ou de propriété et correction justifiée, en gardant quantités, dates, références explicatives et origine. Distinguer la date du fait et sa date de connaissance lorsque le décalage est utile. Une correction conserve le lien avec ce qu’elle rectifie ; elle ne devient pas une réalisation physique fictive. Les règles de reconnaissance et de correction restent à préciser avec les producteurs de faits.

**Exemple fictif.** Vingt pièces changent de propriétaire sans changer de lieu. Enregistrer cette variation et sa justification permet à Inventory Tracking de mettre à jour la dimension de propriété, tout en conservant la même quantité physique au même endroit. À l’inverse, un avis de départ futur ne doit pas être assimilé sans règle à une sortie constatée.

### 3. D02.b — Supply Protection

**Résultat à rendre explicite.** Des protections et limites d’usage gouvernées, valides et effectivement tenues dans les données utilisées par les opérations.

**Périmètre proposé.** Gérer les règles applicables à des groupes de bénéficiaires, leurs quantités ou limites, leur périmètre et leur période de validité. Appliquer une protection signifie tenir transactionnellement les données correspondantes, unitairement, en groupe ou en masse, par les interfaces prévues. Stock Allocation Decision peut déterminer les quantités à retenir ; Supply Protection gouverne leur validité et matérialise leur application. Un seuil de réassort ne devient pas une interdiction de vendre du seul fait qu’il est appelé seuil : son sens et son porteur restent explicites.

**Exemple fictif.** Une décision retient une protection de 200 pièces pour le canal web du lundi au vendredi. La capacité enregistre la protection applicable et sa période, puis son évolution éventuelle. Les décisions ATP en tiennent compte selon les règles d’usage. Ces 200 pièces ne constituent ni un second stock physique ni une réservation pour une commande précise. Le nom actuel Supply Protection est conservé.

### 4. D02.c — Reservation

**Résultat à rendre explicite.** Un engagement de quantité rattaché à un besoin identifié, que les usages concurrents doivent respecter selon les règles applicables.

**Périmètre proposé.** Établir, modifier et libérer cet engagement, avec sa quantité, son périmètre et sa validité. Rendre son effet interprétable pour les capacités qui déterminent ce qui reste mobilisable. La frontière détaillée avec Supply Assignment demeure en réexamen : l’hypothèse à éprouver est que Reservation tient l’engagement opposable, tandis que Supply Assignment tient les liens de couverture par des ressources admissibles. Cette proposition ne tranche ni le rattachement ni l’identité des ressources à réserver.

**Exemple fictif.** Sur 10 pièces mobilisables dans un contexte donné, 6 sont engagées pour un besoin identifié. Les autres besoins doivent tenir compte de cet engagement ; sa libération permet de réexaminer les usages possibles. La réservation ne constitue pas à elle seule une promesse de date, un mouvement physique ou une preuve d’expédition.

### 5. D03.a — Promise Proposal

**Résultat à rendre explicite.** Une proposition Supply compréhensible par son destinataire : quantités, dates, conditions, alternatives et part non couverte.

**Périmètre proposé.** Composer une proposition à partir des solutions et arbitrages produits par ATP, CTP, PTP et Delivery Schedule Decision selon le besoin. Rendre les hypothèses et conditions de réalisation visibles, sans confondre solution candidate et engagement pris. Les capacités de décision ne sont pas des sous-capacités créées par cette composition.

**Exemple fictif.** Pour une demande de 100 pièces vendredi, présenter une solution de 60 vendredi et 40 lundi, ainsi qu’une variante plus coûteuse si elle est réalisable. Indiquer ce qui reste conditionné à un approvisionnement ou une prise en charge d’exécutant. L’émission de cette proposition ne confirme pas automatiquement les dates et ne crée pas automatiquement l’achat, la réservation ou la prestation nécessaires.

### 6. D03.b — Promise Confirmation

**Définition publiée conservée.** « Établir les quantités et dates promises, en distinguant la part confirmée de celle qui ne l’est pas. »

**Périmètre proposé.** Établir l’engagement explicite associé à une solution retenue, avec sa portée et les conditions qui restent pertinentes. Maintenir une lecture distincte de la demande initiale, de la proposition examinée et de la part confirmée. Les règles de validité, les autorisations et les effets sur la couverture et la réservation doivent être précisés ; aucun effet supplémentaire n’est automatique par déduction du verbe confirmer.

**Exemple fictif.** Sur une commande de 100 pièces demandées vendredi, confirmer 60 pièces vendredi et laisser les 40 restantes non confirmées. Une proposition de fourniture lundi pour ces 40 peut continuer à être examinée. La confirmation n’efface pas la quantité demandée dans l’Order et ne démontre pas, par elle-même, que la préparation a commencé.

### 7. D03.i — Available-to-Promise (ATP)

**Définition et maille publiées conservées.** Le résultat est une solution de promesse dans la situation de référence, sans modifier les engagements ni les protections en place.

**Périmètre proposé.** Déterminer les quantités et dates admissibles à partir du stock reconnu, des ressources attendues admissibles, des engagements concurrents, des protections et des contraintes applicables à la commande. Mobiliser la connaissance des services et de leur capacité lorsque leur réalisation conditionne la date proposée. Une valeur de capacité maximale ne prouve pas à elle seule une capacité encore disponible. Les exigences contractuelles de conditionnement participent à la conformité de la solution, même lorsque les colis physiques ne sont pas encore constitués.

**Exemple fictif.** Une commande demande 80 pièces vendredi. Après prise en compte des restrictions et engagements, 50 sont admissibles vendredi et une entrée de 30 lundi est exploitable. ATP peut établir ces possibilités si la préparation, le conditionnement attendu et le transport sont réalisables dans le contexte. Elle n’abaisse pas une protection pour rendre les 80 disponibles vendredi, ne confirme pas la proposition et ne constitue pas physiquement les colis.

### 8. D03.j — Capable-to-Promise (CTP)

**Définition et maille publiées conservées.** Le CTP local construit une adaptation de ressources et d’engagements pour satisfaire l’Order ; ce sens est plus large que certains usages éditeurs.

**Périmètre proposé.** Lorsque la situation de référence ne suffit pas, établir un plan candidat précisant ce qui devrait changer, la solution rendue possible, ses impacts sur les autres besoins et les conditions d’autorisation. Ce plan peut combiner apports supplémentaires, autres dates ou quantités, et changements proposés de protection dans les limites retenues. Il mobilise les responsabilités spécialisées sans les appliquer à leur place. Une adaptation d’exécution D06 répond à un aléa du plan de prestation ; CTP répond à la recherche d’une solution Supply pour honorer l’Order. Si l’aléa affecte la promesse, les deux peuvent intervenir de manière articulée.

**Exemple fictif.** Il manque 40 pièces pour livrer 100 pièces à la date demandée. Examiner un apport supplémentaire disponible à temps ou une réaffectation ayant des conséquences explicites sur une autre commande. Produire la solution candidate et les conditions à satisfaire ; ne pas enregistrer automatiquement l’achat, ne pas modifier une autre promesse et ne pas lever une protection par le seul fait que le plan les propose.

## Priorités de correction documentaire

**Priorité 1 — éviter une interprétation métier erronée.** Réaligner Supply Protection sur U230/U231 ; expliciter Reservation/Supply Assignment sans masquer le réexamen ; rendre lisibles les résultats distincts des actions et décisions D03 ; instruire la nature de D04.o ; corriger les six mentions du domaine D07. Attribuer la mise en action des décisions D05 et les transmissions de faits D06→D01/D04 sans créer une capacité par déduction.

**Priorité 2 — rendre toutes les fiches utilisables isolément.** Ajouter un périmètre aux 15 capacités D01/D03 et un cas situé aux 21 fiches sans exemple. Compléter les six ingestions avec leur résultat propre, leur provenance et un cas de modification, puis renseigner les 11 natures manquantes selon une convention discutée. Ces compléments peuvent être préparés sans changer le catalogue.

**Priorité 3 — rendre l’ensemble régulier à la lecture.** Conserver dans chaque fiche une définition courte, un résultat concret, les principales informations mobilisées, un cas d’application et les frontières utiles. Remplacer les renvois chronologiques tels que « responsabilité auparavant portée par… » par une explication actuelle ; garder l’histoire dans la provenance. Les sept scopes D04 contiennent de bonnes précisions mais répètent des frontières communes : les condenser sans faire disparaître les distinctions vente/achat/transfert/retours.

## Limites

Il s’agit d’une lecture sémantique du modèle publié, pas d’un test d’exécution ni d’une preuve de couverture logicielle. L’absence d’exemple ou de relation explicite ne prouve pas l’absence d’une responsabilité dans l’entreprise. Les cas proposés rendent les définitions discutables ; ils ne fixent ni des seuils opérationnels, ni des cardinalités d’objet, ni des cycles universels. Les descriptions proposées ne remplacent pas la portée exacte des validations existantes. Les manques de catalogue éventuels doivent être arbitrés à partir des cas métier et de la comparaison marché, dans le rapport de synthèse.
