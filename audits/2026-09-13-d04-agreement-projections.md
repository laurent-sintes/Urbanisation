# Audit D04, Agreement et projections de référence

Date : 13 septembre 2026. Source de la demande : U134. Périmètre : backlog structuré et release Urbanisation v002, publication 2026-09-13.4. Analyse interne du modèle ; aucune nouvelle vérification de documentation éditeur. Les recommandations de découpage et de libellés sont **proposées par l’IA**.

## Conclusion

D04 Commercial Commitments et D11 Agreement ne décrivent pas actuellement le même objet : le premier porte les engagements propres aux commandes, le second les contrats de référence reçus. Cette distinction répond à U98. En revanche, les capacités de D04 attribuent potentiellement à la Supply des responsabilités commerciales insuffisamment justifiées. Le réexamen D04/D07 demandé en U100 n’est pas achevé ; des noms raccourcis ne résolvent pas cette difficulté.

Les cinq référentiels respectent la maîtrise externe dans leurs définitions et périmètres. Ils ne montrent toutefois que l’ingestion : la visibilité et la recherche ne sont pas exprimées comme aptitudes. U134 remplace la restriction antérieure « ingestion seule » par un principe de projections consultables, avec au moins une ingestion chacune. Ce principe est consigné en C75, dans AGENTS.md et dans le JSON backlog.

## Ce qui est réellement différent

| Élément | Question couverte | Autorité dans notre modèle |
| --- | --- | --- |
| Agreement de référence | Selon quel cadre contractuel peut-on commander : parties, catalogues, conditions particulières ? | Source de vérité externe ; projection reçue par la Supply. |
| Commande ou document d’autorisation | Quelles marchandises est-on autorisé à déplacer, pour cette demande et dans quelles limites ? | Distinction avec Agreement acquise ; auteur, révision et révocation à préciser pour chaque situation. |
| État transactionnel de la Supply | Qu’a-t-on pris en charge, promis, affecté ou réalisé, et que reste-t-il à exécuter ? | Responsabilités à répartir entre domaines de la Supply et exécutants ; ce n’est pas un référentiel contractuel. |

Exemple hypothétique : un Agreement donne accès à un catalogue sous certaines conditions. Une commande autorise 100 pièces. Après réalisation de 60 pièces, il peut rester 40 pièces à exécuter, hors modification ou autre règle. Enregistrer les 60 pièces réalisées ne modifie pas les conditions de l’Agreement ; recevoir l’Agreement ne crée pas la commande. Les modalités juridiques de formation d’un contrat ne sont pas l’objet de cette distinction de modèle.

## Audit des capacités de D04

Les quatre capacités ci-dessous et la définition de D04 sont identiques dans le backlog examiné et dans la release v002. Elles restent en cours d’instruction ; aucune validation globale de ce domaine n’est établie.

| Capacité courante | Constat | Traitement proposé |
| --- | --- | --- |
| D04.a Commitment Creation | « Établir l’engagement propre à une commande » peut signifier créer la commande commerciale ou accepter sa prise en charge par la Supply. Ce sont deux responsabilités différentes. | Préciser l’autorité. Si la commande vient d’un tiers, distinguer réception de l’autorisation et prise en charge transactionnelle, cette dernière à rapprocher de D07.b. |
| D04.b Commitment Revision | Modifier ou éteindre une obligation commerciale ne relève pas nécessairement de la Supply. | Distinguer réception d’une révision autorisée, traitement de ses conséquences et droit de décider la modification. Ne pas confondre avec Promise Revision. |
| D04.c Commitment Reconciliation | Connaître les obligations restantes peut être utile au socle. Son objet se rapproche cependant du rapprochement des attentes et réalisations de D07.c. | Éprouver la différence entre reliquat autorisé et réalisation d’exécution. Conserver deux capacités seulement si leurs résultats et règles sont distincts. |
| D04.d Return and Replacement Decision | « Donner effet à une solution commerciale admissible » mêle potentiellement décision de recours commercial et faisabilité Supply. | Identifier qui autorise retour ou remplacement. La Supply peut appliquer l’autorisation et décider de sa réalisation sans décider elle-même du droit commercial au recours. |

La règle des projections de référence ne démontre pas, à elle seule, que toutes les commandes sont maîtrisées à l’extérieur. Il faut donc instruire ces autorités avant de transformer toutes les capacités de D04 en ingestion ou de les supprimer.

**Recommandation : ne pas fusionner D04 avec Agreement.** Reprendre D04 avec D07 autour des autorisations reçues et des engagements opérationnels. Un espace problématique provisoirement nommé **Supply Authorizations** pourrait être examiné, sans présumer qu’un domaine autonome est nécessaire. Ce nom et cette frontière sont proposés par l’IA ; aucune substitution n’est effectuée dans la carte.

## Audit des cinq référentiels

