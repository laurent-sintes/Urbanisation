"""Application ponctuelle U460/U461 ; les lectures métier générées restent dérivées du YAML."""
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

FOLDER = Path(__file__).resolve().parent


def save(path, value):
    write_text_if_changed(ROOT / path, dumps(value))


def refs(value, *items):
    value.setdefault('source_refs', [])
    for item in items:
        if item not in value['source_refs']:
            value['source_refs'].append(item)


def comparison(vendor, product, name, kind, relation, common, difference, position, url, version, locator, limit, *sources):
    return dict(vendor=vendor, product=product, element_name=name, element_type=kind,
                relationship=relation, similarities=common, differences=difference, flow_position=position,
                source_title=name, source_url=url, source_version=version, source_locator=locator,
                consulted_on='2026-09-19', evidence_limits=limit, status='proposed', source_refs=list(sources))


PRODUCT = comparison(
    'Microsoft', 'Dynamics 365 Supply Chain Management', 'Product information overview', 'Concepts et fonctions produit',
    'Recouvrement partiel', 'Références communes et variantes ; informations produit pouvant provenir de sources externes.',
    'Microsoft couvre aussi la création des maîtres ; FLOW limite ce référentiel à leur projection.',
    'Appui sur un vocabulaire établi, avec une frontière FLOW explicite : recevoir les références sans administrer leurs maîtres.',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information',
    'Documentation évolutive ; mise à jour affichée le 1er juillet 2026',
    'Product definition ; Distribution, export, and import of product data ; Product masters and product variants',
    'Aucune équivalence de maille, liste de dimensions obligatoire ou conformité produit déduite.', 'U460', 'ELM280', 'CMP175')
INGESTION = comparison(
    'Microsoft', 'Dynamics 365 Supply Chain Management — Warehouse management only mode', 'Exchange data between systems',
    'Fonctions de réception de données de référence', 'Recouvrement partiel',
    'Réception de références produit et de variantes, avec identification de leur origine.',
    'La source de maintien configurée dans ce produit ne détermine pas l’autorité métier de FLOW.',
    'Appui sur un mécanisme documenté ; distinguer autorité, émetteur et projection. Aucun flux installé supposé.',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data',
    'Documentation évolutive du mode Warehouse management only ; édition non figée', 'Master and reference data',
    'Contexte produit spécifique ; pas de transposition des entités techniques ni de maître unique imposé à l’entreprise.',
    'U460', 'ELM281', 'CMP176')
UNIT = comparison(
    'GS1', 'GS1 System — aide à l’identification', 'How does serialisation differ from unique identification in the GS1 System?',
    'Distinction d’identification', 'Appui sémantique', 'La combinaison GTIN et numéro de série distingue une instance individuelle.',
    'Product Unit décrit un exemplaire métier ; elle n’impose pas cette convention d’identification.',
    'Appui sémantique sur GS1, sans GTIN obligatoire ni affirmation de conformité au standard.',
    'https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-',
    'FAQ GS1 GO évolutive ; pas une édition complète des spécifications GS1', 'Différence entre identification et sérialisation',
    'Page explicative consultée, pas audit des règles normatives GS1 ni de tous les rôles Article/Container FLOW.',
    'U460', 'ELM282', 'CMP177')
FACT = comparison(
    'Microsoft', 'Dynamics 365 Supply Chain Management', 'Record the receipt of goods on the purchase order',
    'Exemple de réception et document associé', 'Appui sémantique',
    'L’enregistrement d’une réception produit un document de réception identifiable.',
    'Cet exemple ne démontre pas une règle universelle liant tout événement à un document.',
    'Le lien obligatoire fait–document est une convention FLOW ; cet exemple l’illustre sans la prescrire.',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order',
    'Documentation évolutive ; mise à jour affichée le 1er juillet 2026', 'Record receipt of goods, étapes 4 à 7',
    'Exemple de réception de biens ; ni universalité, ni immutabilité, ni règle de correction déduites.',
    'U461', 'ELM285', 'CMP178')

