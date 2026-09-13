# Journal des évolutions

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
