# Journal des évolutions

## 2026-09-13 — U130 : publication Urbanisation v002 dans Atlas

- Publication `2026-09-13.4`, descripteur `urbanisation-v002-2026-09-13-162623.json`, activée le 13 septembre à 16:26:23 UTC ; modèle révision 2. [Note de release](modeles/release/2026-09-13.4/release-notes.md).
- D01.e remplacée par D01.f Inventory Tracking et D01.g Record Inventory Movements. Six capacités D01, 36 au total ; neuf capacités entièrement validées. Tous les autres nœuds publiés sont inchangés, avec leurs métadonnées préservées.
- ADOPT-048 enregistre le seul nom de D01.g validé en U129 ; 46 décisions antérieures conservées et aucune suspension supplémentaire. Les définitions et frontières proposées restent qualifiées.
- Contrôles du candidat et du modèle publié : zéro erreur. Identité du serveur FLOW Atlas vérifiée, API modèle identique au JSON publié pour les nœuds et relations, catalogue trié avec v002 en tête. Serveur existant PID 836 ; actualisation automatique des données sans relance nécessaire.
- Modèle, révisions, décisions, sources et note figés ; ancienne release conservée. Aucun commit ou push réalisé.

## 2026-09-13 — U124 : audit de complétude D01

- Vérification des anciennes réponses, des sources P81/P82, des releases .2/.3 et de l'API Atlas : six capacités puis cinq par regroupement positions/faits, conforme à U116.
- Ancienne liste de sept autour du stock retrouvée dans la grille U37 ; son périmètre dépassait D01. Aucune mention de ledger antérieure à U124 retrouvée dans les textes du projet et les messages locaux de cette conversation.
- L'audit `audits/2026-09-13-d01-completude.md` distingue fidélité technique et complétude métier : dimensions du stock, règles de consommation des protections, ajustement et libération des réservations moins explicites dans les définitions JSON.
- Aucun changement du modèle ni nouvelle publication. Le souvenir du ledger reste à éclaircir ; aucune capacité supplémentaire inventée.

## 2026-09-09 — Reprise du dossier ChatGPT dans le répertoire de travail

- Création du point d'entrée et des règles de maintenance.
- Import des 15 sections du JSON dans des registres Markdown, en conservant tous les champs, identifiants, statuts, réserves et textes non vides.
- Aucune nouvelle validation métier, aucun arbitrage de cible et aucune nouvelle vérification des références externes.
- Conservation des trois fichiers initiaux. Examen de la structure du Word (17 chapitres, 34 tableaux), sans audit de mise en page ni comparaison exhaustive Word/PDF/JSON.

### Empreintes SHA-256 des sources à la reprise

- `referentiel.json` : `7a548576288a4a72c47eea8f2a7ba39f33df9fc79395b4dd88a930b7325689ed`
- `Beaumanoir_Dossier_reference_v0.1.docx` : `6759ba08f766b50111f7bb814286017c435478604316f9395ddb648bf5aecda9`
- `Beaumanoir_Dossier_reference_v0.1.pdf` : `99252ffbe42a1b3bf7f519a1a236bfd2248a97a7599f212b5dc373ce2228748e`

## 2026-09-09 — Consignes de fonctionnement et archivage

À la demande de Laurent :

- Centralisation de l'objectif et des règles de travail dans `AGENTS.md`.
- Adoption du tutoiement dans les échanges.
- Déplacement des trois fichiers d'origine dans `archive/`, sans modification de leur contenu. Les empreintes ci-dessus restent applicables.
- Mise à jour des liens du README et des références de provenance des registres ; `CONVENTIONS.md` renvoie désormais à `AGENTS.md`.

## 2026-09-09 — Référentiel de marché et premières comparaisons

- Enregistrement de la demande de Laurent en U14 et F103 ; rôles proposés et méthode en P57.
- Création de `marche/` : point d'entrée, huit fiches de référence et ITIL périphérique, méthode, huit éléments externes sélectionnés et huit comparaisons exploratoires.
- Consultation de sources officielles SAP, Oracle, IBM, APQC, OMG, Business Architecture Guild, The Open Group et PeopleCert ; détails et limites conservés dans le catalogue. Les mentions de versions indiquent les éditions observées, sans garantie d'être les dernières disponibles.
- Six pistes lexicales IBM couvrent 11 capacités candidates ; 24 restent sans comparaison d'élément précis. Deux autres observations concernent la structure. Aucune équivalence validée, aucun arbitrage de cible.
- Mise à jour de `AGENTS.md`, du README et du registre bibliographique pour intégrer la comparaison au marché au fonctionnement courant.
- Documents d'origine conservés sans modification dans `archive/`.

## 2026-09-09 — Audit direct de la conversation ChatGPT d’origine

Demande U15. Capture des 30 messages rendus du fil partagé, conservée en JSON et en copie de lecture Markdown dans `archive/`. Les 13 contributions de la consolidation initiale sont identiques après normalisation ; les deux prompts postérieurs sont importés sous U16 et U17.

Réintégration de développements assistant, de leurs réserves et alternatives : P08/P09/P14/P18/P21/P23/P28/P30/P32/P34/P42/P45/P56 ; ajouts P58/P59, CAP036 et A10–A13. Précision de la chronologie A08/A09. Référence Cegid 2019 retrouvée et annonce vérifiée (R23/A03/C28), attribution historique du lexique UR explicitée (R22), réserves de réservation et de coexistence SCORTEX précisées (C29/C30, DEC02). Aucune nouvelle validation métier.

Mise à jour du README, d’AGENTS.md, de l’audit de couverture et du suivi de comparaison marché. Rapport détaillé : [audit du fil](audits/2026-09-09-conversation-chatgpt.md). Le ZIP supplémentaire annoncé dans ChatGPT n’a pas été récupéré ; son contenu reste hors audit. Aucun dépôt Git ni stockage distant créé.

### Empreintes des nouvelles captures

- `archive/conversation-chatgpt-2026-09-09.json` : `09393a0b89be781c769eb18eb978a658b97cbcd6b37b94fdd41baf36b9f8d6a8`
- `archive/conversation-chatgpt-2026-09-09.md` : `e0596d663c934ae4a86b7b09170cb1ec2decf583295417e374d1add42a2fc6a4`

## 2026-09-09 — Deux urbanisations métier et contrats durables

Apports U18/U19/U20 enregistrés : socle ERP lié au métier de manière générique et couche processus/organisation/situations, chacun avec modèle, objets, persistance et urbanisation propres ; interfaces par contrats durables.

- Ajouts F104–F110, A14, P60–P62 et Q062–Q064 ; précisions de F011/F012 et C14 pour conserver la nouvelle intention sans la réduire à une orchestration sans métier.
- Création de l’[analyse d’orientation](connaissance/15-orientation-deux-couches.md) ; mise à jour d’AGENTS.md et de la navigation.
- Comparaison aux distinctions SAP, aux services/contrats OASIS et aux modèles OMG ; OpenAPI/AsyncAPI identifiés comme formats d’interface. DDD utilisé comme appui de conception, sans assimiler ses couches internes aux deux urbanisations complètes.
- Nouveau contrôle ciblé de R13/R15 et ajout R30 (FAQ NIST RBAC). Les passages consultés et limites d’accès sont datés dans la note et le marché.
- Quatre références marché ajoutées (MKT09–MKT12), cinq éléments (ELM009–ELM013) et quatre correspondances méthodologiques proposées (CMP009–CMP012). Aucun standard adopté comme architecture ; aucun candidat reclassé ou renommé. Les 36 candidats restent 11 avec pistes lexicales IBM et 25 sans comparaison précise.
- État courant : 20 contributions utilisateur, 110 assertions/orientations, 14 contributions assistant, 62 propositions, 64 questions dont 56 ouvertes et 8 résolues. Les archives et l’audit antérieur restent des instantanés historiques inchangés.

## 2026-09-09 — Priorité au socle transactionnel et première vue des capacités

Demande U21, priorité F111 : explorer d’abord le socle à partir de l’histoire Beaumanoir. Priorité enregistrée dans AGENTS.md et le README ; réponse A15, proposition P63.

Création de la [vue des capacités du socle](connaissance/16-capacites-socle-transactionnel.md) : huit familles proposées, appuis du récit et réserves, distinction stock/visibilité/disponibilité/protection/engagement. Les 27 candidats mobilisés, parfois partiellement, et les neuf aux frontières couvrent les 36 CAP sans modifier leurs définitions. C-Log conserve son autonomie ; planification et traitement organisationnel restent aux frontières utiles.

Liens ajoutés dans le catalogue candidat, l’orientation à deux couches et le suivi marché. Les pistes lexicales existantes sont réutilisées avec leur limite ; aucune nouvelle vérification externe, équivalence ou validation métier. Les 64 questions restent inchangées, dont 56 ouvertes et 8 résolues.

## 2026-09-09 — Le stock dans les capacités SAP

Demandes U22/U23, analyse A16 et proposition P64. Création de la [note SAP-stock](marche/sap-stock.md) : Inventory Management est un Business Area SAP ; distinction stock, promesse et entrepôt. Lecture visuelle d’un extrait RBA et de cours fonctionnels S/4HANA, avec dates, localisateurs et limites ; aucun export complet ni édition du catalogue établi.

Complément MKT04, ajout MKT13, ELM014–ELM018 et CMP013–CMP017. Les correspondances sont proposées, sans équivalence ni preuve d’usage local. 15 CAP ont désormais au moins un rapprochement documentaire, 21 restent sans comparaison précise. Définitions des 36 CAP inchangées, finance exclue comme domaine, autonomie C-Log et réserves MAP/GBM/ARun conservées.

Q065 ouvre l’exploration du comptage et des corrections d’inventaire autour du stock magasin ; aucune capacité nouvelle ou absente présumée. Navigation et vue du socle actualisées. État : 23 apports utilisateur, 111 assertions, 16 contributions assistant, 64 propositions, 65 questions (57 ouvertes, 8 résolues) ; marché : 13 références hors ITIL périphérique, 18 éléments et 17 comparaisons. Aucune nouvelle validation métier. Archives préservées.

## 2026-09-09 — Correction du niveau Enterprise Domain SAP

Apport U24, correction C31 : Enterprise Domain avait été omis dans la présentation de la hiérarchie complète à U23. Le cours officiel SAP confirme le regroupement supérieur : Enterprise Domain → Business Domain → Business Area → Business Capability. La chaîne du stock est restituée dans la [note SAP-stock](marche/sap-stock.md).

MKT04, ELM001/ELM014, CMP001/CMP013, A16, R03 et navigation corrigés. L’ancienne comparaison fondée sur « les deux options envisagent trois niveaux » est conservée dans C31 comme formulation remplacée. Inventory Management reste une aire métier ; aucune hiérarchie locale ni capacité n’est adoptée ou modifiée. État : 24 apports utilisateur, 31 corrections ; autres comptes inchangés. Archives préservées.

## 2026-09-09 — Étude comparative des modèles du marché

Demande U25, priorité F112, réponse A17 et proposition P65. Étude livrée dans [marche/etudes/2026-09-09-modeles-marche/etude-comparative.md](marche/etudes/2026-09-09-modeles-marche/etude-comparative.md), avec quatre annexes de preuves. Dix références comparées, matrices séparant cartes métier et processus/données, cas stock/allocation/retours, sources numérotées et limites d’accès/version.

Approfondissements : guide Oracle 14.1.1 historique public, fiche Oracle actuelle à mentions de versions hétérogènes, structure PCF générale (fichier Retail 7.2.1 non lu), narration ARTS 7.3 dont vues 02010/07620, matrice IBM 2005, atelier Guild 2019, documents historiques Open Group sur miroirs identifiés, cours et extraits éditoriaux SAP. Ajouts distincts du catalogue de processus Dynamics et de la carte Microsoft retail 2012 hébergée par APQC.

MKT01–MKT08 complétés ; MKT14/MKT15 créés ; ELM019–ELM030 et CMP018/CMP019 ajoutés. Navigation et AGENTS actualisés. Aucune capacité locale, autorité ou frontière C-Log modifiée ; aucune équivalence de catalogue ni hiérarchie principale validée. Q001 et les autres questions restent ouvertes/résolues selon leur état antérieur.

État : 25 contributions utilisateur, 112 assertions/orientations, 17 contributions assistant, 31 corrections, 65 propositions, 65 questions (57 ouvertes et 8 résolues), 36 CAP. Marché : 15 références hors ITIL périphérique, 30 éléments, 19 comparaisons ; 15 CAP avec rapprochement documentaire et 21 sans comparaison précise. Les nouvelles matrices intermodèles ne constituent pas de nouveaux liens validés aux CAP.

Revue indépendante de la synthèse : niveaux Oracle/APQC, attribution Microsoft, portée ARTS et distinctions de structure vérifiés. Précision apportée à la cellule SAP des retours : le support client cité ne démontre pas leur traitement physique. Les cinq archives restent inchangées.

## 2026-09-09 — Bloc stock, disponibilité et stock virtuel/logique

Apports U26/U27 enregistrés sans transformer la proposition en décision. F113/F114 en conservent la portée ; analyse A18 et proposition P66 dans [l’exploration du bloc stock](connaissance/17-exploration-bloc-stock.md).

Proposition de trois familles : états/mouvements/visibilité, disponibilité par usage/horizon et allocations/protections/engagements. Le terme Management est discuté comme axe transversal de modification. Stock virtuel/logique : vue consolidée, quantité calculée, pool affecté ou ressource externe/future à distinguer. Q066 conserve la question ouverte ; aucun quatrième bloc adopté. Exemple fictif avec protections/réservations imbriquées et absence de double compte.

Sources SAP RBA, Microsoft allocation virtuelle et ARTS 07620 reconsultées ; CMP020 ajouté. Visibilité distincte de l’autorité, dimensions lieu/transit/douane potentiellement superposées, autonomie C-Log préservée. Aucun nouveau CAP, aucune définition élargie, aucun comportement GBM/MAP/ARun déduit. Navigation, vue du socle et AGENTS actualisés.

État : 27 contributions utilisateur, 114 assertions/orientations, 18 contributions assistant, 66 propositions, 66 questions (58 ouvertes et 8 résolues), 31 corrections, 36 CAP. Marché : 15 références, 30 éléments, 20 comparaisons ; toujours 15 CAP avec rapprochement documentaire et 21 sans comparaison précise. Archives inchangées.

## 2026-09-09 — Allocation, réservation et évolution SAP

Apports U28/U29, assertions déclaratives F115/F116, analyse A19, proposition P67 et question Q067. La [note SAP/Microsoft](marche/allocation-reservation-sap-microsoft.md) distingue lisibilité du vocabulaire, diversité des mécanismes et évolution des réalisations. Sources primaires Microsoft Inventory Visibility et SAP Learning/Help, avec dates, éditions et limites d’accès.

Ajouts MKT16 pour ERP Fashion historique, ELM031–ELM033 et CMP021. Le regroupement historique d’ARun est étayé pour Fashion ; sa disparition ou une scission unique dans tout ECC ne sont pas démontrées. L’articulation ARun/BOP demeure. Distinction proposée entre enveloppe de groupe, réservation de demande, affectation de ressource, confirmation et réexamen ; pas de cinq nouvelles CAP. La note stock précise la différence entre enveloppe initiale et mesure de solde.

État : 29 apports utilisateur, 116 assertions, 19 contributions assistant, 31 corrections, 67 propositions, 67 questions dont 59 ouvertes et 8 résolues ; 16 fiches marché, 33 éléments, 21 correspondances. Les 36 CAP, leurs définitions et statuts restent inchangés ; 15 avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée. Archives préservées.

## 2026-09-09 — Politiques GBM/BRD et rattachement du réexamen à la promesse

Apports U30/U31, F117–F121, A20, P68/P69 et Q068 intégrés dans la [note de travail](connaissance/18-politiques-engagement-gbm-brd.md). Besoin BRD explicite : protection/allocation, réservation, engagement sur ressources futures et réaffectation prioritaire. Principe GBM de réservation au passage de commande précisé ; Q018 et Q049 partiellement renseignées sans fermeture. Q067 conserve la transition historique et le sens technique de uncovered ouverts. DEC21/DEC22 tracent les décisions BRD attendues sans autorité inventée.

CAP006/CAP010/CAP014/CAP035 enrichies de provenance et de besoin ; résultats et statuts candidats conservés. C32 garde les formulations antérieures. Les vues du socle et du stock sont reliées à l’affinement : réexaminer les promesses relève du côté Order Promising, avec effets coordonnés sur les engagements de ressources ; cette frontière reste proposée, au sein du socle envisagé.

ELM034–ELM036 et CMP022/CMP023 ajoutés. Microsoft SCM documente aussi la réservation d’entrées futures. SAP permet la révision sous conditions ; aucune création de ressource par priorité. BOP est explicitement sous Order Promising dans la documentation de solution SAP ; cela ne prouve pas une feuille RBA. Sources, éditions et accès indexés/textuels datés dans la note.

État : 31 apports utilisateur, 121 assertions, 20 contributions assistant, 32 corrections, 69 propositions, 68 questions dont 60 ouvertes et 8 résolues ; 22 responsabilités de décision. Marché : 16 fiches, 36 éléments et 23 correspondances. Les 36 CAP restent candidates ; 15 avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée. Archives conservées.

Contrôle après intégration : identifiants uniques et séquentiels, comptes ci-dessus vérifiés, 314 liens locaux et leurs ancres valides, exemples quantitatifs cohérents et cinq empreintes d’archives inchangées. Relecture indépendante de la note appliquée (présence physique distincte du disponible libre).

## 2026-09-09 — Libellés canoniques dans les documents

Consigne de Laurent ajoutée dans [AGENTS.md](AGENTS.md) : GBM et BRD sont autorisés dans les échanges et les noms de fichiers ; les documents rédigés utilisent les libellés canoniques des entités, y compris dans les titres, tableaux et légendes. Les verbatims, identifiants et chemins conservent leur fidélité aux sources. Consigne de fonctionnement, sans nouvel apport métier ni changement des comptes des registres.

## 2026-09-09 — Détail sous les fonctions de stock et de promesse

U32, F122, A21 et P70 intégrés dans la [note de granularité](marche/detail-fonctions-stock-promesse.md). Les fonctions précédemment présentées sont détaillées par opérations, objets, états, variantes et règles. Distinction conservée entre ce détail de produit et une hiérarchie de sous-capacités RBA, non vérifiée sous les feuilles consultées. Exemples Microsoft Inventory Visibility/SCM et SAP SUP/PAL/ARun/BOP, avec éditions et localisateurs.

ELM037–ELM039 et CMP024 ajoutés. Grille proposée pour les fiches de capacités : résultat, objets, opérations, règles, effets/garanties et réalisation. Aucun changement des définitions CAP ni nouvelle capacité ; frontières de planification et d’Order Promising préservées. Les nouveaux textes rédigés emploient les dénominations complètes des entités selon AGENTS.md.

État : 32 apports utilisateur, 122 assertions, 21 contributions assistant, 32 corrections, 70 propositions ; 68 questions dont 60 ouvertes et 8 résolues, 22 responsabilités de décision. Marché : 16 fiches, 39 éléments et 24 correspondances. Les 36 CAP restent candidates ; 15 avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée. Archives conservées.

Contrôle : identifiants et comptes vérifiés, 334 liens locaux/ancres valides, cinq archives inchangées. Relecture indépendante appliquée : périmètre historique explicite et critère de décomposition lié à la capacité mère.

## 2026-09-09 — Définition de capacité, glossaire et provenance des verbes

U33–U35 enregistrés, avec F123–F127, A22 et P71. La définition impérative de capacité est réaffirmée dans [AGENTS.md](AGENTS.md) : ce que sait faire l’entreprise indépendamment de son organisation et de ses outils. C33 précise P70, la note de granularité et CMP024 : responsabilités et contrats ne suffisent pas à justifier une décomposition.

Le [glossaire métier](connaissance/19-glossaire-metier.md) amorce 29 notions et 25 verbes, ainsi que des familles de demandes illustratives. Hormis la définition de capacité réaffirmée par Laurent, les définitions restent proposées. Demande/commande, stock logique et politiques de Boardriders conservent leurs questions ouvertes. Aucun schéma de données, cycle de vie universel ou renommage CAP n’est adopté.

C34 clarifie fonction : fonctionnalité de produit dans les réponses précédentes, aucun niveau hiérarchique local adopté. Tenir provient d’une formulation de l’assistant et reste en réexamen après U35. ELM040/CMP025 tracent les exemples anglais SAP Manage/Maintain, avec sources, éditions et accès indexés ; aucune traduction française canonique ni absence du mot tenir chez SAP démontrée.

Navigation, méthode de comparaison et introduction du catalogue reliées au glossaire. Les définitions des 36 candidats restent inchangées. État : 35 apports utilisateur, 127 assertions, 22 contributions assistant, 34 corrections, 71 propositions ; 68 questions dont 60 ouvertes et 8 résolues, 22 responsabilités de décision. Marché : 16 fiches, 40 éléments et 25 comparaisons ; 15 CAP avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée.

Contrôle après intégration : identifiants uniques et séquentiels, comptes vérifiés, 361 liens locaux et ancres valides, cinq empreintes d’archives inchangées. Relecture indépendante du glossaire et de la provenance lexicale : aucune contradiction matérielle relevée avec U33–U35.

## 2026-09-10 — Hypothèse sur les natures de capacité

U36 conserve la demande d’état des lieux et A23 consolide la réponse à huit lignes utilisée dans l’échange suivant. U37/F128 tracent l’hypothèse de Laurent : Capturer, Aider, Décider, Administrer, Administrer, Gérer et Optimiser. L’interprétation écartant la commande client et reliant Optimiser au réexamen des promesses est signalée comme telle.

