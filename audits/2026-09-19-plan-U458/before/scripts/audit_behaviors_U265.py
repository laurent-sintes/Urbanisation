"""One-off, reviewable consolidation for U265/U266; no publication."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-17-audit-comportements'

def append(path, text):
    with (ROOT / path).open('ab') as stream:
        stream.write(('\r\n\r\n' + text.strip() + '\r\n').replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8'))

def main():
    OUT.mkdir(exist_ok=True)
    if (OUT / 'before.json').exists():
        raise SystemExit('Capture already exists; do not repeat the mutation.')
    protected = {}
    for folder in ('release', 'revisions', 'decisions', 'provenance'):
        for p in (ROOT / 'modeles' / folder).rglob('*'):
            if p.is_file() and p.name != 'source-records.json' or (p.is_file() and p.parent.name != 'provenance'):
                protected[p.relative_to(ROOT).as_posix()] = sha256(p.read_bytes()).hexdigest()
    # Explicitly include frozen source-records, exclude only the live index.
    protected.pop('modeles/provenance/source-records.json', None)
    for source, target in [('AGENTS.md', 'AGENTS-before.md'), ('modeles/backlog/model.yaml', 'model-before.yaml')]:
        (OUT / target).write_bytes((ROOT / source).read_bytes())
    (OUT / 'before.json').write_text(json.dumps({'protected': protected}, indent=2), encoding='utf-8')
    contributions = [
        ('U265', 'Audit de granularité avec comportements et simplification des instructions', '''On a délibérément mis un niveau de granularité haut pour les capacités d'action (management, planning etc.). Mais maintenant on va pouvoir décrire plus précisément les comportements attendus : simulation, traitement en masse etc.

Je souhaite que tu fasses un audit du modèle et que tu le compares avec le marché. Je pense que le marché qui décrit un modèle sur plusieurs niveaux n'a pas rendu facile l'alignement jusqu'à aujourd'hui.

Refais une passe sur agents.md et le modèle pour simplifier, éviter les doublons et reprioriser les instructions.

Concernant l'audit du modèle :
Je veux savoir si l'ajout de ce niveau est suffisant (j'espère que oui).
Je veux savoir comment refactorer le modèle actuel en passant des capacité en comportement ou en les décomposant.

P.S. : Il faut que la décomposition en comportement soit justifiée par une complexité ou un bénéfice ciblé => cette notion est en enregistrer dans le modèle.''', 'Audit et simplification autorisés. Exigence adoptée : justifier la décomposition par une complexité ou un bénéfice ciblé. Aucun regroupement, changement de nature ou nouveau comportement particulier validé par cette demande.'),
        ('U266', 'Plan séparant corrections autonomes et arbitrages conjoints', '''Si tu peux prévoir un plan d'actions à présenter coupé en deux :
1- ce que tu peux prendre en compte de manière automatique qui améliore sans risque le modèle
2- ce qui demande un travail conjoint entre toi et moi et de la validation''', 'Distinguer les améliorations sans arbitrage métier et les propositions à instruire avec Laurent. Ne pas déduire une validation de refonte du catalogue.')]
    for identifier, title, verbatim, scope in contributions:
        append('connaissance/01-contributions-utilisateur.md', f'## {identifier}\n\n**id**\n\n{identifier}\n\n**date**\n\n2026-09-17\n\n**titre**\n\n{title}\n\n**texte**\n\n{verbatim}\n\n**contexte et portée**\n\n{scope}')
    model = read(ROOT / 'modeles/backlog/model.yaml')
    model['principles'].append({
        'id': 'PRINCIPLE-JUSTIFIED-BEHAVIOR',
        'statement': 'Une décomposition en comportements doit être justifiée par une complexité ou un bénéfice ciblé. Conserver une granularité haute pour les capacités d’action ; simulation et traitement en masse peuvent préciser leurs comportements attendus.',
        'source_refs': ['U265']})
    atp = next(n for n in model['nodes'] if n['id'] == 'D03.i')
    atp['fields']['decomposition_rationale'] = 'Complexité : distinguer les engagements concurrents, les lieux admissibles, le délai réel de mobilisation et les apports futurs, qui peuvent se combiner. Bénéfice ciblé : expliquer pourquoi un stock enregistré ne garantit pas une promesse immédiate et pourquoi un arrivage à J+7 peut couvrir une échéance à J+60, sans créer quatre capacités ni un niveau marketing.'
    atp['source_refs'].append('U265')
    atp['review']['note'] += ' U265 : justification éditoriale de décomposition proposée ; aucune extension des champs adoptés.'
    corrected = []
    for node in model['nodes']:
        if node['id'] not in ['D04.i','D04.j','D04.k','D04.l','D04.m','D05.c']:
            continue
        original = node['fields'].get('scope', '')
        updated = original.replace('dans D07 et le contexte Services', 'dans [Execution Management](model:D06) et chez les exécutants').replace('prestations suivies par D07', 'prestations suivies par [Execution Management](model:D06)')
        if updated != original:
            assert 'scope' not in node.get('lifecycle', {}).get('validated_fields', []), node['id']
            node['fields']['scope'] = updated
            corrected.append(node['id'])
    (ROOT / 'modeles/backlog/model.yaml').write_text(dumps(model), encoding='utf-8')
    glossary = read(ROOT / 'modeles/backlog/modeling-glossary.yaml')
    term = next(t for t in glossary['terms'] if t['id'] == 'MOD006')
    term['notes'].append('U265 : une décomposition en comportements est justifiée par une complexité ou un bénéfice ciblé ; elle n’est pas systématique. La justification est portée par fields.decomposition_rationale sur la capacité ; sa rédaction détaillée conserve sa propre portée de validation.')
    term['source_refs'].append('U265')
    term['review']['adopted_scope'] += ' U265 : exigence de justification par une complexité ou un bénéfice ciblé.'
    (ROOT / 'modeles/backlog/modeling-glossary.yaml').write_text(dumps(glossary), encoding='utf-8')
    schema_path = ROOT / 'modeles/schemas/urbanism.schema.json'
    schema = read(schema_path)
    schema['$defs']['node']['properties']['fields']['properties']['decomposition_rationale'] = {'type': 'string'}
    schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (OUT / 'automatic-changes.json').write_text(json.dumps({'source_refs':['U265','U266'], 'corrected_obsolete_domain_references': corrected, 'unchanged_capacity_count':41, 'unchanged_behavior_count':4, 'adopted_rule':'Complexité OU bénéfice ciblé', 'proposed_rationale_on':'D03.i'}, ensure_ascii=False, indent=2), encoding='utf-8')
    print('U265/U266 recorded; model principle, ATP rationale and six obsolete references updated.')

if __name__ == '__main__': main()
