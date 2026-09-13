# Référentiels : séparation des modèles et regroupement dans la carte

**État courant U103 — 11 septembre 2026 :** le groupe de présentation **Business References** est retenu selon le Go contextuel de Laurent, avec cinq références autonomes, dont Fulfillment Network. [Carte 0.9](../connaissance/25-domaines-coeur-et-epreuve-recits.md#business-references). L’étude U101 et ses options ci-dessous restent datées ; leurs mentions d’arbitrage ouvert sont remplacées sur la seule présentation. Aucun domaine fusionné adopté, détails du réseau ouverts Q076. CMP061.

11 septembre 2026 — réponse à [U101](../connaissance/01-contributions-utilisateur.md#u101), comparaison de P81 0.7. Analyse et proposition Codex [P87](../connaissance/05-propositions.md#p87), sans arbitrage appliqué.


**Évolution U102 :** Fulfillment Network complète depuis cette étude les quatre références comparées, soit cinq sujets dans la proposition de groupe ; voir le complément en fin de note. L’arbitrage de regroupement reste ouvert.

## Recommandation pour FLOW

Conserver les quatre modèles Party / Role, Agreement, Product Reference et Catalog distincts, et les présenter ensemble dans une vue synthétique sous **Business References**, nom local proposé. Ce regroupement facilite la lecture d’un socle qui reçoit les références et décide à partir d’elles. Il ne signifie ni référentiel maître unique ni modèle commun de persistance.

Je corrige le raccourci possible de la carte 0.7 : l’autonomie de l’article confirmée par Laurent justifie de le distinguer du catalogue ; elle n’établit pas à elle seule son rang de domaine au même niveau qu’Inventory Management. Le nombre de capacités d’un domaine ne suffit pas non plus à justifier sa fusion ou sa séparation. Il faut examiner l’espace de problèmes et les règles propres, selon U45/U46.

## Ce que montrent les sources

| Référence et nature | Organisation constatée | Ce que nous pouvons en retenir |
| --- | --- | --- |
| SAP Master Data Governance — solution et domaines de données | Un dispositif commun accueille des modèles spécialisés par sujet, dont produit et partenaires client/fournisseur. | Regrouper le dispositif reste compatible avec la séparation des modèles. Ce ne sont pas des rangs RBA de capacités. [ELM099](elements.md#elm099), [source SAP](https://learning.sap.com/courses/introducing-sap-master-data-governance/describing-data-domains-and-extensibility-options). |
| Microsoft Dynamics 365 — guide de données et documentation produit | Catégorie master data commune ; description spécialisée du produit et de sa réception depuis des maîtres externes. | Une catégorie de données ne dicte pas le nombre de domaines métier. [ELM100](elements.md#elm100), [architecture](https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/data-management-architecture), [produit](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information). |
| TM Forum ODA — blocs et composants | Party et Agreement sont des composants distincts dans Party Management ; Catalog relève de Core Commerce Management. | Séparation et agrégation coexistent ; tous les référentiels ne sont pas rassemblés sous un même bloc. [ELM101](elements.md#elm101), [annuaire officiel](https://www.tmforum.org/oda/directory/components-map). |
| Business Architecture Guild — principe de capacité | Une décomposition conserve l’objet focal : la capacité Customer ne gère pas les produits ou les accords. | Conserver les sens métier ; un groupe visuel n’est pas automatiquement une capacité parente. [ELM102](elements.md#elm102), [guide public §5.2](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf). |

Les sources soutiennent donc la séparation sémantique et montrent plusieurs agrégations. Elles n’établissent pas de règle universelle « un référentiel = un domaine de capacités », ni de domaine universel regroupant exactement nos quatre références. La structure ODA ne doit pas être confondue avec le principe de décomposition Guild : un Function Block n’est pas une capacité mère.

## Trois options locales

| Option | Intérêt | Limite et statut proposé |
| --- | --- | --- |
| Quatre domaines au premier niveau | Identités, règles, contrats et correspondances de chaque sujet restent très visibles. | Vue détaillée actuelle ; rang de domaine encore proposé. Une seule ingestion chacun dans FLOW, car la maîtrise est externe. |
| Un groupe de présentation Business References contenant les quatre repères | Vue synthétique lisible, modèles et ingestions distincts toujours accessibles. | **Option recommandée maintenant**, sans nouveau rang hiérarchique obligatoire ni fusion. Les quatre repères peuvent être développés dans la vue détaillée. |
| Un domaine commun, portant les quatre capacités de réception | Candidat cohérent si le problème étudié est de disposer des références externes nécessaires aux opérations de la Supply. | Possible dans le périmètre plateforme, mais à justifier et valider : simple similitude des mécanismes d’ingestion insuffisante. Risque de masquer les règles propres aux sujets ou de créer un domaine technique d’intégration. |

La seconde option est une proposition de représentation, pas l’affirmation qu’un univers ou un nouveau niveau a été adopté. La troisième option changerait la structure de la carte ; elle n’est pas appliquée par cette analyse.

## Contenu de la vue proposée

**Business References — Finalité proposée :** disposer des références externes décrivant les parties, articles, propositions commerciales et conditions contractuelles nécessaires aux opérations de la Supply.

| Sujet conservé | Aptitude actuelle dans la plateforme | Distinction à préserver |
| --- | --- | --- |
| Party / Role — D09 | Party / Role Ingestion — D09.d | Identité et rôles des parties. |
| Agreement — D11 | Agreement Ingestion — D11.a | Contrat de référence et conditions particulières ; distinct des commandes. |
| Product Reference — D08 | Product Reference Ingestion — D08.d | Identité de l’article et caractéristiques reçues ; un SKU peut être proposé dans plusieurs catalogues. |
| Catalog — D12 | Catalog Ingestion — D12.a | Catalogues et informations commerciales reçus, dont prix et zones selon U97. |

Ces quatre aptitudes restent séparées dans cette proposition. Leur regroupement visuel n’en crée pas une cinquième nommée ingestion générique, et n’impose pas quatre applications ou services. Les maîtres et les modèles gardent leurs identifiants et leurs autorités ; aucune administration, qualité des maîtres ou procédure de référencement n’est ajoutée dans FLOW.

Le libellé Business References est une construction locale. Master Data Management laisserait entendre un périmètre de maîtrise plus large que celui retenu. Reference Data peut également désigner un autre périmètre chez les éditeurs ; ne pas revendiquer de traduction native exacte de notre groupe, qui contient notamment les Agreements reçus.

## Conséquences et limites

P81 reste en version 0.7, avec onze domaines de travail et 35 aptitudes ; aucun renommage, fusion ou changement de rang appliqué. Les neuf capacités d’Order Promising restent validées. [Q075](../connaissance/06-questions.md#q075) conserve l’arbitrage de présentation/domaine ouvert ; U101 est une question, pas une décision.

Les données de prix, lieux et unités ne sont pas ajoutées automatiquement au groupe : leurs besoins de réception et autorités restent à préciser en Q071/Q072. Les décisions qui utilisent ces références demeurent dans leurs domaines consommateurs. Les comportements commerciaux restent dans le modèle processus, conformément à U100.

Sources textuelles publiques vérifiées le 11 septembre 2026, éditions et localisateurs détaillés en ELM099–ELM102. Le guide BIZBOK complet et les spécifications membres ODA n’ont pas été consultés. La preuve SAP concerne MDG, pas un rang du catalogue RBA. [CMP059](comparaisons.md#cmp059) conserve la portée de ces rapprochements.

## Complément U102 — cinquième référence

11 septembre 2026 : Laurent confirme Party ≠ lieu et demande **Fulfillment Network**. P81 passe à 0.8 avec le repère D13 et une ingestion proposée D13.a. Les trois options de cette étude portent désormais sur cinq références ; les tableaux précédents conservent le périmètre comparé en U101. Le nom Business References et son statut de groupe restent proposés, sans validation implicite de U102.

La Finalité du groupe proposé inclurait les références du réseau nécessaires aux opérations. [D13](../connaissance/25-domaines-coeur-et-epreuve-recits.md#d13-fulfillment-network) détaille les frontières ; [CMP060](comparaisons.md#cmp060) indique l’absence de comparaison précise du réseau complet. Ce cinquième sujet ne constitue pas une capacité générique d’ingestion supplémentaire ni un maître local de la logistique.