A24/P72 et le [complément du glossaire](connaissance/19-glossaire-metier.md#hypothèse-sur-les-natures-de-capacité) examinent une qualification de la contribution métier, transverse aux domaines et niveaux. Distinctions : information, évaluation/décision et engagement ; définition et administration d’une politique ; révision et optimisation. U38/U39 précisent qu’Optimiser et Aider expriment des intentions. Laurent propose Adapter pour l’évolution des volumes et contenus des objets existants ; l’assistant propose Restituer pour la visibilité contextualisée. F129/F130 et C35 tracent cette évolution de A24/P72 et du glossaire. U40/U41, F131/F132, précisent les intentions multiples et conduisent à ajouter une colonne pour le pourquoi au tableau de travail : type d’effet et utilité sont distingués, avec des exemples proposés. U42/F133 retiennent le libellé Finalité ; C36 garde l’intitulé initial et AGENTS.md consigne ce choix. Les catégories et leurs correspondances restent proposées ; aucun niveau d’urbanisation ni classement obligatoire adopté.

Les 36 fiches CAP sont inchangées ; les entrées TER/VER restent au nombre de 29/25. Aucune nouvelle vérification de marché : MKT16, ELM40 et CMP25 en nombre, bilan de 15 CAP avec rapprochement documentaire et 21 sans comparaison précise conservé. État des registres : 42 apports utilisateur, 133 assertions, 24 contributions assistant, 36 corrections, 72 propositions, 68 questions dont 60 ouvertes et 8 résolues. Archives conservées.

Contrôle après intégration : identifiants uniques et séquentiels, comptes et statuts vérifiés, 378 liens locaux/ancres valides. Empreintes du catalogue CAP et des cinq archives inchangées. Colonne Finalité vérifiée ; relecture conceptuelle indépendante appliquée aux distinctions de nature, intention et engagement.

## 2026-09-10 — Premier niveau de regroupement et marché

U43/F134, A25 et P73 intégrés dans la [note comparative ciblée](marche/premier-niveau-regroupement-capacites.md). Six références réexaminées : SAP RBA, TOGAF G189, atelier Guild 2019, IBM CBM 2005, Microsoft Dynamics et introduction APQC. Versions, sources et localisateurs conservés ; les supports historiques ne sont pas présentés comme les dernières éditions.

Comparaison des catégories nommées, capacités composites, matrices et taxonomies de processus. Proposition Domaine → Capacité, avec détails supplémentaires au besoin ; distinction avec Nature et Finalité. Exemple de vue Stock/Promesse, sans rattachement définitif de disponibilité ou d’engagements ni modification des CAP. Domaine, Domain Area et bloc explicités comme choix de convention à discuter.

CMP026 ajouté ; six éléments existants enrichis de leur réexamen, sans nouvel ELM ni MKT. Catalogue, navigation et glossaire reliés à la note. État : 43 contributions utilisateur, 134 assertions, 25 contributions assistant, 36 corrections, 73 propositions ; 68 questions dont 60 ouvertes et 8 résolues. Marché : 16 références, 40 éléments, 26 comparaisons ; 36 CAP candidates, dont 15 avec rapprochement documentaire et 21 sans comparaison précise, zéro équivalence validée. Archives préservées.

Contrôle : identifiants et comptes vérifiés, 398 liens locaux/ancres valides, empreintes du catalogue CAP et des cinq archives inchangées. Sources, types de modèles, éditions et distinction catégorie/capacité relus ; aucune équivalence par numéro de niveau déduite.

Complément pendant le même échange : U44/F135 restituent la proposition Univers / Domaine / Capacité du draft de juin, dont le document lui-même n’a pas été consulté. A25/P73/CMP026 et la note examinent cette hypothèse ainsi que l’option plus compacte ; aucun étage n’est assimilé automatiquement à un niveau SAP. Comptes actualisés : 44 contributions utilisateur et 135 assertions ; autres comptes inchangés.

Complément U45/F136 : le sens du domaine est guidé par l’espace de problèmes métier, dans la lecture de DDD exprimée par Laurent. Source primaire Evans 2015 vérifiée, MKT17/ELM041/CMP027 ajoutés. Définition native distincte de l’interprétation locale ; domaine, modèle et bounded context séparés. C37 actualise la définition de travail dans P73, la note et TER030 ; AGENTS.md consigne le critère de délimitation. État final de l’échange : 45 contributions utilisateur, 136 assertions, 25 contributions assistant, 37 corrections, 73 propositions ; 30 notions et 25 verbes. Marché : 17 références, 41 éléments et 27 comparaisons. Les 36 CAP, les 68 questions et la couverture 15/21 restent inchangées.

Contrôle final après U44/U45 : identifiants et comptes vérifiés, 406 liens locaux/ancres valides ; catalogue CAP et cinq archives inchangés. La provenance de juin, la définition d’Evans et les propositions locales sont séparées ; aucune hiérarchie DDD ou correspondance technique imposée.

## 2026-09-10 — Problèmes liés et limite de l’étape métier

U46, F137/F138 et A26 intégrés. TER030 et P73 précisent la cohérence du domaine par les liens entre ses problèmes, sans exiger l’absence de relations avec les autres domaines. C38 et AGENTS.md conservent la limite de l’étape : cartographier problèmes et capacités, sans engager de conception en bounded contexts, applications ou services. Les définitions externes restent une provenance documentaire.

MKT17/ELM041 distinguent le mémento de 2015 du livre : extrait public éditeur ©2004, impression juin 2011, examiné de manière ciblée. La phrase exacte évoquée n’a pas été localisée dans cet extrait ; aucune absence dans le livre complet déduite. Pas de nouvelle référence, capacité ou équivalence créée ; CMP027 précise la méthode. État : 46 apports utilisateur, 138 assertions, 26 contributions assistant, 38 corrections, 73 propositions ; 30 notions et 25 verbes. Les 36 CAP, 68 questions (60 ouvertes, 8 résolues), 17 références marché, 41 éléments et 27 comparaisons restent inchangés.

Contrôle : identifiants, comptes et statuts vérifiés, 408 liens locaux/ancres valides ; empreintes du catalogue CAP et des cinq archives inchangées.

## 2026-09-10 — Première liste de domaines confrontée aux récits

U47 enregistré avant F139, A27 et P74. La nouvelle note connaissance/20-domaines-candidats.md propose six domaines pour le noyau déjà décrit, des cas d’épreuve sourcés et les zones achats, retours/SAV et référentiels à compléter. Le comptage et les écarts restent à explorer dans Stock. La méthode articule une première liste éclairée par le marché et les récits existants ; l’appréciation de couverture de Laurent reste distincte d’une preuve d’exhaustivité. Besoins Boardriders et réalisation installée restent séparés.

ELM019 réexaminé sur G189 §3.1 (2018) et ELM027 sur la page Microsoft Inventory to deliver du 2025-01-21 ; CMP028 conserve la justification et les limites de l’adaptation. Navigation et prochaine étape actualisées. État : 47 contributions utilisateur, 139 assertions, 27 contributions assistant, 38 corrections, 74 propositions ; 17 références marché, 41 éléments et 28 comparaisons. Les 36 capacités candidates, 68 questions et leur statut, ainsi que la couverture CAP 15/21 restent inchangés. Aucune liste, frontière ou hiérarchie validée.

Contrôle : identifiants et comptes vérifiés, 420 liens locaux/ancres valides ; catalogue CAP et cinq archives inchangés. Questions : 60 ouvertes et 8 résolues.

## 2026-09-10 — Trois cas d’achat et question de l’orchestration

U48 enregistré avant F140–F144. Trois cas du périmètre historique de Beaumanoir conservés avec leurs limites : fabrication complète fournisseur, produits finis sur catalogue et fabrication à façon. La formulation Planned Purchase Order précise le premier cas ; Q034 partiellement renseignée sans fermeture, FL17 et réalisation/source de CAP029 enrichies. C39 conserve les formulations antérieures. La définition, le résultat, le regroupement et le statut candidat de CAP029 sont préservés.

A28/P75 et connaissance/21-achats-et-orchestration.md proposent de distinguer aptitude durable, coordination métier et moyen générique d’orchestration. Les questions de composants confiés, consommations et engagements restent des pistes en Q069. Les vues du socle et des domaines sont actualisées ; la couche haute conserve son propre métier. Aucune plateforme, capacité nouvelle ou frontière n’est adoptée.

Marché : ELM002 réexaminé ; ELM042 BPMN 2.0.2 §7.2.1, ELM043 cours SAP de sous-traitance et ELM044 page Microsoft SCM du 2025-08-13 ajoutés après consultation. CMP029 conserve l’appui de méthode ; CMP030 rapproche partiellement CAP029 et contrôle les hypothèses de sous-traitance. La comparaison ne confond pas Planned Purchase Order local et document SAP. Bilan CAP : 16 rapprochements documentaires, 20 sans comparaison précise, zéro équivalence validée.

TER031–TER033 ajoutent orchestration, fabrication à façon et Planned Purchase Order comme définitions de travail. État : 48 contributions utilisateur, 144 assertions, 28 contributions assistant, 39 corrections, 75 propositions, 69 questions (61 ouvertes, 8 résolues), 36 capacités candidates ; 17 références marché, 44 éléments et 30 comparaisons ; 33 notions et 25 verbes. Navigation actualisée ; archives conservées sans modification.

Contrôle : identifiants et comptes vérifiés, 438 liens locaux/ancres valides ; 61 questions ouvertes et 8 résolues. Les cinq archives sont inchangées. Le catalogue CAP diffère uniquement par les deux compléments de réalisation et de source de CAP029 ; ses définitions et statuts restent inchangés.

## 2026-09-10 — Décision, détermination et orchestration dans les deux couches

U49 enregistré avant F145/F146 ; A29 et C40 intégrés. Laurent précise des moteurs dans le socle et dans la couche processus, cette dernière orientée Case Management. Une même solution reste possible sans choix arrêté. AGENTS.md conserve cette orientation et prévient l’assimilation orchestration/couche haute.

La vue des deux couches, son schéma, la note achats, P75, TER031 et CMP029 sont actualisés. A28 conserve sa formulation historique avec renvoi explicite à la rectification ; C40 reproduit la formulation remplacée. Les exemples de détermination, décision et coordination demeurent proposés ; aucun moteur unique, partage de persistance, produit ou nouvelle capacité décidé. Aucune nouvelle vérification externe : les sources de CMP029 ne prescrivent pas le placement local des moteurs.

État : 49 contributions utilisateur, 146 assertions, 29 contributions assistant, 40 corrections, 75 propositions. Les 69 questions, 36 capacités candidates, 17 références marché, 44 éléments, 30 comparaisons, 33 notions et 25 verbes sont conservés ; couverture CAP 16/20 inchangée.

Contrôle : séquences d’identifiants vérifiées et 442 liens locaux/ancres valides ; les registres CAP et questions ainsi que les cinq archives sont inchangés.

## 2026-09-10 — Portée distincte des deux modèles fonctionnels

U50 enregistré avant F147 ; A30 et C41 intégrés. Laurent réaffirme la capability map pour la couche transactionnelle et un autre modèle fonctionnel orienté processus pour la couche processus. AGENTS.md et les vues courantes rendent cette séparation explicite ; les usages de marché restent distincts de la portée locale dans CMP029. La présence de moteurs des deux côtés ne fusionne pas les modèles.

Les candidats historiques aux frontières restent conservés, sans reclassement ni validation automatique. Aucune nouvelle recherche externe, capacité, notation ou décision technique. État : 50 contributions utilisateur, 147 assertions, 30 contributions assistant, 41 corrections ; 75 propositions, 69 questions et 36 capacités candidates inchangées. Marché : 17 références, 44 éléments, 30 comparaisons ; couverture 16/20 conservée.

Contrôle : identifiants vérifiés, 444 liens locaux/ancres valides ; registres CAP et questions inchangés.

## 2026-09-10 — Options de découpage en domaines du socle

U51 enregistré avant F148 ; A31/P76 et connaissance/22-options-domaines-socle.md ajoutés. Trois approches comparées : référence principale filtrée, grandes familles commerce et domaines de problèmes cohérents. La troisième est recommandée par Codex pour la discussion, sans choix de Laurent. Dix périmètres étendent la première liste U47, avec les apports achats U48, les zones moins étayées et les frontières alternatives. Les sites et conditions commerciales restent visibles comme questions de délimitation.

ELM014/ELM025/ELM027 réexaminés sur le cours SAP, la figure retail IBM de 2005 et la vue Microsoft des scénarios affichant 2025-12-16. CMP031 sépare faits externes et adaptation locale ; aucune comparaison précise de domaine complet ni nouvelle capacité. Les vues antérieures et la navigation renvoient à cette exploration, sans reclassement CAP ni extension à la couche processus.

État : 51 contributions utilisateur, 148 assertions, 31 contributions assistant, 41 corrections, 76 propositions ; 69 questions et 36 capacités candidates inchangées. Marché : 17 références, 44 éléments et 31 comparaisons ; couverture CAP 16/20 conservée, aucune équivalence validée.

Contrôle : identifiants vérifiés, 456 liens locaux/ancres valides ; registres CAP et questions inchangés. Libellés canoniques contrôlés dans la nouvelle note.

## 2026-09-10 — Domaines problématiques et frontières éprouvées par les cas

U52 enregistré avant F149/F150 ; A32 et C42 ajoutés. Laurent distingue Source to Pay comme lecture processus et Order Promising comme approche problématique, donc domaine local, puis confirme la pertinence du travail des frontières avec les exemples. Cette reconnaissance ne fixe pas les frontières ni capacités de la promesse, et ne modifie pas son niveau natif SAP.

P76, les notes domaines, CMP031, AGENTS.md et la navigation sont actualisés : référence principale et grandes familles sont des modalités d’appui ou de présentation, sans mettre en concurrence la définition du domaine déjà guidée par les problèmes cohérents. La liste complète et les regroupements précis restent proposés. Relecture indépendante ciblée concordante sur la portée de l’apport ; aucune nouvelle recherche externe.

État : 52 contributions utilisateur, 150 assertions, 32 contributions assistant, 42 corrections ; 76 propositions, 69 questions, 36 capacités candidates, 17 références marché, 44 éléments et 31 comparaisons inchangés. Aucun candidat CAP modifié ni équivalence validée.

Contrôle : identifiants vérifiés et 458 liens locaux/ancres valides ; capacités et questions inchangées.

## 2026-09-10 — Cœur de Supply, parcours OMS et intelligence logistique

U53–U57 enregistrés au fil de l’échange avant F151–F157 ; A33/P77 et C43 intégrés. U53 éprouve le réassort intra/inter-sociétés. U54/U55 situent les parcours commerciaux dans l’OMS, défini par Laurent comme Case Management préimplémenté de vente au-dessus du transactionnel Supply. U56 définit la Supply comme contrôle, orchestration et optimisation de la logistique ; U57 lui donne aussi une intelligence de backoffice : rééquilibrage, prévision et impondérables.

La note connaissance/23-reassort-transferts-et-promesse.md conserve les cas, distinctions et sources SAP. ELM045–ELM047 examinent transferts, promesse de ventes/transferts et retours ; ELM014 reconsulté, CMP032 ajouté. Accès Help sans texte et leçon BKP 404 signalés ; cours primaires alternatifs effectivement lus. Le périmètre commercial/comptable n’est pas réduit à une facture ; finance reste une interface et C-Log autonome. Les sources ne valident pas un domaine Supply unique ni l’équivalence avec Order Promising.

C43 corrige la comparaison de mailles entre achat et réassort ; les vues antérieures, AGENTS.md et la navigation sont mises en cohérence. TER034/TER035 conservent les définitions locales explicites OMS/Supply. Les candidats historiques ne sont pas reclassés ; prévision opérationnelle à préciser sans import automatique de la planification de saison. Relecture indépendante ciblée sur les frontières et l’effet de U54.

État : 57 contributions utilisateur, 157 assertions, 33 contributions assistant, 43 corrections, 77 propositions ; 69 questions et 36 capacités candidates inchangées. Marché : 17 références, 47 éléments et 32 comparaisons ; 35 notions et 25 verbes. Couverture CAP 16/20 conservée, zéro équivalence validée.

## 2026-09-10 — Logistique hors développement FLOW, en adhérence

U58 enregistré avant F158 ; A34/C44 explicitent la différence entre modèle fonctionnel étudié et périmètre de développement du Programme FLOW. La logistique est hors réalisation de la plateforme et reste en adhérence. Rééquilibrage, prévision et impondérables ne deviennent pas des développements FLOW par leur simple présence dans l’analyse ; aucune exclusion globale de toute Supply n’est déduite.

AGENTS.md, README, note 23, vues des deux couches et du socle, options de domaines, TER035, P77 et CMP032 sont précisés. Les axes de description des contrats restent proposés ; les responsabilités installées et les questions Q040–Q044 sont conservées. Relecture indépendante ciblée concordante. Aucune nouvelle recherche externe ni capacité reclassée.

État : 58 contributions utilisateur, 158 assertions, 34 contributions assistant, 44 corrections, 77 propositions ; 69 questions et 36 capacités candidates. Marché : 17 références, 47 éléments et 32 comparaisons ; 35 notions et 25 verbes. Couverture CAP 16/20 inchangée, zéro équivalence validée.

Contrôle commun U53–U58 : séquences d’identifiants et comptes vérifiés, 488 liens locaux/ancres valides. Registres CAP et questions ainsi que les cinq archives inchangés ; libellés canoniques contrôlés dans la note 23.

## 2026-09-10 — Granularité SAP et autres modèles orientés domaines

U59 enregistré avant F159 ; A35/P78 et CMP033 ajoutés. L’intérêt de Laurent pour la maille SAP est conservé comme appréciation exploratoire. Codex recommande les Business Areas documentées comme première grille d’épreuve des domaines locaux, sans adoption du catalogue principal ni équivalence de niveaux. Le document existant marche/premier-niveau-regroupement-capacites.md reçoit le complément, lié aux options de domaines et à la navigation.

MKT18 BIAN et MKT19 TM Forum ajoutés ; ELM048–ELM051 distinguent partitions de services, fonctions SI, blocs d’architecture et capacités. Recherche primaire ciblée avec contribution indépendante ; guide BIAN 2020 distingué de la version 14.0 annoncée, présentations TM Forum lues mais documents membres non consultés. SAP et IBM reconsultés. Les nouvelles ouvertures Guild échouent ; preuves historiques et extraits indexés sont qualifiés séparément. Aucun catalogue retail détaillé acquis.

État : 59 contributions utilisateur, 159 assertions, 35 contributions assistant, 44 corrections, 78 propositions ; 69 questions et 36 capacités candidates conservées. Marché : 19 références, 51 éléments et 33 comparaisons ; glossaire 35 notions et 25 verbes inchangé. Couverture CAP 16/20, zéro équivalence validée. La logistique reste hors développement FLOW, en adhérence.

Contrôle U59 : séquences d’identifiants et comptes vérifiés ; 503 liens locaux/ancres valides. Registres CAP et questions inchangés ; libellés canoniques contrôlés dans le nouveau complément.

## 2026-09-10 — Approfondissement BIZBOK et priorités des références

U60 enregistré avant F160/F161 ; A36/P79 et C45/CMP034 ajoutés. Laurent juge IBM trop ancien, réserve BIAN à une lecture éloignée de la capacité et maintient l’intérêt de TM Forum ; BIZBOK est approfondi. AGENTS.md, P78 et les vues courantes conservent ces priorités sans supprimer les preuves historiques.

La nouvelle note marche/bizbok-capacites-et-domaines.md distingue domaine problématique, objet central, aptitude et réalisation. Introduction et glossaire BIZBOK 15.0 ©2026 lus sur le CDN officiel après échecs des liens directs ; Metamodel Guide v3.0 de septembre 2024 consulté par passages ; atelier 2019 relu. ELM052–ELM055 séparent ces preuves. Capture de la page 19 du métamodèle en échec, aucune conclusion nouvelle tirée de sa figure. Guide intégral, §2.2 et téléchargements membres non consultés.

Vérification parallèle des catalogues : Common Reference Model proposé, version non affichée ; Companion Guide v3.0 identifié séparément. Équipe Retail/Wholesale identifiée dans l’index, ouverture directe 403 ; livraison d’un modèle, version et contenu non établis. L’annonce historique v7.0 ne suffit pas à établir la version distribuée. Les registres, catalogue et navigation sont actualisés ; aucun accès membre ou achat effectué.

État : 60 contributions utilisateur, 161 assertions, 36 contributions assistant, 45 corrections, 79 propositions ; 69 questions et 36 capacités candidates conservées. Marché : 19 références, 55 éléments et 34 comparaisons ; 35 notions et 25 verbes inchangés. Couverture CAP 16/20 conservée comme avancement documentaire incluant des preuves historiques ; zéro équivalence validée. Aucun candidat renommé ni domaine adopté.

Contrôle U60 : identifiants et comptes vérifiés ; 520 liens locaux/ancres valides. Registres CAP et questions ainsi que les cinq archives inchangés ; libellés canoniques contrôlés dans la note BIZBOK.

## 2026-09-10 — Objets, faits et documents dans les deux modèles (U61/U62)

U61/U62 enregistrés avant F162–F164 ; A37/A38, P80 et C46/C47 intégrés. Laurent distingue objets métier rapprochés d’aggregate roots, faits de gestion associés à des documents représentant des états ou des objets non modifiables produits/captés. U62 précise les objets dans les deux couches, avec Demande de réassort comme exemple du modèle processus orienté Case Management. Le besoin présenté au socle et le suivi du cas sont distingués sans objet Demande universel adopté.

La note connaissance/24-capacites-objets-et-faits.md propose de faire émerger le sens de ces éléments avec les capacités et les cas, dans un modèle métier lié. Les exigences métier sont distinguées de leur réalisation et affinées par itérations avec la conception. L’exemple de promesse et les champs de description restent proposés ; aucune fiche CAP décomposée. AGENTS.md et les vues 15/16/19 sont alignés ; quatre notions ajoutées au glossaire. C46 corrige le statut global des définitions ; C47 précise les objets des deux modèles, après relecture indépendante.

ELM056–ELM061/CMP035 comparent SAP Business Data Catalog et objets de solution, relations capacité/information/états/résultats de la Guild, SID et exemples de notifications/documents. Recherches SAP et TM Forum menées avec contributions indépendantes ; BIZBOK et référence DDD vérifiés de manière ciblée. Guide BIZBOK complet et SID détaillé non consultés ; SAP Help examiné via extraits indexés ; TMF622 ©2019 et schéma Document avec repère 2020 explicitement historiques. L’analogie aggregate root est précisée sans concevoir d’agrégats ni imposer Event Sourcing. Les références ne prouvent aucune configuration Beaumanoir.

État : 62 contributions utilisateur, 164 assertions, 38 contributions assistant, 47 corrections, 80 propositions ; 69 questions et 36 capacités candidates conservées. Marché : 19 références, 61 éléments et 35 comparaisons ; 39 notions et 25 verbes. Couverture CAP 16 rapprochements documentaires /20 sans comparaison précise, zéro équivalence validée. Modèles distincts et logistique hors développement FLOW, en adhérence, conservés.

Contrôle U61/U62 : identifiants et comptes vérifiés ; 559 liens locaux/ancres valides. Registres CAP et questions ainsi que les cinq archives inchangés, vérifiés par empreintes. Libellés canoniques contrôlés dans la nouvelle note ; les trois remarques de relecture sur les objets des deux couches sont intégrées.

## 2026-09-10 — Première carte cœur et contrôle par les récits (U63/U64)

U63/U64 enregistrés avant F165/F166 ; A39/P81 et CMP036 ajoutés. Laurent demande une estimation domaines/capacités, puis précise l’épreuve par les récits du périmètre historique de Beaumanoir et de Boardriders et le signalement des capacités plausibles manquantes. AGENTS.md conserve cette méthode ; les anciens points d’entrée renvoient à P81 sans remplacer leur provenance.

La note connaissance/25-domaines-coeur-et-epreuve-recits.md propose dix domaines, 34 formulations d’aptitudes avec résultats et Finalité, objets utiles, sources, frontières et non-comparés. Vingt cas ou mentions sont qualifiés ; les besoins Boardriders restent distincts d’un fonctionnement installé. Le raccordement conceptuel ne démontre pas une couverture exhaustive. Une matrice conserve le lien avec les 36 CAP sans les renommer ni modifier leurs fiches. Les compléments sur futur, reste à satisfaire, capacité de service, écarts, matières confiées, unités et droits après fourniture sont présentés avec leurs niveaux de preuve.

Relecture indépendante des récits et de la carte ; réexamen primaire ciblé SAP/Microsoft par contribution indépendante. ELM062 complète notamment protection ventes/transferts et BOP ; les sources, dates et limites sont consignées. Le contenu actuel surtout consacré à l’activation de l’ancienne leçon S5 est distingué de la lecture antérieure ; sources directes Basic ATP et BOP retenues pour la proposition courante. Les erreurs de rattachement documentaire ARTS/produits repérées à la relecture de la nouvelle note ont été corrigées avant livraison.

État : 64 contributions utilisateur, 166 assertions, 39 contributions assistant, 47 corrections, 81 propositions ; 69 questions et 36 capacités candidates historiques conservées. Marché : 19 références, 62 éléments et 36 comparaisons ; 39 notions et 25 verbes. Couverture documentaire CAP 16/20 inchangée, sans assimilation aux 34 formulations P81 ni à la couverture de l’entreprise. Aucun domaine ni attribution de développement validés ; logistique hors développement FLOW et en adhérence.

Contrôle U63/U64 : identifiants et comptes vérifiés ; 576 liens locaux/ancres contrôlés, une ancre corrigée puis revérifiée. P81 contient dix domaines, 34 repères de capacités uniques et vingt cas ou mentions ; les 36 CAP sont toutes reliées ou qualifiées en frontière. Registres CAP et questions ainsi que les cinq archives inchangés, vérifiés par empreintes. Libellés canoniques contrôlés dans la nouvelle note.

## 2026-09-11 — Noms de marché proches des dix domaines (U65)

U65 enregistré avant F167 ; A40, ELM063–ELM066 et CMP037 ajoutés. La note marche/correspondances-domaines-coeur.md rapproche les dix domaines P81 des noms SAP, Microsoft et TM Forum, avec les types et niveaux explicites. Les quelques noms publics Guild proviennent d’un atelier de mars 2019, distinct du guide actuel et d’un catalogue retail complet. Les sources et attributions de figures sont qualifiées.

Recherches primaires SAP et TM Forum/Guild réalisées avec contributions indépendantes ; Microsoft examiné directement. SAP RBA reste distinct des cours de produit ; Microsoft distingue processus, modules et référentiels ; TM Forum distingue composants et API. Limites de Service Qualification, Product Inventory et Pricing explicitées. Index et lecture directe sont séparés ; aucune acquisition de contenu membre. Les appuis nouveaux sur produits/unités et capacités de service enrichissent le vocabulaire sans transformer les noms en équivalences de capacités.

État : 65 contributions utilisateur, 167 assertions, 40 contributions assistant, 47 corrections, 81 propositions ; 69 questions et 36 fiches CAP conservées. Marché : 19 références, 66 éléments et 37 comparaisons ; 39 notions et 25 verbes. P81 conserve dix domaines et 34 formulations ; couverture historique CAP 16/20 inchangée. Aucun domaine, intitulé local ou rattachement validé ou remplacé.

Contrôle U65 : identifiants et comptes des douze registres vérifiés ; 593 liens locaux/ancres valides. Dix domaines présents dans chacun des tableaux SAP/Microsoft et TM Forum. Fiches CAP et questions inchangées par empreintes ; libellés canoniques contrôlés dans la nouvelle note.

## 2026-09-11 — Nomenclature anglaise et aptitude métier distincte de sa réalisation (U66/U67)

U66/U67 enregistrés avant F168–F171 ; A41, C48/C49, ELM067/CMP038 ajoutés. Laurent demande les noms anglais avec réemploi du marché, notamment Inventory Management, puis distingue les aptitudes Supply Protection / Supply Assignment du mécanisme Allocation Run. C49 corrige la réponse qui avait trop insisté sur leur présentation dans la documentation produit ; le rang natif RBA non établi ne nie pas leur nature métier.

P81 passe de la version 0.1 (34 formulations) à la version 0.2 (35) : dix domaines et les 34 libellés précédents en anglais, avec anciennes désignations conservées en C48, définitions antérieures conservées et D02.e Supply Assignment explicite. D02.b reprend Supply Protection ; rattachement et frontière avec Reservation restent proposés, y compris la possibilité de deux vues d’une même capacité. Matrice Boardriders et raccordement CAP010 actualisés ; les 36 fiches CAP ne sont pas modifiées.

Recherche primaire SAP et relecture indépendantes ; ELM067 distingue texte consulté et extrait indexé de la fiche SUPPLY_ASSIGNMENT_01. La borne de disponibilité 1709 ne date pas toutes les fonctionnalités ; ni Business Area, ni Business Capability RBA, ni Solution Capability RSA ne sont attribuées aux deux noms sans preuve. Glossaire, règles AGENTS, références, correspondances et navigation alignés. Les anciennes ancres des dix domaines sont conservées.

État : 67 contributions utilisateur, 171 assertions, 41 contributions assistant, 49 corrections, 81 propositions ; 69 questions et 36 fiches CAP historiques. Marché : 19 références, 67 éléments et 38 comparaisons ; 39 notions et 25 verbes. Couverture CAP 16/20 inchangée. P81 comporte dix domaines, 35 formulations et vingt cas ; noms, frontières et définition détaillée restent à éprouver dans les limites des choix explicitement exprimés par Laurent.

Contrôle U66/U67 : identifiants et comptes des douze registres vérifiés ; 615 liens locaux/ancres contrôlés. Dix domaines, 35 repères de capacités uniques, vingt cas et raccordement aux 36 CAP vérifiés. Registres CAP et questions ainsi que les cinq archives inchangés par empreintes. Les trois points de relecture indépendante (liens de Supply Assignment, frontière avec Reservation et absence de mécanisme unique imposé) sont intégrés.

## 2026-09-11 — Revue de D01 Inventory Management (U68)

U68 enregistré avant F172 ; A42 et ELM068/CMP039 ajoutés. Revue domaine par domaine demandée par Laurent, consignée dans AGENTS.md. D01 reçoit une Finalité proposée et un tableau des correspondances de ses quatre aptitudes, dans la carte courante plutôt que dans une synthèse concurrente. Les quatre libellés et définitions sont conservés ; la distinction positions/vue consolidée reste à éprouver.

Sources primaires SAP RBA et produit, Microsoft Inventory Management/Inventory Visibility/Inventory journals et notice TMF687 relues. Passages et versions qualifiés en ELM068 ; ARTS et Guild repris des preuves antérieures sans nouvelle consultation. Stock en transit distinct d’approvisionnement attendu ; portée limitée du Transfer journal Microsoft explicitée dans la preuve. Les fonctions de réservation/ATP/valeur présentes dans les produits n’élargissent pas D01. Logistique hors développement FLOW et en adhérence maintenue.

État : 68 contributions utilisateur, 172 assertions, 42 contributions assistant ; 49 corrections, 81 propositions, 69 questions et 36 CAP conservées. Marché : 19 références, 68 éléments, 39 comparaisons. P81 demeure à dix domaines et 35 formulations ; aucune équivalence ni nouvelle capacité validées.

Contrôle U68 : identifiants des cinq registres enrichis, dix domaines et 35 repères de capacités vérifiés ; 621 liens locaux/ancres contrôlés. Registres CAP et questions inchangés par empreintes.

## 2026-09-11 — Clarification des quatre aptitudes de D01 (U69)

U69 enregistré avant F173 ; A43/C50 ajoutés. Laurent propose une reformulation interrogative : structure, mouvements, visibilité, golden data. Cette lecture n’est pas enregistrée comme validation. La carte et le glossaire expliquent les formulations initiales, conservent les identifiants et signalent le chevauchement a/b, en complément du point a/c déjà ouvert.

Les exemples 100/97 et sortie de 5 sont fictifs. Écart de comptage, désaccord entre sources, correction d’une copie et ajustement métier sont distingués, avec autorité et justification ; aucune centralisation ou architecture datahub retenue. Stock logique/virtuel demeure à qualifier en Q066 ; vue de positions distincte de pool protégé et disponibilité. Les comparaisons de CMP039 reçoivent une précision de portée, sans nouvelle recherche externe ni équivalence.

État : 69 contributions utilisateur, 173 assertions, 43 contributions assistant, 50 corrections ; P81, 35 formulations dans dix domaines, 36 fiches CAP et 69 questions conservés. Marché inchangé : 19 références, 68 éléments, 39 comparaisons. Aucun nouveau candidat ni arbitrage de domaine.

## 2026-09-11 — Frontière entre Inventory Management et protection (U70)

U70 enregistré avant F174 ; A44 ajouté. La question ouvre le rattachement de Supply Protection à un Inventory Management plus large. La carte explicite que D02.b est un choix provisoire ; définir les règles de protection est métier, configurer leur moteur est un moyen. Exemple fictif 100 unités dont 40 protégées, sans variation physique déduite.

Aucun déplacement de capacité, fusion de domaines ou arbitrage imputé à Laurent. U69 reste traité par A43/C50 ; les clarifications sont conservées dans la même section D01. Pas de nouvelle recherche externe. État : 70 contributions utilisateur, 174 assertions, 44 contributions assistant, 50 corrections ; P81, CAP, questions et comptes marché inchangés.

Contrôle U69/U70 : identifiants des quatre registres enrichis et liens locaux/ancres contrôlés ; dix domaines et 35 repères uniques de capacités conservés (les quatre repères D01 sont repris dans le tableau explicatif). Registres CAP et questions inchangés par empreintes.

## 2026-09-11 — Explication immédiate de D01.a (U71)

U71/F175/A45 et complément C50 consignent le manque de clarté confirmé par Laurent. La carte donne immédiatement après les quatre capacités une explication de la position de stock et un exemple fictif. La distinction a/b est à réexaminer ; aucune fusion, nouveau libellé ou définition de protection validés. État : 71 contributions utilisateur, 175 assertions, 45 contributions assistant ; 50 corrections et autres comptes inchangés.

## 2026-09-11 — Sens métier de l’inventaire en D01.d (U72)

U72/F176/A46, complément C50 et précision CMP039 ajoutés. D01.d est expliqué comme constat des quantités, comparaison et régularisation des écarts justifiés. L’exemple 100/97 reste fictif ; le comptage est un constat à qualifier. Physical Inventory est suggéré comme nom plus parlant sur la base des sources déjà examinées ; aucun remplacement automatique ni recherche externe nouvelle.

État : 72 contributions utilisateur, 176 assertions, 46 contributions assistant ; 50 corrections et autres comptes inchangés. Les aptitudes et leur maille restent en discussion ; aucun développement logistique ajouté au périmètre FLOW.

## 2026-09-11 — Restitution complète et consolidation de D01 (U73)

U73/F177/A47 enregistrés. La section D01 est consolidée : une table des quatre formulations historiques, une explication métier, une table marché et les frontières ouvertes. Les clarifications U69–U72 ne restent plus dispersées entre plusieurs tables répétées ; leur provenance demeure en C48/C50 et A42–A46. Physical Inventory est présenté comme nom proposé pour D01.d, sans renommage validé ; les quatre définitions antérieures sont conservées.

Reprise des sources déjà examinées, sans nouvelle recherche externe. Pas de fusion a/b ni de transfert de Supply Protection depuis D02 ; pas de nouveau développement logistique ou équivalence validée. État : 73 contributions utilisateur, 177 assertions, 47 contributions assistant ; 50 corrections et autres comptes inchangés.

## 2026-09-11 — Supply Protection dans Inventory Management (U74)

U74/F178/A48/C51 enregistrés. P81 version 0.3 applique l’orientation de Laurent : Supply Protection rejoint D01. Sa définition et son repère historique D02.b sont conservés ; son emplacement, et non l’identité de l’aptitude, change. D01 compte cinq aptitudes et D02 quatre, total 35 inchangé. Finalité et problème du domaine D01 élargis ; cas, raccordements CAP et frontières actualisés. Aucun déplacement automatique des autres aptitudes de D02.

ELM017/ELM028 relus, CMP040 ajouté : protection SAP et allocation Microsoft rapprochées sur leur contenu, sans rang RBA ni équivalence complète déduits. Règles AGENTS, glossaire, proposition P81, correspondances et navigation actualisés. Définitions détaillées, maille a/b et nom proposé Physical Inventory restent à éprouver. Aucun développement logistique, centralisation de données ou calcul de saison adopté.

État : 74 contributions utilisateur, 178 assertions, 48 contributions assistant, 51 corrections ; 81 propositions, 69 questions et 36 CAP historiques conservées. Marché : 19 références, 68 éléments et 40 comparaisons ; couverture CAP 16/20 inchangée.

Contrôle U73/U74 : identifiants des dix registres contrôlés ; 637 liens locaux/ancres valides. Dix domaines et 35 formulations uniques, dont cinq dans D01 et quatre dans D02. Supply Protection est présente une seule fois dans les tables de capacités ; son repère est préservé. Registres CAP et questions inchangés par empreintes.

## 2026-09-11 — Réservation dans Inventory Management et affectation dans Order Promising (U75)

U75/F179/A49/C52 enregistrés avant l’évolution P81 version 0.4. Réservation et Supply Assignment déplacées vers D01 et D03 selon Laurent, avec repères D02.c/D02.e conservés. Définition de réservation clarifiée par engagement de quantité ; ancienne formulation par affectation conservée en C52. Six aptitudes dans D01, deux dans D02 en réexamen, quatre dans D03 ; 35 au total. Les autres domaines restent candidats, sans justifier D02 par son seul identifiant.

La disponibilité est expliquée comme résultat pour un usage et une date, avec un exemple fictif dont les restrictions sont disjointes et explicites. Stock physique, vues, pools et projections restent distincts ; leur étude dans un même domaine est proposée, sans taxonomie du virtuel validée ni clôture de Q066. Rapprochements et sources actualisés en ELM069/CMP041 après lecture Microsoft/SAP ; autres comparaisons reprises des preuves précédentes.

Carte, cas, raccordement CAP010, glossaire, règles et navigation actualisés. Pas de fusion a/b ni de renommage définitif Physical Inventory. Pas de configuration locale ou choix de moteurs établi. État : 75 contributions utilisateur, 179 assertions, 49 contributions assistant, 52 corrections ; 81 propositions, 69 questions et 36 CAP historiques conservées. Marché : 19 références, 69 éléments, 41 comparaisons ; couverture CAP 16/20 inchangée.

## 2026-09-11 — Distinction physique/logique/virtuel et hypothèse de frontière (U76/U77)

U76/U77 enregistrés avant F180/F181 ; A50/A51/C53 ajoutés. La mise en forme du tableau U76 est normalisée et signalée. Les trois sens explicites remplacent la terminologie assistant trop large : existence physique, états métier logiques, quantité virtuelle calculée. TER040–TER042 ajoutés ; TER021 conserve la notion de pool, avec ancien synonyme et définition en C53. Q066 reçoit une réponse partielle sourcée ; statut ouvert conservé pour les règles, objets et autorités.

Les nombres 100, 60/20/10/5/5 et 60+30−15=75 sont ceux de Laurent, illustratifs. Les conditions de partition, horizon et absence de double déduction sont des précisions d’analyse, sans règle de déploiement déduite. Le partage U77 est conservé comme hypothèse : projection de promesse en D03, positions/états en D01 ; disponible courant réservable possiblement en D01. Aucun nouveau domaine, fusion, rattachement ferme ou recherche externe.

Carte, glossaire, ancienne exploration, P81, CMP041, règles et navigation alignés. État : 77 contributions utilisateur, 181 assertions, 51 contributions assistant, 53 corrections ; 42 notions et 25 verbes. P81 reste à dix domaines provisoires et 35 aptitudes ; 69 questions, 36 CAP, 19 références, 69 éléments et 41 comparaisons. Le registre des questions change pour la réponse partielle Q066 ; fiches CAP conservées.

## 2026-09-11 — Réexamen de la réservation avec SAP et Microsoft (U78)

U78/F182/A52/C54 enregistrés ; ELM070–ELM072/CMP042 ajoutés. SAP Learning et Microsoft Learn ouverts et lus ; SAP Help aATP/MRP via extraits indexés détaillés, ouvertures sans texte exploitable. Versions et limites conservées. La réservation Microsoft peut porter sur du présent ou du commandé non reçu, et SAP nomme des quantités réservées par Supply Assignment. Le contrôle SAP MM est qualifié selon avertissement/erreur configurés, sans verrou absolu présumé.

La note comparative existante reçoit le détail ; carte et glossaire renvoient au réexamen. La frontière U75 est maintenue comme option affichée, avec hésitation U78 explicitée, sans fusion, déplacement ou cycle indépendant imposés. Aucune configuration Beaumanoir ni extension logistique FLOW déduites. État : 78 contributions utilisateur, 182 assertions, 52 contributions assistant, 54 corrections ; 42 notions/25 verbes, 81 propositions, 69 questions, 36 CAP. Marché : 19 références, 72 éléments, 42 comparaisons. P81 dix domaines provisoires et 35 aptitudes, couverture CAP 16/20 conservée.

Contrôle U75–U78 : identifiants et comptes des douze registres vérifiés ; 652 liens locaux/ancres contrôlés. P81 contient dix domaines provisoires, 35 aptitudes uniques (D01 six, D02 deux, D03 quatre), vingt cas et un raccordement aux 36 CAP. Les 36 fiches CAP et les cinq archives sont inchangées par empreintes ; Q066 contient la réponse partielle U76 et reste ouverte.

## 2026-09-11 — Potentiel contractuel et représentation des stocks futurs (U79)

U79 enregistré avant F183 et A53 ; texte conservé avec normalisation de mise en forme signalée. La carte P81 est enrichie par les situations allant du reliquat contractuel aux achats planifiés et à la mise en stock. L’analyse distingue potentiel, entrée attendue, présence physique et résultat virtuel calculé, sans modifier le sens U76 ni imposer une partition entre domaines. TER043 ajouté, TER042 précisé ; son sens et son exemple antérieurs sont conservés. Q066 reçoit un complément sourcé et reste ouverte.

ELM073/ELM074 et CMP043 ajoutés : textes Microsoft consultés, extrait SAP indexé avec limite d’accès documentée. Continuité contrat/plan/commande/réception et absence de double compte proposées ; putaway identifié comme rangement. Logistique toujours en adhérence ; aucune preuve de configuration locale, capacité ou frontière validée nouvelle. P81 conserve dix domaines et 35 aptitudes ; registre CAP et archives non modifiés. État : U79, F183, A53, C54, P81, Q69, CAP36 ; TER43/VER25 ; MKT19, ELM74, CMP43. Navigation actualisée.

## 2026-09-11 — Stock futur dans Inventory Management et Order Promising (U80)

U80 enregistré avant F184/A54. Laurent confirme la présence du stock futur dans les deux domaines et une date de promesse qui dépend aussi de l’amont. Carte, glossaire, Q066, P81, CMP043, navigation et AGENTS alignés. La lecture connaissance des ressources / décision de promesse est proposée ; les autorités détaillées D01/D04/D07 ne sont pas figées. L’analyse précédente U79 « D01 peut en donner une visibilité » est précisée par cette orientation explicite, sans modifier les formulations des capacités. Dates de réception, disponibilité pour usage et livraison promise distinguées avec exemple fictif. État : U80/F184/A54, autres comptes U79 conservés ; dix domaines, 35 aptitudes, 36 CAP historiques.

Contrôle U79/U80 : identifiants uniques et séquentiels des registres modifiés ; 668 liens locaux et ancres valides. Dix domaines et 35 aptitudes uniques conservés ; empreinte des 36 fiches CAP inchangée. Q066 reste ouverte avec les compléments U79/U80.

## 2026-09-11 — Stock logique explicite dans Inventory Management (U81)

U81 enregistré avant F185/A55. C55 conserve les quatre définitions antérieures et les anciennes précisions U77 ; D01.a/b/c explicitent physique, logique et connaissance du futur, D03.a le calcul du stock virtuel et son application à la faisabilité. La présentation précédente masquait le logique sous états ; Physical Inventory reste le seul rapprochement physique, pas la définition du domaine. Finalité D01, carte, glossaire, P81, Q066, CMP043, AGENTS et navigation alignés. Pas de nouvelle recherche : correspondances actualisées comme partielles, sans équivalence native supplémentaire établie.

État : U81/F185/A55/C55 ; P81 version 0.4 conserve dix domaines, 35 aptitudes et leurs repères ; Q066 ouverte, 69 questions et 36 CAP historiques. TER43/VER25, MKT19/ELM74/CMP43 inchangés. Aucune formule universelle, déplacement de capacité ni choix de réalisation décidé.

Contrôle U81 : identifiants U/F/A/C séquentiels et uniques ; 671 liens locaux et ancres valides. Dix domaines et 35 aptitudes uniques, empreinte des 36 fiches CAP inchangée ; Q066 ouverte et complétée.

## 2026-09-11 — Revue des noms de quantités et de comptage du stock (U82)

U82 enregistré avant F186/A56/C56. Sources SAP Learning, glossaire SAP historique et Microsoft Learn lues ; ELM075/ELM076/CMP044 ajoutés avec niveaux et limites. Managing Stocks by Quantity, On-hand inventory, Maintain inventory levels, Count inventory, Counting et stock-taking distingués. Propositions locales Manage inventory quantities et Count and reconcile inventory, Stocktaking comme forme courte ; Inventory accuracy comme Finalité. Physical Inventory reste un nom SAP attesté mais sa proposition locale est remise en discussion, comme Establish inventory positions.

Carte, glossaire, P81, AGENTS et navigation actualisés. Aucun renommage définitif, fusion, formule, élargissement ou nouvelle capacité. État : U82/F186/A56/C56, P81 version 0.4 dix domaines/35 aptitudes ; Q69 et CAP36 inchangés. MKT19/ELM76/CMP44, TER43/VER25. La preuve externe n’atteste pas de configuration locale ; comptage logistique en adhérence FLOW.

## 2026-09-11 — Proposition de cinq capacités Inventory Management (U83)

U83 enregistré avant F187/A57 ; P82 et CMP045 créés. Proposition de réunion D01.a/b sous Inventory Tracking, puis Inventory Visibility, Stocktaking, Supply Protection et Inventory Reservation. Titres courts avec définitions d’aptitudes actives ; physique/logique/futur, faits et finalités conservés. La réservation explicite ajustement/libération dans son cycle sans absorber automatiquement D02.d. Sources U82 et preuves antérieures réutilisées avec limites.

Vue de discussion ajoutée dans la carte et reliée à P82, glossaire et navigation. Aucun renommage ou fusion adopté : P81 garde dix domaines et 35 aptitudes, dont six D01 ; références historiques et CAP36 intactes. État : U83/F187/A57/C56/P82 ; Q69, TER43/VER25 ; MKT19/ELM76/CMP45.

Contrôle U82/U83 : identifiants des registres modifiés uniques et séquentiels ; 690 liens locaux et ancres valides. P81 conserve dix domaines et 35 aptitudes uniques ; P82 reste une alternative de cinq capacités D01, clairement identifiée. Empreinte des 36 fiches CAP inchangée.

## 2026-09-11 — Reservation retenu et Counting proposé (U84)

U84 enregistré avant F188/A58/C57. Reservation remplace le préfixé Inventory Reservation dans P82 et le titre long historique de D02.c dans la vue P81, sans modifier le repère ni la définition. Counting devient le nom proposé de la ligne de comptage P82, avec préférence de Laurent consignée ; Stocktaking conservé comme historique, rapprochement et corrections maintenus. Aucune fusion ou granularité considérée comme définitivement validée.

Carte, P82, glossaire, CMP045/ELM076, règles et comptes de navigation alignés. Microsoft Counting reconsulté ; graphies stocktaking/stock-taking qualifiées avec appui lexical indexé et source SAP déjà lue. Cambridge inaccessible, limite consignée. État U84/F188/A58/C57 ; P82, Q69, CAP36, MKT19/ELM76/CMP45 et TER43/VER25 inchangés. P81 reste à 35 aptitudes ; P82 propose cinq capacités D01.

Contrôle U84 : identifiants U/F/A/C séquentiels et uniques ; 690 liens locaux valides ; 35 aptitudes P81 et empreinte CAP conservées. Reservation présent et Counting qualifié comme proposé dans P82.

## 2026-09-11 — Stocktaking et indépendance des outils (U85)

U85 enregistré avant F189/A59. Stocktaking rouvert face à Counting dans P82 ; l’analyse distingue portée de l’inventaire et dénombrement, sans rendre Counting dépendant d’un outil. Définition de comptage, rapprochement et corrections conservée ; aucune validation définitive. Carte, P82, glossaire, CMP045, AGENTS et comptes de navigation alignés. Aucun nouveau fait externe ni recherche. État U85/F189/A59/C57 ; P82 et autres comptes inchangés.

Contrôle U85 : identifiants U/F/A séquentiels et uniques ; 35 aptitudes P81 conservées. Aucun lien ou repère de capacité ajouté, supprimé ou modifié ; vue P82 ouverte sur les deux noms.

## 2026-09-11 — Adoption de Stocktaking (U86)

Accord explicite U86 enregistré avant F190/A60/C58. Laurent adopte Stocktaking en un mot et Inventory accuracy comme Finalité dans le contexte de A59. Nom appliqué à D01.d et P82, définition explicitée par comptage, confrontation, qualification des écarts et corrections justifiées ; périmètre inchangé. Ancien Reconcile and correct inventory discrepancies et options Physical Inventory/Counting conservés en C58 et historiques. Carte, P82, glossaire, CMP045, AGENTS et navigation alignés. Les preuves externes existantes sont inchangées ; aucun catalogue natif ni déploiement local déduit.

État : U86/F190/A60/C58 ; P82, Q69, CAP36, TER43/VER25, MKT19/ELM76/CMP45. P81 conserve dix domaines et 35 aptitudes ; P82 conserve sa proposition de cinq capacités D01. La décision de nom ne ferme pas les frontières ni la fusion proposée D01.a/b.

Contrôle U86 : identifiants U/F/A/C séquentiels et uniques ; nom Stocktaking présent dans les deux vues, 35 aptitudes P81 et empreinte CAP conservées. Lien de navigation ajouté vérifié ; aucune ancre existante modifiée.

## 2026-09-11 — Audit d’Order Promising et proposition de style (U87/U88)

U87 enregistré avant F191 ; U88 confirme Order Promising avant F192. A61/P83 et audit daté produits. Examen des quatre capacités, distinction possible/confirmé/affecté et conditions de réexamen, cas de vente sur stock, futur et priorité Boardriders ; exemples de robustesse distingués des faits déclarés. Proposition Supply Feasibility, Confirmation, Supply Assignment, Promise Revision, sans nouveaux repères ou adoption. L’audit initial du résiduel D02 est conservé comme examen de frontière et non comme cible de la demande ; retrait de D02 seulement recommandé.

ELM077/CMP046 ajoutés après lecture SAP aATP et Microsoft Order promising/réservations ; versions et limites conservées. Carte, correspondances, P83, navigation et AGENTS mis à jour. Aucun choix de plateforme, équivalence complète ou configuration locale déduit. P81 garde dix domaines/35 aptitudes, P82 cinq capacités D01 proposées ; CAP36 et Q69 conservées. État U88/F192/A61/C58/P83 ; TER43/VER25, MKT19/ELM77/CMP46.

Contrôle U87/U88 : identifiants uniques et séquentiels des registres modifiés ; 708 liens locaux et ancres valides. Dix domaines et 35 aptitudes P81 conservés ; empreinte CAP36 inchangée. Audit et vue proposée identifient Order Promising comme cible confirmée U88.

## 2026-09-11 — Comparaison préalable d’Order Promising au marché (U89)

U89 enregistré avant F193/A62. Comparaison dédiée de P83 : noms, nature documentaire et contribution métier, nombres qualifiés et dix critères de couverture. Lecture visuelle des cinq feuilles de l’extrait SAP RBA ; approfondissement SAP aATP/SBC et Microsoft alternatives. Oracle Fusion GOP 26B ajouté comme MKT20, distinct du RRM ; ELM078–ELM081/CMP047. PDF Oracle Backlog non accessible, aucune preuve détaillée tirée de ce document.

Résultat : quatre critères explicites, quatre partiels et deux non décrits, sans adoption de dix capacités ni taux de couverture du marché. P83 reste proposée ; aucun nom ou périmètre de capacité modifié. Navigation, carte, audit et correspondances reliés à l’étude. État U89/F193/A62/C58/P83, MKT20/ELM81/CMP47 ; CAP36, Q69, TER43/VER25 conservés.

Contrôle U89 : identifiants uniques et séquentiels U/F/A/P/MKT/ELM/CMP ; 724 liens locaux et ancres contrôlés selon les conventions existantes. Dix domaines et 35 aptitudes P81 conservés ; empreinte du registre CAP36 inchangée. Comptages de navigation actualisés. Aucun fichier d’archive modifié.

## 2026-09-11 — Noms centrés sur la promesse et vocabulaire ATP (U90)

U90 enregistré avant F194/A63. Promise Verification et Promise Confirmation intégrés comme candidats dans la vue P83 ; appréciation favorable de Supply Assignment et Promise Revision consignée. C59 conserve les premiers noms et distingue contrôle d’allocation, vérification d’une possibilité et confirmation de l’engagement. Aucun objet unique ou ordre d’exécution imposé. Écarts U89 conservés.

APICS CPIM 2019, extrait officiel ASCM, vérifié pour Available-to-Promise : MKT21/ELM082/CMP048 et TER044. Référence historique, pas dictionnaire actuel ou formule cible adoptés. Carte, glossaire, propositions, étude, audit, correspondances et navigation actualisés ; P81 dix domaines/35 aptitudes et CAP36 conservés. État U90/F194/A63/C59/P83 ; MKT21/ELM82/CMP48 ; TER44/VER25, Q69.

## 2026-09-11 — Décisions et naissance de la promesse (U91/U92)

U91/U92 enregistrés avant F195/F196/A64. Promise Verification rejeté, remplacé par le candidat assistant Promise Formulation dans la vue P83 ; C60 conserve l’étape U90. Ajout exploratoire demandé des quatre aptitudes de décision issues des écarts marché, avec domaines propriétaires proposés et frontières explicites. Leur granularité et articulation avec les capacités existantes restent à éprouver ; aucune carte à huit capacités sœurs adoptée.

CMP049 actualise les correspondances à partir des preuves U89 ; pas de nouvelle recherche. AGENTS, glossaire, carte, proposition, étude, correspondances et navigation actualisés. Les références historiques et le diagnostic de couverture U89 restent datés. État U92/F196/A64/C60/P83, MKT21/ELM82/CMP49, TER44/VER25 ; P81 dix domaines/35 aptitudes historiques, CAP36 et Q69 conservés.

Contrôle U90–U92 : identifiants uniques et séquentiels ; 736 liens locaux et ancres contrôlés selon les conventions existantes. P81 dix domaines/35 aptitudes et empreinte CAP36 conservés. Promise Verification retiré de la table courante ; ajouts de décision présents avec statuts et propriétaires proposés.

## 2026-09-11 — Proposition de promesse et décision d’acheminement (U93)

U93 enregistré avant F197/F198/A65. C61 corrige le nom Promise Formulation et l’insuffisance du seul choix de source. Promise Proposal devient candidat courant de Laurent. Fulfillment Route Decision ajouté à l’exploration : chaîne de transport jusqu’à destination, D03 proposé pour le choix fondant la promesse, possibilités D06 et engagements D07 ; planification détaillée et autorités logistiques distinguées. Cinq aptitudes de décision explorées, sans nouveau niveau ni carte à neuf capacités sœurs validés.

ELM083/CMP050 après examen SAP Transportation Management et relecture Microsoft/Oracle ; MKT13 enrichi sans nouvelle référence. Carte, P83, glossaire, étude, correspondances et navigation actualisés. Statut historique de la grille U89 conservé. État U93/F198/A65/C61/P83 ; MKT21/ELM83/CMP50 ; CAP36, Q69, TER44/VER25 et dix domaines/35 aptitudes P81 historiques conservés.

Contrôle U93 : identifiants des registres modifiés uniques et séquentiels ; 741 liens locaux et ancres contrôlés selon les conventions existantes. Promise Proposal et Fulfillment Route Decision présents dans la vue courante. Dix domaines/35 aptitudes historiques et empreinte CAP36 conservés.

## 2026-09-11 — Distinction Microsoft ATP/CTP (U94)

U94 enregistré avant F199/A66. Explication approfondie dans l’étude Order Promising, avec distinction Supply Chain Management / Business Central, exemple local illustratif et lien proposé vers Promise Proposal / Supply Creation Decision. ATP comprend les réceptions futures ; CTP considère aussi les possibilités de fournir le manque. ELM084/CMP051 et TER045 ajoutés. C62 qualifie la divergence entre les pages Microsoft sur les variantes CTP ; aucun inventaire technique homogène prétendu.

MKT14 enrichi sans nouvelle référence. Navigation et carte reliées à l’analyse. Appréciation favorable de Laurent conservée sans adoption globale. État U94/F199/A66/C62/P83 ; MKT21/ELM84/CMP51, TER45/VER25, Q69 ; P81 dix domaines/35 aptitudes et CAP36 inchangés.

Contrôle U94 : identifiants uniques et séquentiels ; 745 liens locaux et ancres valides selon les conventions existantes ; P81 et empreinte CAP36 conservés.

## 2026-09-11 — Validation des capacités d’Order Promising et report CTP (U95)

U95 enregistré avant F200/F201/A67. Validation explicite des quatre capacités d’action et cinq capacités de décision appliquée à P83 et à la vue unique D03. P81 version 0.5 : dix domaines, 40 capacités recensées, dont neuf validées dans Order Promising. Nouveaux repères D03.d–h pour les décisions, après contrôle de disponibilité ; D03.a/b/c et le repère historique D02.e conservés. C63 garde les quatre anciennes lignes et la portée de l’accord. Le registre CAP36 n’est pas promu par équivalence.

ATP conservé dans la promesse ; CTP déjà présent au glossaire maintenu, placement différé. La piste analytics/planification/protection reste hypothétique. Supply Creation Decision conservée parmi les décisions validées. La demande de glossaire est interprétée contextuellement comme maintien des deux termes, avec verbatim inchangé en U95. CMP052 actualise les correspondances sans nouvelle recherche externe ; validation métier distincte de l’équivalence marché. Carte, P81/P83, glossaire, audit, étude, correspondances, navigation et AGENTS actualisés. État U95/F201/A67/C63/P83 ; MKT21/ELM84/CMP52 ; TER45/VER25, Q69 et CAP36 inchangés.

Contrôle U95 : identifiants uniques et séquentiels ; dix domaines et 40 repères uniques P81, dont neuf en D03. 742 liens locaux et ancres contrôlés selon les conventions existantes, anciennes ancres U87/U88 et U91 conservées. Empreinte CAP36 inchangée ; ATP/CTP toujours au glossaire et CTP différé.

## 2026-09-11 — Première revue de Commercial Commitments (U96)

U96 enregistré avant F202/A68 ; poursuite D04 selon l’ordre courant. P84 propose quatre noms courts pour les aptitudes historiques, finalité et espace problématique, épreuve des trois achats U48 et des frontières U53, D03/D07/D09/D10/processus. L’hypothèse de domaine commun achats/ventes est explicitement à challenger. Retour autorisé, retour accepté et remède distingués ; Q034/Q069 non résolues par les sources externes.

ELM085/ELM086/CMP053 après lecture SAP Sales Order Management et Microsoft accords/retours. Ni domaine Commercial Commitments natif ni quatre capacités natives équivalentes démontrés. Carte, P84, correspondances et navigation enrichies ; D04.a–d historiques et comptes conservés. État U96/F202/A68/C63/P84 ; MKT21/ELM86/CMP53. D03 reste validé, CTP différé, P81 dix domaines/40 capacités et CAP36 inchangés.

Contrôle U96 : identifiants uniques et séquentiels ; 748 liens locaux et ancres valides selon les conventions existantes. P81 à 40 capacités et empreinte CAP36 conservés ; P84 liée à la vue de travail sans adoption automatique.

## 2026-09-11 — Référentiels externes et commandes distinctes des Agreements (U97/U98)

U97 puis la réponse U98 ont été enregistrés avant consolidation F203–F208/A69/C64/P85. Laurent impose la maîtrise externe de Party / Role, Agreement et Catalog, leurs liens lâches par identifiants et une seule capacité d’ingestion par domaine. Il confirme que les commandes sont distinctes des Agreements. Les conditions particulières reçues continuent d’alimenter les décisions d’Order Promising.

P81 passe en version 0.6 : dix domaines actifs, 34 capacités. Neuf anciennes aptitudes D08.a–c/D09.a–c/D10.a–c retirées de la vue plateforme, trois ingestions ajoutées avec nouveaux repères D09.d/D11.a/D12.a. D08/D10 retirés sans réutilisation d’identité ; les trois référentiels sont contigus. D04 est recentré sur les commandes avec ses quatre repères conservés ; noms et regroupement restent proposés. L’audit conserve les définitions remplacées et la première revue D04.

AGENTS, carte, propositions, autorités INF18–INF20, glossaire TER046–TER050, raccordements aux récits et comparaisons actualisés. CAP001–CAP003 conservent les titres importés avec périmètre corrigé ; les 33 autres fiches restent inchangées. Q010 partiellement répondue sur la maîtrise externe, toujours ouverte sur les autorités installées et attributs. CMP054 précise les limites des rapprochements au corpus déjà consulté ; aucune nouvelle recherche externe. D03 reste validé et CTP différé. État U98/F208/A69/C64/P85, INF20/DEC22, TER50/VER25, MKT21/ELM86/CMP54.

Contrôle U97/U98 : identifiants uniques et séquentiels ; dix domaines actifs et 34 capacités uniques, trois ingestions contiguës. Neuf lignes D03 et 33 fiches CAP004–CAP036 inchangées ; 767 liens locaux et ancres contrôlés sans erreur. Résultats et empreinte conservés dans l’audit de correction des référentiels.

## 2026-09-11 — Audit marché achats/ventes, référentiels et capacités (U99)

U99 enregistré avant F209/A70. Audit de P81 0.6 : séparation de Party/Agreement/Catalog/Order par marché, références complémentaires et prix, puis revue des 34 capacités. Douze dossiers ELM087–ELM098 et CMP055–CMP057 ajoutés après consultation officielle SAP, Microsoft, TM Forum et Guild ; les notices Planned/Pre-production et les limites d’accès restent explicites.

P86 propose des variantes achat/vente pour les références, l’épreuve de commandes spécialisées, la réception explicite de Product Reference, les autorités de Transaction Pricing et de consommation d’Agreement, puis la répartition du D02 résiduel et des noms courts. Neuf pistes AC ne sont pas neuf capacités ajoutées. C65 limite le constat historique de couverture ; Q070–Q073 restent ouvertes. Les noms, définitions et statuts des 34 capacités actives et les 36 fiches CAP sont conservés. D03 validé et CTP différé ; aucune maîtrise externe réintroduite dans FLOW.

État : U99/F209/A70/C65/P86/Q73, MKT21/ELM98/CMP57 ; INF20/DEC22, TER50/VER25 inchangés. Rapport dans audits, liens depuis la carte, les correspondances, le glossaire, les autorités, README et AGENTS. Contrôles documentaires consignés après exécution.

Contrôle U99 : 34/34 repères audités, neuf pistes AC, dix domaines actifs ; définitions P81 et registre CAP36 inchangés. Identifiants uniques et séquentiels, 797 liens locaux et ancres valides. Empreinte CAP36 consignée dans le rapport ; aucune proposition promue comme décision.

## 2026-09-11 — Documents d’autorisation de la Supply et article autonome (U100)

U100 enregistré avant F210–F212/A71. Laurent précise le socle transactionnel générique : documents comme preuves d’autorisation de déplacement, décisions contextuelles et parcours commerciaux dans la couche processus. La note 26 distingue, à titre proposé, autorisation/engagement d’exécution/fait réel et Party/lieu ; elle ne fixe ni domaine Supply unique, ni schéma universel, ni solution DMN. D04/D07 passent explicitement en revue selon cette orientation ; leurs quatre capacités respectives restent des propositions antérieures conservées.

P81 0.7 : onze domaines actifs, 35 aptitudes. D08 reprend son sujet article sous le nom proposé Product Reference, avec D08.d ingestion seule dans la continuité de U97 ; D08.a–c demeurent retirées. Autonomie article confirmée U100 ; attributs et source ouverts INF21. Références contiguës D09/D11/D08/D12. C66 conserve l’état remplacé ; P86 et l’audit U99 reçoivent un statut actualisé sans effacer leurs constats. CMP058 qualifie les rapprochements partiels et l’absence de comparaison précise du modèle documentaire. Q070/Q071 partiellement répondues, Q074 ouverte ; TER051–TER053 proposés.

AGENTS, README, orientations, modèle objets/faits, vues historiques pertinentes, correspondances et portée CAP001 actualisés. Les autres fiches CAP, les neuf capacités D03 validées et le report CTP sont conservés. État U100/F212/A71/C66/P86/Q74, INF21/DEC22, TER53/VER25, MKT21/ELM98/CMP58. Contrôles documentaires à suivre.

Contrôle U100 : 823 liens locaux et ancres vérifiés sans erreur ; identifiants U/F/A/C/P/Q/CAP/INF/CMP uniques et séquentiels. Carte : onze domaines, 35 capacités aux repères uniques, quatre référentiels contigus. Aucun ancien repère de capacité supprimé ; aucune archive modifiée.

## 2026-09-11 — Regroupement des référentiels (U101)

U101 enregistré avant F213/A72. Comparaison ciblée des domaines de données SAP MDG, des catégories et données produit Microsoft, des blocs ODA et du principe de capacité Guild. MKT22, ELM099–ELM102, CMP059 ajoutés, avec date, localisateurs, éditions et limites ; pas d’équivalence RBA déduite de MDG. Une page Global address book inaccessible n’est pas utilisée comme preuve nouvelle.

P87 recommande un groupe de présentation Business References conservant les quatre modèles et ingestions. Trois options comparées ; Q075 ouverte. C67 précise que l’autonomie article ne valide pas le rang de domaine. Carte P81 0.7 conservée : onze domaines et 35 aptitudes, aucun nom ni repère de capacité changé, neuf capacités Order Promising toujours validées. Maîtrise externe et CTP différé préservés.

Note dans marche/regroupement-referentiels.md, liée depuis la carte et les index. État U101/F213/A72/C67/P87/Q75, MKT22/ELM102/CMP59 ; autres registres de capacités et autorités inchangés.

Contrôle U101 : 837 liens locaux et ancres valides ; identifiants U/F/A/C/P/Q/MKT/ELM/CMP uniques et séquentiels. P81 conserve onze domaines et 35 aptitudes. Aucune archive modifiée.

## 2026-09-11 — Fulfillment Network distinct de Party (U102)

U102 enregistré avant F214/A73. Laurent confirme Party ≠ lieu et demande le référentiel Fulfillment Network ; verbatim Fullfilment conservé, orthographe normalisée dans la rédaction. P81 0.8 ajoute D13/D13.a : douze repères de domaines, 36 aptitudes. Les 35 lignes précédentes restent inchangées ; rang de domaine, groupe et définition détaillée encore proposés. Cinq références contiguës, sans fusion ni administration ajoutée.

D06 reçoit une clarification d’usage des références D13, distincte des décisions D03 et engagements/faits D07. C68 conserve l’ancien rattachement implicite des lieux et précise CAP002. INF22/TER054/Q076 ajoutés ; Q071/Q074 partiellement répondues, Q075 étendue aux cinq références sans arbitrage présumé. P87, note 26, glossaire, correspondances, AGENTS et navigation actualisés. CMP060 signale les rapprochements partiels existants et la comparaison précise non réalisée ; aucune nouvelle recherche externe.

État U102/F214/A73/C68/P87/Q76, INF22/DEC22, TER54/VER25, MKT22/ELM102/CMP60. D03 validé inchangé, CTP différé, logistique hors développement FLOW et autonomie C-Log conservés.

Contrôle U102 : 846 liens locaux et ancres valides ; identifiants U/F/A/C/Q/INF/CMP uniques et séquentiels. Douze repères de domaines, 36 aptitudes uniques et cinq références contiguës. Les 35 lignes de capacités préexistantes ont été vérifiées inchangées lors de la mise à jour. Archives préservées.

## 2026-09-11 — Application du groupe Business References (U103)

Go enregistré en U103 avant F215/A74. Portée interprétée et explicitée : accord contextuel sur la présentation des cinq références, dont Fulfillment Network. P87 retenue dans cette portée, Q075 résolue. C69 conserve l’état antérieur ; aucune promotion des attributs candidats, des maîtres ou des autres domaines.

P81 0.9 présente effectivement sept domaines transactionnels de travail puis Business References ; tableau détaillé et cinq sections de référence conservés. Douze repères actifs et 36 lignes de capacités inchangés, sans capacité mère ni domaine fusionné. Ancienne ancre des référentiels maintenue. AGENTS, propositions, questions, comparaison et navigation actualisés ; CMP061 sans recherche externe. Q076 reste ouverte, D03 validé et CTP différé préservés.

État U103/F215/A74/C69/P87/Q76, CMP61 ; registres d’autorités et CAP36 inchangés. Contrôles documentaires à suivre.

Contrôle U103 : 850 liens locaux et ancres valides ; identifiants U/F/A/C/P/Q/CMP uniques et séquentiels. Les 36 lignes de capacités sont inchangées ; ancienne ancre des référentiels préservée. Archives non modifiées.

## 2026-09-13 — Proposition d’application d’exploration du modèle (U104)

U104 enregistré avec le texte de Laurent avant la proposition produit. Demande d’une application simple permettant de comprendre le modèle en le parcourant, d’effectuer une recherche directe et d’accueillir de futurs niveaux d’urbanisme, objets métier, documents et événements. Aucune nouvelle hiérarchie métier ni décomposition mécanique adoptée ; distinction transactionnel/processus conservée.

La [note FLOW Atlas](prototypes/model-explorer/README.md) propose une carte à zoom sémantique, un voisinage de relations typées, une recherche avec retour au contexte et une fiche de Finalité, statut et sources. Le prototype interactif est fondé sur un instantané dérivé et daté de P81 0.9 : sept domaines de travail, Business References avec cinq références et 36 aptitudes. Les neuf capacités Order Promising validées en U95 gardent leur statut ; l’exemple de confirmation de promesse de la note 24 reste une illustration. AGENTS et navigation complétés ; registres de capacités et arbitrages métier inchangés.

Architecture proposée : lecteur local, nœuds et relations séparés des sources, identifiants stables, profondeur de navigation libre et index de recherche local. Installation, ingestion automatisée, édition collaborative et liens partageables persistants restent à concevoir ; aucun choix d’outil ou d’hébergement et aucune publication.

Contrôle U104 : prototype interactif assemblé et exécuté dans un navigateur Edge de test isolé. Douze repères, 36 capacités aux identifiants uniques, neuf capacités validées en U95 ; noms et rattachements du snapshot conservés. Navigation jusqu’à Business References → Product Reference → Product Reference Ingestion, relations de l’exemple, historique précédent/suivant, recherche française et par identifiant, filtres par type/statut, raccourcis et parcours guidé vérifiés. Quatre largeurs testées, dont 320 px pour la surface, sans débordement horizontal ; repli des relations en une colonne et thèmes clair/sombre contrôlés visuellement. Corrections du filtre « capacités validées », des options de type et du repli sur écran étroit ; aucun changement métier. Aucune erreur JavaScript dans les contrôles finaux. L’instantané reste une projection de démonstration à régénérer, sans synchronisation automatique ni ouverture directe des registres dans l’aperçu.

## 2026-09-13 — Application locale FLOW Atlas alimentée par les registres (U105)

Go enregistré en U105 avant la réalisation. Accord contextuel pour construire l’explorateur proposé après U104 ; aucun statut métier, niveau d’urbanisme supplémentaire ou relation illustrative promu par cet accord.

Création de l’application locale dans `app/` : serveur Python utilisant la bibliothèque standard, interface HTML/CSS/JavaScript, lecture des noms, définitions et finalités de P81 courante. Les métadonnées de présentation conservent leurs sources et limites. L’exploration combine arborescence de profondeur libre, fiches, relations et recherche ; les adresses de navigation conservent le contexte sur la machine. La lecture des sources et l’actualisation après modification des registres relient la vue à l’état documentaire. Le prototype U104 reste conservé comme historique.

Ajout de `Lancer-FLOW-Atlas.ps1` : recherche d’un Python fonctionnel, lancement caché du serveur sur l’interface locale, réutilisation après contrôle de signature et de racine, ouverture en fenêtre d’application Edge lorsque disponible. Les journaux et métadonnées de processus sont rangés dans `app/.runtime`. Le mode d’arrêt exige la concordance du serveur et du PID enregistré. Documentation de lancement, d’usage et de maintenance ajoutée ; aucune installation globale ni publication externe.

Contrôles U105 : extraction courante P81 0.9 — douze repères, 36 capacités, neuf validations, aucune référence de qualification non résolue. Quatorze tests Python réussis et un test de lien symbolique ignoré faute de permission système ; neuf tests du moteur réussis, dont une hiérarchie plus profonde, les identifiants déplacés et les relations inverses. Parcours navigateur vérifiés : recherche et filtres, clavier, liens directs avec rechargement, historique précédent/suivant, copie du lien, registre et ancre source, recherche dans le document, parcours guidé et rechargement des données. Une réponse modifiée et sa qualification à relire ont été simulées dans le navigateur de test, puis remplacées par les données réelles ; aucun texte métier modifié. Quatre largeurs de 320 à 1 360 px et thèmes clair/sombre contrôlés, sans débordement horizontal ni erreur JavaScript/CSP. Les liens devenus inconnus conservent un diagnostic visible.

Lanceur vérifié de bout en bout sur le port distinct 8766 : démarrage, réutilisation du même PID, arrêt, port libéré et second arrêt sans processus suivi. Correction de comparaison des instants UTC après conversion JSON PowerShell. Le serveur principal reste lancé sur 127.0.0.1:8765. Les sources de capacités et arbitrages restent inchangés ; les métadonnées de qualification sont explicitement datées, et les anciennes illustrations U104 restent proposées.


## 2026-09-13 — Modèles JSON, publication qualifiée et panorama des trois SI

Sources : U106–U112, F216–F219, A75, C70. L’audit demandé devient une reprise effective, avec les noms backlog, release et panorama-as-is choisis par Laurent. U110 demande la centralisation de toutes les règles de refactoring dans AGENTS.md.

- Extraction de P81 0.9 : 53 nœuds de backlog, dont 36 capacités et quatre éléments illustratifs ; alternatives P82/P84 distinctes. Les 36 CAP historiques restent dans un inventaire de provenance séparé.
- Première compilation partielle 2026-09-13.1 conservée comme historique. Après U111, publication de la release complète 2026-09-13.2 : 49 nœuds, 36 capacités, 41 relations. Neuf capacités validées ; huit portent des validations partielles, dont Reservation en réexamen ; dix-neuf sans validation individuelle. Les statuts affichés sont 9 accepted, 7 partial, 8 proposed et 12 under_review.
- 47 transcriptions ADOPT des accords existants, avec portée par champ, sources et empreintes des valeurs. Manifestes, entrées et preuves gelés ; current.json désigne la release publiée. Publication distincte de validation métier, aucun nouvel arbitrage.
- Panorama des trois SI et contexte partagé : 85 repères conservés une fois, 74 décrits dans le panorama, 11 besoins/orientations/mentions à instruire dans le backlog. Sarenza non traité et vide ; dates d’observation inconnues ; 26 extrémités de flux non résolues conservées par leur libellé source.
- Schémas JSON et contrôles d’intégrité, publication locale avec refus d’écrasement, conservation des preuves gelées et activation du pointeur en dernier. Les extracteurs initiaux ne sont plus le circuit d’édition du modèle courant.
- U112 : feuille de route pour le niveau supérieur à définir et les objets/documents/événements ultérieurs ; relations caractérisées prévues entre capacités et vers ces éléments. Registre d’applicabilité à quatre contextes, sans évaluation inventée. Travail actuel limité à domaine/capacité et à leur épreuve sur les trois SI et FLOW cible.
- FLOW Atlas lit désormais les trois espaces JSON ; les Markdown restent consultables comme sources. La configuration applicative porte uniquement la présentation, les anciens apports métier sont conservés dans app/legacy. Restitutions Markdown générées depuis les JSON.
- AGENTS.md, README et guide modeles/README.md actualisés ; les registres historiques de carte et de panorama indiquent leur nouveau rôle de sources. Audit daté dans audits/2026-09-13-structure-modeles.md.

Vérifications : modèles et décisions contrôlés, tests négatifs d’intégrité et de publication, conservation des 85 repères, tests du lecteur et de la navigation, parcours navigateur des trois espaces sur trois largeurs sans erreur JavaScript. Un test de lien symbolique est ignoré lorsque Windows n’autorise pas sa création. Les trois fichiers ChatGPT d’origine conservent leurs empreintes initiales. Les liens locaux de la documentation contrôlée sont résolus.

Le serveur FLOW Atlas du projet a été identifié puis redémarré sur 127.0.0.1:8765 ; il expose la nouvelle API de schéma 2. Aucune publication externe et aucun déploiement SI n’ont été effectués.

Le backlog courant passe également en 2026-09-13.2 : les neuf statuts d’Order Promising sont explicitement accepted, conformément à U95. Il s’agit d’une correction de qualification ; les champs et leurs révisions restent inchangés. La révision d’entrée .1 des releases reste gelée.


## 2026-09-13 — Backlog par défaut et skills de travail

Source : U113. L’exploration et la construction du modèle se font désormais dans le backlog par défaut. FLOW Atlas, son lecteur et les API sans espace explicite suivent cette règle ; les demandes et liens explicites Release / Panorama As Is restent respectés.

- Création du skill `release` : évaluation des évolutions, préparation d’un candidat contrôlable et publication locale distincte de la validation métier. Le nouveau workflow `scripts/prepare_release.py` compare le backlog vivant ; `report` est en lecture seule, `prepare` écrit seulement dans `modeles/staging/<version>/`, `publish --activate` conserve les entrées figées et actualise le pointeur en dernier. Les anciennes décisions incompatibles restent historiques et sont signalées comme suspendues ; elles ne sont pas transportées vers des valeurs ou révisions nouvelles.
- Création de `server-admin` : état, démarrage, arrêt et redémarrage via le lanceur identifié, sans ouvrir automatiquement un navigateur. Test indépendant sur le port 8879 : démarrage, changement de PID au redémarrage, arrêt final et port libéré ; serveur principal préservé pendant cet essai.
- Sources des deux skills dans `skills/`, avec métadonnées d’interface ; installation personnelle dans le dossier de skills Codex du poste. AGENTS.md décrit le déclenchement, la portée, la maintenance et le nouveau cycle.
- `scripts/refresh_sources.py` actualise seulement l’index de provenance courant, sans réimporter les modèles ni modifier les preuves gelées.
- Contrôles finaux : 57 tests des scripts, 17 tests applicatifs Python (un ignoré pour lien symbolique non autorisé), huit tests JavaScript et parcours navigateur de démarrage Backlog / liens explicites / retour historique / mobile réussis. Les tests de publication ont lieu dans des copies isolées.

La création des skills ne publie pas une nouvelle release : la comparaison du modèle courant ne présente aucun changement publiable ; la version 2026-09-13.2 demeure pointée.


Vérification indépendante du skill release : dans une copie isolée, évolution d’une définition validée et ajout d’une qualification de relation, puis préparation/publication de l’essai. Résultat : 36 capacités publiées, huit validées, 46 décisions conservées et l’ancienne validation incompatible suspendue sans nouvelle adoption. Les preuves gelées restent identiques. La fixture a été supprimée après contrôle de son périmètre ; les releases du projet principal restent inchangées. Le test a motivé le contrôle explicite des anciennes notes narratives de validation.

Les deux skills ont été validés et installés avec leurs métadonnées d’interface. PyYAML 6.0.2 est une dépendance d’outillage locale pour le validateur officiel, pas une dépendance de l’application. Le serveur principal a été redémarré via le lanceur identifié ; API et modèle sans espace explicite répondent désormais backlog, version 2026-09-13.2.


## 2026-09-13 — Mise sous Git et skills commit / push

Source : U114. Dépôt distant fourni par Laurent : https://github.com/laurent-sintes/Urbanisation. Lecture GitHub à la configuration : dépôt vide, public, accès administrateur du compte connecté. Initialisation du dépôt local sur main, ajout d’origin en HTTPS et identité GitHub configurée uniquement pour ce dépôt.

- `.gitignore` exclut l’outillage installé, les dépendances, caches, fichiers temporaires, état/logs/captures du serveur et candidats locaux de staging. Archives, preuves, versions publiées et sources des skills sont incluses.
- `.gitattributes` désactive la conversion des fins de ligne pour préserver les octets et empreintes des fichiers figés ; les formats binaires sont déclarés comme tels.
- Création des skills `commit` et `push`, avec sources dans le projet et copies personnelles pour leur découverte. Commit local, push GitHub, publication de modèle et administration du serveur restent des actions distinctes.
- AGENTS.md et les points d’entrée précisent la destination, le périmètre des workflows, les contrôles, le respect des changements existants et l’absence de réécriture forcée de l’historique.

La base initiale est enregistrée dans un premier commit local, après vérification des fichiers indexés et des empreintes. Aucun push n’est déclenché par la demande de création des skills ; aucun changement de visibilité GitHub ni nouvelle release métier n’est effectué.

Contrôles de mise sous Git : 57 tests des scripts, 17 tests applicatifs Python (un ignoré pour lien symbolique non autorisé), huit tests JavaScript, validation des modèles et des deux skills réussis. Les 139 fichiers retenus sont indexés sans changement d’octets ; les dépendances, caches et états du serveur sont exclus. Les avertissements de blancs présents dans les contenus antérieurs sont conservés plutôt que reformater les archives ou preuves. Les fins de ligne CRLF sont reconnues par les attributs Git.


## 2026-09-13 — U115/U116 : corriger D01 dans le backlog et les propositions Atlas

- Diagnostic : l’Atlas lisait correctement les JSON, mais la migration conservait les six nœuds P81 et isolait P82 dans une collection invisible à l’écran. Les réponses conversationnelles doivent distinguer les nœuds courants et les alternatives.
- À la demande U116, D01 utilise désormais cinq capacités dans le backlog 2026-09-13.3 : Inventory Tracking, Inventory Visibility, Stocktaking, Supply Protection et Reservation. D01.e est créé pour le regroupement D01.a/D01.b ; D01.c passe en révision 2. Les anciens identifiants ne sont pas réutilisés. Total courant : 35 capacités.
- Les trois dernières capacités et toutes les validations préexistantes restent inchangées. La comparaison de publication reprend les 47 décisions compatibles, sans nouvelle décision ni validation différée. La release .2 conserve ses 36 capacités et six lignes D01 ; aucune publication ni modification des fichiers figés.
- Les propositions encore distinctes, comme P84 pour D04, deviennent consultables dans le backlog Atlas avec leurs sources ; elles ne remplacent pas les nœuds et ne contaminent pas la release.
- U115/U116, C71, audit daté, correspondances marché, AGENTS et guides actualisés ; restitution backlog et index courant des sources régénérés.
- Vérification : 57 tests des modèles/publications, 17 tests Python Atlas (un ignoré pour lien symbolique Windows), 9 tests JavaScript et parcours navigateur réussis. Contrôle HTTP des cinq noms en backlog et six en release, recherche, rechargement et ouverture de sources vérifiés. Fichiers de release, décisions, révisions, preuves figées et archives identiques octet par octet au commit initial. Aucun redémarrage nécessaire : aucun code serveur Python modifié.


## 2026-09-13 — U117–U123 : Urbanisation publiée, versions et actualisation Atlas

- Audit des douze repères : D01 corrigé, onze noms courts D04–D07 intégrés selon U118, D03 et les cinq références déjà cohérents. D02 et les noms conditionnels D05 restent ouverts. Audit et tableau de renommages dans audits/2026-09-13-domaines-et-urbanisation.md et audits/2026-09-13-renommages.json.
- Publication 2026-09-13.3, modèle v001 : 35 capacités, dont neuf validées. 46 décisions compatibles reprises. ADOPT-001 reste historique, sa reprise étant suspendue par la révision du domaine D01. Aucun autre statut métier promu.
- Modèle global et 94 éléments publiés munis de revision entière automatique et last_modified UTC. Incrément sur changement, stabilité sur republication identique ; empreinte du contenu soumis distincte des annotations calculées. Les métadonnées des anciennes versions restent intactes.
- Descripteur urbanisation-v001-2026-09-13-153941.json et note release-notes.md produits. Index technique activé après les écritures ; ancien current.json conservé dans release/legacy/current-2026-09-13.2.json. Les anciennes publications sont référencées comme historiques, sans horodatage précis inventé.
- Atlas expose uniquement Urbanisation, avec sélection des publications en ordre décroissant. Le backlog et le panorama restent disponibles dans le projet. Le modèle courant se rafraîchit automatiquement ; une ancienne version sélectionnée reste fixe. Métadonnées visibles dans l’inspecteur et API dataRevision distincte de la version entière revision.
- Skills release et server-admin actualisés : release inclut production, publication, disponibilité et actualisation dans Atlas. Serveur relancé sur 127.0.0.1:8765 pour installer le nouveau code Python ; contrôle d’identité réussi.
- Validation : 61 tests Python des modèles/publications, 17 tests Python Atlas (un ignoré pour lien symbolique Windows), neuf tests JavaScript ; parcours navigateur réussi pour tous les domaines, versions historiques, anciens liens, recherche, sources, actualisation automatique et petits écrans. Validation de modèle : zéro erreur. Les tests d’actualisation simulée n’écrivent pas dans les releases.


## 2026-09-13 — U125/U126 : mouvements de stock et Inventory Tracking

- Vérification SAP Goods Movements, Microsoft Inventory transactions/movements et Business Central Item Ledger Entry ; ELM103–ELM105/CMP062 qualifient ces appuis de produit, sans rang natif de capacité affirmé.
- Séparation de travail dans le backlog : D01.f Inventory Tracking et D01.g Inventory Movements remplacent D01.e ; nouveaux repères pour la scission, historique figé conservé. Six capacités D01, 36 au total. Les autres capacités restent inchangées.
- Ledger expliqué comme registre ; Inventory Ledger Management conservé comme nom alternatif non adopté. Glossaire TER055/TER056, correction C73 et AGENTS actualisés.
- Aucun changement de release, aucune nouvelle validation métier. Les détails du registre, documents, événements et autorités restent à explorer.


## 2026-09-13 — U127/U128 : vocabulaire de la capacité de mouvements

- Record Inventory Movements ajouté comme candidat de nom fourni par Laurent, distinct de l’adoption définitive.
- Glossaire : distinction Sourcing dans les achats et Event Sourcing en architecture logicielle, avec appuis SAP/Microsoft datés. Aucune intention technique attribuée à Laurent ; sens de sa question ouvert.
- Réserve de provenance complétée après la scission D01.e. Backlog à six capacités D01 ; release inchangée.


## 2026-09-13 — U129 : Record Inventory Movements adopté

- Nom de D01.g remplacé par Record Inventory Movements ; validation explicite du seul nom par Laurent, statut partiel dans le backlog. Définition et finalité inchangées et proposées.
- Alternatives de nom retirées de la liste active, historique conservé en C74 et au glossaire. Correspondance CMP062 actualisée sans nouvelle équivalence marché.
- Six capacités D01 et 36 au total dans le backlog. Release et Atlas inchangés ; validation à reprendre dans les décisions de la prochaine publication.


## 2026-09-13 — U131 : cycle de vie des éléments

- Trois états enregistrés : Proposé par l’IA, En cours d’instruction, Validé par l’urbaniste. Métadonnées lifecycle distinctes des champs effectivement approuvés.
- Reprise dans le backlog des nœuds et relations : accords existants limités à leur portée, éléments discutés en instruction, illustrations en proposition IA. Aucun contenu métier modifié ni accord élargi.
- Schéma, contrôles, restitutions et lecteur Atlas adaptés ; anciens modèles sans lifecycle conservés. Les nouveaux statuts paraîtront dans Atlas lors d’une prochaine release. Aucune publication implicite.

- Vérification U131 : contrôles des modèles et de publication réussis, 68 tests Python de modèle/cycle, 17 tests Atlas (un ignoré sur Windows), dix tests JavaScript ; navigateur validé pour badges, portée du nom, filtres, compteurs, versions historiques et actualisation. La simulation de publication n’a modifié aucune release.
- Reprise courante : 18 capacités en cours d’instruction et 18 validées par l’urbaniste dans leur portée ; les illustrations restent proposées par l’IA. Candidat vérifié avec 47 accords transcrits et aucune suspension, sans publication. Recharger la page lors de la prochaine release pour utiliser le JavaScript mis à jour.


## 2026-09-13 — U132 : audit ergonomique d’Atlas

- Demande enregistrée avec son texte et sa portée : arbre de navigation à gauche ; examen de la concentration à droite et de l’étroitesse des composants dans les pages de détail.
- Orientation d’interface consignée dans AGENTS.md, en conservant la distinction entre hiérarchie explicite, regroupement de présentation et relations métier transversales.
- [Audit ergonomique](audits/2026-09-13-ergonomie-atlas.md) consacré aux parcours, à la lisibilité et à la navigation de l’application courante. Les recommandations ne constituent pas une modification ou une validation du modèle ; aucune release n’est déclenchée par cette demande.
- Précision U133 : Laurent écarte les visites récentes. Leur suppression est retenue dans les orientations de l’audit, sans maintien dans un accès secondaire ; consigne reprise dans AGENTS.md.
- Audit réalisé sur v002 / 2026-09-13.4, avec lecture du code, neuf captures et mesures sur cinq formats d’écran. Sept constats hiérarchisés : arbre absent, fiche métier comprimée à 253 px sur un écran de 1366 px, répétitions, recherche française incomplète, destinations vides, provenance envahissante et perte de contexte au défilement/clavier. Organisation proposée : arbre gauche, fiche centrale, preuves à la demande. Code de l’application et publication inchangés.

## 2026-09-13 — U134 : audit D04 et projections de référence

- [Audit D04/Agreement](audits/2026-09-13-d04-agreement-projections.md) : distinction des contrats de référence et des commandes conservée ; responsabilités commerciales de D04 et recouvrement D07 à instruire.
- Principe des projections externes consigné dans AGENTS.md et le JSON backlog : au moins une ingestion par référentiel, consultation et recherche en lecture seule. C75 précise la règle historique « ingestion seule » sans effacer sa provenance.
- Cinq ingestions présentes ; visibilité absente de la carte et métadonnées de maîtrise hétérogènes. Pattern Ingestion + Visibility proposé dans l’audit, sans ajout de capacité ni validation implicite. Aucune publication.

## 2026-09-13 — U135 : réorganisation ergonomique d’Atlas

- Go contextuel enregistré ; réalisation de l’arbre gauche et suppression des visites récentes, avec sélection/expansion distinctes, largeur réglable et navigation au clavier. Les relations explicites de la publication restent l’autorité de la structure affichée.
- Fiche métier centrale avec Finalité, Définition et réserves visibles ; sources, versions et preuves détaillées consultables à la demande. Parcours vides supprimés, filtres limités aux valeurs publiées et suggestions de recherche ajustées. Aucun ajout implicite de synonymes depuis le backlog.
- Six formats d’écran vérifiés, jusqu’à 320 px ; texte de définition à 673 px sur écran de 1366 px, contre 253 px auparavant. Sur écran de 390 px, Définition à y ≈ 563 px, contre 947 px. Tiroir mobile et restitution du focus contrôlés.
- Dix tests JavaScript et deux parcours navigateur couvrant l’arbre, les sources, la recherche, les versions, le rafraîchissement et une hiérarchie synthétique plus profonde. Aucun modèle publié modifié, aucun service relancé. Captures et résultats ajoutés à [l’audit ergonomique](audits/2026-09-13-ergonomie-atlas.md).
## 2026-09-13 — U136 : Orders, Agreements et Commitments

- Comparaison SAP, Microsoft et Oracle consignée dans marche/orders-agreements-commitments.md, ELM106–ELM108/CMP063.
- C76 corrige l’assimilation trop générale de Commitment à une commande : Microsoft emploie aussi ce terme dans ses Agreements. Sources SAP limitées aux extraits indexés ; textes Microsoft et Oracle lus.
- Distinction commande source/réalisation à éprouver avec D04/D07 ; aucun renommage, ajout de capacité ou publication.
## 2026-09-13 — U137 : cadre contractuel et période

- Hypothèse de Laurent enregistrée : cadre + engagements de période + commandes de consommation. Statut en cours d’instruction ; aucun objet ou domaine supplémentaire adopté.
- Comparaison complétée : un Agreement Microsoft peut déjà porter période et engagements. Conditions applicables composées, consommation par commande et réalisation effective restent distinctes. Maîtrise externe U134 conservée.
## 2026-09-13 — U138/U139 : localisation des Orders

- Recherche dans cinq références : SAP, Microsoft, Oracle, IBM Sterling OMS et TM Forum ; étude dans marche/localisation-orders-cartographie.md.
- Sources, versions et limites conservées en ELM109–ELM113, MKT23 et CMP064. Distinguer famille de documents, domaines, processus, composants et produits ; aucune équivalence universelle Orders établie.
- Proposition d’un Order Management transactionnel restreint à éprouver avec D07 ; analyse des cas réassort, achats, façon, Boardriders et retours comme accueils conceptuels, sans preuve de couverture installée. Aucun changement de capacité ni publication.
## 2026-09-13 — U140 : univers Supply et Order Management commun

- Orientation enregistrée : Case/demande distinct d’Order/pilotage Supply, univers Case différé ; domaine Order Management commun, retours inclus, tous clients et volumes.
- Nom D04 appliqué dans le backlog avec portée d’accord limitée au nom ; définition/finalité proposées et capacités héritées encore à revoir avec D07. Principe structuré Case/Supply, sans hiérarchie d’univers inventée.
- Étude marche/supply-b2b-b2c.md, ELM114/CMP065 : socles communs mais contraintes opérationnelles différentes, dimensionnement à préciser ; DMN distinct du workflow complet. Aucune publication.
## 2026-09-13 — U141 : application des six mises à jour

- Univers Supply et Case structurés ; Business References conservé comme groupe de présentation. Modèle processus réservé, objets et liens Case/Order préparés dans la feuille de route sans cardinalité imposée.
- D04.e–h remplacent les anciennes capacités D04.a–d, avec noms et descriptions courtes approuvés ; snapshot antérieur conservé. Agreement complet précisé ; D07 recentré sur les prestations et faits, lien de contribution au rapprochement de commande caractérisé.
- C78, Q077 et CMP066 préservent retraits, portée des accords et limites de couverture marché. Note connaissance/27-order-management-et-univers.md. Backlog uniquement ; aucune release, commit ou push.
## 2026-09-13 — U142 : Urbanisation v003 publiée

- Publication `2026-09-13.5`, descripteur `urbanisation-v003-2026-09-13-173533.json` activé : 51 nœuds, 36 capacités, univers Supply/Case, D04 refondu et frontière D07 précisée.
- 54 décisions : 45 transcriptions initiales du cycle U131 et neuf décisions nouvelles ciblées U140/U141. Les portées Agreement antérieures suspendues pour changement de révision sont réaffirmées avec nouveaux identifiants ; historique conservé. Aucune validation des nouveaux détails par simple publication.
- Contrôles modèle et serveur réussis. API Atlas du dépôt vérifiée au port 8765 : version 2026-09-13.5, liste v003 en premier ; interface rechargée pour installer le code courant. Aucune copie du référentiel dans Atlas, aucun commit ni push.

## 2026-09-14 — U143 : étude des outils et parcours d’exploration d’Atlas

- Demande conservée avec son texte ; critère de génération et de maintenance du code par IA consigné dans AGENTS.md. Recherche sur les documentations officielles de LikeC4, IcePanel, React Flow et Cytoscape.js, complétée par Kumu, Obsidian, Structurizr, D2 et trois moteurs de placement.
- [Étude et recommandations](marche/etudes/2026-09-14-exploration-atlas/etude.md), [sources qualifiées](marche/etudes/2026-09-14-exploration-atlas/sources.md) et empreintes de l’état examiné enregistrées. Parcours de navigation réellement effectué dans le Playground LikeC4 ; autres interactions étudiées dans les sources, sans benchmark ni installation.
- Proposition : arbre et sélection communs aux vues Fiche, Carte et Relations ; exploration progressive, qualification des liens, cartes métier lisibles et recherche contextualisée. React Flow proposé comme premier candidat, LikeC4 comme alternative à éprouver, Cytoscape pour les besoins analytiques ultérieurs. Ces choix ne sont pas adoptés par la seule étude.
- Point d’appui réel : relation proposée D07.c → D04.h dans v003 ; l’adaptateur d’Atlas ne projette pas encore sa qualification complète. Aucun ajout d’objet ou de relation, aucune modification applicative ni publication. Aucun commit ou push.
- Vérifications : neuf empreintes applicatives/modèles inchangées, liens locaux de l’étude valides, U143 unique ; index de provenance courant actualisé à 1 003 entrées et `validate_models.py` sans erreur. Aucun test de performance ou d’intégration d’un nouveau moteur n’est présenté comme exécuté.


## 2026-09-14 — U144 : couverture résiduelle de D02

- Accord sur les points d’examen et hypothèse de couverture par D01/D03 enregistrés. Notes d’instruction D02, D02.a et D02.d actualisées dans le backlog.
- Audit `audits/2026-09-14-d02-couverture.md` : Supply Assignment couvre explicitement les affectations ; disponibilité pour réserver et évolution des réservations/protections demandent une clarification textuelle.
- Retrait proposé, non appliqué ; aucune définition validée ou capacité ajoutée, aucune publication. Release et travaux d’ergonomie conservés.


## 2026-09-14 — U145 : retrait de D02 sans renumérotation

- D02, D02.a et D02.d retirés du backlog avec leurs trois relations ; état complet préservé dans `modeles/backlog/history/pre-U145.json`.
- 52 nœuds et 34 capacités. D02.b/D02.c en D01 et D02.e en D03 conservées ; tous les autres identifiants et contenus inchangés.
- U145, C79, audit de couverture et AGENTS.md actualisés. Clarifications des définitions consommatrices toujours à instruire. Aucune publication, aucun commit ni push.


## 2026-09-14 — U147 : décisions et vocabulaire de D03

- Remarques conservées ; ordre des quatre actions appliqué, sans changement de définition. D03 et D03.d/D03.h remis en instruction avec preuves historiques préservées.
- ATP/CTP, échéancement, allocation, ressources et Case/Order examinés dans `marche/revue-d03-decisions-vocabulaire.md` ; sources Microsoft consultées et limites des extraits SAP précisées. Annexe structurée `modeles/backlog/d03-review.json` : propositions non adoptées, aucune nouvelle capacité active.
- Glossaire et AGENTS.md complétés ; aucun changement de release, aucun commit ni push.


## 2026-09-14 — U146 : essai comparatif React Flow / LikeC4

- Go après U143 : prototype local dans prototypes/atlas-exploration/, consultable sur 127.0.0.1:8767. Atlas courant sur 8765 conservé et démarré avec son lanceur. Les travaux métier parallèles U144/U145 ne sont pas incorporés à cet essai de la publication v003.
- Source publiée commune ; arbre, recherche, fiche et sélection partagés, grille React Flow et disposition des relations ELK, vues LikeC4 générées avec correspondance bijective des IDs. Statuts, qualification et sources du lien D07.c → D04.h consultables ; agrégats graphiques annoncés. Aucun historique de visites récentes.
- Quinze tests de données/projection et douze familles de contrôles navigateur réussis, sans erreur console/HTTP ; petit écran 390/320 px, clavier, sources et récupération par lien direct vérifiés. Quatre captures conservées avec le rapport dans marche/etudes/2026-09-14-exploration-atlas/essai/.
- Bilan et recommandation dans prototypes/atlas-exploration/bilan.md : React Flow favorisé pour la composition et la lisibilité métier, LikeC4 pour les vues générées et le contexte des relations. Coût des deux bundles et limites du prototype explicités ; choix définitif non adopté.
- Huit empreintes applicatives et de release identiques à l’état U143. Aucun fichier applicatif d’Atlas ni modèle publié modifié par l’essai, aucune publication, aucun commit ou push. Le backlog a évolué séparément via U144/U145.


## 2026-09-14 — U148 : faisabilité de promesse et plan d’adaptation

- Contribution conservée ; annexe structurée D03 enrichie des deux résultats visés, hypothèses de retrait et frontières calcul/engagement, confirmation/commande et proposition/application.
- Écart de vocabulaire entre CTP de marché et plan global d’adaptation explicité avec sources SAP complémentaires. Promise Feasibility Planning reste un candidat assistant.
- Besoin d’échéancement et ordre des actions confirmés ; aucune suppression ou nouvelle capacité active, aucune release.


## 2026-09-14 — U149 : panorama To-Promise

- PTP identifié dans les sources Oracle ; variantes Channel ATP et Component/Capacity/Product family CTP chez Infor, Multilevel ATP historique SAP. Sources, versions, nature et limites de consultation dans `marche/to-promise-panorama.md`.
- Glossaire et annexe d’instruction D03 enrichis ; distinction entre arbitrage économique, faisabilité et plan d’adaptation. Aucune capacité ajoutée ni release produite.


## 2026-09-14 — U150 : choix React Flow et interface sur mesure validé

- Validation explicite de Laurent conservée avec son texte : React Flow et l’interface sur mesure sont retenus pour Atlas. La comparaison du moteur est close ; LikeC4 reste un historique et une référence d’inspiration.
- AGENTS.md, bilan, README du prototype et étude U143 actualisés pour distinguer décision courante et recommandations historiques. L’intégration dans l’application courante reste à réaliser ; aucun contenu métier n’est validé par cette décision.
- Aucun changement de code applicatif, de modèle métier ou de publication ; aucun commit ni push.


## 2026-09-14 — U151 : proposition D03 au niveau ATP/CTP/PTP

- Orientation de granularité consignée ; réponse explicite au retour U148. Alternative JSON complète à quatre actions et quatre décisions, avec reprise des cinq décisions fines sans perte des règles.
- Liste active et anciennes validations conservées ; les nouvelles définitions restent proposées. Annexe de revue, analyse et AGENTS.md reliés à cette proposition. Aucune release, aucun commit ni push.


## 2026-09-14 — U154/U155 : adoption D03 et exploration Requisition/Order

- D03 à huit capacités validé et appliqué : quatre actions conservées, décisions ATP/CTP/PTP/Delivery Schedule Decision nouvelles D03.i–l. Anciennes D03.d–h archivées avec leur état complet ; règles et couverture reprises. 51 nœuds et 33 capacités au backlog ; release inchangée.
- U155 corrige Requisition ; analyse ERP sourcée distinguant demande interne d’achat, commande et intégration commerce/Supply. Storeland reste un usage rapporté. Aucun renommage de notion adopté, point 5 différé.
- C80/C81, AGENTS.md, glossaire et annexe D03 mis à jour. Aucun commit, push ou release.


## 2026-09-14 — U156 : CTP local et Response Planning

- Recherche de périmètre élargie : Response Planning SAP constitue un rapprochement fort, Oracle Backlog Management un recouvrement partiel, Kinaxis Response Management un appui conceptuel.
- Sources et limites dans marche/ctp-response-planning.md ; annexe D03 et glossaire complétés. Capacité D03.j, noms et validations inchangés ; aucune release.


## 2026-09-14 — U157 : Orders travaillés en carnet et Supply Assignment

- Orientation de Laurent consignée, comparaison SAP/Oracle et C82 : recouvrement réel, périmètre produit Supply Assignment plus large que notre définition locale.
- Annexe D03 et AGENTS.md enrichis. Frontières de résultats et recouvrements D03/D04 à instruire ; aucune fusion, aucun renommage ni release.


## 2026-09-14 — U152/U153 : Atlas React Flow et icônes

- Refactoring de l’application courante : React/TypeScript, arbre gauche, carte React Flow, fiche centrale, recherche filtrée, sources complètes et relations inspectables. Ancien frontend JavaScript remplacé ; prototype comparatif historique conservé, aucune dépendance LikeC4 dans Atlas.
- Icônes Lucide cohérentes pour les 51 éléments publiés, correspondances graphiques centralisées et repli pour chaque type futur. Objets, documents et événements éprouvés uniquement par fixture HTTP, sans ajout au modèle.
- API Python et publication courante/historiques conservées. Compilation Vite servie depuis app/dist ; serveur local relancé et identifié sur 8765. Nœuds et relations toujours issus du JSON publié ; les empreintes de l’index, du descripteur et de v003 restent identiques à l’étude U143.
- Contrôles TypeScript, projection, chargement/API, routes et serveur ; recette navigateur ordinateur/mobile, profondeur supplémentaire, sources, mises à jour et erreurs temporaires. Bilan, résultats et captures dans audits/2026-09-14-refactoring-atlas.md et audits/2026-09-14-atlas-react/.
- Aucun changement métier ni release, aucun commit ou push. Les évolutions du backlog U151/U154–U156 restent celles de l’exploration parallèle.


## 2026-09-14 — U158 : Backlog Management au niveau domaine

- Option de renommage D03 et définition proposées dans le backlog JSON ; aucune modification des valeurs adoptées.
- Frontière D03/D04 et décomposition de Supply Assignment à instruire ; simulation définie comme résultat candidat, avec risque de recouvrement ATP/CTP/PTP explicite.
- Registres et AGENTS.md actualisés. Aucune publication, aucun commit ni push.


## 2026-09-14 — U159 : calcul et impacts globaux

- Distinction explicite de Laurent consignée : solutions calculées par ATP/CTP/PTP, impacts globaux mesurés par simulation. C83 corrige la réserve de doublon trop générale.
- Annexe D03, analyse et AGENTS.md actualisés ; définition et indicateurs proposés. Carte active et release inchangées.


## 2026-09-14 — U160 : audit des manques D03/D04

- Prioritization et Backlog Assessment proposés pour D03 ; Qualification et Structuring à éprouver contre Registration/Revision dans D04. Lancement vers l’exécution à la frontière D03/D07/logistique.
- Sources, résultats et limites dans marche/d03-d04-capacites-manquantes.md ; candidats structurés dans modeles/backlog/d03-d04-gap-review.json, tous proposés par Codex.
- Aucun ajout actif, pas de changement des validations, aucune publication.


## 2026-09-14 — U161/U162 : capacités et Backlog Refinement

- Apports de Laurent conservés ; C84 corrige la dérivation des capacités depuis les étapes ou contrôles de processus.
- Qualification retirée des candidats ; Structuring/Revision et Prioritization en instruction. Backlog Refinement enregistré comme activité.
- Annexe JSON, étude et AGENTS.md actualisés ; aucune modification de la carte active ou de la release.


## 2026-09-14 — U163 : adoption Order Prioritization

- Validation explicite consignée ; ajout D03.m dans le backlog avec relation contains vers D03.
- Nom et définition validés dans le cycle de vie, finalité et nature proposées ; candidats et analyse actualisés.
- D03 compte neuf capacités, le backlog 34 ; aucune publication métier.


## 2026-09-14 — U164 : reprendre le vocabulaire des besoins et commandes

- Demande conservée ; étude des usages SAP, Microsoft et CMMN avec limites de consultation.
- Définitions proposées dans modeles/backlog/vocabulary-review.json ; glossaire et correction C85 précisent notamment Case/Demand et Order/Command.
- Aucun objet supplémentaire, rattachement, renommage de capacité ou publication.


## 2026-09-14 — U165 : intentions et demande d’exécution

- Orientation utilisateur conservée avant reformulation ; C86 distingue pattern logiciel et objet métier Command candidat.
- Nom d’univers Case à réexaminer ; Order réaffirmé. Rapprochement proposé de la demande d’exécution avec D07.
- Annexe de vocabulaire, glossaire, étude et AGENTS.md actualisés ; aucun objet, capacité ou univers ajouté, aucune publication.


## 2026-09-14 — U166 : noms du marché pour l’exécution logistique

- Comparaison sourcée SAP, Microsoft, Oracle et GS1 dans marche/logistics-order-et-demande-execution.md et annexe JSON de vocabulaire.
- Logistics Order attesté en atelier SAP ; Shipment Orders Microsoft rapprochés de la séparation métier/WMS recherchée.
- Aucun nom adopté, aucun ajout de capacité ou d’objet ; aucune publication.


## 2026-09-14 — U167 : demande de prestation générique

- Orientation utilisateur conservée : plateforme exécutante non limitée à la logistique.
- Service Order proposé avec appuis TM Forum/SAP, contenu métier indicatif et distinction demande/engagement/réalisation ; Service Request comparé sans succession automatique.
- Annexe JSON, analyse, glossaire et AGENTS.md actualisés ; aucun objet ni capacité ajouté, aucune publication.


## 2026-09-14 — U168 : contextes Supply / Services

- Distinction utilisateur des Orders et de leurs définitions contextualisées conservée ; portée séparée du schéma détaillé U167.
- Annexe JSON, glossaire, étude et AGENTS.md actualisés ; précision DDD sourcée sur la frontière sémantique et la granularité ouverte.
- Aucun objet, niveau ou capacité ajouté ; aucune publication.


## 2026-09-14 — U169 : validation Supply / Services

- Validation explicite transcrite avec portée, date UTC et empreintes des valeurs dans l’annexe JSON ; lifecycle contrôlé.
- Définitions courtes Supply Order / Service Order, responsabilités et contrats entre modèles validés ; granularité DDD ouverte.
- Feuille de route, glossaire, analyse et AGENTS.md actualisés. Aucun ajout de capacité ou d’objet actif ; aucune publication.


## 2026-09-14 — U170 : nom et définition de l’univers amont

- Proposition utilisateur Processus métier conservée ; Business Processes en instruction, distingué du rôle métier de l’univers.
- Définition et frontière amont proposées dans l’annexe JSON ; analyse et AGENTS.md actualisés.
- Aucun renommage actif ni publication.


## 2026-09-14 — U171 : offre métier et Case Management

- Précision utilisateur enregistrée : processus moyens/longs impactant l’entreprise, offre aux parties prenantes externes et internes.
- Business Services proposé pour l’univers amont ; distinctions offre/processus/plateforme et services d’exécution consignées.
- Annexe JSON, analyse, glossaire et AGENTS.md actualisés ; aucun renommage actif ni publication.


## 2026-09-14 — U172 : grands processus transverses

- Besoins utilisateur conservés : portail, espaces, demandes et coordination multi-services.
- Définition de travail de l’univers amont précisée ; frontières affectation/planification versus Supply consignées.
- Annexe JSON, analyse et AGENTS.md actualisés ; aucun renommage, ajout de capacité, développement de portail ou publication.


## 2026-09-14 — U173 : adoption de Business Services

- Univers universe-case renommé Business Services, révision 2, nom et définition validés avec empreintes ; état antérieur conservé dans history/pre-U173.json.
- Quatre dimensions de périmètre validées dans l’annexe JSON ; domaines explicitement différés.
- Feuille de route, analyse, glossaire et AGENTS.md actualisés ; aucune capacité ajoutée ni publication.


## 2026-09-14 — U174 : clôture du point 6, reprise du point 5

- Clôture utilisateur consignée ; états de travail des annexes actualisés.
- Proposition de sens contextualisé Resource et exemples de fermeté documentés dans l’annexe de vocabulaire et le glossaire.
- Aucun changement des capacités actives ni publication.


## 2026-09-14 — U175 : biens stockés et transportés

- Apport utilisateur conservé : ressource générique contextualisée et priorité à la question stock/mouvement.
- Distinction proposée entre continuité des biens, position de stock et acheminement ; appuis GS1/SAP et exemple de non-double-comptage consignés.
- Annexe JSON, glossaire, étude et AGENTS.md actualisés ; aucun objet, capacité ou publication ajouté.


## 2026-09-14 — U176 : audit article, SKU, biens et colis

- Dix-sept sources SAP, Microsoft et GS1 comparées ; distinction D365 SCM / Business Central et particularités Retail conservées.
- Conclusion : article et unité logistique distincts ; SKU comme pièce physique insécable non généralisable. Sept concepts et sept constats structurés, cinq épreuves illustratives et cinq impacts sur le projet.
- Relecture ciblée SAP et Microsoft effectuée ; nuances intégrées sur Product/famille, type d’emballage, HU et stockkeeping unit.
- Étude, sources JSON, annexe de résultats, glossaire, C87 et AGENTS.md actualisés. Aucune modification de modèle actif ou de release.


## 2026-09-14 — U177 à U179 : Retail et wholesale chez SAP

Clarification sourcée du nom sectoriel Retail, du périmètre Fashion et des usages wholesale des articles structurés. Complément Markdown/JSON dans l’audit U176, C88 ; aucune modification de carte ni publication.


## 2026-09-14 — U181 : définition explicite SAP Article

Comparaison dictionnaire/SAP et correction C89 : ajout de la définition officielle omise dans la synthèse initiale, conservation de la tension avec génériques et ensembles. Audit, annexe JSON, glossaire et AGENTS.md actualisés. Carte active et release inchangées.


## 2026-09-14 — U185 : correspondances Microsoft et univers/domaines

Analyse des niveaux et périmètres Microsoft ; recouvrements proposés avec le backlog. Différences explicites pour workflows, exécution logistique et maîtrise des références. Markdown sourcé et JSON de comparaison ; carte active inchangée.


## 2026-09-14 — U187 : stock unifié et conditionnements inbound/outbound

Orientation utilisateur enregistrée ; proposition structurée de contenus, regroupements et faits, avec exemple de reconditionnement et points de vue du transfert. Glossaire, feuille de route et AGENTS.md précisés. Carte active et release inchangées.


## 2026-09-14 — U188 : conditionnement pendant le stockage et au packing

Complément U187 : stockage reconditionné et containers outbound créés à la volée. Exemple et propositions JSON actualisés ; distinction prévu/constaté et périmètre d’exécution conservés. Aucune instanciation dans la carte active ni publication.


## 2026-09-14 — U189 : packing contractuel dans la promesse

Exigence ATP B2B enregistrée ; distinction exigences/faisabilité/containers constatés et rôles proposés D11/D04/D06/D03/D07. Annexes JSON, analyse, glossaire et AGENTS.md actualisés. Pas de nouvelle capacité, modification de carte ou publication.


## 2026-09-14 — U190 : références et unités concrètes

Proposition utilisateur enregistrée ; grain Article/Product Unit à clarifier, référence de contenant et occurrence distinguées. Vérification GS1 des niveaux d’identification. Exploration ciblée des objets ouverte dans la feuille de route ; propositions dans l’annexe, sans nouveau nœud actif ou publication.


## 2026-09-14 — U191/U192 : identité propre de l’exemplaire

Clarification du grain Article/Product Unit comme exemplaire physique et accord sur l’indépendance du code-barres. Alternatives antérieures conservées en historique ; question résolue dans l’annexe, le glossaire, la feuille de route et AGENTS.md. Les autres détails restent en instruction ; carte active et release inchangées.


## 2026-09-14 — U193 : variante commerciale et identification de l’exemplaire

Contribution enregistrée ; Product Variant ajouté à l’exploration structurée, Serial Number éventuel distingué du GTIN et de son support. Sources GS1 vérifiées pour la série et les niveaux de conditionnement. Glossaire, feuille de route et règles actualisés ; carte active et release inchangées.


## 2026-09-14 — U194 : contenant comme produit et rôle de contenance

Hypothèse utilisateur enregistrée et confrontée aux Packaging Materials et Handling Units SAP. Alternative structurée : références communes, rôle de contenant et composition datée, distinction support/regroupement et contraintes physiques/contextuelles. Glossaire complété ; carte active et release inchangées.


## 2026-09-14 — U195 : rôles Article et Container validés

Principe utilisateur retenu et tracé dans l’annexe JSON : Product commun portant un rôle Article ou Container. Interprétations antérieures archivées dans l’annexe ; glossaire, feuille de route et AGENTS.md alignés. Définitions détaillées et multiplicité restent en instruction ; aucune publication.


## 2026-09-14 — U196 : références au glossaire dans les textes

Faisabilité examinée à partir du schéma actif et du registre documentaire. Proposition JSON préparée : texte segmenté, term_ref stable, glossaire de publication et vérification des liens. Migration et rendu Atlas décrits, pas encore implémentés ; aucune release.


## 2026-09-14 — U197 : syntaxe légère de liens au glossaire

Proposition de segments remplacée par des chaînes avec liens `[texte](glossary:ID)`, après préférence explicite pour la lisibilité humaine. Ancien contrat conservé en historique, règles alignées dans AGENTS.md. Aucun changement du schéma actif, d’Atlas ou de release.


## 2026-09-14 — U198 : alternative YAML pour la rédaction

Alternative consignée dans l’étude des références au glossaire : distinguer syntaxe des liens et format de sérialisation. Direction possible backlog YAML / publication JSON générée, sans deux autorités éditables. Aucun changement de format décidé ou réalisé.


## 2026-09-14 — U202 : audit du vocabulaire puis refactoring YAML

Audit enregistré avant application : huit constats, dix nœuds précisés et principes CTP/Business Services actualisés. Les 34 capacités et la structure restent conservées. Les reformulations de définition sont proposées ; aucun accord métier étendu. Capture et rapport dans `audits/2026-09-14-glossaire-yaml/`.

Conversion de dix documents courants du backlog en YAML, contrôlée par égalité des valeurs décodées. Nouvelles publications métier et descripteurs en YAML ; API JSON via lecteur commun. Captures historiques, preuves et publications antérieures intactes, dont v003 toujours active. Schémas/manifestes/index techniques restent JSON. Les deux captures historiques de backlog liées aux migrations et au panorama restent JSON.

Guides, lanceur, scripts, lecteurs Node et sources de skills actualisés. Skills release/server-admin synchronisés. Les liens au glossaire restent une évolution distincte, non implémentée. Le rapport de préparation repère des portées lifecycle à rapprocher des décisions ADOPT avant prochaine publication ; cette situation existait avant l’audit et reste explicitement bloquante, sans suppression des accords du backlog.


## 2026-09-14 — U203 : Glossaire et liens dans Atlas

Page Glossaire et recherche ajoutées. Liens explicites vers terme ou élément, descriptions au survol/focus, clic et ancres conservant la publication ; références absentes signalées. Catalogue de travail dans `modeles/backlog/glossary.yaml`, 93 termes dont 81 repères historiques préservés et 12 notions récentes. Le workflow fige et versionne le catalogue et ses termes ; le rapport relève les impacts lexicaux. Voir `audits/2026-09-14-glossaire-atlas/bilan.md`. v003 reste la publication courante, sans glossaire ; aucune release métier, aucun commit ni push.


## 2026-09-14 — U204 : publication v004

Publication locale `2026-09-14.1`, descripteur `urbanisation-v004-2026-09-14-145044.yaml`, activée dans Atlas. 48 nœuds, 34 capacités, 47 relations, 93 termes de glossaire. D02 retiré sans renumérotation, D03 recomposé, Business Services et audit de vocabulaire intégrés. 17 transcriptions d’accords existants après réconciliation, sans nouvelle validation métier des formulations proposées. Validateur corrigé pour les univers intégralement validés ; 79 tests du modèle réussis. Historiques inchangés, restitutions régénérées. Voir `audits/2026-09-14-release-v004/bilan.md`. Aucun commit ni push.


## 2026-09-15 — U205 : capacités accessibles depuis la vue Univers

Chaque carte de domaine affiche les liens de ses capacités, avec icônes, aperçus au survol/focus et ouverture directe de la fiche dans la même publication. Les rattachements explicites restent l’autorité, notamment D02.b/c dans D01 et D02.e dans D03. Les groupes de présentation restent distincts.

Les hauteurs mesurées évitent de couper les listes et la grille passe de une à trois colonnes selon l’espace disponible. La page peut défiler à la molette et au toucher ; le raccourci de recherche reste disponible depuis les liens. Compilation TypeScript/Vite et 33 tests unitaires réussis, parcours navigateur existants vérifiés, intégrité du modèle contrôlée sans erreur. Les liens, aperçus, clics/clavier et historiques v004/v003 ont été vérifiés dans le scénario ciblé `app/verify-universe.mjs`. Le geste tactile a été confirmé séparément après stabilisation de la capture mobile : défilement de 335 px sans déplacer le graphe, puis ouverture directe de D07.d. Captures et résultats dans `app/.runtime/qa-universe/` ; pas de nouvelle exécution intégrale après l’ajustement de synchronisation du test tactile.

Contribution et index de provenance courant actualisés. Le serveur sert l’interface recompilée ; un rechargement de page l’installe. Modèles, publications et preuves figées inchangés ; aucun commit ni push.


## 2026-09-15 — U206 : capacités dans les cartes de référentiels

La carte Business References affiche les capacités des cinq référentiels sous forme de liens directs, avec les mêmes icônes, aperçus et dimensions adaptées que les domaines. Le comportement commun se fonde sur les types `domain`/`reference` et leurs rattachements publiés ; la navigation et le rôle de présentation de Business References sont conservés.

Compilation TypeScript/Vite et 33 tests unitaires réussis. Le scénario ciblé `app/verify-references.mjs` passe : contenus et liens exacts en v004/v003, clic/Entrée vers la fiche de la même publication, affichages desktop/mobile sans débordement. Cinq contrôles, aucune erreur navigateur ; captures et rapport dans `app/.runtime/qa-references/`. Contribution et provenance courante actualisées, validation des modèles sans erreur. Interface recompilée servie localement ; modèles publiés inchangés, aucun commit ni push.


## 2026-09-15 — U207 : proposition graphique issue du template FLOW

Template PowerPoint inspecté et ses quatre diapositives rendues. Logos FLOW et Groupe Beaumanoir extraits en PNG sans transformation, avec empreintes et script d’extraction dans `prototypes/atlas-identite-flow/`. Palette des formes de masque distinguée du thème Office et des guides : vert profond, menthe, lavande, sable, pêche et blanc cassé. Sources OOXML, opacités et usages proposés documentés.

Aperçu indépendant sur 5174, fondé sur les composants et API réels d’Atlas : en-tête clair avec les logos, couleurs FLOW, comparaison Actuel/FLOW et panneau de palette avec téléchargement des originaux. Emblème FLOW cadré uniquement en CSS pour l’en-tête. Les parcours et statuts métier sont conservés ; cette identité reste une proposition. L’application courante sur 8765 et ses fichiers compilés ne sont pas remplacés.

Compilation de l’aperçu réussie, captures Univers/référentiels/fiche/mobile et palette inspectées. Les contrôles et passages navigateur sont consignés dans `app/.runtime/branding/`. Sources courantes actualisées, validation des modèles sans erreur ; aucune modification des modèles publiés, aucun commit ni push.


## 2026-09-15 — U208 : identité FLOW intégrée à Atlas

Le Go de Laurent adopte l’aperçu U207. Atlas possède désormais un en-tête clair avec l’emblème FLOW et le logo Groupe Beaumanoir, les couleurs du template, des surfaces pastel et les polices Aptos/Aptos Display avec repli local. Images directement dans les composants React, palette et adaptations dans `app/src/brand.css` ; aucun portail ni comparateur de prototype dans l’application. Le favicon et le manifeste reprennent FLOW. Les deux PNG de `app/public/assets/` conservent les octets des médias du PowerPoint ; empreintes, palette et règles de maintenance dans `app/BRANDING.md`.

Compilation TypeScript/Vite et 33 tests Node réussis. Contrôle Python du serveur réussi ; 22 tests de données exécutés, dont deux ignorés par le scénario existant. Vérification sur le serveur réel 8765 : PNG servis à l’identique, vue Univers vers fiche avec publication conservée, cinq référentiels et leurs capacités, tiroir mobile et absence de débordement de l’en-tête de 320 à 768 px. Captures ordinateur, fiche, référentiels et mobile inspectées ; rapport dans `app/.runtime/branding/integrated-checks.json`, sans erreur navigateur ou HTTP. Le scénario `verify-references.mjs` valide aussi les liens au clic/clavier et la publication historique v003.

L’index de provenance courant est actualisé à 1080 sources ; `validate_models.py` termine sans erreur et la régénération des restitutions ne produit aucun changement. Le scénario navigateur général utilise désormais le même délai de 30 secondes que les contrôles ciblés : deux passages avaient atteint 15 secondes pendant un chargement de publication, sans erreur JavaScript, console ou HTTP ; une lecture de l’API historique a été mesurée à 7,8 secondes sur ce poste.

Le passage complet de `verify-browser.mjs` réussit ensuite ses dix contrôles : cartes et anciens liens, recherche et filtres, sources, publications historiques, relation transversale et rafraîchissement automatique avec reprise après échec simulé. Rapport du 15 septembre à 09:16:22 UTC dans `app/.runtime/qa-react/browser-results.json`, sans erreur JavaScript, console, requête ou HTTP.

Atlas sert l’interface recompilée sur 8765. Le serveur Node temporaire de l’aperçu est arrêté ; le dossier U207 documente désormais son statut historique. L’habillage ne modifie pas les modèles publiés ni leurs validations. Aucun commit ni push.


## 2026-09-15 — U209 : référentiels visibles dans la carte Business References de Supply

La carte de présentation était exclue des listes internes, réservées aux capacités des domaines et référentiels. Le composant partage désormais une liste typée : « Capacités » dans les domaines et référentiels, « Référentiels » dans les groupes de présentation présentant des références. Les groupes des publications existantes sans `group_role` sont traités comme dans le reste d’Atlas ; aucun niveau d’urbanisme n’est déduit ou ajouté.

Business References affiche les cinq références de la publication consultée, depuis les relations structurelles explicites. Icônes, infobulles et liens directs ouvrent leur fiche dans le même snapshot. Les hauteurs mesurées, les cartes responsives et le défilement tactile s’appliquent aussi à cette liste. Les styles partagés sont renommés pour distinguer une liste d’enfants de son type métier ; le pied de carte parle désormais de liens vers les fiches.

Compilation TypeScript/Vite et 33 tests Node réussis. La contribution U209 porte l’index courant à 1081 sources ; validation des modèles sans erreur. Aucune modification du modèle publié, aucune release métier, aucun commit ni push.

Le scénario `app/verify-universe.mjs` réussit ses sept contrôles sur le build final : données courantes/v003, cinq référentiels avec aperçu et accès au clic/Entrée, retour navigateur, capacités déjà affichées et mobile tactile. Les liens restent dans leur carte sans troncature ni débordement ; le dernier référentiel est accessible après défilement. Aucune erreur navigateur. Rapport et captures dans `app/.runtime/qa-universe/`, dont `supply-business-references.png` pour le rendu inspecté. Atlas sert cette correction sur 8765 ; recharger la page pour utiliser le nouveau bundle.


## 2026-09-15 — U210 : abstraction d’Order Management et comparaison au marché

Laurent demande la comparaison Microsoft/SAP/« ITM » et critique le caractère abstrait de D04. IBM est utilisé comme hypothèse explicitée, clarification demandée. Lecture du backlog et comparaison des champs D04/D04.e–h avec v004 : identiques. La note [Order Management : rendre les responsabilités concrètes](marche/order-management-abstraction-comparaison.md) distingue catalogue de processus Microsoft, définition SAP RBA citée, modèle historique IBM CBM et documentation produit Sterling.

Les apports concrets portent sur commande/ligne/échéancier, blocages, annulations partielles, modifications autorisées et reliquats. Proposition : enrichir et éprouver les quatre capacités existantes, sans réintroduire Order Qualification ni transformer chaque opération de produit en capacité. Illustrations et scénarios explicitement proposés ; frontières Case/Order, D03/D04/D07 et références conservées. Sources officielles et limites d’accès documentées. Aucun changement de modèle, de validation, de publication ou d’Atlas.


## 2026-09-15 — U211 : types d’Orders et pilotage de leur cycle opérationnel

Laurent précise rechercher les types d’Orders Supply et les aptitudes de lancement, mise en attente, report, etc. La [note dédiée](marche/order-types-et-cycle-de-vie.md) repart du YAML courant et de la frontière Supply Order / Service Order U169. Elle distingue les familles vente/achat/transfert/retour, les documents d’exécution propres aux services, puis affermissement, libération, blocage/reprise, report, révision, annulation et clôture. Les fonctions produit Microsoft servent de preuves concrètes, avec recherche parallèle complémentaire ; elles ne deviennent pas des capacités métier par simple traduction.

Order Lifecycle Management est une possibilité de regroupement proposée, non adoptée. Le report doit distinguer date demandée, promesse et plan de prestation ; Order Prioritization reste en D03. Aucun type, nœud, objet, cycle universel, domaine Services ou rattachement ajouté. Contribution et provenance courante actualisées, sans changement de modèle ou publication.

## 2026-09-15 — U212–U215 : refonte D04 et descriptions concrètes

U214 autorise le remplacement des quatre capacités communes par cinq capacités par type d’ordre et deux transversales. U215 demande de restituer le concret discuté. État antérieur capturé à l’identique dans `modeles/backlog/history/pre-U214.yaml` ; annexes avant modification et empreintes des publications dans `audits/2026-09-15-d04-refonte/`.

D04.i–o possèdent définitions, finalités et descriptions opérationnelles : split, regroupement, spread, affermissement, libération, attente/reprise, report/avance, annulation et clôture. Exemples par type et cas transfert 100/60/40 ; distinctions entre date demandée/promesse/plan de prestation, autorisation/réalisation et reliquats conservées. Noms et rattachements adoptés ; nouveaux textes détaillés proposés. Aucune validation ancienne transposée.

Sept rattachements remplacent les quatre antérieurs. Le lien D07.c → D04.h est archivé ; cinq contributions par type sont proposées, sans reprendre son identité. Glossaire complété de cinq sens proposés, candidats D03/D04 et feuille de route actualisés, Q077 partiellement répondue, C91 et correspondances marché consignées. Aucun modèle publié ni code Atlas modifié ; contrôles dans le bilan d’audit.


## 2026-09-15 — U216 : publication v005 / 2026-09-15.1

Publication locale du backlog après refonte D04, via prepare/report/publish et activation de l’index. 51 nœuds, 37 capacités, 54 relations et 98 termes de glossaire. Les quatre anciennes capacités D04.e–h sont retirées ; D04.i–o, cinq contributions d’exécution et cinq termes lexicaux sont intégrés avec leurs portées explicites.

48 décisions compatibles conservées, 15 transcriptions sourcées et cinq anciennes décisions non reprises sur cette version, conservées dans l’historique. Les nouvelles descriptions restent proposées ; aucune validation transférée depuis les capacités retirées. Les cinq alertes lexicales concernent les liens des nouvelles capacités vers les cinq nouveaux sens proposés ; examen cohérent, sans étendre les validations aux définitions.

Validation des modèles sans erreur, restitutions régénérées, contrôle serveur réussi. L’API de FLOW Atlas, PID 19836 sur 8765, sert le modèle YAML v005 et son catalogue ; les champs servis correspondent au modèle publié. Empreintes des 60 fichiers historiques vérifiées identiques ; seul l’index existant est activé. Contrôles navigateur et bilan dans `audits/2026-09-15-release-v005/`. Aucun commit ni push.

## 2026-09-15 — U217 : différence et recouvrement D05 / D03

Lecture des définitions courantes et réserves D05. La [note de comparaison](marche/operational-balancing-order-promising.md) distingue besoin/objectif de rééquilibrage et solution de couverture/promesse, sans séparation artificielle global/commande. Recouvrement principal D05.c avec CTP/Supply Assignment ; calcul des besoins nets également à clarifier. Exemple fictif de réassort, contraintes et frontières D04/D07 conservées. Analyse et recommandation proposées, aucun changement du backlog, de la release ou d’Atlas.

## 2026-09-15 — U218 : Orders dans D03, stock dans D05

Laurent précise la finalité respective des deux domaines : satisfaire les Orders pour D03, gérer le stock pour D05. Repère consigné dans l’annexe de revue D03 et en tête de la comparaison U217. La distinction besoin/solution ne suffit plus à définir la frontière. Les interprétations sur les objectifs et la répartition du stock, l’articulation D01/D05 et les capacités détaillées restent à éprouver. Aucun changement des nœuds du modèle ni de la release v005.

## 2026-09-15 — U219/U220/U221 : Inventory Optimization et réapprovisionnement automatique

U219 applique les finalités D01/D03/D05 ; U220 choisit Inventory Optimization pour D05, remplaçant Operational Resource Balancing et la proposition intermédiaire Inventory Balancing. Les trois capacités D05 conservent leurs identités et rattachements ; Coverage Target Decision et Stock Redistribution Decision deviennent leurs libellés proposés courants, Net Requirements Calculation est précisée autour du stock. Descriptions concrètes, frontières et exemples dans `connaissance/30-stock-et-orders.md`, issus du YAML.

U221 envisage le réapprovisionnement automatique : complément de stock et déclenchement selon règles/autorisations figurent dans le périmètre proposé de D05. Granularité à instruire, aucune capacité supplémentaire créée. TER074 Replenishment est ajouté comme sens proposé ; les 98 termes précédents sont inchangés. D04, D03, D01 et les exécutants conservent leurs rôles.

Snapshot pré-U219, portée des finalités adoptées et historique des noms dans `modeles/backlog/stock-order-boundary.yaml` et `audits/2026-09-15-stock-orders-U219/`. Six nœuds modifiés ; 37 capacités et toutes les relations conservées. Les nouvelles descriptions et règles restent proposées. Publication v005 inchangée, aucun commit ni push.


## 2026-09-15 — U222 : comparaison Inventory Optimization

Étude ciblée TM Forum, Microsoft Dynamics 365 SCM et SAP IBP/retail, sources officielles consultées. Sept éléments ELM115–ELM121 et cinq correspondances CMP067–CMP071 distinguent APIs, composants, méthode et fonctions de produit. MKT24 identifie le corpus IBP 2605. Objectifs, calcul net, réapprovisionnement et redistribution confrontés au backlog après U219–U221 ; accès indexés et limites explicites.

Replenishment Decision reste une piste ; aucun nœud ni glossaire modifié. Seuls les statuts de comparaison D05 et D05.a–c de l'annexe sont actualisés ; D01/D03 non réaudités. Étude dans marche/inventory-optimization-comparaison.md. Empreintes de lecture et invariance du modèle et des publications dans marche/etudes/2026-09-15-inventory-optimization/verification.yaml. Aucun commit, push ou publication.


## 2026-09-15 — U223 : définition Inventory Optimization adoptée

La phrase approuvée par Laurent devient la définition D05 : compromis entre disponibilité, immobilisation et risque, puis décision des ajustements nécessaires. Majuscule initiale normalisée, contenu préservé. Portée de validation limitée à la définition, en complément du nom U220 et de la finalité U219. Ancienne rédaction conservée comme précision opérationnelle proposée et dans le snapshot pre-U223.yaml. Trois capacités inchangées ; Replenishment Decision reste candidate. Restitution, provenance et consignes actualisées ; aucune publication, aucun commit ni push.


## 2026-09-15 — U224 : optimisation analytique et application opérationnelle

Direction utilisateur consignée : D05 calcule l'optimisation ; protections, paramètres, déclenchement d'Orders et réapprovisionnement appliquent ses résultats. La candidate U222 mêlant calcul et déclenchement est à revoir. Propositions analytiques conservées dans l'annexe, sans adoption des noms ni modification des nœuds. Le périmètre actuel n'est pas présenté comme déjà aligné. Définition U223 conservée ; aucune publication.


## 2026-09-15 — U225 : comparaison calcul / application au marché

Documentation officielle Microsoft (buffers calculés/actifs, affermissement, allocations), SAP (IBP, SUP/PAL et aATP), légendes SID TM Forum v22.0. Sources datées et accès indexés qualifiés dans marche/optimisation-et-application-stock.md. Six éléments ELM122–ELM127, trois rapprochements CMP072–CMP074 proposés ; annexe de direction enrichie. Aucun nœud, relation, glossaire ni publication modifié. Contrôles de provenance et modèles effectués.


## 2026-09-16 — U226 : préférences de découpage optimisation / application

Préférence Microsoft pour le découpage et le nommage, distinction SAP planification / mise en action, détail analytique de Stock Protection conditionné à sa décomposition opérationnelle. Contribution exacte et direction conservées dans l'annexe stock-order-boundary.yaml ; étude U225 annotée. Pas de nouveaux noms adoptés ni de refonte des nœuds, aucune publication.


## 2026-09-16 — U227 : proposition de capacités concrètes

Proposition consignée dans stock-order-boundary.yaml : D05 à deux capacités de planification (Stock Protection Planning, Replenishment Planning), en regard de Stock Protection et d'une candidate Replenishment Management dans D01. Extension D01, renommage D02.b, intégration du calcul net et de la redistribution explicitement proposés, non appliqués. Rôles D03/D04/exécutants conservés. Aucun changement des nœuds ni publication.


## 2026-09-16 — U228/U229 : Decision et Planning distingués

U228 clarifie la restructuration proposée. U229 conserve Decision, écarte Calculation comme préférence de nommage et définit Planning par reconfigurer/simuler/valider, alimenté par les décisions. Proposition U227 annotée, noms corrigés proposés dans l'annexe sans adoption de granularité ni changement des nœuds. Aucune publication.


## 2026-09-16 — U230 : gouvernance de Stock Protection et décisions spécialisées

Qualification utilisateur Stock Protection = gouvernance/management, rejet du pendant agrégé Stock Protection Decision. Proposition revue à quatre décisions, avec redistribution conservée distincte et allocation aux groupes explicitée. Annexe et récit actualisés, anciennes propositions annotées. Noms et détails restent proposés ; nœuds, relations et publication inchangés.


## 2026-09-16 — U231 : application transactionnelle de Stock Protection

Sens utilisateur consigné : mise à jour transactionnelle des données à l'unité, par groupe ou en masse, via écrans, batch, flux ou streaming. Annexe et récit actualisés ; aucune nouvelle capacité, modification des nœuds, architecture technique ou publication.


## 2026-09-16 — U232 : glossaire de modélisation distinct

Création de modeles/backlog/modeling-glossary.yaml : MOD001 Decision, MOD002 Planning, MOD003 Management, MOD004 Application transactionnelle. Les portées utilisateur et généralisations proposées sont distinguées. Registre en support à la définition des objets, séparé de glossary.yaml et du catalogue métier Atlas ; guide, annexe et consignes actualisés. Les sens discutés n'étaient pas présents comme entrées homonymes dans le glossaire métier ; aucune migration globale des anciens termes réalisée. Lecture YAML et identifiants contrôlés ; modèle métier, glossaire métier et fichiers de release vérifiés inchangés. Aucune publication.


## 2026-09-16 — U233 : proposition D05 à quatre décisions et Inventory Planning

Proposition du domaine : définition U223 conservée, décisions de couverture/allocation/réapprovisionnement/redistribution et Inventory Planning qui les mobilise. Frontières avec le management transactionnel, les Orders et l'exécution explicitées ; calcul net conservé comme moyen. Cinq capacités et périmètres proposés, non appliqués. Glossaire de modélisation distinct et inchangé ; aucune publication.


## 2026-09-16 — U234/U235 : refonte D05 appliquée

Cinq capacités : Coverage Target Decision, Stock Allocation Decision, Replenishment Decision, Stock Redistribution Decision, Inventory Planning. D05.b retirée avec son rattachement et remplacée par D05.e, décision intégrant les calculs ; trois nouveaux identifiants, deux conservés. Quatre relations de mobilisation depuis Planning distinctes des cinq rattachements au domaine. Définition D05 U223 conservée, scope explicite aligné sur décision/Planning/management et mise en action.

Noms et définitions courtes repris à l’identique de la proposition validée ; compléments détaillés et exemples proposés. Descriptions actuelles dans connaissance/31-inventory-optimization.md ; anciennes discussions conservées. D01/D03/D04, autres nœuds, glossaires et publications inchangés. Contrôle documentaire Microsoft ciblé, CMP075 avec limites. Bilan et invariants dans audits/2026-09-16-d05-refonte/. Aucun commit, push ou publication.

## 2026-09-16 — Synthèse des principes structurants dans AGENTS.md

À la demande de Laurent (« Go pour ton optimisation de agents.md »), ajout en tête d'une synthèse des règles en vigueur : autorités, définition et hiérarchie du modèle, Decision/Planning/Management, frontières métier, validation et preuve, maintenance et Atlas. Liens vers les registres faisant autorité ; aucune nouvelle définition métier adoptée. Les sections antérieures sont conservées sous un repère explicite d'historique, avec une règle de lecture des états remplacés. Les futures évolutions doivent actualiser la synthèse concernée plutôt qu'ajouter seulement un nouveau jalon. Modèles, glossaires, application et publications inchangés.


## 2026-09-16 — Publication v006, U236

Publication 2026-09-16.1 activée : 53 nœuds, 39 capacités, 60 relations, 99 termes métier. Frontières D01/D03/D05 et refonte Inventory Optimization intégrées. TER074 corrigé avant préparation pour distinguer décision et mise en action ; définition proposée, état antérieur conservé dans l’audit. Glossaire de modélisation figé comme contexte séparé.

82 décisions : 62 reprises compatibles et 20 transcriptions sourcées ; une ancienne décision sur le nom D03 reste historique, avec transcription du seul nom inchangé après réexamen. Validation sans erreur, vues régénérées, serveur et données API concordants, parcours navigateur et glossaire vérifiés. 88 fichiers protégés inchangés. Bilan : audits/2026-09-16-release-v006/bilan.md. Aucun commit ni push.


## 2026-09-16 — U237 : offre de services et pilotage de l’exécution

Vision utilisateur consignée dans execution-services-review.yaml : référentiel des services exécutants, sollicitation/feedback et SLA de réalisation, domaine unique de pilotage. Noms, contenu détaillé et répartition Codex proposés. Ambiguïté D05/D06 versus D06/D07 signalée ; aucune modification du modèle avant clarification. Release v006 inchangée.


## 2026-09-16 — U238 : périmètre D06/D07 confirmé

Laurent confirme que la refonte concerne D06 et D07, avec D05 conservé. Annexe de discussion actualisée ; noms et capacités proposés restent à instruire. Aucun changement des nœuds ni publication.


## 2026-09-16 — U239 : challenge marché de l’exécution

Étude critique Microsoft/SAP/TM Forum dans marche/execution-services-catalog-and-management.md, ELM129–135 / CMP076. Offre et pilotage appuyés partiellement ; préservation recommandée de la qualification, de la capacité dynamique, des dépendances et des exceptions. SLA/engagement/estimation/résultat et métier/endpoint distingués. Portées de versions et limites des sources explicites. Recommandations proposées dans l’annexe, aucun nœud ou glossaire modifié, release v006 inchangée.


## 2026-09-16 — U240 : capacité contextuelle D06 et promesse D03

Accords enregistrés avec portées et empreintes dans execution-services-review.yaml. Référentiel = services/SLA globaux configurés ; D06 décrit la capacité opérationnelle logistique contextualisée, utilisée par D03 pour calculer sa promesse Supply. Coordination, distinctions des engagements, tracking logistique et séparation métier/accès adoptés dans la portée des cinq réponses. Noms et granularité détaillée proposés, autres services U237 conservés. Synthèse AGENTS et étude mises à jour ; modèle actif et release v006 inchangés.

## 2026-09-16 — U241 : comparaison du modèle d'exécution révisé

Comparaison des principes U240 avec Microsoft, SAP et TM Forum dans marche/execution-services-revised-comparison.md. ELM136/137 et CMP077 documentent CTP et la contribution PP/DS vers aATP. Appuis partiels, sans équivalence des domaines ni couverture installée. Questions proposées : disponibilité résiduelle, consommation/libération de capacité et réexamen de promesse. Accords U240 préservés à l'identique ; aucun nœud, relation, glossaire ou publication modifié.


## 2026-09-16 — U242 : orchestration et adaptation de l'exécution Supply

Contribution enregistrée et accords délimités/empreintés dans execution-services-review.yaml : orchestration, tracking, réaction aux échecs et recherche de variantes du plan ; retour vers D03 pour réexaminer la promesse. Proposition de définition actualisée avec état antérieur conservé. Frontières U240 inchangées ; détails d'autonomie et de réexamen ouverts, points 1/2 de U241 toujours proposés. Synthèse AGENTS, étude et CMP077 actualisées. Aucun nœud actif, relation, glossaire ou publication modifié.


## 2026-09-16 — U243 : latitude d'adaptation hors définition du catalogue

Correction de cadrage enregistrée : la latitude d'adaptation n'impacte pas le catalogue des capacités. Question déplacée vers les règles de fonctionnement dans execution-services-review.yaml, accord sourcé et empreinté. Synthèse AGENTS et étude actualisées ; accords U240/U242 inchangés. Aucun nœud, relation ou publication modifié.


## 2026-09-16 — U244 : refonte de l’exécution appliquée au backlog

D06 Execution Management regroupe les responsabilités D06/D07, ajoute Execution Orchestration et élargit D07.d en Execution Tracking avec conservation des résultats encore attendus. D14 Execution Service Catalog et son ingestion ajoutés. Les relations D03/capacité/révision et tracking/orchestration/options/engagements sont explicites ; cinq liens de rapprochement D04 préservés. D05 inchangé. Captures, portées et contrôles dans audits/2026-09-16-execution-refonte et execution-services-review.yaml. Noms et détails ajoutés proposés ; définition de domaine présentée avant U244 adoptée. TER075/076 proposés, glossaire de modélisation séparé inchangé. Aucune publication, commit ou push.


## 2026-09-16 — U245 : challenge du catalogue d'exécution

Séparation orchestration/adaptation et usage du vocabulaire de modélisation demandés. Explication de Qualification comme admissibilité du service ; fusion avec la décision de service proposée. Proposition de huit responsabilités dans execution-services-review.yaml, review_U245 : décisions de besoins, services, capacité et adaptation ; gestion des engagements, orchestration, tracking et rapprochement. Limites des responsabilités et portée Decision/Planning explicites. Noms, fusion et granularité proposés, nœuds actifs U244 et publications inchangés.


## 2026-09-16 — U246 : Capacity Visibility et clarification des engagements

Execution Capacity Visibility retenu comme nom dans le catalogue en discussion, portée et empreinte enregistrées. Proposition de description précisée sans validation implicite. Execution Commitment Management expliqué par la tenue des demandes, prises en charge et évolutions ; Service Order Management proposé comme nom plus concret et périmètre à discuter. Nœuds actifs U244 et publications inchangés.


## 2026-09-16 — U247 : catalogue d'exécution révisé appliqué

Service Order Management adopté avec sa définition présentée ; Capacity Visibility retenu selon U246. Orchestration et Adaptation Decision séparées. Requirements Decision détermine les prestations nécessaires ; tracking et rapprochement conservés. D06.e regroupe qualification/options comme proposition ; D06.a/c archivées, D06.f nouvel identifiant d'adaptation. Huit capacités directement rattachées à D06, liens actualisés et D03/D05 préservés. Portées dans application_U247 ; descriptions détaillées proposées. Deux glossaires et publications inchangés. Contrôles et captures dans audits/2026-09-16-execution-capacites. Aucun commit, push ni publication.


## 2026-09-16 — U248 : publication v007 de l'exécution

Publication 2026-09-16.2 activée : 55 nœuds, 41 capacités, 74 relations et 101 termes métier. D06 regroupe huit capacités ; D14 ajoute le sixième référentiel. Orchestration et Adaptation Decision sont distinctes ; Service Order Management et Capacity Visibility sont publiés avec leurs portées. La fusion des services et les compléments détaillés restent proposés.

96 décisions : 82 reprises compatibles et 14 transcriptions sourcées des accords récents ; aucune suspension. TER075/076 ajoutés comme propositions, 99 termes antérieurs inchangés et glossaire de modélisation figé comme contexte séparé. Validation sans erreur, restitutions régénérées, API identique au snapshot et interface Atlas vérifiée sur 8765. Anciennes publications et backlog inchangés ; seul l'index d'activation a évolué parmi les fichiers protégés. Bilan : audits/2026-09-16-release-v007/bilan.md. Aucun commit ni push.


## 2026-09-16 — U249 : audit de maturité du modèle

Audit de v007 et des champs courants identiques du backlog, sans modification du modèle. Rapport dans audits/2026-09-16-audit-maturite/ : grille des 41 capacités, comparaison de 29 sources Microsoft/SAP/Oracle/TM Forum, granularité, dépendances et huit compléments de description proposés. ELM138–157, CMP080–085 ; méthodes et limites d’accès explicites.

Constats : frontières principales cohérentes ; application des paramètres/mise en action D05 à attribuer ; rapprochement des représentations de stock et devenir des retours à instruire. 74 relations dont 53 structurelles/de présentation et 21 transversales ; 22 capacités sans lien transverse, dont les six ingestions. Descriptions : 15 périmètres, 21 exemples et 11 natures manquent ; six textes citent encore D07 comme domaine. Les natures de Lifecycle et des gestions sont à discuter, sans reclassification automatique ni fusion de choix adoptés.

La matrice proposée distingue besoins de résultats, flux et structure ; les scénarios préparatoires n’imposent pas un Order ou une promesse déjà confirmés. Les politiques actives restent distinctes des résultats candidats des décisions. Relecture indépendante effectuée. Empreintes de 153 fichiers contrôlées, modèle/backlog/glossaires/publications inchangés ; index de provenance courant actualisé séparément. Aucune validation métier, release, commit ou push.


## 2026-09-16 — U250 : frontières de CTP

Lecture comparée des définitions courantes D03/D05/D06 après l’audit. Risque de recouvrement de CTP avec priorisation, échéancier, arbitrage économique, politiques de stock et choix de services ; proposition de distinguer sa réponse de faisabilité sous adaptation des résultats spécialisés mobilisés. Approvisionnement/transfert pour honorer un Order et optimisation du stock gardent des finalités distinctes. Question et analyse sans modification du modèle ni adoption de la reformulation proposée.


## 2026-09-16 — U251 : CTP et décisions spécialisées

Définition de D03.j remplacée par la formulation adoptée de faisabilité après adaptation ; nom, finalité et nature inchangés de U154 conservés. Scope concret et exemple ajoutés comme propositions, six relations conditionnelles consommateur→fournisseur, sans nouveau type ni hiérarchie. Les autres capacités et relations antérieures restent inchangées. Accord et empreintes dans d03-review.yaml, ctp_boundaries_U251 ; historique pre-U251.yaml et captures dans audits/2026-09-16-ctp-frontieres/.

Principe to-promise et synthèse AGENTS alignés ; TER045 actualisé comme reprise lexicale proposée, glossaire de modélisation inchangé. CMP086 actualise les appuis U249 sans nouvelle équivalence ou recherche revendiquée. Aucune application globale de l’audit, publication, commit ou push.


## 2026-09-16 — U252 : proposition de traitement des manques

Proposition en discussion : élargir la gestion des protections à Inventory Policy Management dans D01 (renommage/extension de D02.b proposé), attribuer explicitement la création/modification des Orders issus de D05 aux gestions achat/transfert D04, et examiner deux capacités D01 : Inventory Reconciliation (rapprochement des représentations) et Stock Disposition Decision (devenir/usages des biens après constat). Contrôle physique chez l’exécutant ; optimisation du stock souhaitable dans D05 ; promesse dans D03. Aucun nom ou périmètre adopté par la question, aucun nœud modifié.


## 2026-09-16 — U253 : Supply Protection conservé

Laurent estime Supply Protection plus large qu’Inventory Policy Management. Retrait du renommage/élargissement proposé U252 : une finalité de protection des possibilités Supply ne se réduit pas à la gestion des paramètres de stock. Nom actif inchangé ; périmètre détaillé et portage des paramètres à clarifier. Aucun élargissement automatique à toutes les ressources logistiques, aucune adoption des autres candidats U252 et aucune modification du modèle.


## 2026-09-16 — U254 : intention et niveau de Supply Protection

Question sur la nature de Supply Protection. Distinguer le résultat étroit de D02.b (tenir les quantités/limites d’usage par groupes) de l’intention transverse de protection, élargie dans la discussion précédente. Un domaine éventuel doit se justifier par un espace cohérent de problèmes ; aucun nouveau domaine ou renommage adopté. Modèle inchangé.


## 2026-09-16 — U255 : recouvrement allocation et affectation

Le rapprochement signalé par Laurent conduit à retirer le candidat Supply Allocation Management. Distinguer dans l’analyse les droits d’usage collectifs, les liens de couverture à des besoins identifiés et les engagements opposables aux usages concurrents ; ces résultats ne préjugent pas de trois capacités. Réexaminer ensemble Supply Protection, Supply Assignment et Reservation avant renommage ou regroupement. Aucune modification du catalogue ni publication.


## 2026-09-16 — U256 : complétude des décisions protection/affectation

Analyse de onze questions/cas sur le backlog après U251, rapprochée de l’historique pré-U154. Sept responsabilités de décision présentes ; choix détaillé de couverture et substitution à expliciter dans ATP/CTP/PTP ; dérogation ponctuelle de protection sans porteur attribué ; contrat de cycle affectation/engagement/libération à préciser. Les cas fins ne sont pas automatiquement des capacités autonomes. Rapport dans audits/2026-09-16-decisions-protection-assignment/rapport.md. Aucun nouveau nœud, renommage, fusion Reservation ou publication.


## 2026-09-16 — U257/U258 : aptitude et granularité d’ATP/CTP/PTP

Examen conceptuel demandé : les définitions courantes expriment des aptitudes de décision avec résultats distincts (faisabilité de référence, possibilités sous adaptation, sélection économique). La maille agrégée ne retire pas leur statut de capacité ; identifier des questions plus fines ne crée pas automatiquement des sous-capacités. Poursuivre la clarification des contrats et du choix de couverture sans modifier le catalogue ou les accords U154/U251.


## 2026-09-16 — U259 : méthode de clarification des décisions

Programme proposé à partir des 13 capacités marquées decision : revue conjointe D03, puis D05/D06 et nature/contrat de Lifecycle. Périmètres par question, contraintes, résultat, frontières et exemples ; premier cas disponibilité locale/apport alternatif/échéancier avec distinction date impérative/préférée. Périmètre détaillé d’ATP et responsabilité du choix de couverture à instruire ; catalogue et publications inchangés.


## 2026-09-16 — U260 : couverture et exploration ATP/aATP

Contribution conservée avant reformulation. Ajout de MOD005 dans le glossaire méthodologique séparé, précision TER022, contexte TER044 et nouveau TER077 Couverture de stock. Les formulations restent proposées ; accord de principe ATP limité à la couverture explicative, tracé dans d03-review.yaml. Catalogue et définition D03.i inchangés.

Recherche officielle APICS/Microsoft/SAP : étude marche/atp-aatp-couverture.md, ELM158–162 et CMP087 proposés. aATP recouvre plusieurs responsabilités FLOW ; pas de nouvelle capacité ni de frontières éditeur adoptées. Synthèse AGENTS actualisée. États antérieurs et empreintes dans audits/2026-09-16-atp-aatp-couverture/. Aucun commit, push ou publication.


## 2026-09-17 — U261 : ATP, variantes et niveaux de description

Verbatim conservé avant interprétation. Les quatre informations ATP et le cas d’une promesse ou d’un ensemble sont consignés dans d03-review.yaml ; pas de nouvelle définition adoptée par extension.

Étude marché marche/capacites-variantes-niveaux-atp.md : décomposition, comportement/variante, réalisation et maturité distingués. Proposition de dimensions combinables et profils contextualisés ; aucun niveau supplémentaire adopté. MKT25/26, ELM163–165, ELM052 reconsulté, CMP088 proposé. Catalogue, glossaires et publications inchangés ; pas de release, commit ou push.


## 2026-09-17 — U262 : Comportement, niveau terminal

Choix de Laurent consigné : Capacité → Comportement, arrêt de la décomposition à ce niveau. Glossaire méthodologique MOD006, feuille de route, revue D03 et synthèse AGENTS actualisés. Recommandation de variantes/profils U261 explicitement remplacée ; historique conservé. Quatre exemples ATP proposés, sans les présenter comme adoptés.

Cette étape applique la convention de modélisation ; nouveaux nœuds, schéma et Atlas ne sont pas encore implémentés. Catalogue des capacités et glossaire métier inchangés ; aucune release, aucun commit ni push.


## 2026-09-17 — U263 : définitions des comportements ATP adoptées

Laurent valide les quatre définitions et exige un vocabulaire factuel, sans niveau marketing Advanced ATP. Valeurs et empreintes dans d03-review.yaml.atp_behaviors_U263 ; noms de présentation français conservés, noms anglais non adoptés. MOD006, synthèse AGENTS et feuille de route actualisés. Catalogue principal et publication inchangés ; comportements documentés, représentation technique encore à réaliser.


## 2026-09-17 — U264 : modèle et Atlas implémentent les comportements

Type behavior et contrat de rattachement terminal validés côté Python et adaptateur Atlas. Quatre nœuds BHV001–BHV004 et quatre relations contains pour ATP, dont les définitions adoptées U263 gardent leurs empreintes. ATP et TER044 actualisés ; synthèse, noms anglais et périmètres éditoriaux restent proposés. Catalogue de 41 capacités conservé, quatre comportements distincts.

Atlas : arbre, fiches détaillées, descriptions directement dans ATP, recherche/filtre, icônes, compteurs et liens des cartes. Restitution Markdown dérivée étendue. Tests de mutation et navigation ajoutés. Le fixture historique des tests de préparation utilise désormais un glossaire figé compatible au lieu du glossaire vivant, qui référençait des éléments absents de son ancien modèle. Bilan et preuves dans audits/2026-09-17-comportements-atlas/. Aucune release, aucun commit ni push.


## 2026-09-17 — U265/U266 : audit des comportements et plan en deux parties

41 capacités et quatre comportements relus ; comparaison primaire Microsoft, SAP, Oracle, TM Forum, BIZBOK et LeanIX. Audit, matrice et plan dans audits/2026-09-17-audit-comportements/ ; propositions distinctes dans behavior-audit.yaml, CMP089. Recommandation : conserver une profondeur terminale Capacité → Comportement, décomposer sélectivement ; Promise Management et Reservation/Assignment demandent arbitrage.

AGENTS consolidé par priorités ; version antérieure complète préservée. Six références de domaines D07 corrigées vers D06 dans des scopes proposés ; identifiants conservés. Limitations historiques du modèle renvoyées à la capture, principes métier conservés. Principe U265 de justification ajouté, champ decomposition_rationale et contrôle non rétroactif ; justification ATP proposée, visible dans les restitutions et fiches Atlas. Les champs adoptés restent inchangés. Aucune fusion ni rétrogradation, aucune nouvelle relation métier, release, commit ou push.


## 2026-09-17 — U267 : comportements du scénario

Proposition de Laurent consignée avant interprétation : construction, simulation, comparaison/évaluation, validation, application. Réponse détaillée et bénéfices dans audits/2026-09-17-audit-comportements/scenario-planning-proposition.md ; suivi dans behavior-audit.yaml et note MOD002. Noms anglais, résultats détaillés et responsabilité d’application proposés. Catalogue et publications inchangés.


## 2026-09-17 — U268 : comparaison et justification systématiques

Règle utilisateur inscrite dans AGENTS.md et marche/methode.md. Reprise de la proposition U267 avec comparaison primaire SAP IBP, Microsoft SCM et Oracle Supply Planning. ELM173/174, CMP090 ; distinction entre promotion des données du scénario et déclenchement de recommandations opérationnelles. Recommandation de cinq comportements justifiée ; mandat d’application en D05.f toujours à arbitrer. Aucun changement du catalogue ou des publications.


## 2026-09-17 — U269 : cinq comportements Inventory Planning adoptés

U269 enregistré puis appliqué : BHV005–BHV009 et cinq rattachements terminaux à D05.f. Noms anglais, descriptions courtes et justification du découpage adoptés ; scopes/exemples ajoutés proposés. L’application sollicite les capacités opérationnelles responsables. Synthèse D05.f et périmètre D05 alignés ; ancienne définition U235 historisée sans transport de validation. MOD002, annexe D05, suivi d’audit et CMP090 actualisés. Catalogue de 41 capacités conservé ; neuf comportements. Aucune release, aucun commit ou push.


## 2026-09-17 — U270 : analyse d’impact en indicateurs

Apport utilisateur enregistré ; comparaison SAP IBP (simulation, Inventory Analysis, Scorecard, Service Level Prediction), contrôle complémentaire Oracle. ELM175/CMP091, accès et limites documentés. Proposition Scenario Impact Analysis avec justification ciblée et frontières à préciser vis-à-vis de Simulation/Evaluation pour éviter les doublons. Reconnaissance du comportement complémentaire consignée ; nom anglais, définition détaillée et reformulations non adoptés. Les cinq comportements U269, leurs valeurs et le catalogue actif restent inchangés.


## 2026-09-17 — U271 : Scenario Impact Analysis adopté

BHV010 ajouté sous Inventory Planning, avec nom, définition et rattachement adoptés. Définitions BHV006/BHV007 précisées par les résultats du tableau accepté ; valeurs U269 conservées dans la capture pré-U271 et le registre historique. Compléments de périmètre proposés. Six comportements Planning et quatre ATP, sans nouvelle capacité. Justification et frontières consignées, glossaire méthodologique et suivi d’audit alignés. Aucune release, aucun commit ni push.


## 2026-09-17 — U280/U281 : étude marché étendue de Supply Protection

Neuf éditeurs et 17 sources primaires retenus ; profondeur et limites d’accès distinguées. Liste proposée de 17 comportements (cinq existants, dix compléments, deux conditionnels) dans supply-protection-review.yaml, restituée dans marche/supply-protection-comportements.md. MKT27–32, ELM177–186 et CMP093 ajoutés. Recommandations sourcées et justifiées par bénéfice ou complexité ; frontières avec D03/D05/exécution conservées. Aucun nœud, glossaire ou fichier de publication modifié. U281 valide la méthode d’étude, pas la nouvelle liste.


## 2026-09-17 — U282 : recentrage des comportements sur les mécanismes métier

Correction utilisateur enregistrée. AGENTS et MOD006 précisés ; D02.b et BHV011–015 placés en réexamen sans changer leurs valeurs historiques ni identifiants. L’étude de 17 opérations est signalée comme matière fonctionnelle historique, plus comme cible recommandée. Sources et accords préservés ; nouveau catalogue de mécanismes à proposer. Aucune publication ni modification des comportements ATP/Planning.


## 2026-09-17 — U283 : critères de comportement et Planning

Apport enregistré avant interprétation. AGENTS et glossaire méthodologique précisés ; direction Planning consignée dans les annexes. D05.f et ses six comportements marqués en réexamen ; requalification fonctionnelle BHV007–010 tracée. Aucun nom, définition adoptée, identifiant ou lien supprimé ; migration cible à préciser. Comparaison Kinaxis ELM187/CMP094, sans équivalence normative. Aucune publication.


## 2026-09-17 — U284 : Simulation & analyse

Accord et précision enregistrés. Direction Planning, glossaire méthodologique, AGENTS et notes de réexamen actualisés : simulation et analyse réunies. Comparaison Kinaxis documentée dans ELM187/CMP094. Valeurs historiques des nœuds et accords conservés ; migration du catalogue toujours distincte de cette clarification. Aucune publication.


## 2026-09-17 — U285 : diagnostic de refonte du modèle

Demande enregistrée ; diagnostic et plan proposés dans behavior-audit.yaml. Revue exhaustive recommandée des 41 capacités ; 15 comportements existants dont 11 directement concernés par les corrections Planning/Protection. Les anciens critères de découpage ne sont plus repris sans examen. Aucun changement de responsabilité, fusion, suppression ou publication effectué par ce diagnostic.


## 2026-09-17 — U286 : cible complète préparée

Revue des 41 capacités, migration des 15 comportements et inventaire de toutes les relations. Proposition de quatre mécanismes Protection, trois Planning et maintien des quatre ATP ; Stocktaking et Orchestration conditionnels. Sept arbitrages regroupés. Consignes obsolètes corrigées ; ancien audit conservé en historique, cible référencée depuis AGENTS. Catalogue actif et accords inchangés. Comparaison CMP095. Aucune publication ou administration serveur.


## 2026-09-17 — U287 : application de plan dans D04

Orientation reçue pendant la préparation U286 et intégrée à la cible : mécanisme d’application du scénario/plan par Order Management. Définition et cas proposés, parent précis à arbitrer A8 ; frontières quotas/Orders/prestations explicitées. Sources Microsoft/Oracle S13/S14 documentées. Aucun nœud nouveau, fusion ou publication exécuté.


## 2026-09-17 — U288 : regroupement Promise Management adopté

Correction reçue pendant U286 : les trois responsabilités de promesse deviennent trois comportements sous Promise Management. Cible actualisée, arbitrage A2 résolu dans cette portée, ancien choix « fonctions seulement » remplacé. Définitions contextualisées, identités et migration encore préparées séparément ; catalogue actif et publication inchangés.


## 2026-09-17 — U289 : terminologie Assignment fixée et interprétation corrigée

Recherche primaire SAP, Microsoft, Oracle. Convention de travail Supply Assignment / affectation et Supply Assignment Plan / plan d’affectation ; aucune alternance avec Allocation seul. Glossaire métier précisé, TER078 ajouté comme formulation proposée, AGENTS et cible U286 corrigés. Ancienne interprétation magasin préservée dans l’historique de la cible ; C93 documente la correction. D05.d : Group Protection Decision proposé en cible, nom actif conservé. Aucun modèle publié modifié.


## 2026-09-17 — U290 : refonte du backlog appliquée

Valeur multidimensionnelle pour Supply Assignment ; Promise Management D03.n et trois comportements ; trois comportements Planning ; quatre mécanismes Supply Protection ; ATP conservé. D05.d devient Group Protection Decision, D04.o management et D05.e explicite les ajustements d’apports sous contraintes. Les opérations restent dans les descriptions. Contrats de dépendance tracés sous instruction ; options conditionnelles et questions sans solution restent ouvertes. Captures, correspondances et portées : modeles/backlog/refactoring-implementation.yaml. Aucune publication modifiée.


## 2026-09-17 — U292 : audit comparatif des comportements manquants

Revue des 39 capacités et des 14 comportements après refonte U290. Recherche primaire Microsoft, SAP, Oracle, Manhattan, Blue Yonder, Kinaxis et RELEX : 28 sources avec éditions et limites. Onze mécanismes ciblés, cinq conditionnels, sept arbitrages et dix cas fictifs ; aucune création de BHV ni modification du modèle actif. ELM191, CMP098, MKT34/MKT35. Annexe YAML autoritative et restitutions dans audits/2026-09-17-comportements-manquants. Contrôle d’empreinte du modèle et des 125 fichiers protégés ; validation métier distincte des vérifications structurelles.


## 2026-09-17 — U293 : précisions du feedback sur l’audit

Contribution enregistrée, C94 et CMP099. Audit U292 annoté : Transit Visibility proposé en complément des exceptions, Lifecycle distingué du processus et de l’orchestration, P11 à clarifier, P05 retiré comme mécanisme autonome au profit de l’adaptabilité du processus. Terme excédent dans les propositions courantes. État antérieur de l’annexe conservé dans history/audit-before-U293.yaml. Catalogue et publications inchangés.


## 2026-09-17 — U294 : vocabulaire marché pour le tracking logistique

Règle de nommage enregistrée dans AGENTS et méthode marché. SAP/Oracle/project44/FourKites comparés : Global Track seul n’est pas un nom commun établi ; Track and Trace remplace Transit Visibility dans la proposition. C95 / ELM193 / CMP100 ; périmètre et non-doublon des exceptions à instruire. Aucun changement du catalogue actif ou publication.


## 2026-09-17 — U297 : Logistics Visibility, nom adopté

Nom validé par Laurent pour le suivi physique du picking à la destination finale. Accord et empreinte enregistrés dans behavior-gap-audit.yaml ; contribution U297 et complément CMP102. Rattachement et granularité distincts de la validation du nom ; aucune mutation de D07.d ni release implicite.


## 2026-09-17 — U298 : consolidation du résultat de l’audit

Vérification : catalogue U290 inchangé. La synthèse conservait des noms et priorités dépassés malgré les feedbacks. Conclusions consolidées : Logistics Visibility adopté dans sa portée, P05 retiré, P11 à clarifier ; P04 et P10 désormais à réexaminer pour risque de reformulation du parent ou doublon. Sept candidats et cinq options conditionnelles restent à instruire. Aucun changement de catalogue, rattachement ou publication. Capture de l’annexe avant consolidation dans history/audit-before-U298.yaml.


## 2026-09-17 — U299 : deux corrections de l’audit validées

Accord enregistré avec portées et empreintes : exceptions logistiques incluses dans Logistics Visibility, sans doublon ; coordination par dépendances non constitutive à elle seule d’un comportement autonome. Les autres candidats, niveau et rattachement restent ouverts. Catalogue et publications inchangés.


## 2026-09-17 — U301–U303 : tracking numérique/physique et granularité logistique

Périmètre utilisateur enregistré avant interprétation : audit de toutes les opérations numériques et physiques. Accord U302 conservé ; U303 réouvre la maille de Logistics Visibility. Comparaison Microsoft/Camunda/SAP/Oracle et proposition sur site/transport dans l’annexe d’audit. Aucun nœud ou rattachement créé pendant cet arbitrage ; catalogue et publications préservés.


## 2026-09-17 — U305 : trois comportements de visibilité adoptés

Accord enregistré avec portées et empreintes dans l’annexe du backlog : Warehouse Visibility, Transportation Visibility, Store Execution Visibility sous Execution Tracking. Logistics Visibility demeure englobant. Nœuds du catalogue non encore intégrés ; aucun changement publié.


## 2026-09-17 — U306 : visibilité des services numériques

Correction C96 : rendre explicites l’exécution et le résultat métier des services numériques. Proposition Digital Service Visibility avec bénéfice de corrélation, distinction résultat technique/métier et comparaison Microsoft/Camunda. Trois comportements logistiques adoptés conservés ; aucun ajout de nœud ni publication pendant la discussion.


## 2026-09-18 — U308 : Store Visibility

Renommage adopté à périmètre constant dans l’annexe du backlog, synthèse et références courantes actualisées. Accord historique U305 conservé intact. Catalogue actif et publications inchangés ; intégration des comportements en nœuds encore distincte de cet arbitrage de nom.


## 2026-09-18 — U309 : document de flux Boardriders

Source SRC-2026-09-18-BRD-FLUX conservée à l’identique avec empreinte SHA-256. Dossier sous connaissance/sources : sept blocs, dix tracés, légende et date probable de 2021, interprétations séparées, réconciliation avec le panorama et associations partielles de capacités à instruire. Import régional manuel explicite ; sens détaillé de l’API, identités SAP/Elastic et actualité non établis. Consignation documentaire demandée, sans modification du panorama versionné ou du catalogue. Aucun accord métier déduit des contrôles techniques.


## 2026-09-18 — U310 : implantation et réassort

Apport Laurent consigné avant interprétation ; termes TER079/TER080 ajoutés au glossaire métier avec notes éditoriales distinctes. Comparaison SAP/RELEX CMP106 : politiques initiale/continue distinctes des méthodes de calcul Microsoft. Deux saisons actuelles conservées comme existant rapporté ; capsules comme possibilité future. Audit D05.e actualisé, sans ajout de capacités/comportements ni publication.


## 2026-09-18 — U311 : comparaisons marché dans le modèle et Atlas

Règle de production ajoutée à AGENTS et méthode marché. Contrat structuré pour nœuds et glossaire ; SAP/RELEX renseignés sur Replenishment Decision, Implantation et Réassort. Affichage Atlas et recherche adaptés au snapshot publié. Recalage explicite du socle de l’audit après contrôle : seul le champ comparatif de D05.e a été ajouté au catalogue, sans altération des autres champs. Aucune release métier implicite.


### 2026-09-18 — U316, décision d’implantation

Initial Stocking Decision (D05.g) ajoutée au backlog avec nom et définition adoptés. Replenishment Decision (D05.e) conserve le réassort continu. Domaine, Planning, glossaire, comparaisons marché et audit actualisés. Relations et compléments éditoriaux restent proposés ; aucune nouvelle décomposition en comportements. Capture et portée : audits/2026-09-18-initial-stocking/. Aucune release ni publication distante.


### 2026-09-18 — U318, comportements de redistribution

Deux comportements ajoutés sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation des stocks dispersés. Définitions françaises et parents adoptés ; noms anglais éditoriaux, détails et correspondances proposés. Assortiments de tailles et regroupement des reliquats conservés dans un même comportement sans niveau supplémentaire. Justification de décomposition, audit et comparaisons mis à jour. Aucune release. Capture : audits/2026-09-18-redistribution-behaviors/.


### 2026-09-18 — U319–U322, Les clés du modèle dans Atlas

Après étude sans modification du source (U319), Laurent retient deux profondeurs de lecture (U320) et autorise la réalisation (U321). Six repères interactifs, entrée dédiée, volet Pour contribuer et sources figées ; navigation par lien direct et conservation de la publication. U322 précise l’indépendance du modèle business et du découpage des solutions : comparaison de réalisations dédiées, mutualisées et distribuées sur des capacités stables. Comparaison primaire et limites consignées dans audits/2026-09-18-modeling-guide/business-solution.md. Guide pédagogique versionné et associé explicitement à v007, avec portée rétrospective visible ; aucun repli backlog ni modification des publications métier.


## 2026-09-18 — U342 : Reservation Policy Decision

Nom et définition intégrés ; D05 proposé comme parent. Quatre mécanismes documentés et proposés avec comparaisons marché, exemples, résultats, limites et inventaire des alternatives. Aucun ancien nœud changé ; preuve différentielle dans audits/2026-09-18-reservation-policy/implementation.yaml. Publications inchangées ; Atlas reste sur la release publiée.


## 2026-09-18 — U343 : adoption des politiques de réservation

Quatre comportements adoptés sous Reservation Policy Decision et rattachement D05 confirmé. Noms et responsabilités présentées tracés séparément des détails éditoriaux ; cinq relations contains validées. État U342 préservé dans audits/2026-09-18-reservation-policy-adoption. Aucune nouvelle publication.


## 2026-09-18 — U349 : affermissement et protection contre les réoptimisations

Ajout de BHV036 Order Firming et BHV037 Order Freezing sous Order Lifecycle Management. Accord sur le nom/définition du premier, principe et parent contextuel du second ; nom anglais du second et détails éditoriaux proposés. Justification de décomposition, exemples concrets, comparaisons marché et deux dépendances proposées vers la protection. État avant conservé et audit des comportements actualisé ; aucune publication.


## 2026-09-18 — U350 : nom Order Freezing adopté

Nom de BHV037 validé champ par champ. Principe et rattachement U349 conservés ; descriptions et contrats gardent leur statut éditorial.


## 2026-09-18 — U363 : refonte D04 appliquée

Quatre capacités, cinq variantes d’Order Type, neuf comportements Lifecycle. Structuring et Archiving séparés. Spread retiré du sens mutation et explicité sous Supply Assignment ; glossaire enrichi. Identifiants, liens métier et valeurs adoptées préservés, nouvelles descriptions et contrats qualifiés. Captures et migration dans audits/2026-09-18-d04-U363 ; aucune publication.


## 2026-09-18 — U364 : comportements Supply Assignment

Intégration BHV045–BHV047 : application de plan, complément préservant les affectations et réaffectation des liens modifiables. Distinction adoptée, compléments éditoriaux qualifiés ; décisions, réservations et Freezing séparés. Comparaisons SAP/Microsoft conservées dans les fiches (CMP134). Audit courant actualisé ; preuves antérieures capturées, aucune publication.


## 2026-09-18 — U365 : cadre de l’ATP et vocabulaire Fulfillment

Contribution enregistrée ; proposition Fulfillment Strategy Decision documentée dans l’annexe dédiée, avec comparaisons SAP/Microsoft ELM224/CMP135 et limites de portée ATP/PTP/CTP. Réexamen de Supply Assignment Decision, sans création ou renommage de catalogue ni publication.


## 2026-09-18 — U366/U367 : audit Supply / Fulfillment et glossaire

Audit local du catalogue, des relations, des deux glossaires, des conventions utiles et des noms d’icônes Atlas. Clarification métier Supply / Supply Chain / Fulfillment ; sens fonctionnel local Supply conservé. Renommage de D03 proposé, aucune substitution globale. Inventaire et recommandations dans audits/2026-09-18-supply-fulfillment et annexe structurée ; catalogue et publications inchangés.


## 2026-09-18 — U368 : Supply Network recommandé

Réexamen documenté de SF-A06 : Supply Network convient mieux au référentiel de lieux et relations partagé par les finalités FLOW. Appuis SAP F&R/Microsoft, différences et limites conservés ELM226/CMP137. Ancienne recommandation capturée ; rapport et annexe actualisés. Noms du catalogue et du glossaire inchangés en attente d’arbitrage.


## 2026-09-18 — U369 : noms D03/D13 acquis, univers SCM proposé

Accords de nommage Fulfillment Optimization et Supply Network enregistrés avec portée et empreintes. Supply Chain Management examiné pour l’univers : appui CSCMP/Microsoft, limites du périmètre FLOW explicites. Question d’univers encore ouverte ; application des noms acquis au catalogue à réaliser séparément de la publication.


## 2026-09-18 — U389 : définition concrète du comportement

Analyse exhaustive des 48 comportements intégrés sous 13 capacités et distinction des scopes de visibilité encore en annexe. MOD006 enrichi de sept formes illustrées ; règle mémorisée dans AGENTS.md, preuve dans modeles/backlog/behavior-typology.yaml. Appui BIZBOK/Microsoft ELM234/CMP145, sans revendication de taxonomie universelle. Catalogue métier et publications inchangés ; liste éditoriale distinguée de l’instruction acquise.


## 2026-09-18 — U390 : proposition des comportements Purchase Order

Après les retours, trois variantes proposées avec comparaison Microsoft/SAP ELM235/CMP146 : stock, livraison directe et prestations. Consignation conservée comme candidat à frontière ouverte. Définition actuelle centrée sur les biens à élargir explicitement si accord. Catalogue et publications inchangés.


## 2026-09-18 — U391 : Purchase Order adopté et consignation recadrée

Trois comportements Purchase Order intégrés BHV058–060, preuves et accords préservés. C102 retire la consignation des candidats achat ; analyse Microsoft/SAP/Oracle ELM236/CMP147 et proposition Consigned Inventory Management sous D01, avec frontières stock/accord/finance/assurance/décision/exécution. Aucune création de cette capacité ni publication implicite.


## 2026-09-18 — U392 : apport fournisseur sans achat

Comparaison Microsoft/SAP/Oracle ELM237/CMP148 : demande d’apport distincte du régime de stock et de l’acquisition. Consignment Replenishment Order proposé comme type ciblé D04 ; Procurement Order générique et Supply Order comparés avec leurs limites. Aucun nouveau nœud ou renommage de Purchase Order.


## 2026-09-18 — U393 : architecture des demandes par intention

Principe mémorisé dans AGENTS.md et order-intent-principles.yaml ; annexes de consignation/apport reliées à cette direction. Offre de stockage/location et réassort tiré par les ventes enregistrés comme intention exprimée, distincte de l’existant et de la définition générale de consignation. Comparaison Microsoft/SAP ELM238/CMP149, avec limites sur les motivations historiques et le jugement de modernité. Catalogue métier inchangé.


## 2026-09-18 — U394 : visibilité métier du design

C103 corrige le déplacement du débat vers la couverture fonctionnelle SAP. Principe et annexes précisent la lisibilité des intentions/processus dans les concepts et liens ; AGENTS.md actualisé. ELM238 reconsulté et CMP149 précisé. Opinion historique distinguée du constat de représentation ; catalogue métier inchangé.


## 2026-09-18 — U395 : deux capacités de consignation adoptées

Consigned Inventory Management D01.h et Consignment Replenishment Order D04.r intégrées au backlog, avec noms, définitions présentées et parents validés. Comparaisons Microsoft/SAP/Oracle dans les fiches ; frontières, exemple des 500 pièces et sens large de Replenishment documentés. Quatre dépendances détaillées restent éditoriales. Aucun comportement ajouté. Annexes, instructions et audit courant alignés ; preuve et capture dans audits/2026-09-18-consignment-U395. Aucune release.


## 2026-09-18 — U396 : non-décomposition de Consignment Replenishment Order

Décision et justification enregistrées dans nonpurchase-supply-order-review.yaml ; assessment D04.r de l’audit actualisé. Comparaison Microsoft/Oracle conservée avec sa limite de preuve. Aucun nœud, relation ou champ du catalogue modifié ; aucun comportement ajouté. Étude des mécanismes de Consigned Inventory Management encore ouverte.


## 2026-09-18 — U397 : comportements métier de l’Order

C104 remplace la conclusion de non-décomposition U396. Règle de lisibilité métier consignée dans AGENTS.md, principes des demandes et annexe D04.r. Initial Stocking et Continuous Replenishment proposés avec descriptions, bénéfices, exemples, frontières et comparaison Microsoft/Oracle ; leurs noms et définitions ne sont pas encore adoptés. Audit courant corrigé. Catalogue, parents et publications inchangés.


## 2026-09-18 — U398 : comportements de consignation et liens métier

BHV061 Initial Stocking et BHV062 Continuous Replenishment intégrés sous D04.r ; noms, définitions présentées et parents validés. Justification de lisibilité conservée. U399 : les règles de comportement différencié selon l’interaction et de liens lisibles sont mémorisées dans AGENTS.md, MOD006 et business-interactions.yaml pour le prochain audit ou les prochaines améliorations. Aucun nouvel audit, remaniement des liens ou chantier Atlas. Captures techniques dans modeles/backlog/history/consignment-behaviors-U398 ; poursuite de l’audit existant. Backlog uniquement.


## 2026-09-18 — U400 : proposition groupée consignation, vente et transfert

Trois capacités traitées ensemble dans la continuation de l’audit existant. Douze comportements proposés dans consignment-sales-transfer-review.yaml avec définitions, exemples, bénéfices, frontières et sources ELM240/CMP151. Catalogue métier et liens inchangés ; aucun nouvel audit. Validation du lot à recueillir sur la proposition présentée, sans confondre regroupement autorisé et adoption préalable.


## 2026-09-18 — U401 : lot consignation, vente et transfert intégré

Douze comportements validés ajoutés au backlog (BHV063–074) avec définitions présentées, parents, exemples, bénéfices et comparaison marché. Justifications de décomposition sur les trois capacités ; audit existant et annexes mis à jour. Aucun lien métier existant ni champ antérieurement validé modifié. Preuves techniques dans modeles/backlog/history/grouped-orders-U401 ; aucune nouvelle étude d’audit, release ou modification Atlas.


## 2026-09-18 — U402 : mécanismes CTP intégrés

Additional Supply Feasibility, Fulfillment Alternative Feasibility et Commitment Rebalancing Feasibility ajoutés sous CTP (BHV075–077), avec descriptions, exemples, justification et comparaisons Microsoft/SAP. Sources primaires reconsultées avant la proposition, tracées ELM241/CMP152. P14–P16 marqués intégrés dans l’audit existant ; frontière de catalogue A05 clarifiée, règles détaillées distinctes. Aucun changement des champs précédemment validés ni des relations métier existantes. Captures et empreintes dans modeles/backlog/history/ctp-behaviors-U402 ; aucune release.


## 2026-09-19 — U403 : Supplier Confirmation

Comportement BHV078 intégré sous Purchase Order avec nom et définition adoptés, exemple 100 vendredi / 60 vendredi + 40 mardi, responsabilités et explication détaillée. Demande, réponse, accord retenu, risque et promesse client distincts ; effets d’un refus ou d’une acceptation expliqués. Sources primaires relues avant la proposition : ELM242/CMP153, limites SAP indexé et impacts Microsoft directs consignées. Audit existant A06 mis à jour ; aucun ancien champ validé ni lien métier modifié, aucune release. Preuves dans modeles/backlog/history/supplier-confirmation-U403.


## 2026-09-19 — U404–U406 : visibilité physique et Business Process Tracking

Préférence de nom, précision Task/appels et accord enregistrés. BHV079–082 intégrés sous Execution Tracking : trois visibilités physiques selon U305/U308, Business Process Tracking selon U406. Description des résultats, attentes, tentatives, réussite technique et fin de Task/processus ; pas de nouveau niveau ni objet de catalogue. Sources Microsoft/Camunda et relecture ciblée SAP/project44/Blue Yonder consignées ELM243/CMP154. Audit existant et AGENTS actualisés ; anciens champs validés, relations métier et preuves historiques conservés. Aucune release.


## 2026-09-19 — U407–U409 : le Process orchestre des Services

Convention et neuf noms présentés adoptés ; deux intitulés dérivés proposés. Références narratives et comparaisons des fiches actualisées, noms natifs éditeurs préservés. Historique des accords capturé, audit existant suivi sans nouvelle étude. Pas de changement de graphe ni de publication.


## 2026-09-19 — U410 : lancement collectif dans Order Release

BHV039 enrichi avec une définition adoptée et des explications individuelles/collectives. P11 clôturé par intégration au comportement existant ; neuf comportements Lifecycle conservés. Comparaison SAP/Oracle consignée ELM245/CMP156. Audit existant et AGENTS actualisés, historique et relations préservés. Aucune release.


## 2026-09-19 — U411–U413 : Order Backlog Management

D03 renommé, mandat collectif explicité avec exemple 100 demandées / 60 prises en charge / 40 restantes. Comparaison Oracle/Microsoft ELM246/CMP157. Réexamen ciblé Lifecycle/Structuring consigné dans l’annexe de l’audit existant ; rattachements inchangés, choix de capacité parente à arbitrer. Anciennes validations et publications préservées ; aucune release.


## 2026-09-19 — U414 : Order Backlog Planning et Order Release

D03.p créé avec nom/définition présentés ; parent D03 adopté. BHV039 déplacé depuis D04.o en conservant son identifiant et sa définition. Lifecycle garde huit comportements ; Split et Structuring inchangés. Justification de décomposition, comparaisons Oracle/Microsoft ELM247/CMP158, audit existant et AGENTS actualisés. Aucune release.


## 2026-09-19 — U416/U417 : structuration et cycle de vie du carnet

D04.n et D04.o déplacés dans D03 ; définition Structuring élargie et adoptée ; BHV044 sous Structuring, BHV039 sous Lifecycle. Planning recentré sur préparation, sans comportement direct. Identifiants et définitions des comportements conservés. Comparaisons CMP159/ELM248, audit existant, descriptions et AGENTS actualisés. Les preuves U414 restent capturées ; aucune release.


## 2026-09-19 — U420 : domaines d’Archiving et Lifecycle

Order Archiving déplacé dans D03 ; Order Lifecycle Management dans D04. Comportements inchangés de parent, donc Release suit Lifecycle en D04. Structuring et Split restent en D03. Descriptions, comparaisons contextuelles, audit existant et instructions actualisés ; historique U417/U418 préservé. Aucun nouveau catalogue ni release.


## 2026-09-19 — U424 : Lifecycle par dimensions et états

Six comportements sous D04.o ; états, portées, contraintes et exemples décrits dans les fiches. Rescheduling intégré à préparation/révision ; Cancellation et Closure réunis dans fin de demande en conservant leurs effets distincts. Définition Lifecycle présentée adoptée ; listes détaillées éditoriales. D03 mobilise Lifecycle ; historique et identifiants retirés conservés. Audit existant actualisé ; aucune release.


## 2026-09-19 — U425 : clôture des candidats de réassort

P01–P03 clos comme couverts par D05.e ; politiques besoins datés/seuil-cible et ajustements explicités. Aucun nouveau comportement ni changement de structure. Audit existant, comparaisons Microsoft et instructions actualisés ; preuves antérieures conservées. Aucune release.


## 2026-09-19 — U426 : réouverture des comportements de réassort

La question de Laurent réouvre P01–P03 avant finalisation du suivi U425. Proposition corrigée : deux politiques d’apports et un mécanisme d’ajustement combinable, avec bénéfices explicites. Les descriptions U425 sont conservées ; aucun comportement créé sans accord sur la proposition. Audit et instructions portent le réexamen courant.


## 2026-09-19 — U427 : réassort décomposé et point d’audit traité

BHV083–085 intégrés sous Replenishment Decision : deux politiques et un mécanisme d’ajustement combinable. P01–P03 marqués intégrés. Justification, exemples, comparaisons Microsoft et instructions actualisés. 139 nœuds, 47 capacités, 74 comportements ; parents et anciennes validations préservés. Aucun autre arbitrage ni release implicite.


## 2026-09-19 — U431 : clôture de l’audit des comportements

Trois candidats clos comme couverts par l’existant, frontière externe consolidée et règles/contrats différés identifiés. Aucun changement du catalogue : 47 capacités et 74 comportements. Accords et versions historiques préservés ; aucune release.

## 2026-09-19 — U432 : contrôle de préparation de release

Défaut des liens vers illustrations corrigé dans compilation/validation et exposé dans le rapport ; 12 tests réussis. Catalogue et publications inchangés. Le rapport brut révèle les transcriptions d’accords encore nécessaires (469 champs sans décision de publication correspondante), à traiter pendant la préparation avec revue des 8 impacts de glossaire. Aucune publication demandée ni effectuée.

## 2026-09-19 — Audit technique des performances

Mesures et recommandations dans audits/2026-09-19-performance/rapport.md. Causes confirmées : double analyse YAML, relecture complète de l’historique, lectures répétées et rapports volumineux, contrôles trop systématiques ; coûts distincts des fixtures de tests et du backend Atlas. Expériences isolées, sans modification du code de production ou des instructions. Aucune reprise de l’audit métier ni release. La validation du modèle a été exécutée une fois comme mesure ; pas de relance systématique après rédaction du rapport.


## 2026-09-19 — Optimisations techniques appliquées

Lecture YAML en une passe et cache borné par contenu, rapports compacts, restitution ciblée, checkpoint historique vérifié, instructions compactées et fixtures réduites. Notifications Atlas évitées en l’absence de changement. Mesures et garanties : audits/2026-09-19-performance/optimisations.md. Tests ciblés et build réussis ; modèle et 125 preuves/publications protégées inchangés. Les 469 erreurs de préparation de release antérieures restent détectées. Aucun nouveau choix métier ni publication.


## 2026-09-19 — U433 : release 2026-09-19.1 publiée dans Atlas

Révision 8 activée : 135 nœuds, 47 capacités, 74 comportements, 323 relations, 110 termes. 207 décisions transcrivent 469 champs déjà adoptés ; 36 décisions conservées automatiquement et 60 reprises anciennes suspendues restent traçables. Huit impacts de glossaire examinés ; Purchase Order inclut les prestations conformément à U391, avec statut lexical proposé conservé. Catalogue métier inchangé, zéro erreur de validation. L’index technique a été activé ; ses octets précédents sont conservés et vérifiés, ainsi que les 124 autres fichiers protégés inchangés. Serveur local démarré, API courante et ancienne publication contrôlées. Revue et preuves : audits/2026-09-19-release-U433/. Aucun commit ni push.

## 2026-09-19 — U434/U435/U436 : audit profond et préparation V0

Audit des 47 capacités, 74 comportements et relations ; comparaison de huit éditeurs et des cadres transverses, avec limites de preuve explicites. Corrections plausibles autorisées U435 : 36 fiches actualisées, 12 liens proposés ajoutés, 17 relations existantes libellées, 16 comparaisons en fiche ajoutées et cinq positions marché périmées corrigées. U436 réserve à Reservation le blocage des usages concurrents, sans cet effet pour l’affectation seule. Les 570 valeurs validées antérieurement sont préservées ; aucune nouvelle capacité ni comportement. Contrat des libellés et restitution Atlas corrigés, 79 tests uniques réussis, validation zéro erreur, build réussi et backlog régénéré. Les publications restent inchangées ; question du devenir des invendus consignés en attente et autres contrats complexes explicitement ouverts. Rapport final et preuves : audits/2026-09-19-audit-profond-v0/modifications.md. Aucun commit ni push.

## 2026-09-19 — U437 : réexamen de la structuration D03

Diagnostic ciblé des onze capacités de D03 et de leurs recouvrements de résultat, avec consultation des sources SAP, Microsoft et Oracle. Proposition de deux domaines Order Promising et Fulfillment Optimization, alternative à domaine unique et deux déplacements vers D04, soumis à Laurent comme choix complexes U435. Le catalogue garde ses noms et parents. Corrections éditoriales appliquées à D03 (autorisation portée par Lifecycle U420) et Supply Assignment (matérialisation des choix, décision collective D03.o U378) ; trois comparaisons proposées ajoutées à D03. Les 570 valeurs validées et leurs empreintes restent identiques. Contribution U437 indexée. Rapport : audits/2026-09-19-d03-U437/revue.md ; autorité des propositions : modeles/backlog/d03-domain-review-U437.yaml. Aucun changement de publication, commit ou push.

## 2026-09-19 — U438 à U446 : deux domaines frères et responsabilités clarifiées

U438 appliqué : D03 Fulfillment Optimization (quatre capacités), nouveau D15 Order Promising (cinq), Structuring et Archiving dans D04. U445 adopte Fulfillment Commitment sur D03.n ; identités et comportements antérieurs conservés. U439/U440/U442 : définition Structuring simplifiée, Grouping BHV086 et Merging BHV087 intégrés comme propositions étayées ; conditions détaillées ouvertes. U441/U443 distinguent engagement de satisfaction et affectation ; U436 reste inchangé. U446 : contrôle explicite, aucun domaine imbriqué, six domaines présentés directement sous Supply. Validation zéro erreur, quinze tests ciblés réussis ; 175 fichiers protégés inchangés. Rapport et preuves : audits/2026-09-19-d03-U437/modifications.md. Aucune release, commit ou push.

## 2026-09-19 — U447 : ordre de lecture des référentiels aux optimisations

Business References en premier, puis Order Management, Inventory Management, Process Management, Order Promising, Fulfillment Optimization et Inventory Optimization. Référentiels présentés dans l’ordre Product, Party / Role, Catalog, Agreement, Fulfillment Network, Service Catalog, avec Party / Role, Catalog et Agreement contigus. Permutation des relations presents et des nœuds domain/reference, sans modification du contenu des éléments, identifiants, parents ou accords. Restitution backlog alignée ; aucun changement frontend ni publication. Convention : modeles/backlog/reading-order-U447.yaml.

## 2026-09-19 — U448 : release 2026-09-19.2 publiée dans Atlas

Urbanisation v009 activée : 138 nœuds, six domaines frères, 47 capacités, 76 comportements, 338 relations et 110 termes. La publication intègre l’audit V0, la séparation Order Promising / Fulfillment Optimization, Fulfillment Commitment et l’ordre de lecture U447 ; Grouping, Merging et les nouvelles clarifications conservent leurs qualifications proposées. 72 décisions transcrivent 141 champs sur preuves historiques ou accords explicites U438/U445 ; 173 décisions compatibles sont reprises, sans étendre les validations. Impact de glossaire D03.o / TER078 examiné et compatible avec la portée U378.

44 tests ciblés réussis, zéro erreur de validation, vues régénérées et frontend disponible. Le modèle et le glossaire servis par Atlas correspondent exactement au snapshot publié ; la version 2026-09-19.1 reste accessible et inchangée. 185 fichiers antérieurs de publication et de preuve vérifiés identiques ; ancien index capturé avant activation. Revue et vérification : [audits/2026-09-19-release-U448/revue.md](audits/2026-09-19-release-U448/revue.md). Aucun commit ni push.

## 2026-09-19 — U449 : types, icônes et décisions en fin de domaine

Les 47 capacités du backlog portent une nature : 17 action, 16 decision, sept management, quatre knowledge, deux planning et une orchestration. Les 37 valeurs existantes sont conservées ; dix compléments proposés et justifiés, sans modifier les champs adoptés. Convention MOD007 et grille dédiée ; appui méthodologique OMG DMN MKT43/ELM259/CMP169, sans taxonomie de marché revendiquée.

Icônes Atlas associées au champ publié, type lisible, décisions placées après les autres capacités par partition stable. Séparation légère dans l’arbre, les cartes et les fiches ; aucun trait dans une liste homogène. Rangement du backlog aligné, comportements et relations métier conservés. Contrat de typage activé par un principe explicite, sans imposer de nouveau contenu aux publications historiques.

28 tests Python, 58 tests frontend, validation sans erreur, compilation et contrôles visuels/clavier/mobile réussis. 230 fichiers protégés inchangés. Interface disponible après rechargement ; v009 reste active, les dix types complétés attendent une prochaine release. [Rapport](audits/2026-09-19-capability-types-U449/rapport.md). Aucun commit ni push.

## 2026-09-19 — U450/U451 : présentation Atlas et formes de comportements

Réserves, validations et sources internes retirées de la présentation. Deux glossaires, métier et méta modèle, avec défilement indépendant de la liste et de la définition. Bouton **Comprendre le méta modèle** et six repères rétablis par l’association explicite de l’édition méthodologique 2026-09-19.1 à v009. Ancienne édition conservée. Le workflow de publication capture et reporte l’association contrôlée pour éviter une nouvelle disparition du guide.

Icônes spécifiques pour les capacités des référentiels ; sept formes et pictogrammes pour les comportements. Les 76 classements sont proposés dans le backlog, sur la grille retenue en U451. Ils attendent, avec les dix types U449, le choix de publication demandé à Laurent. La revue du candidat ne modifie aucun nom, définition ou rattachement ; 73 transcriptions contrôlées préservent 118 champs déjà approuvés sans adopter les types ajoutés.

63 tests frontend réussis, contrôles Python ciblés et compilation réussis, validation modèle sans erreur, parcours navigateur desktop/mobile contrôlés. 231 fichiers historiques et preuves préservés. Serveur redémarré et identifié ; v009 sert toujours son snapshot exact. [Rapport détaillé](audits/2026-09-19-atlas-U450/rapport.md). Aucun commit ni push.

## 2026-09-19 — U452 : publication des types dans Urbanisation v010

Release `2026-09-19.3` publiée et activée à 07:41:05 UTC : 47 capacités et 76 comportements typés. Elle intègre les dix compléments U449 et les 76 formes U451, sans changement des noms, définitions, rattachements ou termes du glossaire. 172 décisions compatibles reprises et 73 transcriptions contrôlées de 118 champs identiques ; les nouveaux types restent proposés. L’association explicite à l’édition méthodologique 2026-09-19.1 est reportée : les six repères et les deux glossaires restent disponibles.

Validation finale sans erreur, restitutions régénérées, API identique au candidat figé, navigateur vérifié sur les données réellement publiées. 242 fichiers antérieurs protégés et inchangés ; v009 reste consultable en version fixe. Serveur local existant conservé, aucun redémarrage nécessaire. [Rapport de release](audits/2026-09-19-release-U452/rapport.md). Aucun commit ni push Git.


## 2026-09-19 — U458 : lancement du plan Atlas, premier jalon

Lots 1 et 2 mis en œuvre : suppression de layer dans les 142 nœuds du backlog, compatibilité des publications historiques, filtres explicites de contenu métier, recherche nom/identifiant et glossaire, fiches à détails progressifs, relations directes par défaut et contrastes renforcés. Le simulateur de réalisations logicielles est retiré du guide. Noms, parents, cycles de validation et extrémités des relations conservés.

Guide 2026-09-19.2 préparé en brouillon non associé à une publication ; terme TER086 Purchase Order Document proposé pour retrouver « bon de commande ». Cinq pilotes proposés dans information-pilots-U458.yaml ; suivi consolidé dans v0-readiness.yaml. La convention fait/document est soumise à Laurent, sans réponse présumée. Aucun maître, flux installé, droit de décision ou réservation automatique inventé.

68 tests frontend, 33 tests Python ciblés, validation modèle sans erreur, compilation et parcours navigateur réussis. 291 fichiers de publication et de preuve vérifiés identiques. Interface locale disponible après rechargement ; v010 demeure la référence publiée. Modèle migré, terme lexical et nouveau guide attendent une publication distincte. Aucun commit ni push. [Bilan et preuves](audits/2026-09-19-plan-U458/rapport.md), [cinq pilotes](audits/2026-09-19-plan-U458/pilotes.md).


## 2026-09-19 — U459 : overview des capacités et repères marché

Infobulles des liens de capacités dans la carte : définition puis liste à puces des comportements issus des relations explicites, au survol et au focus. Rubrique « En quelques mots » retirée des deux glossaires ; anciens liens conservés par redirection vers la définition.

Repères marché rétablis dans les fiches : rapprochement documenté, choix FLOW, différences, sources primaires et portée. Présentation dépliable et recherche sur les champs publics ; statuts et sources backlog restent internes. C107 corrige l’interprétation trop restrictive C106/U458, répercutée dans AGENTS.md, les conventions et le principe courant. Aucune comparaison réécrite ou qualification standard/innovant inventée ; couverture manquante explicite.

69 tests frontend réussis, compilation et parcours navigateur desktop/clavier/mobile contrôlés ; validation zéro erreur et restitution backlog générée. 303 fichiers historiques protégés inchangés ; nœuds, relations et publication v010 inchangés. Interface disponible après rechargement, sans release ni commit/push. [Rapport](audits/2026-09-19-atlas-U459/rapport.md).

## 2026-09-19 — U460/U461 : cinq pilotes approfondis, fait–document confirmé

U461 confirme l’association de tout fait de gestion à un document métier identifié, éventuellement structuré sans PDF. Principe ajouté au backlog et contrôle conditionné à sa présence ; publications historiques conservées. V0-P01 résolu au niveau du principe, sans adoption des versions, corrections ou nombre exact de documents.

Cinq fiches enrichies des responsabilités sur les informations et de quinze cas : sept frontières expliquées, huit suites métier ouvertes. Product Reference distingue autorité, émetteur, validité et fraîcheur ; Purchase Order illustre le document qui consigne une réception partielle. Quatre rapprochements Microsoft/GS1 ajoutés aux fiches, six contextes de glossaire explicités, nom Fulfillment Commitment corrigé dans une comparaison. Guide futur actualisé, suivi V0 consolidé ; aucune nouvelle entité canonique.

Validation zéro erreur, 18 tests Python réussis (quatre relancés hors sandbox après un problème de droits temporaires Windows), guide et références contrôlés, restitution backlog générée. 142 nœuds, 346 relations et accords antérieurs préservés ; 303 fichiers historiques identiques. Relecture PO/expert encore à faire ; aucun lancement de release, commit, push ou serveur. [Rapport](audits/2026-09-19-pilotes-U460/rapport.md), [support des cinq pilotes](audits/2026-09-19-pilotes-U460/pilotes.md).

## 2026-09-19 — U462 : marché, raisons des choix et exemples accessibles

Onglet Marché & choix ajouté à Atlas, avec position FLOW et source primaire datée directement visibles ; vocabulaire et définition expliqués en tête lorsqu’ils sont documentés. Rubrique Exemples concrets placée après la définition, reprenant les passages explicites du snapshot et les exemples structurés. Anciens liens marché, navigation clavier, recherche et séparation publication/backlog préservés.

Backlog : dix choix de terme/définition explicités, quatorze exemples structurés sur neuf fiches et trois rapprochements ajoutés (ELM286–288/CMP179–181). Écart SAP ARun/FLOW sur le blocage concurrent rendu explicite. Les 47 capacités disposent maintenant d’un exemple ; sept restent sans comparaison propre. Les autres lacunes sont listées sans réouverture globale de l’audit des comportements.

77 tests frontend, 15 tests Python, validation zéro erreur, compilation et recette navigateur réussies. Définitions, 142 nœuds, 346 relations et accords préservés ; 303 fichiers historiques identiques. Interface disponible après rechargement ; contenus nouveaux dans le backlog, v010 reste publiée. Aucun commit, push, release ou changement serveur. [Rapport et couverture](audits/2026-09-19-contenu-U462/rapport.md).

## 2026-09-19 — U463 : définition métier de l’univers Supply

Supply Chain Orchestration se définit désormais par commandes, stocks, engagements, optimisation et pilotage de la réalisation. La qualification transactionnelle et la priorité d’exploration sont retirées de sa définition ; TER034/TER035 abandonnent la hiérarchie OMS/Supply. Deux rapprochements sourcés TOGAF/Microsoft et l’exemple U455 sont ajoutés à la fiche, sans changement de périmètre ni nouvelle validation implicite.

U463/C108/CMP182 tracés, instructions et suivi alignés. Validation zéro erreur, 11 tests ciblés réussis, restitution backlog générée. Un nœud et deux termes modifiés ; 142 nœuds, 346 relations, noms et accords conservés. 303 fichiers historiques identiques. Atlas v010 inchangée ; nouvelle release nécessaire pour afficher ces contenus. [Rapport](audits/2026-09-19-definition-supply-U463/rapport.md).

## 2026-09-19 — U464 : Information, recherche et définition proposée

Recherche primaire ISO, SBVR, ORM, TOGAF et Guild. Information Concept et fait élémentaire distingués ; aucune définition normative unique assimilée au groupe minimal demandé. MOD012 Information proposé dans le méta modèle, avec sens, contexte, minimum utile aux capacités et frontière explicite avec les modèles implémentables. La granularité reste à éprouver sur les cinq pilotes ; la convention fait de gestion–document demeure distincte des faits de la logique.

Brouillon du guide et suivi actualisés, U464/MKT51–53/ELM289–291/CMP183 tracés. Modèle métier, glossaire métier, schéma et publications inchangés. Validation zéro erreur, 17 tests du guide réussis et 1 ignoré pour les liens symboliques Windows ; contrôle direct du brouillon, des références et des 306 empreintes protégées réussi. Aucune publication ni changement UI. [Recherche et recommandation](audits/2026-09-19-information-U464/recherche.md).

## 2026-09-19 — U465/U466 : informations métier éprouvées sur les cinq pilotes

Quatorze fiches d’information proposées dans une annexe YAML : cinq pour l’achat, cinq pour la référence produit, deux pour la promesse, une pour l’affectation et une pour la réservation. Questions métier, sens, contexte minimal, frontières, 21 contributions de capacités et 15 liens qualifiés explicités. Quinze cas antérieurs repris et quatre exemples ajoutés ; les règles encore ouvertes restent visibles et la revue humaine reste à faire.

U466 adopte deux informations reliées, proposition et engagement de satisfaction, pouvant coexister pendant un réexamen. Portée limitée à cette distinction ; autres découpages et rédactions proposés. Exemple ajouté à MOD012 et au brouillon du guide. Huit groupes de comparaison et CMP184 documentent les apports Microsoft, Oracle, GS1 et architecture, leurs écarts et les raisons des termes retenus. Candidats et revue U460 préservés, suivi V0 actualisé.

Validation zéro erreur, 17 tests du guide réussis et un ignoré pour les liens symboliques Windows ; sources, rôles, liens et couverture contrôlés. 306 fichiers protégés identiques, dont modèle métier, glossaire métier, schéma et historique. Aucun nouveau nœud canonique, changement UI ou publication. Prochaine étape : contrat minimal et lecture des informations dans Atlas. [Rapport des cinq pilotes](audits/2026-09-19-informations-pilotes-U465/rapport.md).


## 2026-09-19 — U467 : publication Urbanisation v011 pour essai

Release `2026-09-19.4` publiée et activée avec le guide `2026-09-19.2` : retrait des couches, définition Supply corrigée, exemples et marché enrichis, Information et exemple proposition/engagement dans le méta modèle. 138 nœuds, 47 capacités, 76 comportements, 338 relations et 111 termes TER. Les quatorze fiches d’information U465 restent figées comme contexte, sans écran dédié.

123 décisions reprises et 122 transcriptions contrôlées de 208 valeurs approuvées inchangées. Deux blocages de provenance corrigés sans altérer l’historique : portée des sources embarquées du guide et rattachement de notes générales aux nouvelles entrées marché. Validation zéro erreur, 24 tests de préparation/publication réussis (quatre repris hors sandbox Windows), six parcours navigateur réussis et API conforme au snapshot ; 301 fichiers historiques identiques. Serveur existant inchangé, aucun commit/push. [Rapport](audits/2026-09-19-release-U467/rapport.md).

## 2026-09-19 — U468 : contrat et consultation des informations métier

Lot 4 implémenté : 14 informations, 21 usages de capacités et 15 liens qualifiés intégrés dans `model.yaml#information_catalog`, sans nouveau niveau de hiérarchie. Fiches avec exemples et onglet Marché & choix, navigation depuis les capacités, recherche générale et locale, défilement indépendant et repli mobile. Les qualifications internes restent masquées ; les sources marché sont visibles. L’annexe U465 reste une preuve historique, sans second catalogue courant.

Publication préparée depuis le même snapshot que le modèle, contrôle d’identité et de références, révisions automatiques et absence explicite dans les anciennes versions. Validation zéro erreur, 29 tests Python et 82 tests frontend réussis, build réussi, dix parcours navigateur isolés réussis. Rapport de préparation : aucun nœud ou lien de capacité modifié, 245 décisions conservées, aucune nouvelle ou suspendue. Les 368 fichiers historiques contrôlés sont inchangés. V011 reste courante ; aucune release, aucun commit/push ni administration serveur. Autorités et règles détaillées ouvertes préservées. [Rapport et captures](audits/2026-09-19-informations-atlas-U468/rapport.md).

## 2026-09-19 — U469 : publication v012 pour revue de la base

Priorité donnée à la consolidation de la base et aux retours pas à pas de Laurent ; extension et généralisation data/information mises en attente. État courant publié sans enrichissement dans v012 / `2026-09-19.5` : 138 nœuds, 47 capacités, 76 comportements et 338 relations inchangés ; 14 informations et 15 liens U468 existants désormais consultables. Guide `2026-09-19.2` repris par association explicite, glossaires inchangés. Les 245 décisions antérieures sont conservées, sans nouvel accord ni suspension.

Validation zéro erreur, six parcours navigateur réels réussis, API identique au snapshot, 366 fichiers historiques protégés inchangés et anciennes associations conservées. Frontend U468 déjà construit et testé ; aucun changement de code dans cette release. Atlas disponible sur le port 8765, PID 24916 conservé sans redémarrage. Aucun commit ou push. [Rapport](audits/2026-09-19-release-U469/rapport.md).


## 19 septembre 2026 — consolidation de la base U470/U471

Univers Supply réécrit pour une lecture concrète : chaîne d’approvisionnement expliquée, projections des maîtres externes et ingestion, deux exemples, liens glossaire. Trois comparaisons du nom et du périmètre (CSCMP, Microsoft, Oracle). Reprise des 47 fiches à source unique : seconde référence primaire argumentée, 34 avec un autre organisme ou éditeur ; noms et définitions de ces fiches conservés. Règles éditoriales et contrôle de pluralité consignés.

Catalogue Informations métier masqué dans Atlas sans suppression ; infobulles sur définition complète, répétitions identiques des positions marché retirées. 82 tests frontend, 30 tests Python, validation sans erreur, build et recette isolée réussis ; 432 fichiers historiques intacts. Le serveur sert le build actualisé et v012 reste la publication courante. Les contenus corrigés attendent une release distincte ; les accords des révisions enrichies restent à réexaminer, sans transcription automatique. [Rapport](audits/2026-09-19-base-U470/rapport.md).

## 19 septembre 2026 — U472 : retrait de Business Services

Univers vide `universe-case` et terme TER067 retirés du backlog ; aucune capacité ni relation à déplacer. Terme Case, deux principes et frontière de Process Tracking corrigés ; priorité Supply Chain puis commerce consignée, sans univers Commerce créé. U173 et les états antérieurs sont conservés, identifiants non réutilisables. Deux sources de contexte examinées et qualifiées dans CMP187, sans taxonomie de marché imposée.

141 nœuds, 47 capacités, 76 comportements, 346 relations et 110 termes. Validation sans erreur, 12 tests réussis, contrôle du retrait ciblé et 519 fichiers historiques identiques. Restitution backlog régénérée ; v012 reste la publication Atlas, sans release implicite. [Rapport](audits/2026-09-19-business-services-U472/rapport.md).

## 19 septembre 2026 — Atlas : barre haute compacte et signature secondaire

Barre FLOW de 52 px avec fil d’Ariane et actions sur grand écran ; suppression de leur rangée au-dessus du titre. Logo Beaumanoir réduit à 76 px et placé près des statistiques dans le pied de l’arbre. Navigation mobile adaptée ; bandeau descriptif et onglets toujours fixes. Repères Carbon et Fluent documentés, médias d’origine préservés.

Gain mesuré de 78 px de hauteur de contenu sur la vue univers desktop ; 10 à 14 px sur les deux petites tailles contrôlées. 82 tests frontend, 30 contrôles de défilement et recette de la barre sur cinq tailles réussis ; build actualisé. Aucune publication métier. [Rapport et captures](audits/2026-09-19-atlas-shell/rapport.md).

## 19 septembre 2026 — U473 : publication v013 des retours de revue

Release `2026-09-19.6` publiée et activée : univers Supply concret, projections externes et ingestion explicites, 47 fiches enrichies en références marché, Business Services et TER067 retirés. Interface compacte et bandeau fixe déjà construits disponibles ; consultation des informations masquée, catalogue interne inchangé. 137 nœuds, 47 capacités, 76 comportements, 338 relations et 110 termes. Guide `2026-09-19.2` repris par association explicite.

204 décisions reprises automatiquement et 40 transcriptions après réexamen de 75 valeurs approuvées inchangées ; accord sur l’univers retiré conservé dans l’historique, sans validation nouvelle des compléments. Validation zéro erreur, API identique au snapshot, 120 fiches comparées avec au moins deux URL sources distinctes, huit parcours navigateur réussis. 430 fichiers historiques identiques ; modèle et glossaire du backlog préservés. Serveur disponible sur 8765 sans redémarrage, aucun commit/push. [Rapport et preuves](audits/2026-09-19-release-U473/rapport.md).

## 19 septembre 2026 — contrôle du commit de consolidation

Travaux accumulés du modèle Supply, d’Atlas et des publications jusqu’à v013 préparés pour le commit demandé. Suite complète : 144 tests Python du modèle réussis ; 40 tests du lecteur exécutés, dont 37 réussis et trois ignorés faute de création de liens symboliques Windows ; 82 tests frontend réussis. Validation, build et recette navigateur de l’état final déjà contrôlés lors des interventions et de la release.

Deux fixtures de typage corrigées pour respecter le contrat historique des couches, import du test de pluralité marché compatible avec la découverte complète, dossiers temporaires `app/tmp*/` exclus de Git. Les tests de publication du guide ont été rejoués avec les droits Windows requis. Aucun code métier ou fichier publié modifié par ces corrections. Octets indexés identiques aux fichiers de travail ; les 64 espaces finaux de deux inventaires d’audit historiques sont conservés volontairement, sans reformater leurs preuves.

## 19 septembre 2026 — performance des mises à jour par le LLM

Périmètre précisé par Laurent : lenteur du travail sur le référentiel, pas de l’interface Atlas. Cache de parsing YAML persistant, vérifié par empreintes des contenus et du lecteur, ajouté sous `.runtime/` ; contrôles métier et intégrité toujours exécutés. Commande `inspect_model.py` pour lire les seules fiches et valeurs utiles. Fixtures du guide corrigées pour les droits Windows ; règles d’exécution ciblée ajoutées, huit paragraphes de cadrage déplacés intégralement vers les conventions.

Mesures locales avec cache alimenté : validation 6,031 → 1,005 s, rapport de release 10,323 → 1,742 s, restitution backlog 1,787 → 0,185 s. Après invalidation du seul backlog : validation 2,275 s. Ces mesures ne quantifient pas la génération LLM. 153 tests modèle couverts, avec reprise ciblée réussie d’un renommage Windows transitoirement refusé ; 37 tests lecteur réussis et trois ignorés. 777 fichiers métier et preuves inchangés. Aucune publication ni intervention sur Atlas. [Audit, résultats et limites](audits/2026-09-19-reference-update-performance/rapport.md).

## 19 septembre 2026 — Atlas : navigation et version globale

Accès aux deux glossaires et au guide du méta modèle alignés à gauche. Filtre par type retiré de la recherche et des liens de navigation ; les anciens liens gardent leur texte de recherche et leur publication sans restriction invisible. Version déplacée du bandeau de chaque objet vers le pied de la navigation : « Modèle · v013 », près des statistiques et de Beaumanoir. Le survol précise l’identifiant complet et le suivi courant ou fixe. La rangée devenue vide dans les pages de référence est supprimée.

83 tests frontend réussis et build actualisé. Recette de navigation sur cinq tailles d’écran, inspection des captures desktop/mobile et contrôle ciblé des trois pages de référence, de la recherche et de v012 fixe réussis, sans erreur navigateur. Modèle métier et publications inchangés.

## 19 septembre 2026 — mise en œuvre des suites de l’audit de performance

Dossier réutilisable de réexamen des accords : valeurs et empreintes, changements de fiche, de relations et de glossaire, choix explicites et justification de portée. Aucune reprise automatique depuis l’éligibilité ; valeurs modifiées exclues des transcriptions, portée historique conservée, preuves figées et contrôlées jusque dans l’archive. Commande `prepare_release.py inspect` pour lire les rapports par identifiant et section sans recalcul. Préparation finale en une construction ; procédures intégrées aux instructions et au skill release, copies projet/personnelle synchronisées.

Benchmark maintenu sur une modification éditoriale de Purchase Order, dans des copies isolées des seules entrées utiles : quatre constructions contre deux, candidats identiques hors horodatages, médiane de trois passages 18,332 → 14,531 s (−20,7 %). Les 147 fichiers réels utilisés restent inchangés. Cette mesure ne quantifie ni la génération du LLM ni le réexamen sémantique réel. 52 tests ciblés réussis, dont 40 rejoués après le renforcement final des contrôles. Aucune publication réelle ni intervention Atlas, commit ou push. [Réalisation, mesures et limites](audits/2026-09-19-reference-update-performance/workflow-completion.md).

## 19 septembre 2026 — contrôle du commit des optimisations et de la navigation

Suite complète de 162 tests Python réussie ; contrôle du lecteur réussi et 40 tests exécutés, dont 37 réussis et trois ignorés pour les liens symboliques Windows. Les 83 tests frontend, le build et la recette sur cinq tailles restent valables sur le code inchangé depuis leur réussite. Validation du modèle sans erreur déjà réalisée sur cet état ; skill release validé et copies projet/personnelle identiques. Sur les 777 fichiers suivis par l’audit initial, 776 restent identiques et seul `modeles/README.md` porte l’ajout documentaire attendu du nouveau parcours. Aucun modèle, accord ou historique de publication modifié.

## 19 septembre 2026 — Sources d’inspiration publié dans Atlas, U474–U476

Release **v014 / 2026-09-19.7** préparée puis activée sur demande U476. Une seule fiche enrichie : Supply Chain Orchestration, avec choix d’ouverture, tableau de cinq sources, synthèse et exemple Oracle des 75 pièces livrables sur 100 attendues. Format C et rédaction retenus en U475 ; accord sur le nom repris après réexamen explicite, nouvelle décision limitée à `market_inspiration`. Les comparaisons détaillées gardent leur statut proposé. Relations, autres fiches et glossaire conservés ; publications antérieures inchangées.

Les 84 tests frontend, 39 tests de contrats concernés et le build avaient réussi sur le code inchangé depuis U475. Préparation et validation après publication : zéro erreur ; vues générées et contrôle serveur réussis. API `/api/status`, `/api/model` et `/api/releases` vérifiées : FLOW Atlas, dépôt attendu, espace release, version .7 / révision 14 et chemin du snapshot correspondant. Les cinq références, trois synthèses, l’exemple attribué et les 110 termes du glossaire sont servis ; les liens de glossaire de la fiche résolvent dans cette même publication. L’index HTTP sert le JavaScript compilé du nouveau format. Pas de redémarrage ni de navigateur lancé ; une page déjà ouverte doit être rechargée pour installer le nouveau code de présentation.

[Note de release](modeles/release/2026-09-19.7/release-notes.md), [rapport figé](modeles/release/2026-09-19.7/changes.json), [réexamen de portée](modeles/revisions/2026-09-19.7/decision-review/assessment.yaml). Aucun commit ni push effectué.

## 19 septembre 2026 — reprise complète des Sources d’inspiration, U477

Format métier retenu sur Supply étendu aux 247 fiches visibles du périmètre : 137 objets du modèle et 110 termes. La fiche Supply déjà validée est conservée ; 246 fiches sont rédigées, dont 127 auparavant sans référence. Chaque fiche présente un choix, les noms/périmètres/approches des sources, une comparaison entre elles et avec FLOW, puis un exemple attribué ou une illustration FLOW explicite. 502 comparaisons nouvelles ou réexaminées mobilisent 156 documents primaires distincts ; références trop générales remplacées, limites d’accès consignées, conventions locales et recouvrements partiels expliqués.

Relecture croisée et intégration unique dans les YAML d’autorité ; noms, définitions, responsabilités, relations, accords et univers Supply inchangés. Les rapprochements restent proposés. Index de 1 906 sources actualisé ; validation sans erreur, 10 tests des contrats Sources d’inspiration réussis et restitution backlog régénérée avec 247 rubriques. 613 fichiers protégés conservés octet par octet. Aucun build nécessaire sur le code applicatif inchangé, aucune release, aucun commit ni push ; Atlas reste sur v014 / 2026-09-19.7.

[Rapport et preuves](audits/2026-09-19-sources-inspiration-U477/rapport.md), [documents consultés](audits/2026-09-19-sources-inspiration-U477/consulted-documents.yaml). MKT57–MKT66, ELM327–ELM482, CMP189–CMP193. Catalogue Informations métier masqué et audit des comportements conservés sans extension ni réouverture.

## 19 septembre 2026 — autorité locale des références et proposition de nom, U478–U480

Laurent souhaite nommer le périmètre par sa fonction et précise que les référentiels portent la source de vérité locale de Supply Chain Orchestration, les sources de vérité d’entreprise restant externes. Clarification inscrite dans les conventions et la rubrique Sources d’inspiration de `business-references`. Recherche primaire auprès d’EDM Council et d’Oracle : MKT67–68, ELM483–485, CMP194 ; trois documents avec éditions et passages identifiés.

Authoritative Data Domain recommandé, avec alternatives et définition fonctionnelle dans [la proposition](modeles/backlog/authoritative-data-review-U478.yaml). L’autorité est attachée à un périmètre défini, pas nécessairement bornée au local. L’exemple du seuil distingue porter la valeur applicable et décider de cette valeur. Nom canonique, groupe de présentation, référentiels distincts, rattachements et accords préservés ; aucune conversion de groupe en domaine ni déplacement de capacité. [Fiche précédente](audits/2026-09-19-authoritative-data-U478/before-business-references.yaml) conservée ; publications inchangées.

Index actualisé à 1 915 sources, validation zéro erreur, dix tests Sources d’inspiration réussis, restitution backlog régénérée et contrôles de portée/liens réussis. Aucune release, aucun build, commit, push ni intervention serveur.

## 19 septembre 2026 — propositions de noms des niveaux, U481

Comparaison du découpage courant avec SAP Reference Business Architecture, l’analyse de domaine Microsoft, EDGY, le glossaire BIZBOK 15.0 et le catalogue de processus Dynamics 365. Domain → Area → Capability → Behavior recommandé pour la proximité avec les regroupements Supply SAP ; Domain → Subdomain constitue l’alternative principale. Capability Group / Capability Area, Space / Zone et maintien de Behavior sont explicités dans [la proposition](modeles/backlog/model-level-naming-U481.yaml).

Exemple constant : Supply Chain Orchestration → Inventory Optimization → Replenishment Decision → Target-based Replenishment. Les noms des niveaux ne changent ni la responsabilité locale des références U479 ni automatiquement le groupe Business References ; Authoritative Data proposé comme nom indépendant du rang. Cinq comparaisons méthodologiques documentées, MKT69–70 et ELM486–490 / CMP195. Modèle et glossaires conservés octet par octet, propositions séparées ; index à 1 924 sources et validation zéro erreur. Aucun changement d’interface, release, commit ou push ; audit des comportements non rouvert.

## 19 septembre 2026 — Domain, Area et Authoritative Data adoptés, U482

Backlog et lecture Atlas adaptés à Domain → Area → Capability → Behavior : Supply Chain Orchestration devient le Domain ; six anciens domaines deviennent Areas. Business References renommé Authoritative Data, groupe et six référentiels conservés. Identifiants et responsabilités inchangés, 346 relations du backlog de mêmes types et extrémités, exemples illustratifs compris ; une qualification reformulée à sens constant. Guide, glossaires, feuille de route et instructions courantes actualisés, avec sources historiques et exemples pédagogiques conservés.

Contrats et rendu compatibles avec les anciennes publications. Tests ciblés backend, guide, glossaire et frontend réussis ; validation finale sans erreur et build réussi. Projection du backlog vérifiée : six Areas et 210 liens métier conservés aux trois niveaux. Empreintes et portées des deux champs approuvés actualisés explicitement pour U482, anciennes valeurs capturées. Les publications restent inchangées ; aucun navigateur, release, commit ou push.

[Rapport, portée et vérifications](audits/2026-09-19-domain-area-U482/rapport.md). Atlas affiche toujours v014 / 2026-09-19.7 ; la nouvelle nomenclature du backlog sera visible à la prochaine release.


## 19 septembre 2026 — publication des inspirations et niveaux Domain / Area, U483

Release **v015 / 2026-09-19.8** préparée et activée sur demande U483. Les Sources d’inspiration couvrent désormais les 247 fiches visibles (137 objets et 110 termes), y compris celles sans référence auparavant. Authoritative Data et Domain → Area → Capability → Behavior sont publiés selon U482, avec le guide méthodologique 2026-09-19.3. Les six référentiels restent distincts ; les 47 capacités, 76 comportements et 338 relations sont préservés, avec une qualification reformulée à sens constant.

123 accords repris automatiquement ; 120 après réexamen explicite des champs, frontières, relations et termes liés. Deux décisions nouvelles portent uniquement sur les valeurs modifiées explicitement adoptées U475/U482. Les autres inspirations restent proposées. La projection du guide a été corrigée pour conserver les références contextuelles utiles sans embarquer les métadonnées internes du glossaire méthodologique ; sa version antérieure est capturée.

Préparation et validation finale sans erreur, restitutions générées et contrôle serveur réussi. Atlas sert le snapshot .8 / révision 15, ses 247 inspirations et son guide .3 ; nœuds, relations et glossaire API identiques à la publication. Le guide de .7 reste .2. 558 fichiers historiques vérifiés sans changement. HTML et JavaScript servis conformes au build U482. Aucun redémarrage nécessaire ; recharger une page déjà ouverte pour installer ce nouveau code frontend.

[Rapport et vérifications](audits/2026-09-19-release-U483/rapport.md), [note figée](modeles/release/2026-09-19.8/release-notes.md), [réexamen archivé](modeles/revisions/2026-09-19.8/decision-review/assessment.yaml). Aucun navigateur lancé, commit ou push effectué.


## 19 septembre 2026 — fiche Authoritative Data complétée et publiée, U484

Omission signalée après v015 : les Sources d’inspiration étaient présentes mais la fiche métier restait vide. Ajout de la finalité, de la définition, du périmètre et des limites, de la distinction autorité locale / maîtrise d’entreprise et d’un exemple de conditionnement. Les six référentiels restent distincts ; aucune nouvelle responsabilité ni modification des rapprochements marché. Passages EDM Council CDMC et Oracle ORA revérifiés, appuis ELM484/ELM485/CMP194 conservés.

Correction publiée en **v016 / 2026-09-19.9** dans le prolongement de la demande U483. Un seul nœud modifié, nom repris après réexamen explicite, rédaction ajoutée proposée. Validation zéro erreur, vues générées et serveur contrôlé. API Atlas vérifiée : fiche complète, snapshot .9 / révision 16, guide .3 et autres nœuds, relations et glossaire inchangés. 614 fichiers historiques préservés. Pas de modification frontend, build, navigateur, redémarrage, commit ou push.

[Rapport et preuves](audits/2026-09-19-authoritative-data-U484/rapport.md) ; [note figée](modeles/release/2026-09-19.9/release-notes.md).


## 19 septembre 2026 — Orders comme activation et offre du domaine, U485/U486

Laurent relie l’Area Order Management aux demandes, commandes et dossiers qui activent Supply Chain Orchestration et expriment son offre de services. Recommandation proposée : conserver cette responsabilité pour rendre explicites les prises en charge offertes, leur contenu et leur progression. Comparaisons consultées : séparation capture/orchestration et point d’entrée Production de TM Forum, Case et CaseFile/CasePlanModel CMMN, business artifacts IBM et processus centrés sur les objets. MKT71–72, ELM491–494, CMP196 ; ELM011 réexaminé sans réactiver les anciennes couches.

[Proposition structurée et précision U486](modeles/backlog/order-management-positioning-U485.yaml). Aucun changement du modèle, des glossaires ou de la publication v016 ; aucun renommage, déplacement, release ou build.


## 19 septembre 2026 — nom de l’Area des demandes et Backing Services, U487/U488

Management est jugé trop vague par Laurent pour délimiter D04. Recommandation précédente révisée : étudier Supply Requests (intention d’activation) ou Orders (nom sobre), sans renommage appliqué. Appuis Oracle et TM Forum comparés, différences de périmètre explicites dans CMP197. Laurent confirme que Service Catalog décrit les Backing Services appelés par l’orchestration, distincts de l’offre de prises en charge du Domain. Proposition U485 enrichie avec options, limites et portée U488 ; modèle, glossaires et publication v016 inchangés.


## 19 septembre 2026 — piste Service Orders sans Management, U489

Laurent préfère l’approche Service Order de TM Forum. Proposition : Service Orders pour l’Area D04, avec distinction explicite des Backing Service Orders confiés aux exécutants. Collision D07.b / TER066 / TER075 identifiée ; aucune substitution automatique. Notices primaires TMFC007 et TMF641 relues, rapprochement et limites ajoutés à CMP197 et à l’annexe U485. Modèle, glossaires, rattachements et publication courante inchangés.


## 19 septembre 2026 — demandes internes d’optimisation, U490

Laurent propose des demandes internes activant des opérations orchestrées, illustrées par analyse, simulation, validation et activation d’affectations. Proposition tracée dans l’annexe U485 ; notion commune de prise en charge, types spécifiques et origine distincte de l’intention. Parcours rapproché de D03.p, D03.o et D02.e ; autorisation et dossier restent à définir. Comparaison primaire SAP/Oracle CMP198. Une éventuelle extension de Service Orders dépasse un renommage neutre ; aucun changement du modèle, des parents ou de la release, aucun audit rouvert.


## 19 septembre 2026 — réactions du domaine, clarification U491

Laurent précise que l’optimisation du carnet peut réagir à sa situation ou à une promesse devenue intenable, sans sollicitation du commerce. L’analyse U490 est corrigée : distinguer déclencheur, dossier éventuel et processus ; ne pas imposer un Order interne préalable. Annexe U485 et CMP198 complétés, précédents échanges conservés. Aucun changement du modèle ou de la publication.


## 19 septembre 2026 — demandes internes et réactions, U492–U495

Origine interne/externe des transferts confirmée par Laurent ; vérification primaire SAP, Oracle et Salesforce des traitements réactifs et demandes internes. U494/U495 corrigent une opposition trop forte entre demande et réaction : une détection peut engendrer une demande backoffice, illustrée par la vérification d’identité après détection de fraude. Cet exemple reste attribué à Laurent. Sources MKT73, ELM495–498, CMP199 et annexe U485 enrichis ; les conditions d’automatisation et limites interproduits sont explicites. Proposition de périmètre à instruire ; aucun renommage, changement de modèle canonique, de glossaire ou de publication.


## 19 septembre 2026 — Service Requests et Backing Services, U496/U497

Accord appliqué à D04 : Service Requests et intention présentée, avec demandes internes issues de réactions. U497 corrige la reprise initialement trop étroite : Service Catalog explicite l’offre de Backing Services ; D07.b devient Backing Service Orders ; TER066 et TER075 distinguent demande de prestation et prestation. Fiches, inspirations, liens canoniques, glossaire méthodologique et conventions actualisés. Noms et responsabilités des autres capacités, identifiants et relations préservés ; aucune nouvelle capacité, release ou publication. Les valeurs antérieures et portées d’accord sont conservées dans audits/2026-09-19-service-requests-U496/.


## 19 septembre 2026 — lecture directe du Périmètre, U498

La rubrique partagée des fiches Atlas devient Périmètre. Le paragraphe d’ouverture apparaît dans un encart menthe FLOW, puis les paragraphes suivants sont visibles sans dépliage ni répétition du résumé. Liens, texte public et contenu de la publication consultée conservés. Convention éditoriale ajoutée : le périmètre expose inclusions, exclusions, frontières et principes. Changement de présentation ; aucune release métier nécessaire.


## 19 septembre 2026 — demandes internes, comportements et origine, U499/U500

Proposition documentée d’Order Backlog Optimization Request dans Service Requests : deux angles de comportements, déclenchement et activité, sans hiérarchie supplémentaire ni cycle obligatoire. Références Oracle/SAP reconsultées et U397/U398 réappliquées pour expliciter le métier de chaque demande. Deux indicateurs d’origine Frontoffice/Backoffice proposés relativement au Domain, non exclusifs pour les familles telles que Transfer Order. Événement externe et initiative interne restent distincts. Annexe internal-service-requests-U499.yaml et CMP201 ; aucune modification canonique ou publication.


## 19 septembre 2026 — demande d’optimisation et indicateurs adoptés, U501

Création de D04.s Order Backlog Optimization Request et de ses six comportements BHV088–093 ; deux angles de lecture Déclenchement et Activité, sans niveau supplémentaire. Origines explicitement renseignées : Backoffice pour la nouvelle demande, Frontoffice et Backoffice pour Transfer Order. Trois liens qualifient les coopérations avec Planning, Decision et Supply Assignment ; anciennes relations préservées. Chaque nouvelle fiche dispose de deux références primaires et d’une illustration FLOW.

Schéma, validation Python, restitution Markdown et frontend prennent en charge les métadonnées facultatives sans inférence sur les anciennes publications. Les accords restent qualifiés champ par champ ; détails non présentés et traductions anglaises gardent leur statut éditorial. Captures dans audits/2026-09-19-internal-request-U501/ ; aucune release, aucun changement au catalogue Information ni réouverture d’audit.


## 19 septembre 2026 — publication U502, Urbanisation v017

Release 2026-09-19.10 activée : Service Requests, Backing Services, Order Backlog Optimization Request et ses six comportements, indicateurs d’origine explicites. Snapshot de 144 objets, 48 capacités, 82 comportements, 348 relations et 110 termes ; guide .4 associé. Périmètre sans dépliage et nouveau frontend servis.

232 accords conservés automatiquement, dix repris après réexamen, vingt nouvelles décisions sourcées et deux reprises historiques à portée réduite. Compléments éditoriaux toujours proposés. Préparation, publication, validation et contrôle serveur sans erreur ; API et assets vérifiés, 700 fichiers historiques inchangés. Aucun redémarrage, navigateur, commit ou push. Rapport : audits/2026-09-19-release-U502/rapport.md.


## 19 septembre 2026 — refactoring du parcours de release, U504

Ajout de release.py pour une préparation en une passe puis publication, contrôle Atlas et compte rendu chronométré. Accords explicites enregistrables en amont ; report conservateur à contexte métier identique ; réexamen partiel natif des accords composites. Guide explicite figé dans la préparation, reprises sans republication et signalement des écritures incomplètes. Instructions et skill personnel synchronisés.

101 tests distincts réussis et validation sans erreur. Mesure ponctuelle sur copies isolées : préparation 37,40 → 22,80 s, deux calculs de candidat → un, un réexamen → aucun ; mêmes valeurs métier et portées adoptées. 772 fichiers historiques inchangés ; Atlas reste sur v017. Aucun accord réel, release, commit, push ou redémarrage. Détail : audits/2026-09-19-release-workflow-U504/rapport.md.

## 19 septembre 2026 — personnes, rôles et visibilité des référentiels, U505/U506

Party / Role et son ingestion commencent désormais par les personnes physiques et morales et leur participation aux accords et opérations ; Party et Role sont alignés dans le glossaire. SAP Business Partner est documenté, avec Informatica Customer 360, OMG Commons et FIBO. GS1 est retiré des inspirations actives de Party, sans effacer les preuves antérieures. Les limites des guides Informatica indexés et la différence entre Party au sens large et le périmètre juridique FLOW sont explicites. Noms et accords antérieurs préservés.

Six capacités de connaissance Visibility ajoutées comme propositions au backlog, chacune avec deux documents primaires, un exemple et un rattachement explicite à son référentiel. Consultation distincte de maîtrise externe, de calcul de disponibilité, de consommation contractuelle et d’exécution. Aucun comportement ajouté. Les options de nom et l’évolution d’Authoritative Data vers une Area sont documentées ; la structure de groupe reste inchangée en attente de décision. Capture antérieure et relevé documentaire : audits/2026-09-19-party-reference-U505/. Aucune publication, modification frontend, commit ou push.


## 19 septembre 2026 — Authoritative Data devient une Area, U507

Accord appliqué : Authoritative Data est une Area sœur des six autres Areas de Supply Chain Orchestration ; ses six référentiels restent distincts. Le contrat de présentation accepte explicitement Area → Reference sans autoriser une Area imbriquée ; les capacités gardent leur référentiel parent. Les six Visibility sont adoptées sur name/nature avec leurs rattachements. Party / Role conserve son nom et sa définition restituée est adoptée. Rédactions détaillées et rapprochements marché restent qualifiés séparément.

Le registre amont des accords capture les valeurs et leur contexte final ; l’accord structurel kind est tracé dans l’annexe adoption_U507. Conventions, vocabulaire méthodologique et guide de travail sont alignés. Atlas préserve la présentation des références sous une Area et la lecture du groupe historique. Capture : audits/2026-09-19-authoritative-area-U507/. Aucun nouvel identifiant métier, Behavior, release, commit ou push.


## 19 septembre 2026 — Catalog, Assortment et Agreement, U508

Discussion documentée : D12 désigne une offre produits ; Product Catalog proposé comme nom plus explicite. SAP/Microsoft éclairent un assortiment affecté à des destinataires et périodes ; Oracle montre des accords avec ou sans détail des produits. Un assortiment convenu peut être relié à Agreement, sans faire de tout assortiment un composant contractuel. Annexe catalog-assortment-review-U508.yaml, CMP205. Aucun changement au modèle, au glossaire, aux accords U507 ou aux publications ; aucune extension du chantier Commerce ni du catalogue Information.


## 19 septembre 2026 — Product Catalog et Assortment, U509

Catalog devient Product Catalog, avec déclinaison des noms de ses capacités et de son terme de glossaire. Assortment D16 / TER087 est ajouté comme référence distincte sous Authoritative Data. Agreement peut le référencer ou en figer la sélection convenue ; lien métier qualifié, sans composition universelle. Ingestion et Visibility sont décrites comme capacités proposées selon la convention des référentiels ; conception commerciale et maîtrise d’entreprise restent externes. Aucun Behavior créé.

Les accords U507 restent conservés comme preuves. Le changement de contexte exige un réexamen explicite : le registre permet désormais un remplacement append-only des intentions non publiées, à cible identique et sans extension de champs, ainsi qu’une écriture groupée atomique. Aucune intention périmée n’est reprise automatiquement. Capture : audits/2026-09-19-assortment-U509/. Aucune release, commit ou push.


<!-- release-run:2026-09-19.11 -->
## Publication 2026-09-19.11

Sources : U510. État : published_checks_failed. Atlas vérifié : True. Détail : `.runtime/release-runs/2026-09-19.11/completion.md`.

Reprise des contrôles de cette même version : état final `published`, aucune erreur et Atlas vérifié. Le validateur renvoyait un dictionnaire que le parcours regroupé déstructurait comme un tuple ; correction du lecteur de résultat et ajout de deux tests de régression. Aucune seconde publication. Les sources embarquées U507/U509 du guide ont été complétées avant figement. Deux fixtures de tests anciens ont également été ajustées au format Sources d’inspiration. Suite Python : 242 tests couverts avec rejeu des modules corrigés ; Atlas : 93 tests réussis, build déjà vérifié sur le même code frontend. Guide publié : 2026-09-19.5.
