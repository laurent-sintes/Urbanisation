# Analyse — SRC-2026-09-18-BRD-FLUX

Source : [dossier et provenance](index.md), pièce originale conservée et contribution U309. Lecture du 18 septembre 2026.

## Ce que ce document apporte

Le schéma décrit un circuit de préparation de l’offre commerciale vers Elastic : PLM et le studio photo alimentent PIM Homerun ; une flèche attribuée probablement à SAP le rejoint aussi. Homerun, SAP et Salesforce alimentent un point d’échange nommé BRDS SFTP ; Elastic reçoit les imports régionaux et le schéma représente par ailleurs ses échanges avec SAP. Le panorama Boardriders courant ne documentait encore aucun flux : cette source apporte des relations concrètes à qualifier.

Trois constats méritent d’être conservés : **la préparation des catalogues rassemble plusieurs apports**, **la chaîne combine automatisation, import manuel et API**, et **la saisie des commandes dans Elastic est reliée à leur création dans SAP**. Cela ne démontre ni l’ensemble du cycle de commande, ni les règles de promesse, ni la fraîcheur des données.

## Convention de lecture

Une confiance **confirmée** signifie que le libellé ou la forme est clairement visible sur l’image, pas que le déploiement a été vérifié. **Probable** qualifie une lecture ou un rapprochement argumenté mais incomplet ; **incertaine** une ambiguïté restant ouverte. Le statut de tous les constats reste « décrit par le document ». L’actualité opérationnelle n’est pas établie.

Les ancres sont spatiales, car l’image ne porte ni pagination ni numérotation. Les extrémités textuelles ci-dessous sont des lectures du dessin, pas des identités d’instances résolues. Plusieurs flèches s’arrêtent avant les contours des blocs.

## Blocs et fonctions explicitement affichés

| Unité | Ancre dans l’image | Transcription et lecture neutre | Confiance / limite |
| --- | --- | --- | --- |
| <a id="N01"></a>N01 | Haut gauche | `PLM` ; aucune liste de fonctions sous le bloc. | Confirmée ; produit et version inconnus. |
| <a id="N02"></a>N02 | Haut centre | `SAP` ; `Customers Catalogs Permissions & Blocking Datas`, `VISTEX`, `Discounts`, `DD Dates Smoothing`. | Confirmée sur les mentions ; la ponctuation et les responsabilités détaillées ne sont pas précisées. Ni ECC, ni AFS, ni S/4HANA ne sont écrits ici. |
| <a id="N03"></a>N03 | Milieu gauche | `PIM Homerun` ; `Catalogs Creation`, `Assets Management`, `Products Permissions`. | Confirmée ; ne démontre pas une autorité exclusive sur toutes les données produit. |
| <a id="N04"></a>N04 | Centre | `BRDS SFTP`, icônes SFTP et AWS S3 ; `Permissions Mapping`, `Substitution`. | Confirmée ; emplacement d’exécution et sens de « Substitution » inconnus. Le nom d’un point d’échange ne prouve pas le lieu d’une décision métier. |
| <a id="N05"></a>N05 | Milieu droit | `elastic by Emerald`, icône AWS S3 ; `B2B Order Entry`, `Samples Forecast`, `Global FLA`, `FOC Order Entry`, `Mktg Presentations`. | Confirmée ; ne pas assimiler ce logo à Elasticsearch. Fonctions et périmètre effectif non vérifiés. |
| <a id="N06"></a>N06 | Bas gauche | `Photo Studio Global FTP`. | Confirmée ; ne permet pas de séparer le studio, son organisation et le service FTP en instances applicatives. |
| <a id="N07"></a>N07 | Bas centre | `Salesforce`, pictogramme CRM ; `Chatbot Articles`, `FAQ`. | Confirmée ; le contenu du bloc et le flux « Users & Prebook Access » sont deux indications distinctes. Aucun rôle de maître client global n’est prouvé. |

## Les dix tracés du schéma

