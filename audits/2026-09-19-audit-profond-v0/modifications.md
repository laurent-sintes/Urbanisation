# Audit V0 — corrections réalisées sous U435/U436

**19 septembre 2026.** Les corrections évidentes et plausibles ont été appliquées au backlog. Le socle reste à **47 capacités et 74 comportements**. Les textes courants sont plus cohérents, les principales interactions sont explicites et les fiches de décision prioritaires sont plus précises. Les choix complexes encore ouverts sont isolés dans [le suivi V0](../../modeles/backlog/v0-readiness.yaml).

L’[audit approfondi](rapport.md) conserve l’état initial : cohérence, comparaison de huit éditeurs, cadres transverses, relations et limites. Le présent rapport décrit ce qui a effectivement changé. Les 28 références éditeurs examinées incluent quatre lectures limitées aux passages officiels indexés ; les ajouts aux fiches utilisent des documentations ou cours effectivement ouverts. GS1 apporte un appui supplémentaire sur les faits de stock. Une source produit ne prouve aucun déploiement Beaumanoir.

## Changements appliqués

| Intervention | Avant | Après |
| --- | --- | --- |
| Cohérence du contenu courant | Ancien nom Order Promising, Structuring encore attribué à D04 dans certains textes, dix phrases Intercompany hors contexte, références de comportements périmées | Noms et responsabilités courants rétablis ; exemples MOD006 actualisés ; ancienne alternative U158 sortie de la liste active et conservée dans la capture initiale |
| Interactions prioritaires | Planning, autorisation de prise en charge, confirmation fournisseur et consignation insuffisamment reliés | **12 liens qualifiés proposés ajoutés**, appuyés sur les responsabilités décrites |
| Lecture des relations existantes | Aucun libellé propre ; cinq contrats encore ambigus sur l’effet de l’affectation | **17 libellés ajoutés** ; cinq qualifications clarifiées selon U436 ; aucun ancien lien supprimé ou réorienté |
| Décisions et temporalité | PTP, priorités et échéancier très courts ; calendriers et coupures peu visibles | Entrées, contraintes, résultats, limites et exemples complétés ; calendriers, fuseaux, jours ouvrés, fraîcheur et données inconnues explicités |
| Faits de stock | Correction et double réception insuffisamment éprouvées | Enregistrement des faits, établissement des états et restitution distingués ; exemple de réception doublonnée puis corrigée, sans imposer une technologie |
| Comparaison marché en fiche | 24/47 capacités documentées ; 223 entrées au total | **39/47 capacités documentées**, 239 entrées : 16 ajouts proposés et cinq positions FLOW périmées corrigées |
| Principe et vocabulaire | Effet opposable de l’affectation encore ouvert | **Seule Reservation bloque les usages concurrents ; Supply Assignment seul ne les bloque pas**. Principe U436, cinq scopes, cinq liens et trois termes précisés |
| Atlas et contrat technique | La famille `needs` imposait « A besoin de » ; champ de libellé non prévu au schéma | Expression explicite affichée en conservant orientation et famille ; schéma fermé, contrôle de révision et contrôle des données figées étendus |

**36 fiches existantes sont touchées**, avec une seule incrémentation de révision par fiche pour ce lot. Le modèle passe de 331 à **343 relations**, dont 210 métier. **29 relations portent maintenant une expression métier** : les 17 anciennes enrichies et les 12 nouvelles. Les 139 nœuds restent identiques en nombre, identité, nom, type et couche.

Les nouveaux liens rendent visibles six passages prioritaires : Planning vers la décision du plan ; orchestration vers les autorisations Lifecycle ; apport consigné vers le rapprochement ; régime consigné vers les mouvements ; promesse vers la confirmation fournisseur ; Inventory Planning vers l’apport consigné. Six autres liens complètent les responsabilités déjà décrites de la consignation : cycle, structure, archivage, état de stock, achat éventuel et retour fournisseur. Toutes ces relations restent proposées, avec leurs conditions et inconnus.

## Portée des accords préservée

**Les 570 valeurs couvertes par les validations antérieures sont conservées à l’identique.** Aucun nom ou parent n’a été changé. Les définitions déjà validées sont intactes ; les enrichissements portent sur les descriptions éditoriales et les comparaisons. Les anciennes notes de revue du glossaire sont conservées et complétées par la portée précise de U436.

