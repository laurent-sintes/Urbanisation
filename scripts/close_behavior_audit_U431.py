"""Close the existing behavior audit without changing the capability catalogue."""
from pathlib import Path
from hashlib import sha256
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / 'modeles/backlog/history/behavior-audit-closure-U431'


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as stream:
        stream.write('\n\n' + text + '\n')


def save(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8')


def main():
    assert not HISTORY.exists()
    audit_path = 'modeles/backlog/behavior-gap-audit.yaml'
    return_path = 'modeles/backlog/customer-return-behaviors.yaml'
    model_path = ROOT / 'modeles/backlog/model.yaml'
    original_model = model_path.read_bytes()
    audit = read(ROOT / audit_path)
    assert 'closure_U431' not in audit
    assert '## U431\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U431

**id**

U431

**date**

2026-09-19

**titre**

Solder l’audit des comportements

**texte**

On solde.

**contexte et portée**

Accord sur la proposition de clôture présentée : P04, P10 et P12 sont couverts par le modèle actuel, sans création de comportement ; consolider la frontière commerciale/financière externe à Supply. Les règles de réservation, d’application des plans et de capacité engageable restent des travaux ultérieurs non bloquants pour le catalogue. Ne vaut ni validation globale des descriptions, contrats et comparaisons, ni exhaustivité de couverture du marché, ni publication. Aucun arbitrage organisationnel Commerce/Finance supplémentaire déduit de cet accord.''')
    HISTORY.mkdir()
    for path, name in [(audit_path, 'audit-before.yaml'), (return_path, 'returns-before.yaml'), ('AGENTS.md', 'AGENTS-before.md')]:
        (HISTORY / name).write_bytes((ROOT / path).read_bytes())
    coverage = {
        'P04': ('D06.d', 'La coordination des prestations et de leurs dépendances appartient à la définition de Process Orchestration. Aucun mécanisme distinct justifiant un comportement supplémentaire.'),
        'P10': ('D07.d', 'Operations Tracking et ses quatre comportements rendent visibles progression, écarts, attentes et échecs physiques ou numériques. La détection transverse des exceptions ne justifie pas un doublon.'),
        'P12': ('D05.a', 'Inventory Target Decision détermine déjà objectifs et seuils selon besoins, service, délais et risques. Ses comportements magasin, centre de distribution et multi-échelon intègrent ces critères ; aucun bénéfice distinct établi pour le candidat.')
    }
    for candidate in audit['candidates']:
        if candidate['id'] in coverage:
            parent, reason = coverage[candidate['id']]
            candidate.update(status='covered_by_existing_U431', covered_by=parent, review_note='U431 : clôture adoptée. ' + reason + ' La fiche initiale ci-dessous reste historique.')
            candidate['source_refs'] = list(dict.fromkeys(candidate.get('source_refs', []) + ['U431']))
    for assessment in audit['assessments']:
        for candidate, (parent, reason) in coverage.items():
            if assessment['capability_id'] == parent:
                assessment.update(verdict='couverture existante confirmée U431', recommendation=reason + ' Candidat ' + candidate + ' clos sans ajout.')
    synthesis = audit['current_synthesis_U298']
    for key in ['retained_candidate_ids', 'conditional_candidate_ids', 'reassess_candidate_ids']:
        synthesis[key] = [i for i in synthesis[key] if i not in coverage]
        assert not synthesis[key]
    synthesis['covered_candidate_ids'] = list(dict.fromkeys(synthesis.get('covered_candidate_ids', []) + list(coverage)))
    synthesis['conclusion'] = 'Audit des comportements clos U431 au périmètre du catalogue. Tous les candidats sont intégrés, couverts par l’existant ou retirés.'
    synthesis['retained_scope'] = 'Aucun candidat restant à arbitrer ; P04/P10/P12 couverts sans nouveau comportement.'
    synthesis['next_step'] = 'Aucune poursuite automatique de cet audit. Les règles de gestion, contrats et améliorations futures restent séparés ; publication sur demande.'
    synthesis['source_refs'] = list(dict.fromkeys(synthesis['source_refs'] + ['U431']))
    followups = []
    for arbitration in audit['arbitrations']:
        arbitration['catalogue_status_U431'] = 'closed'
        arbitration['closure_source_refs'] = ['U431']
        if arbitration['id'] in ['A01', 'A03', 'A07']:
            arbitration['status'] = 'catalogue_closed_details_deferred_U431'
            followups.append(dict(arbitration_id=arbitration['id'], subject=arbitration['title'], remaining=arbitration['question'], status='deferred_nonblocking', validation_scope='Règles et contrats à instruire ; aucune réponse détaillée adoptée par la clôture.'))
        if arbitration['id'] == 'A04':
            arbitration['status'] = 'catalogue_boundary_closed_U431'
            arbitration['recommendation'] = 'D05.i choisit le devenir du bien ; Customer Return porte les parcours de retour ; D04 prend en charge les demandes liées, D06 les prestations et D01 les stocks. Responsabilités commerciales et financières externes à Supply ; aucune capacité manquante ajoutée pour facturer ou encaisser.'
            arbitration['limit'] = 'Exclusion Supply acquise U429 et clôture U431. Attribution externe Commerce/Finance et détails des interactions restent séparés ; les propositions CMP165/CMP166 ne sont pas validées en bloc. Aucun constat d’exhaustivité des filières.'
            followups.append(dict(arbitration_id='A04', subject='Interfaces commerciales et financières', remaining='Préciser les autorisations, résultats et conditions échangés, ainsi que le rattachement externe si nécessaire.', status='deferred_nonblocking', validation_scope='Hors arbitrage du catalogue Supply ; aucune capacité externe créée.'))
    closure = dict(status='closed', date='2026-09-19', source_refs=['U431', 'U429'], model_sha256=sha256(original_model).hexdigest(), audit_before='modeles/backlog/history/behavior-audit-closure-U431/audit-before.yaml', audit_before_sha256=sha256((HISTORY / 'audit-before.yaml').read_bytes()).hexdigest(), covered_candidates=[dict(candidate_id=k, capability_id=v[0], rationale=v[1]) for k, v in coverage.items()], future_work=followups, scope='Clôture du catalogue de capacités et comportements de l’audit existant ; aucun changement de catalogue.', limits='Ne valide pas globalement les champs éditoriaux, contrats, règles ou comparaisons ; ne prouve ni complétude du marché ni couverture installée ; aucune release.')
    audit['closure_U431'] = closure
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + ['U431']))
    save(audit_path, audit)
    save('modeles/backlog/history/behavior-audit-closure-U431/closure.yaml', closure)
    returns = read(ROOT / return_path)
    returns['audit_closure_U431'] = dict(source_refs=['U429', 'U431'], status='supply_boundary_closed', scope='Suites commerciales et financières hors univers Supply ; contrats d’interface et rattachement externe non bloquants pour le catalogue.', limits='Les variantes et comparaisons historiques gardent leur portée ; aucun comportement financier ou réception physique fictive ajouté.')
    for pattern in returns.get('additional_market_patterns', []):
        if pattern['name'] in ['Customer replacement', 'Returnless resolution']:
            pattern['status'] = 'catalogue_boundary_closed_U431'
            pattern['closure_note'] = 'Frontière Supply close ; détails du contrat avec les responsabilités externes à instruire séparément. Ne vaut pas adoption de toute la description initiale.'
    returns['source_refs'] = list(dict.fromkeys(returns.get('source_refs', []) + ['U431']))
    save(return_path, returns)
    append('AGENTS.md', '## Clôture de l’audit des comportements — U431\n\nL’audit `modeles/backlog/behavior-gap-audit.yaml` est clos au périmètre du catalogue. P04/P10/P12 sont couverts par Process Orchestration, Operations Tracking et Inventory Target Decision ; ne pas les réouvrir depuis leurs anciennes fiches. La frontière commerciale et financière est externe à Supply. Les règles de gestion et contrats restant à préciser sont conservés dans `closure_U431.future_work`, sans bloquer le catalogue ni déclencher une nouvelle étude. Clôture ne vaut pas validation globale des descriptions, comparaisons ou réalisation installée. Les règles U398/U399 restent applicables aux prochaines améliorations ; aucune reprise automatique.')
    append('JOURNAL.md', '## 2026-09-19 — U431 : clôture de l’audit des comportements\n\nTrois candidats clos comme couverts par l’existant, frontière externe consolidée et règles/contrats différés identifiés. Aucun changement du catalogue : 47 capacités et 74 comportements. Accords et versions historiques préservés ; aucune release.')
    assert model_path.read_bytes() == original_model
    print('U431: audit closed; P04/P10/P12 covered; catalogue unchanged.')


if __name__ == '__main__':
    main()