| Unité | Ancre / extrémités lues | Libellé source | Modalité et confiance |
| --- | --- | --- | --- |
| <a id="E01"></a>E01 | Haut horizontal, PLM → SAP | `SMS & PROD Push / Repush` | Gris, non légendé. Direction et libellé confirmés ; automatisation inconnue, SMS/PROD non développés. |
| <a id="E02"></a>E02 | Vertical gauche, PLM → PIM Homerun | `Materials with regional adoptions & Mktg Datas / Mapping SAP Master Datas` | Vert : jobs/services automatiques. Confirmée ; conserver « adoptions » tel qu’écrit, sans le corriger en « adaptations ». |
| <a id="E03"></a>E03 | Diagonale haut centre → milieu gauche, SAP → PIM Homerun | `ATS Products / SAP Master Datas` | Vert : automatique. Libellé confirmé ; attribution à SAP probable par proximité, la flèche ne part pas du contour du bloc. |
| <a id="E04"></a>E04 | Vertical bas gauche, Photo Studio Global FTP → PIM Homerun | `Images / Videos / Mktg Assets` | Gris, non légendé. Confirmée ; ne pas classer manuel ou automatique. |
| <a id="E05"></a>E05 | Horizontal gauche → centre, PIM Homerun → BRDS SFTP | `Catalogs / Products / Assets` | Vert : automatique. Confirmée. |
| <a id="E06"></a>E06 | Vertical centre haut, SAP → BRDS SFTP | `Inventory / Customers / Reps / Prices` | Vert : automatique. Confirmée ; le sens détaillé de Reps n’est pas développé. |
| <a id="E07"></a>E07 | Vertical centre bas, Salesforce → BRDS SFTP | `Users & Prebook Access` | Vert : automatique. Confirmée ; ne définit pas les règles d’habilitation. |
| <a id="E08"></a>E08 | Horizontal centre → droite, BRDS SFTP → Elastic | `Regional imports` | Orange : imports manuels. Confirmée ; opérateur, fréquence, outil et effort inconnus. |
| <a id="E09"></a>E09 | Grand tracé vert périphérique, Elastic → SAP | `Orders Creation (Idocs & Webservices)` | Vert : automatique. Direction confirmée ; ni types de commandes SAP, ni messages, ni gestion des retours décrits. |
| <a id="E10"></a>E10 | Coude jaune entre SAP et Elastic, une pointe vers chaque bloc | `Prices & Inventory Checks` ; `Accounts History / Discounts` | Jaune : appels API. Confirmée pour le tracé à deux pointes et les deux libellés ; affectation précise requête/réponse et initiateur incertains. |

Il y a **un seul connecteur jaune à deux pointes**, pas deux interfaces techniques documentées séparément. Le schéma représente six tracés verts, deux gris, un orange et un jaune. Il ne décrit pas de flux direct Homerun → Elastic contournant BRDS SFTP.

## Légende, acronymes et date

| Unité | Ancre | Lecture | Qualification |
| --- | --- | --- | --- |
| <a id="L01"></a>L01 | Légende en bas à droite | Vert : `Automatic Jobs / Services` ; orange : `Manual imports` ; jaune : `API Calls`. `ATS : Available To Sell (In Stock)` ; `CRM : Customer Relationship Management` ; `FOC : Free of Charge` ; `FLA : Final Line Adoption`. | Confirmée ; le gris ne figure pas dans la légende. ATS n’est pas ici un synonyme établi d’ATP. |
| <a id="L02"></a>L02 | Pied sous la légende | Lecture probable : `Last Update : 11.05.2021`. | Année 2021 lisible ; petits caractères, jour à corroborer. Date de mise à jour du document, pas date d’observation des installations. |

`SMS`, `PROD`, `DD`, `Reps` et `Mktg` ne sont pas développés par la source. Les expansions courantes éventuelles ne sont pas nécessaires à la consignation. `DD Dates Smoothing` ne suffit notamment pas à attribuer une décision d’échéancier à SAP. Aucune explication de VISTEX ni comparaison de version SAP n’est ajoutée depuis une documentation externe.

## Interprétations utiles pour FLOW