U435 autorise la réalisation de corrections plausibles, sans valider globalement leur contenu métier. U436 tranche un point précis : le blocage des usages concurrents. Il ne tranche pas les expirations, consommations, libérations, réservations automatisées ou mécanismes techniques de concurrence. Les protections d’admissibilité et les gels d’affectation gardent leurs responsabilités distinctes.

Le principe historique orienté documents a été remis en cohérence avec U393/U394 : l’intention, les parties, engagements et résultats guident la lecture de l’Order ; un document ne dicte pas la décomposition. Sa formulation initiale reste dans la capture de l’audit. Le catalogue ne s’enrichit d’aucune nouvelle capacité ou de nouveaux comportements.

## Ce qui reste à instruire

La frontière réservation/affectation est tranchée. **La question du choix des invendus consignés après saison a été soumise à Laurent et reste en attente de réponse** : choix porté par D05, reçu d’un responsable externe ou laissé ouvert pour la V0. L’application d’une issue autorisée reste dans D01.h ; les liens ajoutés ne prennent pas cette décision à sa place.

Les autres contrats complexes sont conservés explicitement ouverts : effets détaillés de l’application d’un plan, capacité réellement engageable, autorisations commerciales/financières, et gouvernance/application des versions de politique de réservation. Aucune réponse n’a été inventée pour fermer le dossier.

Les corrections de liens sont ciblées : 115 conditions et 125 effets restent sous une formulation générique. Leur réécriture exhaustive n’a pas été prétendue nécessaire ni réalisée. Huit capacités restent sans comparaison de marché dans leur fiche : Service Requirements Decision, Service Reconciliation et les six ingestions. Les appuis disponibles sur leurs usages ne suffisent pas à fabriquer une correspondance sur leur responsabilité complète.

La cartographie des objets/document/événements et celle de Business Services restent limitées ; l’applicabilité structurée aux SI conserve zéro évaluation et Sarenza reste non évalué. Le [kit de revue](kit-revue-v0.md) expose ces frontières, seize situations d’épreuve et les critères d’une présentation V0. Ces situations sont des supports de discussion, pas des tests réussis d’une application.

## Vérifications réalisées

- Validation du modèle : **0 erreur** sur l’état final.
- **79 tests uniques réussis** : 13 graphe frontend, 44 contrats/préparation/libellés, 7 cycle de vie, 15 comportements/glossaire/comparaisons. Les quatre tests spécifiques des libellés ont aussi été rejoués sur le hash final ; ils ne sont pas comptés deux fois.
- Build `pnpm --dir app build` réussi ; avertissement de taille d’un bundle, sans échec de compilation.
- Restitution du backlog régénérée. Contrôle final : aucune extrémité absente, aucun parent multiple ou cycle structurel, aucun doublon exact ; 217 références textuelles `model:` sans cible cassée.
- Revue technique indépendante : conservation des extrémités, qualifications, accords et données figées ; aucun défaut supplémentaire identifié.
- Empreintes des **175 fichiers protégés** de publications, révisions, décisions et provenance figée contrôlées. Clôture U431 et données publiées préservées.

Preuves : [vérification finale](verification.yaml), [détail des changements](changes-final.yaml), [métriques finales](metrics-after.yaml), [graphe final](metrics-liens-after-U435.yaml). État final du modèle : `bc6331a9e199a4723199f39b26ceb3e94ab5caded35e4075fd91d8054acd7347`.

## État de présentation

Le backlog corrigé constitue une base plus claire pour une **revue V0 assortie de ses questions ouvertes**. Il ne faut pas l’annoncer comme une architecture de solution entièrement contractualisée ou comme une preuve de couverture installée.

La nouvelle restitution est disponible dans [le backlog généré](../../restitutions/backlog.md). **Atlas lit toujours la release 2026-09-19.1** : son code est prêt à afficher les libellés, mais les nouvelles données du backlog nécessitent une prochaine release demandée séparément. Aucun commit ni push n’a été réalisé.

## Détail consultable

Les quatre scripts d’application et leurs journaux documentent les transformations : [cohérence](coherence-changes-U435.yaml), [marché](market-fixes.yaml), [liens](modifications-liens-appliquees.yaml) et [scopes / U436](scope-fixes-applied.yaml). Les captures initiales préservent les valeurs remplacées ; elles ne constituent pas un modèle concurrent. Le rapport d’audit et ses matrices restent explicitement datés de l’état initial, afin de ne pas confondre un défaut constaté et son traitement.
