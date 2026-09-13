# BIZBOK : capacités, objets métier et domaines

10 septembre 2026 — approfondissement de [U60](../connaissance/01-contributions-utilisateur.md#u60), F160/F161, A36/P79 et [CMP034](comparaisons.md#cmp034). Complément de la [comparaison des regroupements](premier-niveau-regroupement-capacites.md), selon la [méthode de provenance](methode.md).

**BIZBOK est un appui solide pour définir et décomposer les capacités. Les textes consultés privilégient toutefois un objet métier central, tandis que nos domaines rassemblent des problèmes liés.** L’usage conjoint est proposé ; aucun catalogue principal ni changement de structure locale adopté.

## Ce qui a été consulté de plus

| Source officielle | Version et passages | Ce qui est établi |
| --- | --- | --- |
| [Glossaire BIZBOK](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_glossary.pdf) | 15.0, ©2026 ; pages 456–457, PDF 4–5 | Définitions capacité/service, instance, niveau et catégorie. ELM052. |
| [Introduction BIZBOK](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok15/BIZBOKv15_introduction.pdf) | 15.0, ©2026 ; pages 3, 6, 12, 15–17 | Positionnement et présentation des chapitres, sans leur contenu détaillé. ELM054. |
| [Metamodel Guide](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf) | 3.0, septembre 2024 ; §§3, 5, 5.2 | Objet central, décomposition et distinction avec la réalisation contextuelle. ELM053. |
| [Atelier de référence](https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/baguild_ref_model_workshop_a.pdf) | 20 juin 2019 ; pages 15–21 | Principes et exemples de décomposition, réexaminés ; source historique explicite. ELM021. |
| [Notices des modèles](https://learning.businessarchitectureguild.org/indref) | État consulté le 10 septembre 2026 | Livrables annoncés et conditions d’accès, sans téléchargement des modèles membres. ELM055. |

Les ouvertures précédentes en échec sont conservées dans l’historique. Le CDN officiel permet maintenant la lecture de ces extraits publics ; le guide BIZBOK complet et les modèles membres restent non consultés. La page [Free Resources](https://learning.businessarchitectureguild.org/free-resources) autorise explicitement la distribution des deux extraits introduction/glossaire aux non-membres ; nous conservons ici une synthèse et des liens.

## Ce qui rejoint notre définition

Le glossaire 15.0 distingue l’aptitude de sa réalisation dans une unité ou une situation donnée. Il distingue également le service décrit dans une lecture SOA de la capacité. Une aptitude peut viser un résultat : cette propriété seule ne transforme donc pas une capacité en service ou en produit. Les différences de contexte ou d’outil ne suffisent pas à créer une nouvelle aptitude. [ELM052]

Pour notre projet, cela conforte le travail sur une définition indépendante des marques, organisations et applications. Les variantes du périmètre historique de Beaumanoir, de Boardriders et de Sarenza peuvent ensuite éclairer cette aptitude. Ce rapprochement ne valide ni les définitions candidates ni leurs frontières.

## La différence structurante : objet central et espace de problèmes

Le Metamodel Guide explique que les sous-capacités gardent le périmètre de l’objet du parent. Dans son exemple client, elles ne prennent pas en charge la gestion des produits ou des accords. Il distingue les capacités de leurs réalisations contextuelles. Le terme Domain y désigne des perspectives telles que capacité, information ou organisation ; il ne fournit pas une nomenclature de domaines Stock ou Promesse. [ELM053]

La conséquence proposée pour nous est de conserver deux questions distinctes :

- **Pour délimiter un domaine :** quels problèmes sont liés au point de justifier leur étude commune ?
- **Pour définir une capacité :** quelle aptitude durable, portant sur quels objets, avec quel résultat et quelles limites ?

Le domaine Order Promising peut nécessiter d’examiner ensemble demande, ressources admissibles, protection et engagement. Le modèle de la Guild incite à préciser l’objet central des aptitudes qui interviennent. Il ne nous impose pas de fusionner ces objets, de transformer tout le domaine en une capacité mère, ni de le scinder automatiquement. Aucun découpage officiel Guild d’Order Promising n’a été consulté : cette application est une analyse locale.

## Niveaux et granularité

Dans le glossaire 15.0, Level indique une profondeur de décomposition ; Tier classe les capacités selon leur rôle stratégique, cœur ou support. Les deux axes sont différents. [ELM052]

L’atelier 2019 illustre par exemple Customer Management → Customer Information Management → Customer State Management. Il propose aussi des motifs de définition et de rapprochement, avec un objet principal préservé même lorsqu’il est relié à d’autres objets. Les exemples sont datés ; leur présence ne prouve pas un catalogue 2026 identique. [ELM021]

Pour notre glossaire et nos candidats stock, nous pouvons ainsi vérifier le sens d’enregistrer, qualifier, rapprocher ou modifier, sans générer une capacité par verbe ni recopier une liste d’opérations. Notre colonne Finalité reste pertinente ; les natures proposées ne sont pas remplacées par ces motifs.

## Modèles de référence et contenu retail

Le Common Reference Model est un livrable proposé aux membres, avec des capacités et des flux de valeur transsectoriels. Sa notice ne donne pas sa version courante. Le Companion Guide v3.0 est un autre livrable ; son numéro ne doit pas être attribué au modèle. Les téléchargements supposent statut membre et licence. [ELM055]

**Une équipe Retail/Wholesale est identifiée, mais la livraison d’un modèle, sa version et son contenu ne sont pas établis par les sources publiques examinées.** La liste publique et la présentation de la partie 8 de BIZBOK 15.0 ne montrent pas de modèle retail ; cela ne prouve pas son inexistence. Le contenu du Common Reference Model n’est pas une carte stock/promesse retail vérifiée. [ELM054/ELM055]

La publication décrit aussi l’articulation de l’architecture métier avec processus et Case Management ; elle annonce notamment les sections de construction des capacités et les modèles de référence. Ces annonces donnent des pistes de lecture, sans preuve de leur détail. [ELM054]

## Rôle retenu pour la suite de la comparaison

U60 conduit à conserver IBM comme historique, sans le mobiliser comme référence actuelle prioritaire. La réserve sur BIAN le place en périphérie de notre travail sur les capacités ; TM Forum demeure une piste intéressante.

P79 propose de garder SAP comme première grille d’épreuve de la maille et du contenu commerce, puis d’utiliser BIZBOK pour contrôler la qualité des aptitudes et de leur décomposition. Pour chaque candidat, vérifier objet(s), résultat, périmètre, lien au domaine et distinction avec sa réalisation. L’objet central n’est pas adopté comme unique critère de découpage de nos domaines.

La Guild vise une architecture métier d’ensemble. Notre capability map reste centrée sur le socle transactionnel ; le modèle processus est distinct. La logistique reste hors développement FLOW, en adhérence. Ni acquisition membre, ni extension du périmètre, ni catalogue principal décidés. Les capacités candidates et leurs statuts sont conservés.

## Complément U61 : objets, faits et documents

La [comparaison SAP/Guild/TM Forum](../connaissance/24-capacites-objets-et-faits.md) approfondit les liens capacité/information/états/résultats en ELM057 et distingue ces notions des documents et notifications. Elle propose d’expliciter leur sens pendant l’analyse métier, sans dériver automatiquement des agrégats ni une persistance depuis la carte. Les choix locaux de U61 restent distincts du vocabulaire des références.
