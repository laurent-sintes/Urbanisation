"""Audit local terminology and add the requested business glossary distinctions."""
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import re

from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'audits/2026-09-18-supply-fulfillment'
PATTERN = re.compile(r'\bsupply\b|\bfulfill?ment\b', re.I)
REFS = ['U366', 'U367', 'ELM225', 'CMP136']


def append(path, text):
    with (ROOT/path).open('a', encoding='utf-8') as f:
        f.write('\n\n'+text.strip()+'\n')


def main():
    assert not OUT.exists(), 'Audit already recorded.'
    OUT.mkdir()
    mp=ROOT/'modeles/backlog/model.yaml'
    gp=ROOT/'modeles/backlog/glossary.yaml'
    model, glossary = read(mp), read(gp)
    before=deepcopy(glossary)
    (OUT/'glossary-before.yaml').write_bytes(gp.read_bytes())
    baseline={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in [
        'modeles/backlog/model.yaml', 'modeles/backlog/glossary.yaml',
        'modeles/backlog/modeling-glossary.yaml', 'modeles/release/index.json']}
    for identifier,title,quote,scope in [
        ('U366','Audit local Supply et Fulfillment',
         "J'aime beaucoup la définition microsoft. Peut être que partout on a mis Supply il fallait mettre Fulfillment. J'aimerais un audit local sur ce sujet.",
         'Demande d’audit ciblé des usages du modèle courant, au regard de Microsoft et des références pertinentes. Hypothèse de renommage à examiner, aucun remplacement global adopté.'),
        ('U367','Distinguer Supply, Supply Chain et Fulfillment dans le glossaire',
         'Il faut bien définir dans le glossaire la diff entre les termes Supply, Supply Chain et Fulfillment',
         'Complément au même audit : ajouter les distinctions au glossaire métier. Le sens fonctionnel local Supply acquis en U56 est préservé et distingué du sens ressources. Les nouvelles formulations sont éditoriales, sans adoption automatique des renommages proposés.')]:
        assert '## '+identifier+'\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        append('connaissance/01-contributions-utilisateur.md',f'## {identifier}\n\n**id**\n\n{identifier}\n\n**date**\n\n2026-09-18\n\n**titre**\n\n{title}\n\n**texte**\n\n{quote}\n\n**contexte et portée**\n\n{scope}')

    def source(identifier,vendor,product,title,url,edition,passage,fact,limit):
        return dict(id=identifier,vendor=vendor,product=product,title=title,url=url,edition=edition,
            consulted_on='2026-09-18',passage=passage,fact=fact,limit=limit,
            evidence='Documentation primaire ouverte ou passage primaire indexé consulté ; synthèse sélective, aucune réalisation Beaumanoir déduite.')
    sources=[
        source('SF01','Microsoft','Dynamics 365 Business Central','Balancing supply and demand',
            'https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-balancing-demand-and-supply',
            'Documentation évolutive','Supply and demand ; Process orders ; Priorities on the supply side',
            'Supply désigne le côté ressources : stock et apports entrants, notamment achats, production, transferts entrants et retours clients. Supply orders alimente ce côté du bilan.',
            'Sémantique de planification Business Central, pas définition d’un périmètre organisationnel FLOW.'),
        source('SF02','CSCMP','Définitions professionnelles','SCM Definitions and Glossary of Terms',
            'https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx',
            'Page de référence sans édition affichée','Definitions of Supply Chain Management ; Logistics Management',
            'SCM couvre approvisionnement, transformation, logistique et coordination entre partenaires. Le fulfillment figure parmi les activités logistiques.',
            'Définition de Supply Chain Management, utilisée pour délimiter le périmètre ; ce n’est pas une taxonomie de capacités FLOW.'),
        source('SF03','ASCM','Ressource professionnelle','What is supply chain logistics?',
            'https://www.ascm.org/topics/logistics/', 'Page évolutive','Supply chain vs logistics ; Order processing and fulfillment',
            'La supply chain est décrite comme un réseau amont-aval ; le fulfillment est orienté vers la réalisation des commandes.',
            'Présentation pédagogique centrée sur les biens ; ne tranche pas tous les cas de retours ou services numériques FLOW.'),
        source('SF04','Microsoft','Dynamics 365 Intelligent Order Management','Intelligent Fulfillment Optimization',
            'https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch',
            'Documentation évolutive','Fulfillment sources ; Business constraints ; Fulfillment strategies',
            'Stratégies de satisfaction associant sources, objectifs et contraintes ; optimisation possible de commandes groupées et restitution d’un plan.',
            'Service logiciel, plus large qu’une décision de cadre. Objectif de proximité documenté ; aucune équivalence complète à D03 ni solveur universel multiobjectif démontré.'),
        source('SF05','Microsoft','Dynamics 365 Commerce','Store order fulfillment',
            'https://learn.microsoft.com/en-us/dynamics365/commerce/order-fulfillment-overview',
            'Documentation évolutive','Introduction ; Pick ; Pack ; Pick up ; Shipping',
            'Fulfillment inclut des opérations effectives de préparation et remise ou expédition des commandes.',
            'Le produit décrit l’exécution magasin ; FLOW distingue pilotage et opérations internes des exécutants.'),
        source('SF06','SAP','S/4HANA aATP','Backorder Processing — Supply Assignment',
            'https://help.sap.com/docs/PRODUCT_ID/f132c385e0234fe68ae9ff35b2da178c/6b8eb017a1d1431abde00056a249f72b.html',
            '2025 FPS01 (Feb 2026)','Supply Selection ; Assignment ; Reassignment',
            'Supply Assignment relie besoins, stocks et réceptions futures ; réaffectation paramétrable.',
            'Fonction intégrée SAP ; FLOW sépare décision, affectation, réservation et promesse.'),
        source('SF07','SAP','S/4HANA Cloud','Supply Protection (SUP)',
            'https://help.sap.com/docs/PRODUCT_ID/32da8359c8ee4e8b8e8c5e15cacba5aa/c4b704762cbd4611a3ee2dc00c7a7277.html?locale=en-US&state=PRODUCTION&version=2602.500',
            '2602, version URL 2602.500','Use',
            'Protection de quantités pour des groupes face aux demandes concurrentes.',
            'Plus étroit que Supply Protection FLOW qui inclut aussi tampon et régulation des apports.'),
        source('SF08','Microsoft','Dynamics 365 SCM — Inventory Visibility','Inventory allocation',
            'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-allocation',
            'Documentation évolutive','Business background ; Allocation definition',
            'Droits de groupes et contrôle de surconsommation avant les commandes ; distincts de la réservation liée aux ventes.',
            'Appui à deux mécanismes de protection, pas équivalence avec toute la capacité FLOW.')]
    by_source={s['id']:s for s in sources}
    def comparison(sid,position):
        s=by_source[sid]
        return dict(vendor=s['vendor'],product=s['product'],element_name=s['title'],element_type='Notion métier ou fonction produit documentée',
            relationship='Appui sémantique',similarities=s['fact'],differences=s['limit'],source_title=s['title'],source_url=s['url'],
            source_version=s['edition'],source_locator=s['passage'],consulted_on=s['consulted_on'],evidence_limits=s['evidence'],
            flow_position=position,status='proposed',source_refs=REFS)

    # Full local occurrence inventory; links/URLs and historic metadata are separate from current business wording.
    inventory=[]
    def walk(value,path,owner='',name=''):
        if isinstance(value,dict):
            owner=value.get('id',owner)
            name=value.get('fields',{}).get('name',value.get('name',name))
            for k,v in value.items():walk(v,path+'/'+k,owner,name)
        elif isinstance(value,list):
            for i,v in enumerate(value):walk(v,path+'/'+str(i),owner,name)
        elif isinstance(value,str) and PATTERN.search(value):
            keys=path.split('/')
            if 'market_comparisons' in keys:category='market_reference'
            elif any(k in keys for k in ['source_refs','source_locator','id','source_id','target_id','adoption_ids']):category='identifier_or_provenance'
            elif any(k in keys for k in ['lifecycle','review','editorial_basis']):category='validation_or_history'
            elif 'fields' in keys or 'qualification' in keys or keys[-1] in ['name','definition','short_description','context','notes','purpose','boundary']:
                category='current_business_text'
            else:category='context_metadata'
            inventory.append(dict(path=path,owner_id=owner,name=name,category=category,count=len(PATTERN.findall(value)),text=value))
    for path in ['modeles/backlog/model.yaml','modeles/backlog/glossary.yaml','modeles/backlog/modeling-glossary.yaml']:
        walk(read(ROOT/path),path)
    code_hits=[]
    for path in [*sorted((ROOT/'app/src').rglob('*')),ROOT/'app/modeling_guide.py',ROOT/'app/BRANDING.md']:
        if not path.is_file() or path.suffix not in ['.ts','.tsx','.py','.md']:continue
        for line_no,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
            if PATTERN.search(line):code_hits.append(dict(path=path.relative_to(ROOT).as_posix(),line=line_no,text=line.strip()))
    names=[dict(id=n['id'],kind=n['kind'],name=n['fields']['name'],parents=[r['source_id'] for r in model['relations'] if r['target_id']==n['id'] and r['type'] in ['contains','presents']],
                approved_fields=n.get('lifecycle',{}).get('validated_fields',[])) for n in model['nodes'] if PATTERN.search(n['fields']['name'])]
    stats=dict(nodes=len(model['nodes']),capabilities=sum(n['kind']=='capability' for n in model['nodes']),behaviors=sum(n['kind']=='behavior' for n in model['nodes']),
        model_names_supply=sum(bool(re.search(r'\bsupply\b',n['name'],re.I)) for n in names),
        model_names_fulfillment=sum(bool(re.search(r'\bfulfill?ment\b',n['name'],re.I)) for n in names),
        strings_by_category=dict(Counter(i['category'] for i in inventory)),
        current_model_nodes_with_terms=len({i['owner_id'] for i in inventory if i['category']=='current_business_text' and i['path'].startswith('modeles/backlog/model.yaml/nodes/')}))
    (OUT/'inventory.yaml').write_text(dumps(dict(baseline=baseline,scope='Avant clarification U367 ; occurrences de chaînes, pas uniquement libellés. Les catégories empêchent de confondre preuve éditeur, identifiant et nom courant.',stats=stats,names=names,occurrences=inventory,app_hits=code_hits)),encoding='utf-8')

    findings=[]
    def finding(ident,targets,recommendation,reason,sids,priority='P2',candidate=None):
        findings.append(dict(id=ident,target_ids=targets,status='proposed',priority=priority,recommendation=recommendation,candidate_name=candidate,
            reason=reason,market_comparisons=[comparison(sid,reason) for sid in sids]))
    finding('SF-A01',['universe-supply','TER035'],'Conserver Supply comme convention locale explicite ; ne pas remplacer automatiquement par Fulfillment.',
        'Le périmètre englobe stock, optimisation des niveaux, achats, retours et référentiels. Le libellé local ne signifie ni seulement offre de ressources, ni toute la Supply Chain. Réécrire sa définition circulaire serait utile après arbitrage.', ['SF01','SF02','SF03'],'P1')
    finding('SF-A02',['D03'],'Candidat prioritaire à un renommage de domaine, après validation du périmètre.',
        'Le domaine vise la meilleure satisfaction et contient déjà ATP/CTP/PTP, priorités, échéancier, promesses et Supply Assignment. Fulfillment Optimization exprime mieux cette finalité que Order Promising seul ; conserver promesse et application des affectations, sans absorber D05 ni D06. Ce choix est une adaptation FLOW, pas une équivalence de module.', ['SF04','SF06'],'P1','Fulfillment Optimization')
    finding('SF-A03',['D02.e','BHV045','BHV046','BHV047','TER078'],'Conserver les noms Assignment actuels ; écarter le remplacement par Fulfillment Optimization.',
        'Supply désigne ici la ressource affectée ; Assignment décrit le résultat transactionnel. Fulfillment Optimization déplacerait une action vers le calcul et masquerait la frontière avec les décisions. Fulfillment Assignment n’a pas de consensus établi dans les références examinées.', ['SF01','SF06'],'P1')
    finding('SF-A04',['D02.b','BHV017'],'Conserver Supply Protection et Group Supply Protection dans cet audit.',
        'La protection agit sur l’accès aux ressources, leur consommation, les tampons et les apports, y compris avant toute commande. Fulfillment Protection suggérerait une garantie de satisfaction plus large. Le périmètre FLOW dépasse SAP SUP ; cette différence doit rester explicite.', ['SF07','SF08'],'P1')
    finding('SF-A05',['BHV004'],'Conserver Future Supply Projection.',
        'Projection intégrant les ressources attendues, pas projection d’un accomplissement de commande. Future Fulfillment Projection changerait le résultat métier.', ['SF01','SF06'])
    finding('SF-A06',['D13','D13.a','TER054'],'Conserver Fulfillment Network et préciser au besoin ses lieux et relations admissibles.',
        'Le nom adopté porte déjà la finalité. Les lieux peuvent contribuer à achats, transferts ou retours selon le périmètre FLOW ; la documentation Microsoft illustre les sources de satisfaction sans prouver tout ce périmètre.', ['SF04'])
    finding('SF-A07',['TER065','D04','D04.p'],'Réexaminer Supply Order ; préférer Order qualifié par son type dans le contexte déjà défini.',
        'Collision sémantique : FLOW regroupe les Orders traités, alors que supply order chez Microsoft désigne un apport au bilan ressources. Ne pas substituer Fulfillment Order qui pourrait être compris comme un ordre de réalisation. Le maintien ou retrait du terme local demande un arbitrage, sans renommer ses types.', ['SF01'],'P1','Order')
    finding('SF-A08',['D03.n','BHV021','D06','D06.b','D07.a','D06.e','D06.f'],'Clarifier les compléments français selon le résultat, sans renommage général.',
        'Promesse de satisfaction de la commande, ressources présentes ou attendues, prestations nécessaires à la réalisation : ces formulations précisent le sens. Execution Management reste distinct de la réalisation des exécutants, et couvre aussi les services numériques.', ['SF05','SF04'])
    finding('SF-A09',['D01','D05','D04','D08','D14'],'Conserver les finalités Inventory, Order et Execution Service ; ne pas tout préfixer Fulfillment.',
        'Stocks à préparer et optimiser, contenu des Orders et références sont des moyens et responsabilités partagés. Leur contribution à la satisfaction ne suffit pas à les rebaptiser.', ['SF02','SF03'])
    finding('SF-A10',['proposal:Fulfillment Strategy Decision'],'Maintenir la proposition U365 à discuter, sans la compter comme capacité existante.',
        'Choisir le cadre de satisfaction reste distinct du calcul ATP et de l’application. Le nom reprend Fulfillment strategies Microsoft à la maille décisionnelle FLOW ; pas de consensus de catalogue revendiqué.', ['SF04'])

    # Retain the historical project-specific definition; introduce the three general business notions explicitly.
    terms={t['id']:t for t in glossary['terms']}
    assert not {'TER083','TER084','TER085'} & terms.keys()
    local=terms['TER035']
    local['context']='Convention fonctionnelle locale FLOW, distincte du sens ressources de Supply et du périmètre global de la Supply Chain.'
    local['notes']+='\n\nClarification U367 : ce sens local demeure conservé. Voir [Supply](glossary:TER083) pour le côté ressources, [Supply Chain](glossary:TER084) pour le système étendu et [Fulfillment](glossary:TER085) pour la satisfaction des commandes. L’emploi local ne transforme pas ces trois notions en synonymes et ne prouve pas que FLOW couvre toute la Supply Chain.'
    local['source_refs']=list(dict.fromkeys(local['source_refs']+['U56','U57','U58']+REFS))
    local['review']['note']+=' U367 précise le contexte et les renvois sans réécrire la définition historique.'
    local['market_comparisons']=[comparison('SF01','Le sens fonctionnel FLOW est une convention locale ; Microsoft emploie ici supply au sens ressources. Aucune équivalence.'),comparison('SF02','Le périmètre fonctionnel FLOW est plus limité que celui de SCM ; aucune extension de responsabilité par le vocabulaire.')]
    definitions=[
        ('TER083','Supply','Ressources présentes ou attendues qui peuvent répondre à une demande.',
         'Dans les mécanismes de disponibilité, de planification et d’affectation, côté ressources du bilan offre-demande : stock présent et apports attendus, considérés selon leurs quantités, dates et conditions d’admissibilité.',
         'Sens métier ressources, illustré par Microsoft Business Central et SAP ARun ; ce n’est pas un synonyme universel d’approvisionnement ni de Supply Chain.',
         'Exemple fictif : 80 pièces en stock et une réception de 40 constituent des ressources à examiner ; elles ne sont pas nécessairement toutes libres, fiables ou mobilisables à la date voulue. Un même transfert est sortant pour le lieu donneur et entrant pour le receveur : la perspective compte. À distinguer du [sens fonctionnel local FLOW](glossary:TER035), de la [Supply Chain](glossary:TER084) et du [Fulfillment](glossary:TER085).',['SF01','SF06']),
        ('TER084','Supply Chain','Réseau de parties, activités et flux reliant les sources d’approvisionnement aux destinataires.',
         'Système de parties, d’activités et de flux qui relie les sources d’approvisionnement aux destinataires, en intégrant approvisionnement, transformation éventuelle, stockage, distribution et coordination entre partenaires.',
         'Définition éditoriale appuyée sur ASCM et sur le périmètre de Supply Chain Management défini par CSCMP. Supply Chain désigne le système ; Supply Chain Management sa gestion.',
         'Le [Fulfillment](glossary:TER085) est une finalité et un ensemble d’activités au sein de ce système. [Supply](glossary:TER083) désigne le côté ressources dans les calculs. Exemple fictif : fournisseurs, entrepôts, transporteurs, magasins et clients reliés par des flux. Le modèle FLOW n’absorbe pas toutes les responsabilités de cette chaîne : gouvernance des fournisseurs, conception, finance et autres fonctions ne deviennent pas des domaines par cette définition. Les retours et flux inverses existent dans la chaîne ; leur périmètre opérationnel reste explicite.',['SF02','SF03']),
        ('TER085','Fulfillment','Satisfaction effective d’une commande selon les quantités, délais et conditions retenus.',
         'Ensemble des activités qui organisent et réalisent la satisfaction d’une commande : mobiliser les ressources et services nécessaires, coordonner leur mise à disposition et accomplir le résultat attendu selon les quantités, délais et conditions retenus.',
         'La documentation Microsoft distingue optimisation de la satisfaction et opérations effectives de fulfillment. Formulation FLOW proposée ; aucune nouvelle capacité agrégée n’est créée par le terme.',
         'Un calcul ATP, une promesse confirmée ou une affectation seule ne prouve pas la réalisation. Fulfillment Optimization recherche comment satisfaire au mieux ; Fulfillment Strategy fixe le cadre ; les exécutants réalisent les prestations. Exemple fictif : choisir un stock et un service puis préparer et livrer les pièces attendues. Le marché décrit souvent les commandes clients ; l’application aux transferts, achats, retours ou services numériques de FLOW doit préciser le résultat et le point de vue, sans prétendre à une équivalence universelle. Les retours ne sont pas automatiquement inclus ou exclus du seul fait du mot. Voir [Supply](glossary:TER083) et [Supply Chain](glossary:TER084). Orthographe canonique proposée : Fulfillment ; Fulfilment est une variante orthographique.',['SF04','SF05','SF03'])]
    for identifier,name,short,definition,context,notes,sids in definitions:
        glossary['terms'].append(dict(id=identifier,name=name,short_description=short,definition=definition,context=context,notes=notes,
            source_refs=REFS,source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u367'),
            review=dict(state='proposed',note='Définition ajoutée à la demande U367 ; formulation et correspondances éditoriales, sans adoption implicite de noms ou de périmètres.'),
            market_comparisons=[comparison(sid,context) for sid in sids]))
    glossary['source_refs']=list(dict.fromkeys(glossary['source_refs']+REFS))
    gp.write_text(dumps(glossary),encoding='utf-8')
    audit=dict(id='SUPPLY-FULFILLMENT-AUDIT-U366-U367',status='audit_completed_renames_proposed',source_refs=REFS,
        baseline=baseline,inventory_path=(OUT/'inventory.yaml').relative_to(ROOT).as_posix(),stats=stats,
        conclusion='Pas de remplacement global. Supply ressources, Supply fonction locale, Supply Chain système et Fulfillment finalité/processus sont distincts. D03 est le candidat prioritaire à examiner.',
        sources=sources,findings=findings,
        glossary_change=dict(added=['TER083','TER084','TER085'],clarified=['TER035'],preserved_fields=['TER035.name','TER035.definition','TER035.short_description'],status='editorial_definitions_added_as_requested'),
        action_plan=dict(completed=['Inventaire local exhaustif des occurrences des trois YAML courants','Comparaison ciblée et propositions par élément','Glossaire métier clarifié, ancien sens fonctionnel préservé'],
            requires_joint_validation=['D03 Order Promising vers Fulfillment Optimization, avec frontières précises','Maintien ou remplacement de Supply Order','Nom et définition du niveau Supply après clarification de son périmètre','Création et périmètre de Fulfillment Strategy Decision U365'],
            no_rename_recommended=['D02.e et ses trois comportements','D02.b et BHV017','BHV004','D13 et D13.a','D01/D04/D05/D06 par remplacement mécanique']),
        implementation_impact=['Préserver les identifiants, notamment universe-supply et D02.e ; les libellés peuvent évoluer sans migration d’identité.',
            'Un renommage validé implique modèle, liens textuels, glossaire, conventions, correspondances, nouveaux accords de champs, vues dérivées et icônes par nom.',
            'app/src/icons.tsx contient les correspondances de noms ; certaines sont historiques et ne prouvent pas un nœud courant.',
            'Ne pas modifier citations, noms de produits, URLs, archives, empreintes ni publications. Atlas suit uniquement une nouvelle release demandée.'])
    (ROOT/'modeles/backlog/supply-fulfillment-audit.yaml').write_text(dumps(audit),encoding='utf-8')
    append('marche/elements.md','### ELM225\n\nAudit terminologique local U366/U367 ; sources primaires consultées le 18 septembre 2026. Définitions métier, présentations et fonctions produit : ne pas aligner automatiquement leur maille.\n\n'+'\n\n'.join('- '+s['id']+' — '+s['vendor']+' / '+s['title']+' ('+s['edition']+').\n  Source : '+s['url']+'\n  Passage : '+s['passage']+'.\n  Constat : '+s['fact']+'\n  Limite : '+s['limit'] for s in sources))
    append('marche/comparaisons.md','''## CMP136

- Codex ; 18 septembre 2026 ; U366/U367 ; ELM225 ; audit du backlog et du glossaire, sans renommage du catalogue.
- Supply, Supply Chain et Fulfillment sont distingués dans TER083–085 ; TER035 conserve la convention locale et sa définition antérieure. Appuis marché et limites dans les fiches.
- D03 vers Fulfillment Optimization est un candidat de nommage orienté finalité, à valider avec ses frontières. D02.e applique déjà les affectations sous D03 : ne pas déplacer sa responsabilité par confusion entre optimisation et application. Supply Protection et Future Supply Projection restent orientés ressources. Supply Order est un faux ami potentiel par rapport aux ordres d’apport Microsoft.
- Inventaire et décisions proposées : modeles/backlog/supply-fulfillment-audit.yaml ; restitution audits/2026-09-18-supply-fulfillment/rapport.md. Correspondances qualifiées par élément, sans consensus universel inventé.
- Aucune nouvelle définition n’étend automatiquement FLOW à toute la Supply Chain, ni Fulfillment à tous les types d’Orders et services. Comparaisons proposées ; demande d’audit et de glossaire ne vaut pas accord sur les renommages.''')
    append('JOURNAL.md','''## 2026-09-18 — U366/U367 : audit Supply / Fulfillment et glossaire

Audit local du catalogue, des relations, des deux glossaires, des conventions utiles et des noms d’icônes Atlas. Clarification métier Supply / Supply Chain / Fulfillment ; sens fonctionnel local Supply conservé. Renommage de D03 proposé, aucune substitution globale. Inventaire et recommandations dans audits/2026-09-18-supply-fulfillment et annexe structurée ; catalogue et publications inchangés.''')
    checks=dict(model_unchanged=sha256(mp.read_bytes()).hexdigest()==baseline['modeles/backlog/model.yaml'],
        methodological_glossary_unchanged=sha256((ROOT/'modeles/backlog/modeling-glossary.yaml').read_bytes()).hexdigest()==baseline['modeles/backlog/modeling-glossary.yaml'],
        release_index_unchanged=sha256((ROOT/'modeles/release/index.json').read_bytes()).hexdigest()==baseline['modeles/release/index.json'],
        new_terms=['TER083','TER084','TER085'],modified_terms=['TER035'])
    old={t['id']:t for t in before['terms']}; new={t['id']:t for t in glossary['terms']}
    assert {i for i in old if old[i]!=new[i]}=={'TER035'}
    assert all(new['TER035'][f]==old['TER035'][f] for f in ['name','definition','short_description'])
    protected=json.loads((ROOT/'audits/2026-09-17-refonte-appliquee/protected.json').read_text(encoding='utf-8'))
    assert all(sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in protected.items())
    checks['protected_files_unchanged']=len(protected)
    assert all(checks[k] for k in ['model_unchanged','methodological_glossary_unchanged','release_index_unchanged'])
    (OUT/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False))


if __name__=='__main__':
    main()
