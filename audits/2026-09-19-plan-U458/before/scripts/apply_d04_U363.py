"""Apply D04 refactoring agreed in U363, with preserved identities and scoped evidence."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'audits/2026-09-18-d04-U363'
TYPES = ['D04.i', 'D04.j', 'D04.k', 'D04.l', 'D04.m']


def append(path, text):
    with (ROOT/path).open('a', encoding='utf-8') as f:
        f.write('\n\n'+text.strip()+'\n')


def main():
    assert not OUT.exists(), 'U363 already applied.'
    OUT.mkdir()
    for file in ['model', 'glossary', 'behavior-gap-audit', 'order-lifecycle-behaviors', 'd04-refactoring', 'assignment-terminology']:
        (OUT/(file+'-before.yaml')).write_bytes((ROOT/('modeles/backlog/'+file+'.yaml')).read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    append('connaissance/01-contributions-utilisateur.md', '''## U363

**id**

U363

**date**

2026-09-18

**titre**

Appliquer la refonte des Orders et la distinction Split / Spread

**texte**

On est d'accord. Tu peux prendre en compte les modifs ?

**contexte et portée**

Demande d’intégration des modifications discutées U351–U362 : regroupement des cinq variantes sous Order Type, mutations internes sous Lifecycle, Structuring et Archiving séparés, mode brouillon et distinction Split/Spread. Les identifiants des variantes sont conservés. Les noms déjà présentés et principes sont retenus dans leur portée ; nouveaux libellés développés, définitions, exemples et contrats éditoriaux ne sont pas validés globalement. Aucun algorithme de décision Spread autonome, objet chapeau obligatoire, release ou push demandé.''')
    mp = ROOT/'modeles/backlog/model.yaml'
    m = read(mp); before = deepcopy(m)
    n = {x['id']: x for x in m['nodes']}
    review = read(ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml')
    assert not ({'D04.p', 'D04.q'} | {f'BHV{i:03}' for i in range(38,45)}) & n.keys()
    now = datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    refs = ['U363', 'CMP133']

    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=now,
                    recorded_by='Codex', source_refs=['U363'], validated_fields=list(approved),
                    value_sha256={f:value_hash(values[f]) for f in approved},
                    note='U363 : principes et rattachements intégrés ; descriptions développées et contrats restent éditoriaux.')

    def markets(items, position):
        result = deepcopy(items)
        for c in result:
            c['source_refs'] = list(dict.fromkeys(c['source_refs']+refs))
            c['flow_position'] = position+' U363 applique la structure ; les correspondances marché restent proposées.'
        return result

    def add(ident, kind, fields, approved=('name',)):
        node = dict(id=ident,revision=1,kind=kind,layer='transactional',fields=fields,source_refs=refs,
                    source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u363'),adoption_ids=[],
                    review=dict(state='partial',note='Portée et principes adoptés ; détails éditoriaux proposés.'),lifecycle=life(fields,approved))
        m['nodes'].append(node); n[ident]=node
        return node

    def touch(node):
        node['revision'] += 1
        node['source_refs'] = list(dict.fromkeys(node['source_refs']+refs))

    def contains(parent, child, ident=None):
        rel=dict(id=ident or 'REL-BEHAVIOR-'+child,revision=1,type='contains',source_id=parent,target_id=child,source_refs=['U363'],review=dict(state='accepted',note='Rattachement de la refonte U363.'))
        rel['lifecycle']=life(rel,['type','source_id','target_id']);m['relations'].append(rel)

    def needs(consumer, provider, meaning):
        rel=dict(id='REL-NEEDS-U363-'+consumer+'-'+provider,revision=1,type='relates-to',source_id=consumer,target_id=provider,source_refs=refs,
                 qualification=dict(role='needs',meaning=meaning,conditions=['Lorsque le contexte et la portée de l’Order le nécessitent.'],effects=['Consommer le résultat sans absorber la responsabilité du fournisseur.'],scope='Contrat métier proposé, sans appel logiciel imposé ni séquence universelle.'),review=dict(state='proposed',note='Précision éditoriale ; pas d’adoption implicite du contrat.'))
        rel['lifecycle']=life(rel);m['relations'].append(rel)

    type_markets=markets(review['architecture_direction_U357']['market_comparisons'], 'Order Type regroupe les variantes métier achat, vente, transfert et retours. Aucun référentiel de types à administrer ou Order universel imposé.')
    add('D04.p','capability',dict(name='Order Type',definition='Gérer les Orders selon leur finalité métier — vente, achat, transfert, retour client ou retour fournisseur — en appliquant les informations, règles et résultats propres à chaque variante.',
        nature='action',finality='Conserver une commande exploitable et un reste à satisfaire explicable dans chacune des finalités métier.',
        scope='Enregistrer, rechercher, consulter et modifier le contenu des commandes selon leur type ; supprimer uniquement les enregistrements dont l’état et les liens l’autorisent. Préserver origine, versions et réalisations. Le clonage simple réutilise un contenu pour créer une nouvelle demande ou de nouvelles lignes ; il ne copie pas implicitement les promesses, réservations ou états fermes.\n\nLe CRUD ne devient pas quatre comportements identiques. Lifecycle gouverne les mutations et leurs autorisations, Structuring la composition persistante entre Orders, Archiving leur conservation historique. Achat et vente peuvent représenter des perspectives distinctes au moyen de commandes liées ; le type n’est pas un état librement interchangeable. Les cinq variantes gardent leurs informations et règles spécifiques, sans cycle universel.',
        decomposition_rationale='Les variantes diffèrent par l’engagement, les parties, le sens du flux et le reste à servir, recevoir, transférer ou retourner. Ces différences métier justifient les comportements ; le CRUD commun et les mécanismes Lifecycle ne sont pas recopiés sous chacun.',market_comparisons=type_markets))
    contains('D04','D04.p','REL-MEMBER-D04.p')
    for ident in TYPES:
        node=n[ident];touch(node);node['kind']='behavior'
        node['fields'].pop('nature',None)
        node['fields']['scope']=node['fields']['scope'].replace('Les transformations de structure mobilisent [Order Structuring](model:D04.n) ; les autorisations et restrictions de progression mobilisent [Order Lifecycle Management](model:D04.o). Ces capacités transversales sont des responsabilités complémentaires, pas des sous-capacités répétées sous chaque type.',
            'Les mutations internes, dont le split avec filiation, mobilisent [Order Lifecycle Management](model:D04.o). La composition métier persistante d’un ensemble d’Orders mobilise [Order Structuring](model:D04.n). La conservation historique mobilise [Order Archiving](model:D04.q). Ces responsabilités restent distinctes du contenu propre au type.')
        node['fields']['scope'] += '\n\nU363 : variante terminale d’Order Type ; identifiant historique conservé. Consultation, création, modification, suppression admissible et copie de contenu restent possibles selon les règles de la variante. La suppression d’un brouillon, l’annulation d’une demande engagée et la purge d’une archive sont distinctes.'
        node['fields']['market_comparisons']=deepcopy(type_markets)
        node['review']['note']='Reclassé en comportement d’Order Type U363 ; nom et responsabilité propres au type conservés. Détails éditoriaux proposés.'
        rel=next(r for r in m['relations'] if r['type']=='contains' and r['target_id']==ident)
        rel['revision']+=1;rel['source_id']='D04.p';rel['source_refs'].append('U363');rel['lifecycle']=life(rel,['type','source_id','target_id'])
        rel['review']=dict(state='accepted',note='U363 remplace le rattachement direct au domaine par Order Type ; preuve historique capturée.')

    draft=review['draft_and_structuring_U353_U354']['draft_proposal']
    draft_markets=review['draft_and_structuring_U353_U354']['market_comparisons'][-1:]
    add('BHV038','behavior',dict(name='Order Drafting',definition=draft['definition'],finality=draft['benefit'],scope=draft['example']+'\n\n'+draft['boundary']+'\n\nMécanisme de préparation différée : sauvegarder et reprendre un contenu incomplet avant soumission. Créer, éditer et retirer un brouillon sont ses opérations ; il n’impose ni validation humaine ni exclusion automatique des calculs de disponibilité. Libellé anglais éditorial ; principe du mode brouillon adopté U354/U363.',market_comparisons=markets(draft_markets,'Préparation en brouillon sous Lifecycle ; contenu par type et effets de réservation restent distincts.')),approved=())
    contains('D04.o','BHV038')
    for number,p in enumerate(review['coverage_review_U351']['proposals'],39):
        ident=f'BHV{number:03}'
        add(ident,'behavior',dict(name=p['name'],definition=p['definition'],finality=p['decomposition_rationale'],scope=p['example']+'\n\n'+p['boundary']+'\n\nPortée : Order, ligne ou quantité selon le contexte ; conditions propres au type et à son avancement. Les modes écran, batch, API ou flux ne sont pas des comportements supplémentaires.',market_comparisons=markets(p['market_comparisons'],'Mutation interne d’un Order sous Lifecycle ; décision spécialisée, orchestration et réalisation gardent leurs responsabilités.')))
        contains('D04.o',ident)
    split_markets=review['split_spread_U360']['market_comparisons'][:1]
    add('BHV044','behavior',dict(name='Order Splitting',definition='Scinder un Order ou ses éléments en parties traitables distinctement, en préservant la filiation, la cohérence des quantités et les engagements applicables.',finality='Adapter le traitement d’une demande sans la dupliquer ni perdre la trace de ses parties.',
        scope='Exemple fictif : un Order de 100 pièces devient deux Orders de 60 et 40, liés à leur origine. Un split peut également porter sur les lignes ou échéances sans créer deux commandes autonomes. Le parent historique et les fragments ne sont pas comptés comme trois demandes. Définir le devenir de l’original et les conditions de mutation au regard des quantités déjà réalisées et des éléments gelés.\n\nLe choix des sites, des dates ou des parts reste du ressort des décisions spécialisées. La mutation applique le choix autorisé ; elle ne recalcule pas silencieusement une autre promesse. D06 ou les exécutants gardent leurs tâches. Si un engagement d’ensemble reste actif et sa composition doit être maintenue, mobiliser Structuring.\n\nSplit coupe les commandes ; Spread répartit des ressources entre commandes existantes. Un plan de répartition peut motiver un split ultérieur, sans les confondre. Le clonage peut ajouter une nouvelle demande ; il n’est pas un split. Nom développé Order Splitting éditorial, notion Split adoptée U362/U363.',market_comparisons=markets(split_markets,'Split comme mutation avec filiation ; composition persistante distincte.')),approved=())
    contains('D04.o','BHV044')

    struct=n['D04.n'];touch(struct)
    struct['fields'].update(definition='Construire et maintenir la composition métier d’un ensemble d’Orders et la cohérence entre la demande d’ensemble et ses composants.',finality='Conserver une lecture cohérente de l’ensemble, de ses engagements et de sa satisfaction au fil des évolutions de ses composants.',
        scope='Maintenir les rattachements et les règles de cohérence d’une composition persistante : agrégation des quantités, lien au besoin d’ensemble, effets des remplacements et regroupements autorisés, lecture de la satisfaction sans double comptage. Un Order chapeau peut porter cet engagement si le métier le requiert ; aucun nouvel objet ou schéma parent-enfants obligatoire n’est introduit.\n\nExemple fictif : une demande d’implantation reste suivie comme un ensemble pendant que plusieurs Orders de transfert la réalisent. Remplacer un composant doit conserver la traçabilité et la cohérence de l’engagement d’ensemble. Il ne suffit pas de sommer des demandes indépendantes ni de compter simultanément chapeau et composants.\n\nUne simple trace de filiation après scission relève de Lifecycle / Order Splitting. La recomposition ou consolidation d’un ensemble durable relève de Structuring ; un simple déplacement d’échéance relève de Rescheduling. « Spread » est réservé ici au sens qualifié SAP ARun : répartition de ressources entre besoins, hors mutation et composition des Orders. Répartir une demande en échéances doit être nommé explicitement.\n\nStructuring ne décide pas la meilleure promesse ou l’affectation et n’orchestre pas les tâches logistiques. Les périmètres précis de composition, homogènes ou entre types, restent à éprouver ; pas de cycle universel ni de nouveau comportement systématique.',
        market_comparisons=markets(review['structuring_boundary_U355']['market_comparisons'],'Composition persistante justifiant Structuring séparé. Une hiérarchie de lignes ou une filiation de split seule n’est pas équivalente.'))
    for r in m['relations']:
        if r['type']=='relates-to' and r['target_id']=='D04.n' and r['source_id'] in TYPES:
            r['revision']+=1;r['source_refs'].append('U363');r['qualification']['meaning']='A besoin des liens de composition persistants et des règles de cohérence de l’ensemble auquel participe l’Order.'
    parent=n['D04.o'];touch(parent)
    parent['fields']['scope']=('Gouverner et appliquer les mutations autorisées d’un Order dans sa préparation, ses engagements et sa progression. Les neuf comportements décrivent des mécanismes combinables, pas neuf états obligatoires : Drafting, Firming, Freezing, Release, Hold & Resume, Rescheduling, Cancellation, Closure et Splitting.\n\n'
        'Le contenu spécifique demeure géré selon Order Type. Le mode brouillon organise la préparation ; le CRUD reste explicite sans quatre comportements artificiels. Distinguer suppression admissible d’un brouillon et annulation du reste engagé. Une copie prépare une nouvelle demande, sans reprendre automatiquement ses garanties.\n\n'
        'Affermir ne libère pas automatiquement, libérer ne constate pas le démarrage physique. Hold bloque une progression ; Freezing limite des modifications. Reporter une échéance ne lève pas une attente. Annuler retire un besoin restant sans effacer les réalisations ; clôturer explique la fin opérationnelle et le reliquat. Archiver est une responsabilité séparée.\n\n'
        'Split coupe une commande ou ses éléments avec filiation et contrôle des quantités. Structuring garde la composition durable entre Orders. Spread ARun répartit les ressources entre commandes : décision des parts et application par Supply Assignment restent hors de cette mutation.\n\n'
        'Exemple fictif : sur un transfert de 100 pièces, 60 sont autorisées et 40 attendent. Reporter les 40 au lundi ne lève pas leur attente. Une scission éventuelle conserve l’origine ; les quantités déjà reçues ne sont pas annulables comme si elles n’avaient jamais existé. L’application d’un plan peut déclencher ces mutations autorisées ; Supply Assignment reste responsable des liens ressources-commandes.\n\n'
        'Conditions et autorités sont propres aux types d’Orders ; automatisation possible. D03 conserve promesses et décisions, D06 les prestations, faits et adaptations d’exécution. Aucun cycle universel aux Supply Orders ou Service Orders ; compensation du processus dans la couche processus.')
    parent['fields']['decomposition_rationale']='Préparation différée, engagement ferme, stabilité face aux optimisations, autorisation, interruption, changement d’échéance, retrait du besoin, terminaison et scission modifient chacun les pratiques et responsabilités métier. Leurs conditions et effets partiels justifient les mécanismes ; pas une décomposition par bouton, statut technique ou interface.'
    parent['fields']['market_comparisons'] += [c for ident in range(38,45) for c in n[f'BHV{ident:03}']['fields']['market_comparisons']]
    archive=review['crud_and_archiving_U352']['archiving_proposal']
    add('D04.q','capability',dict(name='Order Archiving',definition=archive['definition'],nature='management',finality=archive['decomposition_rationale'],scope=archive['example']+'\n\n'+archive['boundary']+'\n\nPréserver les identifiants, versions utiles et liens aux engagements et réalisations, afin de consulter et expliquer les Orders historiques sans les remettre automatiquement dans le stock de commandes à satisfaire. Définir les conditions d’éligibilité, de conservation et de retrait définitif selon le contexte. Clôture opérationnelle, conservation de versions, archivage et purge ne sont pas synonymes. Aucune durée légale ou architecture technique imposée. Les restrictions de Microsoft sur les commandes intersociétés sont une limite produit, pas une règle FLOW adoptée.',market_comparisons=markets(archive['market_comparisons'],'Archiving est une capacité sœur distincte de Lifecycle, pas son comportement. Préserver consultation et liens ; pas d’architecture de stockage imposée.')))
    contains('D04','D04.q','REL-MEMBER-D04.q')
    needs('D04.q','D04.o','A besoin de la situation opérationnelle et du devenir des reliquats pour apprécier l’éligibilité à l’archivage.')
    needs('D04.q','D04.n','A besoin des liens de composition à préserver dans la conservation historique.')
    needs('D04.q','D04.p','A besoin du contenu, des versions et des règles propres aux types d’Orders à conserver.')
    needs('D04.o','D04.n','A besoin de connaître les engagements de l’ensemble qu’une mutation d’un composant doit préserver.')
    spread=markets(review['spread_arun_U361']['market_comparisons'],'Spread est une politique de répartition des ressources entre commandes. Les décisions déterminent les parts ; Supply Assignment applique les liens. Aucun agrégat décisionnel ou comportement automatique ajouté.')
    touch(n['D02.e']);n['D02.e']['fields']['scope']+='\n\nU362/U363 : Spread (sens SAP ARun) répartit les ressources entre commandes existantes ; il ne coupe pas les commandes. La règle de répartition détermine les parts dans les décisions spécialisées, puis Supply Assignment matérialise leurs affectations. Exemple simplifié : besoins de 100 et 200, stock de 150, prorata donnant 50 et 100 ; les demandes restent de 100 et 200. Quotas, priorités et engagements peuvent changer le résultat. Aucun nouvel optimiseur ou parent de décision Spread adopté.'
    n['D02.e']['fields']['market_comparisons']+=spread
    touch(n['D04']);n['D04']['fields']['definition']='Gérer les Orders transactionnels de la Supply selon leur type métier, gouverner leurs mutations, maintenir leurs compositions et assurer leur conservation historique, en distinguant contenu, promesse et exécution.'
    n['D04']['fields']['scope']='Quatre capacités : Order Type, Order Lifecycle Management, Order Structuring et Order Archiving. Les cinq variantes vente, achat, transfert, retour client et retour fournisseur sont des comportements d’Order Type. Les mécanismes Lifecycle sont communs sans imposer un cycle identique. Structuring porte la composition persistante ; Archiving conserve la trace historique. Split transforme les commandes ; Spread répartit des ressources entre commandes et relève des décisions et de Supply Assignment.'
    mp.write_text(dumps(m),encoding='utf-8')

    # Lexical evidence stays separate from methodological vocabulary.
    gp=ROOT/'modeles/backlog/glossary.yaml';g=read(gp)
    for ident,name,definition,notes,comparison in [
        ('TER081','Split','Scission d’une commande ou de ses éléments en parties distinctes, avec préservation de leur filiation.','U362 : « coupe des commandes ». Ne crée pas une demande supplémentaire ; contrôler les quantités et préciser le devenir de l’original. Les réalisations déjà acquises sont conservées. Le nom du comportement est Order Splitting.',n['BHV044']['fields']['market_comparisons']),
        ('TER082','Spread','Répartition de ressources entre plusieurs commandes, dans le sens de la logique ARun discutée.','U362 : « on répartit entre les commandes ». SAP Spread logic peut utiliser une répartition proportionnelle ; cette formule n’est pas imposée à tout mécanisme FLOW. Ce terme qualifié ne désigne ni split ni étalement générique des échéances.',spread)]:
        assert not any(t['id']==ident for t in g['terms'])
        g['terms'].append(dict(id=ident,name=name,short_description=definition,definition=definition,context='Convention U362 intégrée U363 ; formulations développées éditoriales.',notes=notes,source_refs=['U362','U363','CMP133'],source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u362'),review=dict(state='partial',note='Distinction validée ; définition développée et notes proposées.'),market_comparisons=comparison))
    g['source_refs']=list(dict.fromkeys(g['source_refs']+['U362','U363']));gp.write_text(dumps(g),encoding='utf-8')

    migration=dict(source_refs=['U363'],model_before=str((OUT/'model-before.yaml').relative_to(ROOT)).replace('\\','/'),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},behaviors=[],
        reclassified_types=TYPES,type_parent='D04.p',domain_children=['D04.p','D04.o','D04.n','D04.q'],lifecycle_children=['BHV036','BHV037']+[f'BHV{i:03}' for i in range(38,45)],scope='U363 : quatre capacités D04 ; types reclassés, mutations intégrées, composition et archivage séparés, Spread hors mutation. Compléments éditoriaux proposés.')
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in m[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},removed=sorted(old.keys()-new.keys()))
    (OUT/'implementation.yaml').write_text(dumps(migration),encoding='utf-8')
    review['source_refs']+=refs;review['implementation_U363']=migration
    review['status']='applied_to_backlog_U363'
    review['current_structure_U363']=dict(domain_id='D04',capability_ids=migration['domain_children'],type_behaviors=TYPES,lifecycle_behaviors=migration['lifecycle_children'],scope='Cette section remplace les propositions de structure antérieures ; les blocs datés conservent leurs statuts historiques.')
    review['coverage_review_U351']['status']='integrated_U363'
    for p in review['coverage_review_U351']['proposals']:p['status']='integrated_U363'
    review['crud_and_archiving_U352']['archiving_proposal']['status']='integrated_as_capability_D04.q_U363'
    review['architecture_direction_U357']['status']='applied_U363_with_Type_instead_of_Handling'
    (ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml').write_text(dumps(review),encoding='utf-8')
    for filename in ['d04-refactoring','assignment-terminology']:
        path=ROOT/f'modeles/backlog/{filename}.yaml';doc=read(path)
        doc['current_U363']=dict(source_refs=['U363'],registry='modeles/backlog/order-lifecycle-behaviors.yaml',scope='Order Type regroupe cinq comportements. Lifecycle gouverne mutations et Split ; Structuring composition persistante ; Archiving conservation historique. Spread répartit ressources entre commandes via décisions et Supply Assignment. Les sections antérieures conservent leur contexte daté.')
        path.write_text(dumps(doc),encoding='utf-8')

    audit_path=ROOT/'modeles/backlog/behavior-gap-audit.yaml';a=read(audit_path)
    a['source_refs']+=refs;a['implementation_U363']=migration;a['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    previous_assessments={x['capability_id']:x for x in a['assessments']}
    a['assessments']=[x for x in a['assessments'] if x['capability_id'] not in TYPES]
    for ident in TYPES:
        a['existing_behavior_review'].append(dict(behavior_id=ident,status='reclassified_U363',recommendation=previous_assessments[ident]['recommendation']+' U363 : variante terminale, pas de sous-comportement ; arbitrages conservés au niveau approprié.',market_sources=previous_assessments[ident]['market_sources']))
    a['assessments'].append(dict(capability_id='D04.p',name='Order Type',existing_behaviors=TYPES,verdict='regroupement intégré U363',diagnosis=n['D04.p']['fields']['decomposition_rationale'],recommendation='Conserver les responsabilités par finalité sans recopier les mutations ; arbitrages retours et reconfirmation restent ouverts.',market_sources=['S15','S18','S23','S26','S27'],candidate_ids=[]))
    a['assessments'].append(dict(capability_id='D04.q',name='Order Archiving',existing_behaviors=[],verdict='capacité séparée U363',diagnosis=n['D04.q']['fields']['finality'],recommendation='Préciser éligibilité et conservation selon contexte ; pas de décomposition systématique.',market_sources=[],candidate_ids=[]))
    for row in a['assessments']:
        if row['capability_id']=='D04.o':row.update(existing_behaviors=migration['lifecycle_children'],verdict='neuf mécanismes intégrés U363',diagnosis=parent['fields']['decomposition_rationale'],recommendation='Éprouver les règles par type ; P11 conserve sa question de lancement collectif, sans adoption implicite.')
        if row['capability_id']=='D04.n':row.update(verdict='composition persistante U363',diagnosis=struct['fields']['definition'],recommendation='Préciser invariants des ensembles ; simple split sous Lifecycle, Spread hors mutations.')
    for ident in range(38,45):a['existing_behavior_review'].append(dict(behavior_id=f'BHV{ident:03}',status='integrated_U363',recommendation='U363 intègre le mécanisme ; effets détaillés et conditions restent éditoriaux. Ne pas confondre mutation et exécution.',market_sources=[]))
    # Existing contracts may target a precise behavior; no forced rerouting to its broader parent.
    for arb in a['arbitrations']:
        old=[i for i in arb['capabilities'] if i in TYPES]
        if old:
            arb['affected_behavior_ids_U363']=old
            arb['capabilities']=list(dict.fromkeys('D04.p' if i in TYPES else i for i in arb['capabilities']))
    for p in a['candidates']:
        p['needs']=['D04.p' if i in TYPES else i for i in p['needs']]
    audit_path.write_text(dumps(a),encoding='utf-8')
    p=ROOT/'AGENTS.md';text=p.read_text(encoding='utf-8')
    old='| D04 Order Management | Un type d’Order par capacité de gestion : vente, achat, transfert, retour client, retour fournisseur. Structuring et Lifecycle sont transverses, pas copiés sous chaque type. Conserver les exemples split, spread, affermissement, lancement, attente/reprise, report, annulation, clôture. |'
    assert old in text
    text=text.replace(old,'| D04 Order Management | U363 : quatre capacités sœurs — Order Type (cinq variantes métier comme comportements), Order Lifecycle Management (mutations internes, dont brouillon et Split), Order Structuring (composition persistante) et Order Archiving. Les identifiants D04.i–m restent ceux des comportements. Spread répartit les ressources entre commandes ; décisions et Supply Assignment en portent les effets. |')
    p.write_text(text,encoding='utf-8')
    append('marche/comparaisons.md','''## CMP133

- Codex ; 18 septembre 2026 ; U363 ; synthèse des comparaisons CMP125–CMP132 appliquée au backlog. La taxonomie FLOW à quatre capacités n’est pas présentée comme un catalogue éditeur commun.
- Order Type porte les variantes métier ; les identifiants des cinq anciennes capacités sont reclassés en comportements. Lifecycle porte mutations et split, Structuring composition persistante, Archiving conservation historique. Microsoft et SAP documentent les types ; Microsoft/Oracle les transitions, copies et splits. Archivage Microsoft relu : commandes facturées et exclusion des chaînes intersociétés sont des restrictions produit, pas des règles FLOW.
- Spread ARun : décision des parts et affectation distinctes des mutations. Exemple proportionnel simplifié ; aucun nouvel algorithme ni parent de décision introduit. Split/Spread ajoutés au glossaire métier avec limites de preuve.
- Accord U363 appliqué aux principes et rattachements ; descriptions développées, nouveaux libellés Drafting/Splitting et contrats proposés. Marché exposé dans les fiches, pas preuve de réalisation Beaumanoir.''')
    append('JOURNAL.md','''## 2026-09-18 — U363 : refonte D04 appliquée

Quatre capacités, cinq variantes d’Order Type, neuf comportements Lifecycle. Structuring et Archiving séparés. Spread retiré du sens mutation et explicité sous Supply Assignment ; glossaire enrichi. Identifiants, liens métier et valeurs adoptées préservés, nouvelles descriptions et contrats qualifiés. Captures et migration dans audits/2026-09-18-d04-U363 ; aucune publication.''')
    (OUT/'README.md').write_text('# Refonte D04 — U363\n\nArbre courant :\n\n```text\nOrder Management\n├── Order Type\n│   ├── Sales Order Management\n│   ├── Purchase Order Management\n│   ├── Transfer Order Management\n│   ├── Customer Return Management\n│   └── Supplier Return Management\n├── Order Lifecycle Management\n│   ├── Order Drafting\n│   ├── Order Firming\n│   ├── Order Freezing\n│   ├── Order Release\n│   ├── Order Hold & Resume\n│   ├── Order Rescheduling\n│   ├── Order Cancellation\n│   ├── Order Closure\n│   └── Order Splitting\n├── Order Structuring\n└── Order Archiving\n```\n\nLes identifiants D04.i–m sont préservés comme comportements. Type désigne une variante métier ; Lifecycle ses mutations ; Structuring une composition durable ; Archiving la conservation historique. Spread concerne la répartition des ressources, hors D04.\n\n[Portées et descriptions structurées](../../modeles/backlog/order-lifecycle-behaviors.yaml). [Preuve de migration](implementation.yaml). Les snapshots before conservent les validations et l’historique ; aucune release modifiée.\n',encoding='utf-8')
    print('U363 applied: D04 has four capabilities; five type variants and nine lifecycle behaviors.')


if __name__=='__main__':
    main()
