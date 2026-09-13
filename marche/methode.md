# Méthode de comparaison et maintenance

Origine : demande U14. Cette méthode organise le travail documentaire ; elle n'adopte aucun standard comme architecture cible.

## Trois objets distincts

1. **Référence de marché (MKT)** : organisme, modèle, rôle, éditions et conditions d'accès.
2. **Élément externe (ELM)** : concept, règle, capacité, processus, composant ou donnée effectivement localisé dans une source.
3. **Correspondance (CMP)** : relation argumentée entre cet élément et un élément Beaumanoir, avec adaptations et décision.

Une page de présentation peut justifier le rôle d'un modèle. Elle ne suffit pas à attribuer une définition ou une couverture à ses éléments détaillés.

## Informations à conserver

| Objet | Champs obligatoires |
| --- | --- |
| Référence | ID local, nom, organisme, nature, rôle envisagé, source officielle, version ou inconnue, date de consultation, contenu réellement consulté, limites d'accès et de réutilisation connues |
| Élément externe | ID local, référence et édition, identifiant natif s'il existe, libellé natif, nature, définition consultée ou explicitement indisponible, reformulation séparée, localisateur précis, source et date |
| Correspondance | ID local, élément externe, élément Beaumanoir, version/état comparé, relation, contexte, adaptation proposée ou appliquée, justification, limite de preuve, statut, auteur, date ; valideur et date si validation |

Ne jamais fabriquer un identifiant natif, une version ou une définition. Pour une page évolutive sans édition, conserver date, titre et section ; la comparaison reste liée à cet état documentaire. Conserver des synthèses et des liens ; avant toute importation substantielle, relever les conditions de réutilisation du contenu concerné. L'accès public ne suffit pas à établir un droit de redistribution intégrale.

## Nature des relations

- **Équivalence** : résultat, périmètre et maille compatibles, vérifiés sur les définitions.
- **Plus large / plus étroit** : préciser lequel englobe l'autre et sur quelles dimensions.
- **Recouvrement partiel** : décrire intersection et différences.
- **Mobilise** : un processus mobilise une ou plusieurs capacités.
- **Appui sémantique** : un objet ou un terme éclaire le vocabulaire d'une capacité.
- **Appui méthodologique** : un principe éclaire la construction du modèle.
- **Piste lexicale** : ressemblance à examiner ; aucune équivalence établie.
- **Non comparé** : travail non réalisé ou source insuffisante ; ne signifie pas absent du marché.

Une relation peut être plusieurs-à-plusieurs. Ne pas imposer un seul équivalent externe à chaque CAP. Un écart peut révéler une différence de maille, de périmètre, un manque de connaissance ou un choix métier ; le qualifier avant d'en faire une anomalie.

## Niveaux de preuve

Distinguer systématiquement : source identifiée ; présentation consultée ; passage ou élément consulté ; rapprochement proposé ; correspondance validée. La confiance dépend de la définition disponible et du contexte, pas de la notoriété de l'organisme. Une proposition locale reste signalée comme telle, même si la source externe est un standard.

## Choisir éventuellement une structure principale

Comparer les candidats sur les mêmes cas : allocation/protection GBM, allocation B2B Boardriders, SAV Sarenza, réassort IRMA–Storeland et interface C-Log.

| Critère | Preuve attendue |
| --- | --- |
| Adéquation de l'objet | Véritable modèle de capacités ou transformation explicitement justifiée |
| Couverture | Articles, partenaires, achats, commandes, stocks, allocations, SAV ; interfaces et exclusions visibles |
| Lisibilité | Niveaux et granularité compréhensibles par le métier |
| Comparabilité | Variantes retail/B2B et contextes des trois SI représentables |
| Responsabilités | Possibilité de documenter information, décision et exécution sans confondre organisation et capacité |
| Indépendance des produits | Correspondance possible avec l'existant hétérogène et plusieurs réalisations cibles |
| Traçabilité et entretien | Définitions, identifiants, éditions, accès et conditions d'usage identifiés |

Ne pas calculer de classement global avant d'avoir ces preuves. SAP est un candidat à éprouver, pas un gagnant désigné. Les modèles de processus et de données complètent le contrôle sans être notés comme s'ils étaient des catalogues de capacités.

## Décrire une capacité avant sa réalisation

La définition réaffirmée par Laurent en U33 est le critère de construction : **ce que sait faire l’entreprise indépendamment de son organisation et de ses outils**. Une sous-capacité doit elle-même exprimer une aptitude durable dans le périmètre de sa capacité mère. Objets, opérations, règles et fonctionnalités de produit permettent de l’expliquer et de l’éprouver ; ils ne deviennent pas automatiquement des capacités. Responsabilités et contrats éclairent ensuite sa réalisation.

Le [glossaire métier](../connaissance/19-glossaire-metier.md) conserve les notions et verbes proposés, leurs limites et leur provenance. Distinguer les termes natifs de marché de nos formulations françaises ; une proximité lexicale ne vaut ni traduction officielle ni équivalence métier. Voir C33/C34 et CMP024/CMP025.

## Cycle de travail

À chaque création, fusion, scission ou changement de définition d'une capacité, consulter les éléments marché pertinents et actualiser ses correspondances ou son statut « non comparé ». À chaque nouvelle version d'une référence, conserver l'ancienne provenance, qualifier les changements et signaler les correspondances à revalider. Vérifier de nouveau les sources utilisées avant un arbitrage ou une publication ; consigner les contrôles dans le journal.

Une source inaccessible n'arrête pas les autres comparaisons. Enregistrer la limite, exploiter les passages réellement disponibles et laisser la conclusion ouverte. Aucune surveillance automatique n'est configurée ; l'entretien s'effectue au fil des itérations du projet.
