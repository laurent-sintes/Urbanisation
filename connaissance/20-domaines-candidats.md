# Première liste de domaines à éprouver

**Vue de travail courante après U75 (P81 version 0.4, D02 en réexamen) :** la [carte des domaines cœur éprouvée par les récits](25-domaines-coeur-et-epreuve-recits.md) propose dix domaines, 35 formulations de capacités et une matrice des cas. P81 prolonge cette étape ; ses frontières et capacités restent proposées. Les formulations ci-dessous conservent leur provenance historique.

Date : 10 septembre 2026. Sources : [U47](01-contributions-utilisateur.md#u47), F139 ; proposition Codex A27/P74, dans le prolongement de U43–U46/P73. **Liste de travail, sans validation des frontières ni des rattachements.**

Portée réaffirmée en U50 : les domaines étudiés ici servent la capability map de la couche transactionnelle. Un autre modèle fonctionnel orienté processus décrira la couche processus ; les frontières sont documentées sans l’incorporer à la carte du socle.

**Suite U51 :** les [options de découpage du socle](22-options-domaines-socle.md) comparent trois approches et élargissent la discussion à dix périmètres de problèmes, en intégrant les achats U48. Les six propositions ci-dessous restent l’étape initiale U47 ; aucune des listes n’est validée dans son ensemble. U52 reconnaît le rôle de domaine à Order Promising et confirme l’examen des frontières par les cas, sans en arrêter le détail.

## Méthode proposée

Partir d’une première liste de domaines inspirée du marché, puis l’éprouver immédiatement sur les récits et les capacités déjà identifiés. La matière disponible suffit pour commencer une carte utile. La liste reste révisable : un cas qui la met en difficulté peut révéler une frontière à changer, une capacité mal définie ou une connaissance manquante.

Le domaine conserve le sens proposé dans [TER030](19-glossaire-metier.md#notions) : un espace cohérent de problèmes métier liés entre eux, que l’on gagne à comprendre et à traiter ensemble. Un objet commun ou une rubrique de produit ne suffit pas à le définir. Les capacités expriment ce que sait faire l’entreprise indépendamment de son organisation et de ses outils.

1. Décrire pour chaque domaine les problèmes traités, leurs liens, les inclusions et les exclusions ; utiliser le marché pour suggérer des périmètres et des questions.
2. Reprendre les récits existants et deux ou trois aptitudes représentatives pour vérifier ces périmètres. Garder les noms d’applications dans les preuves de réalisation, sans les introduire dans la définition générique.
3. Examiner les chevauchements et omissions. Un même récit mobilise plusieurs domaines ; les capacités candidates encore composites peuvent éclairer plusieurs frontières sans être scindées automatiquement.
4. Discuter avec Laurent les périmètres ainsi rendus concrets, puis approfondir les capacités et les seuls manques de terrain qui empêchent d’avancer.

L’accord recherché porte sur le sens et les frontières, au-delà des intitulés. Univers reste une hypothèse de niveau supérieur. Nature et Finalité demeurent des qualifications distinctes. La conception des applications, services et bounded contexts reste hors de cette étape.

## Six domaines de travail pour le noyau déjà décrit

Ces six propositions ne constituent pas une liste exhaustive du périmètre commerce. Elles prolongent les [huit familles exploratoires du socle](16-capacites-socle-transactionnel.md), en isolant notamment la question de la promesse. Les numéros CAP ci-dessous sont des points d’appui, sans attribution définitive de propriété à un domaine.

| Domaine proposé | Problèmes liés qui justifient le périmètre | Appuis existants et frontière à éprouver |
| --- | --- | --- |
| **Stock** | Quelles quantités sont présentes, où et dans quel état ? Quels mouvements et constats expliquent cette situation et ses écarts ? Comment la rendre visible avec sa provenance ? | CAP004/CAP005 ; U03/U04/U10. L’existant de CAP004 porte sur le magasin. Le comptage et les régularisations restent à approfondir en Q065 ; l’autorité entrepôt ne se déduit pas des copies reçues. |
| **Disponibilité et engagements de ressources** | Quelles quantités sont utilisables pour un usage et un horizon ? Comment protéger des ressources pour des bénéficiaires et affecter ou réserver des quantités à une demande ? | CAP006–CAP010 ; U10/U26/U30. Disponibilité calculée, protection et réservation sont distinguées. La réunion de ces problèmes en un domaine, ou leur séparation, reste à tester ; frontière avec la promesse et avec le calcul amont des protections ouverte. |
| **Promesse / Order Promising** — domaine reconnu en U52, frontières ouvertes | Quelle quantité et quelle date peut-on annoncer à une demande, puis confirmer ou réviser lorsque les ressources et les priorités changent ? | CAP010/CAP035 et P69 ; U30/U31. Le besoin Boardriders sur ressources futures et réaffectation prioritaire est déclaré. Conditions de fermeté et priorités à préciser. Ce domaine dépend des ressources sans se confondre avec la description du stock. |
| **Commandes clients** | Quelle demande commerciale a été acceptée, avec quel contenu, quelles conditions et quels changements admissibles au cours de sa vie ? | CAP014 ; U03–U05. La commande persiste à travers les tentatives d’exécution. Frontière avec le calcul de promesse à préciser ; aucune structure universelle Demande/Commande imposée (Q052). |
| **Réassort opérationnel** | Quel besoin de renouvellement du stock faut-il satisfaire, à partir de quels seuils et objectifs opérationnels, et quelle demande faut-il en déduire ? | CAP011–CAP013 ; U06. Le récit IRMA–Storeland distingue paramètres et déclenchement. La planification de saison reste extérieure au périmètre. |
| **Demandes et engagements d’exécution** | Quelle prestation peut être demandée à un lieu, quel engagement de réalisation est possible, et quel résultat doit être enregistré pour le commerce ? | Parties de CAP015–CAP018, CAP020/CAP036 ; U04–U07. La demande de prestation est distincte de la commande client. Distribution des tâches, relances et réalisation physique ne sont pas incluses globalement dans le socle ; autonomie de C-Log préservée. |

La frontière la plus incertaine est celle entre disponibilité, engagements de ressources et promesse. L’hypothèse consiste à distinguer l’utilisation admissible des ressources de l’engagement annoncé à la demande. Les cas futurs et prioritaires doivent éprouver cette distinction ; ils ne démontrent pas à eux seuls qu’il faut deux domaines distincts au même niveau.

## Cas déjà disponibles pour éprouver la liste

| Cas et provenance | Ce qu’il permet de tester | Limite à conserver |
| --- | --- | --- |
| Protection/allocation avant commande, réservation au passage de commande dans le périmètre historique de Beaumanoir — U30 | Distinguer ressources protégées pour un groupe et engagement envers une demande déterminée. | Le déclencheur métier ne précise pas l’événement technique, l’autorité ni tout le cycle de réservation (Q018). |
| Tentative magasin non aboutie avec maintien de la commande — U04/U05 | Séparer vie commerciale de la commande et vie d’une demande d’exécution. | La libération des ressources et les états exacts restent à documenter. |
| Seuils calculés et référencés par IRMA, déclenchement du réassort par Storeland — U06 | Distinguer détermination du besoin, paramètres applicables et demande de réassort. | Les règles détaillées de quantité ne sont pas établies. |
| Aléa amont et recalcul/republication par MAP — U10 | Examiner les liens entre évolution des ressources, protections applicables et effets opérationnels. | Les objets republiés et l’autorité sur leur état applicable restent ouverts. |
| Besoin Boardriders de couverture par une ressource future — U30 | Éprouver horizon de disponibilité, admissibilité de la ressource et engagement à la demande. | Besoin déclaré, sans preuve de réalisation installée ; règles en Q068. |
| Besoin Boardriders de réaffectation prioritaire — U30/U31 | Examiner la révision des promesses et ses conséquences sur les engagements de ressources. | Le détail de l’ARun installé et de la transition SAP reste ouvert (Q049/Q067). |

Ces cas fournissent déjà plusieurs situations structurantes. Leur réutilisation évite de recommencer la collecte depuis zéro ; elle ne constitue pas une preuve de couverture de tous les besoins du commerce.

## Zones du périmètre à compléter

| Zone à instruire | Problème à préciser avant stabilisation | Matière actuelle |
| --- | --- | --- |
| **Achats opérationnels** | Comment transformer un besoin fournisseur en engagement commercial, puis connaître ses faits de réalisation ? | CAP029–CAP032 ; U48 ajoute trois cas concrets : fabrication complète fournisseur, produits finis sur catalogue et fabrication à façon. Domaine candidat désormais mieux étayé ; engagements fermes, autorités et ressources confiées encore à préciser (Q034–Q036/Q069). Voir la [note achats et orchestration](21-achats-et-orchestration.md). |
| **Retours, échanges et SAV** | Quelles réparations commerciales sont admissibles et quelles conséquences produisent-elles sur la commande, les engagements et les ressources ? | CAP033/CAP034 ; compétence Sarenza déclarée, parcours détaillés manquants (Q048). Délimitation retour/échange/dossier à éprouver. |
| **Connaissance opérationnelle des articles, partenaires, lieux et conditions** | Quels problèmes durables de qualification et d’usage de ces informations doivent être résolus ? | CAP001–CAP003 et Q010. Référentiels est un ensemble à analyser, pas automatiquement un seul domaine cohérent. Les domaines peuvent se séparer selon les problèmes et règles à traiter. |

Le comptage, les écarts et les régularisations sont à compléter dans Stock, sans créer d’emblée un domaine supplémentaire. Le stock virtuel/logique reste une notion à qualifier (Q066), sans domaine autonome présumé. Les exclusions de périmètre et interfaces de la [vue du socle](16-capacites-socle-transactionnel.md) restent applicables.

## Apport du marché et correspondances

La [comparaison des regroupements](../marche/premier-niveau-regroupement-capacites.md) montre des structures de natures différentes. La [comparaison des contenus](../marche/etudes/2026-09-09-modeles-marche/etude-comparative.md) sert de point de départ pour examiner les omissions. Aucun intitulé ci-dessus n’est présenté comme un domaine natif commun à tous les éditeurs.

- **Méthode** : le guide TOGAF G189 de juin 2018, §3.1, pages imprimées 6–7, décrit des départs descendants ou ascendants et leur combinaison pour affiner la carte. C’est un appui à l’itération proposée, sans prescription d’une liste de domaines commerce. Document primaire consulté sur [miroir tiers](https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf) le 10 septembre 2026 ; ELM019, version G211 non examinée.
- **Contrôle de couverture** : la page Microsoft [Inventory to deliver — business process areas](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/inventory-to-deliver-areas), mise à jour le 21 janvier 2025, examinée le 10 septembre 2026, inclut comptage et ajustements dans Maintain inventory levels, retours clients dans Process inbound goods et retours fournisseurs dans Process outbound goods. Ces processus suggèrent des cas à vérifier ; ils ne déterminent ni nos domaines ni l’autorité sur l’exécution logistique. ELM027.
- **Points d’appui locaux déjà rapprochés** : CMP013–CMP017 et CMP020–CMP023 éclairent stock, disponibilité, engagements et promesse ; CMP005 le réassort, CMP006 les commandes. Ce sont des rapprochements d’éléments, sans équivalence des domaines complets proposés ici.
- **Non comparé à cette maille** : les six périmètres complets, ainsi que les domaines à délimiter dans les zones à compléter. La présente liste doit encore être confrontée aux définitions détaillées des références pertinentes. Les limites d’accès de l’étude restent valables.

[CMP028](../marche/comparaisons.md#cmp028) trace cette adaptation méthodologique. À la création de cette vue (U47), les 36 fiches CAP restaient inchangées. U48 enrichit ensuite la réalisation décrite de CAP029 et ses sources, sans modifier son résultat, son statut ni son rattachement. Aucun niveau obligatoire ou catalogue principal n’est adopté.

## Réexamen U53–U57

La [note réassort, transferts et cœur de Supply](23-reassort-transferts-et-promesse.md) réexamine ces frontières après les précisions de Laurent. Le type de parcours OMS relève du modèle de processus commerciaux ; la Supply contrôle, orchestre et optimise la logistique avec une intelligence propre. Les domaines proposés ci-dessus et la liste élargie restent des étapes de travail, à relire selon ce critère.

## Portée courante des référentiels — U97/U98

Les regroupements antérieurs de cette note sont exploratoires. La carte courante remplace les aptitudes de maîtrise des parties, produits et conditions de référence par trois domaines contigus à ingestion seule : Party / Role, Agreement et Catalog. Les commandes restent distinctes des Agreements. L’historique ne constitue pas une instruction d’administration des références dans la plateforme. Voir [P85 et la carte courante](25-domaines-coeur-et-epreuve-recits.md#référentiels-ingérés-u97u98), C64 et INF18–INF20.

**Actualisation U100 — 11 septembre 2026 :** [P81 version 0.7](25-domaines-coeur-et-epreuve-recits.md) distingue maintenant la réception de Product Reference (D08.d) et celle de Catalog (D12.a), aux côtés de Party / Role et Agreement. Les anciennes capacités D08.a–c restent retirées. La [Supply orientée documents d’autorisation](26-supply-documents-autorisations.md) réoriente la revue D04/D07 ; les variantes commerciales ne prescrivent pas des domaines transactionnels Achat/Vente séparés. Les regroupements historiques de cette note restent des pistes, pas la carte courante.
