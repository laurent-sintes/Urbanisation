"""Close P01-P03 within the existing Replenishment Decision scope."""
from copy import deepcopy
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read
from scripts.lifecycle import value_hash

OUT=ROOT/'modeles/backlog/history/replenishment-closure-U425'
REFS=['U425','ELM252','CMP163']
CANDIDATES=['P01','P02','P03']


def main():
    assert not OUT.exists()
    assert '## U425\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md','## U425\n\n**id**\n\nU425\n\n**date**\n\n2026-09-19\n\n**titre**\n\nClore les candidats de réassort sans décomposition supplémentaire\n\n**texte**\n\nGo\n\n**contexte et portée**\n\nAccord sur la proposition de clore P01, P02 et P03 comme couverts par Replenishment Decision D05.e : besoins datés, seuil/cible et ajustement des apports existants restent décrits dans la capacité, sans nouveau comportement. Inventory Target Decision détermine les objectifs et seuils, Replenishment Decision recommande les apports et ajustements, Order Management/Lifecycle applique les changements autorisés et D06 orchestre leur réalisation. Descriptions développées et correspondances produit gardent leur portée éditoriale. Aucun constat de couverture exhaustive du marché ni déploiement Beaumanoir déduit.')
    OUT.mkdir()
    for path,name in [('modeles/backlog/model.yaml','model-before.yaml'),('modeles/backlog/behavior-gap-audit.yaml','audit-before.yaml'),('modeles/backlog/d05-refactoring.yaml','d05-before.yaml'),('AGENTS.md','AGENTS-before.md')]:
        (OUT/name).write_bytes((ROOT/path).read_bytes())
    mp=ROOT/'modeles/backlog/model.yaml';before=read(mp);model=deepcopy(before)
    node=next(n for n in model['nodes'] if n['id']=='D05.e');f=node['fields']
    f['scope']='''Décider les apports de [réassort](glossary:TER080) après la constitution du stock de départ. Chez Beaumanoir, l’alimentation continue des magasins est guidée par des seuils ; la cadence de révision, les formules et le degré d’automatisation ne sont pas imposés par ce constat. Le réapprovisionnement continu peut aussi concerner les stocks du réseau et les compléments fournisseur déjà couverts par cette capacité.

**Politique selon les besoins datés.** Déterminer les apports nécessaires à partir des besoins nets et de leurs dates. Les besoins peuvent être traités individuellement ou regroupés dans une période lorsque les contraintes le permettent ; cette agrégation ne justifie pas un comportement par cadence. Exemple fictif : 120 pièces nécessaires à J+7, 70 utilisables et 20 attendues à temps conduisent à examiner un apport complémentaire de 30, avant contraintes de lot et de délai.

**Politique selon un seuil et une cible.** Déterminer l’apport lorsqu’une position de stock projetée passe sous le seuil applicable, pour retrouver la cible retenue. Exemple fictif : position projetée de 50, seuil de 60 et cible de 100 conduisent à proposer 50 en l’absence d’autres besoins ou restrictions. Si les apports doivent être des multiples de 12, examiner 60 et l’excédent associé. Il ne s’agit pas d’une formule Min/Max universelle.

[Inventory Target Decision](model:D05.a) détermine les objectifs et seuils, qui peuvent dépendre des besoins et varier par produit, lieu et période ; ils ne sont pas présumés stables ou indépendants de la demande. [Supply Protection](model:D02.b) gouverne et applique les versions opérationnelles de ces paramètres. Replenishment Decision les utilise pour déterminer les quantités et dates d’apport. Les deux politiques ci-dessus ne forment pas une chaîne où les apports calculés par la première détermineraient les seuils de la seconde.

Dans les deux politiques, évaluer le stock admissible, les entrées attendues à temps, les actions déjà engagées et les contraintes. Préciser l’horizon, la maille et les règles d’admissibilité ; ne pas déduire deux fois des demandes déjà intégrées à une cible ou couvrir deux fois le même manque. Une décision intègre ses calculs ; aucune capacité Calculation autonome.

**Ajustement des apports existants.** Réexaminer les apports prévus ou engagés lorsqu’évoluent besoins, cibles ou contraintes. Recommander une augmentation, une réduction, une avance, un report ou, si pertinent, une annulation admissible ; ce n’est pas un mécanisme limité à la création de commandes supplémentaires. Exemple fictif : la cible passe de 100 à 80, alors que 30 pièces sont présentes et 70 attendues. Examiner une réduction ou un report de 20. Si l’engagement fournisseur empêche la modification, expliciter l’excédent résiduel et les options encore possibles. Aucune modification d’un Order ferme n’est déduite du seul recalcul.

[Initial Stocking Decision](model:D05.g) conserve les apports de lancement. Le réassort tient compte des apports d’implantation encore attendus, sans les recréer. [Stock Redistribution Decision](model:D05.c) examine le rééquilibrage du stock existant ; coordonner les résultats pour éviter les doublons. Un transfert peut matérialiser un apport courant ou une redistribution selon sa finalité.

Les résultats précisent quantités, dates et ajustements recommandés. [Order Management](model:D04) et [Order Lifecycle Management](model:D04.o) vérifient et appliquent les changements autorisés, avec les accords et protections applicables. [Order Backlog Management](model:D03) décide de la satisfaction des demandes et D06 orchestre les services et leur adaptation. La recommandation ne crée ni promesse, ni modification automatique d’un Order, ni mouvement physique. Une application automatisée reste possible selon les règles et autorités ; le porteur détaillé du déclenchement reste à préciser.

U425 clôt P01, P02 et P03 comme couverts par cette responsabilité. Besoins datés et seuil/cible sont des politiques descriptives ; l’ajustement des apports est une faculté transverse. Leur existence dans les produits ne démontre pas un bénéfice justifiant trois comportements supplémentaires. Aucun nouveau comportement créé ; cette clôture ciblée ne prétend pas couvrir toutes les méthodes du marché.'''
    for c in f.get('market_comparisons',[]):
        if 'U324/C98' in c.get('flow_position',''):
            c['flow_position']='U425 clôt la proposition de décomposition : les politiques restent descriptives dans Replenishment Decision. Inventory Target Decision détermine les cibles et seuils variables, Supply Protection gouverne/applique leurs paramètres, Replenishment Decision détermine les apports et ajustements. Les contraintes produit ne prescrivent pas notre découpage.'
            c['source_refs']=list(dict.fromkeys(c['source_refs']+['U425']))
    for title,url,date,locator,common,diff in [
        ('Coverage settings','https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/coverage-settings','2026-03-25','Coverage codes','Per requirement, Per period et Min/Max décrivent des méthodes distinctes de réapprovisionnement et de dimensionnement des lots.','FLOW conserve ces politiques dans une capacité de décision, sans comportement automatique par méthode. La page présente aussi Priority et Decoupling point : leur présence ne valide pas leur adoption ni une couverture exhaustive par cet arbitrage.'),
        ('Action messages','https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/action-messages','2026-03-26','Introduction ; Select action messages','Les changements de besoins conduisent à des suggestions d’avance, report, augmentation et diminution des ordres existants.','FLOW distingue recommandation, vérification/application autorisée et réalisation. La recommandation d’annulation dans FLOW ne présume pas un code Cancel dans cette liste Microsoft.')]:
        f.setdefault('market_comparisons',[]).append(dict(vendor='Microsoft',product='Dynamics 365 Supply Chain Management',element_name=title,element_type='Méthodes et recommandations produit',relationship='Recouvrement partiel',similarities=common,differences=diff,flow_position='U425 : P01/P02/P03 couverts par D05.e sans nouveau comportement ; comparaisons détaillées éditoriales.',source_title=title,source_url=url,source_version=date,source_locator=locator,consulted_on='2026-09-19',evidence_limits='Page primaire consultée ; aucune preuve de déploiement Beaumanoir ni alignement de taxonomie imposé.',status='proposed',source_refs=REFS))
    node['revision']+=1;node['source_refs']=list(dict.fromkeys(node['source_refs']+REFS))
    node['review']['note']+=' U425 clôt les candidats P01–P03 comme couverts ; descriptions et rapprochements développés restent éditoriaux.'
    save('modeles/backlog/model.yaml',model)
    migration=dict(source_refs=REFS,model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),behaviors=[],closed_candidates=CANDIDATES,delta=dict(nodes=dict(added={},removed=[],changed={'D05.e':value_hash(node)}),relations=dict(added={},removed=[],changed={})))
    save((OUT/'implementation.yaml').relative_to(ROOT),migration)
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml');audit['implementation_U425']=migration;audit['baseline']['sha256']=sha256(mp.read_bytes()).hexdigest();audit['source_refs']=list(dict.fromkeys(audit['source_refs']+REFS))
    for p in audit['candidates']:
        if p['id'] in CANDIDATES:
            p['previous_status_U425']=p['status'];p['status']='covered_by_existing_U425';p['covered_by']='D05.e';p['source_refs']=list(dict.fromkeys(p['source_refs']+REFS))
            p['review_note']='U425 : clôturé comme couvert par Replenishment Decision. Politique ou faculté descriptive, sans nouveau comportement. Formulation et question initiales conservées pour provenance ; pas un arbitrage encore ouvert.'
            p['resolution']=dict(source_ref='U425',decision='covered_by_existing_capability',new_behavior=False)
    a=next(x for x in audit['assessments'] if x['capability_id']=='D05.e');a.update(verdict='P01–P03 clos : couverts sans nouvelle décomposition U425',diagnosis='Le périmètre distingue cibles, apports et modification autorisée des Orders ; politiques et ajustements explicités.',recommendation='Conserver D05.e sans comportement direct. Besoins datés, seuil/cible et ajustements sont décrits ; ne pas réactiver les trois anciens candidats sans besoin métier nouveau.')
    synthesis=audit['current_synthesis_U298'];synthesis['retained_candidate_ids']=[x for x in synthesis['retained_candidate_ids'] if x not in CANDIDATES];synthesis['covered_candidate_ids']=CANDIDATES
    synthesis['source_refs']=list(dict.fromkeys(synthesis['source_refs']+['U425']));synthesis['retained_scope']='U425 clôt P01–P03 comme couverts par D05.e sans nouveaux comportements. P12 reste conditionnel ; P04/P10 restent à réexaminer ; les intégrations antérieures sont conservées.'
    synthesis['next_step']='Poursuivre les points encore ouverts de l’audit existant : P04/P10/P12 et responsabilité commerciale des retours. P01–P03 clos U425, ne plus les présenter comme candidats à créer.'
    save('modeles/backlog/behavior-gap-audit.yaml',audit)
    ann=read(ROOT/'modeles/backlog/d05-refactoring.yaml');ann['replenishment_closure_U425']=dict(status='integrated',source_refs=REFS,candidates=CANDIDATES,capability_id='D05.e',decision='covered_without_new_behaviors',scope='Clôture et frontières adoptées ; descriptions détaillées et comparaisons éditoriales.',evidence=(OUT/'implementation.yaml').relative_to(ROOT).as_posix());save('modeles/backlog/d05-refactoring.yaml',ann)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8');marker='- **Order Lifecycle Management (U349)**';assert marker in text
    text=text.replace(marker,'- **Replenishment Decision (U425)** : P01/P02/P03 sont clos comme couverts par D05.e, sans nouveaux comportements. Besoins datés et seuil/cible restent des politiques descriptives ; ajuster les apports existants est une faculté transverse. Inventory Target Decision détermine cibles/seuils variables, Supply Protection gouverne/applique les paramètres, Replenishment Decision recommande les apports, D04/Lifecycle applique les changements autorisés et D06 orchestre. Ne pas réouvrir ces candidats sans besoin nouveau démontré.\n'+marker);agents.write_text(text,encoding='utf-8')
    append('marche/elements.md','### ELM252\n\nMicrosoft Dynamics 365 SCM — Coverage settings (25 mars 2026, Coverage codes) et Action messages (26 mars 2026, Introduction et Select action messages). Pages primaires consultées le 19 septembre 2026. Méthodes de réapprovisionnement et de lotissement ; recommandations Advance/Postpone/Increase/Decrease. URLs et limites sur D05.e. Pas de taxonomie de capacités ni preuve installée Beaumanoir.')
    append('marche/comparaisons.md','### CMP163\n\nU425 — P01, P02 et P03 clos comme couverts par Replenishment Decision, sans comportements supplémentaires. Les méthodes Microsoft Per requirement/Per period/Min-Max et les Action messages étayent les politiques et ajustements décrits, sans imposer un nœud par méthode. Min/max peut dépendre des besoins par période ; la détermination des cibles reste dans Inventory Target Decision. D04 applique les changements autorisés ; D06 réalise via ses services. Clôture adoptée ; descriptions et rapprochements éditoriaux. Aucun constat d’exhaustivité du marché.')
    append('JOURNAL.md','## 2026-09-19 — U425 : clôture des candidats de réassort\n\nP01–P03 clos comme couverts par D05.e ; politiques besoins datés/seuil-cible et ajustements explicités. Aucun nouveau comportement ni changement de structure. Audit existant, comparaisons Microsoft et instructions actualisés ; preuves antérieures conservées. Aucune release.')
    print('U425: P01-P03 closed as covered; only D05.e enriched, topology unchanged.')


if __name__=='__main__':main()
