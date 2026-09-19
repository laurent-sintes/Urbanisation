"""Apply the approved consignment behaviors and document readable business links."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

OUT = ROOT / 'modeles/backlog/history/consignment-behaviors-U398'


def main():
    assert not OUT.exists()
    mp = ROOT / 'modeles/backlog/model.yaml'
    before = read(mp); m = deepcopy(before)
    assert not {'BHV061', 'BHV062'} & {n['id'] for n in m['nodes']}
    assert '## U398\n' not in (ROOT / 'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    append('connaissance/01-contributions-utilisateur.md', '''## U398

**id**

U398

**date**

2026-09-18

**titre**

Adopter les comportements de l’apport consigné et expliciter les interactions métier

**texte**

Je valide !

La mutualisation apparait éventuellement lorsque on trace des liens entre les capacités.

D'ailleurs, si une capacité est appelée par deux capacités qui implique des comportements différents, on doit différencier les comportements et expliquer pourquoi.

Je pense aussi que les liens entre les capacités doivent être valorisés avec un mot ou une expression pour faire mieux que "a besoin de". En lisant les capacités et les liens, on doit pouvoir reconstruire une logique, une histoire.

**contexte et portée**

Accord sur Initial Stocking et Continuous Replenishment sous Consignment Replenishment Order, leurs noms, responsabilités présentées et rattachements. Exigence de description des comportements différents selon les capacités qui mobilisent une capacité commune, avec explication des différences. Exigence de libellés métier des liens pour reconstruire la logique des interactions. Un appelant différent ne suffit pas à inventer une différence de comportement ; la condition exprimée est une différence réelle. La mutualisation n’est pas imposée comme architecture informatique. Le principe ne valide pas par extension chaque nouveau libellé, contrat ou séquence ; distinguer dépendance, résultat transmis et déclenchement. Aucune release demandée.''')
    OUT.mkdir()
    for stem in ['model', 'nonpurchase-supply-order-review', 'behavior-gap-audit', 'modeling-glossary']:
        (OUT / (stem + '-before.yaml')).write_bytes((ROOT / f'modeles/backlog/{stem}.yaml').read_bytes())
    (OUT / 'AGENTS-before.md').write_bytes((ROOT / 'AGENTS.md').read_bytes())
    refs = ['U397', 'U398', 'CMP148', 'CMP150']
    stamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def life(values, approved=()):
        return dict(state='urbanist_validated' if approved else 'under_instruction', recorded_at=stamp, recorded_by='Codex',
            source_refs=['U398'], validated_fields=list(approved), value_sha256={f:value_hash(values[f]) for f in approved},
            note='Noms, définitions présentées et parents adoptés U398 ; descriptions et libellés détaillés éditoriaux.')

    rp = 'modeles/backlog/nonpurchase-supply-order-review.yaml'; review = read(ROOT / rp)
    proposal = review['current_U397']; parent = next(n for n in m['nodes'] if n['id'] == 'D04.r')
    parent['fields']['decomposition_rationale'] = proposal['decomposition_rationale']
    parent['fields']['scope'] += ('\n\nU398 : deux comportements explicitent les intentions de la demande : '
        '[Initial Stocking](model:BHV061), pour constituer le stock avant le lancement, et '
        '[Continuous Replenishment](model:BHV062), pour alimenter le stock pendant l’activité. '
        'La lisibilité de ces intentions justifie la décomposition même lorsque leur traitement est commun. '
        + proposal['common_description'])
    parent['revision'] += 1; parent['source_refs'] = list(dict.fromkeys(parent['source_refs'] + refs))
    definitions = [
        'Prendre en charge l’apport initial de stock consigné pour une saison, une capsule ou un lancement, et suivre sa satisfaction avant l’échéance de démarrage.',
        'Prendre en charge les apports successifs de stock consigné pendant l’activité, selon l’évolution du besoin, et suivre leur satisfaction.',
    ]
    adoptions = []
    for ident, candidate, definition in zip(['BHV061', 'BHV062'], proposal['proposals'], definitions):
        fields = dict(name=candidate['name'], definition=definition, finality=candidate['benefit'],
            scope=candidate['boundary'] + '\n\nExemple fictif : ' + candidate['example'] + '\n\n'
                + proposal['common_description'] + '\n\n'
                'Le stock demeure sous le régime de consignation après réception. Consigned Inventory Management applique les conditions ; '
                'l’acquisition éventuelle et les prestations conservent leurs responsabilités distinctes. '
                'Aucun sous-comportement, partage de logiciel ou automatisme de commande imposé.',
            market_comparisons=deepcopy(parent['fields']['market_comparisons'][:1]))
        fields['market_comparisons'][0].update(flow_position='U398 adopte ce comportement pour expliciter l’intention métier FLOW. '
            'La source Microsoft décrit la demande d’apport ; elle ne prescrit pas ce découpage en deux comportements.', source_refs=refs)
        n = dict(id=ident, revision=1, kind='behavior', layer=parent['layer'], fields=fields, source_refs=refs,
            source_locator=dict(path='connaissance/01-contributions-utilisateur.md', anchor='u398'), adoption_ids=[],
            review=dict(state='partial', note='Nom, définition présentée et parent adoptés U398 ; finalité, scope et comparaison éditoriaux.'),
            lifecycle=life(fields, ['name', 'definition']))
        m['nodes'].append(n)
        r = dict(id='REL-BEHAVIOR-' + ident, revision=1, type='contains', source_id='D04.r', target_id=ident,
            source_refs=refs, review=dict(state='accepted', note='Rattachement explicitement adopté U398.'))
        r['lifecycle'] = life(r, ['type', 'source_id', 'target_id']); m['relations'].append(r)
        adoptions.append(dict(node_id=ident, parent_id='D04.r', adopted_fields=['name', 'definition'], value_sha256=n['lifecycle']['value_sha256']))
    save('modeles/backlog/model.yaml', m)
    migration = dict(source_refs=['U398'], model_before=(OUT/'model-before.yaml').relative_to(ROOT).as_posix(),
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(), delta={}, adopted_behaviors=adoptions,
        behaviors=[])
    for key in ['nodes', 'relations']:
        old = {x['id']:x for x in before[key]}; new = {x['id']:x for x in m[key]}
        migration['delta'][key] = dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(old.keys() & new.keys()) if old[i] != new[i]}, removed=sorted(old.keys()-new.keys()))
    save((OUT/'implementation.yaml').relative_to(ROOT), migration)
    review['source_refs'].append('U398'); proposal['status'] = 'integrated_U398'
    proposal['proposal_status'] = 'Noms et définitions présentées adoptés U398 ; détails éditoriaux qualifiés séparément.'
    review['current_U398'] = dict(status='integrated', behavior_ids=['BHV061','BHV062'], implementation_ref='modeles/backlog/history/consignment-behaviors-U398/implementation.yaml')
    save(rp, review)
    ap = 'modeles/backlog/behavior-gap-audit.yaml'; audit = read(ROOT/ap)
    audit['source_refs'].append('U398'); audit['implementation_U398'] = migration
    audit['baseline']['sha256'] = sha256(mp.read_bytes()).hexdigest()
    assessment = next(a for a in audit['assessments'] if a['capability_id']=='D04.r')
    assessment.update(existing_behaviors=['BHV061','BHV062'], verdict='deux parcours intégrés U398',
        diagnosis=proposal['decomposition_rationale'], recommendation='Implantation et alimentation continue explicites ; décisions mobilisées et fonctions communes documentées. Les nouvelles règles sur les interactions sont consignées pour la suite U399, sans révision des liens existants.')
    for ident in ['BHV061','BHV062']:
        audit['existing_behavior_review'].append(dict(behavior_id=ident,status='integrated_U398',market_sources=[],recommendation='Nom, définition présentée et parent adoptés U398 ; bénéfice de lisibilité métier ; comparaison Microsoft qualifiée dans la fiche.'))
    save(ap, audit)
    append('connaissance/01-contributions-utilisateur.md', '''## U399

**id**

U399

**date**

2026-09-18

**titre**

Consigner les nouvelles règles pour les travaux futurs sans ouvrir un nouvel audit

**texte**

Les nouvelles règles que je t'expose ne doivent pas générer un nouvel audit. On termine déjà l'existant. Mais je veux que tu consignes ces règles pour le prochain audit et/ou les prochaines améliorations du modèle.

**contexte et portée**

Instruction de déroulement : poursuivre et terminer l’audit existant. Mémoriser les nouvelles règles sans déclencher de nouvel audit, revue globale, reprise des liens existants ou chantier Atlas. L’intégration des deux comportements explicitement validés U398 reste autorisée. Les principes sont destinés au prochain audit ou aux prochaines améliorations ; leur enregistrement n’en programme pas l’exécution.''')
    principles = dict(id='BUSINESS-INTERACTIONS-U398', source_refs=['U398','U399','U397','ELM239','CMP150'], status='rules_recorded_for_future_work',
        principle='Les capacités et leurs liens doivent permettre de reconstruire une logique métier. La mutualisation peut apparaître dans leurs interactions ; elle ne détermine pas le découpage des comportements.',
        contextual_behavior='Lorsqu’une capacité mobilisée par plusieurs capacités agit différemment selon le contexte, distinguer ses comportements et expliquer ce qui change : intention, résultat, contraintes ou engagements. Un appelant différent ne suffit pas si le comportement reste identique.',
        ownership='Chaque comportement reste sous une seule capacité ; les interactions permettent de désigner ou décrire le comportement mobilisé sans le copier sous tous ses appelants.',
        relation_convention=dict(status='editorial_guidance_for_future_work_not_implemented', label='Prévoir une expression courte lue de la source vers la cible ; stockage et restitution à réaliser lors d’une amélioration ultérieure.',
            meaning='Sens complet, résultat métier attendu et comportements concernés dans qualification.meaning.',
            conditions='Conditions dans qualification.conditions ; expliquer pourquoi le comportement diffère.',
            effects='Effets attendus et frontières dans qualification.effects et scope.',
            semantics='Distinguer dépendance de service, information ou résultat transmis, déclenchement causal et réalisation. Ne pas inverser les flèches ni inventer une séquence pour rendre le récit plus fluide.'),
        rollout='U399 : terminer l’audit existant. Règles à utiliser lors du prochain audit et/ou des prochaines améliorations, sans nouvel audit, revue des liens existants ou chantier Atlas déclenché par leur mémorisation. Aucun calendrier ni automatisation créé.',
        market_comparison=dict(source_url='https://archimate-community.pages.opengroup.org/workgroups/archimate-101/',
            title='ArchiMate 101: A Practical Introduction', vendor='The Open Group — ArchiMate Community', edition='Tutoriel évolutif ; pas une adoption normative de la spécification',
            locator='Relationships between systems : Sharing information, money, goods ; Temporal or causal relationship ; Dependencies between systems',
            consulted_on='2026-09-18', finding='Distingue Flow, Triggering et Serving ; leurs orientations peuvent différer selon le contexte.',
            flow_position='Appui méthodologique à des liens au sens précis et orientés. Les libellés métier, le niveau terminal Comportement et la règle de différenciation par contexte sont des conventions FLOW.',
            limit='Ne démontre pas une équivalence entre nos capacités et les éléments ArchiMate ; aucune cartographie complète ni workflow d’exécution adopté.'))
    save('modeles/backlog/business-interactions.yaml', principles)
    gp = 'modeles/backlog/modeling-glossary.yaml'; glossary = read(ROOT/gp)
    glossary['source_refs'].extend(['U398','U399']); term = next(t for t in glossary['terms'] if t['id']=='MOD006')
    term['source_refs'].extend(['U398','U399'])
    term['review']['adopted_scope'] += ' U398 : différencier et expliquer les comportements réellement différents d’une capacité selon les capacités qui la mobilisent ; interactions nommées pour rendre la logique métier lisible.'
    term['notes'].append('U398 : la mutualisation peut se lire dans les liens. Décrire le comportement mobilisé et sa différence métier selon le contexte ; aucun comportement automatique par appelant et aucun sous-comportement. U399 : règles consignées pour le prochain audit et/ou les prochaines améliorations, sans déclencher de nouvelle revue. Convention : modeles/backlog/business-interactions.yaml.')
    save(gp, glossary)
    agents = ROOT/'AGENTS.md'; text = agents.read_text(encoding='utf-8')
    text = text.replace('liste révisée encore proposée dans `modeles/backlog/nonpurchase-supply-order-review.yaml`.', 'Initial Stocking et Continuous Replenishment adoptés U398 sous D04.r (BHV061–062), dans `modeles/backlog/nonpurchase-supply-order-review.yaml`.')
    marker = '- Objets métier, documents et événements restent distincts'
    text = text.replace(marker, '- **Interactions métier lisibles (U398/U399)** : nommer les liens par une expression métier orientée source → cible, préciser sens, résultats, conditions et effets. La mutualisation peut apparaître dans les liens. Si une capacité agit différemment selon celles qui la mobilisent, différencier ses comportements et expliquer pourquoi ; aucun comportement automatique par appelant. Les comportements gardent un parent unique. Distinguer dépendance, résultat transmis et déclenchement ; ne pas inventer un workflow pour produire un récit. **U399 : consigner ces règles pour le prochain audit et/ou les prochaines améliorations ; ne pas déclencher un nouvel audit ni une reprise des liens. Terminer l’audit existant.** Convention et comparaison : `modeles/backlog/business-interactions.yaml`.\n'+marker, 1)
    agents.write_text(text,encoding='utf-8')
    append('marche/elements.md', '''### ELM239

18 septembre 2026 — The Open Group, ArchiMate Community : [ArchiMate 101](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/), tutoriel évolutif ouvert, sections Relationships between systems. Flow distingue les échanges, Triggering la précédence temporelle/causale, Serving la fourniture de comportement utile. Les directions ne sont pas nécessairement identiques. Appui méthodologique, pas catalogue de capacités FLOW ni prescription de notre niveau Comportement.''')
    append('marche/comparaisons.md', '''### CMP150

U398 — ELM239, appui méthodologique. La distinction des sens Flow/Triggering/Serving conforte la qualification des interactions et l’attention au sens des flèches. FLOW retient des expressions métier lisibles et l’explication des comportements selon le contexte. Notre niveau terminal et la différenciation des comportements restent des conventions FLOW, sans assimilation aux éléments ArchiMate. U399 réserve leur mise en œuvre aux travaux futurs : aucun nouvel audit ni remaniement des liens. Convention : modeles/backlog/business-interactions.yaml.''')
    append('JOURNAL.md', '''## 2026-09-18 — U398 : comportements de consignation et liens métier

BHV061 Initial Stocking et BHV062 Continuous Replenishment intégrés sous D04.r ; noms, définitions présentées et parents validés. Justification de lisibilité conservée. U399 : les règles de comportement différencié selon l’interaction et de liens lisibles sont mémorisées dans AGENTS.md, MOD006 et business-interactions.yaml pour le prochain audit ou les prochaines améliorations. Aucun nouvel audit, remaniement des liens ou chantier Atlas. Captures techniques dans modeles/backlog/history/consignment-behaviors-U398 ; poursuite de l’audit existant. Backlog uniquement.''')
    (OUT/'README.md').write_text('# U398 — preuve d’intégration des comportements\n\nBHV061/BHV062 intégrés sous D04.r. Définitions présentées adoptées, détails éditoriaux distincts. Captures techniques et empreintes dans implementation.yaml ; il ne s’agit pas d’un nouvel audit. U399 réserve les nouvelles règles d’interaction aux travaux futurs. Aucun lien métier existant ni publication modifié.\n',encoding='utf-8')
    print('U398 integrated: two behaviors; U399 interaction rules recorded for future work. No new audit.')


if __name__ == '__main__':
    main()
