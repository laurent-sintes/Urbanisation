"""Record a sourced proposal for Protection; do not change the active catalog."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-protection-marche'


def main():
    if OUT.exists():
        raise SystemExit('Study already recorded; do not reapply.')
    OUT.mkdir()
    unchanged_paths = [ROOT/'modeles/backlog/model.yaml', ROOT/'modeles/backlog/glossary.yaml', ROOT/'modeles/backlog/modeling-glossary.yaml']
    for folder in ('release', 'revisions', 'decisions'):
        unchanged_paths.extend(p for p in (ROOT/'modeles'/folder).rglob('*') if p.is_file())
    hashes = {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in unchanged_paths}
    append('connaissance/01-contributions-utilisateur.md', '''## U280

**id**

U280

**date**

2026-09-17

**titre**

Étude marché étendue pour une liste complète des comportements de protection

**texte**

Regarde le marché entièrement pour proposer une liste complete

**contexte et portée**

Demande d’élargir l’étude de Supply Protection au-delà de l’allocation, à la suite des seuils de réassort U279. Rechercher les mécanismes de pénurie, surstock et déséquilibre et proposer une liste documentée ; conserver les frontières des décisions et de l’exécution. Autorise l’étude et ses propositions, pas l’adoption automatique d’un catalogue étendu.''')
    append('connaissance/01-contributions-utilisateur.md', '''## U281

**id**

U281

**date**

2026-09-17

**titre**

Confirmation de l’approche d’étude marché des mécanismes de protection

**texte**

Très bonne approche, c'est ça ce que je veux

**contexte et portée**

Accord sur l’approche annoncée : explorer les principaux ERP et spécialistes, examiner seuils, règles, plafonds, temporalité, dérogations et cas retail, puis justifier les comportements et distinguer paramètres et décisions. Les résultats détaillés de l’étude et la liste candidate ne sont pas encore présentés à ce stade ; aucun nouveau comportement adopté par cet accord de méthode.''')

    # Short selective paraphrases only; the sources remain authoritative for product claims.
    source_rows = [
        ('S01','MKT14','Microsoft','Inventory Visibility inventory allocation','https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation','Page évolutive ; mise à jour affichée 2025-08-13','Business background; Use the allocation APIs; Consume as a soft reservation','documentation produit/API','ouvert et lu','Enveloppes par groupe, opérations et soldes. Ne couvre pas toute la protection FLOW.'),
        ('S02','MKT14','Microsoft','Replenishment methods and quantity modification','https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/replenishment-methods-quantity-modification','Page évolutive ; mise à jour affichée 2026-07-01','Coverage codes; Impact of the order quantity; Min/Max examples','documentation produit','ouvert et lu','Méthodes, seuils et contraintes de lots. Le maximum Min/Max peut être dépassé dans certains cas de multiples.'),
        ('S03','MKT14','Microsoft','Safety stock fulfillment for items','https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-replenishment','Page évolutive ; édition non spécifiée','Set safety stock; Minimum key; Min/max; FEFO; safety stock constraint','documentation produit','ouvert et lu','Niveaux par lieu, dates et variations temporelles ; distinguer sécurité, disponibilité et commande.'),
        ('S04','MKT14','Microsoft','Use the safety stock journal to update minimum coverage for items','https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/safety-stock-journal','Page évolutive ; édition non spécifiée','Overview; Calculate minimum coverage based on historical usage','documentation produit','ouvert et lu','Propositions de valeurs, analyse d’impact et mise à jour effective sont distinguées.'),
        ('S05','MKT13','SAP','Outlining aATP with Supply Protection (SuP)','https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-aatp-with-supply-protection-sup-','Cours S/4HANA ; édition précise non indiquée','Activation; Core/Prioritized Protection; Time Buckets; Consuming Supply Protection','formation produit','ouvert et lu','Groupes, priorités, temporalité, consommation et annulation. Le périmètre SAP SuP est plus étroit que FLOW.'),
        ('S06','MKT13','SAP','Executing Demand-Driven Replenishment in SAP S/4HANA','https://learning.sap.com/courses/exploring-production-planning-in-sap-s-4hana/executing-demand-driven-replenishment-in-sap-s-4hana','Cours S/4HANA ; édition précise non indiquée','Buffer Profiles; Buffer Level Calculation; Manage Buffer Levels; Schedule MRP Runs','formation produit','ouvert et lu','Buffers : sécurité, point de commande et maximum ; propositions puis utilisation des paramètres. DDMRP est une méthode, pas un niveau FLOW.'),
        ('S07','MKT20','Oracle','Policy Assignment Sets','https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faurp/policy-assignment-sets.html','Fusion Cloud 26B','Policy Parameters; Default Policy Values; Policy Overrides; Hierarchy','documentation produit','ouvert et lu','Politiques par segment, dérogations article-lieu et ordre de priorité. Ne pas importer les contraintes techniques de volumétrie.'),
        ('S08','MKT32','Oracle','Activating Items on Replenishment','https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmpug/activating-items-replenishment.htm','Pointeur latest ; numéro de version non affiché dans la page lue','Creating Attributes; Managing Attributes at Item List Level; Replenishment Attributes Window','documentation produit','ouvert et lu','Périmètres article-lieu, mises à jour collectives, présentation et activation/désactivation. Aucune maîtrise de référentiel FLOW déduite.'),
        ('S09','MKT32','Oracle','Manage Scheduled Updates','https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmpug/manage-scheduled-updates.htm','Pointeur latest ; numéro de version non affiché dans la page lue','Create a Scheduled Update; Manage Scheduled Updates','documentation produit','ouvert et lu','Changements datés de paramètres et de statut ; ce n’est pas une simulation de scénario.'),
        ('S10','MKT29','RELEX','Replenishment and allocation','https://www.relexsolutions.com/solutions/automatic-replenishment-system/','Page produit évolutive ; version non indiquée','Key features; store space; seasonal items; new product introductions and ramp-downs','présentation produit','ouvert et lu','Espace, durée de vie et retrait progressif. Appui de cas métier ; opérations détaillées non établies par cette page.'),
        ('S11','MKT29','RELEX','Inventory Planning Software','https://www.relexsolutions.com/solutions/inventory-planning-software/','Page produit évolutive ; version non indiquée','Inventory policies, thresholds and exceptions','présentation produit','ouvert et lu','Seuils et écarts ; aucune preuve d’une interface transactionnelle précise.'),
        ('S12','MKT27','Blue Yonder','Inventory Optimization','https://blueyonder.com/solutions/supply-chain-planning/inventory-optimization','Page produit évolutive ; version non indiquée','Features & Capabilities; Dynamic Segmentation; Multi-echelon Optimization','présentation produit','ouvert et lu','Segmentation et optimisation ; surtout appui des frontières D05, sans détail suffisant de cycle de règle.'),
        ('S13','MKT28','Kinaxis','What is Inventory Optimization','https://www.kinaxis.com/en/inventory-optimization','Article évolutif ; version logicielle non indiquée','Techniques; Key inventory optimization activities','article éditeur','ouvert et lu','Cibles, politiques, visibilité et exceptions ; pas catalogue contractuel des fonctions installées.'),
        ('S14','MKT30','Slimstock','Inventory Management Software — Slim4','https://www.slimstock.com/solutions/inventory-management-software/','Page produit évolutive ; version non indiquée','Key features: stocking policies; stock parameters; network balancing','présentation produit','ouvert et lu','Politiques de stockage liées au cycle produit ; optimisation et rééquilibrage dépassent Protection.'),
        ('S15','MKT31','o9','Allocation & Replenishment','https://o9solutions.com/solutions/merchandise-planning/allocation-replenishment','Page produit évolutive ; version non indiquée','Core Building Blocks; Advanced Building Blocks','présentation produit','ouvert et lu','Distingue moteur, règles, visibilité et transmission des Orders ; allocation peut signifier distribution vers les lieux.'),
        ('S16','MKT23','IBM','Safety stock rules','https://www.ibm.com/docs/en/sip?topic=inventory-managing-safety-stock-rules','Sterling Inventory Visibility / SIP ; version non précisée','Safety stock rules; Network level; Node level','documentation produit','texte indexé lu ; ouverture directe en erreur','Règles par réseau/nœud, mode de livraison et article. Comparaison limitée au passage indexé.'),
        ('S17','MKT23','IBM','Inventory monitor','https://www.ibm.com/docs/en/order-management-sw/9.5.0?topic=monitors-inventory-monitor','Sterling Order Management 9.5.0 ; référence historique','Introduction; inventory availability above/below configured quantities','documentation produit','texte indexé lu ; ouverture directe en erreur','Appui historique de surveillance de seuils ; ne prouve pas la couverture de l’édition courante.')]
    sources = [dict(zip(('id','market_ref','vendor','title','url','edition','passages','nature','access','limit'), row), consulted_at='2026-09-17') for row in source_rows]

    # Candidate keys are local study keys, not reserved model identifiers.
    rows = [
        ('P01','Allocation','Attribuer une enveloppe initiale à un groupe.','Le web reçoit 300 pièces.','Créer des droits utilisables distincts de ressources affectées à une commande.',['S01'],'adopted','BHV011'),
        ('P02','Reallocation','Transférer des droits disponibles entre groupes.','50 pièces de droits web passent aux magasins.','Conserver un total partagé tout en changeant de bénéficiaire.',['S01'],'adopted','BHV012'),
        ('P03','Allocation Release','Restituer les droits inutilisés au disponible commun.','20 pièces non utilisées cessent d’être protégées.','Différencier restitution et changement de bénéficiaire.',['S01'],'adopted','BHV013'),
        ('P04','Allocation Consumption','Imputer un usage à une enveloppe.','80 pièces de droits sont consommées.','Maintenir un solde sans confondre consommation de droits et sortie physique.',['S01'],'adopted','BHV014'),
        ('P05','Allocation Visibility','Consulter les droits alloués, consommés et restants.','Le canal consulte son solde et les mouvements qui l’expliquent.','Lire la disponibilité des droits, distincte de celle du stock.',['S01'],'adopted','BHV015'),
        ('P06','Allocation Consumption Reversal','Corriger ou annuler une imputation de consommation et rétablir les droits selon les règles applicables.','Une annulation de commande rend 10 droits à une enveloppe encore valide.','La libération de droits inutilisés ne corrige pas un usage déjà enregistré.',['S05'],'proposed',None),
        ('P07','Coverage Threshold Setting','Enregistrer et réviser les niveaux de sécurité, déclencheurs, cibles et limites hautes retenus, avec leurs unités et leurs effets.','Pour un magasin : sécurité 40, réassort sous 60, cible 100 ; préciser séparément un éventuel plafond strict.','Distinguer les sémantiques de seuils pour éviter pénurie ou apports excessifs.',['S02','S03','S06','S07'],'proposed',None),
        ('P08','Replenishment Rule Setting','Configurer la méthode de réassort, les contraintes et conditions de renouvellement à appliquer.','Révision chaque lundi, complément jusqu’à la cible, multiples de colis et arrêt à la date de retrait.','Un même seuil donne des résultats différents selon méthode, fréquence et contraintes.',['S02','S07','S08','S10'],'proposed',None),
        ('P09','Consumption Rule Setting','Configurer qui peut utiliser les protections et selon quelles restrictions ou priorités de groupes.','Un groupe prioritaire peut utiliser une ressource sous conditions ; un autre reste plafonné.','Distinguer minimum protégé, plafond et priorité, sans arbitrer les commandes individuellement.',['S01','S05'],'proposed',None),
        ('P10','Protection Scope Assignment','Rattacher une politique de protection à des produits, lieux ou groupes, avec les règles de priorité des rattachements.','Une règle commune couvre un groupe de magasins ; une exception identifie un article-lieu.','Maîtriser les héritages et éviter qu’une règle s’applique au mauvais périmètre.',['S07','S08','S16'],'proposed',None),
        ('P11','Protection Scheduling','Programmer les valeurs et changements de règles sur leurs périodes de validité.','La cible passe de 100 à 60 après la promotion puis revient à 40.','Préparer des changements futurs sans altérer la règle applicable aujourd’hui.',['S03','S05','S09'],'proposed',None),
        ('P12','Protection Activation','Rendre une configuration applicable à son périmètre.','Les nouveaux seuils deviennent effectifs à la date retenue.','Distinguer donnée préparée et règle utilisée ; automatisation possible.',['S05','S08','S09'],'proposed',None),
        ('P13','Protection Deactivation','Suspendre ou arrêter l’application d’une configuration pour son périmètre.','Arrêter le réassort automatique d’un article en retrait, tout en conservant d’autres protections.','Un arrêt de règle diffère d’une suppression de données ou d’une libération de droits.',['S05','S08','S09'],'proposed',None),
        ('P14','Protection Override','Appliquer une dérogation explicite à une règle, avec périmètre, priorité et durée maîtrisés.','Un magasin conserve temporairement une cible différente du groupe.','Préserver la règle commune tout en rendant l’exception visible et réversible.',['S07'],'proposed',None),
        ('P15','Protection Mass Update','Appliquer une modification à un ensemble de protections et rendre compte de ce qui a été appliqué ou rejeté.','Modifier 2 000 couples article-lieu et traiter les exceptions identifiées.','La maîtrise des résultats partiels justifie le comportement ; le nombre de lignes ou l’interface ne suffit pas.',['S04','S08'],'conditional',None),
        ('P16','Protection Visibility','Consulter la configuration effectivement applicable, sa validité et les dérogations qui l’expliquent.','Expliquer pourquoi le magasin utilise une cible de 80 alors que la règle commune indique 100.','Différencier règle, valeur proposée et état effectif ; ne pas doubler Allocation Visibility pour les soldes.',['S03','S07','S09'],'proposed',None),
        ('P17','Protection Monitoring','Détecter et signaler les écarts aux règles de protection et les situations requérant un réexamen.','Stock projeté au-dessus de la limite ou quota presque épuisé.','Passer de la consultation à la détection d’exception ; rattachement à arbitrer avec Inventory Visibility.',['S11','S13','S17'],'conditional',None)]
    candidates = []
    for key,name,result,example,benefit,source_ids,state,node in rows:
        candidates.append({'key':key,'name':name,'result':result,'example':example,'complexity_or_targeted_benefit':benefit,
                           'market_source_ids':source_ids,'state':state,'existing_node_id':node,
                           'evidence_relation':'appui fonctionnel ; décomposition FLOW, pas équivalence normative'})
    boundaries = [
        'Coverage Target Decision détermine les valeurs ; Coverage Threshold Setting configure les valeurs retenues. Stock Allocation Decision reste distincte des opérations sur enveloppes.',
        'Replenishment Decision détermine les apports nécessaires. Configurer une méthode ou un plafond ne crée ni ne lance un Order. D04 et D06 conservent leurs responsabilités.',
        'Supply Assignment lie les ressources aux besoins ; Reservation engage une quantité. Le fait consommant les droits et les corrections doivent prévenir les doubles déductions.',
        'Protection Scheduling programme une applicabilité ; Inventory Planning construit et éprouve des scénarios. Aucune simulation, analyse d’impact ou validation de scénario copiée sous Protection.',
        'Allocation Release restitue des droits encore inutilisés ; Consumption Reversal corrige des droits consommés ; Protection Deactivation arrête une règle. Aucun effet automatique sur un engagement existant présumé.',
        'Replenishment Rule Setting configure les contraintes déjà connues ; les maîtres Product, Agreement et Network restent externes. Les décisions de fournisseur, substitution ou service ne sont pas absorbées.',
        'Les plafonds de stock souhaitables, les cibles Min/Max, les plafonds de consommation et les capacités physiques sont différents. Une cible haute peut être dépassée par des contraintes de lots ; un plafond strict doit être explicitement qualifié.',
        'La configuration d’une limite de place ne mesure pas la capacité opérationnelle : D06 fournit le contexte exécutant pertinent. La conception du planogramme ou de l’assortiment ne devient pas une responsabilité Supply Protection.',
        'La surveillance de seuils peut utiliser Inventory Visibility et des projections ; elle ne recalcule pas une optimisation. Le rattachement exact de P17 reste un arbitrage.',
        'Un surstock existant peut nécessiter redistribution, retour, report/annulation d’apport ou écoulement. Les règles orientent ces réponses mais ne les exécutent pas. La décision de réduire ou reporter des apports reste à vérifier dans D05 ; ne pas la prétendre couverte par la seule définition actuelle de Replenishment Decision.',
        'Finance, démarque commerciale, disposition/destruction, conformité, planification de saison et création de prévision ne sont pas intégrées implicitement à cette capacité. Leurs contraintes utiles peuvent être reçues.']
    mechanisms = [
        ('Droits par groupe et limites de consommation','P01–P06, P09','SAP / Microsoft','Pénurie et concurrence entre usages'),
        ('Sécurité, seuil de réassort, cible et limite haute','P07','Microsoft / SAP / Oracle','Pénurie et surstock'),
        ('Unités ou jours de couverture, niveaux variables dans le temps','P07, P11','Microsoft / Oracle','Éviter des seuils fixes devenus inadéquats'),
        ('Méthode Min/Max, point de commande, cycle périodique et lots','P08','Microsoft / Oracle','Encadrer les apports et le risque d’excédent'),
        ('Minimum de présentation, place disponible et stock de démonstration','P07, P08, P10','Oracle Retail / RELEX','Tenir compte des contraintes magasin sans concevoir les rayons'),
        ('Fin de vie, arrêt progressif, dates de début/fin du réassort','P08, P11, P13','RELEX / Oracle Retail / Slimstock','Limiter le stock résiduel ; dates de saison reçues en entrée'),
        ('Durée de vie résiduelle / péremption','P08, P09, P17','RELEX / Microsoft','Cas conditionnel selon produits ; règle reçue, pas gestion qualité'),
        ('Segments, exceptions article-lieu, règles héritées','P10, P14, P16','Oracle / IBM / Blue Yonder','Éviter ambiguïtés de portée et décisions locales invisibles'),
        ('Activation, arrêt, application collective et lecture de l’effectif','P11–P16','SAP / Oracle / Microsoft','Distinguer préparation et application'),
        ('Détection d’écarts bas/haut et réexamen','P17','IBM / RELEX / Kinaxis','Maîtriser les règles dans la durée, rattachement à arbitrer')]
    study = {'as_of':'2026-09-17','state':'proposed','parent_id':'D02.b','source_refs':['U274','U275','U276','U278','U279','U280','U281','CMP093'],
             'purpose':'Proposition complète pour le périmètre Supply Protection examiné, au-delà des enveloppes ; neuf éditeurs, pas exhaustivité de tout le marché.',
             'catalog_changed':False,'market_comparison':'CMP093','sources':sources,'candidates':candidates,
             'decomposition_rationale_proposed':'Distinguer les résultats métier de partage des droits, configuration de couverture, applicabilité des règles et contrôle de leur usage. Chaque ligne conserve sa complexité ou son bénéfice ciblé ; aucune hiérarchie supplémentaire et aucun comportement automatique par paramètre.',
             'scope_limits':['Aucune liste publique n’établit l’exhaustivité universelle. Couverture recherchée par mécanisme métier sur un panel de neuf éditeurs.', 'Les présentations spécialistes servent de contrôle de couverture, pas de preuve d’opérations transactionnelles détaillées.', 'IBM : accès par texte indexé ; monitor 9.5.0 historique. Oracle Retail latest non figé ; ne pas en déduire une version.', 'Les noms et rattachements P06–P17 sont proposés. P15 et P17 requièrent un arbitrage de maille ou de responsabilité.'],
             'mechanism_coverage':[dict(zip(('mechanism','candidates','support','targeted_benefit'), row)) for row in mechanisms],
             'boundaries':boundaries,
             'not_separate_behaviors':['Un comportement par seuil, SKU, magasin, API, écran ou canal technique', 'Créer/modifier/copier/supprimer chaque paramètre sans résultat métier propre', 'ABC/XYZ, DDMRP, Min/Max ou IA comme niveaux de maturité', 'Un comportement Planning dupliquant les six comportements D05.f'],
             'recommended_review_order':['P07 Coverage Threshold Setting : sécurité, déclencheur, cible, plafond', 'P08 Replenishment Rule Setting et P09 Consumption Rule Setting', 'P06 correction de consommation et frontière Reservation', 'P10–P14 et P16 : portée et vie des règles', 'P15 et P17 : utilité et rattachement à arbitrer'],
             'proposal_location':'modeles/backlog/supply-protection-review.yaml'}
    (ROOT/'modeles/backlog/supply-protection-review.yaml').write_text(dumps(study),encoding='utf-8')
    audit=read(ROOT/'modeles/backlog/behavior-audit.yaml')
    audit['protection_market_U280']={'state':'proposed','source_refs':['U279','U280','U281','CMP093'],
        'proposal_path':study['proposal_location'],'report':'marche/supply-protection-comportements.md','catalog_changed':False,
        'candidate_count':17,'existing_behavior_count':5,'new_candidates':12,'conditional_candidates':['P15','P17'],
        'scope_note':'U281 valide la méthode, pas cette nouvelle liste. Les cinq noms et résultats précédemment présentés sont approuvés U279 ; scopes éditoriaux non adoptés.'}
    (ROOT/'modeles/backlog/behavior-audit.yaml').write_text(dumps(audit),encoding='utf-8')

    new_refs = [('MKT27','Blue Yonder','Inventory Optimization','S12'),('MKT28','Kinaxis','Inventory Optimization','S13'),('MKT29','RELEX','Replenishment and Inventory Planning','S10'),('MKT30','Slimstock','Slim4 Inventory Management','S14'),('MKT31','o9','Allocation & Replenishment','S15'),('MKT32','Oracle','Retail Merchandising Foundation Cloud Service','S08')]
    for identifier,vendor,label,sid in new_refs:
        s=next(s for s in sources if s['id']==sid)
        append('marche/catalogue.md',f'''## {identifier}

- Référence / organisme : {vendor} — {label}.
- Nature et rôle : {s['nature']}, appui fonctionnel des mécanismes de protection ; aucune carte de capacités adoptée.
- Source primaire : {s['url']}
- Édition : {s['edition']}. Consultation : 2026-09-17 ; {s['access']}.
- Passages, compléments et limites : source {sid} et sources du même éditeur dans modeles/backlog/supply-protection-review.yaml ; étude marche/supply-protection-comportements.md.
- Réutilisation : synthèse sélective et liens ; aucun catalogue intégral redistribué. Les annonces produit ne prouvent pas une réalisation Beaumanoir. Oracle Retail produit reste distinct du modèle de référence MKT05.''')
    groups=[('ELM177','MKT14',['S02','S03','S04']),('ELM178','MKT13',['S05','S06']),('ELM179','MKT20',['S07']),('ELM180','MKT32',['S08','S09']),('ELM181','MKT27',['S12']),('ELM182','MKT28',['S13']),('ELM183','MKT29',['S10','S11']),('ELM184','MKT30',['S14']),('ELM185','MKT31',['S15']),('ELM186','MKT23',['S16','S17'])]
    for identifier,ref,ids in groups:
        ss=[s for s in sources if s['id'] in ids]
        append('marche/elements.md',f'''### {identifier}

- Référence : {ref}. Libellés natifs : {' ; '.join(s['title'] for s in ss)}.
- Nature : {' ; '.join(sorted(set(s['nature'] for s in ss)))} ; fonctions ou présentations produit, pas capacités FLOW.
- Éditions, URL primaires, passages et limites d’accès : {' / '.join(ids)} dans modeles/backlog/supply-protection-review.yaml. Consultation 2026-09-17.
- Reformulation et rapprochement : matrice de mécanismes dans marche/supply-protection-comportements.md ; CMP093 proposé.
- Limite : l’étendue fonctionnelle documentée ne prouve pas une décomposition normative ni une réalisation installée. Les règles de synthèse FLOW restent proposées.''')
    append('marche/comparaisons.md', '''## CMP093

- Objet : Supply Protection D02.b, U279–U281 ; compléter les cinq comportements d’enveloppes après la question des seuils de réassort.
- Sources : ELM176 reconsulté ; ELM177–186, neuf éditeurs. Registre détaillé dans modeles/backlog/supply-protection-review.yaml ; rapport marche/supply-protection-comportements.md.
- Relations : appuis fonctionnels partiels et choix de décomposition FLOW ; aucune équivalence normative ni exhaustion de tout le marché revendiquée.
- Résultat proposé : 17 comportements candidats, dont cinq existants, dix compléments de cœur de périmètre et deux conditionnels (mise à jour en masse et surveillance). Détail et bénéfice ciblé par ligne dans l’annexe ; aucun nouveau nœud actif.
- Frontières : configuration de règles versus décision des valeurs, décision des apports, scénarios, affectation aux Orders, réservation et réalisation. Le volet surstock fait apparaître un besoin de vérifier les décisions de réduction/report des apports, non absorbé implicitement.
- Limites : sources spécialistes de présentation ; IBM indexé avec une référence historique 9.5.0 ; Oracle Retail latest non figé. Absence de passage ne signifie pas absence de fonction.
- Auteur/date/statut : Codex, 2026-09-17, proposé. U281 approuve la méthode seulement ; noms, définitions et rattachements nouveaux restent à discuter.''')

    lines=['# Supply Protection — étude des comportements','', 'Étude du 17 septembre 2026, U279–U281. **Proposition, sans ajout au catalogue actif.**', '',
           'Le panel couvre Microsoft, SAP, Oracle (Fusion et Retail), IBM, Blue Yonder, Kinaxis, RELEX, Slimstock et o9. La liste recherche une couverture complète des mécanismes utiles au périmètre FLOW ; elle ne prétend pas épuiser toutes les offres du marché.', '',
           'La proposition détaillée et les sources font autorité dans [l’annexe YAML](../modeles/backlog/supply-protection-review.yaml). Les sections ci-dessous restituent cette annexe ; les familles de lecture ne sont pas des niveaux du modèle.', '',
           '## Lecture marché','',
           'Les ERP documentent précisément les opérations et la vie des paramètres. Les spécialistes complètent la couverture des risques (cycle produit, place, obsolescence, multi-échelon) mais leurs pages publiques donnent moins de preuves sur les opérations transactionnelles. Ces deux niveaux de preuve restent distincts.', '',
           'Trois résultats structurent la recommandation : des seuils sans méthode de réassort sont insuffisants ; une configuration préparée ne prouve pas son application ; prévenir les futurs excédents ne résorbe pas à lui seul le surstock déjà présent.', '',
           '## Mécanismes couverts','', '| Mécanisme | Candidats | Appuis consultés | Bénéfice |','| --- | --- | --- | --- |']
    for m in study['mechanism_coverage']:
        lines.append('| '+' | '.join(m[k] for k in ('mechanism','candidates','support','targeted_benefit'))+' |')
    lines += ['', '## Liste candidate et justification','', 'Cinq comportements existants ; dix nouveaux candidats de cœur de périmètre ; deux candidats conditionnels. Tous seraient directement sous Supply Protection. Aucun sous-comportement.', '',
              '| Repère / nom | Résultat | Exemple fictif | Complexité ou bénéfice justifiant la maille | Appui / statut |','| --- | --- | --- | --- | --- |']
    for c in candidates:
        status={'adopted':'existant U278/U279','proposed':'proposé','conditional':'à arbitrer'}[c['state']]
        lines.append('| '+' | '.join([c['key']+' **'+c['name']+'**',c['result'],c['example'],c['complexity_or_targeted_benefit'],', '.join(c['market_source_ids'])+' ; '+status])+' |')
    lines += ['', '## Points de modélisation à préserver',''] + ['- '+b for b in boundaries]
    lines += ['', 'Les contrôles de cohérence (unités, dates, valeurs incompatibles), la traçabilité et les modalités écran/batch/flux/streaming sont des exigences des comportements concernés. Un comportement supplémentaire ne sera justifié que par un résultat ou une complexité métier propre.', '',
              'P15 est justifié seulement si la prise en charge des résultats partiels et des exceptions constitue un besoin métier ; Oracle atteste la modification collective, pas notre contrat de reprise proposé. P17 reste à arbitrer avec Inventory Visibility ; les calculs d’optimisation et l’analyse d’impact de scénario restent en D05.', '',
              '## Priorités de revue',''] + [str(i+1)+'. '+v for i,v in enumerate(study['recommended_review_order'])]
    lines += ['', '## Sources primaires et limites','', '| Source | Produit / passage | Édition et accès | Portée / limite |','| --- | --- | --- | --- |']
    for s in sources:
        lines.append('| '+s['id']+' ['+s['title']+']('+s['url']+') | '+s['vendor']+' ; '+s['passages']+' | '+s['edition']+' ; '+s['access']+' | '+s['limit']+' |')
    lines += ['', 'Les sources sont consultées le 17 septembre 2026. Les extraits de recherche non retenus (notamment pages Oracle 26D et anciens guides PDF) ne fondent aucune recommandation. Aucune documentation éditeur ne prouve un déploiement Beaumanoir.', '']
    (ROOT/'marche/supply-protection-comportements.md').write_text('\n'.join(lines),encoding='utf-8')
    append('JOURNAL.md', '''## 2026-09-17 — U280/U281 : étude marché étendue de Supply Protection

Neuf éditeurs et 17 sources primaires retenus ; profondeur et limites d’accès distinguées. Liste proposée de 17 comportements (cinq existants, dix compléments, deux conditionnels) dans supply-protection-review.yaml, restituée dans marche/supply-protection-comportements.md. MKT27–32, ELM177–186 et CMP093 ajoutés. Recommandations sourcées et justifiées par bénéfice ou complexité ; frontières avec D03/D05/exécution conservées. Aucun nœud, glossaire ou fichier de publication modifié. U281 valide la méthode d’étude, pas la nouvelle liste.''')
    assert all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    (OUT/'integrity.json').write_text(json.dumps({'unchanged':hashes,'candidate_count':len(candidates),'source_count':len(sources),'vendor_count':len(set(s['vendor'] for s in sources))},indent=2),encoding='utf-8')
    print('Study recorded: 9 vendors, 17 sources, 17 candidates; active model and publications unchanged.')


if __name__=='__main__':
    main()
