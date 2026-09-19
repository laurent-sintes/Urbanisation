# U271 — Scenario Impact Analysis intégré

Accord transcrit dans le backlog : BHV010, nom et définition adoptés, rattachement terminal à D05.f. Six comportements Inventory Planning et quatre ATP ; 41 capacités conservées.

Les définitions BHV006 et BHV007 reprennent les résultats du tableau présenté et validé : situation opérationnelle projetée et appréciation du compromis. Les valeurs U269 restent dans les captures et leur registre ; les portées U271 et empreintes sont dans `d05-refactoring.yaml.scenario_impact_U271`. Les compléments de périmètre restent proposés. La justification du sixième comportement et la possibilité d’exploiter les indicateurs déjà produits par la simulation sont consignées.

AGENTS, glossaire méthodologique, connaissance, suivi d’audit, principe de scénario et CMP091 actualisés. Les correspondances marché restent des appuis fonctionnels ; aucune nouvelle équivalence adoptée.

Contrôles : provenance 1 234 sources, validation 0 erreur, restitutions régénérées ; **31 tests Python réussis** (`scripts.test_behaviors`, `scripts.test_models`), dont contrôle des anciennes valeurs U269 et des nouvelles portées U271. `git diff --check` réussi.

`integrity.json` vérifie les 134 fichiers protégés inchangés, les 97 relations existantes inchangées et le seul nouveau nœud BHV010. Seuls D05.f, BHV006 et BHV007 changent parmi les nœuds existants. Une relation structurelle ajoutée ; aucune relation de séquence ou capacité nouvelle.

Le scénario navigateur existant est adapté aux six comportements. Il n’est pas réexécuté dans ce tour ; le serveur était indisponible lors du contrôle U269. Aucun changement du frontend ni assertion de validation visuelle nouvelle.

La release v007 / 2026-09-16.2 reste inchangée. Aucune publication, aucun commit ni push. Captures avant modification : fichiers `*-before.yaml` ; script ponctuel protégé contre double application : `scripts/apply_impact_U271.py`.
