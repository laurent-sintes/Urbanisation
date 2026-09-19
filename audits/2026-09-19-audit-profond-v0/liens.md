# Audit profond V0 — relations et parcours métier

Les responsabilités principales existent et la structure du graphe est saine. Les lacunes les plus nettes concernent **la représentation des interactions déjà décrites** : scénario du carnet, autorisation de prise en charge, conséquences d’une confirmation fournisseur et chaîne de consignation. Le graphe paraît plus complet qu’il ne l’est pour raconter ces parcours, tout en restant moins lisible que les textes qui l’accompagnent.

L’état initial est conservé dans [model-before-U435.yaml](model-before-U435.yaml), SHA-256 `2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2`. Les [constats et propositions structurés](findings-liens.yaml) ne constituent pas un deuxième catalogue. Ils séparent preuves, interprétations, propositions et inconnus. Les correctifs décrits en fin de document répondent à U435 ; aucune publication n’a été effectuée par ce volet.

## Mesures et limites de lecture

| Contrôle initial | Backlog | Publication courante 2026-09-19.1 | Interprétation |
| --- | ---: | ---: | --- |
| Nœuds | 139 | 135 | Les 4 illustrations sont exclues de la publication |
| Relations totales | 331 | 323 | Même structure ; 8 relations illustratives exclues |
| Relations métier | 198 | 190 | `contains` et `presents` exclus du dénominateur |
| Sens métier renseigné | 190/198 | 190/190 | Les 8 absences concernent les illustrations |
| Rôle `needs` | 177/198 | 177/190 | Dépendance consommateur → fournisseur, pas chronologie |
| Libellé ou verbe court | 0/198 | 0/190 | Le sens détaillé existe mais n’est pas un titre d’arête |
| Conditions non vides | 182/198 | 182/190 | Présence de texte ne signifie pas condition particulière |
| Effets non vides | 182/198 | 182/190 | Même réserve |
| Condition unique exactement générique | 115/198 | 115/190 | Garde-fou utile, insuffisant comme seul contrat |
| Effet unique exactement générique | 130/198 | 130/190 | Rappel de responsabilité, pas résultat détaillé |

Les contrôles exhaustifs n’ont trouvé **aucune extrémité absente, aucun parent structurel multiple, aucun cycle structurel, aucun lien métier sur lui-même et aucun doublon exact `(type, source, cible)`**. Les 216 occurrences de références `model:` dans les champs éditoriaux pointent toutes vers un élément présent. Les comportements ont leur parent explicite ; leurs identifiants historiques ne sont pas utilisés pour reconstruire l’arbre.

La lecture `index.json` → descripteur → snapshot a vérifié les deux empreintes de la publication courante. Pour les éléments communs, les champs métier des nœuds et le contenu des relations sont identiques à l’état initial du backlog. Les huit illustrations non qualifiées ne constituent donc pas huit défauts d’Atlas.

Les 34 occurrences de mentions entre capacités sans paire de lien métier sont des **candidats à examiner**, pas 34 manques avérés. Certaines définissent une frontière : CTP cite Replenishment et Redistribution pour éviter une dépendance obligatoire. Stocktaking cite Inventory Tracking alors que le chemin utile passe déjà par les mouvements et la visibilité. Les relations ne sont ni transitives par défaut ni à multiplier pour recopier toutes les mentions.

Seuls huit comportements participent directement à des liens métier. Cela ne révèle pas 66 comportements orphelins : la dépendance de leur capacité peut suffire. Aucun lien par comportement n’est exigé. Les quatre relations métier `urbanist_validated` ne valident que leurs extrémités ; les qualifications restent éditoriales. Aucun pourcentage global d’accord n’est déduit de cette étiquette.

Les mesures complètes et références sont dans [metrics-liens.yaml](metrics-liens.yaml) et [inventaire-liens.md](inventaire-liens.md). Reproduction :

```powershell
python audits/2026-09-19-audit-profond-v0/audit_links.py --model audits/2026-09-19-audit-profond-v0/model-before-U435.yaml
# État corrigé, dans des sorties distinctes :
python audits/2026-09-19-audit-profond-v0/audit_links.py --tag after-U435
```

## Six interactions prioritaires

Les spécifications proposées, conditions, effets, sources et inconnus figurent dans `top_six_proposed_links` du [registre YAML](findings-liens.yaml). Cette table explique leur intérêt sans imposer de séquence technique.

