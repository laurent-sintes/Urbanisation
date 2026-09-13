# Correction des frontières de maîtrise des référentiels

11 septembre 2026 — U97/U98, F203–F208, A69, C64, P85. Audit d’application d’une instruction locale ; aucune recherche de marché nouvelle.

## Décision appliquée

Party / Role, Agreement et Catalog restent trois référentiels distincts, reliés par identifiants et maîtrisés hors plateforme. Trois domaines contigus exposent chacun une capacité d’ingestion. Pas d’administration, vérification métier, dédoublonnage, enregistrement ou recrutement dans ces domaines. Les commandes restent distinctes des Agreements selon U98. Les neuf capacités d’Order Promising validées demeurent ; elles utilisent les références reçues.

## Repères et état remplacé

Les neuf capacités D08.a–c, D09.a–c et D10.a–c sont retirées de la vue plateforme, pas effacées de la provenance. D09 conserve son identité de domaine des parties et devient Party / Role ; sa nouvelle aptitude est D09.d. D11 Agreement et D12 Catalog reçoivent de nouveaux repères, sans réutiliser D08 ou D10 pour des concepts différents. D08 et D10 deviennent des repères retirés de la carte active. P81 passe de 40 à 34 capacités : neuf retraits et trois ingestions. Dix domaines actifs, dont les trois référentiels contigus dans l’ordre D09/D11/D12 ; les nombres des repères ne dictent pas l’ordre de lecture.

Les blocs suivants sont l’état historique remplacé de la version 0.5 ; ils ne sont plus la carte courante.

### D08 — Product Information Management

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D08.a | **Identify items and components** : distinguer les biens et leurs références utiles aux opérations. | Relier sans ambiguïté achats, stocks et ventes. |
| D08.b | **Qualify operational product characteristics** : établir les propriétés et restrictions nécessaires aux usages opérationnels. | Rendre les biens utilisables dans les décisions du socle. |
| D08.c | **Determine applicable units of measure and packaging configurations** : définir les quantités et conversions pertinentes entre formes d’achat, de détention et de fourniture. | Éviter de traiter comme équivalentes des quantités exprimées différemment. |

**Objets :** article à la maille référence/taille/couleur, composant, référence fournisseur, unité, conditionnement. Les unités et conversions constituent un complément plausible du cas tissus/accessoires ; leurs règles locales ne sont pas racontées. Les compositions nécessaires à une confection peuvent venir du PLM ; leur création et le design produit restent hors périmètre.

