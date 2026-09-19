"""Place structuring and lifecycle in the order backlog domain."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT=ROOT/'modeles/backlog/history/backlog-structure-U417'
REFS=['U416','U417','U418','ELM248','CMP159']
STRUCTURE='Organiser et faire évoluer le découpage et la composition des Orders et de leurs éléments, en préservant leurs liens, leurs quantités et leurs engagements.'
MOVES={'REL-MEMBER-D04.n':'D03','REL-MEMBER-D04.o':'D03','REL-BEHAVIOR-BHV044':'D04.n','REL-BEHAVIOR-BHV039':'D04.o'}


def main():
    assert not OUT.exists()
    mp=ROOT/'modeles/backlog/model.yaml';before=read(mp);m=deepcopy(before);nodes={n['id']:n for n in m['nodes']}
    contributions=[('U416','Structuring inclut Split ; Lifecycle pilote le carnet', '''Split et Structuring, ce sont deux notions séparées ? Pour moi, Structuring est le terme large et Split est un comportement.

"Firming, Freezing, Hold, Rescheduling et Cancellation  " touchent l'état de l'order mais c'est de la gestion de backlog : c'est comme si les orders changeaient de colonne comme pour suivre un processus à étape.''', 'Clarification de responsabilité métier : découpage sous Structuring ; pilotage des engagements et de la progression sous le carnet. La métaphore des colonnes ne prescrit pas une séquence unique ni un modèle de données.'),
    ('U417','Déplacer Structuring et Lifecycle vers le carnet','Go','Adoption de la proposition : déplacer D04.n et D04.o dans D03 en conservant leurs identifiants ; rattacher BHV044 Order Splitting à Structuring et BHV039 Order Release à Lifecycle, révisant explicitement U414. Définition élargie de Structuring adoptée. Planning prépare les scénarios, Lifecycle autorise la prise en charge, Process Orchestration coordonne les services. Gel contre modification et suspension de progression restent combinables, distincts de l’affermissement. D04 conserve les intentions/types et l’archivage. Aucun nouveau domaine ou comportement ; descriptions développées et comparaisons éditoriales. La nouvelle rédaction de Planning traduit le mandat précisé, sans étendre la validation aux mots non présentés.')]
    contributions.append(('U418','Confirmer Order Release dans le domaine du carnet', 'Order Release, je trouverai ça logique que ce soit dans Backlog Management', 'Précision reçue pendant l’intégration U417 : Order Release appartient au domaine D03 Order Backlog Management. Le rattachement via Order Lifecycle Management, lui-même déplacé dans D03 selon U417, est explicité en réponse. Aucun nouveau domaine ou capacité homonyme, ni rattachement direct d’un comportement au domaine, n’est déduit.'))
    for ident,title,verbatim,scope in contributions:
        assert f'## {ident}\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        append('connaissance/01-contributions-utilisateur.md',f'## {ident}\n\n**id**\n\n{ident}\n\n**date**\n\n2026-09-19\n\n**titre**\n\n{title}\n\n**texte**\n\n{verbatim}\n\n**contexte et portée**\n\n{scope}')
    OUT.mkdir()
    for rel,name in [('modeles/backlog/model.yaml','model-before.yaml'),('modeles/backlog/behavior-gap-audit.yaml','audit-before.yaml'),('modeles/backlog/order-backlog-review.yaml','review-before.yaml'),('modeles/backlog/order-lifecycle-behaviors.yaml','lifecycle-before.yaml'),('AGENTS.md','AGENTS-before.md')]:
        (OUT/name).write_bytes((ROOT/rel).read_bytes())
    stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    structure=nodes['D04.n'];lifecycle=nodes['D04.o'];planning=nodes['D03.p'];release=nodes['BHV039'];split=nodes['BHV044']
    structure['fields']['definition']=STRUCTURE
    life=structure['lifecycle'];life['validated_fields']=list(dict.fromkeys(life['validated_fields']+['definition']));life['value_sha256']['definition']=value_hash(STRUCTURE);life['source_refs']=list(dict.fromkeys(life['source_refs']+['U417']));life['recorded_at']=stamp
    life['note']+=' U417 : définition élargie adoptée, ancien périmètre capturé avant modification.'
    structure['fields']['scope']='''Organiser les découpages et compositions des Orders et de leurs éléments pour travailler le carnet tout en gardant lisibles les demandes, leurs liens et leurs engagements. Le périmètre comprend la scission avec filiation ainsi que la composition persistante d’ensembles ; il n’est plus limité à cette dernière.

Order Splitting est le comportement qui scinde un Order ou ses éléments en parties traitables distinctement. Préserver la filiation et les quantités permet de suivre le besoin d’origine sans double comptage. Exemple fictif : 100 pièces sont traitées en deux parties de 60 et 40 ; cette représentation ne présume pas deux commandes commerciales autonomes.

Maintenir aussi les rattachements et invariants d’un ensemble durable lorsqu’il existe : quantités, engagement d’ensemble, remplacements autorisés et lecture de la satisfaction. Un Order chapeau peut être pertinent, mais n’est pas obligatoire. Regroupement et composition restent explicités dans le périmètre ; aucun nouveau comportement par opération n’est créé ici.

La capacité appartient à D03 Order Backlog Management (U417). Les capacités par intention de D04 conservent le sens de la demande et ses conditions. Planning travaille les scénarios ; les décisions spécialisées choisissent les possibilités, dates et affectations ; Structuring matérialise les découpages et compositions autorisés. Spread reste la répartition de ressources entre besoins, distincte de Split et portée par les décisions et Supply Assignment.

Une simple scission comme une composition persistante relèvent désormais de Structuring. L’ancienne distinction plaçant la première sous Lifecycle est remplacée U417. La structure documentaire des éditeurs ne prescrit ni cardinalité ni propriétaire logiciel FLOW.'''
    structure['fields']['decomposition_rationale']='La scission permet à des parties d’une demande de devenir traitables distinctement tout en préservant filiation, quantités et engagements. Cette complexité et ce bénéfice justifient Order Splitting comme comportement de Structuring. La composition persistante demeure dans la responsabilité large de la capacité, sans comportement créé pour chaque opération de regroupement.'
    lifecycle['fields']['scope']='''Gouverner la progression et les engagements des Orders dans le carnet. Les huit comportements combinables sont Order Drafting, Order Firming, Order Freezing, Order Release, Order Hold & Resume, Order Rescheduling, Order Cancellation et Order Closure. Ils ne constituent pas huit états obligatoires ni huit étapes d’une séquence unique.

Le brouillon permet la préparation de l’Order ; le contenu propre à chaque intention reste pris en charge par les capacités de vente, achat, transfert, retours et apport sous consignation. Affermir établit un engagement ; cela ne libère pas automatiquement la prise en charge et ne gèle pas toutes les données.

Freezing protège les éléments désignés contre les réoptimisations. Hold suspend une progression désignée. Ces dimensions sont distinctes et combinables : un Order peut être ferme, gelé sur certains éléments et temporairement suspendu. Une vue en colonnes peut montrer sa progression, sans transformer toutes les protections et échéances en un statut unique.

Order Release autorise la prise en charge individuelle ou collective selon les conditions applicables ; il ne crée pas automatiquement une réservation et ne constate pas le démarrage physique. Planning prépare les scénarios ; Lifecycle porte cette autorisation ; Process Orchestration coordonne les services nécessaires. Autoriser ensemble ne signifie pas démarrer simultanément.

Reporter une échéance ne lève pas une attente. Annuler retire le reste à satisfaire autorisé sans effacer les réalisations acquises ; clôturer explicite la fin du traitement et le devenir du reliquat. Ces mécanismes restent gouvernés selon les contraintes propres aux Orders, sans cycle universel imposé. L’archivage reste distinct en D04.

U417 place la capacité dans Order Backlog Management D03. Order Splitting relève désormais d’Order Structuring ; Order Release revient sous Lifecycle après le rattachement intermédiaire U414 à Planning. Identifiants et définitions des comportements conservés. Les décisions de satisfaction, l’affectation de ressources, les promesses et les processus restent des responsabilités distinctes.'''
    lifecycle['fields']['decomposition_rationale']='Préparation différée, engagement ferme, protection contre les réoptimisations, autorisation de prise en charge, suspension/reprise, changement d’échéance, retrait du besoin et fin du traitement ont des effets métier distincts et combinables. Leur séparation rend lisibles les possibilités de progression et les engagements ; ce n’est pas une décomposition par bouton ou statut technique. Split relève de Structuring.'
    # The approved boundary supersedes authorization in Planning; the exact revised prose was not presented.
    planning['fields']['definition']=planning['fields']['definition'].replace('puis préparer et autoriser la prise en charge','puis préparer la prise en charge')
    planning['lifecycle']['validated_fields'].remove('definition');planning['lifecycle']['value_sha256'].pop('definition')
    planning['lifecycle']['note']+=' U417 remplace la responsabilité d’autorisation par la préparation ; rédaction actualisée de définition proposée. Définition U414 et son empreinte conservées dans la capture historique.'
    planning['fields']['scope']='''Construire, comparer et maintenir les scénarios de satisfaction du carnet en mobilisant Fulfillment Plan Decision et les décisions spécialisées. Planning peut être humain, automatisé ou mixte ; il travaille les hypothèses et leurs impacts et prépare la mise en action du scénario retenu.

Exemple fictif : comparer une hypothèse privilégiant les ouvertures de magasins et une autre préservant davantage les dates promises. Les décisions produisent les scénarios cohérents ; Planning organise leur examen et prépare celui qui sera engagé.

Planning prépare le scénario ; Order Lifecycle Management porte Order Release, qui autorise la prise en charge ; Process Orchestration coordonne les services. Supply Assignment applique les affectations, Promise Management gère les engagements de promesse. Structuring organise les découpages et compositions autorisés, dont Split. Préparer 60 pièces maintenant et 40 plus tard n’impose pas deux commandes clients.

U417 révise explicitement le rattachement U414 : Order Release appartient à Lifecycle dans le même domaine D03. Planning ne porte actuellement aucun comportement direct ; aucune décomposition supplémentaire n’est créée par analogie avec Inventory Planning. Maintenir les scénarios du carnet reste distinct du choix d’adaptation des processus opérationnels.'''
    planning['fields'].pop('decomposition_rationale',None)
    release['fields']['scope']='\n\n'.join(p for p in release['fields']['scope'].split('\n\n') if not p.startswith(('U413 :','U414 :')))+'\n\nU417 : Order Release relève d’Order Lifecycle Management, désormais dans D03. Ce rattachement remplace U414 sous Planning. Identité et définition U410 conservées ; Planning prépare, Lifecycle autorise et Process Orchestration coordonne les services.'
    split['fields']['scope']='\n\n'.join(p for p in split['fields']['scope'].split('\n\n') if not p.startswith('U413 :'))
    split['fields']['scope']=split['fields']['scope'].replace('Si un engagement d’ensemble reste actif et sa composition doit être maintenue, mobiliser Structuring.', 'Structuring porte la scission ainsi que la composition d’ensemble lorsqu’elle doit être maintenue.')
    split['fields']['scope']+='\n\nU417 : Order Splitting est un comportement d’Order Structuring, rattachée à D03 Order Backlog Management. La scission et la composition relèvent de cette responsabilité large ; le comportement garde son identifiant et sa définition.'
    nodes['D03']['fields']['scope']='\n\n'.join(p for p in nodes['D03']['fields']['scope'].split('\n\n') if not p.startswith('U414 :'))+'\n\nU417 : Order Backlog Planning prépare les scénarios ; Order Structuring (D04.n, préfixe historique) organise découpage et composition avec Order Splitting ; Order Lifecycle Management (D04.o) gouverne progression et engagements, dont Order Release. Ces trois capacités appartiennent à D03. Les identifiants restent stables. D04 conserve les demandes selon leur intention et leur conservation historique ; D06 orchestre les services.'
    nodes['D04']['fields']['definition']='Capter et maintenir les demandes Supply selon leur intention métier, leurs parties, leurs conditions et leur résultat attendu, et assurer leur conservation historique, en articulation avec le travail collectif du carnet et les processus.'
    nodes['D04']['fields']['scope']='''Les capacités par intention prennent en charge les demandes de vente, achat, transfert, retour client, retour fournisseur et apport sous consignation. Elles gardent le sens du besoin, les parties, les quantités et conditions demandées, les évolutions autorisées et le suivi du reste à satisfaire selon chaque contexte métier.

U417 rattache Order Structuring et Order Lifecycle Management au domaine Order Backlog Management D03. D04 les mobilise pour les découpages, compositions, engagements et transitions applicables ; ces responsabilités ne sont pas recopiées sous chaque type d’Order. Order Archiving reste dans D04 pour la conservation historique. Les anciens préfixes D04.n et D04.o ne décrivent plus leur parent.

Le besoin d’origine doit rester lisible lorsque le carnet organise sa satisfaction en plusieurs parties ou phases. La prise en charge du sens de la demande ne présume ni un propriétaire logiciel exclusif ni une séquence universelle. D01 garde les faits et régimes de stock, D05 l’optimisation du stock et D06 les processus de services.'''
    replacements={
        'Les mutations internes, dont le split avec filiation, mobilisent [Order Lifecycle Management](model:D04.o). La composition métier persistante d’un ensemble d’Orders mobilise [Order Structuring](model:D04.n).':'La progression et les engagements mobilisent [Order Lifecycle Management](model:D04.o) dans D03. Le split avec filiation et la composition des ensembles mobilisent [Order Structuring](model:D04.n), également dans D03.',
        '[Order Lifecycle Management](model:D04.o) conserve brouillon, affermissement, gel, lancement, attente, report, annulation, clôture et split. [Order Structuring](model:D04.n) conserve la composition persistante':'[Order Lifecycle Management](model:D04.o), dans D03, conserve brouillon, affermissement, gel, lancement, attente, report, annulation et clôture. [Order Structuring](model:D04.n), dans D03, porte split et composition',
        'D04 porte les demandes et leur résultat attendu, D03/D05 les décisions, D01 les faits/régimes de stock, D06 les prestations. Lifecycle/Structuring/Archiving restent disponibles':'D04 porte les demandes et leur résultat attendu ; D03 travaille le carnet, ses décisions, Lifecycle et Structuring ; D05 optimise le stock, D01 conserve ses faits/régimes et D06 orchestre les services. Archiving reste en D04 et ces capacités restent mobilisables',
        '[Order Lifecycle Management](model:D04.o) applique les mutations autorisées, par exemple un report ou une scission de l’Order.':'[Order Lifecycle Management](model:D04.o) applique les transitions autorisées, par exemple un report ; [Order Structuring](model:D04.n) porte une scission éventuelle. Ces capacités relèvent de D03.',
    }
    oldnodes={n['id']:n for n in before['nodes']}
    for n in m['nodes']:
        for field in ['scope','finality']:
            if field in n['fields'] and field not in n.get('lifecycle',{}).get('validated_fields',[]):
                for old,new in replacements.items():n['fields'][field]=n['fields'][field].replace(old,new)
        if n['id'] in {'D04.n','D04.o','D03.p','BHV039','BHV044'}:
            for comp in n['fields'].get('market_comparisons',[]):
                comp['flow_position']={'D04.n':'U417 : Structuring couvre découpage et composition dans D03 ; Split en est un comportement.','D04.o':'U417 : Lifecycle gouverne les engagements et la progression du carnet dans D03 ; Order Release en est un comportement, Split relève de Structuring.','D03.p':'U417 : Planning prépare les scénarios en mobilisant les décisions ; Lifecycle autorise la prise en charge. La release produit Oracle ne se transpose pas automatiquement à FLOW.','BHV039':'U417 : autorisation de prise en charge sous Lifecycle dans D03 ; identité et définition conservées.','BHV044':'U417 : Split est un comportement de Structuring dans D03 ; les structures documentaires éditeurs ne sont pas imposées à FLOW.'}[n['id']]
        if n!=oldnodes[n['id']]:
            n['revision']+=1;n['source_refs']=list(dict.fromkeys(n['source_refs']+REFS))
    for relation in m['relations']:
        if relation['id'] in MOVES:
            relation['source_id']=MOVES[relation['id']];relation['revision']+=1;relation['source_refs']=list(dict.fromkeys(relation['source_refs']+['U417']))
            relation['review']=dict(state='accepted',note='Déplacement explicite U417 ; ancien rattachement et preuves capturés.')
            relation['lifecycle']=dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U417'],validated_fields=['type','source_id','target_id'],value_sha256={f:value_hash(relation[f]) for f in ['type','source_id','target_id']},note='U417 remplace le parent précédent sans changer les identifiants.')
    save('modeles/backlog/model.yaml',m)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),moves=MOVES,structuring_definition=STRUCTURE,behaviors=[],delta={})
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in m[key]};assert old.keys()==new.keys()
        migration['delta'][key]=dict(added={},removed=[],changed={i:value_hash(new[i]) for i in sorted(new) if new[i]!=old[i]})
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    comparisons=[dict(vendor='Oracle',product='Fusion Cloud SCM 26B',element_name='What’s a Split Order Line',element_type='Mécanisme produit',relationship='Recouvrement partiel',similarities='Découper une ligne pour satisfaire la demande entre entrepôts ou dates ; les parties peuvent progresser différemment.',differences='La structure documentaire Oracle et ses restrictions ne prescrivent pas une hiérarchie ou un découpage logiciel FLOW.',source_title='What’s a Split Order Line',source_url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html',source_version='26B',source_locator='How Order Management Determines Availability ; How Split Order Lines Affect Status'),dict(vendor='Microsoft',product='Dynamics 365 Supply Chain Management',element_name='View, manage, and approve planned orders',element_type='Mécanisme produit',relationship='Recouvrement partiel',similarities='Les statuts suivent la préparation des ordres planifiés ; l’approbation préserve certains ajustements face aux recalculs sous conditions.',differences='Périmètre approvisionnements planifiés. Pas de taxonomie universelle ni de preuve que gel, suspension et affermissement forment un seul cycle.',source_title='View, manage, and approve planned orders',source_url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/approved-planned-order',source_version='Page mise à jour le 2 septembre 2026',source_locator='View and edit the status of planned orders ; Approve planned orders')]
    for comp in comparisons:comp.update(flow_position='Structuring et Lifecycle appartiennent à D03 ; Split sous Structuring, Release sous Lifecycle. Frontière de responsabilité FLOW, pas taxonomie éditeur adoptée.',consulted_on='2026-09-19',evidence_limits='Sources primaires ouvertes lors de la proposition ; aucune preuve installée Beaumanoir.',status='proposed',source_refs=REFS)
    # Add comparisons to the concerned sheets, then capture their final hashes.
    structure['fields'].setdefault('market_comparisons',[]).append(comparisons[0]);lifecycle['fields'].setdefault('market_comparisons',[]).append(comparisons[1])
    save('modeles/backlog/model.yaml',m)
    for ident in ['D04.n','D04.o']:migration['delta']['nodes']['changed'][ident]=value_hash(nodes[ident])
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml');audit['implementation_U417']=migration;audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest();audit['source_refs']=list(dict.fromkeys(audit['source_refs']+REFS))
    for a in audit['assessments']:
        if a['capability_id'] in {'D04.n','D04.o','D03.p'}:
            a['existing_behaviors']=[r['target_id'] for r in m['relations'] if r['type']=='contains' and r['source_id']==a['capability_id']]
            a['candidate_ids']=['P11'] if a['capability_id']=='D04.o' else []
            a['verdict']='rattachements révisés U417';a['diagnosis']=nodes[a['capability_id']]['fields'].get('decomposition_rationale','Planning sans comportement direct après U417 ; mandat de préparation conservé.')
            a['recommendation']='Structuring inclut Split ; Lifecycle inclut Release ; les deux capacités sont dans D03. Planning prépare, Lifecycle autorise. Pas de nouveau niveau ni comportement.'
    p=next(p for p in audit['candidates'] if p['id']=='P11');p['parent_id']='D04.o';p['review_note']='P11 intégré BHV039 U410 ; U417 rattache Release à Lifecycle, désormais dans D03. Ancien placement U414 remplacé.'
    for b in audit['existing_behavior_review']:
        if b['behavior_id'] in ['BHV039','BHV044']:b.update(status='reparented_U417',recommendation='U417 : Release sous Lifecycle, Split sous Structuring ; identifiants et définitions conservés, capacités dans D03.')
    audit['order_backlog_U413'].update(status='placements_resolved_U417',note='Structuring et Lifecycle déplacés dans D03 ; Split sous Structuring, Release sous Lifecycle. Arbitrage de placement résolu ; règles détaillées non imposées.')
    save('modeles/backlog/behavior-gap-audit.yaml',audit)
    review=read(ROOT/'modeles/backlog/order-backlog-review.yaml');review['structure_lifecycle_U417']=dict(status='integrated',source_refs=REFS,moves=MOVES,adopted_structuring_definition=STRUCTURE,planning_definition_status='editorial_rewording_after_adopted_boundary_change',market_comparisons=comparisons,implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    review['status']='placements_resolved_U417';review['model_state']='138 nœuds, 47 capacités, 73 comportements. Structuring et Lifecycle sous D03 ; Split sous Structuring ; Release sous Lifecycle ; Planning sans comportement direct.'
    review['next_arbitration']='Bloc commande/carnet résolu sur les rattachements U417 ; poursuivre les autres points de l’audit existant.'
    review['scope']='U417 remplace les réserves de placement U413 et le rattachement Release U414. Identifiants conservés. Colonnes = représentation possible de progression ; gel et suspension restent des dimensions combinables.'
    for item in review['targeted_review']:
        item['status']='superseded_by_U417';item['current_resolution']='Voir structure_lifecycle_U417 ; recommandation précédente conservée pour provenance, non actuelle.'
    review['source_refs']=list(dict.fromkeys(review['source_refs']+REFS));save('modeles/backlog/order-backlog-review.yaml',review)
    ann=read(ROOT/'modeles/backlog/order-lifecycle-behaviors.yaml');ann['placement_U417']=dict(status='integrated',source_refs=REFS,lifecycle_domain='D03',structuring_domain='D03',release_parent='D04.o',split_parent='D04.n',note='Révise U414 : Planning prépare, Lifecycle autorise. Les huit comportements Lifecycle sont combinables, pas une succession de colonnes obligatoires.');save('modeles/backlog/order-lifecycle-behaviors.yaml',ann)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8')
    text=text.replace('**Order Release (U410/U414)**','**Order Release (U410/U417)**').replace('désormais sous Order Backlog Planning D03.p (U414)','sous Order Lifecycle Management D04.o, désormais dans D03 (U417, remplace U414)')
    text=text.replace('U414 crée Order Backlog Planning D03.p et y déplace Order Release BHV039, identité et définition conservées. Lifecycle garde huit comportements ; Split et Structuring restent en D04 à arbitrer.','U417 : Planning D03.p prépare les scénarios ; Order Structuring D04.n et Order Lifecycle Management D04.o sont rattachés à D03. Split BHV044 sous Structuring, Release BHV039 sous Lifecycle ; huit comportements Lifecycle combinables, pas un cycle unique. U414 et les placements U413 sont remplacés sur ces points.')
    text=text.replace('Lifecycle (mutations internes, dont brouillon et Split), Structuring (composition persistante) et Archiving restent transverses.','U417 déplace Lifecycle et Structuring dans D03 : progression/engagements pour Lifecycle, découpage et composition avec Split pour Structuring. Archiving reste dans D04. Les identifiants D04.n/D04.o gardent leur préfixe historique.')
    agents.write_text(text,encoding='utf-8')
    append('marche/elements.md','### ELM248\n\nOracle Split Order Lines 26B ; Microsoft Planned Orders, page mise à jour le 2 septembre 2026. Sources primaires consultées le 19 septembre 2026 ; passages, URL et limites dans modeles/backlog/order-backlog-review.yaml, structure_lifecycle_U417.market_comparisons. Split organise les parties de satisfaction ; statuts et approbation pilotent la préparation des ordres planifiés. Aucune preuve installée ni taxonomie universelle.')
    append('marche/comparaisons.md','### CMP159\n\nU416/U417 — Structuring couvre découpage et composition ; Split est son comportement. Les mutations d’état ne déterminent pas à elles seules un domaine : Lifecycle gouverne les engagements et la progression du carnet dans D03. Oracle documente scission par sites/dates et progression différenciée ; Microsoft documente préparation et approbation des Planned Orders. Le rattachement FLOW est un choix de responsabilité métier, pas une arborescence éditeur reproduite. Planning prépare les scénarios, Lifecycle autorise via Release, Process Orchestration coordonne les services. Gel, affermissement et suspension restent combinables, sans séquence universelle de statuts. U417 révise explicitement U414 ; aucune duplication.')
    append('JOURNAL.md','## 2026-09-19 — U416/U417 : structuration et cycle de vie du carnet\n\nD04.n et D04.o déplacés dans D03 ; définition Structuring élargie et adoptée ; BHV044 sous Structuring, BHV039 sous Lifecycle. Planning recentré sur préparation, sans comportement direct. Identifiants et définitions des comportements conservés. Comparaisons CMP159/ELM248, audit existant, descriptions et AGENTS actualisés. Les preuves U414 restent capturées ; aucune release.')
    (OUT/'README.md').write_text('# U417 — Structuring et Lifecycle dans D03\n\nQuatre liens contains déplacés, aucun identifiant ajouté ou retiré. Split sous Structuring, Release sous Lifecycle ; Planning prépare. Définition Structuring adoptée ; reformulation Planning éditoriale après modification explicite du mandat.\n',encoding='utf-8')
    print('U417 integrated: four parent changes; identifiers and behavior definitions preserved.')


if __name__=='__main__':main()