| Proposition | Interaction | Preuve de besoin | Intérêt avant présentation |
| --- | --- | --- | --- |
| PLNK-01 / LNK-02 | Order Backlog Planning → Fulfillment Plan Decision | D03.p.scope mobilise la décision ; D03.p ne possède qu’un lien vers Lifecycle | Montrer ce que Planning compare et prépare |
| PLNK-02 / LNK-03 | Process Orchestration → Order Lifecycle Management | BHV039.scope articule autorisation puis coordination ; aucun lien entre ces capacités | Montrer qui autorise et ce que l’orchestration respecte |
| PLNK-03 / LNK-04 | Consignment Replenishment Order → Service Reconciliation | D04.r explique réceptions et reliquats ; les cinq autres types Order mobilisent déjà ce rapprochement | Expliquer une réception partielle sans transformer l’apport en achat |
| PLNK-04 / LNK-04 | Consigned Inventory Management → Record Inventory Movements | D01.h.scope nomme le responsable des mouvements | Distinguer fait de stock, propriété et conséquence de l’accord |
| PLNK-05 / LNK-05 | Promise Management → Supplier Confirmation | BHV078.scope nomme le réexamen de promesse, sans lien correspondant | Montrer l’effet d’un report fournisseur sans réviser automatiquement la promesse |
| PLNK-06 / LNK-06 | Inventory Planning → Consignment Replenishment Order | Planning met en action achats et transferts ; l’apport non acheté existe dans D04 | Rendre visible la mise en action du réassort consigné |

PLNK-03 est une **mise en cohérence plausible** : le besoin de réception et reliquat est explicite, mais l’attribution à Service Reconciliation reprend la convention des autres Orders. Les règles d’imputation restent ouvertes. PLNK-04 ne fixe pas où se produit chaque écriture comptable ou de propriété. Ces limites sont conservées dans les qualifications.

Le lot consignation inclut les compléments lisibles dans ses descriptions : Lifecycle, Structuring, Archiving, Inventory Tracking, achat éventuel et retour fournisseur. Il n’en découle ni acquisition à chaque vente, ni achat à la réception, ni droit automatique de destruction.

## Parcours bout en bout éprouvés

Ces parcours sont des **épreuves de cohérence de la cible**, sans preuve de réalisation installée. Les étapes expriment les responsabilités à relier ; les flèches `needs` ne définissent pas une chronologie universelle.

| Scénario | Couverture existante | Rupture ou information à mieux valoriser | Critère V0 |
| --- | --- | --- | --- |
| Vente de 100, disponibilité 60, promesse et lancement partiel | Sales → Promise ; Promise → ATP/CTP/PTP/échéancier ; Assignment → plan ; Sales → Lifecycle ; D06 → prestations ; rapprochement → Sales | Planning ne rejoint pas sa décision ; l’orchestration ne représente pas sa dépendance à l’autorisation | 60 autorisées et 40 en attente distinctes de quantités affectées, réservées ou livrées ; PLNK-01/02 |
| Achat 100 vendredi, fournisseur répond 60 vendredi et 40 mardi | Purchase et Supplier Confirmation ; Replenishment/Initial Stocking lisent les achats attendus ; Stock Procurement lit les réceptions | Engagement fournisseur sans lien explicite vers Promise ; fraîcheur de la ressource future à préciser avant implémentation | Acceptation fournisseur, disponibilité future et promesse client distinctes ; PLNK-05 |
| Consignation : implantation 500, réception partielle, consommation, fin de saison | Agreement ; D04.r et ses deux intentions ; D01.h et ses trois comportements ; D05 besoins | Demande isolée de ses fonctions communes et régime isolé des mouvements/suites | Fin de demande distincte de fin du régime ; réception distincte de propriété ; PLNK-03/04 |
| Retour client : 10 attendues, 6 reçues, stock/réparation/renvoi | Customer Return → Disposition ; Disposition → inspection/stock ; Return to Supplier → Supplier Return ; D06 prestations | Prestations hors vente peu reliées aux intentions ; interfaces commerciales/financières externes | Reçu, accepté, orienté et disponible distincts ; renvoi différent d’un avoir ; LNK-07/08 |
| Réassort ou implantation par achat, transfert ou consignation | Planning mobilise décisions, Purchase et Transfer ; D04.r mobilise besoins initiaux/continus ; BHV083–085 présents | Mise en action de l’apport consigné absente ; origine des restrictions de modification à préciser | Ne pas corriger deux fois le besoin ; refus/prise en compte partielle explicables ; PLNK-06 |
| Aléa de prestation après libération | Tracking → adaptation/orchestration ; adaptation → Promise Revision ; orchestration → services/adaptation/suivi | Lien vers autorisation/Hold manquant | Adapter un plan ne lève pas un Hold, n’annule pas un Order et n’efface pas une réalisation ; PLNK-02 |

La couverture des retours est déjà significative. Cette lecture ne justifie pas de rouvrir P04, P10 ou P12 de U431 ni d’ajouter un comportement de supervision. LNK-07 vise à exposer les besoins de prestations hors vente, puis à choisir la bonne interaction par scénario ; il ne prescrit pas cinq liens identiques ni cinq nouveaux comportements.

## Atlas : information préservée, libellés corrigés

