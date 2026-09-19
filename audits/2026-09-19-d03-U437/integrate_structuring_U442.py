"""Integrate two instructed proposals, keeping their descriptions unapproved."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps
from scripts.element_versions import content_hash
from scripts.lifecycle import value_hash
path=ROOT/'modeles/backlog/model.yaml';out=Path(__file__).parent/'model-before-structuring-U442.yaml'
assert not out.exists();out.write_bytes(path.read_bytes())
before=read(path);model=deepcopy(before);nd={n['id']:n for n in model['nodes']}
review_path=ROOT/'modeles/backlog/order-structuring-review-U439.yaml';review=read(review_path)
assert not {'BHV086','BHV087'} & nd.keys()
stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
elements=ROOT/'marche/elements.md';comparisons=ROOT/'marche/comparaisons.md'
assert '### ELM256\n' not in elements.read_text(encoding='utf-8')
assert '### CMP167\n' not in comparisons.read_text(encoding='utf-8')
with elements.open('a',encoding='utf-8') as f:
    f.write('''

### ELM256

Oracle E-Business Suite Order Management 12.2 — Line Sets / Fulfillment Sets. Source primaire ouverte le 19 septembre 2026 : https://docs.oracle.com/cd/E26401_01/doc.122/e48843/T335476T336783.htm ; sections Line (Ship or Arrival) Sets, Set Function Details, Fulfillment Sets. Mécanisme produit reliant des lignes d’une même commande sous conditions communes. La portée multi-commandes n’est pas démontrée ; aucun identifiant natif de capacité ni définition normative d’entreprise. Synthèse et limites : modeles/backlog/order-structuring-review-U439.yaml. Aucune réalisation Beaumanoir déduite.

### ELM257

SAP Fashion Management, ERP 6.0 EHP8 SP24 — General Requirements Grouping. Passages primaires indexés consultés le 19 septembre 2026 : https://help.sap.com/docs/SAP_ERP_SPV/f48e74ad3b3740bc8c9eaade394a3c1e/c617f055aa2a6d55e10000000a4450e5.html?locale=en-US&state=PRODUCTION&version=6.18.24 ; Use, Grouping Rule and Grouping Criteria, Individual Group Release Rules. Fonction produit de regroupement de besoins ; ne prouve pas un ensemble transactionnel persistant. Synthèse originale sans reproduction ; limites détaillées dans l’annexe U439.

### ELM258

Infor LN 10.7 Procurement — Commingling purchase orders. Texte primaire ouvert le 19 septembre 2026 : https://docs.infor.com/ln/10.7/en-us/lnolh/help/td/onlinemanual/000321.html ; Header level commingling, Line level commingling, Approval. Fonction produit de fusion de commandes d’achat avant approbation, distincte du seul regroupement logistique. Les règles techniques de suppression et de calcul des prix ne sont pas adoptées dans FLOW. Aucun constat installé ni équivalence universelle aux autres Orders. Synthèse originale ; détails dans l’annexe U439.
''')
with comparisons.open('a',encoding='utf-8') as f:
    f.write('''

### CMP167

U439/U440/U442 — Codex, 19 septembre 2026. Rapprochement proposé d’Order Grouping BHV086, sous Order Structuring D04.n, avec ELM256 et ELM257. Recouvrement partiel : préserver des demandes identifiables et des conditions communes ; portée multi-Orders persistante FLOW à instruire. L’accord ne valide pas les définitions ni les règles détaillées. Pas de comportement par opération d’ajout/retrait d’un membre ; décisions, autorisation de prise en charge et réservation distinctes.

### CMP168

U439/U440/U442 — Codex, 19 septembre 2026. Rapprochement proposé d’Order Merging BHV087, sous Order Structuring D04.n, avec ELM258. Mécanisme de remplacement de plusieurs demandes actives par une demande résultante avec traçabilité. Appui documenté pour les achats avant approbation ; autres intentions, engagements, prix et réalisations à examiner. Microsoft Firm planned orders (ELM251) éclaire une frontière différente : création d’un Order depuis des propositions. Ni regroupement d’expéditions ni généralisation automatique des règles produit.
''')
newrefs={'BHV086':['ELM256','ELM257','CMP167'],'BHV087':['ELM258','ELM251','CMP168']}
for prototype in review['proposed_nodes']:
    n=deepcopy(prototype);n['source_refs']=list(dict.fromkeys(n['source_refs']+newrefs[n['id']]))
    n['last_modified']=stamp
    n['lifecycle']=dict(state='under_instruction',recorded_at=stamp,recorded_by='Codex',source_refs=['U439','U440','U442'],validated_fields=[],value_sha256={},note='Comportement demandé à explorer par Laurent ; nom, définition, conditions et comparaison proposés, aucun accord global déduit.')
    for c in n['fields']['market_comparisons']:
        external={'Oracle':'ELM256','SAP':'ELM257','Infor':'ELM258','Microsoft':'ELM251'}[c['vendor']]
        c['source_refs']=list(dict.fromkeys(c['source_refs']+[external,'CMP167' if n['id']=='BHV086' else 'CMP168']))
    model['nodes'].append(n)
for prototype in review['proposed_parent_relations']:
    r=deepcopy(prototype);r['last_modified']=stamp
    r['lifecycle']=dict(state='under_instruction',recorded_at=stamp,recorded_by='Codex',source_refs=['U440','U442'],validated_fields=[],value_sha256={},note='Rattachement proposé en instruction selon le périmètre demandé ; comportement terminal unique.')
    model['relations'].append(r)
parent=nd['D04.n'];old_definition=parent['fields']['definition']
parent['fields']['definition']='Scinder, regrouper ou fusionner des commandes et leurs éléments, en préservant la traçabilité des demandes, les quantités et les engagements.'
parent['fields']['decomposition_rationale']=review['parent_wording_proposal']['decomposition_rationale']
parent['fields']['scope']='''Trois effets à distinguer : Order Splitting sépare une demande en parties ; Order Grouping relie des demandes qui restent distinctes ; Order Merging remplace des demandes compatibles par une demande résultante. Exemples fictifs : scinder 100 en 60 et 40 ; relier deux transferts nécessaires à une ouverture magasin ; fusionner deux achats encore modifiables de 30 et 20 en une demande de 50.

Les deux derniers comportements et la formulation simplifiée sont proposés à la suite de U439/U440/U442. Les conditions de compatibilité et d’autorisation restent à instruire ; la fusion n’est pas réputée applicable à tous les types et états d’Orders. Les anciennes définitions et leurs accords sont conservés dans la capture préalable.

'''+parent['fields']['scope']
parent['lifecycle']['validated_fields'].remove('definition')
old_approval=parent['lifecycle']['value_sha256'].pop('definition')
parent['lifecycle']['note']+=' U439/U442 : nouvelle définition simplifiée proposée ; ancienne définition adoptée et empreinte conservées dans model-before-structuring-U442.yaml. Le nom adopté reste validé.'
parent['review']['note']+=' U439/U442 : définition reformulée et regroupement/fusion en instruction ; aucune adoption des nouvelles descriptions déduite.'
parent['source_refs']=list(dict.fromkeys(parent['source_refs']+['U439','U440','U442','CMP167','CMP168']))
parent['revision']+=1;parent['last_modified']=stamp
if 'content_sha256' in parent:parent['content_sha256']=content_hash(parent)
for original in before['nodes']:
    current=nd[original['id']]
    for field in original.get('lifecycle',{}).get('validated_fields',[]):
        if original['fields'][field]!=current['fields'][field]:assert original['id']=='D04.n' and field=='definition'
model['source_version']+=' + U439/U442 Structuring clarifié, Grouping et Merging proposés'
for e in model['source_files']:e['sha256']=sha256((ROOT/e['path']).read_bytes()).hexdigest()
path.write_text(dumps(model),encoding='utf-8')
review['status']='integrated_as_proposals_U442'
review['integration']=dict(recorded_at=stamp,model='modeles/backlog/model.yaml',behavior_ids=['BHV086','BHV087'],parent='D04.n',approved_fields=[],definition_proposed=parent['fields']['definition'],previous_approved_definition=old_definition,previous_approved_definition_sha256=old_approval,historical_model=out.relative_to(ROOT).as_posix())
review['integration_notes'][0]='Le catalogue courant fait autorité dans modeles/backlog/model.yaml ; les prototypes de cette annexe conservent la proposition documentée avant intégration.'
review_path.write_text(dumps(review),encoding='utf-8')
print('Structuring clarified; BHV086 Grouping and BHV087 Merging integrated as proposals; historical definition approval preserved.')
