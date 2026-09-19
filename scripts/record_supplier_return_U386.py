"""Record a market-backed Supplier Return proposal; leave the catalog unchanged."""
from pathlib import Path
from scripts.structured_io import dumps

ROOT = Path(__file__).resolve().parents[1]


def append(path, text):
    with (ROOT / path).open('a', encoding='utf-8') as f:
        f.write('\n\n' + text.strip() + '\n')


def main():
    target = ROOT / 'modeles/backlog/supplier-return-behaviors.yaml'
    assert not target.exists()
    assert '## U386\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U386

**id**

U386

**date**

2026-09-18

**titre**

Poursuivre la décomposition des Orders après Customer Return

**texte**

next

**contexte et portée**

Demande de poursuivre après l’intégration U385. Codex examine Supplier Return, directement lié au parcours Return to Supplier de Customer Return. Deux comportements sont proposés : Return for Credit et Return for Replacement. Return for Repair est documenté comme candidat conditionnel à la frontière avec l’achat et l’exécution d’une prestation. Aucune validation de ces propositions ni modification du catalogue par cette demande.''')
    urls = {
        'ms': 'https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-process-purchase-returns-cancellations',
        'sap': 'https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d9b97f7722d1014a974a1fa1d11fd10.html',
        'oracle': 'https://docs.oracle.com/en/cloud/saas/readiness/scm/25a/inv25a/25A-inventory-wn-f35542.htm',
        'repair': 'https://docs.oracle.com/cd/E18727-01/doc.121/e13338/T515331T515340.htm'}
    comparisons = []
    evidence = [
        ('Microsoft', 'Dynamics 365 Business Central', 'Purchase return order / replacement purchase order', urls['ms'], 'Documentation évolutive', 'Create a replacement purchase order from a purchase return order ; introduction',
         'Le retour peut être associé à un avoir ; un remplacement peut générer une commande d’achat distincte.',
         'Fonctions produit mêlant logistique et comptabilité ; ne pas attribuer cette documentation Business Central à Dynamics 365 SCM. La nouvelle commande est un choix produit, pas une obligation FLOW.', 'Page primaire ouverte.'),
        ('SAP', 'Business ByDesign', 'Create a New Return to Supplier', urls['sap'], 'May 2026 affiché dans le passage primaire indexé', 'Overview ; Create a Return to Supplier in Purchasing',
         'Suites : avoir, remplacement ou combinaison partielle. Le remplacement modifie le reste à livrer de l’achat ; la seule émission d’un avoir ne crée pas ce même attendu.',
         'Documentation ByDesign, pas S/4HANA. Restrictions particulières au scénario tiers ; séparation de vues acheteur/logistique non imposée à l’organisation FLOW.', 'Texte primaire indexé effectivement consulté ; ouverture directe sans contenu exploitable.'),
        ('Oracle', 'Fusion Cloud SCM — Receiving', 'Return to Supplier for Credit Only', urls['oracle'], '25A', 'Présentation de la fonctionnalité Return for credit',
         'Retour pour avoir sans remplacement attendu : conserver la commande d’achat fermée aux réceptions futures, plutôt que la rouvrir.',
         'Effet produit sur une commande existante ; FLOW retient la différence d’attendu Supply sans imposer cette mécanique de statut ou absorber la comptabilité.', 'Page primaire ouverte.'),
        ('Oracle', 'E-Business Suite — Service Parts Planning', 'Repair at sourcing / Repair-Return', urls['repair'], 'Release 12.1, référence historique', 'Repair at sourcing ; documents du scénario Pull or Repair-Return',
         'La réparation externe peut mobiliser un achat au réparateur et des documents de mouvement du bien.',
         'Planification de pièces de service et réparation, pas preuve d’un comportement de retour fournisseur dans Oracle Fusion ou dans le retail FLOW.', 'Passage primaire indexé consulté ; référence historique limitée à son périmètre.')]
    for vendor, product, label, url, version, locator, common, difference, access in evidence:
        comparisons.append(dict(vendor=vendor, product=product, element_name=label, element_type='Processus et fonctions produit', relationship='Recouvrement partiel',
            similarities=common, differences=difference, flow_position='Éclairer les mécanismes et leurs frontières, sans importer les étapes, statuts ou documents produit comme capacités.',
            source_title=label, source_url=url, source_version=version, source_locator=locator, consulted_on='2026-09-18',
            evidence_limits=access+' Aucune réalisation Beaumanoir déduite.', status='proposed', source_refs=['U386','ELM233','CMP144']))
    review = dict(id='SUPPLIER-RETURN-BEHAVIORS-U386', status='proposed', source_refs=['U386','ELM233','CMP144'], capability_id='D04.m',
        proposed_definition='Prendre en charge les retours de marchandises aux fournisseurs et suivre leurs suites attendues, selon les accords applicables, en distinguant renvoi, remplacement et règlement financier.',
        decomposition_rationale='Le retour sans remplacement éteint l’attente de marchandises au titre des quantités reprises ; le retour avec remplacement conserve un apport attendu. Cette différence change le suivi des quantités, des dates et des engagements aval. Elle justifie deux parcours métier, indépendamment des motifs du retour et des interfaces.',
        proposals=[
            dict(id='SR-P01', name='Return for Credit', status='proposed', parent_id='D04.m',
                definition='Prendre en charge un retour fournisseur donnant lieu à un avoir ou remboursement attendu, sans remplacement des marchandises retournées.',
                mechanism='Suivre le renvoi et son acceptation, matérialiser l’absence de remplacement attendu pour les quantités concernées et relier les références du règlement financier géré ailleurs.',
                benefit='Éviter de compter un apport de remplacement inexistant dans les stocks futurs ou de rouvrir à tort un reste à recevoir.',
                example='Exemple fictif : 100 pièces invendues sont reprises en fin de saison contre avoir. Elles sortent du stock ; aucun arrivage de remplacement n’est attendu pour ces 100 pièces.',
                boundary='Accord de reprise consommé, non négocié ici ; finance émet, comptabilise et rapproche l’avoir. Retour expédié, accepté et financièrement réglé restent distincts. Ne pas confondre avec Credit only côté client, qui peut ne comporter aucun retour physique.'),
            dict(id='SR-P02', name='Return for Replacement', status='proposed', parent_id='D04.m',
                definition='Prendre en charge un retour fournisseur associé à un remplacement attendu, en conservant les liens entre marchandises renvoyées et apports de remplacement.',
                mechanism='Suivre les quantités et dates de remplacement convenues, leurs révisions et leurs réceptions via Purchase Order ; rapprocher sortant et entrant sans les compter deux fois.',
                benefit='Rendre visible le besoin de remplacement restant et ses conséquences possibles sur les promesses, sans confondre expédition du retour et satisfaction du besoin.',
                example='Exemple fictif : 20 pièces défectueuses sont renvoyées. Le fournisseur doit les remplacer ; 12 arrivent et 8 restent attendues.',
                boundary='Purchase Order porte l’apport attendu ; le marché utilise selon le produit une nouvelle commande liée ou le rétablissement d’un attendu sur la commande initiale. Aucun choix documentaire imposé. La date convenue ne vaut pas réception, ni disponibilité opposable automatique pour ATP.')],
        conditional_candidate=dict(name='Return for Repair', status='boundary_to_review',
            definition='Prendre en charge l’envoi d’un bien au fournisseur pour réparation puis sa récupération, en préservant son identité et l’attendu de restitution.',
            benefit='Distinguer retour du même bien réparé et fourniture d’un autre produit de remplacement.',
            issue='Si le fournisseur reprend le bien au titre de son obligation d’origine, le rattachement à Supplier Return est plausible. Si une prestation est achetée à un réparateur, Purchase Order et les Service Orders D06 peuvent porter le mécanisme. Le seul lieu physique fournisseur ne tranche pas la responsabilité.',
            recommendation='Conserver comme candidat documenté sans le créer sous Supplier Return avant clarification du périmètre.', source_refs=['ELM233','CMP144']),
        combination='Un même retour peut associer avoir pour certaines quantités et remplacement pour d’autres. Pas de comportement autonome pour cette combinaison partielle.',
        shared_functions=['Référence à l’achat, à la réception et au retour client lorsque connus.', 'Autorisation de retour fournisseur/RMA selon le cas ; aucune obligation universelle de document.', 'Quantités, dates, destinataire, avancement et preuves de réception.', 'Mutations par Lifecycle, composition par Structuring, conservation par Archiving ; exécution D06 et stocks D01.'],
        not_behaviors=['Défaut, erreur de livraison, excédent et fin de saison sont des motifs ; ils ne suffisent pas seuls à justifier un parcours différent.', 'Saisie, émission, consultation, annulation et traitement en masse restent fonctions ou modalités.', 'La compensation financière sans renvoi physique ne crée pas un flux de retour fictif.'],
        naming='Return for Credit reprend le vocabulaire Oracle ; Return for Replacement est une formulation explicite cohérente avec replacement delivery SAP et replacement purchase order Microsoft. Aucun catalogue universel de comportements revendiqué.',
        market_comparisons=comparisons)
    target.write_text(dumps(review),encoding='utf-8')
    append('marche/elements.md', '''### ELM233