model_path = 'modeles/backlog/model.yaml'
model = read(ROOT / model_path)
nodes = {n['id']: n for n in model['nodes']}
for node_id, entry in [('D08', PRODUCT), ('D08.d', INGESTION)]:
    node = nodes[node_id]
    assert not node['fields'].get('market_comparisons'), 'Ne pas appliquer deux fois'
    node['fields']['market_comparisons'] = [entry]
    node['proposed_fields'].append('market_comparisons')
    refs(node, *entry['source_refs'])
    node['revision'] += 1
commitment = nodes['D03.n']
old = commitment['fields']['market_comparisons'][0]['differences']
assert 'Promise Management' in old
commitment['fields']['market_comparisons'][0]['differences'] = old.replace('Promise Management', 'Fulfillment Commitment')
refs(commitment, 'U460')
refs(commitment['fields']['market_comparisons'][0], 'U460')
commitment['revision'] += 1
model['principles'].append({
    'id': 'PRINCIPLE-MANAGEMENT-FACT-DOCUMENT',
    'statement': 'Tout fait de gestion est associé à un document métier identifié. Ce document peut être un enregistrement structuré, sans fichier PDF. Objet métier, document et fait restent distincts ; cette convention ne fixe ni nombre exact de documents, ni règles de version ou de correction, ni responsabilité d’autorisation.',
    'source_refs': ['U61', 'U461']})
save(model_path, model)

glossary_path = 'modeles/backlog/glossary.yaml'
glossary = read(ROOT / glossary_path)
terms = {t['id']: t for t in glossary['terms']}
contexts = {
    'TER052': 'Supply reçoit ces références depuis leurs autorités externes. La source qui les transmet peut être un relais : elle ne devient pas pour autant l’autorité sur leur contenu. Exemple fictif : une même variante de tee-shirt, bleu taille M, est proposée dans deux catalogues ; elle reste une seule référence de variante et ne désigne pas les exemplaires physiques détenus.',
    'TER057': 'Exemple fictif : un modèle de tee-shirt constitue la référence commune ; bleu taille M en est une déclinaison. Cette référence ne désigne ni une offre de catalogue, ni une pièce physique particulière. Le rôle Article ou Container exprime l’usage métier retenu dans FLOW.',
    'TER058': 'Exemple fictif : bleu taille M est une déclinaison d’un modèle de tee-shirt. Cent pièces de cette déclinaison peuvent partager la même référence de variante ; elles ne deviennent pas une seule Product Unit. Taille et couleur illustrent ce cas, sans imposer ces dimensions à tous les produits.',
    'TER059': 'Exemple fictif : deux tee-shirts bleus taille M sont deux exemplaires physiques de la même variante. Un identifiant de référence partagé ne suffit donc pas à les distinguer individuellement. L’identité de l’exemplaire reste distincte du code-barres ou du support RFID qui permet de la lire.',
    'TER036': 'Dans FLOW, tout fait de gestion est associé à un document métier identifié. Exemple fictif : « 60 pièces reçues vendredi » est le fait ; le document de réception identifié qui le consigne peut être un enregistrement structuré sans PDF. Le document ne se confond ni avec la commande attendue ni avec un message technique.',
    'TER037': 'Un document métier peut être conservé sous forme structurée sans fichier PDF. Exemple fictif : un document de réception identifié consigne le fait « 60 pièces reçues vendredi ». Le document, le fait qu’il consigne et la commande concernée restent des notions distinctes.'}
for term_id, context in contexts.items():
    term = terms[term_id]
    term['context'] = context
    refs(term, 'U461' if term_id in ('TER036', 'TER037') else 'U460')
    term['revision'] = term.get('revision', 1) + 1
for term_id, entry in [('TER059', UNIT), ('TER036', FACT)]:
    assert not terms[term_id].get('market_comparisons')
    terms[term_id]['market_comparisons'] = [entry]
    refs(terms[term_id], *entry['source_refs'])
save(glossary_path, glossary)

