# Consolidation de la base — retours U470/U471

19 septembre 2026. Corrections du backlog et de la présentation Atlas ; aucune nouvelle publication.

Les **47 fiches qui n’avaient qu’une référence disposent maintenant de deux documents primaires distincts**, avec rapprochement argumenté, passage consulté et limites. L’univers Supply est réécrit pour une lecture sans connaissance préalable du domaine. Le catalogue Informations métier est temporairement masqué dans Atlas.

## Contenu de l’univers

Le nom adopté **Supply Chain Orchestration** est conservé. La fiche commence par :

> Organiser l’approvisionnement, la répartition et la livraison des produits pour tenir les quantités et les dates promises.

La définition précise ensuite les décisions concrètes — quoi, combien, depuis quel lieu, à quelle date — et explique « Supply Chain » par les fournisseurs, entrepôts, transporteurs, magasins et clients. Les liens Supply Chain, Orchestration, Commande, Stock, Reference Ingestion et Product Reference donnent accès au glossaire avec infobulle.

Le périmètre explique le choix client : les applications externes gardent la responsabilité des référentiels maîtres. La Supply reçoit leurs projections par ingestion ; elle ne crée, ne corrige ni ne supprime les maîtres à leur place. Elle coordonne les commandes, stocks, promesses et services ; les exécutants réalisent les opérations physiques.

Deux illustrations : livrer 100 tee-shirts vendredi avec 60 en stock et 40 attendus ; recevoir une nouvelle variante depuis son référentiel maître. Ces cas pédagogiques ne décrivent aucun fonctionnement installé ni automatisme obligatoire. Ils conservent la distinction entre promesse et réservation.

Trois termes sont clarifiés : Supply Chain, Orchestration et le contexte de Reference Ingestion. Les anciennes notes d’Orchestration évoquant des couches sont remplacées dans le glossaire courant ; leurs formulations restent dans la capture antérieure.

## Marché : justifier le nom et la frontière de l’univers

Les trois comparaisons portent sur l’univers lui-même :