18 septembre 2026 ; U386 ; Supplier Return. Sources primaires et périmètres distincts :

- Microsoft Dynamics 365 Business Central, Process purchase returns or cancellations, page évolutive ouverte : introduction et Create a replacement purchase order from a purchase return order. https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-process-purchase-returns-cancellations .
- SAP Business ByDesign, Create a New Return to Supplier, édition May 2026 affichée dans le passage indexé : Overview et Create a Return to Supplier in Purchasing. https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d9b97f7722d1014a974a1fa1d11fd10.html . Texte primaire indexé consulté, portail direct vide ; avoir, remplacement et combinaison partielle.
- Oracle Fusion Cloud SCM Receiving 25A, Return to Supplier for Credit Only, présentation ouverte. https://docs.oracle.com/en/cloud/saas/readiness/scm/25a/inv25a/25A-inventory-wn-f35542.htm . Ne pas rouvrir l’achat aux réceptions lorsqu’aucun remplacement n’est attendu.
- Oracle EBS Service Parts Planning 12.1, Repair at sourcing / Repair-Return : passage primaire indexé consulté. https://docs.oracle.com/cd/E18727-01/doc.121/e13338/T515331T515340.htm . Réparation externe avec achat et mouvements ; référence historique, pas Oracle Fusion ni un périmètre retail démontré.

