"""Record the challenge to the no-decomposition recommendation."""
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read


def main():
    assert '## U426\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md','## U426\n\n**id**\n\nU426\n\n**date**\n\n2026-09-19\n\n**titre**\n\nReconsidérer les politiques de réassort comme comportements\n\n**texte**\n\nIl faut les mettre en comportement de la décision, non ?\n\n**contexte et portée**\n\nQuestion reçue pendant la finalisation U425. Réouvre le choix de non-décomposition : politiques et mécanismes sont des critères admis, une fois distingués calcul des cibles et décision des apports. Les trois candidats sont remis à l’étude ; aucune création de nœud ni validation des nouveaux noms et définitions déduite de la question. Les descriptions enrichies U425 restent conservées. Codex reconnaît avoir prolongé trop largement la réserve U324/C98.')
    audit=read(ROOT/'modeles/backlog/behavior-gap-audit.yaml')
    audit['source_refs']=list(dict.fromkeys(audit['source_refs']+['U426']))
    for p in audit['candidates']:
        if p['id'] in ['P01','P02','P03']:
            p['closure_U425']=dict(status=p['status'],resolution=p['resolution'],note=p['review_note'])
            p['status']='needs_reassessment_U426';p['source_refs']=list(dict.fromkeys(p['source_refs']+['U426']))
            p['review_note']='U426 remet en cause la clôture U425 : deux politiques distinctes de détermination des apports et un mécanisme d’ajustement justifient un réexamen comme comportements combinables. Aucune confusion avec le calcul des cibles ; nouveaux noms/définitions proposés, non appliqués.'
            p.pop('covered_by',None);p.pop('resolution',None)
    s=audit['current_synthesis_U298'];s['covered_candidate_ids']=[];s['reassess_candidate_ids']=list(dict.fromkeys(s['reassess_candidate_ids']+['P01','P02','P03']))
    s['retained_scope']='U426 réouvre P01–P03 comme comportements possibles de décision ; politiques et mécanismes sont des critères légitimes après clarification des responsabilités.'
    s['next_step']='Préciser les trois comportements de Replenishment Decision suite à U426, sans nouveau domaine ni confusion avec Inventory Target Decision.'
    a=next(x for x in audit['assessments'] if x['capability_id']=='D05.e');a.update(verdict='décomposition réouverte U426',diagnosis='Les politiques produisent des apports selon des logiques distinctes ; ajuster un apport existant évite une création supplémentaire. Cette différence relève des critères de comportement du modèle.',recommendation='Proposer deux politiques de réassort et un mécanisme d’ajustement combinable ; conserver objectifs/seuils dans Inventory Target Decision.')
    audit['replenishment_reassessment_U426']=dict(source_refs=['U426'],status='proposed',candidate_ids=['P01','P02','P03'],reason='La réserve C98 portait sur la confusion de responsabilités et le bénéfice insuffisamment explicité ; elle ne disqualifie pas les politiques comme comportements.',proposal=[dict(candidate_id='P01',name='Requirement-based Replenishment',definition='Déterminer les apports nécessaires pour satisfaire des besoins datés, nets des ressources admissibles et des apports déjà prévus.',benefit='Répondre aux besoins identifiés à leurs échéances, individuellement ou regroupés sur une période.'),dict(candidate_id='P02',name='Target-based Replenishment',definition='Déterminer les apports nécessaires pour rétablir un niveau de stock cible selon les seuils et règles de déclenchement applicables.',benefit='Maintenir la disponibilité selon un objectif de stock, sans exiger une commande identifiée pour chaque apport.'),dict(candidate_id='P03',name='Replenishment Adjustment',definition='Déterminer les modifications des apports existants lorsque les besoins ou contraintes évoluent, en respectant les engagements et restrictions applicables.',benefit='Réduire les excédents et décalages sans recréer systématiquement un apport ; se combine avec les deux politiques.')],market_refs=['ELM252','CMP163'],limits='Proposition FLOW appuyée sur méthodes Microsoft et Action messages ; noms non présentés comme taxonomie Microsoft. Le catalogue garde pour l’instant D05.e sans comportement direct.')
    save('modeles/backlog/behavior-gap-audit.yaml',audit)
    ann=read(ROOT/'modeles/backlog/d05-refactoring.yaml');ann['replenishment_reassessment_U426']=audit['replenishment_reassessment_U426'];save('modeles/backlog/d05-refactoring.yaml',ann)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8');start=text.index('- **Replenishment Decision (U425)**');end=text.index('\n',start)
    text=text[:start]+'- **Replenishment Decision (U425/U426)** : U425 a documenté besoins datés, seuil/cible et ajustements sans comportement nouveau. U426 remet cette non-décomposition en question : P01–P03 sont réouverts comme politiques/mécanisme possibles, avec bénéfice à expliciter. La réserve U324/C98 ne disqualifie pas toute politique. Cibles/seuils relèvent d’Inventory Target Decision, apports/ajustements de Replenishment Decision, changements autorisés de D04/Lifecycle et orchestration de D06. Proposition dans `d05-refactoring.yaml`, `replenishment_reassessment_U426` ; aucun nouveau nœud adopté à ce stade.'+text[end:];agents.write_text(text,encoding='utf-8')
    append('JOURNAL.md','## 2026-09-19 — U426 : réouverture des comportements de réassort\n\nLa question de Laurent réouvre P01–P03 avant finalisation du suivi U425. Proposition corrigée : deux politiques d’apports et un mécanisme d’ajustement combinable, avec bénéfices explicites. Les descriptions U425 sont conservées ; aucun comportement créé sans accord sur la proposition. Audit et instructions portent le réexamen courant.')
    print('U426 recorded: P01-P03 reopened; no new behavior nodes.')


if __name__=='__main__':main()