pilot_path = 'modeles/backlog/information-pilots-U458.yaml'
pilots = read(ROOT / pilot_path)
refs(pilots, 'U459', 'U460', 'U461')
pilots['status'] = 'document_principle_confirmed_pilot_details_proposed'
pilots['conventions']['established'].append('Tout fait de gestion est associé à un document métier identifié, éventuellement structuré sans PDF (U461). Versions, correction et nombre exact de documents restent à préciser.')
by_pilot = {p['id']: p for p in pilots['pilots']}
purchase = by_pilot['PILOT-PURCHASE']
refs(purchase, 'U460', 'U461')
purchase['open_items'] = ['V0-P03']
purchase['resolved_items'] = ['V0-P01']
receipt = next(i for i in purchase['information_candidates'] if i['name'] == 'Receipt Fact')
receipt['role'] = 'Fait de réception associé à un document métier identifié, à rapprocher de l’attendu (convention U461).'
receipt['essentials'].append('Document métier associé identifié')
purchase['information_candidates'].append({
    'name': 'Receipt Document', 'role': 'Document identifié qui consigne la réception ; peut être structuré sans PDF.',
    'essentials': ['Référence du document', 'Constat de réception consigné', 'Attendus concernés'],
    'granularity': 'Exemple candidat du pilote ; pas un nouveau nœud. Identité, version, correction et nombre exact de documents à instruire.'})
purchase['example'] += ' Le fait « 60 pièces reçues » est associé au document de réception identifié REC-EXEMPLE-01, sous forme structurée dans cet exemple ; ce document ne remplace ni le bon de commande ni l’engagement fournisseur.'

product = by_pilot['PILOT-PRODUCT']
refs(product, 'U460', 'ELM280', 'ELM281', 'ELM282', 'CMP175', 'CMP176', 'CMP177')
product['projection']['missing_information'] = 'Distinguer une référence inconnue d’une indisponibilité physique. Le comportement opérationnel permis en cas de référence absente reste à déterminer par usage.'
product['projection']['validity'] = 'Période ou contexte dans lequel la caractéristique vaut ; distinct du moment de réception de l’information.'
product['projection']['freshness'] = 'Ancienneté de l’information disponible par rapport au besoin métier. Recevoir maintenant une ancienne description ne la rend pas récente ; aucun délai universel ni arrêt automatique des commandes adopté.'
product['information_candidates'] += [
    {'name': 'Reference Origin', 'role': 'Informations de provenance métier de la projection, sans nouveau maître dans Supply.',
     'essentials': ['Autorité déclarée sur le contenu', 'Source qui le transmet', 'Contexte concerné'],
     'granularity': 'Attributs conceptuels à éprouver ; ni application ni identité d’acteur réelle supposée.'},
    {'name': 'Reference Validity', 'role': 'Situer le contenu dans le temps et son contexte d’usage.',
     'essentials': ['Validité applicable lorsqu’elle est connue', 'Moment de réception', 'Fraîcheur requise selon l’usage'],
     'granularity': 'Aucun champ technique obligatoire, seuil universel ou stratégie de conflit imposé.'}]

