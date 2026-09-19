"""Apply the precise domain partition chosen in U438; keep editorial scope explicit."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash
from scripts.element_versions import content_hash

OUT = ROOT / 'modeles/backlog/history/order-domains-U438'
assert not OUT.exists()
OUT.mkdir()
paths = ['modeles/backlog/model.yaml', 'modeles/backlog/glossary.yaml', 'modeles/backlog/modeling-glossary.yaml',
         'modeles/backlog/order-backlog-review.yaml', 'modeles/backlog/order-lifecycle-behaviors.yaml',
         'modeles/backlog/d03-domain-review-U437.yaml']
for path in paths:
    (OUT / Path(path).name).write_bytes((ROOT / path).read_bytes())
def save(path, value):
    (ROOT / path).write_text(dumps(value), encoding='utf-8')
stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
before = read(ROOT / paths[0]); model = deepcopy(before)
nodes = {n['id']: n for n in model['nodes']}
assert 'D15' not in nodes
def refs(item):
    item['source_refs'] = list(dict.fromkeys(item.get('source_refs', []) + ['U438']))
def approve(item, fields, node=False):
    values = item['fields'] if node else item
    life = item.setdefault('lifecycle', {})
    approved = list(dict.fromkeys(life.get('validated_fields', []) + fields))
    life.update(state='urbanist_validated', recorded_at=stamp, recorded_by='Codex',
        source_refs=list(dict.fromkeys(life.get('source_refs', []) + ['U438'])),
        validated_fields=approved, value_sha256={f:value_hash(values[f]) for f in approved},
        note='U438 adopte noms et rattachements explicitement présentés ; autres champs non validés par extension. Accord antérieur conservé dans history/order-domains-U438/.')
def replace_paragraph(identifier, prefix, text):
    parts = nodes[identifier]['fields']['scope'].split('\n\n')
    assert any(p.startswith(prefix) for p in parts), (identifier, prefix)
    nodes[identifier]['fields']['scope'] = '\n\n'.join(text if p.startswith(prefix) else p for p in parts)

domain = nodes['D03']
domain['fields']['name'] = 'Fulfillment Optimization'
domain['fields']['definition'] = ('Arbitrer la satisfaction des Orders sous contraintes et objectifs concurrents, '
    'déterminer un plan cohérent et matérialiser les affectations de ressources retenues.')
domain['fields']['scope'] = '''Order Prioritization établit les priorités ; Fulfillment Plan Decision détermine un plan cohérent de satisfaction ; Order Backlog Planning organise le travail des hypothèses et scénarios ; Supply Assignment matérialise les affectations retenues. La valeur reste multidimensionnelle, sans pondération universelle.

[Order Promising](model:D15) établit les possibilités ATP/CTP, porte les arbitrages économiques et d’échéancier, puis tient les propositions et engagements de promesse. D03 mobilise ces résultats ; les échanges peuvent conduire à réexaminer possibilités, plan et promesses. Les autorités respectives de PTP, de Delivery Schedule Decision et de Fulfillment Plan Decision restent à préciser sans second plan final implicite.

[Order Management](model:D04) conserve la demande selon son intention, sa structure et sa conservation. Order Lifecycle Management autorise la prise en charge ; [Process Management](model:D06) coordonne les services et leurs adaptations. D03 peut demander les mutations utiles mais ne reprend pas leur application ni la réalisation physique.

Exemple fictif : deux commandes sollicitent 120 pièces pour 80 admissibles. Le domaine arbitre un plan compatible avec les priorités, possibilités et engagements, puis matérialise ses affectations. Une priorité ne lève pas une réservation et le plan ne confirme pas automatiquement une promesse. Selon U436, seule Reservation bloque les usages concurrents.

Le carnet reste une vue de travail, comprenant aussi le reste à satisfaire de commandes déjà engagées. La séparation D03/D15 repose sur les responsabilités de choix et de promesse, pas sur individuel/collectif : une optimisation peut concerner une seule commande et ATP plusieurs demandes. Inventory Optimization D05 conserve les objectifs et ajustements de stock.

U438 remplace le nom Order Backlog Management adopté U413 et les rattachements concernés U417/U420. D03 conserve quatre capacités ; D15 reçoit ATP, CTP, PTP, Delivery Schedule Decision et Promise Management ; Structuring et Archiving rejoignent D04. Les identifiants de capacités et leurs comportements restent stables. Les descriptions développées restent éditoriales.'''
approve(domain, ['name'], node=True)
domain['review'] = dict(state='partial', note='U438 adopte Fulfillment Optimization et sa composition. Finalité antérieure conservée ; définition, périmètre et comparaisons restent éditoriaux. U439–U442 instruisent séparément Structuring et Promise Management.')
for c in domain['fields']['market_comparisons']:
    c['flow_position'] = ('U438 : D03 Fulfillment Optimization porte priorités, plan de satisfaction, Planning et affectations ; '
        'D15 Order Promising porte possibilités et engagements. D04 conserve structure, cycle et archivage. '
        'La source éclaire des responsabilités traversant cette partition FLOW ; elle ne prescrit pas les domaines.')
    refs(c)
newdomain = dict(id='D15', revision=1, kind='domain', layer='transactional', fields=dict(
    name='Order Promising',
    definition='Établir ce qui peut être promis pour satisfaire les Orders, sous quelles conditions, puis maintenir les propositions et engagements de quantités et de dates.',
    finality='Rendre les engagements de satisfaction explicites et compatibles avec les possibilités et arbitrages applicables.',
    scope='''ATP établit les possibilités dans la situation de référence ; CTP examine la faisabilité sous adaptation ; PTP porte l’arbitrage économique ; Delivery Schedule Decision retient l’échéancier ; Promise Management tient propositions, confirmations et révisions autorisées.

[Fulfillment Optimization](model:D03) porte les priorités, le plan de satisfaction, le travail des scénarios et l’application des affectations. Les choix de promesse et de plan doivent rester compatibles ; le partage précis d’autorité entre PTP, échéancier et plan demeure à instruire. Cette séparation ne définit ni une séquence logicielle ni une frontière individuel/collectif.

Exemple fictif : 100 pièces demandées vendredi, 60 proposées vendredi et 40 lundi. Possibilités, proposition et engagement confirmé restent distincts ; un recalcul ne modifie pas silencieusement la promesse. Les dates de demande, de proposition, d’engagement et de réalisation ne sont pas interchangeables.

D01 apporte connaissance des ressources, protections et réservations ; D06 apporte conditions et possibilités des services ainsi que les faits d’exécution. D04 conserve intention, contenu, structure et cycle des Orders. D15 ne réalise pas les prestations et ne réserve pas implicitement des ressources : U436 demeure applicable.

Le nom et la composition sont adoptés U438 ; les descriptions développées et comparaisons sont proposées. L’utilité et la clarté de Promise Management font l’objet de U441, sans suppression adoptée.''',
    market_comparisons=deepcopy([c for c in domain['fields']['market_comparisons'] if c['source_title'] in ['Exploring Backorder Processing','Order promising']])),
    source_refs=['U438','U437','U436'], source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u438'),
    review=dict(state='partial',note='Nom et cinq rattachements adoptés U438 ; descriptions et comparaisons proposées, sans validation globale.'),
    editorial_basis='Description développée à partir du découpage présenté en U438 ; responsabilités antérieures des capacités préservées.', adoption_ids=[], last_modified=stamp)
approve(newdomain, ['name'], node=True)
model['nodes'].insert(model['nodes'].index(domain)+1,newdomain)
nodes['D15']=newdomain

replace_paragraph('D04','U420 rattache', 'U438 : Order Structuring et Order Archiving rejoignent D04, où Order Lifecycle Management conserve les transitions et l’autorisation de prise en charge. D03 optimise la satisfaction et D15 porte les possibilités et engagements de promesse. Ce choix remplace les placements de Structuring et Archiving issus de U417/U420. Les identifiants historiques ne déterminent pas les parents.')
nodes['D04']['fields']['definition']='Capter et maintenir les demandes Supply selon leur intention, leurs parties, leurs conditions et leur résultat attendu, gouverner leur cycle de vie, leur structure et leur conservation, en articulation avec leur optimisation, leur promesse et les processus.'
replace_paragraph('D04.n','La capacité appartient à', 'U438 : la capacité appartient à D04 Order Management. Elle maintient les découpages et compositions autorisés ; D03 et D15 conservent les choix de satisfaction et de promesse, tandis que Lifecycle autorise les transitions. Ce placement remplace U417. U439/U440/U442 demandent une formulation plus lisible et l’examen du regroupement et de la fusion comme comportements distincts ; leurs descriptions restent proposées.')
replace_paragraph('D04.q','U420 :', 'U438 : Order Archiving rejoint D04 Order Management, où se trouvent aussi Lifecycle et Structuring. Ce choix remplace son rattachement à D03 adopté U420. Clôturer reste une responsabilité de Lifecycle ; archiver conserve l’historique sans modifier rétroactivement les engagements et réalisations.')
replace_paragraph('BHV044','U417 :', 'U438 : Order Splitting reste sous Order Structuring D04.n, désormais dans D04. Ce rattachement de domaine remplace U417 ; identité, parent de comportement et définition sont conservés.')

common_old='D04 porte les demandes, leur résultat attendu et Lifecycle ; D03 travaille le carnet, ses décisions, Structuring et Archiving ; D05 optimise le stock, D01 conserve ses faits/régimes et D06 orchestre les services.'
common_new='D04 porte les demandes, leur résultat attendu, Lifecycle, Structuring et Archiving ; D03 optimise leur satisfaction et D15 porte possibilités et engagements de promesse ; D05 optimise le stock, D01 conserve ses faits/régimes et D06 orchestre les services.'
replacements={
    '[Order Backlog Management](model:D03)':'[Fulfillment Optimization](model:D03)',
    'disponibilité virtuelle pour la promesse dans Order Backlog Management':'disponibilité virtuelle pour la promesse dans Order Promising',
    'Priorités, couverture et promesses restent dans Order Backlog Management':'Les priorités et le plan de satisfaction relèvent de Fulfillment Optimization ; les possibilités et engagements de promesse relèvent d’Order Promising',
    common_old:common_new,
    '[Order Structuring](model:D04.n), dans D03':'[Order Structuring](model:D04.n), dans D04',
    'Order Structuring dans D03':'Order Structuring dans D04',
    'Structuring et Archiving en D03':'Structuring et Archiving en D04',
    'Order Structuring et Order Archiving restent dans D03':'Depuis U438, Order Structuring et Order Archiving appartiennent à D04',
    'Lifecycle relève de D04 ; Structuring relève de D03':'Lifecycle et Structuring relèvent de D04',
    'porté par Order Archiving en D03':'porté par Order Archiving en D04',
    'D03 décide source/promesse':'D03 décide le plan de satisfaction ; D15 porte les possibilités et engagements de promesse',
    'le réexamen de la promesse dans D03':'le réexamen de la promesse dans D15',
    'puis mobiliser D03 si la promesse':'puis mobiliser D15 si la promesse',
    'D03 conserve la décision de promesse Supply':'D15 conserve les décisions et engagements de promesse Supply',
    'Donner à D03 et aux décisions d’exécution':'Donner à D03, à D15 et aux décisions d’exécution',
    'D03 l’utilise pour sa promesse Supply':'D15 l’utilise pour la promesse Supply',
    'ni sa promesse D03':'ni sa promesse D15',
    'et D03 la promesse Supply':'et D15 la promesse Supply',
    'D03 conserve le réexamen de la promesse':'D15 conserve le réexamen de la promesse',
    'besoin Supply et les contraintes portés par D03':'besoin Supply et les contraintes issus des choix de satisfaction D03 et des possibilités et engagements de promesse D15',
    'fournir à D03 les faits et variantes':'fournir à D15 les faits et variantes',
    'Remonter effet promesse à D03':'Remonter effet promesse à D15'
}
for n in model['nodes']:
    for field in ['definition','scope','finality','decomposition_rationale']:
        if field not in n['fields'] or field in n.get('lifecycle',{}).get('validated_fields',[]): continue
        for old,new in replacements.items(): n['fields'][field]=n['fields'][field].replace(old,new)
    if n['id'] in ['D04.n','D04.q','BHV044']:
        for c in n['fields'].get('market_comparisons',[]):
            c['flow_position']='U438 : Structuring et Archiving appartiennent à D04, ainsi que Lifecycle ; Split reste sous Structuring et Release sous Lifecycle. Les résultats propres à ces capacités restent distincts des choix D03 et promesses D15. La source produit ne prescrit pas ce découpage FLOW.'
            refs(c)
    if n['id'] in ['D03.i','D03.j','D03.k','D03.l','D03.n','D04.n','D04.q','D03.p','D03.o','D03.m','D02.e']:
        n['review']['note'] += ' U438 : nom de capacité conservé ; parent de domaine explicite dans les relations contains, adopté séparément des descriptions.'

members={'D03.i':'D15','D03.j':'D15','D03.k':'D15','D03.l':'D15','D03.n':'D15','D04.n':'D04','D04.q':'D04',
         'D03.m':'D03','D03.o':'D03','D03.p':'D03','D02.e':'D03'}
changed_parent_ids=[]
for r in model['relations']:
    if r['type']=='contains' and r['target_id'] in members:
        if r['source_id']!=members[r['target_id']]:changed_parent_ids.append(r['id'])
        r['source_id']=members[r['target_id']]
        refs(r);approve(r,['type','source_id','target_id'])
        r['review']=dict(state='accepted',note='U438 adopte ce rattachement dans le découpage présenté ; identités et définitions des capacités et comportements préservées. Ancien rattachement capturé avant application.')
    if r['id'] in ['REL-SERVICE-CATALOG-PROMISING','REL-EXECUTION-PROMISING']:
        r['target_id']='D15';refs(r)
        r['qualification']['meaning']=r['qualification']['meaning'].replace('D03','D15')
        r['review']['note'] += ' U438 : cible de promesse portée par D15 ; relation toujours proposée.'
    if r['id']=='REL-EXECUTION-ADAPTATION-PROMISE-REVISION':
        r['qualification']['meaning']=r['qualification']['meaning'].replace('D03','D15');refs(r)
present=deepcopy(next(r for r in model['relations'] if r['id']=='REL-UNIVERSE-SUPPLY-D03'))
present.update(id='REL-UNIVERSE-SUPPLY-D15',target_id='D15',revision=1,source_refs=['U438'],last_modified=stamp)
present['review']=dict(state='proposed',note='Présentation du domaine Order Promising dans Supply ; le domaine reste une partition métier de même couche.')
present['lifecycle']=dict(state='ai_proposed',recorded_at=stamp,recorded_by='Codex',source_refs=['U438'],validated_fields=[],value_sha256={},note='Relation de présentation proposée ; distincte des rattachements métier adoptés.')
model['relations'].append(present)
for p in model['principles']:
    if p['id']=='PRINCIPLE-TO-PROMISE':p['statement']=p['statement'].replace('D03 distingue','D15 distingue');refs(p)
    if p['id']=='PRINCIPLE-EXECUTION-ORCHESTRATION':p['statement']=p['statement'].replace('D03 utilise','D15 utilise');refs(p)
    if p['id']=='PRINCIPLE-EXECUTION-DECISION-AND-COORDINATION':p['statement']=p['statement'].replace('D03 conserve','D15 conserve');refs(p)
model['limitations'][4]=model['limitations'][4].replace('Order Structuring et Order Archiving appartiennent à D03 ; Order Lifecycle Management appartient à D04 selon U417/U420.', 'Depuis U438, Structuring, Archiving et Lifecycle appartiennent à D04 ; D03 porte Fulfillment Optimization et D15 Order Promising. U439–U442 instruisent de nouvelles propositions sans rouvrir le périmètre historique U431.')
model['source_version'] += ' + U438 séparation Order Promising et Fulfillment Optimization'
for entry in model['source_files']:entry['sha256']=sha256((ROOT/entry['path']).read_bytes()).hexdigest()

changed=[];preserved=0;replaced=[]
for collection in ['nodes','relations','principles']:
    old={x['id']:x for x in before[collection]}
    for item in model[collection]:
        original=old.get(item['id'])
        if original:
            a=original['fields'] if collection=='nodes' else original
            b=item['fields'] if collection=='nodes' else item
            for f in original.get('lifecycle',{}).get('validated_fields',[]):
                if a[f]!=b[f]:
                    assert (item['id']=='D03' and f=='name') or (item['id'] in changed_parent_ids and f=='source_id'),(item['id'],f)
                    replaced.append(dict(id=item['id'],field=f,before=a[f],after=b[f],source_ref='U438'))
                else:
                    assert original['lifecycle']['value_sha256'][f]==item['lifecycle']['value_sha256'][f]
                    preserved+=1
        if original!=item:
            refs(item)
            if collection!='principles':
                item['revision']=original.get('revision',1)+1 if original else 1
                item['last_modified']=stamp
                if 'content_sha256' in item:item['content_sha256']=content_hash(item)
            changed.append(dict(collection=collection,id=item['id']))
save(paths[0],model)
assert sum(n['kind']=='capability' for n in model['nodes'])==47
assert sum(n['kind']=='behavior' for n in model['nodes'])==74
assert sum(n['kind']=='domain' for n in model['nodes'])==6

g=read(ROOT/paths[1]); term=next(t for t in g['terms'] if t['id']=='TER085')
term['notes']=term['notes'].replace('Order Backlog Management recherche comment satisfaire au mieux', 'Fulfillment Optimization recherche comment satisfaire au mieux ; Order Promising établit les possibilités et tient les engagements de promesse')
term['market_comparisons'][0]['differences']='Service logiciel regroupant plusieurs responsabilités ; proximité documentée, sans équivalence complète au domaine Fulfillment Optimization D03 ni preuve d’un solveur universel multiobjectif.'
refs(term);save(paths[1],g)
mg=read(ROOT/paths[2])
def correct_mod(value):
    if isinstance(value,dict):return {k:correct_mod(v) for k,v in value.items()}
    if isinstance(value,list):return [correct_mod(v) for v in value]
    if isinstance(value,str):return value.replace('dans D03','dans D04')
    return value
mod=next(t for t in mg['terms'] if t['id']=='MOD006')
mod['concrete_forms']=correct_mod(mod['concrete_forms']);refs(mod);save(paths[2],mg)

review=read(ROOT/paths[5]);review['status']='structure_adopted_U438_semantic_boundaries_open'
review['source_refs'].append('U438')
review['decision_required']='Découpage adopté U438 ; frontières fines PTP/échéancier/plan à préciser. Structuring et Promise Management réexaminés U439–U442.'
review['adoption_U438']=dict(recorded_at=stamp,source_refs=['U438'],adopted_domains={'D03':'Fulfillment Optimization','D15':'Order Promising'},capability_parents=members,
    approved_scope='Noms des deux domaines et rattachements des onze capacités présentés dans la question ; aucun nom de capacité, définition développée, contrat détaillé ou rapprochement marché adopté par extension.',
    replaced_approved_values=replaced,implementation_ref='modeles/backlog/history/order-domains-U438/implementation.yaml')
review['recommendation']['status']='structure_adopted_U438';review['recommendation']['domains'][0]['identifier']='D15';review['recommendation']['domains'][1]['identifier']='D03'
save(paths[5],review)
legacy=read(ROOT/paths[3]);legacy.update(status='superseded_domain_structure_U438',current_review_ref=paths[5],
    scope='Les sections U411–U424 ci-dessous conservent leur état historique. U438 remplace le nom D03 et les rattachements concernés par deux domaines D03/D15 et Structuring/Archiving en D04 ; voir current_review_ref.')
refs(legacy);save(paths[3],legacy)
life=read(ROOT/paths[4]);life['placement_U438']=dict(status='integrated',source_refs=['U438'],lifecycle_domain='D04',archiving_domain='D04',structuring_domain='D04',release_parent='D04.o',split_parent='D04.n',note='U438 remplace uniquement les rattachements concernés de U417/U420 ; sections antérieures conservées pour provenance.');save(paths[4],life)
implementation=dict(id='ORDER-DOMAINS-SPLIT-U438',source_refs=['U438'],recorded_at=stamp,
    model_before_sha256=sha256((OUT/'model.yaml').read_bytes()).hexdigest(),model_after_sha256=sha256((ROOT/paths[0]).read_bytes()).hexdigest(),
    adopted_domains={'D03':'Fulfillment Optimization','D15':'Order Promising'},capability_parents=members,
    replaced_approved_values=replaced,unchanged_previous_approved_values=preserved,changed=changed,
    previous_node_ids_preserved=True,behavior_parents_unchanged=True,capability_count=47,behavior_count=74,domain_count=6)
save('modeles/backlog/history/order-domains-U438/implementation.yaml',implementation)
print(f'U438 integrated: 6 domains, 47 capabilities, 74 behaviors; {preserved} prior approved values unchanged; {len(replaced)} explicitly replaced.')
