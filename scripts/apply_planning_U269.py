"""Apply the explicit U269 agreement; preserve earlier values and publications."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-planning-comportements'

def append(path, text):
    with (ROOT/path).open('ab') as f:
        f.write(('\n\n'+text.strip()+'\n').replace('\n','\r\n').encode('utf-8'))

def cycle(values, fields, sources, note):
    return {'state':'urbanist_validated','recorded_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
            'recorded_by':'Codex','source_refs':sources,'validated_fields':fields,
            'value_sha256':{k:value_hash(values[k]) for k in fields},'note':note}

def main():
    if OUT.exists(): raise SystemExit('U269 capture already exists; do not reapply.')
    OUT.mkdir()
    protected={}
    for directory in ['release','revisions','decisions','provenance']:
        for p in (ROOT/'modeles'/directory).rglob('*'):
            if p.is_file() and p != ROOT/'modeles/provenance/source-records.json':
                protected[p.relative_to(ROOT).as_posix()]=sha256(p.read_bytes()).hexdigest()
    (OUT/'protected.json').write_text(json.dumps(protected,indent=2),encoding='utf-8')
    for name in ['model','modeling-glossary','d05-refactoring','behavior-audit']:
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    append('connaissance/01-contributions-utilisateur.md','''## U269

**id**

U269

**date**

2026-09-17

**titre**

Validation des cinq comportements du scénario pour Inventory Planning

**texte**

On valide.

**contexte et portée**

Accord sur la proposition immédiatement précédente : Scenario Construction, Scenario Simulation, Scenario Evaluation, Scenario Validation et Scenario Application sous Inventory Planning, avec les descriptions courtes présentées et le bénéfice du découpage. Application déclenche les actions retenues et connaît leur prise en compte via les capacités opérationnelles responsables ; Supply Protection, gestions d’Orders D04 et pilotage D06 conservent leurs responsabilités. Les correspondances marché justifient la proposition sans devenir des équivalences normatives validées. Autorise la mise à jour du backlog ; aucune release demandée. Les compléments éditoriaux rédigés lors de l’intégration restent proposés.''')
    model=read(ROOT/'modeles/backlog/model.yaml')
    assert not any(n['id'] in ['BHV005','BHV006','BHV007','BHV008','BHV009'] for n in model['nodes'])
    records=[
        ('BHV005','Scenario Construction','Définir périmètre, hypothèses, objectifs et contraintes.',
         'Construire un premier scénario, le copier ou modifier ses hypothèses. Exemple fictif : préparer deux scénarios de couverture magasin à 10 et 15 jours pour une promotion, avec le même périmètre de comparaison. La construction explicite ce qui sera exploré ; elle ne change pas à elle seule les protections ou Orders opérationnels.'),
        ('BHV006','Scenario Simulation','Produire les conséquences projetées en mobilisant nos décisions spécialisées.',
         'Mobiliser les décisions pertinentes de cibles de couverture, allocations, réapprovisionnement et redistribution. Exemple fictif : établir les apports et transferts proposés et leurs conséquences pour chaque scénario. Les calculs restent dans les décisions spécialisées ; les résultats simulés ne sont pas des mouvements de stock réalisés.'),
        ('BHV007','Scenario Evaluation','Apprécier les résultats selon des critères. La comparaison fait partie de cette évaluation, qui peut aussi concerner un seul scénario.',
         'Apprécier disponibilité, immobilisation et risque selon des critères explicites ; comparer si utile à une référence ou à plusieurs scénarios. Exemple fictif : examiner si le service attendu justifie davantage de stock et signaler les contraintes non satisfaites. Les critères détaillés, pondérations et règles d’arbitrage restent à préciser.'),
        ('BHV008','Scenario Validation','Retenir et autoriser un scénario, avec ses conditions et réserves.',
         'Identifier le scénario autorisé pour application et les conditions de cet accord. Exemple fictif : retenir le scénario de couverture à 10 jours sur certains magasins, sous réserve des ressources admissibles. Une validation peut être automatique selon les règles ; elle ne prouve pas l’application effective et ne valide pas les définitions du modèle d’urbanisme.'),
        ('BHV009','Scenario Application','Déclencher les actions retenues et connaître leur prise en compte, via les capacités opérationnelles responsables.',
         'Solliciter [Supply Protection](model:D02.b) pour les protections applicables, les capacités d’[Order Management](model:D04) pour les Orders concernés, puis [Execution Management](model:D06) pour les prestations. Ces capacités conservent leurs responsabilités transactionnelles et opérationnelles. Exemple fictif : demander l’application des seuils retenus et la création des Orders nécessaires, puis distinguer les actions prises en compte, refusées ou restant à traiter. Ne pas confondre scénario retenu, actions engagées et prestations physiquement réalisées. Le détail des dépendances, reprises et conditions de traitement partiel reste proposé ; aucun lot atomique ni séquence technique universelle imposé.')]
    adopted=[]
    for identifier,name,definition,scope in records:
        fields={'name':name,'definition':definition,'scope':scope}
        note='U269 adopte nom et définition courte présentés ; périmètre et exemple éditoriaux ajoutés restent proposés.'
        node={'id':identifier,'revision':1,'kind':'behavior','layer':'transactional','fields':fields,
              'source_refs':['U267','U269','CMP090'],'source_locator':{'path':'connaissance/35-comportements-inventory-planning.md','anchor':identifier.lower()},
              'review':{'state':'partial','note':note},'adoption_ids':[],
              'lifecycle':cycle(fields,['name','definition'],['U269'],note)}
        model['nodes'].append(node)
        relation={'id':f'REL-PLANNING-{identifier}','revision':1,'type':'contains','source_id':'D05.f','target_id':identifier,
                  'source_refs':['U267','U269'],'review':{'state':'accepted','note':'Comportement terminal d’Inventory Planning adopté U269.'}}
        relation['lifecycle']=cycle(relation,['type','source_id','target_id'],['U269'],'Rattachement adopté avec le découpage présenté.')
        model['relations'].append(relation)
        adopted.append({'node_id':identifier,'relation_id':relation['id'],'adopted_fields':['name','definition'],
                        'value_sha256':{k:value_hash(fields[k]) for k in ['name','definition']},'source_refs':['U269']})
    parent=next(n for n in model['nodes'] if n['id']=='D05.f')
    parent['fields']['definition']='Construire, simuler, évaluer et valider des scénarios de stock en mobilisant les décisions spécialisées, puis déclencher les actions retenues et connaître leur prise en compte via les capacités opérationnelles responsables.'
    parent['fields']['finality']='Retenir un scénario de stock cohérent et explicite, puis relier ce choix à sa mise en action.'
    parent['fields']['decomposition_rationale']='Distinguer ce qu’on envisage, ses conséquences, son intérêt, ce qu’on retient et ce qu’on met effectivement en action.'
    parent['fields']['scope']='Les cinq comportements rattachés décrivent la construction, la simulation, l’évaluation, la validation et l’application du scénario. Inventory Planning mobilise les quatre décisions d’Inventory Optimization ; elles conservent leurs responsabilités et ne sont pas ses comportements enfants.\n\nExemple fictif : construire deux scénarios de couverture magasin à 10 et 15 jours avant une promotion, simuler leurs apports et transferts, comparer disponibilité, immobilisation et risque, retenir un scénario puis solliciter les capacités responsables pour sa mise en action.\n\nL’application déclenche les actions retenues et connaît leur prise en compte ; elle sollicite Supply Protection, les gestions d’Orders D04 et D06 pour les prestations. La validation du scénario ne prouve pas que ses actions sont appliquées. Les opérations peuvent être automatiques selon les règles ; aucun contrôle humain systématique ni enchaînement technique imposé. Les exécutants conservent la réalisation physique.\n\nLes horizons restent opérationnels ; les prévisions, coûts et contraintes peuvent être des entrées sans ajout de planification de saison. Les détails d’application partielle, de refus et de reprise sont à instruire.'
    parent['source_refs']+=['U267','U269','CMP090']
    parent['source_locator']={'path':'connaissance/35-comportements-inventory-planning.md','anchor':'inventory-planning'}
    parent['editorial_basis']='U269 adopte les cinq comportements et le bénéfice du découpage. La synthèse de définition/finalité/périmètre rédigée lors de l’intégration est proposée ; ancienne définition U235 conservée dans la capture pré-U269.'
    parent['review']={'state':'partial','note':'Nom Inventory Planning conservé ; justification du découpage adoptée U269. Les cinq noms/définitions de comportements sont adoptés sur leurs propres nœuds. Synthèse de capacité et périmètre éditorial proposés.'}
    parent['lifecycle']=cycle(parent['fields'],['name','decomposition_rationale'],['U235','U269'],'Nom U235 conservé et justification U269 adoptée. Ancienne définition U235 remplacée par une synthèse proposée ; pas de validation héritée de cette formulation.')
    domain=next(n for n in model['nodes'] if n['id']=='D05')
    domain['fields']['scope']=domain['fields']['scope'].replace('les mobilise pour reconfigurer, simuler et valider un scénario cohérent','les mobilise pour construire, simuler, évaluer et valider un scénario cohérent, puis en déclencher l’application via les capacités responsables').replace('Le déclenchement effectif n’est pas une capacité ajoutée dans D05.','Le comportement Scenario Application d’Inventory Planning déclenche les actions retenues et connaît leur prise en compte via ces capacités responsables ; aucune nouvelle capacité autonome de déclenchement n’est ajoutée dans D05.')
    domain['source_refs'].append('U269')
    domain['review']['note']+=' U269 : périmètre aligné sur les comportements adoptés ; les trois champs validés du domaine restent inchangés.'
    model['principles'].append({'id':'PRINCIPLE-INVENTORY-SCENARIO-APPLICATION','statement':'Inventory Planning comporte construction, simulation, évaluation, validation et application du scénario. L’application déclenche les actions retenues et connaît leur prise en compte via les capacités opérationnelles responsables ; Supply Protection, gestion des Orders et pilotage des prestations conservent leurs responsabilités.','source_refs':['U267','U269']})
    (ROOT/'modeles/backlog/model.yaml').write_text(dumps(model),encoding='utf-8')
    annex=read(ROOT/'modeles/backlog/d05-refactoring.yaml')
    annex['scenario_behaviors_U269']={'source_refs':['U267','U269'],'state':'accepted_in_stated_scope','parent_id':'D05.f','behaviors':adopted,
        'decomposition_rationale_sha256':value_hash(parent['fields']['decomposition_rationale']),
        'historical_capture':'audits/2026-09-17-planning-comportements/model-before.yaml',
        'proposed_details':'Synthèse de la capacité, périmètres et exemples ajoutés ; aucune reprise de la validation de l’ancienne définition U235 sur sa nouvelle formulation.',
        'market_comparison':'CMP090 ; appui fonctionnel, pas équivalence normative adoptée.'}
    (ROOT/'modeles/backlog/d05-refactoring.yaml').write_text(dumps(annex),encoding='utf-8')
    audit=read(ROOT/'modeles/backlog/behavior-audit.yaml')
    audit['scenario_planning_U267'].update({'state':'adopted_in_stated_scope','catalog_changed':True,'implementation_source':'U269','behavior_ids':[r[0] for r in records], 'scope_note':'Cinq noms, descriptions courtes, rattachements et bénéfice adoptés ; mandat d’application via les capacités responsables adopté. Autres arbitrages de l’audit inchangés.'})
    audit['scenario_planning_U267']['source_refs'].append('U269')
    audit['decision_boundary']='Les recommandations de l’audit restent proposées sauf les portées explicitement adoptées en scenario_planning_U267 / U269. Aucune fusion ou rétrogradation de capacité appliquée.'
    entry=next(e for e in audit['assessments'] if e['capability_id']=='D05.f')
    entry.update({'state':'adopted_in_stated_scope','recommendation':'Conserver et décomposer en cinq comportements adoptés U269','candidate_detail':'; '.join(r[1] for r in records),'complexity_or_targeted_benefit':parent['fields']['decomposition_rationale']})
    entry['source_refs'].append('U269')
    (ROOT/'modeles/backlog/behavior-audit.yaml').write_text(dumps(audit),encoding='utf-8')
    glossary=read(ROOT/'modeles/backlog/modeling-glossary.yaml')
    term=next(t for t in glossary['terms'] if t['id']=='MOD002')
    term['definition']='Construire, simuler, évaluer et valider des scénarios en mobilisant les capacités de décision, puis déclencher leur application via les capacités opérationnelles responsables.'
    term['notes']=[term['notes'][0],term['notes'][1], 'U269 adopte ces cinq comportements pour Inventory Planning, avec les noms et descriptions présentés. L’application relie le scénario aux actions des capacités opérationnelles sans absorber leurs responsabilités. La généralisation de cette synthèse à toutes les capacités Planning reste proposée.']
    term['source_refs'].append('U269')
    term['review']['adopted_scope']='U229 : les capacités Planning se nourrissent de Decision. U269 : cinq comportements de scénario adoptés pour Inventory Planning, dont l’application via les capacités opérationnelles responsables.'
    term['review']['proposed_scope']='Synthèse de définition et généralisation au-delà d’Inventory Planning ; aucune nouvelle décomposition automatique des autres capacités.'
    glossary['source_refs'].append('U269')
    (ROOT/'modeles/backlog/modeling-glossary.yaml').write_text(dumps(glossary),encoding='utf-8')
    lines=['# Comportements d’Inventory Planning — U269','','## Inventory Planning','',
           'Les cinq noms, descriptions courtes et rattachements sont adoptés le 17 septembre 2026. La justification du découpage est adoptée ; les périmètres et exemples ajoutés restent proposés. L’ancienne définition U235 de la capacité est historisée ; sa nouvelle synthèse ne reprend pas automatiquement cette validation.','',
           '**Bénéfice du découpage :** '+parent['fields']['decomposition_rationale'],'']
    for identifier,name,definition,scope in records:
        lines += [f'## {identifier}', '', f'**{name}** — {definition}', '', '**Périmètre et exemple proposés :** '+scope,'']
    lines+=['## Sources et portée','','U267 propose le découpage ; U268 exige sa justification ; U269 valide la réponse présentée. [Comparaison marché CMP090](../audits/2026-09-17-audit-comportements/scenario-planning-proposition.md) : SAP IBP, Microsoft SCM et Oracle Planning, fonctions consultées sans équivalence normative. Les quatre décisions D05 restent directement rattachées au domaine. Aucune release implicite.','']
    (ROOT/'connaissance/35-comportements-inventory-planning.md').write_text('\n'.join(lines),encoding='utf-8')
    append('connaissance/31-inventory-optimization.md','''## Actualisation U269 — comportements du scénario

La description D05.f ci-dessus conserve l’état U235. U269 adopte désormais Scenario Construction, Scenario Simulation, Scenario Evaluation, Scenario Validation et Scenario Application. L’application déclenche les actions retenues et connaît leur prise en compte via les capacités opérationnelles responsables. Leurs responsabilités restent distinctes ; les quatre décisions D05 ne deviennent pas des comportements. Valeurs et portées courantes dans le modèle YAML et [les cinq comportements](35-comportements-inventory-planning.md). La synthèse de capacité actualisée reste proposée, sans héritage automatique de l’ancienne définition.''')
    append('marche/comparaisons.md','''Complément U269 à CMP090 — 17 septembre 2026 : les cinq noms, descriptions courtes, rattachements à Inventory Planning et bénéfice du découpage sont adoptés. Application via capacités opérationnelles responsables adoptée. Les rapprochements SAP/Microsoft/Oracle restent des appuis fonctionnels proposés, sans adoption d’équivalence normative ; sources déjà consultées U267/U268, aucune nouvelle comparaison nécessaire pour cette transcription.''')
    append('JOURNAL.md','''## 2026-09-17 — U269 : cinq comportements Inventory Planning adoptés

U269 enregistré puis appliqué : BHV005–BHV009 et cinq rattachements terminaux à D05.f. Noms anglais, descriptions courtes et justification du découpage adoptés ; scopes/exemples ajoutés proposés. L’application sollicite les capacités opérationnelles responsables. Synthèse D05.f et périmètre D05 alignés ; ancienne définition U235 historisée sans transport de validation. MOD002, annexe D05, suivi d’audit et CMP090 actualisés. Catalogue de 41 capacités conservé ; neuf comportements. Aucune release, aucun commit ou push.''')
    print('Applied U269: 41 capabilities, 9 behaviors; publication untouched.')

if __name__=='__main__': main()
