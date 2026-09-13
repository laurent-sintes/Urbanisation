# Glossaire des notions et des actions métier

Amorce du 9 septembre 2026, issue de [U33](01-contributions-utilisateur.md#u33) et [U34/U35](01-contributions-utilisateur.md#u34), F123–F127, A22 et P71. Ce glossaire accompagne le [catalogue des capacités candidates](09-capacites-candidates.md). Il donne un sens commun aux mots ; il ne détermine ni la hiérarchie des capacités ni le schéma de données.

**Statut :** la définition de capacité est réaffirmée par Laurent en U33. Les définitions locales OMS/Supply sont explicitement formulées par Laurent en U55/U56. Les sens stock physique, logique et virtuel sont explicitement fournis par Laurent en U76 (TER040–TER042). Les autres définitions et conventions ci-dessous sont des **propositions locales à discuter**. Les rapprochements de marché existants sont des appuis, pas une adoption des définitions SAP ou Microsoft. Aucune capacité n’est renommée ou validée par cette amorce.

## Utilisation et entretien

Portée réaffirmée en U50 : la capability map cible la couche transactionnelle. La couche processus sera décrite par un autre modèle fonctionnel orienté processus. Ce glossaire peut éclairer les notions des deux couches sans les réunir dans une même carte de capacités ; les moyens de décision, détermination et orchestration présents des deux côtés ne changent pas cette séparation.

- Lire un libellé avec sa définition, son résultat et son périmètre. Le verbe seul ne permet pas de reconnaître une capacité.
- Conserver les identifiants TER et VER lors des évolutions. Chaque ligne constitue une entrée ; ne pas réutiliser son identifiant pour un autre sens.
- Employer un qualificatif lorsqu’un mot a plusieurs sens utiles. Un terme de marché peut correspondre à plusieurs notions locales ; conserver son contexte dans les comparaisons.
- Lors d’un arbitrage, consigner le libellé retenu, la définition, les synonymes admis, les exclusions, la source, l’auteur et la date. Tracer la formulation remplacée dans les corrections ; garder les verbatims intacts.
- Faire évoluer les termes et les capacités ensemble, sans créer mécaniquement une capacité pour chaque combinaison d’un verbe et d’un objet.

## Notions

Les définitions impératives ou explicitement déclarées par Laurent sont distinguées des propositions dans la colonne de limites et sources ; TER001, TER034/TER035 et les précisions U61 conservent cette provenance. Les repères N1–N6 renvoient aux sources internes en fin de document. Les exemples expliquent le sens ; ils n’affirment pas une configuration existante.

| ID | Terme | Définition de travail | Distinction et appui |
| --- | --- | --- | --- |
| TER001 | Capacité métier | Ce que sait faire l’entreprise indépendamment de son organisation et de ses outils. | Définition réaffirmée par Laurent, U33. Précision de lecture proposée : une opération ou une étape ne constitue pas automatiquement une capacité ; examiner l’aptitude exprimée et sa maille. |
| TER002 | Objet métier | Notion sur laquelle l’entreprise raisonne, tient des faits ou prend des décisions. | Un objet n’est pas une table, un message ou une application. N1. Sens large du glossaire ; U61 rapproche certains objets de la plateforme d’aggregate roots, sans définir leurs frontières. Voir la [note objets/faits](24-capacites-objets-et-faits.md). |
| TER003 | Ressource | Moyen, bien ou droit mobilisable pour obtenir un résultat métier, sous des conditions à préciser. | Distinguer la ressource de sa quantité et de sa représentation ; accès, date et admissibilité peuvent limiter son usage. N1/N3. |
| TER004 | Article / unité de gestion | Bien décrit à la maille nécessaire à son identification et à sa gestion commerciale ou opérationnelle. | Préciser modèle, variante ou SKU, par exemple taille/couleur. Ne pas confondre référence et exemplaire physique. N4. |
| TER005 | Stock | Ensemble de biens matériels considéré dans un périmètre et à une date ; ici, principalement les marchandises du commerce. | Qualifier stock physique et stock enregistré : le second en est la représentation tenue à partir des faits connus. Ni disponibilité ni propriété ne se déduisent du seul mot stock. N2. |
| TER006 | Position de stock | Quantité de stock décrite à une date, pour une maille et des dimensions métier explicites. | Article, unité, lieu ou transit, état, détenteur ou propriétaire selon le besoin ; conserver la provenance. Plusieurs copies ne constituent pas plusieurs stocks. N2. |
| TER007 | Mouvement de stock | Fait de changement d’une position de stock, par exemple une réception, une sortie ou un transfert entre positions. | Une intention de déplacement et son exécution sont distinctes. Une réservation ne signifie pas un mouvement physique. N2. |
| TER008 | Ressource attendue | Ressource dont la mise à disposition est attendue à une date et sous des conditions identifiées. | Ne pas l’assimiler au stock déjà présent. Distinguer prévision, approvisionnement commandé et réception annoncée. N3. |
| TER009 | Disponibilité | Quantité mobilisable pour un usage et un horizon donnés, compte tenu des faits, engagements et règles applicables. | Ce n’est pas une propriété absolue du stock ; une réponse de disponibilité n’engage pas nécessairement une quantité. Une quantité de disponibilité calculée relève du sens Stock virtuel donné en U76 ; son rattachement dépend de l’usage (U77/A51). N2/N3. |
| TER010 | Besoin | Résultat recherché ou manque à satisfaire, avant ou après sa formalisation. | Un besoin peut exister avant une demande identifiable. Convention proposée pour clarifier les échanges. N1/N3. |
| TER011 | Demande | Expression identifiable d’un résultat souhaité, avec objet, quantité, échéance et bénéficiaire lorsque ces précisions sont pertinentes. | Ne prouve ni acceptation, ni promesse, ni couverture. Les familles ci-dessous peuvent avoir des objets et cycles distincts. N3/N4. |
| TER012 | Commande | Acte ou document métier formalisant une instruction commerciale ou opérationnelle et ses conditions. | Qualifier commande client, commande fournisseur ou ordre opérationnel. L’enregistrement ne garantit pas confirmation, réservation ou exécution. Q052 reste ouverte : aucun objet universel Demande n’est adopté. N3/N4. |
| TER013 | Engagement | Décision tenue envers une demande ou un usage, avec résultat attendu, bénéficiaire et conditions explicites. | Distinguer engagement commercial, de ressource et d’exécution ; leur fermeté et leur révision ne sont pas présumées. N3. |
| TER014 | Promesse | Engagement sur ce qui pourra être fourni à une demande, notamment une quantité et une date. | Une proposition calculée n’est pas encore une promesse prise. Une promesse peut exister sans affectation à une ressource précise. N3. |
| TER015 | Confirmation de promesse | Acte ou résultat établissant la quantité et la date promises à une demande dans le contexte défini. | Distinguer d’une confirmation de réception de message ou de constat d’un fait ; préciser l’effet d’engagement. N3. |
| TER016 | Réservation de ressource | Engagement quantitatif enregistré pour une demande identifiée, avec des effets définis sur les possibilités d’engagement pour les demandes concurrentes. | Préciser modification, consommation et libération. Réviser un engagement existant relève de règles explicites ; ni sortie physique ni irrévocabilité implicite. N2/N3. |
| TER017 | Affectation de ressource | Lien entre une demande et une ressource identifiée au degré de précision utile. | La quantité affectée peut différer de la quantité demandée ou promise. Qualifier l’affectation d’une tâche, qui relève d’un autre objet. N1/N3. |
| TER018 | Allocation de groupe | Attribution d’une enveloppe à un usage ou une population, avec des règles d’horizon et de consommation. | Employer le qualificatif ; distinguer cette notion d’une affectation à une demande et d’un plafond de confirmation. N2/N3. |
| TER019 | Protection de ressource | Restriction qui préserve une ressource ou une quantité face à certaines demandes concurrentes. | Une allocation peut porter une protection ; les deux mots ne sont pas des synonymes systématiques. Priorités et horizon sont à expliciter. N2/N3. |
| TER020 | Plafond de confirmation | Limite de quantité confirmable pour des critères et une période définis. | Une limite n’assure pas l’existence de la ressource ; elle diffère d’une quantité protégée. N3. |
| TER021 | Pool de ressources | Regroupement de ressources selon des critères et des règles explicites, pouvant porter une enveloppe et sa consommation. | Définition proposée ; ancien synonyme stock logique retiré après U76 et conservé en C53. Un pool peut contribuer à des états ou calculs, sans définir à lui seul le stock logique ou virtuel. N2. |
| TER022 | Couverture d’une demande | Relation à qualifier entre une demande et ce qui permet de la satisfaire. | Toujours préciser couverture par promesse, par ressources affectées ou par un autre critère défini. « Couvert » et « uncovered » seuls sont insuffisants. N3. |
| TER023 | Règle métier | Condition ou principe qui détermine la validité, l’admissibilité ou les effets d’une décision ou d’un fait métier. | Sa mise en œuvre peut varier avec les outils. Une variante de politique n’est pas automatiquement une capacité différente. N1/N3. |
| TER024 | Processus | Déroulement d’activités, d’événements et de décisions mobilisant des capacités pour atteindre un résultat dans un contexte. | Décrit comment le travail s’accomplit ; ne définit pas à lui seul ce que l’entreprise sait faire. N1. |
| TER025 | Opération métier | Action exercée sur des objets métier avec des conditions et des effets déterminés. | Plusieurs opérations peuvent réaliser une même capacité ; une opération d’API n’est pas automatiquement une capacité. N5. |
| TER026 | Réalisation d’une capacité | Moyens concrets mobilisés pour exercer une capacité : acteurs, pratiques, outils et échanges. | Une réalisation peut évoluer sans changer l’aptitude métier. N1/N5/N6. |
| TER027 | Fonction | Mot à qualifier avant emploi : il ne désigne pas un niveau unique adopté dans notre modèle. | Dans les réponses A19–A21 sur les produits, l’assistant désignait surtout une fonctionnalité de produit. « Fonction métier » pourrait recevoir un autre sens explicite, sans le présumer. U34, C34. |
| TER028 | Fonctionnalité de produit | Comportement ou ensemble de comportements offert par un produit dans une édition et une configuration données. | Peut contribuer à une ou plusieurs capacités, ou à une partie de capacité. Exemple : BOP comme fonctionnalité SAP ; aucune équivalence automatique avec une boîte métier. N5/N6. |
| TER029 | Regroupement de capacités | Ensemble de capacités rapprochées selon un critère métier explicite pour faciliter la lecture de la carte. | Le nom, la maille et le critère sont à préciser ; une catégorie de regroupement n’est pas automatiquement une capacité mère. Aucun étage nommé Fonction n’est adopté. U34, N6. |
| TER030 | Domaine | Espace cohérent de problèmes métier liés entre eux, que l’on gagne à comprendre et à traiter ensemble. | Définition rédactionnelle proposée à partir de U45/U46 : expliciter les liens et limites avant de classer les capacités. Des relations entre domaines n’imposent pas leur fusion. Conception des bounded contexts hors de cette étape ; souvenir du livre et textes vérifiés distingués dans MKT17/ELM041/CMP027. |
| TER031 | Orchestration | Coordination du déroulement d’activités et d’événements selon des dépendances et des règles de conduite explicites. | Définition proposée : qualifier processus métier, aptitude durable de coordination ou moyen logiciel générique. Le mot seul ne fixe ni capacité ni couche. U49 prévoit des moyens d’orchestration dans les deux couches, avec Case Management dans la couche processus ; U48/U49/P75/C40, ELM042, CMP029. |
| TER032 | Fabrication à façon | Mode d’achat dans lequel le donneur d’ordre acquiert des composants et confie leur transformation en produit à un façonnier. | Définition de travail ancrée dans U48 ; propriété, livraisons et consommations restent à préciser. Pas équivalence universelle à une catégorie de document éditeur ; Q069/CMP030. |
| TER033 | Planned Purchase Order | Nom rapporté pour le document que MAP émet dans le premier cas d’achat décrit en U48, après planification en volumes et délais. | Sens local incomplet : ne prouve ni commande ferme ni équivalence avec Planned Order, Purchase Requisition ou Purchase Order. Q034, F141. |
| TER034 | OMS — sens fonctionnel du projet | Case Management préimplémenté pour la vente, au-dessus du transactionnel Supply. | Définition explicite de Laurent en U55 ; U54 situe ici les parcours réassort, eCommerce et retours. Pas définition normative de tout produit ; ne crée pas les mêmes domaines dans le socle. |
| TER035 | Supply — sens fonctionnel du projet | Couche transactionnelle de contrôle, d’orchestration et d’optimisation de la logistique. | Définition explicite de Laurent en U56 ; U57 ajoute exécution pour le commerce et intelligence de backoffice : rééquilibrage, prévision, impondérables. U58 distingue ce modèle fonctionnel du développement FLOW : logistique hors réalisation de la plateforme, en adhérence ; attribution détaillée des aptitudes à préciser. |
| TER036 | Fait de gestion — sens plateforme | Événement métier associé à un document, selon la distinction exprimée par Laurent. | Reformulation de U61/F162 ; source, date, objets concernés et effets à préciser. Ne vaut pas identité automatique avec un message publié ou un Outcome de la Guild. |
| TER037 | Document — sens plateforme | Représentation d’un état d’objet métier, ou objet non modifiable produit ou capté. | Reformulation de U61/F162. Contenu exact des états, versions et règles de correction à préciser ; aucune équivalence avec tout Document SAP/TM Forum. |
| TER038 | État d’objet métier | Situation et valeurs pertinentes d’un objet à un instant donné. | Définition proposée pour éclairer U61 ; distinguer état courant, état représenté par un document et événement qui explique un changement. |
| TER039 | Notification d’événement | Message qui informe un destinataire d’une occurrence avec les références nécessaires à sa compréhension. | Définition proposée, éclairée par ELM059/ELM060 ; la notification et le fait de gestion qu’elle peut signaler sont distincts. Ne fixe ni protocole ni mécanisme de persistance. |
| TER040 | Stock physique | Biens qui existent réellement quelque part dans le périmètre considéré. | Sens explicitement fourni par Laurent en U76, reformulé. Exemple utilisateur : 100 pièces effectivement dans l’entrepôt. Distinguer existence réelle et information enregistrée sur cette existence. |
| TER041 | Stock logique | Description des états métier du stock physique considéré. | Sens explicitement fourni par Laurent en U76, reformulé. Exemple utilisateur : 60 libres, 20 réservées, 10 allouées, 5 bloquées et 5 défectueuses sur 100 pièces. L’exemple forme une partition ; les règles d’exclusivité ou de combinaison des dimensions restent à préciser. |
| TER042 | Stock virtuel | Quantité considérée comme disponible selon un calcul. | Sens explicitement fourni par Laurent en U76, reformulé sans dépendance à un outil. Exemple utilisateur : 60 libres + 30 attendues demain − 15 promises = 75. Horizon, usage, fermeté et absence de double déduction à préciser ; ni stock physique supplémentaire ni formule universelle. U79 évoque aussi une existence virtuelle des ressources futures : distinguer cette représentation anticipée du résultat calculé, sans assimiler futur et virtuel. |
| TER043 | Stock futur | Expression de travail pour les ressources dont la mise à disposition est envisagée ou attendue à un lieu et pour un usage futurs. | U79 cite potentiel contractuel, achats planifiés et approvisionnements en cours. Qualification proposée : distinguer potentiel encore non daté et ressource attendue TER008 ; des biens déjà physiques en transit peuvent être futurs pour leur destination. Ne prouve ni engagement fournisseur ni disponibilité garantie. |

## Familles de demandes à distinguer

Ce tableau propose un vocabulaire, sans imposer une classe mère, un cycle d’états commun ou une persistance unique. Les liens entre demandes doivent être explicités plutôt que déduits de mots voisins.

| Forme qualifiée | Sens proposé | Confusion à éviter / source |
| --- | --- | --- |
| Demande de vente | Besoin de fourniture exprimé par un client envers le vendeur. | Préciser ligne, quantité et date ; la demande n’implique pas une promesse déjà faite. U30, CAP014. |
| Demande d’achat | Besoin d’obtenir des biens ou prestations par un achat. | Ne pas la confondre avec la commande fournisseur ferme ; rôle décrit de MAP et Q034. CAP029. |
| Demande d’approvisionnement ou de réassort | Besoin de remettre une ressource à disposition d’un périmètre. | Peut être satisfait avec ou sans engagement d’achat/vente selon le cas ; distinguer besoin, parcours OMS et transfert exécuté. U53–U57, CAP011–CAP013. U62 cite Demande de réassort comme objet de processus ; distinguer son suivi du besoin présenté au socle, avec correspondance entre représentations à préciser. |
| Demande de transfert | Besoin de déplacer des biens entre deux périmètres ou lieux définis. | Ne vaut pas constat de départ ou d’arrivée ; préciser les changements de détention ou propriété éventuels. N2/N3. |
| Demande d’exécution / de prestation | Résultat opérationnel demandé à un exécutant ou prestataire, par exemple préparer et expédier. | La demande d’exécution magasin peut être annulée sans supprimer la commande client. CAP018/CAP020, U05. |
| Demande de retour ou d’échange | Résultat commercial ou opérationnel demandé à la suite d’une fourniture. | Demande, autorisation de retour et réception des biens restent distinctes ; pratiques à documenter. CAP033/CAP034. |

Une commande fournisseur et l’offre attendue qu’elle peut représenter répondent à des points de vue différents. De même, satisfaire une demande de vente peut mobiliser plusieurs demandes d’exécution. Ces relations n’autorisent pas à fusionner les objets par défaut.

## Verbes et effets attendus

Toutes les conventions VER sont proposées. Les sens sont destinés aux libellés et définitions des capacités ; **la liste n’est pas un catalogue de sous-capacités ni un enchaînement obligatoire d’étapes**. Appuis N2–N6 selon les exemples. Le verbe est à compléter par l’objet et, si nécessaire, le résultat ou le contexte métier.

| ID | Verbe | Sens proposé | Précaution de formulation |
| --- | --- | --- | --- |
| VER001 | Définir | Établir la signification, les règles ou les caractéristiques d’un objet ou d’une politique. | Distinguer définition et application effective. |
| VER002 | Tenir — en réexamen | Terme proposé par l’assistant pour conserver des informations métier cohérentes et à jour. | Jugé peu clair par Laurent en U35 ; ne pas l’utiliser par défaut pour de nouveaux libellés. Aucun libellé français SAP vérifié ; choisir une formulation selon le résultat attendu. |
| VER003 | Déterminer | Établir un résultat à partir de faits et de règles. | Exemple : déterminer une disponibilité ; le calcul peut être un moyen. |
| VER004 | Calculer | Produire une valeur par des opérations quantitatives définies. | L’employer si le résultat quantitatif est bien le besoin métier ; ne pas imposer un algorithme. |
| VER005 | Vérifier | Établir si des conditions sont respectées et produire un constat. | Un contrôle favorable n’autorise pas nécessairement l’action. |
| VER006 | Autoriser | Rendre une action admissible dans un périmètre et sous des conditions définis. | Ne signifie pas exécuter l’action ni réserver sa ressource. |
| VER007 | Enregistrer | Prendre en compte durablement un fait ou une décision dans la connaissance métier. | Décrire ce qui devient connu et ses effets ; ne pas réduire le résultat à une écriture technique. |
| VER008 | Demander | Exprimer un résultat souhaité à un destinataire, avec les conditions pertinentes. | Distinguer demande, acceptation et engagement de fourniture. |
| VER009 | Protéger | Rendre une ressource ou quantité indisponible à certaines demandes pour préserver un usage. | Préciser les usages concurrents et les règles ; aucune protection absolue implicite. |
| VER010 | Allouer à un groupe | Attribuer une enveloppe à un usage ou une population. | Qualifier l’objet ; éviter « allouer » comme synonyme indifférencié de réserver ou affecter. |
| VER011 | Réserver | Engager une quantité de ressource pour une demande identifiée. | Définir les effets sur les possibilités d’engagement des demandes concurrentes ; la révision d’engagements existants relève de règles explicites. |
| VER012 | Affecter | Établir un lien entre une ressource et une demande ou un bénéficiaire précis. | Qualifier ressource ou tâche ; ne pas confondre avec une promesse commerciale. |
| VER013 | Promettre | Prendre un engagement sur le résultat qui pourra être fourni à une demande. | Préciser quantité/date et conditions ; distinguer proposition et engagement. |
| VER014 | Confirmer | Établir ou attester un résultat, un fait ou un engagement, en précisant la portée et l’effet de cette confirmation. | Compléter obligatoirement le sens : confirmer une promesse et accuser réception ne sont pas équivalents. |
| VER015 | Prioriser | Établir un ordre relatif de traitement ou de satisfaction entre des demandes. | Ne réaffecte pas nécessairement les ressources à lui seul. |
| VER016 | Arbitrer | Choisir entre des possibilités ou demandes concurrentes selon des règles et contraintes. | Exprimer ce qui est décidé ; ne nomme pas un comité ou un outil. |
| VER017 | Réviser | Réexaminer puis modifier, si nécessaire, une règle, décision ou engagement existant. | Une simple republication technique ne démontre pas une révision métier. |
| VER018 | Réaffecter | Modifier une affectation existante de ressource. | Distinguer l’effet sur le lien de ressource de l’éventuelle modification de promesse. |
| VER019 | Libérer | Lever tout ou partie d’une restriction ou d’un engagement sur une ressource. | Préciser « libérer une quantité réservée » ; « libérer pour livraison » peut vouloir dire autoriser. |
| VER020 | Consommer | Imputer une utilisation sur un droit, une enveloppe, une quantité ou un engagement. | Préciser l’objet : consommation d’allocation et sortie physique ne sont pas le même fait. |
| VER021 | Annuler | Retirer l’effet encore applicable d’une demande, décision ou engagement identifié, selon ses règles. | Ne signifie pas effacer l’historique ni annuler automatiquement les autres objets liés. |
| VER022 | Rapprocher | Comparer des faits ou représentations pour établir leur concordance ou leurs écarts. | Constater un écart ne signifie pas autoriser sa correction. |
| VER023 | Exécuter | Accomplir la prestation ou l’action métier demandée. | Préciser le résultat ; distinguer l’intention, l’exécution et l’enregistrement de son constat. |
| VER024 | Gérer | Couvrir un ensemble d’aptitudes ou d’actions relatives à un objet. | Acceptable si le périmètre est défini ; ne suffit pas seul à préciser les effets. |
| VER025 | Valider | Terme courant dont le sens doit être explicité avant emploi canonique. | Choisir vérifier, autoriser, accepter ou confirmer selon l’effet recherché ; ces verbes ne sont pas interchangeables. |

## Règles proposées pour les libellés de capacités

1. Employer un verbe à l’infinitif et un objet métier défini ; ajouter un complément lorsqu’il lève une ambiguïté.
2. Écrire une définition qui décrit **l’aptitude durable de l’entreprise**, son résultat et ses limites, sans dépendre d’une équipe, d’une application ou d’un déroulement imposé.
3. Éprouver la formulation en changeant mentalement l’organisation ou les outils : la capacité doit garder son sens. Son exercice peut mobiliser des humains, des partenaires et des logiciels.
4. Décomposer seulement si plusieurs aptitudes métier durables et intelligibles se distinguent dans le périmètre parent. Les opérations, règles et variantes peuvent rester dans la description d’une même capacité.
5. Examiner ensuite les responsabilités, contrats et réalisations. Ils servent à concevoir ou comparer la mise en œuvre ; ils ne créent pas à eux seuls une capacité.

Exemples **illustratifs**, pas nouveaux candidats : « déterminer la disponibilité pour une demande », « réserver des ressources pour une demande », « réexaminer les promesses aux demandes ». La normalisation du vocabulaire doit les rendre comparables sans fixer leur maille ni en faire trois capacités déjà validées.

## Sources internes, limites et suites

- **N1** — [Orientation à deux couches](15-orientation-deux-couches.md), U18–U20 et [définition U33](01-contributions-utilisateur.md#u33). Les modèles métier et les réalisations sont distingués.
- **N2** — [Exploration du stock](17-exploration-bloc-stock.md), U26/U27, P66 et Q066. Les sens du stock logique restent ouverts.
- **N3** — [Politiques du périmètre historique de Beaumanoir et de Boardriders](18-politiques-engagement-gbm-brd.md), U30/U31, P68/P69 et [comparaison allocation/réservation](../marche/allocation-reservation-sap-microsoft.md). Appuis sémantiques de marché déjà documentés ; aucune équivalence de termes adoptée ici.
- **N4** — [Catalogue des capacités candidates](09-capacites-candidates.md), notamment référentiels, commandes, réassort, achats, exécution et retours. Les réalisations et autorités non connues le restent.
- **N5** — [Détail des fonctions de marché](../marche/detail-fonctions-stock-promesse.md), U32/P70 : les objets, opérations et règles expliquent les capacités sans imposer leur décomposition.
- **N6** — A22/P71 : propositions de formulation de cette amorce. Les définitions ne sont pas des citations normatives ni un nouveau catalogue métier.

Les questions [Q052](06-questions.md#q052) sur commande/demande, [Q066](06-questions.md#q066) sur le stock logique et [Q068](06-questions.md#q068) sur les règles de Boardriders restent ouvertes. Le glossaire n’impose ni héritage entre objets, ni transitions d’état, ni périmètres de persistance. Commencer la discussion par ressource/stock/disponibilité, besoin/demande/commande, puis engagement/promesse/réservation/affectation ; éprouver ensuite les verbes sur les 36 candidats avant tout renommage.

## Provenance de tenir et choix de formulations

U35 remet en question la lisibilité de « tenir ». C’était une formulation de l’assistant ; elle n’avait pas été reprise d’un libellé SAP français vérifié. Les sources consultées attestent les mots anglais **Manage** et **Maintain**, notamment pour la protection et les données de référence. Elles ne démontrent pas que « tenir » serait leur traduction française canonique.

Selon le résultat voulu, on peut proposer « gérer les protections applicables » pour une aptitude composite explicitée, « mettre à jour les quantités protégées » pour une opération précise, ou « déterminer la protection applicable » pour une décision. Ces formulations n’ont pas la même portée ; elles ne sont pas des remplacements automatiques de CAP008 ni des synonymes validés. En particulier, gérer seul reste large et doit être défini.

Vérification ponctuelle du 2026-09-09 : [Apps for Supply Protection](https://help.sap.com/docs/SAP_S4HANA_CLOUD/32da8359c8ee4e8b8e8c5e15cacba5aa/d308d458b5794b1cbf647aca23de4d9d.html), sections Use et Business Roles, documentation affichée 2608 Latest, passage indexé consulté : nom Manage Supply Protection et emploi de maintain pour les quantités protégées ; [Maintaining Material Master Data](https://learning.sap.com/courses/business-processes-in-sap-s-4hana-sourcing-procurement/maintaining-material-master-data), titre/objectif, cours sans édition produit précisée. ELM040/CMP025 : preuve lexicale anglaise, pas nomenclature française de capacités.

## Hypothèse sur les natures de capacité

Complément du 10 septembre 2026 : [U37](01-contributions-utilisateur.md#u37), [U38](01-contributions-utilisateur.md#u38), [U39](01-contributions-utilisateur.md#u39), [U40](01-contributions-utilisateur.md#u40), [U41](01-contributions-utilisateur.md#u41), [U42](01-contributions-utilisateur.md#u42), F128–F133, A24, [P72](05-propositions.md#p72), [C35](04-corrections.md#c35) et [C36](04-corrections.md#c36). **La grille et ses définitions restent à éprouver** ; les entrées TER/VER et les fiches CAP ne sont pas modifiées.

Laurent propose d’abord Capturer, Aider, Décider, Administrer, Administrer, Gérer et Optimiser. Il précise ensuite qu’Optimiser et Aider expriment des intentions ; il propose Adapter pour le changement des volumes et contenus d’objets métier existants. Restituer, proposé ci-dessous pour la visibilité, est une suggestion assistant qui n’a pas été validée par Laurent. Les termes initiaux restent conservés dans U37. U40 précise qu’une même nature Adapter peut servir plusieurs intentions ; U41 propose une colonne pour le pourquoi. **Finalité** est l’intitulé retenu par Laurent en U42, qui remplace la proposition initiale consignée dans C36. Les exemples de finalités restent proposés.

Une nature pourrait qualifier **le type de contribution métier d’une capacité**. Cet axe traverse les domaines et niveaux de décomposition. Il n’impose ni séquence de processus ni répartition entre le socle et la couche processus ; une capacité reste ce que sait faire l’entreprise indépendamment de son organisation et de ses outils.

### Lecture proposée sur le stock

La réponse [A23](03-contributions-assistant.md#a23) à U36 présentait huit lignes, dont les commandes clients. Pour éprouver les sept qualifications de U37, la lecture suivante écarte cette ligne et associe la dernière qualification au réexamen des promesses. **Ce rattachement est une interprétation assistant**, pas une correspondance explicitement validée par Laurent. Les libellés résument la discussion ; ils ne renomment pas les CAP.

La colonne **Nature envisagée** décrit le type d’effet ou de contribution. La colonne **Finalité** décrit l’utilité recherchée, le pourquoi. Ses contenus ci-dessous sont des exemples proposés à partir des discussions ; ils ne constituent pas des objectifs validés pour les entités du groupe.

| Capacité discutée et appui | Nature envisagée | Finalité — pourquoi | Précaution de lecture |
| --- | --- | --- | --- |
| Enregistrer les états et mouvements du stock — CAP004 | Capturer | Disposer de faits de stock permettant d’expliquer les quantités et leurs variations. | La capture ne garantit pas à elle seule la fiabilité. CAP004 est documentée sur le magasin ; rapprochement et correction peuvent contribuer au résultat. |
| Rendre les stocks visibles — CAP005 | Restituer — proposition assistant après U39 | Permettre aux opérations et aux décisions de s’appuyer sur une connaissance du stock partagée et contextualisée. | Provenance, fraîcheur et périmètre ; visibilité ne donne pas autorité de modification. |
| Déterminer la disponibilité — CAP006 | Décider ou évaluer — portée à préciser | Établir ce qui peut être proposé pour un usage et un horizon en respectant les contraintes applicables. | Une réponse calculée peut exprimer une décision métier sans constituer une promesse ou une réservation. |
| Définir les protections — CAP007 | Administrer dans U37 ; contribution de décision à examiner | Préserver des ressources pour les usages ou groupes de demandes retenus par la politique métier. | Concevoir ou choisir la politique ne se réduit pas à saisir ses paramètres. Frontière planification/opération conservée. |
| Gérer les protections en vigueur — CAP008 | Administrer — à éprouver | Faire reposer les décisions sur les protections effectivement applicables au contexte et à la date considérés. | Version applicable distincte de son application dans une décision ; candidat et autorité encore à préciser. |
| Gérer les engagements de ressources — CAP010 | Gérer — à préciser ; Adapter pour certaines évolutions d’engagement | Matérialiser et faire évoluer l’engagement de ressources envers les demandes, avec des effets cohérents sur les demandes concurrentes. | Réserver, affecter, confirmer et libérer restent regroupés dans la fiche. Pas de nouvelle décomposition ni d’adaptation comme nature exclusive. |
| Réexaminer et réviser les promesses — CAP035/P69 | Adapter — proposé par Laurent en U38 | Ajuster les engagements à l’évolution des ressources, besoins ou priorités ; éventuellement améliorer leur répartition selon un objectif explicite. | Optimiser est une intention possible. Révision, faisabilité et optimisation ne sont pas synonymes. |

### Adapter et restituer : définitions de travail

**Adapter — définition proposée à partir de U38 :** modifier les quantités, contenus ou relations d’objets métier existants pour répondre à une évolution des faits, des besoins ou des contraintes, selon les règles applicables. Laurent mentionne explicitement volumes et contenus ; l’extension aux relations, pertinente pour les affectations, est proposée par l’assistant.

Exemple fictif : une promesse existante de 10 unités pour une demande A passe à 7 ; une autre demande existante B reçoit une promesse de 3, dans un périmètre de 10 unités et si les règles l’autorisent. Le résultat étudié est la modification de la répartition et des engagements. Il ne démontre pas à lui seul une optimisation ni l’absence de tout nouvel objet associé au changement. On peut aussi modifier la date d’une même promesse après un retard de ressource. Les objets concernés peuvent conserver leur identité métier ; les engagements liés doivent rester cohérents.

U40 enrichit les intentions possibles d’Adapter : redresser une donnée fausse, optimiser, engager ou valider au sens de promettre discuté ici. Ces finalités peuvent partager un type de changement sans produire les mêmes effets métier : rectifier une quantité ne crée pas le même engagement que rendre une promesse effective. Valider doit conserver le sens qualifié prévu par VER025 ; toute validation n’est pas une promesse.

La remarque sur l’absence de nouveaux objets porte sur l’adaptation discutée. Elle ne constitue ni une règle universelle sur toutes les capacités ni une interdiction de conserver des versions, décisions, événements ou historiques. Aucun schéma de données ou mode de persistance n’en est déduit.

**Restituer — proposition assistant après U39 :** fournir une représentation métier des faits ou résultats connus, avec le contexte nécessaire à leur compréhension et à leur usage. Pour le stock : positions, provenance, fraîcheur et périmètre de lecture. Restituer ne veut pas dire donner un droit de modification, ni imposer un écran, un rapport ou une interface technique. Une consolidation peut être nécessaire ; l’effet métier prime sur l’opération informatique de lecture.

### Frontières à éprouver

Décider précise le résultat ou le choix retenu selon les règles ; adapter fait évoluer la situation existante ; administrer concerne ici les règles, paramètres et protections applicables. Leurs recouvrements restent à discuter : une adaptation peut nécessiter une décision et une administration peut modifier des objets existants. Gérer couvre encore un ensemble large d’actions. Ces distinctions ne justifient pas automatiquement plusieurs capacités séparées.

Pour une intention d’optimisation, préciser ce qu’on cherche à améliorer et les contraintes à respecter. Réduire le retard total tout en préservant certains engagements fermes est un objectif illustratif. Reporter une promesse après un retard fournisseur peut simplement rétablir une situation réalisable. Donner priorité à une demande Gold exprime une politique ; cela ne démontre pas à lui seul la recherche d’un optimum. Aucun objectif local de ce type n’est adopté par ces exemples.

On peut essayer une contribution dominante et des contributions secondaires, sans exiger des catégories exclusives. La grille ne devient pas un découpage en lecture/écriture ni une classification technique création/lecture/mise à jour/suppression. Aucun catalogue par combinaison d’un objet et d’un verbe n’est construit. Aucun standard externe n’est invoqué ou nouvellement vérifié ; aucune équivalence de marché ni classification native n’est revendiquée.

### Décrire le pourquoi dans la colonne Finalité

La finalité répond à **« À quoi sert cette capacité pour l’entreprise ? »**. Elle peut se formuler par « permettre de… », « assurer… » ou « rendre possible… », avec le bénéfice ou l’engagement métier recherché. Elle ne doit pas seulement répéter le libellé de capacité. Un indicateur et une cible chiffrée peuvent la préciser ultérieurement ; ils ne sont pas requis pour lui donner un sens.

Les exemples de U40 permettent d’éprouver la séparation :

| Nature dans l’hypothèse | Changement métier illustratif | Intention ou finalité possible |
| --- | --- | --- |
| Adapter | Rectifier une quantité enregistrée après constat d’un écart. | Rétablir une connaissance fidèle des faits et éviter des décisions fondées sur une information fausse. |
| Adapter | Modifier la répartition de quantités entre engagements existants. | Améliorer la satisfaction des demandes selon l’objectif et les contraintes choisis. |
| Adapter | Faire évoluer un objet existant pour matérialiser un engagement de ressource. | Donner effet à cet engagement envers la demande et préciser les possibilités des demandes concurrentes. |
| Adapter | Modifier la quantité, la date ou le statut d’une promesse pour la rendre effective selon les règles applicables. | Prendre ou confirmer un engagement de fourniture envers une demande. |

Ces exemples n’imposent pas que tout engagement ou toute promesse provienne d’une modification d’objet préexistant : ils illustrent la lecture d’Adapter proposée par Laurent. Nature, finalité et objet ne suffisent pas séparément à définir la capacité ; son aptitude, son résultat et ses limites restent à expliciter. Le tableau conserve donc plusieurs angles de lecture sans transformer les intentions en nouvelles capacités.

## Regroupement et qualifications

[U43](01-contributions-utilisateur.md#u43) ouvre la question du premier niveau. [U44](01-contributions-utilisateur.md#u44) restitue l’hypothèse Univers / Domaine / Capacité du draft de juin. La [comparaison du marché et proposition P73](../marche/premier-niveau-regroupement-capacites.md) distingue les regroupements envisagés, la capacité composite et la profondeur de décomposition. Nature et Finalité qualifient la capacité ; elles ne définissent pas son domaine. Aucun terme TER/VER ni niveau de hiérarchie supplémentaire n’est adopté par ce renvoi.

U45/U46 précisent le critère de délimitation : le domaine est abordé comme un espace de problèmes métier liés dans un périmètre cohérent. [TER030 et l’analyse DDD](../marche/premier-niveau-regroupement-capacites.md#donner-un-sens-au-domaine-avec-ddd) distinguent la définition rédactionnelle proposée, la formulation native d’Evans et la frontière d’application d’un modèle. Les domaines concrets et leurs capacités restent à éprouver ; Nature et Finalité ne se substituent pas à leur espace de problèmes.

U46 recentre explicitement cette étape sur la cartographie des problèmes et des capacités. Les références aux modèles et à leurs frontières restent une provenance documentaire ; elles n’ouvrent pas un travail de conception des bounded contexts, des applications ou des services. C38 conserve cette précision et la limite de la vérification du livre.

## Éclairage BIZBOK après U60

La [recherche BIZBOK](../marche/bizbok-capacites-et-domaines.md), ELM052–ELM055/CMP034, distingue définitions externes et conventions locales. Elle éclaire notamment aptitude, réalisation contextuelle, niveau et catégorie. Le sens de Domain dans les perspectives Guild n’est pas celui de nos domaines problématiques. Aucune entrée, définition ni nature n’est renommée ou validée automatiquement ; U33 et les choix explicites de Laurent restent les règles du projet.

## Portée des objets après U62

Laurent confirme des objets métier dans les deux couches : Demande de réassort est son exemple pour le modèle processus orienté Case Management ; les domaines transactionnels ont aussi leurs objets. TER002 conserve cette portée commune. Le sens, les règles, le cycle de vie et l’autorité doivent être précisés dans chaque modèle, avec leurs [relations contractuelles](24-capacites-objets-et-faits.md#des-objets-métier-dans-les-deux-couches) ; aucun nouveau terme ni objet Demande universel adopté.

## Noms anglais et sens métier — U66/U67

Laurent demande une nomenclature anglaise et le réemploi des noms de marché adéquats, notamment **Inventory Management**. Les définitions demeurent en français ; la [carte courante](25-domaines-coeur-et-epreuve-recits.md) applique cette consigne. C48 conserve les libellés précédents ; les termes natifs réemployés restent distincts des traductions locales proposées.

La précision U67 distingue **Supply Protection**, aptitude à protéger des ressources pour des groupes ou usages, et **Supply Assignment**, aptitude à couvrir des demandes par des ressources admissibles, du mécanisme **Allocation Run**. Ces définitions de travail prolongent les notions de protection, d’affectation et de réservation du glossaire ; leurs frontières détaillées restent proposées. Un nom de capacité n’a pas besoin d’être nouveau lorsque le marché exprime déjà correctement l’aptitude.

La distinction avec **Reservation** doit être éprouvée par les résultats : l’affectation établit la couverture par une ressource et peut déjà l’engager ; la réservation précise les effets sur les usages concurrents. Il peut s’agir de deux vues d’une même capacité selon les définitions retenues. Ce repère n’impose pas deux objets ni deux composants. Le rang natif SAP des noms et la documentation de leurs réalisations constituent une question distincte de leur nature métier : [C49](04-corrections.md#c49), [ELM067/CMP038](../marche/comparaisons.md#cmp038).

## Clarification de D01 et du stock logique — U69

**Lecture historique U69–U75 :** les hésitations de sens ci-dessous sont précisées ensuite par U76. Pour le vocabulaire courant, lire TER040–TER042 et le complément U76/U77 en fin de document.

U69 propose une lecture interrogative de D01 ; [C50](04-corrections.md#c50) distingue définition des dimensions, connaissance des positions, faits qui les font évoluer, visibilité et rapprochement des écarts. Les quatre capacités de la [carte courante](25-domaines-coeur-et-epreuve-recits.md#d01-stocks) restent proposées ; état et évolution peuvent relever d’une même aptitude, sans découpage CRUD adopté.

« Logique/virtuel » ne désigne pas encore une catégorie unique : une vue regroupant des positions est distincte d’un pool protégé, d’une disponibilité par usage ou d’une ressource future. TER021 et Q066 restent ouverts. Présenter ces informations ensemble ne fusionne pas les autorités ni les domaines qui portent leurs règles.

« Golden data » est employé par Laurent dans une question, sans définition ni architecture validées. Une information de référence fiable peut résulter de plusieurs capacités et règles d’autorité. Comparer des sources à des dates ou périmètres différents ne constitue pas un écart physique établi ; corriger une copie de donnée et ajuster une position métier doivent rester distingués. Le rapprochement métier peut être nécessaire avec un seul système ; datahub et moyens de qualité ne constituent pas à eux seuls sa définition. Aucun nouveau terme TER ou VER adopté.

**Évolution après U74 :** Supply Protection est rattachée à Inventory Management dans P81 version 0.3, selon l’orientation de Laurent. Les mentions D02 ci-dessus conservent leur contexte antérieur ; la vue courante place les protections en D01 et leur prise en compte dans la disponibilité et les engagements en D02. Le sens du stock logique/virtuel reste à préciser ; une vue, un pool protégé et une disponibilité ne deviennent pas synonymes.

**Évolution U75 :** réservation rattachée à Inventory Management ; Supply Assignment à Order Promising. Réserver exprime un engagement de quantité pour un besoin et ses effets sur les usages concurrents ; affecter exprime la couverture d’une demande par des ressources. Les deux aptitudes doivent rester cohérentes, sans présumer deux objets ni une séquence fixe. La définition proposée D02.c est clarifiée en C52, en continuité de TER016.

La disponibilité décrit ce qui est utilisable pour un usage et une date, selon ressources et restrictions ; c’est un résultat calculé, dont la nécessité d’une capacité autonome reste à éprouver. Exemple fictif : 100 unités présentes, 20 bloquées, 30 réservées parmi les 80 utilisables, aucune autre contrainte ni ressource future : 50 encore réservables. Cette illustration n’est pas une formule universelle ; protections et réservations peuvent se recouvrir.

Regrouper positions physiques, vues logiques, pools et projections dans un domaine de connaissance commun est une proposition assistant après U75. Préserver les notions : des vues du même stock ne sont pas des stocks additionnels, un pool peut porter des règles d’engagement et une quantité attendue ne vaut pas présence physique. Q066 reste ouverte ; la question de Laurent n’adopte pas une taxonomie unique du virtuel. Voir A49 et CMP041.

## Distinction courante des stocks et frontière proposée — U76/U77

La convention de Laurent est désormais : **physique = existence réelle**, **logique = état métier**, **virtuel = quantité calculée disponible**. Les exemples U76 illustrent une partition de 100 et une projection donnant 75 ; ils ne décrivent pas un déploiement ou un stock réel. C53 corrige les formulations antérieures ; stock logique, pool et vue consolidée ne sont pas des synonymes.

Conditions de cohérence proposées : dans une vue qui totalise 100, éviter de compter deux fois une unité portant plusieurs qualifications. Si qualité, protection et réservation sont modélisées sur des dimensions distinctes, définir la règle qui produit les catégories présentées. Pour 60 + 30 − 15, vérifier que les 15 promises ne sont pas déjà retirées des 60 libres et que les 30 attendues sont admissibles à l’horizon choisi. Aucun calcul métier universel n’est déduit de ces exemples.

U77 propose physique/logique dans Inventory Management et virtuel dans Promising. A51 soutient ce partage pour la projection utilisée pour promettre quantité et date ; un simple disponible courant pour réservation peut rester dans Inventory Management. Le sens générique de virtuel U76 n’est pas restreint à la promesse. Une vue peut exposer plusieurs informations sans posséder tous leurs calculs ; le partage détaillé reste proposé.

**Réexamen marché U78 — C54/CMP042 :** le mot réservation recouvre plusieurs effets de produit. Microsoft peut réserver stock présent ou commandé non reçu ; SAP distingue Reservation de mouvement planifié et quantités réservées par Supply Assignment dans aATP. TER016/TER017 restent des définitions locales ; elles ne prouvent pas deux objets ou cycles indépendants. Une réservation sur ressource future ne décrit pas l’état d’un stock physique déjà présent. Préserver les sens U76 sans faire présent/futur la frontière automatique des domaines.

**Complément U79 — ressources futures :** [analyse dans la carte](25-domaines-coeur-et-epreuve-recits.md#stock-futur-potentiel-et-ressources-attendues-u79), A53 et CMP043. L’aptitude à représenter le futur et la décision de le mobiliser restent distinctes ; le potentiel contractuel ne constitue pas automatiquement une réception attendue datée. TER008 reste inchangé ; TER043 explicite le terme plus large employé par Laurent.

**Précision U80 — F184/A54 :** Laurent confirme la gestion du stock futur dans Inventory Management et Order Promising. Distinguer date d’arrivée/réception, date de disponibilité pour un usage et date de promesse au destinataire. La date de promesse dépend aussi de l’approvisionnement et de la mise à disposition amont. Cette orientation n’impose ni modèle d’objet commun ni transfert d’autorité des faits sources.

**Clarification courante U81 — F185/A55/C55 :** Inventory Management gère explicitement le stock physique TER040 et ses états logiques TER041 ; il connaît aussi les ressources futures TER043. Order Promising calcule le stock virtuel TER042 pour l’usage et l’horizon considérés et l’utilise pour déterminer une promesse quantité/date. Cela précise le partage esquissé en U77. Le stock logique n’est pas un autre lot de biens et le stock virtuel n’est pas une ressource supplémentaire. Les calculs de positions ou d’états dans D01 restent nécessaires ; calcul et confirmation de promesse sont distincts. Les définitions U76 demeurent conservées.

## Quantités, comptage et exactitude — revue de vocabulaire U82

- **Stocktaking / stock-take :** vocabulaire de comptage ; SAP emploie stock-taking dans l’explication de Physical Inventory. Stocktaking est proposé comme titre court, avec la définition de rapprochement et de correction conservée.
- **Inventory counting / Count inventory :** comptage ; Count inventory est un nom de processus Microsoft, Counting un type de journal. Cela peut éclairer une aptitude métier sans importer le processus ou le produit.
- **Inventory accuracy :** exactitude ou fiabilité des quantités enregistrées au regard des constats. Finalité proposée de D01.d, pas synonyme du comptage qui y contribue.
- **Truth / Inventory Accuracy Assurance :** pistes U82, sans libellé natif exact établi ; Truth trop absolu selon A56. Accuracy Assurance est une formulation plus naturelle que accuracy ensurment, mais de portée à définir si elle doit couvrir plus que comptage/rapprochement.
- **Manage inventory quantities :** proposition locale pour remplacer Establish inventory positions, inspirée du SAP Managing Stocks by Quantity. La définition conserve états logiques et ressources futures ; ni renommage définitif ni fusion D01.a/D01.b.

Sources et limites : [ELM075/ELM076](../marche/elements.md#elm075), [CMP044](../marche/comparaisons.md#cmp044), A56/C56. Ces pistes ne créent pas de nouvelles notions TER ni de capacités ; [revue dans la carte](25-domaines-coeur-et-epreuve-recits.md#noms-des-capacités-de-stock-revue-u82).

**Proposition U83 — P82 :** [cinq capacités D01](25-domaines-coeur-et-epreuve-recits.md#proposition-de-cinq-capacités-d01-u83) : Inventory Tracking, Inventory Visibility, Stocktaking, Supply Protection et Inventory Reservation. Inventory Tracking est un nom local de connaissance et d’évolution des stocks, au-delà du suivi de lots ou transports. Les titres courts sont accompagnés de définitions actives ; ils ne constituent ni des notions TER nouvelles ni un renommage adopté. CMP045 qualifie les rapprochements.

**Précision U84 — Reservation et Counting :** Reservation est retenu sans préfixe par Laurent dans D01. Counting est proposé pour le comptage et rapprochement ; la définition inclut toujours constat, comparaison, qualification des écarts et corrections justifiées. Inventory accuracy reste la Finalité.

Vérification lexicale du 2026-09-11 : [Stocktaking](https://www.dictionary.com/browse/stocktaking), entrée indexée Dictionary.com examinée, forme sans tiret ; la forme stock-taking est employée par SAP dans le cours consulté en ELM075. Stocktacking ne correspond pas à la graphie voulue. Tentative d’ouverture de l’entrée Cambridge stocktaking : 403, contenu non lu. Ces appuis lexicaux ne sont pas des référentiels de capacités. [Microsoft Counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-journals), texte reconsulté, appui ELM076 ; pas de restriction de la capacité locale à un type de journal logiciel.

**Réexamen U85 — F189/A59 :** Stocktaking évoque faire l’inventaire ; Counting souligne le dénombrement. Les deux peuvent exprimer une aptitude indépendante des outils. Le critère déterminant proposé est la portée métier du titre, pas son emploi par un éditeur. La définition locale conserve comptage, rapprochement et corrections justifiées, avec Inventory accuracy comme Finalité ; nom encore à arbitrer dans P82.

**Décision courante U86 — 2026-09-11, Laurent :** **Stocktaking**, en un mot, est retenu pour la capacité de comptage, rapprochement des quantités et établissement des corrections justifiées. **Inventory accuracy** en exprime la Finalité. Cette décision clôt le choix de nom rouvert en U85 ; Counting reste le terme de marché et l’option historique, pas le nom local courant. Voir F190/A60/C58.

## ATP et vérification d’une possibilité de promesse — U90

| Repère | Notion | Définition et usage proposé | Limites et provenance |
| --- | --- | --- | --- |
| TER044 | Available-to-Promise — ATP | Quantité non engagée disponible pour soutenir une promesse à un horizon donné, dans le périmètre et selon les règles considérés. Son calcul et son contrôle contribuent à évaluer une possibilité de fourniture. | Appui APICS historique ELM082, rapproché des descriptions SAP/Microsoft ELM077/ELM080. Définition locale synthétique ; aucune formule unique adoptée. ATP ne signifie pas Availability To Promise et ne désigne ni la promesse confirmée ni toute la faisabilité incluant les capacités ou nouvelles fournitures à créer. |

**Proposition U90/A63 :** Promise Verification évalue une possibilité de promesse ; Promise Confirmation établit l’engagement. La vérification peut être mobilisée dans Promise Revision pour réexaminer un engagement existant. Supply Assignment établit sa couverture par des ressources. Ces liens n’imposent pas une séquence, un objet unique ni quatre applications. Les candidats et limites de couverture restent dans P83 et [CMP048](../marche/comparaisons.md#cmp048).

**Correction U92 et précision U91 :** Promise Verification, discuté ci-dessus, est rejeté. Promise Formulation est le nouveau candidat assistant : faire naître une proposition de promesse, son statut avant confirmation restant à éprouver. Employer décision pour les aptitudes de choix ajoutées ; distinguer capacité à décider, décision produite et autorité pour décider. Voir C60 et P83 ; ATP conserve TER044.

**Suite U93 :** Promise Proposal remplace le candidat rejeté Promise Formulation. Le nom court désigne l’aptitude à produire une proposition ; il ne doit pas être confondu avec la proposition produite. Acheminement désigne ici la chaîne permettant d’aller de la source à destination ; le choix d’une source ne suffit pas à le décrire. Fulfillment Route Decision ajouté à P83, avec frontière et propriétaire proposés ; C61/CMP050.

## CTP et ressources futures — U94

| Repère | Notion | Définition et usage proposé | Limites et provenance |
| --- | --- | --- | --- |
| TER045 | Capable-to-Promise — CTP | Raisonnement de faisabilité de promesse prenant en compte les moyens nécessaires pour rendre une fourniture disponible, au-delà des ressources déjà présentes ou attendues mobilisables. | Synthèse locale appuyée sur ELM084 Microsoft ; composants/capacités dans Supply Chain Management, production/achat/transfert nouveau dans Business Central. ATP comprend déjà le futur planifié. Les capacités de production sont des ressources, pas les Business Capabilities de la carte. Aucun algorithme universel ou domaine Manufacturing adopté. |

ATP/CTP peuvent contribuer à Promise Proposal ; le CTP n’est ni la réservation, ni l’affectation, ni le réexamen prioritaire. [Comparaison](../marche/order-promising-comparaison-capacites.md#atp-et-ctp-chez-microsoft-u94), CMP051. Les délais de préparation et de transport peuvent intervenir dans les deux raisonnements.

## Statut local ATP et CTP — U95

**Décision de Laurent, 11 septembre 2026 :** ATP (TER044) appartient à la promesse. CTP (TER045) est conservé dans le glossaire mais son placement dans la carte et son utilisation sont reportés. L’hypothèse d’analytics opérationnelle alimentant planification des commandes ou protection des stocks reste à explorer ; aucune attribution à un domaine analytique adoptée.

Les définitions de marché ci-dessus restent conservées : CTP peut soutenir directement la promesse dans les références Microsoft. La proposition U94 d’en faire une contribution locale de Promise Proposal est désormais différée. La liste validée d’Order Promising conserve Supply Creation Decision ; aptitude métier et méthode de calcul sont distinctes. Aucun nouveau terme ni changement de définition native.

## Référentiels externes et commandes — U97/U98

Définitions de travail fondées sur les précisions explicites de Laurent du 11 septembre 2026. Les libellés et leur rédaction sont une synthèse ; ils ne constituent pas un schéma technique ni des définitions universelles de marché.

| Repère | Notion | Définition et usage local | Limites et provenance |
| --- | --- | --- | --- |
| TER046 | Party | Partie identifiée dans le référentiel externe, à laquelle sont rattachées les responsabilités et relations utiles aux opérations. | U97 cite les personnes juridiquement responsables et une identité sans doublon ; types détaillés et autorités par attribut non arrêtés. D09 reçoit cette référence. |
| TER047 | Role | Rôle métier d’une Party dans une relation ou une opération, notamment client ou fournisseur. | Synthèse U97 : référentiel Party / Role distinct des habilitations RBAC de la couche processus ; aucun catalogue complet de rôles adopté. |
| TER048 | Agreement | Contrat de référence client ou fournisseur indiquant le ou les catalogues permettant de commander, le Party concerné et les conditions particulières utiles pour honorer la promesse d’une commande. | U97/U98 : maître externe, ingestion D11 ; une commande est distincte d’un Agreement. Liens par identifiants, sans cardinalités détaillées ni règle juridique universelle. |
| TER049 | Catalog | Catalogue de référence construit à l’extérieur, portant les références proposées à la commande, les prix et les zones géographiques d’application. | U97 : ingestion D12 ; distinguer le catalogue commercial de la totalité des caractéristiques du modèle produit. |
| TER050 | Reference Ingestion | Aptitude à recevoir les informations de référence et leurs évolutions pour les rendre utilisables dans les opérations, en conservant les liens et identifiants du maître externe. | Rédaction proposée pour appliquer U97 : seule aptitude retenue dans chacun des trois domaines ; administration, vérification des données et parcours de référencement externes. Aucune technologie prescrite. |

Les modèles Party / Role, Agreement et Catalog restent distincts. Les commandes transactionnelles D04 et les promesses D03 utilisent ces références selon leurs responsabilités propres ; leur présence dans le socle ne signifie pas que le socle est maître de leur contenu. Voir [la carte courante](25-domaines-coeur-et-epreuve-recits.md#référentiels-ingérés-u97u98).

**Précautions issues de l’audit U99 :** Agreement et Order restent distincts, mais chacun peut porter des engagements. Distinguer Product Reference, Catalog/Offering, référence tarifaire et prix appliqué ; il s’agit de distinctions proposées à approfondir, sans modifier TER048–TER050 ni présumer de nouveaux domaines. Voir [audit](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md), C65/P86.

## Précisions documentaires et article — U100

11 septembre 2026 ; définitions de travail reformulées par Codex, avec statut indiqué. [Note de référence](26-supply-documents-autorisations.md).

| Repère | Notion | Définition et usage local | Limites et provenance |
| --- | --- | --- | --- |
| TER051 | Movement Authorization | Autorisation métier de déplacer une marchandise dans un périmètre et sous des conditions, dont un document porte la preuve. | Sens fondé sur U100 ; nom anglais proposé. Ne vaut pas preuve de départ ou réception, ni habilitation RBAC. Cycle et autorité ouverts Q074. |
| TER052 | Product Reference | Référence de l’article indépendante des catalogues qui peuvent proposer le même SKU. | Autonomie confirmée U100 ; libellé proposé. D08.d reçoit ces informations, sans administration locale. Identité détaillée, source et attributs à préciser. |
| TER053 | Location | Lieu pouvant servir d’origine, destination ou étape d’un mouvement ; un point du réseau peut offrir un espace de stockage, sans que ce soit systématique. | Raffinement proposé à partir des points U100 : le lieu est à relier aux Party responsables. U102 confirme depuis Party ≠ lieu et demande Fulfillment Network ; détail et rang de domaine ouverts. |

TER050 Reference Ingestion s’applique désormais aux quatre références D09/D11/D08/D12 dans la carte 0.7 ; sa définition reste inchangée. U100 confirme la distinction article/catalogue proposée dans l’audit U99. La séparation des prix reste à examiner, Q071/Q072.

## Réseau de réalisation — U102

11 septembre 2026 : la distinction Party/lieu évoquée en TER053 est confirmée par Laurent ; sa proposition de Fulfillment Network remplace la réserve « Aucun domaine ou référentiel autonome supplémentaire adopté » concernant l’absence de demande de référentiel. Le rang de domaine et le détail du modèle restent proposés.

| Repère | Notion | Définition et usage local | Limites et provenance |
| --- | --- | --- | --- |
| TER054 | Fulfillment Network | Réseau de points et de relations décrivant les possibilités de réalisation des mouvements de marchandises ; référentiel distinct des Party auxquelles les lieux sont reliés. | Nom demandé en U102, orthographe normalisée hors verbatim ; définition proposée. D13.a reçoit les références ; nœuds, liaisons et attributs à préciser Q076. Ni quantité de stock, ni charge courante, ni parcours déjà choisi. |

Dans P81 0.8, TER050 Reference Ingestion s’applique à cinq références, D13 compris à titre proposé dans la continuité U97. Aucune maîtrise du réseau ni réalisation logistique attribuée à FLOW.


## Mouvements, registre et état de stock — U125/U126

13 septembre 2026 ; [comparaison CMP062](../marche/comparaisons.md#cmp062), sources ELM103–ELM105. Définitions proposées, sauf l’identification des mouvements de stock par Laurent.

| Repère | Terme | Sens et frontière |
| --- | --- | --- |
| TER055 | Stock movement / Inventory movement ; Goods movement chez SAP | Mouvement de stock : fait de variation de quantité, localisation ou qualification du stock. Inclut notamment réceptions, sorties, transferts et changements d’état sans déplacement physique. Les écritures et justificatifs qui le représentent restent à distinguer du fait. |
| TER056 | Ledger / Inventory Ledger | Registre ; grand livre dans un contexte comptable. Pour notre exploration : registre des écritures justifiant les variations du stock. Le terme ne désigne pas le mouvement lui-même et n’impose ni valorisation financière ni technologie de persistance. Inventory Ledger Management est un candidat de nom de capacité, non adopté. |

Inventory Movements décrit actuellement l’aptitude à enregistrer et qualifier les mouvements ; Inventory Tracking établit et actualise les quantités et états ; Inventory Visibility les rend consultables dans une vision cohérente. Ces trois résultats doivent rester distincts, avec des relations métier à approfondir.


### Record et Sourcing — U127/U128

13 septembre 2026. **Record Inventory Movements**, proposé par Laurent en U127, explicite l’aptitude à enregistrer les mouvements. Nom alternatif conservé dans le backlog, sans adoption définitive.

**Sourcing** désigne couramment, dans les achats, la recherche, l’évaluation et la sélection des fournisseurs : [SAP, Outlining Sourcing](https://learning.sap.com/courses/sourcing-in-sap-s4hana/outlining-sourcing-in-sap-s-4hana-), introduction indexée consultée le 2026-09-13, édition inconnue. Ce sens n’exprime pas l’enregistrement des mouvements.

**Event Sourcing** désigne un modèle d’architecture logicielle où une succession d’événements permet de conserver et reconstruire l’état : [Microsoft, Event Sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing), résumé indexé et [exemple officiel Cosmos DB](https://learn.microsoft.com/en-us/samples/azure-samples/cosmos-db-design-patterns/event-sourcing/) consultés le 2026-09-13. Ce sont des moyens de réalisation, pas le nom d’une aptitude métier indépendante des outils. Le fait de séparer mouvements et état n’impose pas ce choix. Le sens visé par Laurent en U128 reste ouvert.


### Nom adopté — U129

13 septembre 2026 : Laurent retient **Record Inventory Movements** pour la capacité D01.g. Ce nom exprime l’enregistrement des mouvements. Inventory Movements et Inventory Ledger Management restent des options historiques ; Ledger conserve son sens de registre. Définition et finalité de la capacité restent proposées.
