# Corrections et précautions de lecture

Import initial : [référentiel JSON archivé](../archive/referentiel.json), section `corrections`, consolidation du 9 septembre 2026. Les entrées importées conservent leur provenance ; les compléments et corrections d’audit sont datés et sourcés.

## C01

**id**

C01

**source**

U01;U02

**formulation_a_eviter**

Sarenza uniquement marketplace tiers

**formulation_retenue**

Retenir l’activité de revente B2C de catalogues fournisseurs décrite ; conserver le qualificatif initial de plateforme sans en inférer toutes les responsabilités.

**statut**

Clarifié

## C02

**id**

C02

**source**

U03;A03

**formulation_a_eviter**

UR = uniquement OMS eCommerce

**formulation_retenue**

Séparer périmètre générique du produit et rôle du déploiement GBM ; ne pas inventer des modules utilisés.

**statut**

Clarifié

## C03

**id**

C03

**source**

U03;A03

**formulation_a_eviter**

UR ne sait jamais faire du ship-from-store

**formulation_retenue**

Conserver le constat de limite du déploiement GBM ; une capacité produit annoncée ne prouve ni disponibilité ni usage dans la version installée.

**statut**

Précaution

## C04

**id**

C04

**source**

U03

**formulation_a_eviter**

Storeland fait aussi la caisse

**formulation_retenue**

Attribuer caisse et commandes client en magasin aux logiciels POS spécialisés.

**statut**

Clarifié

## C05

**id**

C05

**source**

U03

**formulation_a_eviter**

Pas de middleware = pas d’intégration transverse

**formulation_retenue**

Distinguer architecture Oracle/Storeland et plateforme Talend transverse.

**statut**

Clarifié

## C06

**id**

C06

**source**

U03;U07

**formulation_a_eviter**

C-Log est une application

**formulation_retenue**

C-Log est une filiale avec DSI ; distinguer organisation, SI, OMS Crossroad et autres outils.

**statut**

Confirmé

## C07

**id**

C07

**source**

U04;U05

**formulation_a_eviter**

Annulation de la commande client après 15 minutes

**formulation_retenue**

Seule la demande magasin est annulée ; la commande client persiste ; nouvelle tentative magasin.

**statut**

Confirmé

## C08

**id**

C08

**source**

U04

**formulation_a_eviter**

Escalade en fin de journée certaine

**formulation_retenue**

Conserver « dans la journée, il me semble » comme délai incertain.

**statut**

Réserve maintenue

## C09

**id**

C09

**source**

U06;U07

**formulation_a_eviter**

SCO-TEX

**formulation_retenue**

Nom normalisé SCORTEX ; conserver le nom antérieur uniquement dans l’historique/verbatim.

**statut**

Confirmé

## C10

**id**

C10

**source**

U06;U07

**formulation_a_eviter**

Crossroad est l’éditeur

**formulation_retenue**

KBRW est l’éditeur ; Crossroad est le logiciel.

**statut**

Confirmé

## C11

**id**

C11

**source**

U06

**formulation_a_eviter**

IRMA a déjà remplacé SCORTEX partout

**formulation_retenue**

Déploiement en cours ; inventaire des périmètres de migration non fourni.

**statut**

Réserve maintenue

## C12

**id**

C12

**source**

U07;U09

**formulation_a_eviter**

Recentrer la carte sur information et décision

**formulation_retenue**

La carte reste métier ; prendre ces notions en compte au niveau d’urbanisme pertinent, encore à définir.

**statut**

Confirmé

## C13

**id**

C13

**source**

U07

**formulation_a_eviter**

Absorber le SI C-Log dans le futur ERP

**formulation_retenue**

Hors objectif ; documenter la frontière de responsabilité et les décisions éventuellement à redéfinir.

**statut**

Confirmé

## C14

**id**

C14

**source**

U02;A02;A06

**formulation_a_eviter**

Les deux plateformes sont les deux branches L1 de la carte

**formulation_retenue**

Les deux plateformes sont une orientation de réalisation ; la décomposition métier reste distincte.

**statut**

Proposition cohérente, à formaliser

**precision_2026_09_09**

U18/U19 affinent l’orientation : chaque couche a son modèle, ses objets, sa persistance et sa propre urbanisation. Ne pas utiliser C14 pour nier ces deux urbanisations ou imposer une vue globale unique. Leur découpage interne et le vocabulaire du catalogue restent à préciser ; P60 propose un rapprochement au marché sans renommer les capacités.

## C15

**id**

C15

**source**

U10

**formulation_a_eviter**

MAP est sur Snowflake avec certitude

**formulation_retenue**

Hypothèse explicite ; contrairement à IRMA, la plateforme de MAP n’est pas confirmée.

**statut**

Réserve maintenue

## C16

**id**

C16

**source**

U06;U10

**formulation_a_eviter**

MAP et IRMA font le même calcul de seuils

**formulation_retenue**

IRMA : réassort magasin ; MAP : prévisions/protection marque-canal/stockage/achats. Relations et recouvrements à établir.

**statut**

Clarifié

## C17

**id**

C17

**source**

U10

**formulation_a_eviter**

Annule et remplace = annulation des ventes

**formulation_retenue**

MAP remplace des données dans le système opérant ; objets et effets sur engagements inconnus.

**statut**

Réserve maintenue

## C18

**id**

C18

**source**

U10

**formulation_a_eviter**

GBM réalloue au client Gold comme l’exemple hypothétique

**formulation_retenue**

Scénario explicitement écarté du fonctionnement décrit : pas de repriorisation commerciale.

**statut**

Confirmé

## C19

**id**

C19

**source**

U10

**formulation_a_eviter**

FIFO décrit la rotation des lots physiques

**formulation_retenue**

Dans le récit, FIFO désigne l’ordre de service des demandes.

**statut**

Clarifié

## C20

**id**

C20

**source**

U10

**formulation_a_eviter**

Vente sur stock garantit l’absence technique de survente

**formulation_retenue**

Politique nominale déclarée ; garanties de synchronisation et stock réel restent à instruire.

**statut**

Réserve maintenue

## C21

**id**

C21

**source**

U01;U10

**formulation_a_eviter**

Documenter MAP réintègre toute la planification amont

**formulation_retenue**

Conserver le contexte et les interfaces ; statut de frontière pour protections/achats, sans élargissement implicite.

**statut**

Précaution de périmètre

## C22

**id**

C22

**source**

U03;U10

**formulation_a_eviter**

CBS est forcément toute l’application achats sur mesure initiale

**formulation_retenue**

Rapprochement plausible mais non confirmé ; MAP produit la demande, CBS suit l’amont.

**statut**

Réserve maintenue

## C23

**id**

C23

**source**

U10

**formulation_a_eviter**

Une demande d’achat est déjà une commande ferme

**formulation_retenue**

Ne pas poser cette équivalence sans connaître validation, émission fournisseur et engagement.

**statut**

Réserve maintenue

## C24

**id**

C24

**source**

A08;A09;U13

**formulation_a_eviter**

Les notes mémorisées constituent déjà un dossier versionné

**formulation_retenue**

Avant cette livraison, pas de document maître créé dans le fil ; la version 0.1 constitue le premier dossier effectif.

**statut**

Écart traité

## C25

**id**

C25

**source**

A02

**formulation_a_eviter**

Commande = état de la Demande, doctrine validée dans ce fil

**formulation_retenue**

Formulation introduite par l’assistant en rappel d’un autre contexte ; conserver comme proposition/rappel non validé dans ce corpus. Ne pas imposer un modèle d’objet unique.

**statut**

Statut corrigé

**precision_audit_2026_09_09**

Formulation exacte retrouvée dans T04 : « commande = état d’engagement de la Demande ». Le raccourci initial omettait « engagement » ; le statut non validé reste inchangé.

## C26

**id**

C26

**source**

A06;U07

**formulation_a_eviter**

Capacités logistiques candidates toutes incluses dans le cœur ERP

**formulation_retenue**

Conserver les responsabilités comme interfaces/frontière ; exécution C-Log hors décomposition détaillée de la cible commerce.

**statut**

Statut corrigé

## C27

**id**

C27

**source**

U08;U12

**formulation_a_eviter**

Relances utilisateur ignorées

**formulation_retenue**

Conserver la trace des deux interruptions et le besoin de livraisons effectives/retours visibles. Aucune information métier supplémentaire à inférer.

**statut**

Traçabilité

## C28

**id**

C28

**source**

T06 ; R23 ; audit du 2026-09-09

**formulation_a_eviter**

