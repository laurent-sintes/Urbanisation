"""Adopt Order Backlog Management and record the bounded placement review."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/order-backlog-U413'
REFS = ['U411', 'U412', 'U413', 'ELM246', 'CMP157']
NAME = 'Order Backlog Management'


def main():
    assert not OUT.exists()
    path = ROOT / 'modeles/backlog/model.yaml'
    before = read(path); model = deepcopy(before)
    contributions = [
        ('U411', 'Reconsidérer le carnet comme backlog et ses responsabilités', '''On avait parlé à une époque de gestion du carnet de commandes comme une backlog : on affine, on split, on regroupe, on valide, on release. Je crois qu'il ya une référence comme ça chez microsoft. Comme nom de domaine ça pourrait être sympa, non ? Pas de nouveau domaine mais un renommage peut être. Qu'en penses-tu ? Peut être que les traitements externes aux orders (split, release etc) sont des capacités de backlog et non d'order. Il y a peut être du déplacement de capacité si on veut rester logique.''', 'Demande de comparaison et de réexamen, sans ajout de domaine. Historique U157/U158 retrouvé : Oracle Backlog Management ; Microsoft Planned Orders apporte une pratique proche, pas une taxonomie universelle.'),
        ('U412', 'Distinguer demande individuelle et travail collectif du carnet', '''Et pourtant ça me plait bien et ça correspond au langage du métier qui parle de "faire tourner le carnet de commande, le travailler". Il y a le niveau commande qu'on capte, qu'on gère à l'unité pour comprendre le besoin du client et puis il y a la vision carnet de commande comme une backlog : c'est là qu'on a une vision globale et qu'on priorise, découpe ce qu'on va vraiment satisfaire, c'est la notion de release qui est envoyée à l'éxécution (le process).''', 'Frontière par responsabilité métier : demande et conditions individuelles, travail collectif du carnet, puis prise en charge par les processus. Le résultat retenu peut fractionner la satisfaction sans imposer deux commandes clients ni une hiérarchie documentaire.'),
        ('U413', 'Adopter Order Backlog Management et le réexamen ciblé', 'Go', 'Accord sur le renommage D03 en Order Backlog Management et le mandat présenté : travailler collectivement le carnet, préparer et engager sa satisfaction vers Process Management. D04 conserve la demande selon son intention. Les décisions spécialisées restent dans D03. Réexamen ciblé de Lifecycle et Structuring autorisé ; pas de déplacement en bloc, de nouveau domaine ou de parent précis de comportement adopté. Release et préparation collective sont candidates au rattachement D03 ; Split/regroupement à distinguer selon leur finalité. Nom et principe adoptés ; définition développée, matrice détaillée et comparaisons éditoriales. Aucun nouveau cycle d’audit ni release.')]
    for ident, title, verbatim, scope in contributions:
        assert f'## {ident}\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
        append('connaissance/01-contributions-utilisateur.md', f'## {ident}\n\n**id**\n\n{ident}\n\n**date**\n\n2026-09-19\n\n**titre**\n\n{title}\n\n**texte**\n\n{verbatim}\n\n**contexte et portée**\n\n{scope}')
    OUT.mkdir()
    for rel, filename in [('modeles/backlog/model.yaml', 'model-before.yaml'), ('modeles/backlog/behavior-gap-audit.yaml', 'audit-before.yaml'), ('modeles/backlog/glossary.yaml', 'glossary-before.yaml'), ('AGENTS.md', 'AGENTS-before.md')]:
        (OUT / filename).write_bytes((ROOT / rel).read_bytes())
    comparisons = [dict(vendor='Oracle', product='Fusion Cloud SCM 26B', element_name='Start Backlog Planning', element_type='Processus et fonction produit', relationship='Recouvrement partiel', similarities='Prioriser et replannifier la satisfaction sur l’ensemble du carnet à partir des ressources et demandes actualisées.', differences='Documentation d’un produit et de son traitement planifié, pas taxonomie de capacités ni preuve de prise en charge de tous les types d’Orders FLOW.', source_title='Start Backlog Planning', source_url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faspc/start-backlog-planning.html', source_version='26B', source_locator='Introduction ; When to Use'),
        dict(vendor='Oracle', product='Fusion Cloud SCM 25D', element_name='Key Actions on Orders', element_type='Fonction produit', relationship='Recouvrement partiel', similarities='Travail du carnet, priorisation, simulation puis transmission des résultats retenus à Order Management.', differences='Release Planning Results transmet des résultats de planification ; ce n’est pas une équivalence exacte de l’autorisation FLOW vers les processus. La séparation demande/carnet/processus est la convention FLOW.', source_title='Key Actions on Orders', source_url='https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25d/faubm/key-actions-on-orders.html', source_version='25D, édition explicitement consultée', source_locator='Plan Run Actions ; Attribute Data Simulation Actions ; Release Actions'),
        dict(vendor='Microsoft', product='Dynamics 365 Supply Chain Management', element_name='View, manage, and approve planned orders', element_type='Pratique et fonction produit', relationship='Recouvrement partiel', similarities='Revoir et modifier les ordres planifiés, approuver les ajustements et préparer leur affermissement ; conservation des ajustements approuvés sous conditions lors des planifications suivantes.', differences='Approvisionnements planifiés de production, achat et transfert. Aucun équivalent universel aux commandes clients, retours ou à tout le carnet FLOW ; approbation, affermissement et release restent distincts.', source_title='View, manage, and approve planned orders', source_url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/approved-planned-order', source_version='Page mise à jour le 2 septembre 2026', source_locator='View and edit the status of planned orders ; Approve planned orders')]
    for comp in comparisons:
        comp.update(flow_position='D03 Order Backlog Management : les décisions spécialisées alimentent le travail collectif du carnet. D04 conserve la demande selon son intention, D06 orchestre les services. Rattachements de préparation/release en réexamen ciblé.', consulted_on='2026-09-19', evidence_limits='Source primaire ouverte lors de la discussion ; aucune preuve de déploiement Beaumanoir. Niveaux et périmètres produits non transposés automatiquement.', status='proposed', source_refs=REFS)
    domain = next(n for n in model['nodes'] if n['id'] == 'D03')
    domain['fields']['name'] = NAME
    domain['fields']['definition'] = 'Travailler collectivement le carnet d’Orders Supply pour prioriser les demandes, évaluer leurs possibilités de satisfaction, construire les scénarios d’affectation et préparer puis engager la part retenue vers les processus, en préservant le sens des demandes et les engagements applicables.'
    domain['fields']['scope'] = '''Le carnet est un ensemble de demandes que l’entreprise travaille : prioriser, examiner les possibilités, préparer les découpages et regroupements utiles et autoriser la prise en charge retenue. Les décisions ATP, CTP, PTP, de priorité, d’échéancier et de plan d’affectation alimentent ce travail. Les responsabilités de Supply Assignment et Promise Management sont conservées ; aucun critère unique de valeur ni suppression des garanties de réservation ou de gel.

Exemple fictif : un client demande 100 pièces. Sa demande reste lisible comme telle ; le carnet prépare une satisfaction de 60 maintenant et 40 ensuite ; les processus prennent en charge les 60 autorisées. Préparer deux fractions de satisfaction ne présume ni deux commandes clients, ni un nouvel Order chapeau, ni un cycle uniforme pour tous les types d’Orders.

Order Management D04 capte et maintient la demande selon son intention : vente, achat, transfert, retour ou apport sous consignation. Order Backlog Management D03 porte la vision collective et la préparation de ce qui sera satisfait. Process Management D06 orchestre les services nécessaires à la réalisation autorisée et adapte leur coordination selon les décisions responsables. Un processus en cours peut fournir des faits et aléas qui conduisent à retravailler le reste du carnet ; aucun parcours linéaire à sens unique imposé.

L’optimisation de satisfaction reste une responsabilité du domaine : Fulfillment Plan Decision choisit un scénario cohérent de valeur multidimensionnelle, avec les décisions spécialisées. Inventory Optimization D05 conserve la finalité de disponibilité, immobilisation et risque du stock ; un transfert peut servir l’une ou l’autre finalité sans fusion des domaines. D01 conserve stock, protections et réservations.

État de transition U413 : le nom et le mandat du domaine sont adoptés. Les rattachements de capacités et comportements sont conservés pendant le réexamen ciblé de Lifecycle et Structuring. Order Release BHV039 reste actuellement sous D04.o ; son positionnement du côté du carnet est une direction à concrétiser par un parent de capacité explicite. P11 reste résolu sur son contenu depuis U410. Split/regroupement doivent distinguer modification de la demande et préparation de la satisfaction. Aucun déplacement en bloc, doublon de comportement ou quatrième niveau n’est appliqué.

Le carnet opérationnel décrit ici est distinct du backlog de conception de la cartographie. L’usage de Backlog ne présume ni retard, ni demande non engagée : le reste à satisfaire d’Orders partiellement réalisés et les engagements déjà pris restent pris en compte. Cette portée FLOW est explicitée, sans prétendre à une définition universelle du marché.'''
    domain['fields'].setdefault('market_comparisons', []).extend(comparisons)
    life = domain['lifecycle']
    life['value_sha256']['name'] = value_hash(NAME)
    life['source_refs'] = list(dict.fromkeys(life['source_refs'] + ['U413']))
    life['recorded_at'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    life['note'] += ' U413 : nom et mandat adoptés ; définition et scope développés restent éditoriaux. Finalité antérieure préservée. Historique U369/U378 conservé dans la capture U413.'
    domain['review'] = dict(state='partial', note='U413 : nom adopté et mandat consigné ; rattachements de préparation/release à arbitrer. Pas de transfert implicite. Définition développée et comparaisons éditoriales.')
    for node in model['nodes']:
        old = next(n for n in before['nodes'] if n['id'] == node['id'])
        validated = set(node.get('lifecycle', {}).get('validated_fields', []))
        for field in ('scope', 'finality', 'decomposition_rationale'):
            if field in node['fields'] and field not in validated:
                node['fields'][field] = node['fields'][field].replace('Fulfillment Optimization', NAME)
        if node['id'] in {'D04.n', 'D04.o', 'BHV039', 'BHV044'}:
            assert 'scope' not in validated
            node['fields']['scope'] += '\n\nU413 : responsabilité réexaminée selon la frontière demande individuelle / travail collectif du carnet. Le contenu et le parent actuels sont conservés jusqu’à un arbitrage précis ; voir order-backlog-review.yaml. Aucun déplacement validé de cette fiche déduit du renommage D03.'
        if old != node:
            node['revision'] += 1
            node['source_refs'] = list(dict.fromkeys(node['source_refs'] + REFS))
    assert model['relations'] == before['relations']
    save('modeles/backlog/model.yaml', model)
    migration = dict(source_refs=REFS, model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(), model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(), adopted_name=NAME, name_sha256=value_hash(NAME), behaviors=[], delta={})
    for key in ('nodes', 'relations'):
        old = {x['id']: x for x in before[key]}; new = {x['id']: x for x in model[key]}
        assert old.keys() == new.keys()
        migration['delta'][key] = dict(added={}, removed=[], changed={i: value_hash(new[i]) for i in sorted(new) if new[i] != old[i]})
    save((OUT/'implementation.yaml').relative_to(ROOT), migration)
    # The bounded review is an annex of the existing audit, not a new audit campaign.
    matrix = [
        dict(ids=['D04.i','D04.j','D04.k','D04.l','D04.m','D04.r'], recommendation='Conserver D04 : intention, parties, conditions et suivi de la demande selon son type.', status='direction_adopted'),
        dict(ids=['BHV038','BHV043','D04.q'], recommendation='Conserver préparation de la demande, clôture et conservation côté Order ; aucun transfert en bloc de Lifecycle.', status='direction_adopted'),
        dict(ids=['BHV039'], recommendation='Candidat au côté carnet D03 : autoriser la part retenue vers les processus. Choisir explicitement une capacité parente D03 avant de changer contains ; D03 est un domaine, pas un parent de comportement.', status='placement_proposed', open_point='Réutiliser ou définir une capacité d’action justifiée pour la préparation et l’engagement du carnet, sans absorber les décisions spécialisées.'),
        dict(ids=['BHV044','D04.n'], recommendation='Distinguer scission/composition de la demande et organisation des fractions ou ensembles à satisfaire. Découper la satisfaction ne crée pas automatiquement de nouveaux Orders ; ne pas déplacer toute la composition commerciale en D03.', status='placement_proposed', open_point='Déterminer quels résultats sont des mutations d’Orders et lesquels sont portés par le plan ; préserver parent unique et pas de copie par contexte.'),
        dict(ids=['BHV036','BHV037','BHV040','BHV041','BHV042'], recommendation='Réexaminer la portée réelle avant déplacement : engagement de l’Order, protection contre optimisation, suspension, modification de date demandée ou planifiée, retrait de demande ou de son lancement sont distincts. L’usage collectif ne suffit pas à changer le propriétaire métier.', status='editorial_review', open_point='Pas de transfert en bloc. Montrer les effets sur demande et plan à partir des définitions existantes.'),
    ]
    review = dict(source_refs=REFS, status='name_and_direction_adopted_placements_pending', domain_id='D03', adopted_name=NAME, adopted_responsibility='Travailler le carnet : prioriser, évaluer les possibilités, construire des scénarios de satisfaction, préparer les découpages et regroupements utiles, puis autoriser la prise en charge retenue.', model_state='137 nœuds ; relations et parents inchangés. Aucun nouveau domaine ou comportement.', market_comparisons=comparisons, targeted_review=matrix, next_arbitration='Préciser la capacité d’action D03 qui porte préparation et engagement du carnet, puis son articulation avec Order Lifecycle Management et Order Structuring. Ne pas déplacer un comportement directement sous un domaine.', scope='Réexamen ciblé dans l’audit existant, U399 préservé. Le Go ne choisit pas un parent précis ni une nouvelle décomposition.', implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    save('modeles/backlog/order-backlog-review.yaml', review)
    audit = read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['implementation_U413'] = migration
    audit['baseline']['sha256'] = sha256(path.read_bytes()).hexdigest()
    audit['source_refs'] = list(dict.fromkeys(audit['source_refs'] + REFS))
    audit['order_backlog_U413'] = dict(status='targeted_placement_review', path='modeles/backlog/order-backlog-review.yaml', source_refs=REFS, note='D03 renommé ; P11 reste intégré BHV039. Sa responsabilité côté carnet et les rattachements de préparation font l’objet du réexamen ciblé adopté, sans réouvrir sa définition ni créer un audit.')
    save('modeles/backlog/behavior-gap-audit.yaml', audit)
    glossary = read(ROOT/'modeles/backlog/glossary.yaml')
    for term in glossary.get('terms', []):
        if term['id'] == 'TER085':
            term['notes'] = term['notes'].replace('Fulfillment Optimization', NAME)
            term['source_refs'] = list(dict.fromkeys(term['source_refs'] + ['U413']))
    save('modeles/backlog/glossary.yaml', glossary)
    agents = ROOT/'AGENTS.md'
    text = agents.read_text(encoding='utf-8')
    old = next(line for line in text.splitlines() if line.startswith('| D03 Fulfillment Optimization |'))
    text = text.replace(old, '| D03 Order Backlog Management | Nom et mandat adoptés U413, remplaçant Fulfillment Optimization U369. Travailler collectivement le carnet, préparer et engager la satisfaction vers les processus ; ATP/CTP/PTP, priorités, échéancier, Fulfillment Plan Decision, Supply Assignment et Promise Management gardent leurs responsabilités. D04 conserve la demande par intention, D06 orchestre les services. Réexamen ciblé Lifecycle/Structuring : aucun déplacement en bloc ni parent précis adopté ; BHV039 reste sous D04.o en attendant cet arbitrage. Portées : `modeles/backlog/order-backlog-review.yaml`. |')
    agents.write_text(text, encoding='utf-8')
    append('marche/elements.md', '### ELM246\n\nOracle Backlog Planning 26B et Key Actions on Orders 25D ; Microsoft Dynamics 365 SCM Planned Orders, page mise à jour le 2 septembre 2026. Sources primaires ouvertes le 19 septembre 2026 ; URL, passages et limites dans modeles/backlog/order-backlog-review.yaml. Vision collective du carnet chez Oracle ; préparation et approbation des propositions d’approvisionnement chez Microsoft. Pas de taxonomie métier universelle ni de preuve installée.')
    append('marche/comparaisons.md', '### CMP157\n\nU411–U413 : Order Backlog Management nomme D03 et sa responsabilité collective. Oracle étaye le nom et la priorisation/replanification du carnet ; Microsoft apporte la pratique de travail des Planned Orders. FLOW distingue demande selon son intention (D04), travail collectif et engagement du carnet (D03), orchestration de services (D06). Oracle Release Planning Results transmet au système de gestion de commandes ; la release vers les processus est la convention FLOW. Le périmètre achat/vente/transfert/retour ne se déduit pas des seuls produits consultés. Renommage et mandat adoptés, placements détaillés en réexamen ciblé ; les anciens accords ne sont pas effacés.')
    append('marche/backlog-management-supply-assignment.md', '## Direction courante U413 — Order Backlog Management\n\nD03 est renommé Order Backlog Management. Le mandat adopté comprend le travail collectif du carnet et la préparation de son engagement vers les processus ; les décisions spécialisées le nourrissent. D04 conserve la demande selon son intention. Réexamen ciblé de Lifecycle/Structuring dans modeles/backlog/order-backlog-review.yaml ; aucun déplacement en bloc ni parent de comportement adopté. Les réserves et propositions U157–U159 ci-dessus restent historiques. Comparaison actualisée CMP157.')
    append('JOURNAL.md', '## 2026-09-19 — U411–U413 : Order Backlog Management\n\nD03 renommé, mandat collectif explicité avec exemple 100 demandées / 60 prises en charge / 40 restantes. Comparaison Oracle/Microsoft ELM246/CMP157. Réexamen ciblé Lifecycle/Structuring consigné dans l’annexe de l’audit existant ; rattachements inchangés, choix de capacité parente à arbitrer. Anciennes validations et publications préservées ; aucune release.')
    (OUT/'README.md').write_text('# U413 — Order Backlog Management\n\nD03 renommé et mandat consigné. Réexamen ciblé dans order-backlog-review.yaml ; aucun déplacement de capacité/comportement ni nouveau domaine. Nom adopté, définition développée et matrice éditoriales.\n', encoding='utf-8')
    print('U413 integrated: D03 renamed; targeted review recorded; graph unchanged.')


if __name__ == '__main__':
    main()
