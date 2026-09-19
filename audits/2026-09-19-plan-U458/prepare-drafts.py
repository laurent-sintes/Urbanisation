"""Prepare unpublished editorial material; never touch release snapshots or guide associations."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.structured_io import read, dumps, write_text_if_changed

root = Path(__file__).resolve().parents[2]
guide = read(root / 'modeles/modeling-guides/versions/2026-09-19.1.yaml')
guide['version'] = '2026-09-19.2'
guide['scope'] += ' Brouillon U458 pour une future publication ; aucune association au modèle publié courant.'
contributions = (root / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
for ref in ['U455', 'U456']:
    section = contributions.split(f'## {ref}\n', 1)[1].split('\n## ', 1)[0]
    title = section.split('**titre**', 1)[1].split('\n**', 1)[0].strip()
    excerpt = section.split('**texte**', 1)[1].split('\n**', 1)[0].strip()
    guide['sources'].append({'id': ref, 'title': title, 'excerpt': excerpt, 'scope': 'Verbatim de la contribution ; principe adopté, formulation pédagogique proposée.'})
    guide['source_refs'].append(ref)
lesson = guide['lessons'][0]
lesson.update({
    'title': 'Des responsabilités métier qui coopèrent',
    'rule': 'Une capacité décrit ce que l’entreprise sait faire durablement. Univers et domaines regroupent des responsabilités qui coopèrent par des informations, des demandes et des engagements.',
    'established_at': '2026-09-19',
    'scene': {'kind': 'responsibilities', 'caption': 'Illustration métier : possibilités, refus et écarts peuvent circuler en retour. Cet exemple ne crée pas trois nouveaux domaines dans le catalogue.', 'items': [
        {'label': 'Commerce', 'text': 'Exprimer l’intention et les attentes'},
        {'label': 'Supply', 'text': 'Établir un engagement de satisfaction'},
        {'label': 'Logistique', 'text': 'Concrétiser les prestations attendues'}]},
    'question': 'Plusieurs domaines contribuent à satisfaire une commande. Cela les transforme-t-il en une hiérarchie de couches ?',
    'choices': [
        {'label': 'Non, ils coopèrent avec des responsabilités distinctes', 'feedback': 'Une interaction indique ce qui est attendu ou partagé. Elle ne crée ni parent-enfant ni responsabilité unique.'},
        {'label': 'Oui, chaque étape devient une couche du modèle', 'feedback': 'L’ordre d’un parcours ne définit pas la structure de la carte. Les retours, refus et écarts mobilisent aussi plusieurs responsabilités.'}],
    'explanation': 'La carte organise des problèmes métier durables. Les interactions expliquent leur coopération. Un parcours traverse plusieurs responsabilités sans créer un étage supplémentaire dans la décomposition.',
    'contributor': {'criterion': 'Décris le résultat, les limites et les informations échangées ; distingue ce qui est demandé, décidé, engagé et constaté.', 'boundary': 'Atlas reste une référence métier. Les choix de produits, applications et réalisations sont documentés séparément, hors d’Atlas.', 'scope': 'Principes U455/U456 appliqués ; exemple de coopération et formulation pédagogique proposés, aucun domaine ajouté.', 'source_refs': ['U33', 'U455', 'U456']},
    'model_links': [{'id': 'D03.n', 'label': 'Fulfillment Commitment'}, {'id': 'D04.i', 'label': 'Sales Order'}],
})
for lesson in guide['lessons']:
    lesson['contributor']['boundary'] = lesson['contributor']['boundary'].replace('une seule capacité de même couche', 'une seule capacité, explicitement reliée à son parent')
    if lesson['id'] == 'useful-detail':
        lesson['contributor']['source_refs'].append('U455')
write_text_if_changed(root / 'modeles/backlog/modeling-guide-U458.yaml', dumps(guide))

path = root / 'modeles/backlog/glossary.yaml'
glossary = read(path)
if not any(term['id'] == 'TER086' for term in glossary['terms']):
    glossary['terms'].append({
        'id': 'TER086', 'name': 'Purchase Order Document',
        'short_description': 'Bon de commande : document exprimant le contenu d’une commande d’achat à un moment donné.',
        'definition': 'Bon de commande : document exprimant le contenu d’une commande d’achat à un moment donné. Le document, la commande métier et la capacité qui la prend en charge sont des notions distinctes.',
        'context': 'Se rapporte à l’objet [Purchase Order](glossary:TER070), pris en charge par la capacité [Purchase Order](model:D04.j). Le document ne désigne pas toute l’activité d’achat.',
        'notes': 'Ajout lexical proposé pour U458, sans création de nœud documentaire, cardinalité ou règle de correction. Usage français « bon de commande » vérifié dans Microsoft Learn, Vue d’ensemble des approvisionnements, section Accusé de réception de marchandises et facture : https://learn.microsoft.com/fr-fr/dynamics365/supply-chain/procurement/procurement-sourcing-overview (consulté le 19 septembre 2026). Distinction conceptuelle document/objet/capacité issue de U61/U384 ; la terminologie Microsoft n’impose pas cette convention FLOW.',
        'source_refs': ['U61', 'U384', 'U453', 'U458'],
        'source_locator': {'path': 'connaissance/01-contributions-utilisateur.md', 'anchor': 'u458'},
        'review': {'state': 'proposed', 'note': 'Précision lexicale Codex, non validation globale des conventions documentaires.'},
        'revision': 1, 'last_modified': '2026-09-19',
    })
    write_text_if_changed(path, dumps(glossary))
print('Guide draft and lexical term prepared; no publication changed.')
