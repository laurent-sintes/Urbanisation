# Informations métier — cinq pilotes U465/U466

19 septembre 2026. Restitution dérivée de [l’annexe YAML du backlog](../../modeles/backlog/information-cards-U465.yaml), qui fait autorité pour ces propositions. Ce document est un support de lecture interne, pas une publication Atlas.

## Ce qui est maintenant explicite

**Proposition de satisfaction et engagement de satisfaction sont deux informations métier reliées.** U466 adopte cette distinction : une nouvelle proposition peut être examinée pendant que l’engagement actuel reste valable. Les noms anglais et les définitions détaillées restent des rédactions proposées.

Les cinq pilotes portent **14 fiches, 15 liens qualifiés et 21 contributions de capacités**. Chaque fiche explicite une question, son contexte minimal, son exemple et les raisons de ses choix de vocabulaire et de définition. Les 15 cas antérieurs sont repris ; quatre exemples complètent l’épreuve de granularité. Aucun résultat de recette humaine n’est revendiqué.

Le découpage sépare des sens utiles : demandé, répondu, accepté, constaté, restant ; référence, caractéristique, identifiant, autorité, réception ; proposé, engagé, affecté, réservé. Ces informations sont transverses aux capacités. Elles ne forment ni une nouvelle couche ni un niveau sous Comportement.

## Vue d’ensemble

