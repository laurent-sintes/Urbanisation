"""Record the mechanism-first correction without inventing its target catalog."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.apply_planning_U269 import append

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-comportements-mecanismes'


def main():
    if OUT.exists():
        raise SystemExit('U282 already recorded.')
    OUT.mkdir()
    for name in ('model','supply-protection-review','behavior-audit','modeling-glossary'):
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    (OUT/'study-before.md').write_bytes((ROOT/'marche/supply-protection-comportements.md').read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    protected={p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for folder in ('release','revisions','decisions') for p in (ROOT/'modeles'/folder).rglob('*') if p.is_file()}
    append('connaissance/01-contributions-utilisateur.md','''## U282

**id**

U282

**date**

2026-09-17

**titre**

Comportements centrés sur les mécanismes métier de protection

**texte**

Je viens de lire l'étude complète.

Je me rends compte que le terme d'allocation et lister les opérations qu'on peut faire sur le concept d'allocation n'est peut être pas la bonne méthode de découpage. L'approche qui liste les mécanismes de protection est plus ce que je recherche dérriere le concept de comportement. Allouer / désallouer, etc. ça ressemble à des fonctions que je laisserai au chef de produit pour le développement. Les mécanismes m'interessent bcp plus.

**contexte et portée**

Laurent précise la maille recherchée derrière Comportement : mécanismes métier, plutôt que catalogue des opérations sur un concept. Le découpage Allocation/réallocation/libération/consommation/consultation et la liste de 17 opérations doivent être réexaminés selon ce critère. Les détails fonctionnels restent utiles au chef de produit. Cette correction n’adopte aucun nouveau nom ni catalogue de mécanismes et ne retire pas automatiquement les comportements ATP ou Inventory Planning. Conserver les accords historiques et les identifiants ; signaler explicitement le réexamen courant.''')
    note='U282 : découpage par opérations remis en question au profit des mécanismes métier de protection. Valeurs et accords historiques conservés pour traçabilité ; cible à refondre, pas à reprendre comme découpage recommandé.'
    model=read(ROOT/'modeles/backlog/model.yaml')
    before=read(OUT/'model-before.yaml')
    for n in model['nodes']:
        if n['id'] in ('D02.b','BHV011','BHV012','BHV013','BHV014','BHV015'):
            n['review']['state']='under_review'
            n['review']['note']+=' '+note
            n['source_refs'].append('U282')
    (ROOT/'modeles/backlog/model.yaml').write_text(dumps(model),encoding='utf-8')
    study=read(ROOT/'modeles/backlog/supply-protection-review.yaml')
    study['state']='under_review'
    study['source_refs'].append('U282')
    study['current_direction_U282']={'state':'adopted_direction_target_pending','source_refs':['U282'],
        'direction':'Décrire les mécanismes métier par lesquels Supply Protection protège contre pénurie, surstock et déséquilibre ; distinguer les opérations fonctionnelles qui les administrent.',
        'previous_candidates_status':'Les 17 lignes restent une matière fonctionnelle historique ; elles ne sont plus le découpage cible recommandé.',
        'proposed_description_grid':['Risque métier adressé','Principe du mécanisme','Conditions et résultat métier','Cas concret','Décisions mobilisées et frontières','Complexité ou bénéfice ciblé'],
        'next_step':'Requalifier la matrice des mécanismes, vérifier les recouvrements et proposer les comportements sans les déduire des API.'}
    (ROOT/'modeles/backlog/supply-protection-review.yaml').write_text(dumps(study),encoding='utf-8')
    audit=read(ROOT/'modeles/backlog/behavior-audit.yaml')
    for key in ('allocation_U278','protection_market_U280'):
        audit[key]['current_review_U282']=note
    audit['protection_market_U280']['state']='under_review'
    entry=next(e for e in audit['assessments'] if e['capability_id']=='D02.b')
    entry['state']='under_review'
    entry['recommendation']='Refondre les comportements autour des mécanismes métier de protection (U282) ; opérations conservées comme matière fonctionnelle produit.'
    entry['candidate_detail']='Cible à proposer depuis les mécanismes ; la liste des opérations ne vaut plus recommandation de découpage.'
    entry['source_refs'].append('U282')
    audit['decision_boundary']+=' U282 remet en question la décomposition opérationnelle U278/U280 au profit des mécanismes ; accords antérieurs historisés, nouveau catalogue à proposer.'
    (ROOT/'modeles/backlog/behavior-audit.yaml').write_text(dumps(audit),encoding='utf-8')
    glossary=read(ROOT/'modeles/backlog/modeling-glossary.yaml')
    term=next(t for t in glossary['terms'] if t['id']=='MOD006')
    term['notes'].append('U282 précise la maille recherchée sur Supply Protection : mécanismes métier de protection, plutôt que liste des opérations sur Allocation. Les opérations fonctionnelles restent matière de conception produit ; elles ne constituent pas un nouveau niveau inférieur dans le modèle. La nouvelle décomposition cible reste à proposer.')
    term['source_refs'].append('U282')
    term['review']['adopted_scope']+=' U282 : préférence explicite pour les mécanismes métier plutôt que les opérations, illustrée par Supply Protection.'
    glossary['source_refs'].append('U282')
    (ROOT/'modeles/backlog/modeling-glossary.yaml').write_text(dumps(glossary),encoding='utf-8')
    path=ROOT/'AGENTS.md'
    text=path.read_text(encoding='utf-8')
    anchor='- Objets métier, documents et événements restent distincts ;'
    assert anchor in text
    text=text.replace(anchor,'- **Maille des comportements (U282)** : rechercher les mécanismes métier et leurs effets, plutôt qu’une liste d’opérations sur un concept. Pour Supply Protection, le découpage allocation/réallocation/libération et la liste de 17 opérations sont en réexamen ; les détails fonctionnels alimentent la conception produit. Ne pas réappliquer ce découpage historique ni refondre automatiquement ATP ou Planning.\n'+anchor,1)
    path.write_text(text,encoding='utf-8')
    path=ROOT/'marche/supply-protection-comportements.md'
    old=path.read_text(encoding='utf-8')
    marker='# Supply Protection — étude des comportements\n'
    assert old.startswith(marker)
    path.write_text(marker+'\n> **Réorientation U282 — 17 septembre 2026.** La liste de 17 opérations ci-dessous est remise en question comme décomposition en comportements. Elle reste une matière fonctionnelle documentée pour la conception produit. La cible doit être reconstruite à partir des mécanismes de protection : risque, principe, conditions et effet métier. Les cinq comportements existants sont en réexamen ; aucun nouveau catalogue de mécanismes n’est encore adopté.\n'+old[len(marker):],encoding='utf-8')
    append('marche/comparaisons.md','''Complément U282 à CMP093 — 17 septembre 2026 : la recommandation de 17 comportements est remise en question. Conserver les preuves fonctionnelles, reprendre la décomposition par mécanismes. Sources S05 SAP SuP, S02 Microsoft méthodes de réassort et S07 Oracle politiques reconsultées : mécanismes/politiques et opérations d’administration sont des lectures distinctes. La cible de mécanismes sera un choix FLOW justifié par risques et effets ; aucune nouvelle équivalence ni liste adoptée.''')
    append('JOURNAL.md','''## 2026-09-17 — U282 : recentrage des comportements sur les mécanismes métier

Correction utilisateur enregistrée. AGENTS et MOD006 précisés ; D02.b et BHV011–015 placés en réexamen sans changer leurs valeurs historiques ni identifiants. L’étude de 17 opérations est signalée comme matière fonctionnelle historique, plus comme cible recommandée. Sources et accords préservés ; nouveau catalogue de mécanismes à proposer. Aucune publication ni modification des comportements ATP/Planning.''')
    assert all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in protected.items())
    assert model['relations']==before['relations']
    old_nodes={n['id']:n for n in before['nodes']}
    assert all(n['fields']==old_nodes[n['id']]['fields'] and n.get('lifecycle')==old_nodes[n['id']].get('lifecycle') for n in model['nodes'])
    (OUT/'integrity.json').write_text(json.dumps({'publications_unchanged':protected,'all_node_values_and_adoption_hashes_unchanged':True,'relations_unchanged':True,'reviewed_nodes':['D02.b','BHV011','BHV012','BHV013','BHV014','BHV015']},indent=2),encoding='utf-8')
    print('U282 recorded; operational decomposition under review; historic values and publications preserved.')


if __name__=='__main__':
    main()