| Unité | Appuis | Interprétation de Codex et intérêt | Limite / compromis |
| --- | --- | --- | --- |
| <a id="I01"></a>I01 | N01–N06, E02–E06 | **Préparation de l’offre à plusieurs contributeurs.** Homerun apparaît comme un lieu de préparation des catalogues et contenus, enrichi par PLM, SAP et les médias. Pour la cartographie, distinguer références produit, contenus commerciaux, prix et stock permet de rechercher leurs autorités par information. Confiance probable. | Un flux sortant ne prouve pas un maître exclusif. Les mentions « SAP Master Datas » ne font pas de SAP le maître de tous les attributs. |
| <a id="I02"></a>I02 | E05–E08, L01 | **Passage manuel dans une chaîne partiellement automatisée.** L’import régional mérite une investigation sur le déclenchement, le contrôle et la fraîcheur des données. Confiance confirmée sur le passage manuel, probable sur son importance opérationnelle. | Ni retard, ni erreur, ni irritant utilisateur avéré. Une automatisation cible n’est pas décidée ; le rôle de contrôle humain peut être intentionnel. |
| <a id="I03"></a>I03 | N02, N05, E06, E09–E10 | **Saisie commerciale et création dans l’ERP reliées mais distinctes.** Elastic porte une saisie B2B/FOC dans le dessin ; la création des Orders vise SAP, avec des contrôles prix/stock par API. Cela aide à séparer expérience de saisie, enregistrement transactionnel et consultation. Confiance probable sur cette lecture d’ensemble. | L’ordre temporel des contrôles, l’acceptation, la promesse, la réservation et la confirmation ne sont pas décrits. « Checks » ne prouve ni ATP, ni temps réel, ni engagement ferme. |
| <a id="I04"></a>I04 | N02–N04, E07 | **Permissions réparties entre plusieurs points du circuit.** Permissions/blocages SAP, permissions produits Homerun, mapping BRDS SFTP et accès Prebook Salesforce justifient d’examiner les règles et leur propagation. Confiance probable. | Il peut s’agir de notions différentes : visibilité d’assortiment, droits commerciaux ou accès technique. Pas de règle commune ni d’incohérence démontrée ; aucun comportement Supply Protection déduit. |

Ces propositions s’appuient sur les frontières du modèle local : produit/catalogue, transaction Order, visibilité du stock et habilitations restent distincts. Leur bénéfice est la qualification des interfaces ; leur compromis est de conserver les responsabilités ouvertes lorsque le schéma ne les établit pas. Aucune comparaison marché nouvelle n’est établie par ce dossier.

## Réconciliation avec le dépôt

Références consultées : [index As Is](../../../modeles/panorama-as-is/current.json), [panorama Boardriders 2026-09-13.1](../../../modeles/panorama-as-is/boardriders/versions/2026-09-13.1/panorama.json), [composants](../../07-composants.md), [flux](../../08-flux.md), [autorités](../../10-autorites-information.md), [responsabilités](../../11-responsabilites-decision.md), [corrections](../../04-corrections.md), [besoins à instruire](../../../modeles/backlog/panorama-candidates.json) et [modèle courant](../../../modeles/backlog/model.yaml).

| Connaissance existante | Unités | Relation | Effet proposé et réserve |
| --- | --- | --- | --- |
| Boardriders : APP-ECC, APP-AFS, APP-NEW ; aucun flux dans la version consultée | N01–N07, E01–E10 | Enrichit / Nouveau | Ajouter ultérieurement une description documentaire datée de ce circuit ; zéro flux antérieur signifie absence de documentation, pas absence d’interfaces. |
| APP-ECC : SAP ECC déclaré Boardriders | N02 | Enrichit, identité à confirmer | Le document emploie seulement « SAP ». Conserver ce libellé avant rapprochement avec une instance ECC. |
| APP-AFS et APP-NEW, Boardriders | N02, N05 | Non couvert par cette source | AFS/Allocation Run et NewStore ne sont pas nommés. Leur absence ne les contredit pas ; Elastic ne remplace pas NewStore par déduction. |
| APP-ELA, APP-ZOH, FL20, INF10/INF16, périmètre historique Beaumanoir ; U03 commence par « On commence par GBM » | N05, N07, E05–E08 | Nouveau contexte / identité non résolue | Préserver l’Elastic historique et son contexte Zoho. Aucune instance partagée ou migration Zoho → Homerun/Salesforce n’est prouvée. |
| INF18–INF20 et U97/U98 : orientations Party / Role, Agreement et Catalog | N02–N07 | Enrichit comme cas d’épreuve ; aucune confirmation de déploiement cible | Préparation des catalogues et données clients éclairent les interfaces ; aucun Agreement n’est explicite, aucun maître exclusif désigné. |
| DEC21/DEC22 : besoins Boardriders d’engagement, arbitrage et réexamen | E03, E06, E09–E10 | Non couvert par cette source | ATS, stock et création des Orders ne prouvent pas affectation, réservation ou réarbitrage installés. |