| Pilote | Information proposée | Question métier |
| --- | --- | --- |
| Purchase | [Purchase Requirement](#pinfo-001) — Attendu d’achat | Qu’est-ce qui est demandé au fournisseur pour cette partie de l’achat ? |
| Purchase | [Supplier Response](#pinfo-002) — Réponse fournisseur | Quelle réponse le fournisseur apporte-t-il à cet attendu d’achat ? |
| Purchase | [Supplier Commitment](#pinfo-003) — Engagement fournisseur accepté | Quelles conditions de réalisation de cet achat sont actuellement retenues ? |
| Purchase | [Purchase Fulfillment Result](#pinfo-004) — Réalisation d’achat constatée | Qu’a-t-on constaté comme réalisé pour cet attendu d’achat ? |
| Purchase | [Purchase Fulfillment Balance](#pinfo-005) — Reste à réaliser d’achat | Que reste-t-il à réaliser au regard de l’attendu actuellement applicable ? |
| Product | [Product Reference Identity](#pinfo-006) — Identité de référence produit | De quelle référence de produit ou variante parle-t-on ? |
| Product | [Product Characteristic](#pinfo-007) — Caractéristique produit | Quelle caractéristique est affirmée pour cette référence dans ce contexte ? |
| Product | [Product Identifier Association](#pinfo-008) — Association d’identifiant produit | À quelle référence correspond cet identifiant dans ce système d’identification ? |
| Product | [Reference Authority](#pinfo-009) — Autorité sur l’information de référence | Quelle autorité fait foi pour cette information dans ce périmètre ? |
| Product | [Reference Receipt](#pinfo-010) — Réception d’information de référence | Quel contenu de référence a été reçu, de qui et quand ? |
| Commitment | [Fulfillment Proposal](#pinfo-011) — Proposition de satisfaction | Quelles conditions de satisfaction sont proposées pour cette demande ? |
| Commitment | [Fulfillment Commitment](#pinfo-012) — Engagement de satisfaction | Quelles conditions de satisfaction sont actuellement promises pour cette demande ? |
| Assignment | [Supply Assignment](#pinfo-013) — Affectation de ressources | Quelle ressource est affectée à quelle demande, pour quelle part ? |
| Reservation | [Reservation](#pinfo-014) — Réservation de ressources | Quelle part de ressource est rendue indisponible aux demandes concurrentes, au bénéfice de qui ? |

## Comment lire ces fiches

- Lire la question métier avant les éléments essentiels ; ces derniers décrivent le sens, pas des colonnes obligatoires.
- Le minimum est relatif à la question et aux capacités. Il n’établit ni normalisation de données ni irréductibilité logique SBVR/ORM.
- Les liens décrivent une signification, ses conditions et son effet ; leur flèche n’est ni un flux technique ni une séquence imposée.
- Les rôles des capacités décrivent leur contribution ; aucun propriétaire exclusif, acteur installé ou architecture de composants n’est inféré.
- Objet, information, document et fait restent distincts. Les documents peuvent formaliser plusieurs informations ; tout fait de gestion a son document identifié U461.
- Les exemples sont illustratifs et contextualisés à partir des échanges ; aucune observation installée ni validation humaine des scénarios.

**Critère de maille.** Chaque fiche explique un sens autonome, avec les liens nécessaires à sa compréhension. Un ensemble de plusieurs échéances peut réunir plusieurs occurrences d’information ; le choix de cette maille ne démontre pas une irréductibilité logique. Il ne prescrit pas davantage un enregistrement ou une mise à jour technique indivisible.

**Documents et faits.** Purchase Order reste un objet métier, et les documents d’achat ou de réception gardent leur nature. Les fiches d’information en explicitent le contenu. Le résultat de réception associé à un fait de gestion conserve son document identifié, conformément à U461. Ni un poids produit ni un solde calculé ne deviennent automatiquement des faits de gestion.

## Les fiches

<a id="pinfo-001"></a>

### Purchase Requirement — Attendu d’achat

**Question :** Qu’est-ce qui est demandé au fournisseur pour cette partie de l’achat ?

Attendu exprimé envers un fournisseur pour une partie identifiée d’un achat : bien ou prestation, quantité ou résultat attendu, destinataire et conditions de réalisation demandées.

**Contexte :** Une partie de Purchase Order dont l’attendu peut être expliqué séparément. Une commande peut en réunir plusieurs ; aucune structure de ligne informatique imposée.

**Éléments qui portent le sens :**

- Commande et partie concernées ; fournisseur sollicité.
- Bien ou prestation et quantité avec unité, ou résultat attendu si la prestation n’est pas quantifiée.
- Destinataire, échéance et conditions nécessaires pour comprendre l’attendu.

**Pourquoi cette maille :** Conserver ensemble l’objet demandé, son étendue et ses conditions évite de confondre deux demandes du même bien. Une autre échéance autonome se décrit avec son propre attendu.

**Frontières :** La réponse fournisseur, les conditions acceptées et la réalisation répondent à d’autres questions. Prix ou modalités de paiement ne sont décrits ici que s’ils changent le sens de l’attendu étudié ; aucun dossier achat exhaustif.

**Capacités concernées :**

- Purchase Order (D04.j) **établit et fait évoluer** : Maintient l’attendu de l’achat selon les changements autorisés.
- Service Reconciliation (D07.c) **utilise** : Rapproche les résultats de service de ce qui était attendu.

**Exemple illustratif :** La partie A de l’achat PO-EXEMPLE-01 demande 100 pièces de la variante V au fournisseur F, livrées au site S vendredi. « 100 » seul ne dit ni quoi, ni pour qui, ni quand.

**Terme retenu :** Purchase Requirement est un libellé descriptif proposé pour l’attendu au sein d’un Purchase Order ; ce n’est ni une Purchase Requisition distincte ni un nom normalisé revendiqué.

**Définition et marché :** La documentation Microsoft distingue commande envoyée et réponse du fournisseur. FLOW en extrait l’attendu métier sans reprendre les états, lignes ou écrans du produit.

Appui : [MS-PURCHASE](#ms-purchase). Origines : U464, U465, U391, U403, U460, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03.

<a id="pinfo-002"></a>

### Supplier Response — Réponse fournisseur

**Question :** Quelle réponse le fournisseur apporte-t-il à cet attendu d’achat ?

Position reçue d’un fournisseur sur une partie d’achat demandée : acceptation, refus ou proposition de conditions différentes.

**Contexte :** Une réponse attribuée à un fournisseur et rattachée à l’attendu auquel elle répond ; ses conditions conservent leurs associations quantité–date.

**Éléments qui portent le sens :**

- Fournisseur répondant et attendu concerné.
- Position exprimée et conditions proposées ou motif de refus utile.
- Moment ou contexte permettant de distinguer cette réponse de celles qu’elle réexamine.

**Pourquoi cette maille :** Une réponse peut être reçue et étudiée sans être acceptée. Son sens autonome justifie une fiche distincte de l’engagement accepté.

**Frontières :** Réception d’une réponse ne vaut pas acceptation. Identité des révisions, délai de réponse et pouvoir d’acceptation restent ouverts.

**Capacités concernées :**

- Purchase Order (D04.j) **reçoit et connaît** : Supplier Confirmation BHV078 explicite les réponses et écarts à l’attendu.

**Exemple illustratif :** Pour 100 pièces demandées vendredi, F propose 60 vendredi et 40 mardi. La réponse est connue ; aucune acceptation de ces nouvelles conditions n’est supposée.

**Terme retenu :** Supplier Response conserve le sens métier des vendor responses Microsoft, avec Supplier déjà utilisé dans FLOW. L’information ne se limite pas à une confirmation positive.

**Définition et marché :** Acceptation, refus et changements documentés par Microsoft étayent la séparation entre réponse et conditions retenues. U466 ne valide pas cette séparation côté achats par extension.

Appui : [MS-PURCHASE](#ms-purchase). Origines : U464, U465, U403, U460, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03.

<a id="pinfo-003"></a>

### Supplier Commitment — Engagement fournisseur accepté

**Question :** Quelles conditions de réalisation de cet achat sont actuellement retenues ?

Conditions de réalisation retenues comme engagement du fournisseur pour une partie identifiée d’un achat, après l’acceptation requise dans ce contexte métier.

**Contexte :** Engagement relatif à l’achat fournisseur. Il ne se confond pas avec la promesse faite au bénéficiaire d’une autre commande.

**Éléments qui portent le sens :**

- Fournisseur et partie d’achat concernée.
- Quantité et unité, ou résultat attendu, associés aux échéances et conditions retenues.
- Référence au contexte d’acceptation qui permet de distinguer engagement et simple réponse.

**Pourquoi cette maille :** L’engagement peut rester valable pendant l’examen d’une réponse différente. Les preuves et règles permettant de le reconnaître restent à préciser, sans inférer une nouvelle règle d’autorisation.

**Frontières :** Ne désigne pas tout le dossier fournisseur. N’entraîne ni réception, ni nouvelle promesse client, ni réservation automatique.

**Capacités concernées :**

- Purchase Order (D04.j) **maintient** : Distingue l’attendu initial des conditions fournisseur effectivement acceptées.
- Fulfillment Commitment (D03.n) **utilise** : Prend en compte les conditions fournisseur pertinentes pour examiner la promesse de satisfaction, sans copie automatique.

**Exemple illustratif :** Les 60 pièces vendredi et 40 mardi sont acceptées pour cet achat. Une promesse client de 100 vendredi reste un engagement distinct à réexaminer ; elle n’est pas réécrite silencieusement.

**Terme retenu :** Supplier Commitment reprend le candidat existant en précisant ici « accepté ». Confirmed Purchase Order serait plus documentaire et trop large pour cette partie d’achat.

**Définition et marché :** Microsoft distingue réponse fournisseur et commande confirmée. L’engagement conceptuel proposé ne reprend ni la confirmation automatique du produit ni son modèle de versions.

Appui : [MS-PURCHASE](#ms-purchase). Origines : U464, U465, U403, U441, U460, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03.

<a id="pinfo-004"></a>

### Purchase Fulfillment Result — Réalisation d’achat constatée

**Question :** Qu’a-t-on constaté comme réalisé pour cet attendu d’achat ?

Résultat de réception d’un bien ou de réalisation d’une prestation, rapproché d’un attendu d’achat et qualifié avec ses éventuels écarts.

**Contexte :** Un résultat métier constaté pour une partie d’achat et un moment donnés ; aucune réalisation physique exécutée par la seule cartographie.

**Éléments qui portent le sens :**

- Attendu concerné et bien reçu ou prestation réalisée.
- Quantité avec unité ou résultat observé, moment et écarts utiles.
- Document métier identifié qui consigne le fait de gestion correspondant.

**Pourquoi cette maille :** Sans attendu, moment et quantité ou résultat, le constat ne permet pas de dire ce qui a été réalisé. Un autre constat indépendant garde son propre sens.

**Frontières :** Un résultat n’est ni l’engagement fournisseur ni le solde restant. Le lieu de constat, la validation de qualité et les corrections ne sont détaillés que si les règles métier l’exigent.

**Capacités concernées :**

- Service Reconciliation (D07.c) **rapproche et qualifie** : Rapproche les réalisations reçues des attendus et qualifie les écarts ; ne devient pas le réceptionnaire physique.
- Purchase Order (D04.j) **utilise** : Explique la progression de l’achat à partir des réalisations reconnues.

**Exemple illustratif :** REC-EXEMPLE-01 consigne la réception de 60 pièces sur les 100 attendues. Pour une prestation, un document identifié pourrait consigner le résultat observé ; son type et son auteur restent à établir.

**Terme retenu :** Purchase Fulfillment Result est proposé pour couvrir biens et prestations. Product receipt serait trop étroit ; Receipt Fact reste le cas illustré de réception.

**Définition et marché :** Le document de réception Microsoft fournit un exemple concret de constat documenté. Le lien obligatoire fait–document vient de U461 ; la généralisation aux prestations reste conceptuelle.

Appui : [MS-RECEIPT](#ms-receipt). Origines : U464, U465, U391, U460, U461, CMP184.

**Document / fait :** Le résultat rend compte d’un fait de gestion. U461 impose un document identifié ; son auteur, le nombre exact de documents, les corrections et les preuves d’acceptation ne sont pas inventés.

**À préciser :** V0-P03.

<a id="pinfo-005"></a>

### Purchase Fulfillment Balance — Reste à réaliser d’achat

**Question :** Que reste-t-il à réaliser au regard de l’attendu actuellement applicable ?

Part encore attendue d’un achat, expliquée à partir de l’attendu applicable et des réalisations reconnues dans un contexte d’appréciation donné.

**Contexte :** Une partie d’achat et une situation de référence explicites ; le reste peut être quantitatif ou exprimé comme résultat restant à atteindre.

**Éléments qui portent le sens :**

- Attendu applicable et contexte d’appréciation.
- Réalisations reconnues et ajustements métier applicables, lorsqu’ils sont établis.
- Reste à réaliser, avec unité ou résultat attendu et explication du rapprochement.

**Pourquoi cette maille :** Le solde répond à une question différente du dernier constat. On conserve ses bases d’interprétation pour ne pas confondre restant demandé, accepté et réalisé.

**Frontières :** Aucune formule universelle pour retours, annulations, dépassements ou prestations. Une information calculée n’est pas automatiquement un nouveau fait de gestion.

**Capacités concernées :**

- Purchase Order (D04.j) **connaît et fait évoluer** : Rend lisible la part restant à réaliser dans le suivi de l’achat.

**Exemple illustratif :** Dans le cas simple sans autre changement : 100 pièces encore applicables, 60 reconnues reçues, donc 40 restantes. Une annulation autorisée de 10 demanderait une règle explicite ; elle n’est pas déduite de cette soustraction.

**Terme retenu :** Purchase Fulfillment Balance est descriptif et proposé. Le vocabulaire exact d’un solde de réception ERP n’est pas adopté comme terme universel.

**Définition et marché :** Le suivi des réceptions éclaire le besoin ; la fiche FLOW est motivée par la question « que reste-t-il ? ». La source ne prouve pas une information autonome identique pour toutes les prestations.

Appui : [MS-RECEIPT](#ms-receipt). Origines : U464, U465, U391, U460, U461, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03.

<a id="pinfo-006"></a>

### Product Reference Identity — Identité de référence produit

**Question :** De quelle référence de produit ou variante parle-t-on ?

Identification métier du produit ou de la variante auxquels se rapportent les informations projetées dans Supply, avec les distinctions nécessaires pour les reconnaître.

**Contexte :** Une référence partagée de produit ou variante, distincte d’un exemplaire physique et de sa présence dans un catalogue.

**Éléments qui portent le sens :**

- Référence reconnue et nature Produit ou Variante.
- Pour une variante, produit de rattachement et combinaison de caractéristiques qui la distingue dans ce contexte.

**Pourquoi cette maille :** La référence fournit le sujet des autres informations sans absorber toutes ses caractéristiques. La combinaison distinctive d’une variante est utile à sa reconnaissance, sans prétendre être un fait logique élémentaire.

**Frontières :** Présence dans un catalogue, identifiant commercial et unité physique gardent des sens distincts. Article et Container restent des rôles déjà définis, sans créer ici de nouveaux types de produits.

**Capacités concernées :**

- Product Reference Ingestion (D08.d) **reçoit et projette** : Reconnaît les références externes dans la projection Supply.
- Purchase Order (D04.j) **utilise** : Désigne la référence concernée par l’achat sans devenir maître de sa définition.

**Exemple illustratif :** La variante V « modèle M, bleu, taille 38 » apparaît dans deux catalogues. Il s’agit d’une référence de variante, pas de deux variantes ni d’un exemplaire physique unique.

**Terme retenu :** Product et Product Variant sont déjà définis dans FLOW et présents chez Microsoft. Product Reference Identity décrit leur reconnaissance ; ce composé n’est pas revendiqué comme standard.

**Définition et marché :** La distinction produit/variante étaye le sujet projeté. La création et l’administration de maîtres décrites par Microsoft restent extérieures à Supply.

Appui : [MS-PRODUCT](#ms-product). Origines : U464, U465, U460, ELM280, ELM282, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P02.

<a id="pinfo-007"></a>

### Product Characteristic — Caractéristique produit

**Question :** Quelle caractéristique est affirmée pour cette référence dans ce contexte ?

Valeur d’une propriété d’un produit ou d’une variante, reliée à son sujet et au contexte dans lequel cette valeur s’applique.

**Contexte :** Une assertion de caractéristique utile aux capacités étudiées. Deux propriétés autonomes ou deux contextes contradictoires ne sont pas fusionnés en une valeur unique.

**Éléments qui portent le sens :**

- Référence concernée et propriété décrite.
- Valeur et unité lorsqu’elle est nécessaire au sens.
- Périmètre et période d’application utiles ; origine permettant de qualifier l’affirmation.

**Pourquoi cette maille :** « 0,4 kg » ne porte pas le sens étudié sans sujet et propriété. Couleur et poids répondent à deux questions autonomes ; on ne déclare pas toute la fiche produit insécable.

**Frontières :** Réception récente ne garantit pas validité actuelle. Une propriété n’exige pas un document distinct au titre de U461.

**Capacités concernées :**

- Product Reference Ingestion (D08.d) **reçoit et met à jour la projection** : Conserve les caractéristiques reçues avec le contexte permettant de les interpréter.

**Exemple illustratif :** L’émetteur A affirme « poids net de V : 0,4 kg, applicable au lot de fabrication considéré » ; B affirme 0,5 kg dans le même contexte. Les deux assertions sont compréhensibles, mais leur conflit ne se tranche pas par la date de réception seule.

**Terme retenu :** Product Characteristic désigne le sens métier commun des propriétés et attributes documentés. Attribute pourrait évoquer un champ de produit ; aucun schéma de champs n’est prescrit.

**Définition et marché :** Microsoft fournit des exemples de propriétés produit. Le choix d’une assertion contextualisée est la proposition de granularité FLOW, pas une équivalence avec son stockage des attributs.

Appui : [MS-PRODUCT](#ms-product). Origines : U464, U465, U460, ELM280, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P02.

<a id="pinfo-008"></a>

### Product Identifier Association — Association d’identifiant produit

**Question :** À quelle référence correspond cet identifiant dans ce système d’identification ?

Correspondance entre un identifiant interprété dans son système ou contexte d’attribution et la référence produit ou variante qu’il désigne.

**Contexte :** Identification d’une référence ; aucune unicité mondiale d’un code local ni identification implicite d’un exemplaire.

**Éléments qui portent le sens :**

- Valeur de l’identifiant et système ou contexte d’attribution.
- Référence désignée et périmètre d’application utile.

**Pourquoi cette maille :** Le même texte de code peut avoir des sens différents selon son émetteur. Sujet désigné et système d’identification sont indispensables à la correspondance.

**Frontières :** Identité métier et code qui la désigne ne sont pas synonymes. Une association GTIN–référence ne prouve pas l’identité d’une unité physique.

**Capacités concernées :**

- Product Reference Ingestion (D08.d) **reçoit et projette** : Conserve les correspondances reçues pour reconnaître les références.

**Exemple illustratif :** Le code fournisseur F:123 renvoie à V. Un identifiant de référence partagé par dix exemplaires ne suffit pas à distinguer ces dix unités ; GS1 illustre cette autre question par GTIN et numéro de série.

**Terme retenu :** Identifier est établi dans les sources Microsoft/GS1 ; Association explicite ici la correspondance métier. Aucun format d’identifiant FLOW n’est imposé.

**Définition et marché :** La distinction GS1 référence/instance borne le sens de cette fiche. Il ne s’agit ni d’une conformité GS1 ni d’une obligation de sérialiser toutes les unités.

Appui : [GS1-IDENTITY](#gs1-identity). Origines : U464, U465, U460, ELM280, ELM282, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P02.

<a id="pinfo-009"></a>

### Reference Authority — Autorité sur l’information de référence

**Question :** Quelle autorité fait foi pour cette information dans ce périmètre ?

Attribution d’une autorité métier sur un contenu de référence et un périmètre donnés, permettant d’expliciter à quel titre une information est tenue pour référence.

**Contexte :** Autorité sur une information ou un ensemble cohérent de propriétés ; aucune autorité unique sur toute la fiche produit supposée.

**Éléments qui portent le sens :**

- Rôle métier faisant autorité, s’il est établi.
- Contenu et périmètre couverts par cette autorité.
- Conditions de reconnaissance de l’autorité, lorsqu’elles sont connues.

**Pourquoi cette maille :** Un nom d’émetteur seul ne dit ni sur quoi il fait foi ni à quel titre. L’autorité a un sens distinct de la réception d’une valeur.

**Frontières :** L’émetteur peut être un intermédiaire. Pas de PIM, d’équipe, de système maître ou d’arbitre Beaumanoir inventé.

**Capacités concernées :**

- Product Reference Ingestion (D08.d) **utilise** : Interprète la projection à la lumière des autorités établies ; ne les attribue pas par simple ingestion.

**Exemple illustratif :** Une autorité externe pourrait faire foi sur les dimensions physiques, une autre sur une classification commerciale. Cet exemple illustre la portée d’une autorité ; il ne décrit aucune organisation installée.

**Terme retenu :** Reference Authority est une formulation descriptive proposée de la responsabilité faisant foi. Aucun objet éditeur homonyme n’a été établi dans les sources consultées.

**Définition et marché :** La séparation est motivée par la convention FLOW de projection et par V0-P02. Les références d’architecture soutiennent la description métier ; elles ne désignent pas les autorités locales.

Appui : [FLOW-PROJECTION](#flow-projection). Origines : U464, U465, U460, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P02.

<a id="pinfo-010"></a>

### Reference Receipt — Réception d’information de référence

**Question :** Quel contenu de référence a été reçu, de qui et quand ?

Contexte de réception d’un contenu de référence dans la projection Supply : contenu concerné, émetteur et moment de réception, avec l’origine connue utile à son interprétation.

**Contexte :** Une réception métier d’information ; pas un message technique ou un journal d’interface. Deux réceptions du même contenu peuvent éclairer sa fraîcheur sans changer sa validité.

**Éléments qui portent le sens :**

- Contenu de référence reçu, identifié sans en recopier tout le dossier.
- Émetteur et moment de réception.
- Origine déclarée et contexte de transmission lorsqu’ils sont utiles et connus.

**Pourquoi cette maille :** La fraîcheur de réception est relative à un contenu précis. Une date seule ne dit pas ce qui a été reçu ; une réception ne suffit pas à établir la vérité du contenu.

**Frontières :** Validité du contenu et heure de réception sont distinctes. Le seuil de fraîcheur dépend de l’usage ; aucune règle automatique d’acceptation ou de rejet.

**Capacités concernées :**

- Product Reference Ingestion (D08.d) **connaît** : Conserve le contexte utile de l’information reçue pour expliquer la projection.

**Exemple illustratif :** Une caractéristique valable au 1er septembre est reçue le 19 septembre par un distributeur. Sa réception est récente ; sa validité aujourd’hui et l’autorité de son origine restent à examiner.

**Terme retenu :** Reference Receipt décrit la provenance de réception pour les lecteurs métier ; aucun terme standard unique n’est revendiqué. Ce n’est pas Product Receipt, qui concerne les biens.

**Définition et marché :** La séparation réception/validité répond aux cas du pilote. Le besoin de provenance ne prescrit pas un flux, un mécanisme d’intégration ou un journal applicatif.

Appui : [FLOW-PROJECTION](#flow-projection). Origines : U464, U465, U460, CMP184.

**Document / fait :** La fiche décrit le contexte de provenance. Si l’arrivée est également modélisée comme fait de gestion, U461 exige son document identifié ; ce classement et ce document ne sont pas inventés ici.

**À préciser :** V0-P02.

<a id="pinfo-011"></a>

### Fulfillment Proposal — Proposition de satisfaction

**Question :** Quelles conditions de satisfaction sont proposées pour cette demande ?

Conditions de satisfaction proposées pour une partie identifiée d’une demande, soumises à confirmation sans valoir à elles seules engagement.

**Contexte :** Une proposition relative à une demande. Elle peut concerner un engagement initial ou une révision ; un engagement actuel peut rester valable pendant son examen.

**Éléments qui portent le sens :**

- Demande et partie concernées ; destinataire de la proposition.
- Quantité avec unité associée à la date et aux conditions proposées.
- Contexte de proposition ; engagement concerné en cas de réexamen.

**Pourquoi cette maille :** Proposition et engagement ont des sens et effets distincts, adoptés U466. Dans chacun, préserver l’association partie–quantité–date ; un échéancier peut réunir plusieurs parties sans devenir un fait élémentaire unique.

**Frontières :** La proposition n’est pas une réservation ni une affectation. Identités, versions, durée de validité et acceptation partielle restent à préciser.

**Capacités concernées :**

- Fulfillment Commitment (D03.n) **établit et révise** : Promise Proposal BHV021 formalise ce qui peut être proposé sans refaire la décision d’échéancier.
- Delivery Schedule Decision (D03.l) **détermine les conditions utilisées** : Delivery Schedule Decision choisit la distribution quantité–date qui alimente la proposition ; ne la confirme pas pour autant.

**Exemple illustratif :** L’engagement actuel prévoit 100 pièces vendredi. Une proposition de révision prévoit 60 vendredi et 40 lundi. Tant que le changement n’est pas confirmé selon les règles applicables, l’engagement actuel reste distinct et valable.

**Terme retenu :** Fulfillment Proposal est proposé en cohérence avec Fulfillment Commitment et Promise Proposal BHV021. Delivery Schedule ne distinguerait pas à lui seul proposition et engagement.

**Définition et marché :** Microsoft et Oracle illustrent les répartitions quantité–date ; U466 fonde la séparation des deux informations. Les sources ne prouvent pas une taxonomie commune à tous les éditeurs.

Appui : [MARKET-PROMISE](#market-promise). Origines : U464, U465, U441, U443, U466, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03, V0-A02.

**Portée U466 :** distinction et coexistence adoptées ; noms, rédaction et règles détaillées proposés.

<a id="pinfo-012"></a>

### Fulfillment Commitment — Engagement de satisfaction

**Question :** Quelles conditions de satisfaction sont actuellement promises pour cette demande ?

Conditions de satisfaction confirmées pour une partie identifiée d’une demande : ce qui est promis, à qui, pour quelle quantité et quelle date, sous les conditions métier applicables.

**Contexte :** Engagement métier distingué de la capacité homonyme qui le maintient. Une proposition peut préparer sa révision sans le remplacer automatiquement.

**Éléments qui portent le sens :**

- Demande et partie concernées ; bénéficiaire de l’engagement.
- Quantité avec unité associée à la date et aux conditions confirmées.
- Contexte de confirmation permettant de reconnaître l’engagement applicable.

**Pourquoi cette maille :** Le même couple quantité–date peut être proposé ou engagé : son effet métier diffère. L’engagement n’inclut pas toute la ressource choisie pour l’honorer.

**Frontières :** N’attribue pas de ressource précise et ne bloque pas les usages concurrents. Les règles de confirmation, correction, remplacement et effets sur d’autres commandes restent ouvertes.

**Capacités concernées :**

- Fulfillment Commitment (D03.n) **confirme et fait évoluer** : Promise Confirmation BHV022 et Promise Revision BHV023 maintiennent les conditions engagées.

**Exemple illustratif :** 60 pièces vendredi et 40 lundi sont confirmées. Affecter demain une autre ressource compatible peut conserver exactement cet engagement. Une nouvelle proposition de dates reste une information distincte.

**Terme retenu :** Fulfillment Commitment reprend le nom adopté de la capacité U445 pour l’information qu’elle entretient ; la nature Information évite de les confondre.

**Définition et marché :** Le nom et le périmètre restent FLOW. Confirmation de commande chez un éditeur n’est pas une équivalence complète ; l’absence de réservation implicite est la convention U436.

Appui : [MARKET-PROMISE](#market-promise). Origines : U464, U465, U441, U443, U445, U436, U466, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-P03, V0-A02.

**Portée U466 :** distinction et coexistence adoptées ; noms, rédaction et règles détaillées proposés.

<a id="pinfo-013"></a>

### Supply Assignment — Affectation de ressources

**Question :** Quelle ressource est affectée à quelle demande, pour quelle part ?

Lien retenu entre une ressource et une partie de demande à satisfaire, avec la quantité et les conditions d’application de cette affectation.

**Contexte :** Une affectation identifiée par son sens ressource–demande, distincte du plan qui l’a choisie, de la promesse et du droit de réservation.

**Éléments qui portent le sens :**

- Ressource concernée et demande bénéficiaire.
- Quantité avec unité et contexte d’application.
- Conditions particulières de maintien, par exemple un gel, seulement lorsqu’elles sont explicites.

**Pourquoi cette maille :** Ressource seule ou quantité seule ne dit pas à quelle demande elle est affectée. Plusieurs liens peuvent composer un plan sans fusionner leur sens.

**Frontières :** Un gel limite la modification de l’affectation ; il ne réserve pas automatiquement. L’affectation peut changer sans modifier la promesse si les conditions restent compatibles.

**Capacités concernées :**

- Supply Assignment (D02.e) **établit et fait évoluer** : Applique et maintient les liens choisis ; ne décide pas à nouveau le plan.
- Fulfillment Plan Decision (D03.o) **détermine le choix utilisé** : Fulfillment Plan Decision choisit le scénario dont découlent les affectations à appliquer.

**Exemple illustratif :** 40 pièces affectées depuis A à la demande L sont réaffectées depuis B. Si la même date et les mêmes conditions sont possibles, la promesse reste inchangée. Sans réservation, ce lien ne bloque pas les usages concurrents.

**Terme retenu :** Supply Assignment conserve le vocabulaire FLOW d’affectation. Pegging est un terme produit de rapprochement offre–demande ; Allocation peut désigner d’autres droits ou protections.

**Définition et marché :** La préservation de liens pour une demande confirmée chez Microsoft éclaire le maintien d’une affectation. Son paramétrage ne prescrit ni le gel FLOW ni un blocage implicite.

Appui : [MS-ASSIGNMENT](#ms-assignment). Origines : U464, U465, U345, U364, U436, U443, U460, ELM284, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-A02.

<a id="pinfo-014"></a>

### Reservation — Réservation de ressources

**Question :** Quelle part de ressource est rendue indisponible aux demandes concurrentes, au bénéfice de qui ?

Droit établi pour un besoin bénéficiaire sur une quantité de ressources définies par un périmètre, qui bloque les usages concurrents selon les conditions de réservation applicables.

**Contexte :** Périmètre de ressources suffisamment défini pour comprendre ce qui est réservé ; pas nécessairement un lot ou exemplaire déjà affecté.

**Éléments qui portent le sens :**

- Besoin bénéficiaire et périmètre de ressources concerné.
- Quantité avec unité.
- Conditions métier de l’opposabilité ; limites de durée seulement lorsqu’elles sont établies.

**Pourquoi cette maille :** Quantité, périmètre et bénéficiaire forment le sens du droit. Un lot précis n’est pas indispensable à toute réservation ; son attribution répond à une autre question.

**Frontières :** Réservation n’est ni mouvement physique ni simple affectation. Expiration, libération, consommation et effets d’une annulation ne sont pas automatisés par la définition.

**Capacités concernées :**

- Reservation (D02.c) **établit et fait évoluer** : Maintient le droit opposable selon les règles métier de réservation.
- Supply Assignment (D02.e) **utilise** : Tient compte des droits de réservation lors de l’application d’une affectation.

**Exemple illustratif :** 40 pièces de V sur le périmètre P sont réservées au besoin L, sans lot choisi. Les demandes concurrentes doivent tenir compte de ce droit ; l’annulation de L ne prouve pas à elle seule une règle de libération automatique.

**Terme retenu :** Reservation est un terme établi ; FLOW conserve le nom de la capacité et précise son effet métier. Soft reservation est un mécanisme particulier, pas le nom imposé à toute réservation.

**Définition et marché :** Microsoft illustre la diminution de la quantité disponible à réserver sans mouvement de stock. La portée exclusive du blocage dans FLOW vient de U436 ; les options produit d’overselling ou de libération ne sont pas importées.

Appui : [MS-RESERVATION](#ms-reservation). Origines : U464, U465, U436, U460, ELM283, CMP184.

**Document / fait :** Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.

**À préciser :** V0-A01, V0-A02, V0-A06.

## Liens : sens, conditions et effets

Ces liens sont propres au pilote. Ils ne remplacent pas les relations publiées et n’infèrent pas un flux technique depuis une dépendance.

### PILINK-01 — Supplier Response → Purchase Requirement

**Sens :** répond à l’attendu d’achat.

**Condition :** La réponse désigne l’attendu auquel elle se rapporte.

**Effet :** Rend l’écart demandé/proposé intelligible, sans modifier la demande.

Origines : U403, U460.

### PILINK-02 — Supplier Commitment → Supplier Response

**Sens :** retient des conditions issues d’une réponse fournisseur.

**Condition :** Une acceptation selon les règles applicables est établie ; son autorité reste ouverte.

**Effet :** Distingue les conditions retenues de celles encore examinées ; aucune confirmation automatique.

Origines : U403, U460.

### PILINK-03 — Supplier Commitment → Purchase Requirement

**Sens :** précise les conditions acceptées pour l’attendu d’achat.

**Condition :** Les deux informations concernent la même partie d’achat.

**Effet :** Permet de comparer demandé et engagé sans effacer la demande initiale.

Origines : U403, U460.

### PILINK-04 — Purchase Fulfillment Result → Purchase Requirement

**Sens :** rend compte d’une réalisation de l’attendu.

**Condition :** Le résultat est rapproché de l’attendu ; le fait de gestion dispose de son document identifié.

**Effet :** Explique une réalisation partielle, complète ou un écart sans confondre engagement et fait.

Origines : U460, U461.

### PILINK-05 — Purchase Fulfillment Balance → Purchase Requirement

**Sens :** s’apprécie par rapport à l’attendu applicable.

**Condition :** La situation de référence et les modifications autorisées sont connues.

**Effet :** Explique le restant ; aucune formule universelle déduite.

Origines : U391, U460.

### PILINK-06 — Purchase Fulfillment Balance → Purchase Fulfillment Result

**Sens :** tient compte des réalisations reconnues.

**Condition :** Les réalisations concernées sont qualifiées et rattachées au même attendu.

**Effet :** Le solde est expliqué par les faits retenus ; il n’est pas le dernier constat recopié.

Origines : U460, U461.

### PILINK-07 — Supplier Commitment → Fulfillment Commitment

**Sens :** peut alimenter le réexamen d’un engagement de satisfaction.

**Condition :** Un lien métier entre cet achat et la demande promise est établi ; tous les achats ne sont pas dédiés.

**Effet :** Une réponse ou un changement fournisseur ne réécrit pas automatiquement la promesse.

Origines : U441, U460.

### PILINK-08 — Product Characteristic → Product Reference Identity

**Sens :** décrit une caractéristique de la référence.

**Condition :** Sujet et contexte d’application sont identifiés.

**Effet :** La valeur est interprétable sans assimiler toute la fiche produit à une information unique.

Origines : U460, U464.

### PILINK-09 — Product Identifier Association → Product Reference Identity

**Sens :** désigne la référence dans un système d’identification.

**Condition :** Le système et le périmètre de l’identifiant sont connus.

**Effet :** Permet la reconnaissance de la référence sans désigner automatiquement une unité physique.

Origines : U460, ELM282.

### PILINK-10 — Reference Authority → Product Characteristic

**Sens :** qualifie l’autorité sur un contenu de référence.

**Condition :** Une autorité et sa portée sont effectivement établies ; elles peuvent rester inconnues.

**Effet :** Éclaire à quel titre une caractéristique fait référence ; n’attribue pas ce droit à l’émetteur par défaut.

Origines : U460.

### PILINK-11 — Reference Receipt → Product Characteristic

**Sens :** situe la réception d’un contenu de référence.

**Condition :** Le contenu reçu et son émetteur sont identifiés.

**Effet :** Distingue date de réception et validité de la caractéristique ; aucune autorité déduite.

Origines : U460.

### PILINK-12 — Fulfillment Proposal → Fulfillment Commitment

**Sens :** peut donner lieu à un engagement de satisfaction.

**Condition :** Les conditions proposées sont confirmées selon les règles métier applicables, encore à préciser.

**Effet :** L’engagement est distingué de la proposition ; ni réservation ni cardinalité un-à-un déduite.

Origines : U466, U436.

### PILINK-13 — Fulfillment Proposal → Fulfillment Commitment

**Sens :** peut proposer la révision d’un engagement existant.

**Condition :** La proposition vise un engagement actuel ; la révision n’est pas encore confirmée.

**Effet :** L’engagement actuel peut rester valable pendant l’examen de la proposition.

Origines : U466.

### PILINK-14 — Supply Assignment → Fulfillment Commitment

**Sens :** peut contribuer à honorer l’engagement.

**Condition :** Ressource affectée et conditions promises sont compatibles ; leur rattachement à la demande est établi.

**Effet :** L’affectation peut changer à promesse constante ; un retard peut nécessiter une nouvelle proposition sans réaffectation.

Origines : U436, U443, U460.

### PILINK-15 — Reservation → Supply Assignment

**Sens :** contraint l’utilisation des ressources lors de l’affectation.

**Condition :** Les périmètres se recoupent ; le bénéficiaire et les droits concurrents sont connus.

**Effet :** La réservation bloque les usages concurrents ; l’affectation ne crée pas ce droit et n’est pas nécessairement déjà établie.

Origines : U436, U460.

## Épreuve des cas déjà préparés

Cette matrice vérifie la capacité explicative du découpage. Les questions ouvertes et les résultats antérieurs de U460 sont conservés ; aucun cas ouvert n’est déclaré résolu par la seule rédaction.

| Cas | Lecture avec les informations | Règles encore ouvertes |
| --- | --- | --- |
| CASE-01 — Réception partielle documentée | Le constat documenté de 60 et le reste de 40 sont deux informations, rattachées au même attendu de 100. (PINFO-001, PINFO-004, PINFO-005) | Frontière expliquée, sans recette humaine |
| CASE-02 — Réponse fournisseur différente de la demande | La réponse 60/40 reste distincte des conditions d’achat acceptées ; qui accepte reste ouvert. (PINFO-001, PINFO-002, PINFO-003) | V0-P03 |
| CASE-03 — Achat d’une prestation | L’attendu peut décrire une prestation et son résultat ; les règles de reconnaissance de la prestation restent à préciser. (PINFO-001, PINFO-003, PINFO-004, PINFO-005) | V0-P03 |
| CASE-04 — Une variante dans deux catalogues | L’identité de référence n’est pas multipliée par le nombre de catalogues ou de codes qui la désignent. (PINFO-006, PINFO-008) | Frontière expliquée, sans recette humaine |
| CASE-05 — Deux descriptions contradictoires | Deux assertions contradictoires se décrivent avec leur origine ; la règle d’autorité n’est pas inventée. (PINFO-007, PINFO-009, PINFO-010) | V0-P02 |
| CASE-06 — Information reçue récemment mais ancienne | Réception récente et validité du contenu répondent à deux questions distinctes. (PINFO-007, PINFO-010) | V0-P02 |
| CASE-07 — Proposition sans confirmation | La proposition est distincte de l’engagement ; U466 permet leur coexistence sans confirmation implicite. (PINFO-011, PINFO-012) | Frontière expliquée, sans recette humaine |
| CASE-08 — Changement de ressource à conditions constantes | Un lien d’affectation peut évoluer à conditions promises constantes. (PINFO-012, PINFO-013) | Frontière expliquée, sans recette humaine |
| CASE-09 — Retard sans changement de ressource | Une nouvelle proposition peut viser l’engagement sans changement de la ressource affectée ; la règle de confirmation reste ouverte. (PINFO-011, PINFO-012, PINFO-013) | V0-P03 |
| CASE-10 — Affectation sans réservation | Le lien d’affectation est connu, le droit opposable n’est pas établi par ce seul lien. (PINFO-013, PINFO-014) | Frontière expliquée, sans recette humaine |
| CASE-11 — Affectation gelée | Le gel qualifie le maintien de l’affectation ; seul le droit de réservation bloque la concurrence. (PINFO-013, PINFO-014) | Frontière expliquée, sans recette humaine |
| CASE-12 — Plan recalculé | Un nouveau plan propose d’autres affectations ; appliquer, maintenir ou libérer les droits existants demande des règles explicites. (PINFO-013, PINFO-014) | V0-A02 |
| CASE-13 — Quantité réservée sans lot individuel | Le droit peut porter sur un périmètre de ressources avant le choix du lot. (PINFO-013, PINFO-014) | Frontière expliquée, sans recette humaine |
| CASE-14 — Échéance dépassée | L’information explique l’échéance connue ; elle n’invente pas ce que produit son dépassement. (PINFO-014) | V0-A01, V0-A06 |
| CASE-15 — Commande annulée | La demande bénéficiaire annulée et ses droits doivent être rapprochés ; libération, consommation ou réaffectation ne sont pas déduites. (PINFO-013, PINFO-014) | V0-A01, V0-A02, V0-A06 |

### Exemples supplémentaires

**Révision proposée, engagement encore valable.** 100 vendredi reste engagé pendant l’examen d’une proposition 60 vendredi / 40 lundi. Deux informations reliées ; l’existence de la proposition ne remplace pas l’engagement.

**Émetteur intermédiaire et autorité distincts.** Un distributeur transmet une caractéristique dont l’autorité déclarée est un autre rôle externe. Transmission, autorité et validité ont des sens distincts. Le cas ne prouve aucune source installée.

**Référence partagée, exemplaires distincts.** Dix exemplaires de la même variante portent le même identifiant de référence. La correspondance à la référence ne suffit pas à identifier chacun des dix exemplaires.

**Préserver les associations quantité–date.** 60 vendredi et 40 lundi ne signifient pas la même chose que 40 vendredi et 60 lundi. Le lien quantité–date est indispensable ; cela ne prouve pas qu’un échéancier complet est un fait élémentaire unique.

## Références et positionnement

Les références suivantes apportent des exemples et des concepts. Elles ne constituent ni une sélection de produits ni une preuve d’implémentation. Les mots descriptifs FLOW ne sont qualifiés ni standards ni innovants en l’absence de preuve. Les sources d’architecture de U464 restent des appuis méthodologiques, distincts des exemples éditeurs.

<a id="ms-purchase"></a>

### MS-PURCHASE

**Constat sourcé :** La documentation distingue réponses du fournisseur, acceptation ou changements proposés et confirmation de commande. Une version confirmée peut subsister pendant le traitement d’un changement.

**Point commun :** Attendu, réponse et conditions retenues sont compréhensibles séparément.

**Différence et limite FLOW :** FLOW propose des informations conceptuelles ; aucun état ERP, mécanisme de confirmation automatique, règle de version ni autorité d’acceptation n’est importé.

- [Microsoft — Vendor collaboration with external vendors](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors) — Working with POs ; Confirmation and acceptance ; Changing a PO. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.

Traçabilité : ELM242 ; CMP184. Rapprochement proposé par Codex.

<a id="ms-receipt"></a>

### MS-RECEIPT

**Constat sourcé :** L’exemple produit décrit un document identifié qui rend compte de la réception enregistrée.

**Point commun :** Illustre un constat de réception documenté et son rapprochement avec l’achat.

**Différence et limite FLOW :** Le lien obligatoire fait–document vient de U461. Les informations conceptuelles de prestation et de solde ne sont pas présentées comme des objets Microsoft identiques.

- [Microsoft — Record the receipt of goods on the purchase order](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order) — Record receipt of goods, étapes 4–7 ; consultation U461, mise à jour indiquée le 1er juillet 2026. Consultation : 2026-09-19. Appui repris de ELM285/CMP178, consulté pendant U461 le même jour. Une tentative de réouverture U465 n’a pas abouti ; aucun constat nouveau.

Traçabilité : ELM285, CMP178 ; CMP184. Rapprochement proposé par Codex.

<a id="ms-product"></a>

### MS-PRODUCT

**Constat sourcé :** La documentation distingue produits, variantes, propriétés et identifiants ; les variantes se définissent selon des combinaisons de dimensions.

**Point commun :** Aide à distinguer référence concernée et caractéristiques utiles.

**Différence et limite FLOW :** Le produit Microsoft inclut l’administration de maîtres. Les référentiels Supply FLOW sont des projections ; leurs autorités externes ne sont pas attribuées ici.

- [Microsoft — Product information overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information) — Product definition ; Product masters and product variants ; page indiquée mise à jour le 1er juillet 2026. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.

Traçabilité : ELM280 ; CMP184. Rapprochement proposé par Codex.

<a id="gs1-identity"></a>

### GS1-IDENTITY

**Constat sourcé :** GS1 illustre l’identification d’une instance par l’association du GTIN et d’un numéro de série.

**Point commun :** Un identifiant de référence ne suffit pas toujours à identifier un exemplaire.

**Différence et limite FLOW :** Aucun format GS1 imposé aux références FLOW ni obligation de sérialisation de chaque unité.

- [GS1 — Serialisation and unique identification](https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-) — FAQ, distinction GTIN et identification sérialisée ; modification indiquée le 28 août 2024. Consultation : 2026-09-19. FAQ officielle, pas lecture exhaustive des spécifications normatives GS1.

Traçabilité : ELM282, ELM280 ; CMP184. Rapprochement proposé par Codex.

<a id="flow-projection"></a>

### FLOW-PROJECTION

**Constat sourcé :** La cartographie d’information relie concepts métier et capacités indépendamment des réalisations informatiques.

**Point commun :** Autorité et provenance rendent la projection intelligible pour ses capacités utilisatrices.

**Différence et limite FLOW :** Le découpage Reference Authority / Reference Receipt est une proposition FLOW motivée par les cas U460 ; aucun objet normalisé homonyme ni autorité Beaumanoir prouvée.

- [TOGAF — Information Mapping, G190](https://governance.foundation/assets/frameworks/togaf/g190%20-%20Information%20Mapping.pdf) — Chapitres 1–2 et 4–6 ; lecture U464. Consultation : 2026-09-19. Document primaire de 2019 sur miroir tiers, relu en U464 ; aucune vérification de toute la 10e édition ni de règle d’autorité locale.

Traçabilité : U460, ELM269, ELM276, CMP183 ; CMP184. Rapprochement proposé par Codex.

<a id="market-promise"></a>

### MARKET-PROMISE

**Constat sourcé :** Microsoft et Oracle documentent des répartitions d’une demande en quantités associées à des dates ou ressources différentes.

**Point commun :** Les associations quantité–date doivent conserver leur sens dans une proposition comme dans un engagement.

**Différence et limite FLOW :** Ces sources illustrent les échéances ; elles ne démontrent pas deux concepts universels Proposal/Commitment. La distinction est adoptée par U466, avec versions et confirmations encore ouvertes.

- [Microsoft — Delivery schedules](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-schedules) — Delivery schedules ; répartition en plusieurs livraisons ; mise à jour indiquée le 7 mai 2025. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.
- [Oracle 26B — What’s a Split Order Line](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html) — Introduction et éclatement selon ressources ou dates. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.

Traçabilité : ELM220, ELM248, U466 ; CMP184. Rapprochement proposé par Codex.

<a id="ms-assignment"></a>

### MS-ASSIGNMENT

**Constat sourcé :** Microsoft décrit le maintien de liens de couverture pour les demandes confirmées et un contrôle du pegging du stock disponible.

**Point commun :** Un lien ressource–demande peut être maintenu ou réexaminé lors de la planification.

**Différence et limite FLOW :** Le mécanisme produit recoupe plusieurs capacités FLOW. Il ne prouve ni équivalence complète avec Supply Assignment ni réservation par une affectation FLOW.

- [Microsoft — Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) — What data is preserved ; Control how on-hand inventory is pegged ; documentation indiquée le 27 juillet 2026. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.

Traçabilité : ELM284 ; CMP184. Rapprochement proposé par Codex.

<a id="ms-reservation"></a>

### MS-RESERVATION

**Constat sourcé :** La réservation souple affecte la quantité disponible à réserver sans changer la quantité physique. Le service propose aussi des options de comportement.

**Point commun :** Le droit de réservation et le mouvement physique restent distincts.

**Différence et limite FLOW :** U436 définit l’opposabilité FLOW. Aucune option d’overselling, libération ou consommation Microsoft n’est adoptée ; le fonctionnement installé n’est pas évalué.

- [Microsoft — Inventory Visibility reservations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations) — Introduction ; Sample use case. Consultation : 2026-09-19. Page officielle consultée ; synthèse sans reproduction du contenu.

Traçabilité : ELM283, U436 ; CMP184. Rapprochement proposé par Codex.

## Bilan et suite

Les cinq pilotes permettent de distinguer des sens autonomes sans ajouter de niveau à Univers/Domaine/Capacité/Comportement.

**Modifications opérées :** catalogue pilote créé ; cinq pilotes reliés aux fiches tout en préservant leurs candidats initiaux ; exemple U466 ajouté à MOD012 et au brouillon du guide ; arbitrage, correspondances marché et suivi V0 actualisés. La définition générale de MOD012 reste inchangée et proposée.

**Prochaine étape recommandée :** Préparer le contrat minimal de catalogue et la lecture métier dans Atlas à partir de ces fiches : question, définition, contexte, liens, usages, exemples et marché. Conserver les règles non établies comme inconnues explicites, sans inventer de réalisation.

**Questions métier conservées :**

- V0-P02 : autorités des projections, conflits, fraîcheur par usage.
- V0-P03 : acceptation fournisseur et confirmation/révision des engagements ; reconnaissance des prestations.
- V0-A01/V0-A02/V0-A06 : coordination des affectations et droits, expiration, consommation et libération.

Faire relire les frontières et les mots par PO et experts ; cet exercice documentaire ne remplace pas leur revue.

**Contrôles ciblés réussis :** sources, capacités, liens, couverture des quinze cas, conservation des candidats et de leur revue antérieure, cohérence MOD012/guide. Les 306 empreintes protégées sont identiques, dont le catalogue métier, son glossaire, son schéma et 303 fichiers historiques. [Résultats du contrôle](verification.json).

Atlas reste sur sa publication actuelle : aucune fiche pilote n’est lue depuis le backlog. Aucun nouveau type canonique, changement UI ou publication n’est réalisé dans cette étape.

**Validation et tests exécutés :** validation des modèles à zéro erreur ; 17 tests du guide réussis, 1 ignoré car Windows n’autorise pas la création de liens symboliques. Index des sources actualisé à 1 681 entrées. [Trace des commandes](execution-checks.json). Aucun build frontend requis pour ces modifications documentaires.
