"""Apply the scoped agreement U316; preserve prior values and published evidence."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path

from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash
from scripts.record_tracking_U303 import append

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-initial-stocking'


def main():
    assert not OUT.exists(), 'Agreement already captured; do not reapply.'
    assert '## U316\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    OUT.mkdir()
    for name in ['model', 'glossary', 'd05-refactoring', 'behavior-gap-audit']:
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    (OUT/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    append('connaissance/01-contributions-utilisateur.md', '''## U316

**id**

U316

**date**

2026-09-18

**titre**

Adoption d’Initial Stocking Decision pour l’implantation

**texte**

Ok pour ta proposition

**contexte et portée**

Accord sur la proposition immédiatement précédente : Initial Stocking / Initial Stocking Decision pour l’implantation, avec la définition présentée (« Déterminer les quantités à apporter à chaque magasin et leurs dates pour constituer le stock initial nécessaire au lancement, à partir de l’assortiment retenu, des objectifs de stock et des contraintes applicables. »). Deux décisions distinctes selon U313 : constituer le stock de départ et entretenir la disponibilité pendant la commercialisation. Le nom Replenishment Decision est conservé. L’accord ne valide pas les équivalences marché, les nouveaux exemples, les fonctions ou toutes les relations détaillées ajoutées lors de l’intégration. Backlog autorisé ; aucune release demandée.''')
    m = read(ROOT/'modeles/backlog/model.yaml')
    before = deepcopy(m)
    nodes = {n['id']: n for n in m['nodes']}
    assert 'D05.g' not in nodes
    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    refs = ['U310', 'U313', 'U315', 'U316', 'CMP107', 'CMP108']

    def cycle(values, fields, note):
        return dict(state='urbanist_validated' if fields else 'under_instruction', recorded_at=now,
                    recorded_by='Codex', source_refs=['U313', 'U316'], validated_fields=fields,
                    value_sha256={f: value_hash(values[f]) for f in fields}, note=note)

    def touch(n):
        n['revision'] += 1
        n['source_refs'] = list(dict.fromkeys(n['source_refs'] + ['U313', 'U316']))
        n['editorial_basis'] = n.get('editorial_basis', '') + ' U316 : distinction implantation/réassort intégrée ; compléments éditoriaux proposés. État antérieur : audits/2026-09-18-initial-stocking/model-before.yaml.'

    g = read(ROOT/'modeles/backlog/glossary.yaml')
    terms = {t['id']: t for t in g['terms']}
    position = 'Initial Stocking Decision est le nom FLOW adopté U316 pour l’implantation ; Replenishment Decision reste distincte pour les apports continus. Initial Stocking est attesté dans UBL, Initial Distribution dans les sources retail. Les intitulés éditeurs sont conservés pour comparaison, sans équivalence de hiérarchie ni déploiement Beaumanoir déduit. Les rapprochements restent proposés.'
    initial_comparisons = deepcopy(terms['TER079']['market_comparisons'])
    for c in initial_comparisons:
        c['flow_position'] = position
        c['source_refs'] = list(dict.fromkeys(c['source_refs'] + ['U316']))
    definition = 'Déterminer les quantités à apporter à chaque magasin et leurs dates pour constituer le stock initial nécessaire au lancement, à partir de l’assortiment retenu, des objectifs de stock et des contraintes applicables.'
    initial = dict(id='D05.g', revision=1, kind='capability', layer='transactional', fields=dict(
        name='Initial Stocking Decision', definition=definition, nature='decision',
        finality='Préparer la disponibilité initiale des produits en magasin, en maîtrisant l’immobilisation et le risque dès le lancement.',
        scope='''Décider les apports d’[implantation](glossary:TER079) destinés à constituer le stock de départ de chaque magasin à la date de lancement. Chez Beaumanoir, les deux saisons été/hiver constituent le contexte rapporté ; collections, capsules ou périodes plus fines sont des extensions possibles, pas des pratiques actuelles déduites. Le résultat précise produits ou variantes, magasins, quantités, dates et éventuels besoins non couverts.

L’assortiment retenu, les objectifs de stock et les contraintes constituent les entrées. [Coverage Target Decision](model:D05.a) conserve la détermination des cibles ; cette décision détermine les apports pour les atteindre au lancement. Examiner stock déjà présent et admissible, apports attendus à temps, conditionnements, protections et contraintes de disponibilité. Le calcul net fait partie de la décision ; ne pas compter deux fois les mêmes entrées.

Exemple fictif : pour un lancement au 1er mars, une cible de 100 pièces, 20 pièces admissibles déjà présentes et 30 attendues à temps laissent 50 pièces à apporter. Si seulement 40 peuvent être disponibles, expliciter le manque de 10 et les options à examiner ; ne pas annoncer implicitement une promesse ni modifier la cible sans mobiliser la décision responsable. Les tailles, couleurs et conditionnements peuvent contraindre le résultat sans constituer automatiquement des comportements supplémentaires.

La finalité distingue l’implantation du [réassort continu](model:D05.e). Un complément tardif destiné à achever la mise en place initiale reste à qualifier selon cette finalité ; la date seule ne suffit pas à le transformer en réassort. Les apports d’implantation engagés restent visibles pour les décisions ultérieures de réassort, afin d’éviter les doublons.

[Inventory Planning](model:D05.f) mobilise la décision pour ses scénarios. D04 gère les Orders nécessaires, D03 décide comment les satisfaire et D06 pilote les prestations ; retenir ces apports ne réalise ni livraison ni mise en rayon. [Supply Assignment](model:D02.e) conserve l’affectation des ressources aux commandes. Le choix de l’assortiment et la planification commerciale de saison ne deviennent pas des responsabilités de cette capacité.''',
        market_comparisons=initial_comparisons), source_refs=refs,
        source_locator={'path':'connaissance/01-contributions-utilisateur.md','anchor':'u316'},
        review={'state':'partial','note':'Nom et définition présentés adoptés U316. Finalité, nature formalisée, périmètre détaillé, exemple et correspondances marché restent éditoriaux.'},
        adoption_ids=[], editorial_basis='Séparation U313 et nom/définition U316 ; détails éditoriaux et relations proposés, sans nouvelle décomposition en comportements.')
    initial['lifecycle'] = cycle(initial['fields'], ['name','definition'], initial['review']['note'])
    m['nodes'].insert(m['nodes'].index(nodes['D05.e']), initial)

    repl = nodes['D05.e']; touch(repl)
    repl['fields']['definition'] = 'Déterminer les apports successifs et leurs ajustements en quantité et en date pour entretenir la disponibilité pendant la commercialisation, selon les besoins, les objectifs de stock, les apports engagés et les contraintes applicables.'
    repl['fields']['finality'] = 'Entretenir la disponibilité en ajustant les apports continus, tout en maîtrisant l’immobilisation et le risque d’excédent.'
    repl['fields']['scope'] = '''Décider les apports de [réassort](glossary:TER080) après la constitution du stock de départ. Chez Beaumanoir, l’alimentation continue des magasins est guidée par des seuils ; la cadence de révision, les formules et le degré d’automatisation ne sont pas imposés par ce constat. Le réapprovisionnement continu peut aussi concerner les stocks du réseau et les compléments fournisseur déjà couverts par cette capacité.

Évaluer les besoins nets selon les cibles, le stock admissible, les entrées attendues, les contraintes et les actions déjà engagées. [Coverage Target Decision](model:D05.a) conserve la détermination des objectifs et seuils. Une décision intègre les calculs nécessaires : aucune capacité Calculation autonome. Préciser l’horizon, la maille et les règles d’admissibilité, sans déduire deux fois des demandes déjà intégrées à la cible.

Exemple fictif : au point de revue, le stock projeté est de 50 pièces, sous un seuil de 60 ; avec une cible de 100 et en l’absence d’autres besoins ou restrictions, proposer un apport de 50. Si le conditionnement impose des multiples de 12, examiner un apport de 60 et l’excédent associé. Seuil et cible sont distincts ; cet exemple n’adopte pas une formule Min/Max universelle.

[Initial Stocking Decision](model:D05.g) décide les apports de lancement. Le réassort tient compte des apports d’implantation encore attendus, sans les recréer. [Stock Redistribution Decision](model:D05.c) examine séparément le rééquilibrage du stock existant ; coordonner les résultats pour ne pas couvrir deux fois le même manque. Un transfert peut matérialiser un apport courant ou une redistribution selon sa finalité.

Réviser les apports encore modifiables lorsque le besoin évolue : augmenter, réduire, reporter ou proposer une annulation. Exemple fictif : 30 pièces présentes et 80 attendues pour une cible de 100 conduisent à examiner une réduction ou un report de 10. Si les engagements empêchent la modification, conserver l’excédent résiduel et les options restantes.

Les résultats précisent les quantités, dates et ajustements recommandés ; [Order Management](model:D04) vérifie et applique les changements autorisés aux Orders. [Order Promising](model:D03) décide de leur satisfaction et D06 pilote l’exécution. Une recommandation ne crée pas à elle seule une promesse, une modification d’Order ferme ou un mouvement physique. Le déclenchement peut être automatisé selon les règles et autorités ; son porteur opérationnel détaillé reste à instruire.'''
    for c in repl['fields']['market_comparisons']:
        c['element_name'] = 'In-Season Fill-In' if c['vendor']=='SAP' else 'In-season replenishment'
        c['similarities'] = 'Réapprovisionnement après les premières ventes ou pendant la commercialisation, distinct de la mise en place initiale. Appui au réassort continu demandé U313.'
        c['flow_position'] = position
        c['source_refs'] = list(dict.fromkeys(c['source_refs']+['U316']))
    repl['review']['note'] = 'Nom conservé et séparation du réassort continu adoptée U313/U316. Nouvelle définition détaillée, périmètre et exemples éditoriaux proposés ; ancienne valeur conservée dans la capture U316.'
    repl['lifecycle']['note'] = repl['review']['note']
    repl['lifecycle']['source_refs'].append('U316')

    domain = nodes['D05']; touch(domain)
    domain['fields']['scope'] = domain['fields']['scope'].replace('Quatre décisions spécialisées portent respectivement les cibles de couverture, les droits de protection des groupes, les apports de réapprovisionnement et la redistribution du stock existant.', 'Les décisions spécialisées portent les cibles de couverture, les droits de protection des groupes, les apports initiaux de lancement, le réassort continu et la redistribution du stock existant.')
    domain['fields']['scope'] = domain['fields']['scope'].replace('[Replenishment Decision](model:D05.e) intègre notamment les besoins nets, les contraintes, les quantités et dates à retenir.', '[Initial Stocking Decision](model:D05.g) détermine les apports du lancement ; [Replenishment Decision](model:D05.e) détermine les apports continus. Chacune intègre les besoins nets, contraintes, quantités et dates utiles à sa finalité.')
    planning = nodes['D05.f']; touch(planning)
    planning['fields']['scope'] = planning['fields']['scope'].replace('Group Protection Decision, Replenishment Decision', 'Group Protection Decision, Initial Stocking Decision, Replenishment Decision')

    def relation(identifier, source, target, meaning=None, conditions=None):
        r = dict(id=identifier, revision=1, type='relates-to' if meaning else 'contains', source_id=source,
                 target_id=target, source_refs=['U313','U316'], review={'state':'proposed','note':'Rattachement ou contrat formalisé lors de l’intégration U316 ; non présenté dans le détail lors de l’accord.'})
        if meaning:
            r['qualification'] = dict(role='needs', meaning=meaning,
                conditions=conditions or ['Lorsque nécessaire au scénario ; pas de séquence ni d’appel technique systématique.'],
                effects=['Consommer le résultat sans transférer la responsabilité métier de la capacité fournisseur.'])
        r['lifecycle'] = cycle(r, [], r['review']['note'])
        m['relations'].append(r)
    relation('REL-MEMBER-D05.g','D05','D05.g')
    relation('REL-INVENTORY-PLANNING-D05.g','D05.f','D05.g','A besoin des quantités et dates d’implantation pour construire et simuler un scénario comprenant un lancement.')
    for suffix,target,meaning in [
        ('INVENTORY','D01.c','A besoin des quantités et états de stock admissibles par magasin, avec provenance et fraîcheur.'),
        ('TARGET','D05.a','A besoin des objectifs de stock au lancement, proposés ou retenus, pour déterminer les apports initiaux.'),
        ('PROTECTION','D02.b','A besoin des protections et droits d’usage applicables au périmètre et à la période du lancement.'),
        ('PURCHASE','D04.j','A besoin des apports fournisseur engagés, de leurs dates et de leurs possibilités de modification lorsque ces achats contribuent au lancement.'),
        ('TRANSFER','D04.k','A besoin des transferts engagés et de leurs dates pour éviter de demander deux fois les mêmes apports initiaux.'),
        ('TRACKING','D07.d','A besoin de l’avancement et des estimations des prestations engagées pour apprécier si les apports arriveront à temps pour le lancement.')]:
        relation('REL-INITIAL-STOCKING-'+suffix,'D05.g',target,meaning)
    relation('REL-REDISTRIBUTION-INITIAL-STOCKING','D05.c','D05.g','A besoin des apports initiaux recommandés lorsqu’un rééquilibrage peut couvrir les mêmes manques ; coordonner les résultats sans double comptage.')

    for tid in ['TER079','TER080']:
        t=terms[tid]
        t['source_refs']=list(dict.fromkeys(t['source_refs']+['U316']))
        for c in t['market_comparisons']:
            c['flow_position']=position
            c['source_refs']=list(dict.fromkeys(c['source_refs']+['U316']))
    terms['TER079']['notes'] += '\n\nU316 : Initial Stocking est le terme anglais adopté pour l’implantation. [Initial Stocking Decision](model:D05.g) porte la décision ; [Replenishment Decision](model:D05.e) reste distincte pour le réassort continu. Initial Distribution est une alternative de marché documentée, pas le nom retenu.'
    terms['TER079']['review']['note'] += ' U316 adopte le terme anglais Initial Stocking et le nom/définition de la capacité associée ; les correspondances restent proposées.'
    terms['TER074']['notes'] += '\n\nU313/U316 : dans le contexte retail discuté, distinguer le réassort continu de l’[implantation](glossary:TER079), dont les apports sont décidés par [Initial Stocking Decision](model:D05.g). Un produit couvrant les deux ne fusionne pas ces responsabilités.'
    terms['TER074']['source_refs']+=['U313','U316']
    (ROOT/'modeles/backlog/model.yaml').write_text(dumps(m),encoding='utf-8')
    (ROOT/'modeles/backlog/glossary.yaml').write_text(dumps(g),encoding='utf-8')

    delta = {}
    for collection in ['nodes','relations']:
        old={x['id']:x for x in before[collection]}; new={x['id']:x for x in m[collection]}
        delta[collection] = dict(added={i:value_hash(new[i]) for i in new.keys()-old.keys()},
            changed={i:value_hash(new[i]) for i in old.keys()&new.keys() if new[i]!=old[i]}, removed=sorted(old.keys()-new.keys()))
    registry=dict(source_refs=['U313','U316'], state='applied_in_backlog',
        model_before='audits/2026-09-18-initial-stocking/model-before.yaml',
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),
        model_after_sha256=sha256((ROOT/'modeles/backlog/model.yaml').read_bytes()).hexdigest(),delta=delta,
        adopted_node={'id':'D05.g','validated_fields':['name','definition'],'value_sha256':initial['lifecycle']['value_sha256']},
        preserved_identity='D05.e conservée pour Replenishment Decision ; D05.b retirée reste inutilisée.',
        proposed_details='Finalités, détails éditoriaux, exemples, rattachement et contrats détaillés non validés automatiquement ; correspondances marché proposées.',
        no_new_behaviors='Aucun mécanisme différenciant supplémentaire justifié par le seul découpage ; pas de décomposition systématique.',
        open_boundary='Préciser les contraintes et les échanges Coverage Target / Initial Stocking sans déplacer implicitement la détermination des objectifs.')
    annex=read(ROOT/'modeles/backlog/d05-refactoring.yaml')
    annex['initial_stocking_U316']=registry
    (ROOT/'modeles/backlog/d05-refactoring.yaml').write_text(dumps(annex),encoding='utf-8')
    a=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    a['implementation_U316']=registry
    a['baseline'].update(sha256=registry['model_after_sha256'],nodes=len(m['nodes']),capabilities=sum(n['kind']=='capability' for n in m['nodes']),relations=len(m['relations']))
    old_assessment=next(x for x in a['assessments'] if x['capability_id']=='D05.e')
    old_assessment.update(verdict='réexaminer les mécanismes après séparation',diagnosis='U313/U316 séparent implantation et réassort ; D05.e conserve les apports continus, D05.g porte le lancement.',recommendation='P01/P02/P03 restent des pistes à réexaminer, pas des comportements adoptés. Le calcul net, les seuils et les ajustements ne justifient pas automatiquement une décomposition. Examiner les bénéfices dans le périmètre du réassort continu.')
    a['assessments'].append(dict(capability_id='D05.g',name='Initial Stocking Decision',existing_behaviors=[],verdict='ne pas décomposer systématiquement',diagnosis='Décision distincte adoptée U316 pour les apports du lancement ; aucun comportement supplémentaire adopté.',recommendation='Éprouver le périmètre avec cibles, apports déjà engagés et ressources contraintes avant de proposer des mécanismes différenciants. Ne pas transformer quantités, dates, tailles ou conditionnements en comportements.',market_sources=['S51','S52'],candidate_ids=[]))
    a['feedback_U315']['superseded_by']='Nom et définition adoptés U316 ; catalogue mis à jour.'
    (ROOT/'modeles/backlog/behavior-gap-audit.yaml').write_text(dumps(a),encoding='utf-8')
    (OUT/'implementation.yaml').write_text(dumps(registry),encoding='utf-8')
    append('marche/comparaisons.md','''Complément U316 à CMP108 — 18 septembre 2026 : Initial Stocking / Initial Stocking Decision et la définition présentée sont adoptés. D05.g créée dans le backlog, D05.e conservée pour le réassort continu. Les rapprochements documentaires avec OASIS, Logility, Nextail, SAP et RELEX restent proposés ; aucune équivalence normative ni réalisation installée validée. Les comparaisons de D05.e sont recentrées sur In-Season Fill-In / In-season replenishment ; celles de l’implantation sont portées par D05.g et TER079.''')
    append('JOURNAL.md','''### 2026-09-18 — U316, décision d’implantation

Initial Stocking Decision (D05.g) ajoutée au backlog avec nom et définition adoptés. Replenishment Decision (D05.e) conserve le réassort continu. Domaine, Planning, glossaire, comparaisons marché et audit actualisés. Relations et compléments éditoriaux restent proposés ; aucune nouvelle décomposition en comportements. Capture et portée : audits/2026-09-18-initial-stocking/. Aucune release ni publication distante.''')
    print(json.dumps(delta,ensure_ascii=False))


if __name__=='__main__':
    main()