Annonce Cegid 2019 sans référence exploitable dans le fil

**formulation_retenue**

Lien retrouvé et annonce officielle corroborée ; ne prouve aucun usage GBM. A03/R23 actualisés.

**statut**

Correction documentaire à l’audit ; pas de nouvelle validation métier.

## C29

**id**

C29

**source**

T08 ; P32 ; Q018

**formulation_a_eviter**

Sélection ne vaut ni acceptation ni réservation

**formulation_retenue**

Sélection distincte de l’acceptation ; éventuel effet et moment de réservation inconnus. Réserve rendue explicite, Q018 reste ouverte.

**statut**

Correction documentaire à l’audit ; pas de nouvelle validation métier.

## C30

**id**

C30

**source**

U06 ; F069 ; Q009 ; DEC02

**formulation_a_eviter**

Coexistence SCORTEX formulée sans réserve

**formulation_retenue**

Coexistence éventuelle avec SCORTEX, à préciser par périmètre ; aucune présence simultanée locale confirmée.

**statut**

Correction documentaire à l’audit ; pas de nouvelle validation métier.

## C31

**id**

C31

**source**

U24 ; MKT04 ; cours SAP Discovering the Reference Architecture Content, sections Reference Architecture Content Example et Business Capability Model Example ; contrôle Codex du 2026-09-09.

**formulation_a_eviter**

« Hiérarchie des capacités à trois niveaux » présentée comme complète ; CMP001 : « les deux options envisagent trois niveaux » ; tableau de réponse à U23 omettant Enterprise Domain.

**formulation_retenue**

Restituer Enterprise Domain → Business Domain → Business Area → Business Capability. Pour le stock : Supply – Fulfill Demand → Supply Chain Execution → Inventory Management → par exemple Physical Inventory. Le cours décrit les trois niveaux de décomposition du modèle puis leur regroupement supérieur en Enterprise Domains. Inventory Management demeure un Business Area.

**statut**

Correction documentaire appliquée : note SAP-stock, MKT04, ELM001/ELM014, CMP001/CMP013, A16, R03 et navigation. Aucune décision de hiérarchie Beaumanoir.

## C32

**id**

C32

**source**

U30 ; U31 ; F117/F120/F121 ; mise à jour Codex du 2026-09-09.

**formulation_a_eviter**

Après U30, présenter encore la réservation GBM comme un simple candidat sans principe déclaré, et conserver « GBM FIFO ; BRD à explorer » comme seule description de CAP035. Q018/Q049 avaient pour réponse « — ».

**formulation_retenue**

GBM : réservation au passage de commande déclarée au niveau métier ; détails SFS/autorités encore ouverts. BRD : besoin explicite des comportements cités, dont engagement futur et réaffectation prioritaire ; réalisation installée à explorer. Q018/Q049 partiellement renseignées, sans fermeture. U31 propose la révision des promesses côté Order Promising ; pas de reclassement CAP validé.

**statut**

Actualisation de connaissance sourcée, anciennes formulations conservées ici. Les résultats et statuts candidats CAP sont inchangés.

## C33

**id**

C33

**source**

U33 ; F123/F124 ; P70 ; CMP024 ; correction du 2026-09-09.

**formulation_a_eviter**

P70 et la note de granularité proposaient de décomposer selon un résultat métier distinct utile pour attribuer une responsabilité ou définir un contrat durable. Ce critère ne rappelait pas explicitement l’indépendance de l’aptitude envers l’organisation et les outils.

**formulation_retenue**

Décomposer uniquement lorsque plusieurs aptitudes métier durables et intelligibles se distinguent, indépendantes de l’organisation et des outils, dans le périmètre parent. Le résultat aide à décrire l’aptitude ; responsabilités et contrats éclairent ensuite sa réalisation et ne justifient pas à eux seuls une capacité.

**statut**

Précision méthodologique appliquée à AGENTS.md, P70, à la note et à CMP024. Définition utilisateur réaffirmée ; aucune définition CAP modifiée.

## C34

**id**

C34

**source**

U34 ; U35 ; A22 ; TER027/TER028/TER029 ; VER002 ; 2026-09-09.

**formulation_a_eviter**

L’emploi non qualifié de fonction dans les réponses sur les produits pouvait suggérer un étage hiérarchique. Les formulations tenir les protections / tenir les engagements pouvaient être comprises comme une terminologie SAP reconnue.

**formulation_retenue**

Dans ce contexte, fonction désignait surtout une fonctionnalité de produit ; employer regroupement de capacités pour une agrégation dans la carte. Tenir était une proposition française de l’assistant, jugée peu claire par Laurent ; aucun libellé français SAP canonique correspondant n’a été vérifié. Mettre VER002 en réexamen et expliciter l’effet recherché avant de choisir un autre verbe.

**statut**

Provenance et sens clarifiés, sans affirmer que SAP n’emploie jamais ce mot. Aucun remplacement global ni niveau hiérarchique adopté.

## C35

**id**

C35

**source**

U38 ; U39 ; F129/F130 ; A24 ; P72 ; 2026-09-10.

**formulation_a_eviter**

La première lecture de U37 conservait Aider et Optimiser parmi les natures possibles ; A24 proposait notamment informer ou éclairer pour préciser Aider. Elle associait Optimiser au réexamen des promesses selon une interprétation de la liste.

**formulation_retenue**

Après U38/U39, Aider et Optimiser expriment des intentions dans cette grille. Laurent propose Adapter pour l’évolution de volumes et contenus d’objets métier existants. L’assistant propose Restituer pour la visibilité contextualisée du stock ; Éclairer n’est plus proposé comme nature. Ces termes ne fixent pas une partition exclusive et leurs définitions restent à éprouver. L’adaptation concerne les objets métier du cas discuté, sans règle universelle interdisant de nouveaux objets, versions ou historiques.

**statut**

Évolution de l’hypothèse tracée dans U37–U39 ; A24, P72 et glossaire actualisés. Aucune CAP renommée ou reclassée. Adapter est une préférence utilisateur à éprouver ; Restituer reste une proposition assistant.

## C36

**id**

C36

**source**

U42 ; F133 ; 2026-09-10.

**formulation_a_eviter**

Finalité métier, intitulé initial proposé par l’assistant après U41.

**formulation_retenue**

Finalité, intitulé choisi par Laurent pour la colonne décrivant le pourquoi d’une capacité. Le contexte Business Capabilities rend le qualificatif métier superflu.

**statut**

Libellé appliqué au tableau et aux règles de rédaction ; ancien intitulé conservé ici et dans la provenance historique. Les contenus de colonne restent proposés.

## C37

**id**

C37

**source**

U45 ; F136 ; MKT17/ELM041 ; CMP027 ; 2026-09-10.

**formulation_a_eviter**

Définir le domaine uniquement comme un ensemble cohérent de capacités partageant un périmètre d’objets et de résultats, formulation initiale de P73 et de la comparaison des regroupements.

**formulation_retenue**

Partir de l’espace de problèmes et de connaissances métier, expliciter ses concepts, règles et limites, puis identifier et regrouper les aptitudes nécessaires. La catégorie de carte en est une représentation. La définition rédactionnelle proposée est : champ cohérent de problèmes, de connaissances et de règles métier auxquels l’entreprise doit répondre. Elle interprète l’orientation de Laurent ; elle n’est pas une citation littérale d’Evans.

**statut**

Précision de sens intégrée à P73, à la note, au glossaire et à AGENTS.md. Hiérarchie et périmètres concrets restent à éprouver ; aucune CAP déplacée ni équivalence avec un bounded context adoptée.

## C38

**id**

C38

**source**

U46 ; F137/F138 ; A26 ; 2026-09-10.

**formulation_a_eviter**

Faire de la distinction avec le bounded context un axe de travail de la catégorisation actuelle. Laisser entendre que la définition courte du mémento de 2015 permet de statuer sur le passage dont Laurent se souvient dans le livre. La définition précédente du domaine évoquait un champ de problèmes, de connaissances et de règles sans expliciter les liens entre les problèmes comme critère central.

**formulation_retenue**

Le domaine est envisagé comme un espace cohérent de problèmes métier liés entre eux, que l’on gagne à comprendre et à traiter ensemble. Rester sur les problèmes, leurs liens et les capacités ; laisser la conception des bounded contexts hors de l’étape actuelle. Le livre et le mémento sont deux sources distinctes : la recherche dans un extrait du premier ne permet ni d’attester le passage exact ni d’en conclure l’absence du livre complet.

**statut**

