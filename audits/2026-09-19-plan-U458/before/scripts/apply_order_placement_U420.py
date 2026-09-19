"""Apply Laurent's explicit Archiving/Lifecycle domain correction."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/order-placement-U420'
MOVES = {'REL-MEMBER-D04.q': 'D03', 'REL-MEMBER-D04.o': 'D04'}
NOTE = 'U420 : Order Archiving appartient à D03 Order Backlog Management ; Order Lifecycle Management appartient à D04 Order Management. Structuring reste dans D03. Les comportements restent sous leurs capacités : Order Release suit Lifecycle dans D04 ; Split reste sous Structuring dans D03. Aucun identifiant ni définition de comportement modifié.'


def main():
    assert not OUT.exists()
    assert '## U420\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '## U420\n\n**id**\n\nU420\n\n**date**\n\n2026-09-19\n\n**titre**\n\nCorriger les domaines d’Archiving et Lifecycle\n\n**texte**\n\nOrder Archiving  doit être dans D03\n**Order Lifecycle Management** doit être dans D04\n\n**contexte et portée**\n\nCorrection explicite des deux rattachements de capacités après U417/U418. Archiving rejoint D03 ; Lifecycle revient dans D04. Les comportements restent sous leurs capacités : Order Release suit donc Lifecycle dans D04, conséquence explicitée en réponse, qui remplace son appartenance indirecte à D03 issue de U418. Aucun nouveau rattachement autonome de Release ni changement de définition déduit. Structuring et Split restent en D03. Les mises en cohérence rédactionnelles restent éditoriales.')
    OUT.mkdir()
    for rel, name in [('modeles/backlog/model.yaml','model-before.yaml'), ('modeles/backlog/behavior-gap-audit.yaml','audit-before.yaml'), ('modeles/backlog/order-backlog-review.yaml','review-before.yaml'), ('modeles/backlog/order-lifecycle-behaviors.yaml','lifecycle-before.yaml'), ('AGENTS.md','AGENTS-before.md')]:
        (OUT/name).write_bytes((ROOT/rel).read_bytes())
    mp=ROOT/'modeles/backlog/model.yaml'
    before=read(mp); model=deepcopy(before)
    nodes={n['id']:n for n in model['nodes']}
    oldnodes={n['id']:n for n in before['nodes']}
    def replace_paragraph(identifier, prefix, replacement):
        f=nodes[identifier]['fields']
        parts=f['scope'].split('\n\n')
        assert any(p.startswith(prefix) for p in parts), (identifier,prefix)
        f['scope']='\n\n'.join(replacement if p.startswith(prefix) else p for p in parts)
    replace_paragraph('D03','U417 :', NOTE+' Planning prépare les scénarios, Lifecycle applique les transitions et autorise la prise en charge, Process Orchestration coordonne les services. Le carnet mobilise Lifecycle en D04 ; son archivage conserve les Orders éligibles hors de l’usage opérationnel courant avec leurs liens consultables.')
    nodes['D04']['fields']['definition']='Capter et maintenir les demandes Supply selon leur intention métier, leurs parties, leurs conditions et leur résultat attendu, et gouverner leur cycle de vie, en articulation avec le travail collectif du carnet et les processus.'
    replace_paragraph('D04','U417 rattache', 'U420 rattache Order Lifecycle Management à D04 : progression, engagements et transitions, dont Order Release, restent transverses aux types d’Orders. Order Structuring et Order Archiving appartiennent à D03 Order Backlog Management ; D04 les mobilise pour le découpage, la composition et la conservation historique. Les préfixes D04.n et D04.q sont historiques et ne déterminent pas leur parent.')
    replace_paragraph('D04.o','U417 place', NOTE+' Les décisions de satisfaction, l’affectation de ressources, les promesses et les processus restent des responsabilités distinctes. Le carnet mobilise Lifecycle pour appliquer les évolutions autorisées aux Orders.')
    replace_paragraph('BHV039','U417 :', 'U420 : Order Release demeure sous Order Lifecycle Management, désormais dans D04. Ce déplacement remplace son appartenance indirecte à D03 issue de U417/U418. Identité et définition U410 conservées ; Planning prépare, Lifecycle autorise et Process Orchestration coordonne les services.')
    replace_paragraph('D03.p','U417 révise', 'U420 : Order Release demeure sous Lifecycle, désormais dans D04 ; Planning le mobilise pour autoriser la prise en charge du scénario préparé. Planning ne porte actuellement aucun comportement direct ; aucune décomposition supplémentaire n’est créée par analogie avec Inventory Planning. Maintenir les scénarios du carnet reste distinct du choix d’adaptation des processus opérationnels.')
    nodes['D04.q']['fields']['scope']+='\n\n'+NOTE+' Le domaine du carnet porte ainsi la conservation des commandes sorties de son usage opérationnel courant. Clôturer reste une responsabilité de Lifecycle en D04 ; archiver ne change pas rétroactivement les engagements et réalisations.'
    replacements={
        '[Order Lifecycle Management](model:D04.o) dans D03':'[Order Lifecycle Management](model:D04.o) dans D04',
        '[Order Lifecycle Management](model:D04.o), dans D03':'[Order Lifecycle Management](model:D04.o), dans D04',
        '[Order Structuring](model:D04.n), également dans D03':'[Order Structuring](model:D04.n), dans D03',
        'D04 porte les demandes et leur résultat attendu ; D03 travaille le carnet, ses décisions, Lifecycle et Structuring ; D05 optimise le stock, D01 conserve ses faits/régimes et D06 orchestre les services. Archiving reste en D04 et ces capacités restent mobilisables et les opérations utiles doivent être expliquées dans chaque contexte métier.':'D04 porte les demandes, leur résultat attendu et Lifecycle ; D03 travaille le carnet, ses décisions, Structuring et Archiving ; D05 optimise le stock, D01 conserve ses faits/régimes et D06 orchestre les services. Ces capacités restent mobilisables et les opérations utiles doivent être expliquées dans chaque contexte métier.',
        'L’archivage reste distinct en D04.':'L’archivage reste distinct, porté par Order Archiving en D03.',
        'Ces capacités relèvent de D03.':'Lifecycle relève de D04 ; Structuring relève de D03.',
        'Les mutations, la structuration et l’archivage mobilisent les capacités transverses D04.':'Les mutations mobilisent Lifecycle en D04 ; la structuration et l’archivage mobilisent Structuring et Archiving en D03.',
    }
    positions={
        'D04.o':'U420 : Lifecycle relève de D04 ; Release en demeure un comportement. Les mécanismes éditeurs n’imposent pas ce découpage en domaines.',
        'D04.q':'U420 : Archiving relève de D03, distinct de Lifecycle en D04. Conservation et consultation des Orders historiques ; aucun choix de stockage ni règle légale imposé. Le rattachement au carnet est un choix FLOW, pas une taxonomie éditeur.',
        'BHV039':'U420 : autorisation de prise en charge sous Lifecycle en D04 ; identité et définition conservées. Planning en D03 prépare le scénario.',
    }
    for n in model['nodes']:
        for field in ['scope','finality']:
            if field in n['fields'] and field not in n.get('lifecycle',{}).get('validated_fields',[]):
                for old,new in replacements.items():
                    n['fields'][field]=n['fields'][field].replace(old,new)
        for comp in n['fields'].get('market_comparisons',[]):
            if n['id'] in positions:
                comp['flow_position']=positions[n['id']]
                comp['source_refs']=list(dict.fromkeys(comp.get('source_refs',[])+['U420']))
            elif comp.get('flow_position','').startswith('Structuring et Lifecycle appartiennent à D03'):
                comp['flow_position']='U420 : Structuring dans D03, Lifecycle dans D04 ; Split sous Structuring, Release sous Lifecycle. Frontière FLOW, pas taxonomie éditeur adoptée.'
        if n!=oldnodes[n['id']]:
            n['revision']+=1; n['source_refs']=list(dict.fromkeys(n['source_refs']+['U420']))
    stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    for r in model['relations']:
        if r['id'] in MOVES:
            r['source_id']=MOVES[r['id']];r['revision']+=1;r['source_refs']=list(dict.fromkeys(r['source_refs']+['U420']))
            r['review']=dict(state='accepted',note='Correction explicite U420 ; rattachement antérieur conservé dans la capture.')
            r['lifecycle']=dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U420'],validated_fields=['type','source_id','target_id'],value_sha256={f:value_hash(r[f]) for f in ['type','source_id','target_id']},note='Seul le parent de la capacité change ; les comportements suivent leur capacité.')
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=['U420'],model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),moves=MOVES,behaviors=[],delta={})
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in model[key]};assert old.keys()==new.keys()
        migration['delta'][key]=dict(added={},removed=[],changed={i:value_hash(new[i]) for i in sorted(new) if new[i]!=old[i]})
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['implementation_U420']=migration; audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest();audit['source_refs']=list(dict.fromkeys(audit['source_refs']+['U420']))
    for a in audit['assessments']:
        if a['capability_id'] in {'D04.n','D04.o','D04.q','D03.p'}:
            a['recommendation']=NOTE
    next(p for p in audit['candidates'] if p['id']=='P11')['review_note']='P11 intégré BHV039 U410. Release reste sous Lifecycle, déplacé en D04 U420 ; définition et parent de comportement conservés.'
    for b in audit['existing_behavior_review']:
        if b['behavior_id'] in {'BHV039','BHV044'}: b['recommendation']=NOTE
    audit['order_backlog_U413'].update(status='placements_resolved_U420',note=NOTE)
    save('modeles/backlog/behavior-gap-audit.yaml',audit)
    review=read(ROOT/'modeles/backlog/order-backlog-review.yaml')
    review['status']='placements_resolved_U420';review['model_state']=NOTE
    review['scope']='U420 remplace les rattachements de Lifecycle et Archiving ; les autres choix U417 restent acquis. Les anciennes sections conservent les étapes historiques.'
    review['next_arbitration']='Rattachements corrigés U420 ; poursuivre les autres points de l’audit existant.'
    review['placement_U420']=dict(status='integrated',source_refs=['U420'],moves=MOVES,note=NOTE,implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix(),market_comparison=dict(consulted_on='2026-09-19',sources=[dict(vendor='Microsoft',title='Archive Dynamics 365 Supply Chain Management Sales orders data',url='https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/archive-so',version='2026-01-14',locator='Prerequisites ; View historical data'),dict(vendor='Microsoft',title='View, manage, and approve planned orders',url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/approved-planned-order',version='2026-09-02',locator='View and edit the status of planned orders')],finding='Microsoft distingue conservation consultable des commandes archivées et pilotage des états des ordres planifiés. Ces pages décrivent des mécanismes produits, pas une cartographie de capacités.',flow_interpretation='D03 conserve le carnet historique ; D04 gouverne les états et engagements des Orders. Le rattachement aux domaines est un choix FLOW explicite ; aucune correspondance taxonomique exacte revendiquée. Les restrictions produit ne deviennent pas des règles FLOW.'))
    review['source_refs']=list(dict.fromkeys(review['source_refs']+['U420']))
    for item in review['targeted_review']:item['current_resolution']='Voir placement_U420 et structure_lifecycle_U417 ; recommandations précédentes conservées pour provenance.'
    save('modeles/backlog/order-backlog-review.yaml',review)
    ann=read(ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml')
    ann['placement_U420']=dict(status='integrated',source_refs=['U420'],lifecycle_domain='D04',archiving_domain='D03',structuring_domain='D03',release_parent='D04.o',split_parent='D04.n',note=NOTE)
    save('modeles/backlog/order-lifecycle-behaviors.yaml',ann)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8')
    text=text.replace('**Order Release (U410/U417)**','**Order Release (U410/U420)**').replace('sous Order Lifecycle Management D04.o, désormais dans D03 (U417, remplace U414)','sous Order Lifecycle Management D04.o dans D04 (U420 remplace le domaine U417/U418 ; le parent du comportement reste Lifecycle)')
    text=text.replace('Order Structuring D04.n et Order Lifecycle Management D04.o sont rattachés à D03.','Order Structuring D04.n reste dans D03. U420 place Order Archiving D04.q dans D03 et Order Lifecycle Management D04.o dans D04.').replace('U417 déplace Lifecycle et Structuring dans D03 : progression/engagements pour Lifecycle, découpage et composition avec Split pour Structuring. Archiving reste dans D04. Les identifiants D04.n/D04.o gardent leur préfixe historique.','U420 : Lifecycle est dans D04, avec ses huit comportements dont Release ; Structuring (avec Split) et Archiving sont dans D03. Les identifiants restent stables ; leurs préfixes ne déterminent pas le parent.')
    agents.write_text(text,encoding='utf-8')
    append('JOURNAL.md','## 2026-09-19 — U420 : domaines d’Archiving et Lifecycle\n\nOrder Archiving déplacé dans D03 ; Order Lifecycle Management dans D04. Comportements inchangés de parent, donc Release suit Lifecycle en D04. Structuring et Split restent en D03. Descriptions, comparaisons contextuelles, audit existant et instructions actualisés ; historique U417/U418 préservé. Aucun nouveau catalogue ni release.')
    (OUT/'README.md').write_text('# U420 — Correction des domaines\n\n'+NOTE+'\n',encoding='utf-8')
    print('U420 integrated: two domain changes; behavior definitions and parents preserved.')


if __name__=='__main__':main()