# Liens de responsabilité candidats, justifiés par le modèle courant ; pas de nouveaux flux.
rows = {
 'PILOT-PURCHASE': [
  ('Attendus d’achat', 'D04.j', 'Établit et maintient', 'Biens ou prestations, quantités, échéances et reste à satisfaire.'),
  ('Résultats de prestation et écarts', 'D07.c', 'Rapproche et qualifie', 'Transmet les faits utiles à Purchase Order ; ne se substitue pas à la réception physique.'),
  ('Document de réception associé au fait', 'D04.j', 'Utilise pour le rapprochement', 'Porteur de production et règles de correction du document à préciser ; aucune propriété exclusive déduite.')],
 'PILOT-PRODUCT': [
  ('Product / Product Variant', 'D08.d', 'Reçoit et actualise la projection', 'L’autorité sur les maîtres reste externe.'),
  ('Référence produit utile à l’achat', 'D04.j', 'Consulte', 'La dépendance publiée ne constitue pas une preuve de flux installé.')],
 'PILOT-COMMITMENT': [
  ('Proposition et engagement de satisfaction', 'D03.n', 'Propose, confirme et révise', 'Quantités, dates et conditions distinctes de la demande ; autorisations détaillées à préciser.')],
 'PILOT-ASSIGNMENT': [
  ('Lien ressource–commande', 'D02.e', 'Établit et modifie selon choix autorisé', 'Ne bloque pas les usages concurrents ; ne choisit pas à nouveau le plan.')],
 'PILOT-RESERVATION': [
  ('Engagement de ressource opposable', 'D02.c', 'Établit', 'Effet de blocage concurrent adopté ; détails de libération et de consommation ouverts.')]
}
for pilot_id, values in rows.items():
    p = by_pilot[pilot_id]
    refs(p, 'U460')
    p['information_responsibilities'] = [dict(information=i, node_ref=n, role=r, boundary=b, status='proposed_reading_of_current_model') for i,n,r,b in values]

