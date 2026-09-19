"""Correctifs éditoriaux préparés U435 ; aucune modification sans --apply.

Ne modifie aucun champ validé par lifecycle, aucun nom, parent ou catalogue.
L'alternative active U158 est retirée seulement après contrôle de sa sauvegarde.
Utilisation par l'agent coordinateur, après création du snapshot original :
  python audits/2026-09-19-audit-profond-v0/apply_coherence_fixes.py --apply
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps

AUDIT = Path(__file__).resolve().parent
MODEL = ROOT / 'modeles/backlog/model.yaml'
METHOD = ROOT / 'modeles/backlog/modeling-glossary.yaml'
SNAPSHOT = AUDIT / 'model-before-U435.yaml'
BASELINE_SHA256 = '2fcc8262e753400ad74d518c7159a3f7ba06487247e4b3b923d059e58d01b1f2'


def protected_values(model):
    result = {}
    for collection in ('nodes', 'relations'):
        for item in model[collection]:
            ident = item['id']
            result[(collection, ident, 'lifecycle')] = deepcopy(item.get('lifecycle'))
            for field in item.get('lifecycle', {}).get('validated_fields', []):
                value = item.get('fields', {}).get(field, item.get(field))
                result[(collection, ident, field)] = deepcopy(value)
    return result


def prepare(model, method):
    original = deepcopy(model)
    old_method = deepcopy(method)
    nodes = {n['id']: n for n in model['nodes']}
    changed_nodes = set()
    change_reasons = {}

    def replace(ident, field, old, new, reason):
        node = nodes[ident]
        if field in node.get('lifecycle', {}).get('validated_fields', []):
            raise ValueError(f'Champ validé protégé : {ident}.{field}')
        target = node['fields'] if field in node['fields'] else node
        current = target[field]
        if old not in current:
            if new in current:
                return
            raise ValueError(f'Précondition absente : {ident}.{field}: {old}')
        target[field] = current.replace(old, new)
        changed_nodes.add(ident)
        change_reasons.setdefault((ident, field), []).append(reason)

    for ident in ('D01', 'D04.i', 'D04.k', 'D05', 'D05.c'):
        replace(ident, 'scope', 'Order Promising', 'Order Backlog Management',
                'U413 : nom et mandat courants de D03 ; renommage des seules références internes actives.')
    replace('D01', 'definition', 'Order Promising', 'Order Backlog Management',
            'U413 : nom courant de D03 ; définition D01 non comprise dans lifecycle.validated_fields.')

    for ident in ('BHV045', 'BHV046', 'BHV047'):
        replace(ident, 'scope',
                'Modifier le contenu, l’état ou la structure d’un Order mobilise les responsabilités D04 ; D06 conserve l’exécution.',
                'Modifier le contenu ou l’état d’un Order mobilise les responsabilités D04 ; modifier sa structure mobilise Order Structuring dans D03. D06 conserve l’exécution.',
                'U417/U420 : Structuring appartient à D03 ; Lifecycle et intentions restent D04.')

    replace('D02.e', 'scope',
            'La décision collective et les contrats d’engagement restent à préciser dans A01/A02.',
            'La décision collective relève de [Fulfillment Plan Decision](model:D03.o), intégrée U378. Les contrats détaillés d’engagement et d’application restent à préciser selon les travaux A01, A03 et A07 conservés à la clôture U431.',
            'U378 : Fulfillment Plan Decision intégrée ; U431 préserve les contrats restant à instruire.')

    stale = 'Intercompany est un axe de relation commerciale ; les autres parcours décrivent principalement le mode de satisfaction.'
    for ident in ('D01.h', 'BHV063', 'BHV064', 'BHV065'):
        replace(ident, 'scope', stale,
                'Les comportements distinguent le transfert de propriété à la consommation, le transfert à une échéance contractuelle et la sortie autorisée de la consignation ou de la détention.',
                'U401 : critères déjà adoptés des trois comportements de consignation ; phrase de vente hors contexte retirée.')
    for ident in ('D04.k', 'BHV070', 'BHV071', 'BHV072', 'BHV073', 'BHV074'):
        replace(ident, 'scope', stale,
                'Les comportements distinguent les intentions du transfert : constituer le stock initial, l’alimenter pendant l’activité, rééquilibrer les lieux, regrouper des stocks dispersés ou satisfaire une commande identifiée.',
                'U401 : cinq intentions de transfert déjà présentes ; phrase de vente hors contexte retirée.')

    replace('BHV060', 'scope',
            'Extension explicite de la définition actuelle centrée sur les biens.',
            'Purchase Order couvre les biens et les prestations depuis U391.',
            'U391 : définition courante de Purchase Order inclut les prestations.')
    replace('D06.b', 'scope',
            'Service Decision et Adaptation Decision peuvent la mobiliser.',
            'Service Selection Decision et Process Adaptation Decision peuvent la mobiliser.',
            'U409 : noms courants des décisions ; responsabilités inchangées.')

    # Une note de revue n'élargit pas la validation des libellés/détails éditoriaux.
    old_review = nodes['D02.e']['review']['note']
    new_review = ('Intégration U290 ; principes d’application U345 et trois mécanismes sous Supply Assignment intégrés U364. '
                  'Noms et compléments éditoriaux conservent leurs portées propres ; aucune validation globale déduite. '
                  'U435 : références au placement de Structuring et à la décision collective actualisées.')
    if old_review != new_review:
        nodes['D02.e']['review']['note'] = new_review
        changed_nodes.add('D02.e')
        change_reasons[('D02.e', 'review.note')] = ['U364/U378/U417/U420 : note active actualisée sans extension de validation.']

    # Le schéma ne permet que state=proposed : retirer de la liste active,
    # plutôt qu'inventer un état superseded ou modifier le schéma.
    alternative_id = 'D03-BACKLOG-DOMAIN-U158'
    removed = [a for a in model['alternatives'] if a['id'] == alternative_id]
    if len(removed) > 1:
        raise ValueError('Alternative dupliquée')
    model['alternatives'] = [a for a in model['alternatives'] if a['id'] != alternative_id]

    old_limitation = ('Refonte U290 appliquée au socle recommandé. Décompositions Stocktaking/Orchestration conditionnelles, '
                      'articulation réservation-affectation, rattachement du comportement transverse D04 et contrats détaillés '
                      'restent à instruire. Registre : modeles/backlog/refactoring-implementation.yaml.')
    new_limitation = ('Audit des comportements clos U431 au périmètre du catalogue. Stocktaking porte ses trois comportements '
                      'U334 ; Process Orchestration couvre P04 sans décomposition supplémentaire. Order Structuring et Order '
                      'Archiving appartiennent à D03 ; Order Lifecycle Management appartient à D04 selon U417/U420. Les contrats '
                      'détaillés et interfaces encore ouverts sont conservés dans modeles/backlog/behavior-gap-audit.yaml, '
                      'closure_U431.future_work ; la clôture ne valide pas globalement les formulations ni la réalisation installée.')
    if old_limitation in model['limitations']:
        model['limitations'][model['limitations'].index(old_limitation)] = new_limitation
    elif new_limitation not in model['limitations']:
        raise ValueError('Limitation historique attendue absente')

    for ident in changed_nodes:
        nodes[ident]['revision'] += 1
        if 'U435' not in nodes[ident]['source_refs']:
            nodes[ident]['source_refs'].append('U435')

    # MOD006 : exemples éditoriaux seulement ; définition et portée d'accord inchangées.
    term = next(t for t in method['terms'] if t['id'] == 'MOD006')
    note_changes = [
        ('U282 précise la maille recherchée sur Supply Protection : mécanismes métier de protection, plutôt que liste des opérations sur Allocation. Les opérations fonctionnelles restent matière de conception produit ; elles ne constituent pas un nouveau niveau inférieur dans le modèle. La nouvelle décomposition cible reste à proposer.',
         'U282 précise la maille recherchée sur Supply Protection : mécanismes métier de protection, plutôt que liste des opérations sur Allocation. Les opérations fonctionnelles restent matière de conception produit ; elles ne constituent pas un nouveau niveau inférieur dans le modèle. Les quatre mécanismes BHV017–020 ont été intégrés U290 ; la proposition antérieure reste historique.'),
        ('U389 : les exemples de scopes de visibilité proviennent des arbitrages U305/U308, distincts des 48 comportements intégrés. Leur mention méthodologique ne les intègre ni ne les publie.',
         'U389 a analysé les exemples de visibilité comme propositions distinctes du catalogue de l’époque. Depuis U406/U409, Operations Tracking porte Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking (BHV079–082). L’analyse U389 reste une photographie historique ; leur présence actuelle ne vaut pas publication ni validation globale des détails.')]
    for old, new in note_changes:
        if old in term['notes']:
            term['notes'][term['notes'].index(old)] = new
        elif new not in term['notes']:
            raise ValueError('Note MOD006 attendue absente')
    examples = {f['key']: f['examples'] for f in term['concrete_forms']}
    example_changes = [
        ('business_scope', 'Execution Tracking : Warehouse, Transportation et Store Visibility, arbitrés en annexe U305/U308 mais non intégrés comme nœuds dans le catalogue analysé.',
         'Operations Tracking : Warehouse Visibility, Transportation Visibility, Store Visibility et Process Tracking, intégrés comme comportements directs BHV079–082 (U406/U409).'),
        ('business_effect', 'Order Lifecycle Management : Drafting, Firming, Freezing, Release, Hold & Resume, Rescheduling, Cancellation, Closure, Splitting (BHV036–044).',
         'Order Lifecycle Management : Order Firming, Order Freezing, Order Preparation & Revision, Order Release, Order Hold & Resume et Order Termination (BHV036–040, BHV043 ; U424). Order Splitting BHV044 relève d’Order Structuring dans D03 (U417).')]
    for key, old, new in example_changes:
        if old in examples[key]:
            examples[key][examples[key].index(old)] = new
        elif new not in examples[key]:
            raise ValueError('Exemple MOD006 attendu absent')
    for owner in (term, method):
        for source in ('U290', 'U406', 'U409', 'U417', 'U424', 'U435'):
            if source not in owner['source_refs']:
                owner['source_refs'].append(source)
    method['as_of'] = '2026-09-19'

    if protected_values(original) != protected_values(model):
        raise ValueError('Un champ validé ou son lifecycle aurait changé')
    original_term = next(t for t in old_method['terms'] if t['id'] == 'MOD006')
    for field in ('definition', 'review', 'decomposition_rule'):
        if term[field] != original_term[field]:
            raise ValueError(f'MOD006.{field} protégé')

    changes = []
    old_nodes = {n['id']: n for n in original['nodes']}
    for ident in sorted(changed_nodes):
        for field in sorted(set(nodes[ident]['fields']) | set(old_nodes[ident]['fields'])):
            before = old_nodes[ident]['fields'].get(field)
            after = nodes[ident]['fields'].get(field)
            if before != after:
                changes.append({'target': ident, 'field': 'fields.' + field,
                                'before': before, 'after': after,
                                'justification': change_reasons.get((ident, field), [])})
        if nodes[ident]['review'] != old_nodes[ident]['review']:
            changes.append({'target': ident, 'field': 'review.note',
                            'before': old_nodes[ident]['review']['note'], 'after': nodes[ident]['review']['note'],
                            'justification': change_reasons.get((ident, 'review.note'), [])})
    if removed:
        changes.append({'target': alternative_id, 'field': 'alternatives', 'before': removed[0],
                        'after': 'Retirée des propositions actives ; valeur complète préservée dans model-before-U435.yaml.',
                        'justification': ['U413 : Order Backlog Management adopté ; historique U158 conservé.']})
    if original['limitations'] != model['limitations']:
        changes.append({'target': 'model', 'field': 'limitations', 'before': original['limitations'],
                        'after': model['limitations'], 'justification': ['U334/U417/U420/U431 : état courant.']})
    if original_term != term:
        for field in ('notes', 'concrete_forms'):
            changes.append({'target': 'MOD006', 'field': field, 'before': original_term[field],
                            'after': term[field], 'justification': ['Exemples éditoriaux actualisés U290/U406/U409/U417/U424.']})
    report = {'id': 'coherence-editorial-fixes-U435', 'status': 'prepared', 'source_refs': ['U435'],
              'model_before_sha256': sha256(MODEL.read_bytes()).hexdigest(),
              'changed_nodes': sorted(changed_nodes), 'changes': changes,
              'protected_fields_unchanged': True,
              'not_changed': [
                  'PRINCIPLE-SUPPLY-DOCUMENTS : contextualisation U100/U393/U394 à arbitrer séparément.',
                  'Noms, parents, définitions validées, natures manquantes, formulations de résultats et nouveaux comportements.',
                  'Applicabilité, preuve de déploiement, objets et domaines Business Services.',
                  'Contrats métier A01/A03/A04/A07 et décisions U436 : mise à jour distincte par le coordinateur.']}
    return model, method, report, removed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    model, method, report, removed = prepare(read(MODEL), read(METHOD))
    if args.apply:
        if not SNAPSHOT.is_file() or sha256(SNAPSHOT.read_bytes()).hexdigest() != BASELINE_SHA256:
            raise ValueError('Snapshot original model-before-U435.yaml requis, avec empreinte de l’audit initial.')
        archived = {a['id']: a for a in read(SNAPSHOT)['alternatives']}
        if any(archived.get(a['id']) != a for a in removed):
            raise ValueError('Alternative retirée non préservée à l’identique dans le snapshot')
        model_text, method_text = dumps(model), dumps(method)
        report['status'] = 'applied'
        report['model_after_sha256'] = sha256(model_text.encode('utf-8')).hexdigest()
        # Aucune écriture d'archive, publication ou preuve immuable.
        MODEL.write_text(model_text, encoding='utf-8', newline='')
        METHOD.write_text(method_text, encoding='utf-8', newline='')
        (AUDIT / 'coherence-changes-U435.yaml').write_text(dumps(report), encoding='utf-8', newline='')
        print(f"Appliqué : {len(report['changed_nodes'])} nœuds ; {len(report['changes'])} changements documentés.")
    else:
        print(dumps(report))


if __name__ == '__main__':
    main()
