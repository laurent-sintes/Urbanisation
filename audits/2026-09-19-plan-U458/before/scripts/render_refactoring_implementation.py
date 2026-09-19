"""Check and render the U290 migration against its immutable evidence."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from scripts.structured_io import read

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-17-refonte-appliquee'


def main():
    registry=read(ROOT/'modeles/backlog/refactoring-implementation.yaml')
    model=read(ROOT/'modeles/backlog/model.yaml')
    before=read(ROOT/registry['baseline'])
    nodes={n['id']:n for n in model['nodes']}
    old={n['id']:n for n in before['nodes']}
    relations={r['id']:r for r in model['relations']}
    retired=registry['retired_node_redirects']
    assert set(old)-set(nodes)==set(retired)
    assert all(n in nodes for n in retired.values())
    assert all(n not in nodes for n in registry['retired_ids_never_reuse'])
    for n in nodes.values():
        if n['kind']=='behavior':
            parents=[r['source_id'] for r in model['relations'] if r['type']=='contains' and r['target_id']==n['id']]
            assert len(parents)==1 and nodes[parents[0]]['kind']=='capability'
            assert nodes[parents[0]]['fields']['decomposition_rationale']
    for identifier in ['BHV001','BHV002','BHV003','BHV004']:
        assert nodes[identifier]==old[identifier], 'ATP agreement changed'
    audited={r['id'] for r in registry['relation_migration']}
    assert all(r['id'] in relations or r['id'] in audited for r in before['relations'])
    assert len(registry['dependency_contracts'])==133
    for dep in registry['dependency_contracts'].values():
        if 'relation_id' in dep:
            rel=relations[dep['relation_id']]
            assert rel['source_id']!=rel['target_id']
            assert rel['qualification']['role']=='needs'
            assert rel['qualification']['conditions'] and rel['qualification']['effects']
    protected=read(OUT/'protected.json')
    assert all(sha256((ROOT/path).read_bytes()).hexdigest()==digest for path,digest in protected.items())
    counts=Counter(n['kind'] for n in nodes.values())
    checks=dict(nodes=len(nodes),capabilities=counts['capability'],behaviors=counts['behavior'],relations=len(relations),
        retired_nodes=len(retired),reviewed_dependency_contracts=133,
        integrated_dependency_relations=len({d['relation_id'] for d in registry['dependency_contracts'].values() if 'relation_id' in d}),
        ATP_records_unchanged=True,protected_files_unchanged=len(protected),structural_checks='passed',
        business_scope='Core applied; detailed editorial values and dependencies retain their individual review scopes.')
    (OUT/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows=['# Refonte appliquée — U290','',
        'Le backlog contient désormais **39 capacités et 14 comportements**. La refonte porte sur le socle recommandé U286–U289 ; elle conserve la profondeur Capacité → Comportement. Les publications et la version consultée dans Atlas sont inchangées.',
        '', 'Autorité : [modèle courant](../../modeles/backlog/model.yaml) et [registre de migration](../../modeles/backlog/refactoring-implementation.yaml). La [cible initiale](../2026-09-17-refonte-modele/rapport.md) conserve la revue avant application.',
        '', '## Changements appliqués','',
        '| Ensemble | Résultat |','| --- | --- |',
        '| Promise Management | D03.n remplace trois capacités ; proposition, confirmation et révision deviennent BHV021–023. |',
        '| Inventory Planning | Scenario Construction, Simulation & Analysis, Scenario Execution Adaptation. Comparaison, autorisation et mise en action restent décrites. |',
        '| Supply Protection | Group Supply Protection, Consumption Capping, Safety Stock Policy, Replenishment Regulation. Les opérations sur enveloppes restent dans le périmètre. |',
        '| ATP | Quatre comportements et leurs accords préservés intégralement. |',
        '| Supply Assignment | Maximiser la valeur multidimensionnelle de la satisfaction des commandes sous contraintes ; ni volume seul, ni marge seule. |',
        '| D05.d | Group Protection Decision remplace le nom ambigu Stock Allocation Decision, sans changer le résultat attendu. |',
        '| D04.o et D05.e | Cycle de vie qualifié management ; ajustements des apports futurs explicités sous contraintes. L’application des conséquences de plans sur les Orders est décrite. |',
        '', '## Portée de validation','',
        'U290 autorise cette mise en œuvre et confirme la finalité de valeur multidimensionnelle. Les descriptions de synthèse, exemples fictifs et contrats détaillés ajoutés restent éditoriaux ; le cycle de vie conserve seulement les accords correspondant aux valeurs effectivement inchangées ou aux libellés retenus. Les décisions historiques et leurs empreintes ne sont pas réécrites.',
        '', 'Les arbitrages spécialisés restent distincts : Order Prioritization pour les priorités, ATP/CTP pour les possibilités et la faisabilité, PTP pour le compromis économique, Delivery Schedule Decision pour les échéanciers. La finalité de valeur de Supply Assignment ne crée pas une décision générale absorbant ces capacités.',
        '', '## Dépendances et identités','',
        f"Les 133 contrats proposés ont tous une destination tracée ; {checks['integrated_dependency_relations']} relations les portent après regroupement des contrats équivalents. Les dépendances devenues internes à Promise Management ne créent pas de boucle. Les relations de sens différent et les liens objets/documents/événements sont préservés. Les contrats détaillés sont en instruction, pas déclarés validés collectivement.",
        '', '| Identifiant retiré | Destination |','| --- | --- |']
    rows += [f"| {k} — {old[k]['fields']['name']} | {v} — {nodes[v]['fields']['name']} |" for k,v in retired.items()]
    rows += ['', 'Ces correspondances assurent la traçabilité de migration et la réécriture des liens actifs. Elles ne redirigent pas les liens de publications anciennes : chaque publication reste autonome. Les identifiants retirés ne sont pas réutilisés.',
        '', '## Points maintenus ouverts','']+['- '+q for q in registry['open_questions']]
    rows += ['', '## Étape suivante — U291','',
        'Examiner les capacités encore peu décrites en comportements, en partant de cas métier et de mécanismes documentés sur le marché. Pour chaque ajout, démontrer une complexité ou un bénéfice ciblé ; ne pas réintroduire de listes de fonctions ni chercher une décomposition uniforme. Cette étape est demandée pour après la refonte et n’est pas engagée dans cette passe.',
        '', '## Comparaison marché et contrôles','',
        'Les choix s’appuient sur la [comparaison de la cible](../2026-09-17-refonte-modele/sources.md) et la [convention Assignment](../../marche/assignment-allocation-convention.md). [Microsoft Intelligent Fulfillment Optimization](https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/ifo-arch) documente objectifs métier et contraintes, notamment les coûts ; cela appuie une finalité plurielle, sans prescrire les dimensions ni les pondérations FLOW.',
        '', f"Contrôles structurels : {len(nodes)} nœuds, {len(relations)} relations ; chaque comportement possède un seul parent capacité, tous les retraits sont tracés, quatre enregistrements ATP identiques, {len(protected)} fichiers historiques protégés inchangés. [Résultats](checks.json). Les tests et la validation générale complètent ces contrôles ; ils ne valent pas validation métier.",
        '', 'Régénération : `python -m scripts.render_refactoring_implementation`.']
    validation_path=OUT/'validation.json'
    if validation_path.exists():
        validation=read(validation_path)
        rows += ['', '## Vérification finale','', validation['summary']]
    (OUT/'rapport.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    print(json.dumps(checks,ensure_ascii=False))


if __name__=='__main__': main()