cases = [
 ('PILOT-PURCHASE', 'Réception partielle documentée', '100 pièces attendues ; 60 réellement reçues.', 'Le document REC-EXEMPLE-01 consigne le fait de réception ; le rapprochement explique 40 restantes.', 'Une confirmation fournisseur ne constitue pas une réception.', [], ['U391','U461']),
 ('PILOT-PURCHASE', 'Réponse fournisseur différente de la demande', '100 vendredi demandées ; réponse de 60 vendredi et 40 mardi.', 'Demande, réponse et conditions acceptées restent distinguées ; la promesse client ne change pas automatiquement.', 'Qui accepte une révision et comment l’identifier restent à qualifier.', ['V0-P03'], ['U391','U443']),
 ('PILOT-PURCHASE', 'Achat d’une prestation', 'Une prestation achetée est annoncée terminée ; un écart est constaté.', 'Purchase Order conserve l’attendu d’achat ; Service Reconciliation qualifie le résultat. Le fait de gestion est associé à un document identifié.', 'Ne pas transformer une prestation en quantité de stock ; le document métier exact reste à qualifier.', ['V0-P03'], ['U391','U461']),
 ('PILOT-PRODUCT', 'Une variante dans deux catalogues', 'Un tee-shirt bleu M est proposé dans deux catalogues ; deux exemplaires physiques sont présents.', 'Une même référence de variante peut servir aux offres ; les deux exemplaires restent deux Product Units.', 'Ni identité individuelle déduite du catalogue, ni fusion d’exemplaires.', [], ['U191','U193','U202']),
 ('PILOT-PRODUCT', 'Deux descriptions contradictoires', 'Deux sources transmettent des caractéristiques incompatibles pour la même référence.', 'Distinguer autorité métier et émetteur rend la question visible ; le pilote ne choisit pas le gagnant.', 'Aucun écrasement automatique par le dernier message ni arbitrage maître confié à Supply.', ['V0-P02'], ['U134','U460']),
 ('PILOT-PRODUCT', 'Information reçue récemment mais ancienne', 'Une description datée de lundi est reçue vendredi pour un usage samedi.', 'Réception, validité et fraîcheur utile sont trois questions distinctes ; il faut qualifier l’usage.', 'Aucune durée de fraîcheur ni autorisation de poursuivre inventée.', ['V0-P02'], ['U460']),
 ('PILOT-COMMITMENT', 'Proposition sans confirmation', '60 vendredi et 40 lundi sont proposés pour une demande de 100 vendredi.', 'Les possibilités et la proposition n’établissent pas seules un engagement confirmé.', 'La confirmation ne produit pas implicitement une réservation.', [], ['U441','U443','U436']),
 ('PILOT-COMMITMENT', 'Changement de ressource à conditions constantes', 'L’arrivage B remplace A avec les mêmes quantités, dates et conditions de satisfaction.', 'L’affectation change ; l’engagement de satisfaction peut rester identique.', 'La compatibilité des conditions doit être vérifiée ; aucune nouvelle autorisation générale déduite.', [], ['U443']),
 ('PILOT-COMMITMENT', 'Retard sans changement de ressource', 'La même ressource reste affectée, mais un retard compromet la date promise.', 'Le retard appelle le réexamen de l’engagement, sans effacer la demande ni modifier automatiquement la promesse.', 'L’autorité qui accepte ou refuse la révision reste à préciser.', ['V0-P03'], ['U443']),
 ('PILOT-ASSIGNMENT', 'Affectation sans réservation', '40 pièces d’un arrivage sont affectées à la commande A ; B les demande aussi.', 'L’affectation seule ne donne pas à A un droit opposable à B.', 'La politique d’arbitrage reste distincte ; ne pas annoncer une disponibilité physique garantie.', [], ['U436']),
 ('PILOT-ASSIGNMENT', 'Affectation gelée', 'Une modification de l’affectation est interdite dans le scénario.', 'Le gel protège la modification du lien ; il ne devient pas une réservation de ressource.', 'Le gel n’interdit pas à lui seul tout usage concurrent.', [], ['U364','U436']),
 ('PILOT-ASSIGNMENT', 'Plan recalculé', 'Un nouveau plan recommande de remplacer A par B.', 'La recommandation et son application aux liens ressource–commande restent distinctes.', 'Les conditions de prise en compte et les effets sur les Orders sont à préciser.', ['V0-A02'], ['U443']),
 ('PILOT-RESERVATION', 'Quantité réservée sans lot individuel', '40 pièces d’un périmètre de ressource sont réservées ; le lot précis n’est pas encore affecté.', 'La réservation peut être opposable avant la désignation d’un lot précis.', 'Pas d’affectation physique ni de mouvement de stock déduits.', [], ['U436']),
 ('PILOT-RESERVATION', 'Échéance dépassée', 'Une réservation existe ; l’échéance demandée est dépassée.', 'Il faut une règle explicite pour décider du maintien, de l’expiration ou de la libération.', 'Aucune libération automatique déduite de la seule date.', ['V0-A01','V0-A06'], ['U436']),
 ('PILOT-RESERVATION', 'Commande annulée', 'L’annulation d’une commande bénéficiant d’une réservation est demandée.', 'Distinguer autorisation d’annulation, évolution de la commande et devenir de l’engagement de ressource.', 'Le devenir de la réservation et ses conditions d’application restent à préciser.', ['V0-A01','V0-A02','V0-A06'], ['U436'])
]
pilots['review_U460'] = {
    'qualification': 'Quinze cas fictifs analysés sur les responsabilités courantes ; revue documentaire Codex, pas recette PO/expert ni validation humaine. Les suites ouvertes restent explicitement visibles.',
    'cases': [dict(id=f'CASE-{i:02d}', pilot=p, title=t, given=g, reading=r, boundary=b,
                   status='business_rule_open' if o else 'boundary_explained', open_items=o, source_refs=s)
              for i,(p,t,g,r,b,o,s) in enumerate(cases,1)],
    'next_step': 'Relire les cinq fiches avec PO et expert ; instruire V0-P02/P03 et les règles ciblées sans bloquer la description des frontières déjà établies. Lot 4 : contrat minimal et navigation des informations, sans généralisation anticipée.'}
pilots['market_support']['current_refs'] = ['CMP175','CMP176','CMP177','CMP178','ELM283','ELM284']
pilots['market_support']['scope_U461'] = 'Le document de réception Microsoft illustre le lien fait–document ; ni ce cas ni le tutoriel ArchiMate ne rendent la convention FLOW universelle.'
save(pilot_path, pilots)

