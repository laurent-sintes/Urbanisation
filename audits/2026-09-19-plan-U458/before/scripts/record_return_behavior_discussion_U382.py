"""Record the discussion only; no catalog adoption or behavior creation."""
from pathlib import Path
from scripts.structured_io import read, dumps

contributions = Path('connaissance/01-contributions-utilisateur.md')
text = contributions.read_text(encoding='utf-8')
assert '## U381\n' not in text and '## U382\n' not in text
for identifier, title, quote, scope in [
    ('U381', 'Analyser les comportements de Return Disposition Decision',
     'On peut analyser les comportements possibles de cette nouvelle décision ?',
     'Demande d’analyse de D05.i après U380 ; aucune adoption de comportements.'),
    ('U382', 'Distinguer prises en charge des retours et stratégies de décision',
     "En effet, c'est la capacité de gestion des retour qui doit être décomposée en remise en stock, réparation, renvoi. La Décision doit être décomposée en stratégies.",
     'Orientation explicite : les prises en charge du bien relèvent de la gestion des retours ; les stratégies relèvent de la décision. Les formulations détaillées proposées par Codex restent à discuter. Le catalogue actuel ne possède pas de capacité autonome de gestion complète des retours : D04.l est un comportement d’Order Type centré sur les commandes. Aucun sous-comportement ni nouvelle capacité créé implicitement.')]:
    text += f'\n\n## {identifier}\n\n**id**\n\n{identifier}\n\n**date**\n\n2026-09-18\n\n**titre**\n\n{title}\n\n**texte**\n\n{quote}\n\n**contexte et portée**\n\n{scope}\n'
contributions.write_text(text, encoding='utf-8')

p = Path('modeles/backlog/return-disposition-review.yaml')
review = read(p)
review['behavior_review_U382'] = {
    'status': 'proposed',
    'source_refs': ['U381', 'U382', 'ELM229', 'ELM230', 'CMP141'],
    'user_direction': 'Gestion des retours : prises en charge du produit ; Return Disposition Decision : stratégies qui orientent le choix.',
    'structural_issue': 'D04.l est déjà un comportement d’Order Type limité aux commandes de retour. Ne pas lui ajouter des sous-comportements. Le porteur de la gestion complète du retour et ses liens à D01/D04/D06 restent à instruire.',
    'proposed_decomposition_rationale': 'Distinguer les cas dont la disposition est déterminée par une politique connue des cas nécessitant un arbitrage contextuel entre plusieurs devenirs autorisés ; rendre visibles la standardisation des prises en charge et la récupération de valeur, sans imposer une technologie de décision.',
    'candidates': [
        {'name': 'Policy-based Disposition', 'status': 'proposed',
         'definition': 'Déterminer le devenir du produit par application d’une politique de disposition à son état constaté, sa catégorie et ses conditions de retour.',
         'benefit': 'Rendre les orientations cohérentes et reproductibles lorsque les cas sont connus.',
         'example': 'Exemple fictif : article intact et complet orienté vers remise en stock ; défaut relevant d’un accord fournisseur orienté vers renvoi selon cet accord.',
         'boundary': 'Appliquer une politique au cas ; ni administrer la politique ni inspecter ou réparer le bien. Une règle par défaut ne crée pas un comportement par code.'},
        {'name': 'Value Recovery Optimization', 'status': 'proposed',
         'definition': 'Choisir entre plusieurs devenirs autorisés en comparant la valeur récupérable, les coûts, délais, risques et objectifs applicables dans le contexte.',
         'benefit': 'Éviter une orientation systématique qui dégrade la valeur récupérée lorsque le contexte change.',
         'example': 'Exemple fictif textile : comparer remise en état puis revente, seconde main et renvoi fournisseur, selon coût, délai et potentiel de revente avant la fin de saison.',
         'boundary': 'Les objectifs peuvent être multidimensionnels ; aucun poids imposé. La décision ne réalise pas le traitement, ne calcule pas seule tous les transferts du réseau et n’absorbe pas remboursement ou autorisation commerciale.'}
    ],
    'combination': 'Les stratégies peuvent se combiner : une politique borne les choix, une optimisation les départage. Pas une séquence obligatoire ni une opposition règles/IA.',
    'not_separate_at_this_stage': [
        'Remise en stock, réparation et renvoi : prises en charge, pas stratégies autonomes de décision.',
        'Circularité et rapidité : objectifs ou politiques possibles ; un comportement autonome nécessite un mécanisme distinct démontré.',
        'Choix du site : dimension contextuelle documentée, à articuler avec Stock Redistribution Decision et les décisions D06 plutôt que les dupliquer.',
        'Mode humain, règle, IA ou batch : choix de réalisation, pas stratégie métier par lui-même.'
    ],
    'naming_limit': 'Libellés de travail FLOW ; les sources documentent les mécanismes mais ne démontrent pas un catalogue commun de comportements portant ces deux noms.',
    'market_comparisons': [
        {'vendor': 'Microsoft', 'source_url': 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/specify-how-to-dispose-of-returned-items',
         'source_version': 'Mise à jour affichée 2025-05-07', 'consulted_on': '2026-09-18',
         'source_locator': 'Disposition type, common code et disposition action',
         'similarities': 'Les codes de disposition représentent différentes suites du retour, dont réparation, renvoi fournisseur et revente.',
         'differences': 'La documentation de configuration ne prouve pas un moteur de sélection automatique par état. Les actions mêlent effets physiques et financiers.',
         'flow_position': 'Appui au vocabulaire et à la prise en charge ; le mécanisme Policy-based Disposition reste une interprétation FLOW.', 'status': 'proposed'},
        {'vendor': 'Blue Yonder', 'source_url': 'https://blueyonder.com/solutions/returns-management/smart-disposition',
         'source_version': 'Page produit évolutive, sans édition affichée', 'consulted_on': '2026-09-18',
         'source_locator': 'Intelligent routing ; Customizable reason codes and rules ; Key Benefits',
         'similarities': 'Choix de canal et destination selon règles et contexte, récupération de valeur et coûts.',
         'differences': 'Produit plus large incluant admission et remboursement ; page commerciale sans détail algorithmique ni preuve de déploiement Beaumanoir.',
         'flow_position': 'Appui aux deux mécanismes proposés ; conserver uniquement le choix du devenir logistique dans D05.i.', 'status': 'proposed'},
        {'vendor': 'Manhattan', 'source_url': 'https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management',
         'source_version': 'Page produit évolutive, sans édition affichée', 'consulted_on': '2026-09-18',
         'source_locator': 'Returns Done Right ; Maximize Returns Profitability',
         'similarities': 'Détermination dynamique du lieu de retour pour accélérer la remise en vente.',
         'differences': 'Ne démontre pas à elle seule la sélection de toutes les filières de réparation ou de disposition.',
         'flow_position': 'Le contexte réseau nourrit la stratégie ; frontière à maintenir avec redistribution et exécution.', 'status': 'proposed'}
    ]
}
p.write_text(dumps(review), encoding='utf-8')

