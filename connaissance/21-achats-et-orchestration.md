# Trois cas d’achat et place de l’orchestration

Date : 10 septembre 2026. Récit : [U48](01-contributions-utilisateur.md#u48), F140–F144. Analyse Codex A28/P75 ; **propositions à éprouver**, sans capacité ou frontière validée. Périmètre : achats du périmètre historique de Beaumanoir, sans extension automatique à Boardriders ou Sarenza.

## Ce que Laurent ajoute au récit

| Cas déclaré | Objet et partage des responsabilités décrits | Ce qui reste inconnu |
| --- | --- | --- |
| Fabrication complète par le fournisseur | La négociation en conception porte sur la fabrication complète. Le fabricant recherche les composants dans son réseau. PLM et MAP planifient les volumes et délais ; MAP envoie des « Planned Purchase Order ». | Destinataire et portée du document MAP, validation et engagement ferme. Conception PLM hors périmètre. |
| Produits finis sur catalogue | Beaumanoir achète des références dans un catalogue préconstruit par le fournisseur. | Cycle de commande, engagements et modalités de réception. L’analogie avec un wholesaler ne prouve pas un canal de revente B2B. |
| Fabrication à façon | Beaumanoir achète tissus et accessoires auprès de fournisseurs distincts et demande au façonnier la confection. Exemples de motifs : produits techniques ou plus haut de gamme mobilisant des fournisseurs spécialisés. | Propriété, détention et circuits des composants ; liens à la confection, consommations, pertes et reliquats ; engagement du façonnier. |

Ces cas complètent les achats jusque-là décrits principalement par la demande MAP et le suivi CBS. Ils ne prouvent pas que CBS opère les trois variantes. Planned Purchase Order est ici le terme rapporté par Laurent, sans assimilation à un document SAP ou Microsoft. [Q034](06-questions.md#q034) reste ouverte sur la fermeté de l’engagement ; [Q069](06-questions.md#q069) regroupe les points de fond de la fabrication à façon.

## Proposition sur l’orchestration

**Précision U49 du 10 septembre 2026 :** Laurent prévoit d’équiper les deux couches de moteurs de décision, détermination et orchestration, avec une orientation Case Management dans la couche processus. La formulation initiale réservant trop largement les moyens génériques à la couche haute est corrigée par C40. Même solution ou solutions distinctes : choix ouvert.

Pour la carte des capacités du socle, ne pas ajouter une boîte générique « Orchestration » sur la seule base d’un besoin d’enchaînement. Distinguer trois objets :

| Objet | Exemple illustratif dans la fabrication à façon | Traitement proposé |
| --- | --- | --- |
| Aptitude métier durable | Engager l’achat d’un bien ou d’une prestation ; connaître les ressources confiées à un tiers ; constater leur consommation. | Explorer le socle, avec résultat, objets et règles indépendants des organisations et outils. Ce sont des hypothèses de couverture, pas des fiches CAP validées. |
| Coordination métier d’un cas | Déterminer les travaux encore nécessaires, attendre des réponses, traiter un retard ou demander une décision avant de poursuivre. | Modèle de processus ou de situation dans la couche haute, avec ses propres objets et faits de traitement. Le scénario exact reste à décrire ultérieurement. |
| Moyens de décision, détermination et orchestration | Calculer, appliquer des règles et coordonner des opérations ; conduire un dossier avec tâches, événements et reprises selon la couche. | Moyens envisagés dans les deux couches selon U49, avec orientation Case Management dans la couche haute. Même solution possible, non décidée. |

La coordination spécifique n’est donc pas vidée de son sens métier parce qu’un moyen générique peut la supporter. Les deux couches conservent les modèles durables demandés par Laurent. Un moteur peut appliquer les règles de validité d’une consommation, d’un engagement d’achat ou d’une acceptation de prestation ; le domaine métier conserve le sens et l’autorité de ces règles, quel que soit leur support d’exécution.

U50 réaffirme la portée locale : la capability map cible la couche transactionnelle ; un autre modèle fonctionnel orienté processus décrira la couche processus. La coordination propre aux dossiers et situations sera décrite dans ce second modèle, avec les capacités du socle qu’elle sollicite. Les usages plus larges du terme Business Capability dans le marché ne constituent pas une extension du périmètre de notre carte.

Test pratique proposé : changer entièrement l’enchaînement, les intervenants et les logiciels. L’aptitude et son résultat conservent-ils leur sens ? Si oui, examiner une capacité ; si le libellé décrit surtout cet enchaînement ou un moteur, le documenter dans les vues de processus ou de réalisation. Le caractère transverse ne suffit ni à inclure ni à exclure une capacité.

## Ce que le marché permet d’affirmer

Sources primaires consultées le 10 septembre 2026. Les reformulations et adaptations locales sont séparées ; aucun processus de produit n’est importé comme hiérarchie de capacités.

| Référence et passage | Constat documentaire | Conséquence proposée pour notre travail |
| --- | --- | --- |
| **SAP RBA**, cours [Defining Business Architecture](https://learning.sap.com/courses/intelligent-enterprise-architecture-fundamentals/defining-business-architecture), passage sur les modèles métier et de solution ; édition du cours/catalogue non précisée. ELM002. | SAP distingue aptitude métier, activités qui la mobilisent et moyens logiciels qui la soutiennent. | Distinguer la capacité, sa coordination et la fonctionnalité d’orchestration ; le cours ne prescrit pas notre architecture à deux couches. |
| **OMG BPMN 2.0.2**, janvier 2014, [§7.2.1, page imprimée 21](https://www.omg.org/spec/BPMN/2.0.2/PDF). ELM042. | Les processus sont présentés sous l’angle de l’orchestration. Des modèles privés exécutables et non exécutables sont distingués ; collaboration et chorégraphie apportent d’autres vues. | L’orchestration a un sens de processus avant son automatisation. BPMN ne statue pas sur son classement en capacité métier. Aucun modèle BPMN à produire à cette étape. |
| **SAP S/4HANA Cloud**, [Outlining Subcontracting](https://learning.sap.com/courses/detailing-subcontracting-and-supplier-consignment/outlining-subcontracting_af403e3e-188d-4dbb-bde1-632253739fa6), introduction et Applicable Process Steps ; édition produit non précisée. ELM043. | La sous-traitance décrite relie une commande, des composants fournis, leur stock chez le fournisseur et leur consommation à la réception du résultat. | Le cas à façon appelle des questions sur les engagements et les ressources, au-delà du déroulement. Ce comportement de produit ne prouve pas l’existant Beaumanoir. |
| **Microsoft Dynamics 365 SCM**, [Manage subcontracting work in production](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/manage-subcontract-work-production), introduction, Subcontracting of route operations et paragraphes sur le stock au site fournisseur ; page du 13 août 2025. ELM044. | La documentation articule achat de service, opérations sous-traitées et mise à disposition des matières ; les variantes de production ont des représentations différentes. | Conserver des aptitudes génériques et qualifier les réalisations. Ni les ordres de production ni les modèles de données Microsoft ne deviennent des exigences locales. |

La conclusion est une recommandation de modélisation fondée sur ces distinctions, pas une règle de marché interdisant toute capacité de coordination. Les références de processus et de produit décrivent comment réaliser un besoin ; elles n’établissent pas seules la maille d’une capability map.

## Ce que les trois cas peuvent changer dans les capacités

Une variante d’achat peut mobiliser les mêmes aptitudes avec des objets, règles et engagements différents. La fabrication à façon peut également révéler une aptitude absente du catalogue. Il faut départager ces possibilités par les résultats attendus.

| Aptitude à examiner — formulation proposée | Finalité | Appui local et question de maille |
| --- | --- | --- |
| Formaliser un besoin d’achat et engager un achat de bien ou de prestation | Obtenir une fourniture identifiée dans des conditions convenues. | U48 enrichit CAP029 sur l’émission d’une demande ; cette fiche ne couvre pas encore un engagement ferme. Unifier ou distinguer biens et prestations reste à éprouver. |
| Connaître les ressources confiées à un tiers | Savoir quelles ressources restent utilisables, par qui et pour quel besoin. | Piste issue du cas à façon et des produits examinés. CAP004/CAP005 éclairent stock et visibilité ; aucune extension de leur périmètre ni propriété des matières affirmée. |
| Déterminer les composants nécessaires à une confection donnée | Établir le besoin de ressources correspondant au résultat attendu. | Hypothèse à confirmer : la composition et les quantités peuvent être fournies par l’amont. Définition produit et planification de saison restent hors domaines du périmètre. |
| Rapprocher composants mis à disposition, consommations et résultats reçus | Expliquer la transformation des ressources et les écarts. | Piste à partir du cas et du marché, sans pratique locale démontrée. Examiner les résultats distincts avant une éventuelle décomposition ; Q069. |

Les verbes et résultats de ce tableau servent à l’exploration, sans créer une capacité pour chaque opération. La couche processus peut solliciter ces aptitudes et enregistrer le traitement d’un retard ; les domaines concernés conservent les faits et règles de leurs ressources et engagements.

Exemple hypothétique : les tissus sont disponibles mais les accessoires manquent. Le processus peut attendre, relancer ou solliciter une décision. Déterminer ce qui manque, ce qui est déjà affecté et ce qui peut être engagé requiert une connaissance métier des ressources et du besoin. La règle autorisant une confection partielle doit être explicitée ; elle ne se déduit ni d’une temporisation ni du choix d’un moteur.

## Effet sur la première liste de domaines

U48 donne désormais trois cas concrets pour éprouver **Achats opérationnels** dans la [première liste](20-domaines-candidats.md). L’achat à façon mobilise aussi les problèmes de stock, d’engagement de ressources et de prestation ; il ne justifie pas automatiquement un domaine distinct « Fabrication à façon » ou « Orchestration ». Les trois modalités peuvent rester des cas d’épreuve traversant plusieurs domaines.

[CMP029](../marche/comparaisons.md#cmp029) trace le raisonnement sur l’orchestration ; [CMP030](../marche/comparaisons.md#cmp030) les apports de sous-traitance et le rapprochement partiel de CAP029. Les autres aptitudes proposées ne sont pas des équivalences de capacités établies. Aucun processus détaillé ni choix d’urbanisation supplémentaire n’est engagé.