TER030, P73, note de comparaison et AGENTS.md précisés. Sources antérieures et définitions externes conservées comme provenance, sans en faire un découpage applicatif à produire maintenant.

## C39

**id**

C39

**source**

U48 ; F140–F144 ; 2026-09-10.

**formulation_a_eviter**

Avant U48, la vue des achats se limitait à « MAP produit la demande ; CBS suit la fabrication et l’amont » ; la réponse de Q034 était « — » et FL17 ne qualifiait son contenu que de demande d’achat fournisseur. Ces formulations ne rendaient pas compte des trois cas désormais décrits.

**formulation_retenue**

Trois cas d’achat sont déclarés : fabrication complète par le fournisseur, produits finis sur catalogue et fabrication à façon avec achats séparés de composants. Dans le premier cas, MAP émet des Planned Purchase Order. Ce libellé précise le récit, sans établir l’engagement ferme, le destinataire ni la correspondance à un document éditeur. L’orchestration est interrogée, pas adoptée comme capacité ni mécanisme cible.

**statut**

Complément de connaissance intégré aux vues achats, à CAP029 et FL17 ; Q034 partiellement renseignée, sans fermeture ni changement de définition de capacité.

## C40

**id**

C40

**source**

U49 ; F145/F146 ; A29 ; 2026-09-10.

**formulation_a_eviter**

A28/P75 et la note achats proposaient « les moyens génériques dans la vue de réalisation de la couche processus ». La réponse disait : « l’orchestration générique est un moyen transverse de la couche processus ». Cette formulation pouvait réserver l’orchestration à la couche haute et présenter le socle comme sans moteur de coordination.

**formulation_retenue**

Les deux couches sont envisagées avec des moyens de décision, détermination et orchestration. La couche processus est orientée Case Management. Chacune conserve son modèle métier, ses objets, sa persistance et son urbanisation ; la même solution ou des solutions distinctes restent possibles. Distinguer les objets et règles coordonnés, pas la présence d’un moteur. Un moteur peut exécuter des règles métier ; cela ne déplace pas l’autorité de ces règles hors de leur domaine.

**statut**

Orientation U49 intégrée à AGENTS.md, à la vue des deux couches, à la note achats, à P75 et CMP029. A28 reste une contribution historique rectifiée ; aucune CAP modifiée.

## C41

**id**

C41

**source**

U50 ; F147 ; A30 ; 2026-09-10.

**formulation_a_eviter**

Laisser le périmètre de la capability map ambigu après la formulation assistant selon laquelle le moteur réalise une aptitude « dans l’une ou l’autre couche ». Présenter encore uniquement comme proposée la séparation des modèles ou rouvrir une carte d’entreprise plus large dans l’analyse courante de l’orchestration.

**formulation_retenue**

Dans ce projet, la capability map cible la couche transactionnelle. Un autre modèle fonctionnel orienté processus décrira la couche processus. Les moteurs présents dans les deux couches ne modifient pas cette séparation. Les usages de vocabulaire plus larges dans le marché sont des différences de portée à documenter, sans extension de notre carte.

**statut**

Périmètre réaffirmé intégré aux règles et vues courantes ; définitions et statuts CAP conservés, candidats historiques à la frontière non supprimés ni reclassés automatiquement.

## C42

**id**

C42

**source**

U52 ; F149/F150 ; A32 ; 2026-09-10.

**formulation_a_eviter**

La présentation de A31/P76 comme trois options pouvait faire apparaître les domaines de problèmes comme une méthode encore interchangeable avec une classification de parcours ou de simples familles. Order Promising restait entièrement présenté comme candidat dans la liste, sans distinguer la reconnaissance de son rôle et l’ouverture de ses frontières.

**formulation_retenue**

Le domaine comme espace problématique guide déjà la carte ; U52 qualifie Order Promising de domaine local et confirme l’examen des frontières par les exemples. Source to Pay reste une lecture processus. Le choix d’une référence et d’un niveau de regroupement est distinct du choix des frontières de problèmes. La liste, les capacités et les frontières détaillées restent à éprouver.

**statut**

Méthode et statut local précisés ; aucune modification de niveau natif SAP ni validation de la liste complète.

## C43

**id**

C43

**source**

U53 ; F151–F153 ; A33/P77 ; 2026-09-10.

**formulation_a_eviter**

Dans la note 22, la ligne Achats / Réassort opposait « achats externes et réassort interne » puis proposait « Achats/engagements fournisseurs et Réassort opérationnel distincts ». Elle suggérait deux destinations concurrentes pour un flux entier en comparant formation du besoin et engagement commercial.

**formulation_retenue**

Le réassort exprime un besoin de renouvellement et sa satisfaction peut mobiliser un transfert interne ou des engagements d’achat/vente selon le cas. Séparer les questions de besoin, couverture/promesse, exécution, faits de stock et engagement commercial ; éprouver leurs frontières par des cas intra-société et entre sociétés. Les qualifier ne revient pas à fusionner tous les problèmes dans Order Promising.

**statut**

Note 22 et P76 précisés ; cas détaillé dans P77/note 23. Ni domaine fusionné ni fiche CAP modifiée ; hypothèses et vocabulaire antérieurs conservés dans la provenance.

## C44

**id**

C44

**source**

U58 ; F158 ; A34 ; 2026-09-10.

**formulation_a_eviter**

Déduire des formulations « la Supply est la couche transactionnelle de contrôle, d’orchestration et d’optimisation de la logistique » et « possède une intelligence propre de rééquilibrage, prévision et gestion des impondérables » que toutes ces aptitudes doivent être développées dans la plateforme FLOW. La seule mention antérieure de l’autonomie du SI C-Log ne rendait pas explicite le périmètre de développement du programme.

**formulation_retenue**

La logistique est hors du développement de la plateforme FLOW et reste en adhérence. Distinguer cartographie des problèmes métier et périmètre de réalisation ; représenter les responsabilités et interactions utiles avec la logistique sans en faire des développements de la plateforme. Qualifier les frontières détaillées sans exclure automatiquement toute Supply ni transférer les décisions actuelles de C-Log.

**statut**

Précision de périmètre intégrée aux règles, à la note 23 et aux vues courantes ; orientations U56/U57 conservées. Aucun candidat CAP reclassé ni contrat d’interface arrêté.

## C45

**id**

C45

**source**

U60 ; F160/F161 ; A36 ; ELM052–ELM055 ; 2026-09-10.

**formulation_a_eviter**

P78 et la conclusion U59 proposaient encore IBM comme contrelecture retail active et BIAN comme appui de regroupement sans intégrer les réserves nouvelles de Laurent. La formule « catalogue retail complet non consulté » ne distinguait pas assez clairement absence de consultation et absence de preuve d’un modèle retail livré. Les échecs d’ouverture BIZBOK 15.0 pouvaient être relus comme une impossibilité d’accès durable.

**formulation_retenue**

Après U60, IBM est conservé comme historique non prioritaire ; BIAN reste périphérique à la définition de capacité, tandis que TM Forum demeure une piste et BIZBOK est approfondi. Une équipe Retail/Wholesale Guild est identifiée, mais modèle livré, version et contenu ne sont pas établis. Introduction et glossaire BIZBOK 15.0 ©2026, ainsi que le Metamodel Guide v3.0 de 2024, sont maintenant consultés sur le CDN officiel ; cela ne vaut pas accès au guide complet ni aux modèles membres.

**statut**

Priorités et accès précisés dans les vues courantes et le catalogue ; provenance des analyses antérieures conservée. Aucun candidat CAP ni définition locale remplacés.

Précision de provenance C45 : MKT03 indiquait précédemment « L’ouverture du glossaire a échoué ; aucun contenu du guide détaillé n’est revendiqué comme lu » et proposait d’examiner les règles « lorsqu’elles seront consultables ». Ces formulations sont remplacées par le constat d’accès aux extraits publics, sans revendiquer le guide intégral.

## C46

**id**

C46

**source**

U55/U56/U61 ; F155/F156/F162 ; 2026-09-10.

**formulation_a_eviter**

Le glossaire indiquait « Toutes les lignes sauf TER001 ont le statut proposé », malgré les définitions explicites OMS/Supply et les nouvelles distinctions de Laurent. Son sens large d’Objet métier pouvait également être confondu avec l’analogie aggregate root formulée pour la plateforme.

**formulation_retenue**

Qualifier séparément les définitions impératives, déclarations utilisateur et propositions. TER002 conserve son sens métier large ; U61 décrit une distinction de plateforme à préciser, sans faire de tout objet métier une racine d’agrégat. Les termes fait/document conservent la provenance utilisateur et leurs règles détaillées restent ouvertes.

