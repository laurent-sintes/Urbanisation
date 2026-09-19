"""Apply requested short names and record the Customer Return behavior proposal."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'audits/2026-09-18-customer-return-U384'
NAMES = {'D04.i': 'Sales Order', 'D04.j': 'Purchase Order', 'D04.k': 'Transfer Order',
         'D04.l': 'Customer Return', 'D04.m': 'Supplier Return'}


def save(path, data):
    (ROOT / path).write_text(dumps(data), encoding='utf-8')


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    assert not OUT.exists(), 'Do not overwrite prior evidence.'
    mp = ROOT / 'modeles/backlog/model.yaml'; before = read(mp); m = deepcopy(before)
    assert '## U384\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U384

**id**

U384

**date**

2026-09-18

**titre**

Nommer les capacités d’Order sans Management et détailler Customer Return

**texte**

Il faut détailler les comportements des orders maintenant en commencant par Customer Return.

En terme de naming, enlever management à la fin de Purchase Order etc.

**contexte et portée**

Renommage demandé des cinq capacités par type : Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return. Aucun changement de nature ni suppression de Management dans les autres capacités/domaines. Demande d’instruction détaillée des comportements, en commençant par Customer Return, sur la direction U382. Les compléments proposés (distinction des destinataires du renvoi, mise au rebut et descriptions développées) ne sont pas adoptés par anticipation. La distinction capacité/objet reste portée par le modèle et les définitions ; aucune release demandée.''')
    OUT.mkdir()
    for stem in ['model', 'glossary', 'behavior-gap-audit']:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    (OUT / 'AGENTS-before.md').write_bytes((ROOT / 'AGENTS.md').read_bytes())
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    mapping = {n['fields']['name']: NAMES[n['id']] for n in m['nodes'] if n['id'] in NAMES}
    assert all(k.endswith(' Management') for k in mapping)
    def replace(text):
        for old, new in mapping.items(): text = text.replace(old, new)
        return text
    for node in m['nodes']:
        previous = deepcopy(node)
        for key, value in node['fields'].items():
            if isinstance(value, str): node['fields'][key] = replace(value)
        if node['id'] in NAMES:
            node['fields']['scope'] += ('\n\nNommage U384 : le libellé court désigne ici une capacité d’action, définie par « gérer les commandes » ; '
                'le document ou objet Order reste distinct dans le glossaire. Cette convention ne renomme pas les capacités transverses.')
            node['lifecycle']['value_sha256']['name'] = value_hash(node['fields']['name'])
            node['lifecycle']['source_refs'] = list(dict.fromkeys(node['lifecycle']['source_refs'] + ['U384']))
            node['lifecycle']['recorded_at'] = stamp
            node['lifecycle']['note'] = 'Nom court adopté U384 ; nature capacité et accords antérieurs conservés. Descriptions et décompositions qualifiées séparément.'
        if node != previous:
            for field in previous.get('lifecycle', {}).get('validated_fields', []):
                if field == 'name' and node['id'] in NAMES: continue
                assert node['fields'][field] == previous['fields'][field], (node['id'], field)
            node['revision'] += 1
            node['source_refs'] = list(dict.fromkeys(node['source_refs'] + ['U384', 'CMP143']))
    for relation in m['relations']:
        scope = relation.get('qualification', {}).get('scope')
        if isinstance(scope, str) and replace(scope) != scope:
            assert 'qualification' not in relation.get('lifecycle', {}).get('validated_fields', [])
            relation['qualification']['scope'] = replace(scope)
            relation['revision'] += 1
            relation['source_refs'] = list(dict.fromkeys(relation['source_refs'] + ['U384']))
    save('modeles/backlog/model.yaml', m)
    gp = 'modeles/backlog/glossary.yaml'; glossary = read(ROOT / gp)
    for term in glossary['terms']:
        if isinstance(term.get('notes'), str) and replace(term['notes']) != term['notes']:
            term['notes'] = replace(term['notes'])
            term['source_refs'] = list(dict.fromkeys(term['source_refs'] + ['U384']))
    save(gp, glossary)
    migration = dict(source_refs=['U384', 'CMP143'], model_before=(OUT / 'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT / 'model-before.yaml').read_bytes()).hexdigest(), delta={}, behaviors=[], adopted_names=NAMES,
        scope='Noms courts des cinq capacités et labels de référence actualisés ; comportements Customer Return proposés en annexe, aucun comportement créé.')
    for key in ['nodes', 'relations']:
        old = {x['id']: x for x in before[key]}; new = {x['id']: x for x in m[key]}
        migration['delta'][key] = dict(added={i: value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i: value_hash(new[i]) for i in sorted(new.keys() & old.keys()) if new[i] != old[i]}, removed=sorted(old.keys()-new.keys()))
    (OUT / 'implementation.yaml').write_text(dumps(migration), encoding='utf-8')
    ap = 'modeles/backlog/behavior-gap-audit.yaml'; audit = read(ROOT / ap)
    audit['implementation_U384'] = migration
    audit['source_refs'] += ['U384', 'ELM232', 'CMP143']
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    for assessment in audit['assessments']:
        if assessment['capability_id'] in NAMES: assessment['name'] = NAMES[assessment['capability_id']]
        if assessment['capability_id'] == 'D04.l':
            assessment['recommendation'] = 'Cinq parcours détaillés en proposition U384 dans customer-return-behaviors.yaml ; préserver les frontières décision, Orders, exécution et stocks.'
    save(ap, audit)
    sap_url = 'https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html'
    ms_url = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items'
    sales_url = 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns'
    comparisons = [
        dict(vendor='SAP', product='S/4HANA Cloud — Warehouse Management', element_name='Logistical Follow-Up Activities',
             element_type='Suites de processus produit', relationship='Recouvrement partiel',
             similarities='Remise en stock disponible, réparation, expédition fournisseur, restitution client et rebut documentés.',
             differences='Documents, mouvements et étapes de processus ne sont pas automatiquement des capacités ou comportements FLOW ; absence d’équivalence de niveau.',
             flow_position='Appui au choix de parcours métier ; préserver D05.i pour choisir, D04 pour les Orders, D06 pour les prestations et D01 pour les stocks.',
             source_title='Logistical Follow-Up Activities', source_url=sap_url, source_version='2602 affiché par le passage primaire indexé',
             source_locator='Table : 0011, 0012, 0005, 0021 et 0026', consulted_on='2026-09-18',
             evidence_limits='Texte primaire indexé consulté ; portail direct partiellement inaccessible. Aucune réalisation Beaumanoir déduite.',
             status='proposed', source_refs=['U384', 'ELM232', 'CMP143']),
        dict(vendor='Microsoft', product='Dynamics 365 Supply Chain Management', element_name='Disposition codes and disposition actions',
             element_type='Configuration et actions de traitement produit', relationship='Recouvrement partiel',
             similarities='Codes réparation, reconditionnement, renvoi fournisseur ; actions de remise en stock, rebut et restitution au client.',
             differences='Les six actions prédéfinies combinent effets logistiques et financiers ; un code libre ne prouve pas un processus natif complet de réparation.',
             flow_position='Conserver les parcours logistiques et expliciter les interfaces commerciales sans absorber remboursement et comptabilité.',
             source_title='Specify how to dispose of returned items', source_url=ms_url, source_version='Mise à jour affichée 2025-05-07',
             source_locator='Disposition types/codes ; six disposition actions', consulted_on='2026-09-18',
             evidence_limits='Page primaire ouverte ; fonctionnalités produit, sans preuve de couverture Beaumanoir.', status='proposed', source_refs=['U384', 'ELM232', 'CMP143'])]
    proposals = [
        dict(id='CR-P01', name='Return to Stock', definition='Prendre en charge un retour destiné à redevenir disponible dans le stock, selon l’état et les conditions retenus.',
             mechanism='Parcours de remise en disponibilité : suivre les quantités et conditions à satisfaire, demander les suites nécessaires et rapprocher la remise en disponibilité constatée.',
             benefit='Éviter qu’un produit simplement reçu soit promis avant sa remise en état ou sa libération effective.',
             example='Un vêtement intact reçu en magasin doit être contrôlé et réétiqueté avant de redevenir vendable. Reçu, accepté et disponible restent distincts.',
             boundary='D05.i retient l’orientation ; D06 organise les prestations et D01 enregistre état et disponibilité. Aucun stock réputé disponible par simple clôture de l’Order.', market_terms=['SAP Transfer to Free Available Stock', 'Microsoft Credit (volet logistique uniquement)']),
        dict(id='CR-P02', name='Repair and Refurbishment', definition='Prendre en charge un retour nécessitant une remise en état avant sa destination finale.',
             mechanism='Parcours avec prestation corrective : préserver le lien au produit et au retour, suivre la prise en charge, le résultat et la suite autorisée.',
             benefit='Récupérer un bien utilisable tout en rendant visible l’immobilisation et les échecs de remise en état.',
             example='Une fermeture défectueuse est réparée ; selon la décision applicable, le vêtement revient au client ou au stock. Un échec remonte pour réexaminer le devenir.',
             boundary='La réalisation de la réparation reste chez l’exécutant et son orchestration dans D06. Le coût acceptable et le choix du devenir sont dans D05.i. Aucun atelier interne imposé.', market_terms=['SAP In-House Repair (Service)', 'Microsoft Repair / Remanufacture-Refurbish (codes)']),
        dict(id='CR-P03', name='Return to Supplier', definition='Prendre en charge la suite d’un retour client dont les biens doivent être renvoyés au fournisseur.',
             mechanism='Relais vers une commande de retour fournisseur liée au retour client ; suivre les quantités transférées à cette responsabilité et leur résultat.',
             benefit='Conserver la traçabilité entre réclamation client, biens reçus et reprise fournisseur sans gérer deux fois la même commande.',
             example='Trois pièces présentant un défaut fournisseur sont rattachées à un Supplier Return ; l’expédition ne prouve ni réception fournisseur ni avoir.',
             boundary='Supplier Return D04.m porte la commande fournisseur ; ce comportement porte son articulation avec le retour client. L’accord de reprise est une condition, jamais déduit du choix logistique.', market_terms=['SAP Ship to Supplier', 'Microsoft Return to Vendor (code)']),
        dict(id='CR-P04', name='Return to Customer', definition='Prendre en charge la restitution au client du produit concerné par son retour.',
             mechanism='Parcours de restitution du même produit, après réparation ou après décision applicable de ne pas le reprendre ; préserver identité, destinataire et preuve de restitution.',
             benefit='Distinguer restitution du bien et envoi d’un nouveau produit de remplacement.',
             example='Le produit réparé est rendu au client. Un autre cas peut être le retour non accepté, restitué après la décision compétente.',
             boundary='Ne décide pas du refus commercial. Ne crée pas implicitement une nouvelle vente, ne remplace pas la réservation/promesse d’un article de remplacement. D06 suit l’acheminement.', market_terms=['SAP Send Back to Customer', 'Microsoft Return to customer']),
        dict(id='CR-P05', name='Scrapping', definition='Prendre en charge la sortie définitive d’un produit retourné orienté vers le rebut.',
             mechanism='Parcours de retrait contrôlé : conserver le motif et l’autorisation, suivre la prestation et rapprocher la preuve avec la sortie de stock.',
             benefit='Éviter remise en vente ou disponibilité indue et distinguer décision de rebut, stock en attente et réalisation effective.',
             example='Un article non récupérable attend une prestation de traitement ; le retour garde sa trace jusqu’au résultat et à l’enregistrement de la sortie.',
             boundary='D05.i décide du devenir, l’exécutant réalise, D06 trace et D01 enregistre. Ne regroupe pas donation, recyclage et revente secondaire sous le même résultat.', market_terms=['SAP Transfer to Scrap', 'Microsoft Scrap'])]
    for proposal in proposals:
        proposal.update(status='proposed', parent_id='D04.l', source_refs=['U382', 'U384', 'ELM232', 'CMP143'])
    review = dict(id='CUSTOMER-RETURN-BEHAVIORS-U384', status='proposed', source_refs=['U382', 'U383', 'U384', 'ELM232', 'CMP143'],
        capability_id='D04.l', current_name='Customer Return',
        proposed_definition='Prendre en charge les retours clients, leurs commandes et leurs suites logistiques, jusqu’au résultat attendu selon les décisions et autorisations applicables.',
        definition_status='proposed_not_applied',
        decomposition_rationale='Les parcours diffèrent par le devenir attendu, les responsabilités sollicitées, les immobilisations et les preuves nécessaires pour considérer le retour traité. Cette complexité justifie des comportements métier ; les étapes de saisie, inspection, validation et clôture ne constituent pas chacune un comportement.',
        rationale_status='proposed_not_applied', proposals=proposals, market_comparisons=comparisons,
        combination='Parcours combinables par produit ou quantité : réparation puis remise en stock ou restitution client. Pas cinq étapes obligatoires ni duplication des opérations communes.',
        renvoi_clarification='Distinguer fournisseur et client : contrepartie, obligation et preuve finale différentes. Deux comportements proposés pour préciser le terme renvoi U382.',
        shared_functions=['Enregistrer origine, motif et références utiles.', 'Rapprocher quantités attendues et reçues ; exploiter constats et écarts.', 'Conserver liens entre retour et suites, avancement et résultats.', 'Mobiliser Lifecycle, Structuring et Archiving pour leurs responsabilités communes.'],
        additional_market_patterns=[
            dict(name='Customer replacement', status='separate_boundary_to_review', reason='Microsoft utilise un Sales Order lié. Le devenir de l’ancien bien et l’envoi du remplacement sont deux axes combinables ; ne pas les mélanger dans une liste exclusive.', source_url=sales_url),
            dict(name='Returnless resolution', status='commercial_boundary_to_review', reason='Microsoft Credit only documente un règlement sans retour physique. Un tel parcours ne doit pas enregistrer une réception fictive ; autorisation et remboursement restent à attribuer.', source_url=sales_url),
            dict(name='Secondary resale, donation, recycling', status='to_review_if_applicable', reason='Filières distinctes ; ne pas les assimiler au rebut. Les codes Microsoft attestent notamment vente secondaire, donation et salvage, sans prouver un parcours complet FLOW.', source_url=ms_url)],
        naming_convention='Les libellés courts des cinq capacités sont adoptés U384. Les noms des nouveaux comportements et la définition élargie restent proposés. Le renvoi fournisseur est un relais vers D04.m, pas sa duplication.')
    save('modeles/backlog/customer-return-behaviors.yaml', review)
    for stem in ['d04-refactoring', 'order-lifecycle-behaviors']:
        path = f'modeles/backlog/{stem}.yaml'; data = read(ROOT / path)
        data['current_U384'] = dict(source_refs=['U384'], names=NAMES, naming_status='adopted',
            behavior_review='modeles/backlog/customer-return-behaviors.yaml', behavior_status='detailed_proposal_not_adopted')
        save(path, data)
    append('marche/elements.md', '''### ELM232

18 septembre 2026 ; U384. Sources primaires consultées pour Customer Return :

- SAP S/4HANA Cloud, Warehouse Management, Logistical Follow-Up Activities, version 2602 affichée dans le texte indexé. Table 0011 stock disponible, 0012 rebut, 0005 fournisseur, 0021 client et 0026 réparation. https://help.sap.com/docs/SAP_S4HANA_CLOUD/87f9b54f9c4f4e75aff0061860a6589a/aeb252c114df4dac9abf1626ccb04233.html . Portail direct partiellement inaccessible ; texte primaire indexé effectivement consulté.
- Microsoft Dynamics 365 SCM, Specify how to dispose of returned items, page ouverte, mise à jour affichée 7 mai 2025 ; tables des codes et actions. https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items .
- Microsoft Dynamics 365 SCM, Sales returns, page évolutive ouverte ; Return order process, RMA et Disposition codes and actions. https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-returns . Retours physiques et credit only ; remplacement porté par commande de vente liée.

Nature : processus, configurations et activités produit ; aucune équivalence automatique avec des comportements métier, aucune preuve de réalisation Beaumanoir. Synthèses sélectives, sans reproduction intégrale.''')
    append('marche/comparaisons.md', '''## CMP143

Codex ; 18 septembre 2026 ; U384 ; ELM232. Noms courts des cinq capacités D04.i–m appliqués sur demande ; aucune nouvelle équivalence avec les objets documentaires du même nom. Microsoft emploie Sales returns pour le processus et Purchase order pour le document ; la convention FLOW conserve le type capacité et une définition verbale explicite.

Cinq comportements Customer Return proposés dans modeles/backlog/customer-return-behaviors.yaml : Return to Stock, Repair and Refurbishment, Return to Supplier, Return to Customer et Scrapping. Rapprochement partiel aux suites logistiques SAP et dispositions Microsoft. Les contreparties et preuves justifient la distinction des renvois ; Supplier Return reste la capacité qui porte la commande fournisseur. FLOW sépare les décisions D05.i, les suites D04, les prestations D06 et les stocks D01, là où les fonctions produit peuvent les associer avec des effets financiers.

Les parcours sont combinables ; réparation puis restitution ou stock. Remplacement client et règlement sans retour sont d’autres axes, à instruire avec les frontières commerciales. Donation, revente secondaire et recyclage ne sont pas assimilés au rebut. Noms, descriptions et élargissement proposé de Customer Return restent à discuter ; seul le retrait de Management est appliqué au catalogue dans U384.''')
    (OUT / 'README.md').write_text('''# Customer Return — U384

Les noms Sales Order, Purchase Order, Transfer Order, Customer Return et Supplier Return sont appliqués aux cinq capacités avec identifiants conservés. Les références textuelles courantes et notes de glossaire suivent ce nommage. Order Management et Order Lifecycle Management ne sont pas renommés.

La proposition détaillée fait autorité dans modeles/backlog/customer-return-behaviors.yaml : cinq parcours, bénéfices, exemples, frontières et comparaisons. Elle distingue renvoi fournisseur et restitution client, ajoute le rebut comme candidat et conserve les autres axes du marché à instruire. Aucun comportement ni élargissement de définition validé implicitement dans le catalogue. Les captures et le delta préservent les accords antérieurs.
''', encoding='utf-8')
    print('U384: five short capability names applied; Customer Return proposal recorded separately.')


if __name__ == '__main__':
    main()