readiness_path = 'modeles/backlog/v0-readiness.yaml'
readiness = read(ROOT / readiness_path)
refs(readiness, 'U460', 'U461')
readiness['status'] = 'plan_U458_lot_3_document_convention_resolved_pilots_deepened'
q = next(x for x in readiness['decisions'] if x['id']=='V0-P01')
q['status'] = 'principle_resolved_U461'
q['adopted_statement'] = 'Tout fait de gestion est associé à un document métier identifié, qui peut être un enregistrement structuré sans PDF.'
q['remaining'] = 'Versions, correction, nombre exact de documents et responsabilités d’autorisation ne sont pas fixés par U461 ; détail des identités suivi dans V0-P03.'
q.pop('recommendation', None)
refs(q, 'U61', 'U461')
q = next(x for x in readiness['decisions'] if x['id']=='V0-P03')
q['status'] = 'to_instruct_on_pilot_examples'
lot = next(x for x in readiness['execution_U458']['lots'] if x['lot']==3)
lot['status'] = 'document_convention_resolved_five_pilots_deepened_for_review'
lot['remaining'] = 'Relecture PO/expert des cinq fiches et quinze cas ; autorités de projection et détail des engagements à préciser. La préparation documentaire ne vaut pas recette humaine.'
readiness['implemented'].append({'id': 'V0-U460-PILOTS',
    'result': 'Cinq pilotes enrichis de responsabilités sur les informations et de quinze cas. Quatre rapprochements marché ajoutés, six contextes de glossaire explicités et nom canonique corrigé dans une comparaison.',
    'qualification': 'U461 confirme seulement le principe fait–document ; informations candidates, exemples et comparaisons restent proposés. Aucun nouveau nœud ni lien canonique.'})
readiness['execution_U458']['follow_up_U460'] = {
    'report': 'audits/2026-09-19-pilotes-U460/rapport.md',
    'review': 'audits/2026-09-19-pilotes-U460/pilotes.md',
    'arbitration': 'V0-P01 résolu au niveau du principe par U461 ; V0-P02/P03 et les détails V0-A01/A02/A06 restent ouverts.'}
save(readiness_path, readiness)

guide_path = 'modeles/backlog/modeling-guide-U458.yaml'
guide = read(ROOT / guide_path)
(FOLDER / 'before/modeling-guide-U458.yaml').write_bytes((ROOT / guide_path).read_bytes())
refs(guide, 'U461')
guide['sources'].append({'id': 'U461', 'title': 'Lien fait de gestion–document confirmé',
    'excerpt': 'Oui, conserver le lien fait–document',
    'scope': 'Réponse du 19 septembre 2026 : tout fait de gestion est associé à un document métier identifié, éventuellement structuré sans PDF. Versions, correction et nombre exact de documents non adoptés par extension.'})
lesson = next(x for x in guide['lessons'] if x['id']=='business-objects')
lesson['established_at'] = '2026-09-19'
lesson['rule'] = 'Objet métier, document et fait de gestion restent distincts. Dans FLOW, tout fait de gestion est associé à un document métier identifié, éventuellement structuré sans PDF ; aucun n’est un sous-comportement.'
lesson['scene']['caption'] = 'Exemple fictif : le document de réception identifié consigne le fait ; la commande porte ce qui était attendu.'
lesson['scene']['items'] = [{'label':'Objet métier','text':'La commande d’achat attendue'}, {'label':'Document','text':'Le document de réception REC-EXEMPLE-01'}, {'label':'Fait de gestion','text':'60 pièces reçues vendredi'}]
lesson['explanation'] += ' Un document métier peut être un enregistrement structuré sans PDF. La convention FLOW relie chaque fait de gestion à un document identifié.'
lesson['contributor']['boundary'] = 'Le lien fait–document est requis dans FLOW ; il ne fixe ni nombre exact de documents, ni règles de version/correction, ni propriétaire unique. Ces détails se précisent selon le contexte.'
lesson['contributor']['scope'] = 'U461 confirme le lien fait–document. Exemple et formulation pédagogique proposés ; aucun objet canonique ajouté, aucune autre convention de cycle de vie adoptée.'
refs(lesson['contributor'], 'U461')
save(guide_path, guide)
print('U460/U461 appliqués : 3 nœuds, 1 principe, 6 contextes, 4 comparaisons nouvelles ; 5 pilotes, 15 cas et guide brouillon.')