**statut**

Statuts et portée du glossaire précisés ; aucune définition historique supprimée, aucun agrégat ou métamodèle complet adopté.

## C47

**id**

C47

**source**

U62 ; F164 ; A38 ; 2026-09-10.

**formulation_a_eviter**

Le tableau « Modèle propre » de la note 15 donnait « Ressources, demandes, engagements, faits de gestion et règles qui les gouvernent » pour le socle et « Dossiers, objectifs, tâches, responsabilités et faits de traitement » pour les processus. Cette asymétrie pouvait réserver le mot demande au socle. L’exemple de promesse de la note 24 employait Demande sans distinguer la représentation du besoin de l’objet de suivi du processus.

**formulation_retenue**

Expliciter les objets métier dans les deux modèles et l’exemple Demande de réassort donné par Laurent pour les processus. Qualifier le besoin présenté à la promesse dans l’illustration, avec ses relations à l’objet processus à préciser. La famille de demandes du glossaire conserve cette distinction ; aucun objet Demande universel n’est déduit.

**statut**

Vues précisées sans fusion des modèles, nouvelle capacité ni frontière d’agrégat décidée ; Q052 reste ouverte.

## C48

**id**

C48

**source**

U66 ; F168/F169 ; 2026-09-11.

**formulation_a_eviter**

Conserver la nomenclature française de la carte courante alors que Laurent demande l’anglais, ou inventer un nouveau nom pour un périmètre déjà correctement nommé Inventory Management par les références pertinentes.

**formulation_retenue**

Employer des libellés anglais dans la carte courante et réutiliser les noms de marché lorsqu’ils conviennent au sens. Inventory Management est retenu pour D01 ; les traductions locales et leurs frontières restent proposées. Définitions et explications restent en français. Les anciennes formulations sont conservées dans la table de provenance ci-dessous.

**statut**

Consigne de nomenclature appliquée ; identifiants stables et définitions conservés. Aucun alignement de périmètre déduit du seul nom.

| Repère | Libellé précédent | Libellé courant après U66 |
| --- | --- | --- |
| D01 | Stocks | Inventory Management |
| D02 | Disponibilité et engagements de ressources | Resource Availability and Commitments |
| D03 | Promesse de fourniture | Order Promising |
| D04 | Engagements commerciaux | Commercial Commitments |
| D05 | Équilibrage opérationnel des ressources | Operational Resource Balancing |
| D06 | Possibilités d’exécution | Execution Options |
| D07 | Engagements et faits d’exécution | Execution Commitments and Facts |
| D08 | Produits opérationnels | Product Information Management |
| D09 | Parties et relations | Party Management |
| D10 | Conditions commerciales | Commercial Terms |
| D01.a | Établir les positions de stock | Establish inventory positions |
| D01.b | Enregistrer les faits de stock | Record inventory facts |
| D01.c | Restituer une vision consolidée des stocks | Provide a consolidated inventory view |
| D01.d | Rapprocher et régulariser les écarts de stock | Reconcile and correct inventory discrepancies |
| D02.a | Déterminer la disponibilité pour un usage | Determine resource availability for a given use |
| D02.b | Protéger des ressources pour des bénéficiaires | Supply Protection |
| D02.c | Réserver des ressources pour un besoin déterminé | Reserve resources for a specific requirement |
| D02.d | Adapter les engagements de ressources | Adjust resource commitments |
| D03.a | Évaluer les possibilités de fourniture | Assess supply feasibility |
| D03.b | Confirmer une promesse de fourniture | Confirm a supply promise |
| D03.c | Réexaminer les promesses de fourniture | Reassess supply promises |
| D04.a | Établir un engagement commercial | Establish a commercial commitment |
| D04.b | Adapter les obligations commerciales | Amend commercial obligations |
| D04.c | Déterminer la réalisation et le reste à satisfaire d’un engagement | Determine commitment fulfillment and remaining obligations |
| D04.d | Autoriser une reprise ou un remplacement | Authorize a return or replacement |
| D05.a | Déterminer les objectifs opérationnels de couverture | Determine operational coverage targets |
| D05.b | Déterminer les besoins nets de ressources | Determine net resource requirements |
| D05.c | Déterminer une redistribution de ressources | Determine resource redistribution |
| D06.a | Qualifier les lieux et prestations réalisables | Qualify locations and feasible services |
| D06.b | Déterminer la capacité de réalisation disponible | Determine available execution capacity |
| D06.c | Déterminer les options d’exécution admissibles | Determine eligible execution options |
| D07.a | Formaliser un besoin de prestation | Formalize a service requirement |
| D07.b | Établir et adapter les engagements d’exécution | Establish and adjust execution commitments |
| D07.c | Qualifier les réalisations et leurs écarts | Qualify execution results and discrepancies |
| D07.d | Établir les ressources attendues | Identify and qualify expected resources |
| D08.a | Identifier les articles et composants | Identify items and components |
| D08.b | Qualifier les caractéristiques opérationnelles des produits | Qualify operational product characteristics |
| D08.c | Déterminer les unités et conditionnements applicables | Determine applicable units of measure and packaging configurations |
| D09.a | Identifier les parties aux opérations | Identify parties to business operations |
| D09.b | Qualifier les rôles et relations des parties | Qualify party roles and relationships |
| D09.c | Déterminer l’admissibilité d’une relation commerciale | Determine commercial relationship eligibility |
| D10.a | Définir les conditions commerciales applicables | Define applicable commercial terms |
| D10.b | Déterminer les prix et conditions d’une opération | Determine transaction prices and terms |
| D10.c | Déterminer les droits après fourniture | Determine post-supply entitlements |

D02.e Supply Assignment est un complément de P81 après U67 ; elle n’a pas d’ancien libellé à remplacer. Les 34 définitions précédentes conservent leur contenu.

## C49

**id**

C49

**source**

U67 ; F171 ; A41 ; 2026-09-11.

**formulation_a_eviter**

La réponse à U66 soulignait « Supply Protection et Supply Assignment sont documentés comme des fonctionnalités de produit », ce qui pouvait être compris comme une négation de leur nature de capacité métier.

**formulation_retenue**

Dans la carte locale, Supply Protection et Supply Assignment désignent des aptitudes de l’entreprise indépendantes des outils. Allocation Run désigne un mécanisme de réalisation. SAP peut employer les mêmes libellés pour les fonctionnalités de produit qui réalisent ces aptitudes ; cette documentation n’est pas contradictoire avec leur lecture métier. Le rang exact dans le catalogue RBA est une question distincte, non établi pour ces deux noms dans le corpus consulté.

**statut**

Erreur de plan d’analyse corrigée : distinguer sens métier, mécanisme de réalisation et classement documentaire. Ni absence de capacité métier ni niveau RBA déduits du seul type de source.

## C50

**id**

C50

**source**

U69 ; F173 ; A43 ; 2026-09-11.

**formulation_a_eviter**

La présentation D01.a « déterminer les quantités et états connus par article, lieu, détenteur et propriétaire » pouvait être comprise comme configurer une structure. D01.d « confronter positions et constats, puis établir les corrections justifiées » pouvait être comprise comme produire une golden data multisource. La séparation de D01.a et D01.b pouvait aussi laisser croire que le résultat position et son évolution justifiaient nécessairement deux capacités.

**formulation_retenue**

D01.a vise la connaissance effective des quantités et états à une date ; la définition des dimensions et règles de représentation est un sujet lié, qui ne se confond pas avec ce résultat. D01.b qualifie les faits et leurs effets, y compris des changements d’état sans déplacement physique ; son chevauchement avec D01.a est à réexaminer. D01.c vise une visibilité métier cohérente, au-delà du simple accès technique. D01.d confronte positions et constats pour établir un écart expliqué et une correction justifiée, y compris avec un seul système : ce n’est pas une définition de datahub ou de production de golden data. Un désaccord entre systèmes doit être instruit selon date, périmètre, faits et autorités, sans correction automatique du stock ni choix arbitraire d’une source.

**statut**

Clarification de formulations assistant ; les questions de Laurent ne sont pas transformées en décisions. Libellés et définitions antérieurs conservés avec explication ; maille D01.a/D01.b/D01.c à éprouver, aucune fusion ni capacité de configuration ajoutée. Le sens de logique/virtuel reste à qualifier en Q066.

**Complément C50 après U71 — 2026-09-11 :** Laurent confirme le manque de clarté de D01.a. Explication A45 : établir combien de stock est connu, où et dans quel état à une date. Exemple fictif 100 unités dont 20 bloquées ; aucune configuration de structure ou de protection impliquée. Le chevauchement a/b demande un réexamen avant maintien de deux capacités distinctes ; aucun renommage ni fusion validés.