**Provenance :** U02/U06/U48 ; CAP001. **Marché :** thème produits repéré dans l’[étude U25](../marche/etudes/2026-09-09-modeles-marche/etude-comparative.md#5-contenu-commerce-les-récurrences-effectivement-observées). Les trois définitions proposées ne sont pas encore comparées individuellement.

<a id="d09-parties-et-relations"></a>

### D09 — Party Management

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D09.a | **Identify parties to business operations** : distinguer les personnes ou organisations intervenant dans les fournitures. | Relier les engagements et les droits aux bonnes parties. |
| D09.b | **Qualify party roles and relationships** : établir qui achète, vend, détient, reçoit ou réalise une prestation et les relations applicables. | Distinguer des responsabilités que le seul lieu ou canal ne décrit pas. |
| D09.c | **Determine commercial relationship eligibility** : appliquer les restrictions connues sur la possibilité de contracter ou de servir une partie. | Prendre des engagements avec les parties admissibles. |

**Objets :** partie, rôle, relation et restriction applicable. Les rôles métier ne sont pas des rôles RBAC. La sortie d’un mauvais payeur mentionnée en U10 justifie d’examiner l’admissibilité, sans importer recouvrement, scoring ou politique de crédit. Les relations entre sociétés sont distinctes de la topologie des lieux D06 ; un transfert ne se caractérise pas seulement par sa facture.

**Provenance :** U03/U10/U48/U53 ; CAP002. **Marché :** partenaires repérés dans l’étude ; domaine et aptitudes non comparés précisément. Les règles d’identité et d’éligibilité restent peu étayées.

<a id="d10-conditions-commerciales"></a>

### D10 — Commercial Terms

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D10.a | **Define applicable commercial terms** : établir les règles, valeurs et périodes régissant une fourniture. | Donner une référence aux accords commerciaux. |
| D10.b | **Determine transaction prices and terms** : identifier les règles applicables aux parties, biens et circonstances considérés. | Former une proposition ou un engagement cohérent avec ses conditions. |
| D10.c | **Determine post-supply entitlements** : qualifier les conditions de reprise, remplacement ou autre correction commerciale admissible. | Éclairer les décisions de service après-vente. |

**Objets :** condition, prix applicable, règle de droit, période de validité. D04 conserve les conditions effectivement convenues et autorise les effets sur les engagements ; D10 qualifie les règles et droits. Un régime détaillé de taxes, paiements ou conformité n’est pas inclus. Ce domaine est **le moins étayé** ; une réunion avec D04 est une alternative raisonnable tant que ses connaissances propres ne sont pas mieux décrites.

**Provenance :** CAP003, P29/P53, U01/U02 ; contenu détaillé proposé. **Marché :** sujet repéré dans les parcours commerciaux ; aucune comparaison précise des trois aptitudes réalisée. Ne pas présenter la liste comme des pratiques installées.

## Limites préservées

Les caractéristiques des articles nécessaires aux opérations restent des informations à recevoir ; aucun domaine de création PIM n’est conservé par défaut. La source précise par attribut reste à documenter. L’application opérationnelle des conditions, droits ou prix ne doit pas être confondue avec l’administration ou la vérification des références. Aucun moteur de pricing ou domaine de décision supplémentaire ajouté.

Le cycle des commandes de D04 reste une proposition distincte ; sa création/révision n’est plus étendue aux Agreements. Les autorités transactionnelles détaillées sont ouvertes. Q010 reçoit une réponse partielle sur l’orientation de maîtrise externe ; les applications installées et autorités par attribut ne sont pas prouvées.

Les définitions des CAP001–CAP003 restent comme provenance historique ; leur statut de périmètre est corrigé pour exclure la maîtrise de ces référentiels par la plateforme. Les 33 autres fiches CAP ne sont pas modifiées. Archives conservées intactes.

## Historique D04 remplacé — version 0.5

### D04 — Commercial Commitments

| Repère | Capacité proposée et résultat attendu | Finalité |
| --- | --- | --- |
| D04.a | **Establish a commercial commitment** : formaliser les parties, biens ou prestations, quantités, conditions et degré de fermeté convenus. | Donner une référence aux obligations d’achat, de vente ou de prestation. |
| D04.b | **Amend commercial obligations** : modifier ou éteindre les engagements selon les règles applicables en conservant leur histoire. | Faire évoluer un accord sans perdre ses effets ni ses références. |
| D04.c | **Determine commitment fulfillment and remaining obligations** : rapprocher les obligations des réalisations et corrections qui leur sont imputables. | Connaître ce qui reste dû après réalisation partielle ou modification. |
| D04.d | **Authorize a return or replacement** : déterminer les droits applicables et les obligations correctives qui en résultent. | Donner effet à une solution commerciale admissible après fourniture. |

**Objets et faits :** engagement d’achat, de vente ou de prestation, accord modifié, autorisation de reprise, réalisation imputée. Le regroupement traite les obligations ; il ne fusionne ni achats et ventes ni les dossiers de processus. D10 détermine les conditions applicables ; D04 porte celles retenues dans l’engagement. D03 porte la promesse de fourniture ; D07 les engagements de réalisation. Les faits utiles à la finance restent des interfaces, sans facturation, encaissement ou remboursement développés par cette carte.

L’achat ferme dépasse l’émission d’une Planned Purchase Order connue dans le récit ; Q034 reste ouverte. D04.d maintient les effets du SAV visibles, avec faible preuve de détail. Un domaine autonome de droits après fourniture reste une option si garanties, admissibilité et obligations correctives forment un espace de problèmes assez riche.

**Provenance :** U01/U02/U03–U05/U48/U53/U54 ; CAP003/CAP014/CAP029–CAP034. **Marché :** ELM029/ELM043/ELM044/ELM047 et étude U25 : appuis partiels pour commandes, sous-traitance et retours. **Le domaine commun achat/vente/prestation n’est pas comparé précisément à un domaine standard.**

#### Première revue Commercial Commitments — U96

**Statut : proposition P84, 11 septembre 2026.** Nom et frontières du domaine à challenger ; aucune adoption après la seule demande de poursuivre. Les quatre lignes historiques ci-dessus sont conservées. La définition des capacités demeure indépendante de l’organisation et des outils.

**Finalité proposée :** établir et maintenir une connaissance explicite des engagements commerciaux et de ce qui reste à accomplir entre les parties.

**Espace problématique :** qui s’est engagé envers qui, à fournir ou acquérir quoi, selon quelles conditions ? Que devient cet engagement après une modification, une réalisation partielle ou un retour ? Le lien entre ces problèmes tient aux mêmes parties, obligations, conditions convenues, règles de changement et imputations des réalisations.

| Nom proposé | Nature de contribution | Ce que sait faire l’entreprise | Finalité | Repère historique |
| --- | --- | --- | --- | --- |
| **Commitment Creation** | Action | Établir un engagement commercial en précisant parties, biens ou prestations, quantités, conditions convenues et degré de fermeté. | Disposer d’une référence partagée sur ce qui est convenu. | D04.a |
| **Commitment Revision** | Action | Modifier ou éteindre tout ou partie d’un engagement selon les règles et accords applicables, en préservant son histoire et ses effets. | Faire évoluer les obligations sans perdre leur continuité. | D04.b |
| **Commitment Reconciliation** | Action de rapprochement | Rapprocher les obligations des réalisations, annulations et corrections qui leur sont imputables pour établir ce qui reste dû. | Connaître les obligations encore ouvertes. | D04.c |
| **Return and Replacement Decision** | Décision | Décider si un retour ou remplacement peut être autorisé et quelles obligations correctives en résultent selon les droits, les faits et les accords applicables. | Donner une réponse commerciale admissible après fourniture. | D04.d |

Les trois premières lignes ne sont pas une séquence de processus obligatoire. Commitment Reconciliation établit une situation à partir des faits ; un calcul n’est pas une nouvelle capacité de décision par son seul nom. L’acceptation initiale et l’acceptation d’une modification demandent des règles et des autorités explicites ; leur autonomie de capacité reste à examiner, sans ajouter une décision à chaque opération.

#### Marché et couverture de cette première vue

[ELM085](../marche/elements.md#elm085), [ELM086](../marche/elements.md#elm086), [CMP053](../marche/comparaisons.md#cmp053), vérifiés le 11 septembre 2026. Le nombre quatre vient de notre proposition P81 ; aucun catalogue externe de quatre capacités équivalentes n’est démontré.

| Objet comparé | Ce que le corpus de marché apporte | Écart ou limite pour D04 |
| --- | --- | --- |
| Nom de domaine | SAP distingue Sales Order Management et Purchase Order Management ; Microsoft distingue Sales agreements et Purchase agreements, outre les commandes. | Commercial Commitments reste un regroupement local. Les ressemblances entre achats et ventes ne prouvent pas qu’il faille fusionner leurs modèles. |
| Création et changement | Accords Microsoft avec engagements, validité, conditions, modifications et historique. | Appui partiel aux deux premières capacités ; accord-cadre et commande ne sont pas identiques. Ne pas confondre confirmation documentaire du produit et prise d’engagement métier. |
| Rapprochement et reste | Suivi Microsoft de la consommation des engagements et du reliquat. | Appui à Reconciliation ; commande imputée sur accord et livraison imputée sur commande sont des relations différentes. La page produit ne définit pas une règle locale universelle de calcul. |
| Retour et remplacement | Microsoft distingue autorisation, réception/inspection et suite donnée au retour. | Le dernier candidat est large ; séparer l’autorisation de renvoyer, l’acceptation du retour et le choix du remède avant de décider d’une décomposition. Facturation et remboursement restent hors domaine. |
| Structure | TM Forum identifie Agreement Management, Product Order Capture & Validation et Purchase Management comme composants distincts, ELM065. | Appui antérieur limité ; pas nouvelle lecture du catalogue. BIZBOK ne fournit pas dans notre corpus un domaine retail commun équivalent démontré. |

#### Épreuve par les récits

| Cas | Accueil proposé | Point restant à éclaircir |
| --- | --- | --- |
| Fabrication complète fournisseur, périmètre historique de Beaumanoir — U48 | Engagement d’achat des produits finis et conditions retenues. | La Planned Purchase Order MAP n’est pas une preuve d’engagement ferme ; Q034 demeure ouverte. |
| Achat de produits sur catalogue — U48 | Même aptitude d’engagement, sur des références déjà proposées par le fournisseur. | Les différences de parcours ne créent pas automatiquement une autre capacité. |
| Fabrication à façon — U48 | Engagements sur composants et prestation de confection, avec obligations liées mais distinctes. | Ne pas fusionner les obligations de fournisseurs différents ; propriété, consommations et reliquats à préciser, Q069. |
| Réassort entre sociétés distinctes — U53 | Lecture commerciale des obligations de part et d’autre, reliée au même besoin de fourniture. | Un transfert interne n’engendre pas automatiquement achat et vente ; les règles d’intercompany restent à documenter. |
| Commande et réexamen prioritaire Boardriders — U30/U31 | Engagement commercial D04 lié à une promesse révisable D03. | Réviser une promesse ne réécrit pas automatiquement l’accord commercial ; effets et information du processus à préciser. |
| Retours et SAV Sarenza — périmètre initial | Point d’accueil D04.d pour les droits et obligations correctives. | Couverture seulement partielle : les règles d’admissibilité et remèdes ne sont pas décrits avec assez de précision. |

#### Frontières à éprouver

- **Order Promising — D03 :** proposition et engagement de fourniture en quantité/date, couverture et révision ; D04 porte les obligations commerciales. Leur distinction n’impose pas deux documents ni deux engagements sans lien. Un même fait de confirmation peut contribuer aux deux vues, avec des effets à expliciter. La validation U95 n’est pas remise en cause.
- **Commercial Terms — D10 et Party Management — D09 :** règles et conditions applicables, identité et admissibilité des parties ; D04 porte celles retenues pour l’engagement. Identifier le propriétaire de chaque décision sans dupliquer les contrôles.
- **Execution Commitments and Facts — D07, Inventory Management et logistique :** engagements de réalisation et faits utilisables pour le rapprochement ; inspection, mouvements et transport ne deviennent pas des traitements commerciaux D04. Une autorisation de retour ne prouve pas une réception.
- **Modèle processus :** dossiers achats, vente ou SAV, négociation, tâches, validations organisationnelles et relances. Les modèles conservent leurs objets propres ; un objet de commande ou d’accord du socle peut être mobilisé par un dossier sans devenir ce dossier.
- **Finance :** conditions et événements utiles en interface ; aucune facturation, comptabilité, émission d’avoir ou exécution de remboursement incluse comme capacité D04.

**Premier arbitrage proposé :** éprouver le domaine commun achats/ventes avant d’affiner sa liste. Le marché expose des traitements distincts et des notions communes ; un domaine partagé, ou des domaines spécialisés reliés par un vocabulaire commun, restent deux possibilités. Le nom Order Management risquerait de réintroduire les parcours OMS que Laurent situe dans la couche processus. Commercial Commitments n’est pas adopté pour autant ; aucun bounded context ou service n’est déduit.

## Contrôle final — 11 septembre 2026

Contrôle des identifiants uniques et séquentiels : U98, F208, A69, C64, P85, Q69, CAP36, INF20, DEC22, TER50, VER25, MKT21, ELM86 et CMP54. La carte comporte dix domaines actifs et 34 repères de capacité uniques ; D09/D11/D12 sont contigus et portent chacun une seule ingestion. Les neuf lignes de capacités d’Order Promising sont identiques à l’état précédant cette correction.

Les 33 fiches CAP004–CAP036 sont inchangées ; empreinte SHA-256 du texte à partir du contenu suivant le titre CAP004 : `e4af9ae38474068b5b72eab0ab701b5abdf25195f75933e50c4e4b59fe90d91e`. CAP001–CAP003 portent la correction de périmètre, avec anciennes valeurs conservées. Les anciennes définitions D08/D09/D10 et la première revue D04 sont conservées ci-dessus comme historique remplacé. Aucun fichier d’archive n’a été édité par cette mise à jour.

767 liens Markdown locaux et leurs ancres contrôlés dans les documents hors archive, sans erreur selon les conventions d’ancres existantes. Q010 reste partiellement ouverte sur les autorités installées et par attribut ; CTP reste différé. Les correspondances des trois ingestions sont qualifiées comme locales et partielles, sans nouvelle recherche externe.