Nature : configurations, processus et effets produit ; synthèses sélectives, aucune preuve de déploiement Beaumanoir. Détails et limites dans modeles/backlog/supplier-return-behaviors.yaml.''')
    append('marche/comparaisons.md', '''## CMP144

Codex ; 18 septembre 2026 ; U386 ; ELM233 ; D04.m Supplier Return après U385. Recouvrement partiel ; statut proposé, aucun comportement créé.

Proposition de deux parcours : Return for Credit sans remplacement attendu, et Return for Replacement avec maintien d’un apport de remplacement. Oracle explicite l’effet sur les réceptions futures ; SAP ByDesign distingue avoir, remplacement et mélange par quantité ; Microsoft Business Central produit une commande de remplacement liée. FLOW conserve cette différence d’attendu Supply, sans imposer l’objet technique, la réouverture d’un statut ou reprendre le règlement comptable. Motifs, opérations et interfaces ne deviennent pas des comportements.

Return for Repair demeure conditionnel : une reprise au titre de l’obligation du fournisseur et un achat de prestation à un réparateur ne sont pas automatiquement la même responsabilité. Oracle EBS documente la réparation externe via achat et mouvements, sans prouver son rattachement à un Supplier Return FLOW. Proposition et exemples : modeles/backlog/supplier-return-behaviors.yaml. Aucun accord implicite sur la définition élargie, les noms ou les contrats.''')
    print('U386: Supplier Return proposal recorded; catalog unchanged.')


if __name__ == '__main__':
    main()