**Complément C50 après U72 — 2026-09-11 :** Laurent reformule D01.d par l’inventaire. A46 confirme le noyau métier : constater les quantités présentes, comparer aux positions enregistrées et régulariser les écarts justifiés. Enregistrer les quantités constatées précise ici comptabiliser ; ni vérité automatique de chaque comptage ni valorisation financière implicite. Physical Inventory est un nom proposé avec appui ELM014/ELM068, sans remplacement automatique de l’intitulé courant.

## C51

**id**

C51

**source**

U74 ; F178 ; A48 ; 2026-09-11.

**formulation_a_eviter**

Dans P81 version 0.2, Supply Protection (D02.b) était rattachée à D02 Resource Availability and Commitments et D01 limité à la connaissance, aux faits, à la visibilité et aux écarts de stock. Après U70–U73, son rattachement était encore présenté comme entièrement ouvert.

**formulation_retenue**

P81 version 0.3 rattache Supply Protection à D01 Inventory Management selon l’orientation U74 de Laurent. D01 couvre la connaissance des stocks et la maîtrise de leur protection. Le repère historique D02.b est conservé pour la même aptitude, sans nouvelle capacité ni réutilisation d’identifiant ; sa localisation courante est D01. Le nom, la définition et la Finalité de cette capacité restent ceux de la proposition précédente. La finalité du domaine est élargie ; les autres capacités de D02 conservent leur rattachement de travail.

**statut**

Rattachement local mis à jour selon l’orientation explicite de Laurent, sans équivalence de catalogue ni validation des frontières détaillées. La séparation a/b et la portée des protections sur les ressources futures restent à éprouver. L’ancien préfixe du repère ne désigne plus le domaine courant de Supply Protection.

## C52

**id**

C52

**source**

U75 ; F179 ; A49 ; 2026-09-11.

**formulation_a_eviter**

P81 version 0.3 maintenait réservation (D02.c) et Supply Assignment (D02.e) dans D02. La définition de réservation était « établir une affectation dont les décisions concurrentes doivent tenir compte », ce qui brouillait la distinction explicitée par Laurent. La disponibilité pouvait être lue comme un stock supplémentaire ou comme une capacité indépendante déjà établie.

**formulation_retenue**

P81 version 0.4 rattache la réservation à D01 et Supply Assignment à D03 selon U75, avec leurs repères historiques conservés. La définition proposée de réservation devient « établir un engagement de quantité pour un besoin identifié, dont les usages concurrents doivent tenir compte ». L’affectation couvre des demandes en leur reliant des ressources admissibles, présentes ou futures ; son nom et sa définition restent inchangés. La disponibilité répond à une question d’usage et de date, à partir des ressources et restrictions ; sa maille et son rattachement restent à éprouver. La proposition de regrouper les représentations physiques/logiques/virtuelles dans un même domaine ne fusionne pas leurs notions et ne constitue pas une décision utilisateur.

**statut**

Rattachements U75 appliqués ; définition de réservation clarifiée comme proposition en cohérence avec TER016 et U75. Autres questions et frontières ouvertes. D02 conserve provisoirement deux aptitudes à réexaminer, sans nécessité de domaine autonome présumée ; aucun identifiant supprimé ou réutilisé.

## C53

**id**

C53

**source**

U76/U77 ; F180/F181 ; A50/A51 ; 2026-09-11.

**formulation_a_eviter**

L’assistant employait logique/virtuel comme un ensemble indifférencié de vues, pools, ressources externes et projections. TER021 portait le libellé « Pool / stock logique » et la définition « Terme de travail pour un regroupement ou une représentation de ressources selon des critères explicites », avec une limite demandant de préciser vue, quantité calculée ou enveloppe. La formulation pouvait faire de stock logique un synonyme de regroupement multisource, de virtuel ou de pool.

**formulation_retenue**

Selon U76 : physique = existence réelle des biens ; logique = états métier des mêmes biens ; virtuel = quantité considérée disponible selon un calcul. TER040–TER042 enregistrent ces trois sens. TER021 conserve la notion de pool et son identité, en retirant le synonyme stock logique et en conservant son ancienne formulation dans cette correction. Une vue consolidée peut exposer les trois informations, sans en changer le sens. U77 ouvre leur partage entre domaines ; le rattachement de toute quantité calculée à Order Promising n’est pas décidé.

**statut**

Vocabulaire local corrigé selon la distinction explicite de Laurent. Les précisions sur partition des états et absence de double déduction dans les exemples sont des conditions de cohérence proposées par Codex, pas des règles utilisateur déjà établies. Pas de formule universelle ni equivalence native adoptées.

## C54

**id**

C54

**source**

U78 ; F182 ; A52 ; ELM070–ELM072/CMP042 ; 2026-09-11.

**formulation_a_eviter**

Lire notre distinction locale réservation/affectation comme une séparation étanche et universelle SAP/Microsoft, ou comme réservation limitée au stock présent et affectation portant seule le futur. Déduire qu’une réservation SAP MM empêche toujours tout autre retrait, ou qu’une réservation Microsoft sur stock présent choisit forcément une pièce individuelle.

**formulation_retenue**

Microsoft réserve aussi des entrées commandées non reçues et peut préciser progressivement les dimensions. SAP décrit d’une part des Reservations pour mouvements planifiés avec contrôle de disponibilité configurable, et d’autre part des quantités réservées par Supply Assignment dans aATP. Affectation et réservation peuvent donc être deux faces d’un même engagement, avec plusieurs réalisations. Le rattachement local U75 est remis en discussion par U78 ; il reste affiché comme option, sans déplacement ou fusion automatique.

**statut**

Précaution de lecture renforcée par nouvelles preuves documentaires ; aucune équivalence de capacité, aucun cycle local ni rôle d’autorité définis par la documentation seule.

## C55

**id**

C55

**source**

U81 ; F185 ; A55 ; 2026-09-11.

**formulation_a_eviter**

La présentation mettait les états de stock dans des descriptions génériques sans nommer clairement le stock logique dans D01. Le libellé Physical Inventory de la seule capacité d’inventaire pouvait être pris pour le périmètre du domaine entier. Anciennes lignes de capacités :

| D01.a | **Establish inventory positions** : déterminer les quantités et états connus par article, lieu, détenteur et propriétaire lorsque ces dimensions sont pertinentes. | Disposer d’une connaissance exploitable des ressources. |
| D01.b | **Record inventory facts** : qualifier les entrées, sorties, changements d’état et consommations qui expliquent les positions. | Expliquer les variations et leur provenance. |
| D01.c | **Provide a consolidated inventory view** : présenter les positions sans double comptage, avec source, périmètre et fraîcheur. | Permettre une lecture commune des stocks distribués. |
| D03.a | **Assess supply feasibility** : déterminer les quantités et dates confirmables pour un besoin, en combinant ressources et possibilités d’exécution admissibles. | Éclairer l’engagement réalisable envers le destinataire. |

Anciennes précisions de frontière :

- **Stock virtuel et frontière U77 — proposition :** Inventory Management porte les positions physiques, leurs états, protections et réservations ; Order Promising porte la projection destinée à établir quantité et date promettables. Exemple U76 : 60 libres + 30 attendues demain − 15 promises = 75, sous condition que les promises ne soient pas déjà déduites et que le futur soit admissible à l’horizon choisi. Toutefois, un calcul de disponible à réserver maintenant peut rester dans Inventory Management : calculé ne signifie pas automatiquement domaine Order Promising. Le sens virtuel U76 reste large ; le partage détaillé est proposé, pas arbitré. Q066 reçoit une réponse partielle sur les définitions et reste ouverte sur règles, objets et autorités. Le besoin d’une capacité séparée de disponibilité demeure à éprouver.

**Projection de promesse — hypothèse U77/A51 :** le stock virtuel qui sert à établir une quantité/date promettable peut appartenir au modèle d’Order Promising, alimenté par les positions et états d’Inventory Management, les ressources attendues et les engagements. Ces informations conservent leurs autorités métier ; leur combinaison dans une projection ne transfère pas leur propriété au domaine. Un simple disponible courant pour réservation peut rester dans Inventory Management. La convention de stock virtuel de U76 est plus large que cette seule projection ; aucune attribution de tous les calculs à D03 n’est décidée.

**formulation_retenue**