| Référentiel | Ingestion présente | Maîtrise externe | Consultation explicite dans la carte |
| --- | --- | --- | --- |
| D09 Party / Role | D09.d Party / Role Ingestion | Champ mastership et périmètre explicites. | Absente. |
| D11 Agreement | D11.a Agreement Ingestion | Champ mastership et périmètre explicites. | Absente. |
| D08 Product Reference | D08.d Product Reference Ingestion | Définitions et périmètre explicites ; pas de champ mastership homogène aux trois autres. | Absente. |
| D12 Catalog | D12.a Catalog Ingestion | Champ mastership et périmètre explicites. | Absente. |
| D13 Fulfillment Network | D13.a Fulfillment Network Ingestion | Réception externe explicite ; maître précis inconnu, champ mastership absent. | Absente. |

Les cinq ingestions excluent déjà l’administration et la validation des données maîtresses. Le manque concerne l’expression de leur accès et l’homogénéité des métadonnées de maîtrise, pas un constat de capacités d’administration indûment présentes dans ces cinq domaines.

**Pattern minimal proposé : Ingestion + Visibility**, la recherche étant d’abord comprise dans Visibility. Les noms candidats seraient Party / Role Visibility, Agreement Visibility, Product Reference Visibility, Catalog Visibility et Fulfillment Network Visibility. Leur résultat durable serait de retrouver et consulter la référence applicable avec son contexte et sa provenance. Une capacité Search autonome ne serait utile que si l’analyse fait apparaître un résultat métier distinct ; un écran ou une opération d’API ne suffit pas.

Ces cinq candidats restent dans cet audit, au statut **Proposé par l’IA**. Le modèle conserve ses 36 capacités : la demande d’audit ne vaut pas adoption de cinq ajouts. Leur correspondance marché détaillée n’est pas encore examinée ; aucun rang natif éditeur n’est revendiqué.

## Règles à préserver

- **Lecture seule pour les consommateurs** : l’ingestion peut créer, actualiser ou invalider la copie locale selon les informations du maître. Cela ne donne pas à la plateforme le droit de corriger la donnée maîtresse ou d’inventer sa propre version contractuelle.
- **Décisions dans les domaines consommateurs** : appliquer un prix reçu, une condition ou une restriction pour produire une promesse n’est pas administrer Catalog ou Agreement. Le résultat de la décision appartient à son domaine transactionnel.
- **Contrôle de réception distinct de validation métier** : contrôler le format, la version ou une référence reçue ne revient pas à certifier ou à dédoublonner le référentiel maître. Aucun domaine Data Quality supplémentaire n’est déduit de ce besoin.
- **Sources à qualifier** : préciser ultérieurement source de vérité, portée, identifiant externe, version, validité et fraîcheur utiles. CRM, SRC et PLM sont les exemples de U134, sans preuve de maîtrise installée par attribut. Le sigle SRC n’est pas assimilé à SRM sans confirmation.
- **Modèles distincts** : Party n’est pas un lieu ; Product Reference reste autonome des catalogues ; les références sont reliées par identifiants. La projection du réseau ne contient pas par défaut le stock, la charge ou l’itinéraire décidé.
- **Compteurs contractuels** : distinguer un reliquat de contrat reçu du maître et un calcul opérationnel local. Suivre une consommation ne donne pas le droit de modifier le plafond contractuel. Q072 reste ouverte.
- **Périmètre plateforme** : l’entreprise sait administrer ses références via d’autres produits ; leur exclusion de la vue Supply ne signifie pas leur absence à l’échelle de l’entreprise.

## Frontières à instruire ensuite

Q074 accueille déjà la question des autorisations, engagements et faits entre D04, D07 et couche processus. La prochaine revue doit déterminer qui peut émettre, réviser et révoquer une autorisation commerciale, puis quel état la Supply conserve pour l’appliquer. D03 garde les décisions de promesse ; D01 les états et mouvements de stock ; D07 les engagements et faits d’exécution. Ces repères guident l’examen sans résoudre automatiquement tous les recouvrements.

Q072 conserve les autorités de prix et de consommation contractuelle ; Q076 conserve les sources et le contenu du réseau. Aucune de ces questions n’est fermée par le présent audit. Les documents et objets seront précisés ensuite, sans imposer un document universel ou un découpage logiciel.

## Sources et traçabilité

- [Contributions utilisateur](../connaissance/01-contributions-utilisateur.md) : U97/U98, U100, U102/U103 et U134.
- [Correction C75](../connaissance/04-corrections.md) : évolution de la règle d’ingestion seule.
- [Supply, documents et autorisations](../connaissance/26-supply-documents-autorisations.md) : réexamen D04/D07 déjà identifié en U100.
- [Audit marché du 11 septembre](2026-09-11-modele-marche-achats-ventes-referentiels.md) : distinction références, commandes et décisions ; recommandations historiques à relire avec U100/U134, sans nouvelle vérification externe ici.
- [Questions ouvertes](../connaissance/06-questions.md) : Q072, Q074, Q076.
- [Backlog structuré](../modeles/backlog/model.json) et [release examinée](../modeles/release/2026-09-13.4/model.json).

Les nouvelles recommandations restent dans le backlog documentaire. Aucune capacité renommée, fusionnée ou ajoutée ; aucune release publiée.