- **CSCMP** décrit un SCM large, comprenant notamment approvisionnement, transformation, logistique et coordination. Il sert à situer ce que FLOW retient et laisse externe. [Définition professionnelle](https://cscmp.org/CSCMP/Educate/SCM_Definitions_and_Glossary_of_Terms.aspx).
- **Microsoft SCM** présente un périmètre de suite incluant notamment gestion produit, production, stocks et entrepôts. Notre univers ne reprend pas toute cette couverture. [Périmètre de Dynamics 365 SCM](https://learn.microsoft.com/en-us/dynamics365/supply-chain/supply-chain-management-welcome).
- **Oracle** emploie déjà Supply Chain Orchestration pour une responsabilité de coordination, mais son module coopère avec d’autres produits que FLOW ne découpe pas de la même manière. Le terme est documenté ; le périmètre reste un choix FLOW. [Overview of Supply Chain Orchestration, 26B](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauco/overview-of-supply-orchestration.html).

Ces appuis remplacent dans la fiche la comparaison méthodologique TOGAF et la synthèse de composants IOM, qui n’expliquaient pas assez son nom et sa frontière. Ils sont conservés dans la capture avant correction et dans leur provenance historique. Aucun alignement intégral sur un éditeur, consensus universel ou caractère innovant n’est déduit.

## Reprise des 47 fiches

| Périmètre | Fiches complétées |
| --- | ---: |
| Capacités | 14 |
| Référentiel Product Reference | 1 |
| Comportements | 28 |
| Termes métier | 4 |
| **Total** | **47** |

**34 compléments apportent un autre éditeur ou organisme** ; 13 apportent un autre document du même éditeur. C’est explicité lorsque nécessaire : deux documents Oracle sur PTP ou sur le transfert de propriété à échéance ne prouvent pas un consensus interéditeurs.

Chaque ajout précise les points communs, les différences, le choix du terme et la portée de la définition. Exemples de limites conservées : le stock initial UBL éclaire le motif d’un transfert sans définir un Transfer Order ; les tâches magasin ne démontrent pas toute la visibilité de mise en rayon ; la sélection d’un transporteur illustre un type de service ; le document de réception ne transforme pas notre convention fait–document en loi universelle.

Les premières comparaisons, noms, définitions et frontières des 47 fiches sont préservés. Les nouvelles comparaisons restent proposées. Le doublon documentaire initialement détecté sur Intercompany Sales a été remplacé par le parcours SAP Advanced Intercompany Sales, distinct du document Microsoft déjà présent.

Résultat du contrôle : **120 fiches comportent des comparaisons, toutes avec au moins deux documents distincts**. Le périmètre contrôlé comprend les nœuds publiables et le glossaire embarqué ; **129 éléments restent sans comparaison propre**. Leur étude n’était pas la reprise des 47 sources uniques autorisée ici : aucun lien de remplissage n’a été ajouté et l’audit des comportements U431 n’est pas rouvert.

- [Détail des 47 compléments](additions.yaml) : contenus intégrés aux fiches.
- [Registre des 31 documents consultés](sources.yaml) : titres, éditions, passages, dates et organismes.
- [Contrôle de couverture et de préservation](verification.json).
- Traçabilité : U470/U471, ELM292–ELM322, CMP185/CMP186, MKT54 pour UBL.

## Atlas et règles durables

Le catalogue Informations métier disparaît de la navigation, des fiches, des résultats et du filtre de recherche. Les anciens liens reviennent à la fiche de la capacité, ou à la carte, en conservant la version demandée. Les 14 informations et leurs liens restent intacts dans le modèle et dans les publications ; aucun contenu data n’est ajouté.

Les infobulles donnent priorité à la définition complète. Elles fonctionnent au survol et au focus clavier, se ferment avec Échap et ouvrent le terme de la même publication. Les phrases « Position FLOW » strictement identiques à une justification déjà affichée ne sont plus répétées.

Les règles sont consignées dans AGENTS.md, CONVENTIONS-MODELE.md et marche/methode.md : entrée concrète, jargon expliqué, exemple, liens explicites vers le glossaire, comparaison au niveau de la fiche, deux documents primaires pertinents au minimum dès qu’un rapprochement est présenté. La pluralité est contrôlée automatiquement dans le backlog et les nouvelles préparations portant `market_reference_policy: two_primary_sources` ; elle ne remplace pas l’examen humain de la pertinence.

## Vérifications et état de publication

- Validation des modèles : **0 erreur**.
- **82 tests frontend et 30 tests Python réussis** ; compilation Atlas réussie.
- Recette Edge sans fenêtre visible : univers, exemples, sources, infobulles au clavier et à la souris, glossaire, retrait des informations, anciens liens et écran de 390 px ; aucune erreur JavaScript. [Résultats](browser/2026-09-19T11-55-08-431Z/result.json).
- **432 fichiers historiques inchangés**, 346 relations et 14 informations conservées. Les empreintes des accords métier n’ont pas été modifiées.
- Le serveur existant sert bien le nouveau build. Son index publié reste **v012 / 2026-09-19.5** ; pas d’arrêt ni de redémarrage.

L’allègement de l’interface est disponible après rechargement. **Les nouvelles définitions, exemples, liens de glossaire et références restent dans le backlog jusqu’à une nouvelle release.** La recette de ces contenus utilise un aperçu isolé, sans repli du serveur sur le backlog.

Le contrôle de candidature signale les accords attachés aux anciennes révisions : leur report sur les révisions enrichies doit être réexaminé lors de la préparation de release. Les noms et définitions adoptés des 47 fiches sont inchangés, mais aucune décision n’a été automatiquement transcrite. L’aperçu testé ne vaut donc pas préparation de publication validée. Les diagnostics sont conservés dans le résultat de recette.

Captures : [fiche de l’univers](browser/2026-09-19T11-55-08-431Z/univers-desktop.png), [marché et choix](browser/2026-09-19T11-55-08-431Z/marche-univers.png), [infobulle](browser/2026-09-19T11-55-08-431Z/infobulle.png), [lecture mobile](browser/2026-09-19T11-55-08-431Z/univers-mobile.png).
