"""Record the evidence-based methodological clarification U389; no catalog migration."""
from pathlib import Path
from hashlib import sha256

from scripts.structured_io import read, dumps

ROOT = Path(__file__).resolve().parents[1]


def main():
    def path(relative):
        return ROOT / relative

    def append(relative, text):
        with path(relative).open('a', encoding='utf-8', newline='') as out:
            out.write('\n\n' + text.strip() + '\n')

    capture = path('audits/2026-09-18-behavior-definition-U389')
    assert not capture.exists(), 'One-shot record already exists'
    assert '## U389' not in path('connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    capture.mkdir()
    glossary_path = path('modeles/backlog/modeling-glossary.yaml')
    (capture / 'modeling-glossary-before.yaml').write_bytes(glossary_path.read_bytes())
    (capture / 'AGENTS-before.md').write_bytes(path('AGENTS.md').read_bytes())
    model_path = path('modeles/backlog/model.yaml')
    model_hash = sha256(model_path.read_bytes()).hexdigest()
    model = read(model_path)

    append('connaissance/01-contributions-utilisateur.md', '''## U389

**id**

U389

**date**

2026-09-18

**titre**

Étayer et mémoriser la définition de Comportement par une typologie concrète issue de l’existant

**texte**

Le niveau "comportement" du modèle traite de :

- mécanisme ou policy pour les décision
- variante de processus pour les orders
- scope pour les actions
- ....

Ce serait bien que la définition de comportement soit étayée par une liste concrete comme je vient de le faire. Il faut la construire par analyse de l'existant. J'aimerais que cette règle soit mémorisée.

**contexte et portée**

Instruction de construire une liste concrète à partir du modèle et de la conserver dans la méthode. Les trois exemples donnés orientent l’analyse ; ils ne fixent pas une correspondance exclusive entre nature de capacité et forme de comportement. L’exigence est acquise ; la typologie détaillée et sa rédaction résultent de l’analyse Codex et ne sont pas réputées intégralement validées par Laurent. Aucun changement de capacités, comportements, relations ou publication demandé.''')

    # Illustrations, not a closed type system or a new hierarchy.
    forms = [
        dict(key='policy_strategy', label='Politique ou stratégie métier', explanation='Distinguer une logique de choix, de protection ou de contrôle qui change la réponse ou la façon d’agir.', examples=['Reservation Policy Decision : Milestone-Based et Risk-Adaptive Reservation Policy (BHV032, BHV035).', 'Return Disposition Decision : Policy-based Disposition et Value Recovery Optimization (BHV048, BHV049).', 'Stocktaking : Periodic Physical Inventory, Cycle Counting, Spot Counting (BHV029–031).'], boundary='Une valeur de seuil, une fréquence précise ou le choix humain/IA ne suffit pas à créer un comportement.'),
        dict(key='process_variant', label='Variante de processus ou de prise en charge', explanation='Distinguer un parcours par son résultat attendu, ses obligations, ses acteurs ou ses flux métier, sans détailler toutes ses étapes.', examples=['Customer Return : Return to Stock, Repair and Refurbishment, Return to Supplier (BHV050–052).', 'Supplier Return : Return for Credit, Return for Replacement, Return for Repair (BHV055–057).'], boundary='Saisie, validation et clôture ne deviennent pas automatiquement trois comportements sous chaque Order ; les parcours peuvent se combiner.'),
        dict(key='intervention_mechanism', label='Mécanisme d’intervention', explanation='Distinguer comment une capacité produit son effet métier, notamment en préservant ou en révisant un état existant.', examples=['Supply Assignment : Plan Application, Incremental Supply Assignment, Supply Reassignment (BHV045–047).', 'Supply Protection : Group Supply Protection, Consumption Capping, Safety Stock Policy, Replenishment Regulation (BHV017–020).', 'Stock Redistribution Decision : Inventory Rebalancing et Stock Consolidation (BHV024–025).'], boundary='Ne pas confondre mécanisme métier et algorithme, API, batch ou liste des opérations CRUD.'),
        dict(key='business_scope', label='Périmètre métier d’intervention ou d’arbitrage', explanation='Distinguer une portée qui change les contraintes, interdépendances, faits observés ou responsabilités ; ce critère vaut aussi pour les décisions.', examples=['Inventory Target Decision : Store, Distribution Center et Multi-Echelon Inventory Optimization (BHV026–028).', 'Execution Tracking : Warehouse, Transportation et Store Visibility, arbitrés en annexe U305/U308 mais non intégrés comme nœuds dans le catalogue analysé.'], boundary='Un comportement par site, équipe ou application n’est pas justifié par le seul changement de périmètre. Le tracking est une capacité de connaissance, pas une action au sens strict de fields.nature.'),
        dict(key='decision_dimension', label='Dimension de raisonnement ou d’information prise en compte', explanation='Distinguer les informations ou contraintes qui changent les possibilités établies par une décision ; les dimensions sont combinables.', examples=['ATP : engagements existants, stock du réseau, délai de mobilisation opérationnelle et apports futurs (BHV001–004).'], boundary='Ne pas transformer chaque donnée d’entrée ou étape de calcul en comportement ; Decision garde ses calculs.'),
        dict(key='business_effect', label='Effet sur l’état métier ou l’engagement', explanation='Distinguer des effets substantiels sur les obligations, l’autorisation, la stabilité ou la continuité du traitement.', examples=['Promise Management : Promise Proposal, Confirmation, Revision (BHV021–023).', 'Order Lifecycle Management : Drafting, Firming, Freezing, Release, Hold & Resume, Rescheduling, Cancellation, Closure, Splitting (BHV036–044).'], boundary='Le nom d’un statut ou d’un bouton ne suffit pas ; expliquer l’effet métier. Ce critère n’autorise pas à dupliquer Lifecycle sous chaque type d’Order.'),
        dict(key='planning_practice', label='Pratique de planification et d’adaptation', explanation='Distinguer une manière de travailler sur un scénario qui transforme l’analyse, la coordination humaine ou les interactions avec l’exécution.', examples=['Inventory Planning : Scenario Construction, Simulation & Analysis, Scenario Execution Adaptation (BHV005, BHV006, BHV016).'], boundary='Évaluation, validation et application restent des fonctions utiles sans comportement autonome justifié à ce stade ; ne pas déplacer la responsabilité d’adaptation opérationnelle de D06.'),
    ]
    assignments = {
        'D01.d': ['policy_strategy'], 'D02.b': ['intervention_mechanism', 'policy_strategy'],
        'D02.e': ['intervention_mechanism'], 'D03.i': ['decision_dimension'],
        'D04.l': ['process_variant'], 'D04.m': ['process_variant'],
        'D04.o': ['business_effect'], 'D05.a': ['business_scope'],
        'D05.c': ['intervention_mechanism'], 'D05.f': ['planning_practice'],
        'D03.n': ['business_effect'], 'D05.h': ['policy_strategy'], 'D05.i': ['policy_strategy'],
    }
    nodes = {n['id']: n for n in model['nodes']}
    behaviors = {key: n for key, n in nodes.items() if n['kind'] == 'behavior'}
    evidence = []
    seen = []
    for parent, categories in assignments.items():
        children = [r['target_id'] for r in model['relations'] if r['type'] == 'contains' and r['source_id'] == parent and r['target_id'] in behaviors]
        assert children
        seen.extend(children)
        evidence.append(dict(capability_id=parent, capability_name=nodes[parent]['fields']['name'], nature=nodes[parent]['fields'].get('nature', 'not_specified'), illustrative_forms=categories, decomposition_rationale=nodes[parent]['fields']['decomposition_rationale'], behaviors=[dict(id=b, name=behaviors[b]['fields']['name'], definition=behaviors[b]['fields']['definition']) for b in children]))
    assert len(seen) == len(set(seen)) == len(behaviors) == 48
    assert set(seen) == set(behaviors)
    rule = 'Pour définir ou réexaminer un comportement, partir d’exemples du modèle, expliciter sa forme concrète, ce qui le distingue des autres comportements de la capacité et son effet métier. Justifier la décomposition par une complexité ou un bénéfice ciblé ; ne pas imposer une catégorie exclusive par nature de capacité, une décomposition systématique ou un niveau supplémentaire.'
    glossary = read(glossary_path)
    glossary['as_of'] = '2026-09-18'
    glossary['source_refs'].append('U389')
    term = next(t for t in glossary['terms'] if t['id'] == 'MOD006')
    term['definition'] = 'Un comportement décrit une manière métier identifiable dont une capacité agit dans certaines circonstances : politique ou stratégie, mécanisme, variante de prise en charge, périmètre significatif, dimension de raisonnement, effet sur un engagement ou pratique de planification. Il précise ce qui change dans la réponse, l’action ou le résultat attendu, sans détailler les fonctions du produit.'
    term['concrete_forms'] = forms
    term['decomposition_rule'] = rule
    term['analysis_ref'] = 'modeles/backlog/behavior-typology.yaml'
    term['notes'].extend([
        'U389 exige une liste concrète issue de l’existant. Les formes se recouvrent et ne sont ni des sous-niveaux ni une classification obligatoire des nœuds.',
        'Le bénéfice ciblé reste un critère transversal de justification U265/U283 : il peut différencier une manière d’agir, mais un bénéfice vague ne remplace pas la description de cette manière d’agir.',
        'U389 : les exemples de scopes de visibilité proviennent des arbitrages U305/U308, distincts des 48 comportements intégrés. Leur mention méthodologique ne les intègre ni ne les publie.',
    ])
    term['source_refs'].extend(['U389', 'CMP145'])
    term['review']['adopted_scope'] += ' U389 demande une définition étayée par une liste concrète construite à partir de l’existant et la mémorisation de cette règle.'
    term['review']['proposed_scope'] += ' La reformulation, les sept formes illustratives et leur analyse transversale U389 sont éditoriales ; aucune classification exhaustive validée par Laurent n’est présumée.'
    term['market_comparison'] = dict(comparison_ref='CMP145', common='BIZBOK décrit Capability Behavior comme une manière d’agir selon les circonstances ; Microsoft illustre plusieurs politiques de comptage.', difference='Les sept formes et le niveau terminal sont des conventions FLOW ; les sources ne prescrivent pas cette typologie ni une équivalence de niveaux.', sources=['ELM052', 'ELM234'], consulted_on='2026-09-18')
    glossary_path.write_text(dumps(glossary), encoding='utf-8')
    analysis = dict(id='flow-behavior-typology-U389', kind='methodological_analysis', as_of='2026-09-18', source_refs=['U389', 'U265', 'U283', 'CMP145'], status='editorial_analysis_rule_requested', canonical_definition='modeles/backlog/modeling-glossary.yaml#MOD006', model_sha256=model_hash, catalog_behavior_count=len(behaviors), decomposed_capability_count=len(evidence), method='Lecture des définitions, justifications et rattachements explicites des 48 comportements ; regroupement par différence métier. Aucun changement de catalogue.', observations=evidence, supplementary_scope_evidence=dict(path='modeles/backlog/behavior-gap-audit.yaml', section='current_visibility_names', parent_id='D07.d', names=['Warehouse Visibility', 'Transportation Visibility', 'Store Visibility'], source_refs=['U305', 'U308'], status='arbitrated_in_annex_not_integrated', excluded_from_catalog_count=True), conclusion='Les sept formes sont des repères combinables. Politiques aussi sous les actions, périmètres aussi sous les décisions ; pas de correspondance exclusive avec fields.nature. Le bénéfice justifie transversalement la décomposition.')
    path('modeles/backlog/behavior-typology.yaml').write_text(dumps(analysis), encoding='utf-8')
    agents_path = path('AGENTS.md')
    agents = agents_path.read_text(encoding='utf-8')
    marker = '- Objets métier, documents et événements restent distincts'
    insertion = '- **Définition concrète des comportements (U389)** : étayer la définition par l’analyse de l’existant et maintenir les exemples dans [MOD006](modeles/backlog/modeling-glossary.yaml) ; analyse traçable dans [behavior-typology.yaml](modeles/backlog/behavior-typology.yaml). Repères : politique/stratégie, variante de processus, mécanisme d’intervention, périmètre métier, dimension de raisonnement, effet sur l’état ou l’engagement, pratique de planification. Pour chaque proposition, expliciter la différence et l’effet métier ; appliquer U265. Ces formes sont combinables et non exclusives par nature (scope aussi pour les décisions, politique aussi pour les actions) ; aucune nouvelle hiérarchie ni décomposition systématique. Distinguer exemples du catalogue et arbitrages encore en annexe.\n'
    assert marker in agents
    agents_path.write_text(agents.replace(marker, insertion + marker, 1), encoding='utf-8')
    append('marche/elements.md', '''### ELM234

U389 — consulté le 18 septembre 2026. Microsoft Dynamics 365 Supply Chain Management (MKT14), **Cycle counting**, page évolutive mise à jour le 20 novembre 2025 : introduction, Automatically create cycle counting work et Perform a cycle count by using a mobile device. Source primaire : https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting .

Nature : processus et fonctions produit WMS. Le texte distingue comptage selon plan récurrent, déclenchement par seuil et comptage ponctuel. Rapprochement avec des politiques de contrôle métier, sans reprendre les écrans ou étapes comme comportements. Ne couvre pas tout Stocktaking ni une taxonomie de capacités ; aucune preuve Beaumanoir. Synthèse, sans reproduction intégrale.

ELM052 reconsulté pour U389 : glossaire BIZBOK 15.0, ©2026, page imprimée 456 (PDF page 4), entrées Business Process, Capability, Capability Behavior ; page 457 (PDF page 5), Capability Instance / Level. Source primaire : https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf . La définition de Behavior traite de la manière d’agir selon les circonstances. Extrait public seulement ; aucune prescription des sept formes FLOW trouvée dans ces entrées.''')
    append('marche/comparaisons.md', '''### CMP145

U389 — Codex, 18 septembre 2026 ; appui méthodologique proposé pour MOD006 et la typologie issue du backlog courant (empreinte dans modeles/backlog/behavior-typology.yaml).

ELM052/BIZBOK éclaire la manière d’agir contextualisée, distincte du niveau de décomposition et du processus comme suite d’activités. ELM234/Microsoft fournit un exemple de régimes de comptage aux effets métier différents. Points communs : circonstances, politiques et pratiques peuvent différencier la réalisation d’une capacité. Adaptation FLOW : une grille de sept formes, déduite de ses 48 comportements sous 13 capacités et enrichie des scopes de visibilité arbitrés en annexe ; pas de correspondance exclusive par nature.

Écart et limite : ni la liste de sept formes ni le niveau terminal Capacité → Comportement ne sont une norme universelle démontrée. Microsoft expose des processus, modalités et fonctions que FLOW sélectionne à sa maille ; tous ne sont pas des comportements. Bénéfice : rendre le critère opérant sans nouveau niveau ni catalogue produit. La règle de documentation est demandée par Laurent ; formulation et rapprochement restent éditoriaux, sans validation globale ni publication.''')
    append('JOURNAL.md', '''## 2026-09-18 — U389 : définition concrète du comportement

Analyse exhaustive des 48 comportements intégrés sous 13 capacités et distinction des scopes de visibilité encore en annexe. MOD006 enrichi de sept formes illustrées ; règle mémorisée dans AGENTS.md, preuve dans modeles/backlog/behavior-typology.yaml. Appui BIZBOK/Microsoft ELM234/CMP145, sans revendication de taxonomie universelle. Catalogue métier et publications inchangés ; liste éditoriale distinguée de l’instruction acquise.''')
    assert sha256(model_path.read_bytes()).hexdigest() == model_hash
    (capture / 'README.md').write_text('# U389 — définition de Comportement\n\nAnalyse et preuve : [annexe](../../modeles/backlog/behavior-typology.yaml). Définition canonique : MOD006 du glossaire méthodologique. Les deux fichiers before conservent les textes antérieurs ; aucune migration métier.\n\nCatalogue inchangé : `' + model_hash + '`. Les 48 comportements sont couverts une fois dans les observations, sous leurs 13 parents explicites.\n', encoding='utf-8')
    print('U389 recorded: 48 behaviors, 13 parents, 7 illustrative forms; business catalog unchanged.')


if __name__ == '__main__':
    main()
