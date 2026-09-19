"""Transcribe U271 into the working model; never publish."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append, cycle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-17-scenario-impact'

def save(name, data):
    (ROOT/f'modeles/backlog/{name}.yaml').write_text(dumps(data),encoding='utf-8')

def main():
    if OUT.exists(): raise SystemExit('U271 already captured; do not reapply.')
    OUT.mkdir()
    for name in ['model','d05-refactoring','behavior-audit','modeling-glossary']:
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    protected={}
    for folder in ['release','revisions','decisions','provenance']:
        for p in (ROOT/'modeles'/folder).rglob('*'):
            if p.is_file() and p!=ROOT/'modeles/provenance/source-records.json':
                protected[p.relative_to(ROOT).as_posix()]=sha256(p.read_bytes()).hexdigest()
    (OUT/'protected.json').write_text(json.dumps(protected,indent=2),encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md','''## U271

**id**

U271

**date**

2026-09-17

**titre**

Validation de Scenario Impact Analysis et de ses frontières

**texte**

je valide

**contexte et portée**

Accord sur la réponse immédiatement précédente : sixième comportement Scenario Impact Analysis sous Inventory Planning, définition proposée, bénéfice de rendre les conséquences métier explicites avant appréciation, et distinction des résultats de Simulation, Impact Analysis et Evaluation. La simulation peut déjà produire les indicateurs exploités par l’analyse, sans recalcul imposé. Les trois résultats du tableau sont conservés comme preuves des frontières adoptées ; les exemples sont fictifs. Les compléments d’intégration restent proposés. Aucun niveau supplémentaire, release, commit ou push demandé.''')
    model=read(ROOT/'modeles/backlog/model.yaml')
    assert not any(n['id']=='BHV010' for n in model['nodes'])
    fields={'name':'Scenario Impact Analysis',
            'definition':'Quantifier et expliquer les effets attendus d’un scénario sur les indicateurs métier, par rapport à une situation de référence, pour un périmètre et un horizon donnés.',
            'scope':'Exploiter les résultats de [Scenario Simulation](model:BHV006), qui peut déjà produire les indicateurs ; aucun recalcul indépendant imposé. Expliciter les écarts de service, de stock immobilisé, de risques ou de flux, selon les informations et hypothèses disponibles. Les indicateurs, unités, références, périmètres et horizons doivent permettre une lecture cohérente. Exemple fictif : service projeté de 94 % à 97 %, stock moyen supplémentaire de 120 k€ et transferts en hausse de 15 %. Examiner aussi les écarts par magasin ou période, car une amélioration globale peut masquer des dégradations locales. [Scenario Evaluation](model:BHV007) apprécie ensuite le compromis ; cette séparation de résultats n’impose ni workflow fixe ni logiciels séparés. Les règles précises d’indicateurs et d’explication restent à instruire, sans causalité inventée.'}
    note='U271 adopte le nom, la définition et le rattachement présentés. Périmètre de synthèse ajouté proposé ; frontières conceptuelles adoptées conservées dans le registre U271.'
    node={'id':'BHV010','revision':1,'kind':'behavior','layer':'transactional','fields':fields,
          'source_refs':['U270','U271','CMP091'],'source_locator':{'path':'connaissance/35-comportements-inventory-planning.md','anchor':'bhv010'},
          'review':{'state':'partial','note':note},'adoption_ids':[],
          'lifecycle':cycle(fields,['name','definition'],['U271'],note)}
    # Reading order only, no business sequencing relation.
    model['nodes'].insert(next(i for i,n in enumerate(model['nodes']) if n['id']=='BHV007'),node)
    rel={'id':'REL-PLANNING-BHV010','revision':1,'type':'contains','source_id':'D05.f','target_id':'BHV010','source_refs':['U270','U271'],
         'review':{'state':'accepted','note':'Sixième comportement terminal d’Inventory Planning adopté U271 ; aucun niveau supplémentaire.'}}
    rel['lifecycle']=cycle(rel,['type','source_id','target_id'],['U271'],rel['review']['note'])
    model['relations'].insert(next(i for i,r in enumerate(model['relations']) if r['id']=='REL-PLANNING-BHV007'),rel)
    boundaries={
        'BHV006':'Une situation opérationnelle projetée : stocks, apports, transferts, demandes satisfaites ou restantes.',
        'BHV007':'Une appréciation du compromis selon les objectifs et contraintes.'}
    revised=[]
    for identifier, definition in boundaries.items():
        n=next(n for n in model['nodes'] if n['id']==identifier)
        n['fields']['definition']=definition
        n['fields']['scope']+=(' U271 distingue la situation opérationnelle projetée et son analyse en indicateurs par [Scenario Impact Analysis](model:BHV010). La simulation peut déjà produire ces indicateurs ; aucun calcul doublonné imposé.' if identifier=='BHV006' else ' U271 précise le résultat : apprécier le compromis en exploitant notamment [Scenario Impact Analysis](model:BHV010). Quantifier et expliquer les impacts fournit les éléments d’appréciation ; comparer plusieurs options reste possible, sans conditionner toute évaluation à plusieurs scénarios.')
        n['source_refs']+=['U271','CMP091']
        n['review']['note']='Nom U269 conservé ; définition reprise du résultat présenté dans le tableau adopté U271. Ancienne définition U269 historisée ; périmètre éditorial proposé.'
        n['lifecycle']=cycle(n['fields'],['name','definition'],['U269','U271'],n['review']['note'])
        revised.append({'node_id':identifier,'adopted_fields':['name','definition'],'value_sha256':dict(n['lifecycle']['value_sha256']),'source_refs':['U271']})
    parent=next(n for n in model['nodes'] if n['id']=='D05.f')
    parent['fields']['definition']=parent['fields']['definition'].replace('Construire, simuler, évaluer','Construire, simuler, analyser les impacts, évaluer')
    parent['fields']['scope']=parent['fields']['scope'].replace('Les cinq comportements rattachés décrivent la construction, la simulation, l’évaluation','Les six comportements rattachés décrivent la construction, la simulation, l’analyse d’impact, l’évaluation')
    parent['fields']['scope']+='\n\nU271 distingue situation opérationnelle projetée, conséquences exprimées en indicateurs et appréciation du compromis. Le bénéfice est de rendre explicites les conséquences métier avant appréciation, y compris les écarts locaux masqués par les résultats globaux. Cette clarification justifie le sixième comportement, au même niveau terminal que les cinq autres.'
    parent['review']['note']=parent['review']['note'].replace('Les cinq noms/définitions de comportements sont adoptés sur leurs propres nœuds.','Les six noms/définitions de comportements sont adoptés sur leurs propres nœuds selon U269/U271.')
    parent['source_refs']+=['U270','U271','CMP091']
    principle=next(p for p in model['principles'] if p['id']=='PRINCIPLE-INVENTORY-SCENARIO-APPLICATION')
    principle['statement']=principle['statement'].replace('construction, simulation, évaluation','construction, simulation, analyse d’impact, évaluation')
    principle['source_refs'].append('U271')
    save('model',model)
    annex=read(ROOT/'modeles/backlog/d05-refactoring.yaml')
    annex['scenario_impact_U271']={'source_refs':['U270','U271'],'state':'accepted_in_stated_scope','parent_id':'D05.f',
        'new_behavior':{'node_id':'BHV010','relation_id':rel['id'],'adopted_fields':['name','definition'],'value_sha256':dict(node['lifecycle']['value_sha256'])},
        'revised_behaviors':revised,
        'adopted_boundary_results':{'BHV006':boundaries['BHV006'],'BHV010':'Les conséquences exprimées en indicateurs, leurs écarts à une référence et leurs explications.','BHV007':boundaries['BHV007']},
        'adopted_benefit':'Rendre les conséquences métier explicites avant d’apprécier le scénario ; montrer qu’une amélioration globale masque éventuellement une dégradation sur certains magasins ou certaines périodes.',
        'computation_boundary':'La simulation peut déjà produire les indicateurs : l’analyse d’impact les exploite et les explique, sans imposer de les recalculer.',
        'historical_capture':'audits/2026-09-17-scenario-impact/model-before.yaml',
        'proposed_details':'Synthèses de périmètre ajoutées ; pas d’adoption des règles détaillées d’indicateurs ni des équivalences marché.',
        'market_comparison':'CMP091'}
    save('d05-refactoring',annex)
    audit=read(ROOT/'modeles/backlog/behavior-audit.yaml')
    audit['scenario_impact_U270'].update({'state':'adopted_in_stated_scope','catalog_changed':True,'implementation_source':'U271','node_id':'BHV010','adopted_name':fields['name'],'adopted_definition':fields['definition'],'scope_note':'Nom, définition, rattachement, bénéfice et frontières présentés adoptés ; compléments éditoriaux proposés.'})
    audit['scenario_impact_U270']['source_refs'].append('U271')
    audit['scenario_impact_U270'].pop('proposed_name');audit['scenario_impact_U270'].pop('proposed_definition')
    entry=next(e for e in audit['assessments'] if e['capability_id']=='D05.f')
    entry['recommendation']='Conserver et décomposer en six comportements adoptés U269/U271'
    entry['candidate_detail']=entry['candidate_detail'].replace('Scenario Simulation;','Scenario Simulation; Scenario Impact Analysis;')
    entry['source_refs'].append('U271')
    audit['decision_boundary']+=' U271 adopte également les portées détaillées dans scenario_impact_U270.'
    save('behavior-audit',audit)
    glossary=read(ROOT/'modeles/backlog/modeling-glossary.yaml')
    term=next(t for t in glossary['terms'] if t['id']=='MOD002')
    term['definition']=term['definition'].replace('Construire, simuler, évaluer','Construire, simuler, analyser les impacts, évaluer')
    term['notes'].append('U271 ajoute Scenario Impact Analysis pour Inventory Planning : quantifier et expliquer les effets attendus sur les indicateurs avant appréciation du compromis. Simulation peut déjà produire ces indicateurs ; aucune duplication de calcul ni nouveau niveau de décomposition.')
    term['source_refs'].append('U271');glossary['source_refs'].append('U271')
    term['review']['adopted_scope']+=' U271 : sixième comportement et frontières Simulation / Impact Analysis / Evaluation adoptés pour Inventory Planning.'
    save('modeling-glossary',glossary)
    append('marche/comparaisons.md','''Complément U271 à CMP091 — 17 septembre 2026 : Scenario Impact Analysis, sa définition, son rattachement à Inventory Planning, son bénéfice et les frontières présentées avec Simulation/Evaluation sont adoptés. Les fonctions SAP et Oracle restent des appuis, sans équivalence normative adoptée. Les sources consultées U270 sont réutilisées pour transcrire cet accord ; aucune nouvelle proposition marché.''')
    append('JOURNAL.md','''## 2026-09-17 — U271 : Scenario Impact Analysis adopté

BHV010 ajouté sous Inventory Planning, avec nom, définition et rattachement adoptés. Définitions BHV006/BHV007 précisées par les résultats du tableau accepté ; valeurs U269 conservées dans la capture pré-U271 et le registre historique. Compléments de périmètre proposés. Six comportements Planning et quatre ATP, sans nouvelle capacité. Justification et frontières consignées, glossaire méthodologique et suivi d’audit alignés. Aucune release, aucun commit ni push.''')
    print('Applied U271: 41 capabilities, 10 behaviors, six under Inventory Planning.')

if __name__=='__main__': main()