with Path('marche/elements.md').open('a', encoding='utf-8') as f:
    f.write('''\n\n### ELM230

18 septembre 2026 ; U381/U382. Pages primaires ouvertes, synthèses sélectives ; édition produit non affichée.

- Blue Yonder, Smart Disposition : Intelligent routing, Customizable reason codes and rules, Key Benefits. https://blueyonder.com/solutions/returns-management/smart-disposition . Nature : présentation produit, règles et optimisation du devenir/destination. Périmètre également commercial, aucune preuve d’algorithme ou de réalisation Beaumanoir.
- Blue Yonder, Returns decisioning: The secret hack to higher recovery and improved margins, 18 février 2026 : Decisioning at any touchpoint is key. https://blueyonder.com/blog/2026/returns-decisioning-the-secret-hack-to-higher-recovery-and-improved-margins . Nature : article éditeur. État, saisonnalité, valeur, coûts et stock éclairent les orientations ; les points du parcours ne sont pas automatiquement des comportements.
- Manhattan, Returns Management : Returns Done Right et Maximize Returns Profitability. https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/returns-management . Nature : page commerciale. Orientation dynamique vers le lieu favorisant la remise en vente ; ne prouve pas un catalogue complet de stratégies de disposition.
- Microsoft ELM229 relu : table des codes et actions, mise à jour affichée 7 mai 2025. Configuration des suites physiques et financières, pas preuve de sélection automatisée.

Interprétation, limites et propositions dans modeles/backlog/return-disposition-review.yaml, behavior_review_U382.
''')
with Path('marche/comparaisons.md').open('a', encoding='utf-8') as f:
    f.write('''\n\n### Intégration CMP140 — U380

Return Disposition Decision intégrée sous D05.i : nom, définition, nature et parent D05 adoptés. Aucun comportement ; contrats et comparaisons proposés. Preuve : audits/2026-09-18-return-disposition-U380/implementation.yaml. Les contrôles passent, dont préservation de 125 fichiers figés.

## CMP141

Codex ; 18 septembre 2026 ; U381/U382 ; ELM229/ELM230 ; D05.i et D04.l après U380. Recouvrement partiel et appui sémantique, statut proposé.

Laurent distingue prises en charge par la gestion des retours et stratégies de décision. Proposition de deux mécanismes combinables : Policy-based Disposition et Value Recovery Optimization. La standardisation des cas connus et l’arbitrage contextuel justifient une décomposition à discuter. Les noms sont des formulations FLOW, pas un catalogue éditeur commun. Les sources produit combinent souvent choix et réalisation, ainsi que des effets commerciaux hors D05.i. Aucun comportement par code, objectif, canal ou opération automatique.

D04.l est déjà un comportement d’Order Type : la gestion des Orders n’est pas la gestion complète du devenir des produits. Le porteur des prises en charge reste à instruire sans quatrième niveau, transfert implicite de D01/D06 ni création automatique. Aucun changement au catalogue dans cette discussion ; pas de validation attribuée aux deux candidats éditoriaux. Analyse : behavior_review_U382 dans modeles/backlog/return-disposition-review.yaml.
''')
print('U381/U382 and proposed comparison recorded; catalog unchanged.')