L’inventaire du dépôt ne contient pas de registre gouverné `docs/as-is/insights`, `hotspots` ou de convergence tel que celui du skill. Les analyses proches conservées dans [connaissance/18](../../18-politiques-engagement-gbm-brd.md), les questions et les annexes du backlog restent leurs supports existants ; aucun insight/hotspot parallèle n’est créé. Aucune contradiction franche avec une observation de même date, même instance et même périmètre n’est établie.

## Rapprochements possibles avec les capacités existantes

Les capacités ont été recherchées dans le modèle courant par finalité. Ces rapprochements sont des **candidats de lecture**, non des résultats d’applicabilité ou de couverture validés. Le rôle est relatif à la portion explicitement décrite, jamais au produit entier.

| Capacité existante | Réalisation décrite / rôle candidat | Unités | Couverture et confiance |
| --- | --- | --- | --- |
| D04.i — Sales Order Management | Elastic : **Contributeur** pour la saisie ; SAP : **Partiel** pour la création des commandes reçues | N05, E09 | Probable ; B2B rend le rapprochement plausible, mais types d’Orders, périmètre FOC et cycle complet non établis. Aucun porteur Principal démontré. |
| D01.c — Inventory Visibility | SAP : **Contributeur** de données ; Elastic : **Consommateur** de données/contrôles | E06, E10 | Probable ; contenu du stock, disponibilité et fraîcheur non détaillés. |
| D08.d — Product Reference Ingestion | PLM/SAP : **Contributeurs** d’informations ; Homerun : **Consommateur** apparent | E02–E03 | Probable ; cas analogue de réception de références, sans équivalence entre PIM et projection Supply ni extension à l’administration des maîtres. |
| D12.a — Catalog Ingestion | Homerun : **Contributeur** amont ; BRDS SFTP : **Contributeur** technique ; Elastic : **Consommateur** via import | N03, E05, E08 | Probable ; préparation des catalogues externe à distinguer de leur ingestion. Prix/versions/zones à préciser. |
| D09.d — Party / Role Ingestion | SAP : **Contributeur** pour Customers ; Salesforce : contribution d’utilisateurs à qualifier | E06–E07 | Incertaine ; client, représentant, utilisateur et Party/Role ne sont pas équivalents par défaut. Aucun mapping Salesforce → référentiel Party validé. |

Photo Studio Global FTP contribue aux contenus marketing (E04), sans capacité Supply autonome déduite. La mention VISTEX reste attachée à N02, sans assimilation à une application installée autonome. Aucun **Contournement** n’est démontré : l’import manuel peut être une pratique normale. Aucune nouvelle capacité n’est justifiée ; aucune couverture D03.i ATP, D03.n Promise Management, D02.b Supply Protection, D02.e Supply Assignment ou D11.a Agreement Ingestion n’est établie par ce schéma.

## Questions qui conditionnent une intégration plus précise

1. **Date et périmètre** : confirmer la date imprimée, l’auteur, les pays/marques concernés, l’usage réel à cette date et ce qui reste valable aujourd’hui.
2. **Identité des systèmes** : quel SAP et quel PLM ? Quel périmètre d’Elastic by Emerald ? Une instance partagée avec le périmètre historique est-elle documentée ?
3. **Contrats de flux** : fréquence, déclencheur, granularité, identifiants, acquittements et reprises des imports ; rôle exact de BRDS SFTP et des icônes S3.
4. **Sémantique** : sens de Substitution, SMS/PROD, DD Dates Smoothing, Reps ; définition opérationnelle d’ATS et du stock transmis ; contenu de Global FLA.
5. **API et commandes** : initiateur et réponses des contrôles, moment dans la saisie, effet d’un refus, différence entre commande créée et commande acceptée/promesse confirmée.
6. **Permissions** : objets autorisés, règles commerciales vs accès technique, producteurs et contrôles de cohérence.

Suivis proposés : recueillir la documentation d’interface et un scénario réel d’import/création. Aucun responsable, délai, incident, volume, SLA ou coût n’est inventé. Aucun arbitrage de convergence, impact Change avéré ou récit de migration historique n’est déduit. Les zones à instruire sont la fraîcheur des données, la propagation des permissions et la visibilité des échecs ; elles restent des hypothèses d’investigation.