Inventory Management gère explicitement les stocks physiques et leurs états logiques, avec la connaissance des ressources futures U79/U80. Order Promising calcule le stock virtuel utile à la promesse à partir des ressources, états, restrictions et engagements, puis détermine quantité et date réalisables. Physical Inventory désigne le constat/comptage et rapprochement du physique ; il ne limite pas tout D01 au physique. La capacité de faisabilité décrit cette aptitude métier, sans créer une capacité pour chaque opération de calcul.

**statut**

Clarification du modèle local et correction de présentation ; libellés, repères et compte des capacités conservés. Les définitions détaillées restent proposées, avec frontière U81 explicitée. Les calculs élémentaires de positions et états dans D01 ne sont pas interdits ; le calcul de stock virtuel destiné à la promesse est rattaché à D03. Aucun standard externe ni configuration locale déduit.

## C56

**id**

C56

**source**

U82 ; F186 ; A56 ; ELM075/ELM076/CMP044 ; 2026-09-11.

**formulation_a_eviter**

Employer Physical Inventory comme nom local déjà choisi de D01.d ou maintenir Establish inventory positions comme un libellé satisfaisant après la critique de Laurent. Présenter les noms proposés comme une paire native de capacités SAP/Microsoft, ou confondre Inventory accuracy et le moyen de comptage.

**formulation_retenue**

Physical Inventory reste le terme natif SAP, mais sa proposition comme nom local est en réexamen. Establish inventory positions est le nom historique proposé de D01.a, désormais contesté. Les options locales examinées sont Manage inventory quantities et Count and reconcile inventory ; Stocktaking explicite le comptage. Inventory accuracy est proposée pour la Finalité, Truth est déconseillé car trop absolu et non délimité.

**statut**

Réexamen de nomenclature consigné ; tables conservées comme trace de travail avec avertissement et options, sans renommage définitif. Aucun élargissement de D01.d à toute la qualité des informations ni confusion entre réalisation logistique et développement FLOW.

## C57

**id**

C57

**source**

U84 ; F188 ; A58 ; 2026-09-11.

**formulation_a_eviter**

Le titre proposé P82 Inventory Reservation et le titre historique P81 Reserve resources for a specific requirement sont inutilement longs dans D01 après le choix explicite de Laurent. Stocktaking était le titre proposé de la capacité de comptage et rapprochement ; ne pas le présenter comme le seul nom possible ni comme écrit obligatoirement avec tiret.

**formulation_retenue**

Reservation devient le libellé local de l’aptitude repérée historiquement D02.c dans D01. Counting devient la proposition de titre de comptage dans la vue P82 ; la définition de constat, comparaison, qualification des écarts et correction est inchangée. Stocktaking et stock-taking sont des graphies rencontrées ; la préférence pour Counting ne prouve pas une décision de maille.

**statut**

Choix Reservation appliqué ; Counting proposé, sans adoption définitive ni réutilisation de repère. Noms antérieurs conservés ici et dans les historiques ; aucune définition de capacité modifiée.

## C58

**id**

C58

**source**

U86 ; F190 ; A60 ; 2026-09-11.

**formulation_a_eviter**

Présenter Stocktaking / Counting comme un nom encore à arbitrer après U86. Le titre historique D01.d était Reconcile and correct inventory discrepancies, avec Physical Inventory, puis Counting comme options proposées.

**formulation_retenue**

Stocktaking est le nom local retenu par Laurent le 2026-09-11, repère D01.d conservé. La définition conserve constat par comptage, comparaison, qualification des écarts et corrections justifiées ; Inventory accuracy exprime la Finalité. Counting et Physical Inventory restent des termes externes ou historiques.

**statut**

Renommage local adopté et appliqué ; aucune nouvelle capacité ni changement des autorités. La décision ne valide pas à elle seule toute la proposition P82.

## C59

**id**

C59

**source**

U90/F194/A63 ; 2026-09-11 ; ELM082/CMP048.

**formulation_a_eviter**

Présenter Supply Feasibility et Confirmation comme les seuls noms courants de discussion après U90 ; développer ATP en Availability To Promise ; assimiler Promise Confirmation à Product Allocation Check ; conclure que toutes les capacités manipulent nécessairement un même objet Promise.

**formulation_retenue**

Promise Verification et Promise Confirmation sont les nouveaux candidats de Laurent ; les anciens noms Supply Feasibility et Confirmation restent la base historique de la comparaison U89. La vérification proposée évalue une possibilité quantité/date avant engagement ; Promise Revision réexamine l’engagement existant. ATP signifie Available-to-Promise dans les sources consultées. Contrôle d’allocation et confirmation restent distincts.

**statut**

Clarification et évolution de la vue proposée, sans renommage des lignes historiques P81 ni clôture des questions de couverture.

## C60

**id**

C60

**source**

U91/U92 ; F195/F196/A64 ; 2026-09-11.

**formulation_a_eviter**

Conserver Promise Verification comme candidat courant après U92 ; limiter la première capacité à contrôler une proposition fournie ailleurs ; confondre une capacité à décider avec une décision particulière ou son moteur.

**formulation_retenue**

Promise Verification est rejeté par Laurent. La première capacité doit faire naître une promesse ; Promise Formulation est proposé par Codex. L’interprétation courante produit une proposition quantité/date avant son engagement par Promise Confirmation, statut à confirmer. Employer décision pour les nouvelles aptitudes de choix et identifier leur domaine propriétaire proposé ; conserver les libellés natifs externes en provenance.

**statut**

Correction appliquée à la vue proposée ; noms historiques conservés dans U90/A63/C59 et les études datées. Aucun objet Promise unique ni périmètre détaillé validé.

## C61

**id**

C61

**source**

U93/F197/F198/A65 ; ELM083/CMP050 ; 2026-09-11.

**formulation_a_eviter**

Présenter Fulfillment Source Decision comme couvrant toutes les décisions de fulfillment ; réduire le transport à un délai ajouté à la disponibilité ; conserver Promise Formulation comme candidat courant après son rejet.

**formulation_retenue**

Le choix de la source et le choix de l’acheminement sont deux problèmes liés. Fulfillment Route Decision est ajouté comme aptitude candidate ; son propriétaire D03 pour la promesse et ses relations avec les options D06 et la planification de transport restent proposés. Promise Proposal est le nouveau candidat de Laurent pour la première capacité ; la définition active précise produire une proposition de fourniture.

**statut**

Correction de couverture et de vocabulaire appliquée à la vue de discussion, sans nouveau développement logistique ni validation des frontières. Promise Formulation conservé en historique U92/A64/C60.

## C62

**id**

C62

**source**

U94/A66/ELM084 ; contrôle du 2026-09-11.

**formulation_a_eviter**

Présenter ATP comme limité au stock physique et CTP comme tout stock futur ; généraliser la restriction de la page Order promising excluant CTP avec Planning Optimization à toutes les versions/configurations actuelles.

**formulation_retenue**

ATP inclut des réceptions futures planifiées ; CTP considère aussi les moyens de créer la fourniture, notamment les composants et capacités. La page détaillée Calculate sales order delivery dates using CTP expose Near real-time CTP avec Planning Optimization sous conditions et le renommage de CTP for Planning Optimization en Batch CTP à partir de 10.0.41. La liste de cinq méthodes en U89 reste un relevé de sa page source, pas un inventaire actuel homogène de toutes les configurations.

**statut**

Précaution documentaire ajoutée ; distinction métier stable et variantes de réalisation séparées. Aucune configuration locale ou adoption technique déduites.

## C63

**id**

C63

**source**

U95/F200/F201/A67 ; 2026-09-11.

**formulation_a_eviter**

Présenter les neuf capacités d’Order Promising comme encore non validées ; maintenir CTP comme contribution locale déjà retenue de Promise Proposal après son report ; interpréter l’accord comme une validation de toutes les frontières ou des correspondances marché.

Anciennes quatre lignes de P81 version 0.4, avant intégration de P83 :

| D03.a | **Assess supply feasibility** : déterminer le stock virtuel mobilisable par horizon pour un besoin, à partir des ressources présentes et futures admissibles, de leurs états et des engagements, puis les quantités et dates confirmables compte tenu des possibilités d’exécution. | Éclairer l’engagement réalisable envers le destinataire. |
| D03.b | **Confirm a supply promise** : établir les quantités et dates engagées et distinguer la part restant à couvrir. | Donner un engagement explicite sans masquer le besoin non couvert. |
| D03.c | **Reassess supply promises** : adapter confirmations et priorités à l’évolution des ressources et règles, avec leurs effets sur les demandes concernées. | Rendre les engagements compatibles avec la situation et les priorités retenues. |
| D02.e | **Supply Assignment** : établir la couverture de demandes par des ressources admissibles présentes ou futures, selon les règles applicables. | Relier les demandes à satisfaire aux ressources qui peuvent les couvrir. |