L’inspection statique confirme la conservation des relations originales et qualifications dans l’adaptateur, la projection des comportements vers leur capacité sans perte des extrémités d’origine, et l’affichage du sens, des conditions, effets, réserves et sources dans l’inspecteur. Les relations internes aux regroupements restent inspectables. Aucune perte de données brutes n’a été établie.

Le code initial imposait cependant « A besoin de » à toutes les arêtes de cette famille, même avec un futur `fields.label`. **Le correctif U435 est réalisé dans le code** : une expression explicite et identique sur toutes les relations regroupées est affichée aussi pour `needs`. Des expressions différentes ou absentes conservent le titre de famille et leurs détails d’origine. Le rôle et l’orientation restent inchangés.

Le schéma ne prévoyait pas encore `relation.fields`, malgré sa lecture par Atlas. Il accepte désormais uniquement `label` et `verb`, chaînes non vides optionnelles. Les raccords d’intégrité sont inclus : comparaison au snapshot figé, contrôle de révision lors d’un changement et vérification des extrémités approuvées même en présence de champs d’affichage. Le contrat est documenté dans `modeles/README.md`.

Le correctif ne rend pas le backlog visible dans Atlas. La publication courante conserve ses octets ; présenter les nouvelles données dans Atlas nécessitera une nouvelle release explicitement demandée.

## Intégration et vérifications

U435 autorise les corrections évidentes ou plausibles. Le script [apply_link_fixes.py](apply_link_fixes.py) a été exécuté par l’intégrateur : **12 liens qualifiés et 12 expressions sur des relations existantes** ont été ajoutés. Il archive les octets immédiatement antérieurs, refuse rejeu/concurrence, augmente une seule fois la révision des relations modifiées et inscrit U435 sans fabriquer d’adoption. Le [manifeste d’application](modifications-liens-appliquees.yaml) conserve les changements exacts.

Les nouvelles relations restent `proposed` / `under_instruction`. Les expressions ajoutées restent éditoriales ; ce lot ne réécrit aucune qualification existante. Les cinq relations U436 (`REL-NEEDS-U290-018/019/025/029/030`) sont exclues pour leur intégration séparée : **seule la réservation bloque les usages concurrents ; l’affectation seule ne les bloque pas**. LNK-08 décrit l’état initial ; U436 remplace la question ouverte A01 dans le suivi courant sans réécrire U431.

Le contrôle après intégration générale, SHA-256 `bc6331a9e199a4723199f39b26ceb3e94ab5caded35e4075fd91d8054acd7347`, donne **343 relations dont 210 métier, 29 expressions courtes et aucune rupture structurelle**. Les 29 expressions comprennent les 24 de ce lot et les cinq ajoutées séparément lors d’U436. Les 217 références textuelles `model:` sont résolues. Les nouvelles [métriques](metrics-liens-after-U435.yaml) et le nouvel [inventaire](inventaire-liens-after-U435.md) sont séparés des preuves initiales. La publication demeure à 323 relations dont 190 métier, avec ses empreintes intactes.

Vérifications achevées :

- **13 tests du graphe** : labels/verbes, sens des flèches, agrégats hétérogènes, publications historiques. Le premier essai avait rencontré `spawn EPERM` au lancement de Python ; le même test a réussi après escalade autorisée.
- **44 tests Python** des contrats, préparation de publication et nouveaux libellés : modifications après gel et absence de révision rejetées.
- **7 tests existants de cycle de vie**.
- Lecture du registre YAML et contrôle syntaxique du script d’application. Validation finale du backlog et build frontend confiés à l’intégration générale ; aucun navigateur ouvert.

Les quatre tests des nouveaux libellés ont également été rejoués sur l’état final `bc6331a9…`, avec succès ; ils sont déjà compris dans les 44 tests Python ci-dessus. L’intégrateur a confirmé la validation globale sans erreur, le rendu backlog et le build frontend.

## Références externes consultées

Le [tutoriel ArchiMate de The Open Group Community](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/) distingue échanges, causalité et fourniture de fonctionnalité ; leurs orientations ne sont pas automatiquement identiques. Cela appuie le sens des liens FLOW et la conservation de `needs` comme dépendance. Le tutoriel n’est ni une norme adoptée ni une équivalence de maille avec les comportements FLOW.

Microsoft [Set up consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment) distingue demande d’apport, réception en propriété fournisseur et changement ultérieur de propriété. Ce découpage conforte les responsabilités déjà adoptées. Son exemple de consommation de production ne prouve ni règle retail universelle ni pratique Beaumanoir.

Microsoft [Release to warehouse](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/release-to-warehouse-process) relie les lignes libérées aux shipments, loads et travaux. FLOW garde une abstraction plus haute : autorisation, orchestration et réalisation. Aucun mécanisme Microsoft n’est importé comme capacité. Les consultations datent du 19 septembre 2026 ; localisateurs, limites et position FLOW figurent dans le registre YAML.
