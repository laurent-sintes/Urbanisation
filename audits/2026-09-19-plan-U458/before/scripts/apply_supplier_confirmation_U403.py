"""Integrate Supplier Confirmation and its business explanation, approved U403."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT = ROOT/'modeles/backlog/history/supplier-confirmation-U403'
REFS = ['U403','ELM242','CMP153']


def main():
    assert not OUT.exists(), 'Preserve historical evidence.'
    mp=ROOT/'modeles/backlog/model.yaml'; before=read(mp); model=deepcopy(before)
    ap='modeles/backlog/behavior-gap-audit.yaml'; audit=read(ROOT/ap)
    rp='modeles/backlog/purchase-order-behaviors.yaml'; review=read(ROOT/rp)
    assert not any(n['id']=='BHV078' for n in model['nodes'])
    assert '## U403\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    parent=next(n for n in model['nodes'] if n['id']=='D04.j')
    assert not set(['scope','decomposition_rationale','market_comparisons']) & set(parent['lifecycle']['validated_fields'])
    append('connaissance/01-contributions-utilisateur.md', '''## U403

**id**

U403

**date**

2026-09-19

**titre**

Adopter Supplier Confirmation et conserver une explication détaillée

**texte**

C'est malin. L'explication doit être claire et détaillée comme tu l'expliques. Je valide

**contexte et portée**

Accord sur Supplier Confirmation sous Purchase Order, son nom, sa définition présentée et le mécanisme d’établissement et révision d’un engagement avec le fournisseur. Combinable avec Stock Procurement, Direct Delivery et Service Procurement ; accepter, refuser, proposer et reconfirmer restent des opérations internes au comportement. Conserver l’exemple de 100 pièces demandées vendredi, avec proposition fournisseur de 60 vendredi et 40 mardi. Distinguer demande, réponse, engagement accepté, risque opérationnel et promesse client. Refuser le report ne restaure pas la capacité fournisseur ; accepter son nouvel engagement ne modifie pas automatiquement notre promesse client. Le partage exposé avec Fulfillment Optimization, Order Lifecycle Management, Promise Management, Execution Management et Inventory Management est confirmé. La négociation générale des accords reste distincte ; aucun nouveau comportement de consignation adopté par extension. Les compléments rédactionnels et correspondances marché gardent leur qualification séparée. Poursuite de l’audit existant, aucune publication demandée.''')
    OUT.mkdir()
    for path,name in [(mp,'model-before.yaml'),(ROOT/ap,'behavior-gap-audit-before.yaml'),(ROOT/rp,'purchase-order-review-before.yaml')]:
        (OUT/name).write_bytes(path.read_bytes())
    definition='Prendre en charge l’établissement et les révisions de l’engagement fournisseur sur une commande d’achat, en distinguant la demande, la réponse fournisseur et les conditions finalement acceptées.'
    mechanism='La construction d’un engagement avec une autre partie, qui peut répondre autrement que ce qui lui est demandé.'
    example='On demande 100 pièces vendredi. Le fournisseur propose 60 vendredi et 40 mardi.'
    boundaries=[
        dict(responsibility='Demande initiale, réponse fournisseur et engagement accepté',owner='D04.j',behavior='BHV078'),
        dict(responsibility='Étude des conséquences sur les commandes à satisfaire et des alternatives',owner='D03'),
        dict(responsibility='Application d’un report ou d’une scission autorisée de l’Order',owner='D04.o'),
        dict(responsibility='Modification éventuelle de notre promesse client',owner='D03.n'),
        dict(responsibility='Expédition et réception réellement constatées',owner='D06'),
        dict(responsibility='Enregistrement des effets sur le stock',owner='D01'),
    ]
    scope='''**Mécanisme métier.** Construire et maintenir un engagement avec le fournisseur, qui peut répondre autrement que ce qui lui est demandé. Le comportement couvre la confirmation initiale et les révisions ultérieures. Accepter, refuser, proposer une modification et reconfirmer sont ses opérations ; elles ne constituent pas quatre comportements. Il peut se combiner avec [Stock Procurement](model:BHV058), [Direct Delivery](model:BHV059) et [Service Procurement](model:BHV060).

**Informations à distinguer.** La demande indique ce que l’entreprise attend. La réponse indique ce que le fournisseur accepte, refuse ou propose de réaliser. Les conditions finalement acceptées définissent l’engagement retenu selon les règles applicables. L’historique conserve la demande, les réponses et leurs évolutions pour expliquer les écarts ; une nouvelle annonce ne doit pas effacer ce qui était convenu. Une estimation de réalisation ou une alerte fournisseur peut différer de cet engagement : aucune annonce n’est assimilée automatiquement à un accord ni à une réalisation.

**Exemple fictif : 100 pièces vendredi.** On demande 100 pièces vendredi. Le fournisseur propose 60 vendredi et 40 mardi. Purchase Order / Supplier Confirmation rend lisibles la demande de 100 vendredi, cette réponse fractionnée et l’engagement finalement accepté. Une acceptation partielle ou un refus restent explicables, sans imposer une règle universelle d’acceptation ou de tolérance.

**Conséquences sur les commandes aval.** [Fulfillment Optimization](model:D03) étudie les commandes dépendant de ces apports et les alternatives, en mobilisant ses décisions existantes. Les ressources futures ne sont pas considérées comme du stock physiquement reçu. [Order Lifecycle Management](model:D04.o) applique les mutations autorisées, par exemple un report ou une scission de l’Order. [Promise Management](model:D03.n) conserve la modification éventuelle de notre promesse client. La confirmation reçue du fournisseur et la promesse émise par FLOW sont donc deux engagements distincts.

**Si le report est refusé.** Refuser le report ne rend pas le fournisseur capable de livrer vendredi. Son annonce reste une information de risque à conserver et à prendre en compte dans l’examen des possibilités, même si la modification de l’engagement n’est pas acceptée. Maintenir l’attendu initial ne permet pas de traiter les 100 pièces vendredi comme un apport fiable par simple maintien d’une date dans la commande. Le résultat peut être une recherche d’autre solution ou la mise en évidence d’un risque restant ; aucune modification automatique des engagements n’est déduite de ce constat.

**Si le nouvel engagement est accepté.** Accepter 60 vendredi et 40 mardi ne modifie pas automatiquement la promesse client. Ses conséquences sont examinées par les capacités responsables. L’acceptation fournisseur ne garantit pas non plus la réalisation : [Execution Management](model:D06) conserve les prestations et les faits d’expédition et de réception ; [Inventory Management](model:D01) enregistre leurs effets sur le stock.

**Frontières.** Le périmètre reste la commande d’achat de biens ou de prestations. La négociation générale des accords fournisseurs demeure distincte. Le comportement n’absorbe ni l’optimisation des ressources, ni le cycle de vie transverse, ni la réalisation physique. L’exemple n’établit aucune pratique installée chez Beaumanoir. Portail, échange de messages, API ou intervention humaine sont des moyens possibles, sans comportement distinct par interface ni étape manuelle obligatoire.'''
    sources=[
        dict(id='SC-S1',vendor='Microsoft',product='Dynamics 365 Supply Chain Management',title='Vendor collaboration with external vendors',
            url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors',
            edition='Documentation évolutive ; mise à jour affichée 2025-07-21',locator='Working with POs when vendor collaboration is used ; Changing a PO ; Updating a PO when a vendor suggests changes',
            finding='Le processus distingue envoi de la commande, réponse fournisseur (acceptation, refus, changements) et confirmation, avec versions et historique. Les changements peuvent porter sur quantités, dates et échéanciers.',
            limit='Vendor collaboration couvre plus que ce comportement (notamment RFQ et factures). FLOW conserve le mécanisme d’engagement sur Purchase Order, sans copier l’interface, les étapes manuelles ou tous les statuts produit.',access='Texte primaire ouvert et consulté'),
        dict(id='SC-S2',vendor='Microsoft',product='Dynamics 365 Supply Chain Management',title='Review and accept changes to confirmed purchase orders',
            url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-changes-after-confirmation',
            edition='Documentation évolutive ; mise à jour affichée 2026-07-01',locator='Review changes to confirmed purchase orders ; Step 3, note on direct downstream impacts',
            finding='L’examen de modifications d’achats confirmés s’appuie sur leurs conséquences sur les demandes aval avant reconfirmation et permet des échanges avec le fournisseur.',
            limit='Cette fonction documente les impacts directs, pas tous les impacts indirects. FLOW répartit engagement fournisseur, analyse des possibilités, décision collective et promesse client entre capacités distinctes. Aucune capacité Copilot ou écran créée.',access='Texte primaire ouvert et consulté'),
        dict(id='SC-S3',vendor='SAP',product='SAP S/4HANA Cloud Best Practices / Direct Procurement with Inbound Delivery (2TX)',title='Create Supplier Confirmation (Optional)',
            url='https://help.sap.com/docs/s4hana-cloud-best-practices/direct-procurement-with-inbound-delivery-2tx-hr/create-supplier-confirmation-optional',
            edition='Édition non affichée dans le passage indexé consulté',locator='Enter Reference Purchase Order ; Create Supplier Confirmation Item ; Create Confirmation Line Data',
            finding='Le passage expose une Supplier Confirmation rattachée au Purchase Order, avec date de livraison et quantité confirmées.',
            limit='Appui au nom et aux données d’engagement ; le passage ne démontre pas à lui seul la totalité du mécanisme FLOW, ses révisions et impacts. Supplier Confirmation y est un objet/processus produit, pas une taxonomie de comportements d’entreprise.',access='Passage primaire indexé consulté ; ouverture directe du portail sans texte exploitable'),
    ]
    for source in sources: source['consulted_on']='2026-09-19'
    def comparison(s):
        return dict(vendor=s['vendor'],product=s['product'],element_name=s['title'],element_type='Processus, fonction ou objet produit',
            relationship='Recouvrement partiel',similarities=s['finding'],differences=s['limit'],
            flow_position='Supplier Confirmation est un mécanisme combinable de Purchase Order ; engagement reçu distinct de la promesse client et de la réalisation. Confirmation et révision restent dans un seul comportement.',
            source_title=s['title'],source_url=s['url'],source_version=s['edition'],source_locator=s['locator'],consulted_on=s['consulted_on'],
            evidence_limits=s['access']+' ; aucune preuve de réalisation installée chez Beaumanoir.',status='proposed',source_refs=REFS)
    fields=dict(name='Supplier Confirmation',definition=definition,finality='Fiabiliser les engagements reçus du fournisseur et rendre leurs écarts explicables, sans confondre accord, risque opérationnel et promesse client.',
        scope=scope,market_comparisons=[comparison(s) for s in sources])
    stamp=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def life(values, approved):
        return dict(state='urbanist_validated',recorded_at=stamp,recorded_by='Codex',source_refs=['U403'],validated_fields=approved,
            value_sha256={f:value_hash(values[f]) for f in approved},note='U403 : nom, définition présentée et parent adoptés ; explication détaillée demandée. Compléments rédactionnels et comparaisons qualifiés séparément.')
    node=dict(id='BHV078',revision=1,kind='behavior',layer=parent['layer'],fields=fields,source_refs=REFS,adoption_ids=[],
        source_locator=dict(path='connaissance/01-contributions-utilisateur.md',anchor='u403'),
        review=dict(state='partial',note='Nom, définition, parent et principes expliqués adoptés U403. Finalité et scope développés éditoriaux ; détails de règles non adoptés.'),lifecycle=life(fields,['name','definition']))
    relation=dict(id='REL-BEHAVIOR-BHV078',revision=1,type='contains',source_id='D04.j',target_id='BHV078',source_refs=REFS,
        review=dict(state='accepted',note='Supplier Confirmation sous Purchase Order adopté U403.'))
    relation['lifecycle']=life(relation,['type','source_id','target_id'])
    model['nodes'].append(node);model['relations'].append(relation)
    parent['fields']['scope']+='\n\nU403 : [Supplier Confirmation](model:BHV078) explicite l’établissement et les révisions de l’engagement reçu du fournisseur, en complément des trois parcours. La demande, la réponse et les conditions acceptées restent distinctes. Refuser un report ne restaure pas la capacité fournisseur ; accepter un nouvel engagement ne modifie pas automatiquement notre promesse client. La fiche du comportement détaille le cas de 100 pièces demandées vendredi, puis de 60 vendredi et 40 mardi proposés.'
    parent['fields']['decomposition_rationale']+=' Supplier Confirmation ajoute le mécanisme de construction d’un engagement avec une autre partie, qui peut répondre autrement que demandé : cette différence change le pilotage de l’achat et la fiabilité des ressources attendues. Il se combine avec les trois parcours ; les opérations accepter, refuser et reconfirmer ne sont pas des comportements séparés.'
    parent['fields']['market_comparisons'].extend(comparison(s) for s in sources)
    parent['revision']+=1;parent['source_refs']=list(dict.fromkeys(parent['source_refs']+REFS))
    parent['review']['note']+=' U403 : Supplier Confirmation adopté en complément ; responsabilités et exemple détaillés dans BHV078.'
    new_nodes={n['id']:n for n in model['nodes']}
    for old in before['nodes']:
        for field in old.get('lifecycle',{}).get('validated_fields',[]):
            assert new_nodes[old['id']]['fields'][field]==old['fields'][field]
    assert model['relations'][:-1]==before['relations']
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),delta={},
        adopted_behaviors=[dict(node_id='BHV078',parent_id='D04.j',adopted_fields=['name','definition'],value_sha256=node['lifecycle']['value_sha256'])],behaviors=[])
    for key in ['nodes','relations']:
        old={x['id']:x for x in before[key]};new={x['id']:x for x in model[key]}
        migration['delta'][key]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(new.keys()&old.keys()) if new[i]!=old[i]},removed=sorted(old.keys()-new.keys()))
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit['source_refs'].extend(REFS);audit['implementation_U403']=migration;audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest()
    assessment=next(a for a in audit['assessments'] if a['capability_id']=='D04.j')
    assessment['existing_behaviors'].append('BHV078');assessment['verdict']='trois parcours et engagement fournisseur intégrés U403'
    assessment['diagnosis']=parent['fields']['decomposition_rationale']
    assessment['recommendation']='Supplier Confirmation distingue demande, réponse et engagement accepté, ainsi que risque et promesse client. Consignation reste distincte dans D01.h et D04.r ; aucune extension du comportement par analogie.'
    audit['existing_behavior_review'].append(dict(behavior_id='BHV078',status='integrated_U403',market_sources=['S26'],recommendation='Confirmation et révision reçues du fournisseur sous Purchase Order ; explication détaillée, sources Microsoft/SAP et limites dans la fiche et purchase-order-behaviors.yaml (ELM242/CMP153).'))
    a06=next(a for a in audit['arbitrations'] if a['id']=='A06')
    a06.update(status='responsibility_and_behavior_resolved_U403',recommendation='Supplier Confirmation BHV078 porte l’engagement reçu sur Purchase Order, distinct de Promise Management. Fulfillment Optimization examine les impacts et alternatives ; Lifecycle applique les mutations autorisées. Refuser un report ne rétablit pas la capacité fournisseur.',
        limit='Tolérances, autorités et règles d’acceptation restent à préciser. La négociation générale des accords n’est pas absorbée ; aucune extension automatique à la consignation ou à tous les Orders.')
    save(ap,audit)
    review['source_refs'].extend(REFS)
    review['supplier_confirmation_U403']=dict(status='integrated',node_id='BHV078',parent_id='D04.j',source_refs=REFS,name=fields['name'],definition=definition,
        adopted_explanation=dict(mechanism=mechanism,example=example,boundaries=boundaries,
            rejected_change='Refuser le report ne rend pas le fournisseur capable de livrer vendredi. Son annonce reste une information de risque, même si la modification contractuelle n’est pas acceptée.',
            accepted_change='Accepter le nouvel engagement fournisseur ne modifie pas automatiquement notre promesse client.',
            operations='Accepter, refuser, proposer une modification et reconfirmer restent les opérations de ce comportement.'),
        source_comparisons=sources,editorial_fields=['finality','scope','market_comparisons'],implementation_ref=(OUT/'implementation.yaml').relative_to(ROOT).as_posix())
    save(rp,review)
    append('marche/elements.md', '''### ELM242

19 septembre 2026 — textes primaires Microsoft Dynamics 365 SCM ouverts avant U403 : Vendor collaboration with external vendors (mise à jour 2025-07-21), sections échanges sur PO, réponses et versions ; Review and accept changes to confirmed purchase orders (mise à jour 2026-07-01), modifications et impacts aval directs. SAP S/4HANA Cloud Best Practices, Create Supplier Confirmation (Optional) : passage primaire indexé sur référence au Purchase Order, date et quantité confirmées ; portail ouvert sans texte exploitable, édition non établie.

Nature : processus, fonctions et objet produit. URL, localisateurs, constats et limites dans modeles/backlog/purchase-order-behaviors.yaml, supplier_confirmation_U403.source_comparisons. La source SAP appuie le nom et les données, sans prouver tout le comportement. Aucune taxonomie de capacités ou réalisation Beaumanoir déduite. Synthèses sélectives uniquement.''')
    append('marche/comparaisons.md', '''### CMP153

U403 — Codex, 19 septembre 2026. ELM242 rapproché de Purchase Order D04.j et Supplier Confirmation BHV078 : recouvrement partiel des échanges et du suivi de l’engagement fournisseur ; appui lexical SAP. Le comportement couvre établissement et révision, combinables avec les parcours achat ; son bénéfice est la lisibilité de la demande, de la réponse, de l’engagement accepté et du risque opérationnel. Noms, responsabilité, parent et principes exposés adoptés ; comparaisons et compléments rédactionnels qualifiés séparément.

Vendor collaboration Microsoft est plus large que ce comportement. L’analyse Microsoft consultée couvre les impacts directs, pas tous les effets indirects. FLOW sépare contenu de l’engagement, étude des possibilités/impacts, mutations d’Order et promesse client. Refuser une modification ne rétablit pas la capacité physique du fournisseur ; accepter son engagement ne modifie pas automatiquement le nôtre. Ces frontières expriment le modèle FLOW ; aucun comportement logiciel, taxonomie universelle ou preuve installée prétendu. La négociation générale des accords reste distincte.''')
    append('JOURNAL.md', '''## 2026-09-19 — U403 : Supplier Confirmation

Comportement BHV078 intégré sous Purchase Order avec nom et définition adoptés, exemple 100 vendredi / 60 vendredi + 40 mardi, responsabilités et explication détaillée. Demande, réponse, accord retenu, risque et promesse client distincts ; effets d’un refus ou d’une acceptation expliqués. Sources primaires relues avant la proposition : ELM242/CMP153, limites SAP indexé et impacts Microsoft directs consignées. Audit existant A06 mis à jour ; aucun ancien champ validé ni lien métier modifié, aucune release. Preuves dans modeles/backlog/history/supplier-confirmation-U403.''')
    (OUT/'README.md').write_text('# U403 — intégration Supplier Confirmation\n\nBHV078 sous D04.j. Noms, définition et parent adoptés ; principes et exemple exposés conservés dans l’annexe Purchase Order. Description développée et comparaisons qualifiées séparément. Capture et empreintes pour poursuivre l’audit existant.\n',encoding='utf-8')
    print('U403 integrated: Supplier Confirmation BHV078; detailed explanation and market comparison recorded.')


if __name__=='__main__':
    main()