**formulation_retenue**

Laurent valide quatre capacités d’action et cinq capacités de décision d’Order Promising. P81 version 0.5 porte la liste courante à neuf capacités D03 et 40 au total. Nouveaux repères D03.d Allocation Eligibility Decision, D03.e Fulfillment Source Decision, D03.f Fulfillment Route Decision, D03.g Product Substitution Decision et D03.h Supply Creation Decision ; D03.a/b/c et le repère historique D02.e sont conservés. ATP appartient à la promesse ; CTP reste au glossaire et son placement est différé. Analytics/planification/protection demeure une hypothèse.

**statut**

Validation locale appliquée avec auteur Laurent et date 2026-09-11. Pas de suppression D02, de transfert C-Log, de reclassement CAP36 ou de capacité CTP ajoutée. Supply Creation Decision conservée ; archives et anciennes comparaisons non réécrites.

## C64

**id**

C64

**source**

U97/U98 ; F203–F208 ; 2026-09-11.

**formulation_a_eviter**

Faire administrer, qualifier, vérifier, dédoublonner, enrichir ou recruter les référentiels Party / Role, Agreement et Catalog dans la plateforme. Confondre l’Agreement de référence avec une commande transactionnelle ou faire créer/réviser les contrats externes dans D04. Présenter D08.a–c, D09.a–c ou D10.a–c comme capacités actives de la plateforme.

**formulation_retenue**

Trois domaines contigus : D09 Party / Role, D11 Agreement et D12 Catalog, avec une ingestion chacun. Les applications externes font autorité ; les modèles sont reliés par identifiants. Les conditions particulières de l’Agreement alimentent Order Promising, qui conserve ses décisions opérationnelles. D04 reste à examiner pour les commandes distinctes des Agreements. Les anciens repères ne sont pas réutilisés ; contenu remplacé dans l’audit.

**statut**

Correction appliquée selon instruction de Laurent, 2026-09-11. [État remplacé et contrôle](../audits/2026-09-11-reference-data-boundaries.md). P81 version 0.6 : dix domaines actifs et 34 capacités. Maîtrise externe déclarée, configuration et autorités par attribut non démontrées.

## C65

**id**

C65

**source**

Audit U99 ; ELM087–ELM098 ; A70 ; 2026-09-11

**formulation_a_eviter**

Déduire de la correction U97 que trois référentiels suffisent selon le marché, que toute information article est couverte par Catalog, ou que seuls les Orders portent des engagements. Interpréter le constat historique « pas de famille clairement orpheline » comme une couverture exhaustive après retrait D08/D10. Présenter Purchase Management ODA comme une spécification détaillée publiée.

**formulation_retenue**

Le trio courant reste une orientation locale ; produit, prix, relations fournisseur/article et lieux appellent des frontières explicites. Agreement et Order sont distincts mais peuvent tous deux porter des engagements. La couverture en réception produit et les autorités du prix appliqué/consommé contractuel restent à établir. TMFC033 est Planned dans la notice consultée ; l’audit propose des évolutions sans les appliquer.

**statut**

Précaution documentaire appliquée ; aucun arbitrage de Laurent remplacé. [Preuves et propositions](../audits/2026-09-11-modele-marche-achats-ventes-referentiels.md). Les capacités actives et leurs statuts sont conservés.

## C66

**id**

C66

**source**

U100/F210–F212 ; A71 ; 2026-09-11

**formulation_a_eviter**

Maintenir comme prochaine étape imposée le choix de domaines Purchase Order/Sales Order à partir de P86 ; laisser toute référence article implicite dans Catalog après U100. Ancien état : P81 0.6, dix domaines et 34 capacités, D08 retiré.

**formulation_retenue**

Étudier les différences achat/vente/retour comme contextes de la Supply transactionnelle générique fondée sur des documents d’autorisation, avec les parcours commerciaux dans le modèle processus. Autonomie article confirmée : D08 réactivé pour ce même sujet sous le nom proposé Product Reference ; nouvelle ingestion D08.d, anciennes D08.a–c toujours retirées. P81 0.7 contient onze domaines et 35 capacités. D04/D07 restent à revoir ; aucune fusion ni capacité générique nouvelle validée.

**statut**

Correction d’orientation appliquée. P86 conservée comme proposition antérieure, mise à jour de statut ; correspondances CMP058. L’audit U99 conserve ses constats datés. Aucun changement des neuf capacités validées D03.

## C67

**id**

C67

**source**

U101 ; analyse A72, ELM099–ELM102 ; 2026-09-11

**formulation_a_eviter**

Déduire de l’autonomie du référentiel article U100 que Laurent a validé quatre domaines de capacités au même rang qu’Inventory Management ; assimiler domaines de données MDG, blocs ODA et capacités Guild.

**formulation_retenue**

Les quatre modèles de référence sont distincts ; leur niveau de regroupement reste proposé. P81 0.7 les affiche comme domaines de travail, pas comme niveaux validés. P87 recommande un groupe de présentation conservant leurs ingestions, sans fusion appliquée.

**statut**

Précision de statut ajoutée à la carte ; aucun contenu ni repère modifié. La comparaison concerne des objets de nature explicitement différente.

## C68

**id**

C68

**source**

U102/F214 ; A73 ; 2026-09-11

**formulation_a_eviter**

Laisser le référentiel des lieux implicite dans D06 ou le confondre avec Party ; lire TER053 comme si aucun référentiel de réseau n’avait été demandé. Déduire de Fulfillment Network une maîtrise FLOW de la logistique ou une validation du regroupement P87.

**formulation_retenue**

Party/lieu distincts selon Laurent U102. D13 Fulfillment Network explicite le référentiel de réseau, avec ingestion seule proposée dans la continuité U97. D06 conserve l’appréciation des possibilités d’exécution, à préciser par rapport aux références reçues ; D03 décide source/acheminement selon ses autorités et D07 suit engagements/faits. La topologie, les attributs et les sources du réseau restent à définir.

**statut**

Correction de carte et de portée CAP002 ; formulations historiques conservées. P81 0.7 à onze domaines/35 aptitudes devient 0.8 à douze repères de domaines/36 aptitudes. Le rang des références reste en discussion, Q075 ; aucune capacité D03 modifiée.

## C69

**id**

C69

**source**

U103/F215 ; A74 ; 2026-09-11

**formulation_a_eviter**

Présenter encore Business References comme une option de présentation non retenue après le Go U103, ou affirmer que les douze repères actifs doivent tous figurer au même niveau de la vue synthétique.

**formulation_retenue**

Le Go est appliqué au groupe de présentation Business References contenant cinq références distinctes. P81 0.9 distingue sept domaines transactionnels de travail et ce groupe dans la vue synthétique. Douze repères détaillés et 36 aptitudes conservés ; aucun domaine unique ni niveau hiérarchique universel adopté.

**statut**

Ancien état 0.8 conservé dans les historiques U102. P87 retenue sur la présentation, Q075 résolue dans cette portée ; maîtres et contenu détaillé du réseau toujours ouverts Q076.


## C70

**id**

C70

**source**

U106–U112 ; F216–F219 ; A75 ; 2026-09-13

**formulation_a_eviter**

Les registres Markdown sont encore le modèle courant lu par FLOW Atlas ; la release ne contient que des capacités validées ; les 36 CAP historiques sont la même nomenclature que les 36 capacités P81 ; un récit ou un besoin est une preuve de déploiement actuel.

**formulation_retenue**

Les JSON de backlog, release et panorama-as-is font autorité pour les modèles. Les Markdown conservent les sources, analyses, corrections et restitutions. La release publie les 36 capacités avec leurs statuts et preuves de validation distincts. Les CAP historiques restent séparées. Le panorama conserve les qualifications de preuve ; Sarenza reste non traité. U112 prépare l’extension de structure et l’épreuve sur les quatre contextes, sans adopter le nom Univers ni des objets ou liens détaillés.

**statut**

Remplace l’autorité décrite en U105 et l’interprétation initiale de release limitée aux éléments adoptés. La release 2026-09-13.1 restreinte reste historique, current.json pointe vers 2026-09-13.2 complète. Les validations de fond antérieures et leurs réserves demeurent.


## C71

**id**

C71

**source**

U115/U116 ; diagnostic local du 2026-09-13, JSON backlog/release et API Atlas.

**formulation_a_eviter**

Présenter les cinq capacités P82 comme la carte JSON courante avant U116, ou affirmer que la proposition non validée devait rester invisible dans le backlog. Anciens noms courants : Establish inventory positions, Record inventory facts et Provide a consolidated inventory view. Ne pas confondre état de travail et validation métier.

**formulation_retenue**

Le choix U116 fait de P82 le découpage courant de D01 dans le backlog : Inventory Tracking (nouveau D01.e, regroupant D01.a/D01.b), Inventory Visibility (D01.c révision 2), Stocktaking (D01.d), Supply Protection (D02.b) et Reservation (D02.c). Les trois dernières capacités restent inchangées, avec leurs validations partielles et réserves. La release 2026-09-13.2 garde les six capacités publiées ; sa mise à jour nécessite une publication explicite. Les autres propositions encore distinctes, comme P84, deviennent visibles dans Atlas sans remplacer les nœuds courants.

**statut**

Correction appliquée au backlog et à la présentation Atlas. Historique préservé dans les versions figées et Git ; aucune nouvelle validation métier ni release.


## C72

**id**

C72

**source**

U117/U118 ; P83–P87 ; audit du 2026-09-13.

**formulation_a_eviter**

Atlas doit proposer le backlog comme espace initial ; les propositions de noms courts sont toutes intégrées dans les nœuds JSON ; tous les domaines sont nécessairement obsolètes. Déduire une validation des aptitudes du choix de leurs noms de travail.

**formulation_retenue**

Atlas affiche uniquement la release sous le libellé Urbanisation. Le backlog et le panorama restent des fichiers de travail hors de cette interface. L’audit des douze repères confirme D01 corrigé, onze noms courts de D04–D07 à intégrer selon U118, neuf capacités D03 et cinq ingestions correctement reprises. D02, les décisions potentielles D05.a/c et les frontières D04/D06/D07 demeurent à discuter. Publier ces contenus conserve leurs statuts et n’arbitre pas leurs frontières.

**statut**

Remplace la consigne d’interface backlog par défaut et la visibilité des alternatives issue de U113/U115. La construction du modèle dans le projet reste dans le backlog. Les versions historiques restent conservées ; aucune nouvelle validation métier.


## C73

**id**

C73

**source**

U125/U126 ; CMP062, ELM103–ELM105.

**formulation_a_eviter**

La fusion des mouvements et de l’état dans Inventory Tracking reste la dernière orientation de travail. Ledger et mouvement sont synonymes ; Inventory Ledger Management est un nom adopté ou une capacité native Microsoft.

**formulation_retenue**

U125 demande de séparer les mouvements de stock du suivi de leur état. Le backlog remplace la capacité regroupée D01.e par D01.f Inventory Tracking (état résultant) et D01.g Inventory Movements (enregistrement, qualification et justification des mouvements), avec de nouveaux identifiants pour cette scission. U126 ouvre le nom Ledger ; Inventory Ledger Management reste une alternative proposée. Le registre est distinct des mouvements qu’il conserve. Six capacités D01 et 36 au total dans le backlog ; la release v001 garde ses cinq capacités D01 et 35 au total.

**statut**

Orientation de séparation appliquée au backlog ; définitions, noms et frontières détaillés proposés. Historique et release conservés, sans publication ni nouvelle validation métier.


## C74

**id**

C74

**source**

U129 ; candidat U127, séparation U125.

**formulation_a_eviter**

Inventory Movements est le nom courant de D01.g ; Record Inventory Movements et Inventory Ledger Management sont encore des noms en concurrence.

**formulation_retenue**

Record Inventory Movements est le nom adopté par Laurent le 2026-09-13 pour D01.g. La définition et la finalité restent proposées ; ne pas étendre la validation du nom. Les noms antérieurs Inventory Movements et Inventory Ledger Management restent historiques. Inventory Ledger peut continuer à désigner le registre, sans devenir le nom de la capacité. La séparation avec D01.f Inventory Tracking est conservée.

**statut**

Choix appliqué au backlog ; six capacités D01, 36 au total. Aucune publication. À la prochaine release, transcrire la validation U129 du seul champ name dans une nouvelle décision de publication visant D01.g et sa révision préparée.
## C75

**id**

C75

**source**

U134 ; précision de U97/U103, distinction U98 et orientation U100 conservées.

**formulation_a_eviter**

Chaque référentiel de la plateforme ne peut avoir exactement qu’une capacité d’ingestion ; visibilité et recherche sont exclues. D04 et Agreement peuvent être fusionnés parce qu’ils parlent tous deux d’engagements.

**formulation_retenue**

Les référentiels de la Supply sont des projections de sources de vérité gérées par des produits tiers. Chacun comporte au moins une ingestion ; visibilité et recherche en lecture seule sont admises. Création, administration et validation métier des données maîtresses restent externes. L’ingestion actualise la projection, sans lui transférer la maîtrise. Agreement de référence et commande restent distincts selon U98. Les responsabilités commerciales de D04 et sa frontière avec D07 restent à instruire ; la demande d’audit ne valide pas leur fusion ou leur remplacement.

**statut**

Principe consigné dans AGENTS.md et le backlog ; analyse dans audits/2026-09-13-d04-agreement-projections.md. Aucun ajout de capacité ni publication. Les formulations historiques U97/U103 sont conservées comme provenance ; U134 prévaut pour les aptitudes de consultation.
## C76

**id**

C76

**source**

U136 ; vérification Microsoft ELM106 du 13 septembre 2026.

**formulation_a_eviter**

Commitment est un synonyme de commande, ou désigne exclusivement l’engagement porté par une commande dans le marché.

**formulation_retenue**

D04 visait localement les engagements de commandes, mais Commitment ne désigne pas exclusivement cet objet : Microsoft nomme ainsi les engagements quantitatifs ou en valeur des lignes de Sales Agreements et Purchase Agreements, consommés par des commandes. Order désigne plus directement la commande ; Agreement et Order restent distincts. Les noms et frontières de D04 restent en instruction.

**statut**

Précaution lexicale enregistrée ; aucun renommage ni publication. Voir marche/orders-agreements-commitments.md et CMP063.
## C77

**id**

C77

**source**

U140 ; comparaison CMP065.

**formulation_a_eviter**

La demande de la couche Case et l’Order Supply sont un même objet ; Order Management reste seulement une suggestion sans orientation utilisateur, ou vise uniquement la vente B2C. Le choix d’un moteur suffit à définir toutes les variantes métier.

**formulation_retenue**

U140 distingue explicitement Case et Order et retient un domaine Order Management commun dans l’univers Supply, pour toutes natures de commandes, clients et volumes. D04 reprend ce nom ; ses capacités et frontières détaillées avec D07 ne sont pas automatiquement validées. Les contraintes B2B/B2C enrichissent l’analyse des aptitudes et règles ; elles ne justifient pas d’office deux domaines. Les univers et l’analogie TM Forum n’imposent pas une structure technique ou des cardinalités. Décisions et workflows restent distincts de leurs moteurs.

**statut**

Orientation et nom appliqués au backlog, ancienne formulation Commercial Commitments conservée ici et dans les releases. Définition nouvelle proposée par Codex ; aucune publication, aucune validation automatique des capacités héritées.
## C78

**id**

C78

**source**

U140/U141 ; CMP066.

**formulation_a_eviter**

Le backlog D04 contient toujours Commitment Creation, Commitment Revision, Commitment Reconciliation et Return and Replacement Decision ; les univers ne sont pas structurés ; l’Agreement exclut les engagements contractuels de période.

**formulation_retenue**

U141 applique Supply/Case comme univers explicites. D04 Order Management contient D04.e Order Registration, D04.f Order Revision, D04.g Order Visibility et D04.h Order Reconciliation. Les noms et descriptions courtes présentés sont validés par Laurent ; les compléments nouveaux restent proposés. Les anciens D04.a–d sont retirés de la carte active et conservés dans modeles/backlog/history/pre-U141.json : nouveaux résultats, nouveaux identifiants, aucune réutilisation. Agreement porte le contrat complet projeté, y compris périodes et engagements ; aucun pouvoir d’administration transféré. D04 suit la commande autorisée, D07 les engagements et faits d’exécution ; correspondances détaillées, reliquats et cas limites restent à instruire.

**statut**

Appliqué au backlog uniquement. Réexamen du droit commercial de retour/remplacement différé avec Case ; pas de perte du besoin, pas de capacité Case inventée. Release v002 conservée. Note de mise en œuvre : connaissance/27-order-management-et-univers.md.
