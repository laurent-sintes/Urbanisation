# D02 — couverture par Inventory Management et Order Promising

Date : 14 septembre 2026. Source utilisateur : U144. Espace examiné : backlog JSON courant.

Laurent partage l’hypothèse que les deux capacités résiduelles sont déjà couvertes par D01 et D03. Le retrait de D02 est proposé, pas encore appliqué. Les définitions des domaines consommateurs restent inchangées.

| Contenu de D02 | Accueil envisagé | Constat sur les définitions courantes |
| --- | --- | --- |
| D02.a : quantité admissible pour réserver | D01 — Reservation | Établissement d’un engagement explicite ; appréciation de la quantité réservable encore implicite. |
| D02.a : quantité et date possibles pour promettre | D03 — Promise Proposal | Construction d’une proposition réalisable explicite ; ATP déjà rattaché à la promesse selon U95. |
| D02.d : affecter, réaffecter, libérer une ressource couvrant une demande | D03 — Supply Assignment | Ces trois comportements sont déjà explicites. |
| D02.d : modifier ou libérer une réservation, si visé par le terme engagement | D01 — Reservation | Complément proposé à la définition ; ne pas annoncer une couverture textuelle complète. |
| Ajuster les protections, si visé par le terme engagement | D01 — Supply Protection | Établir/appliquer des limites est explicite ; leur évolution reste à préciser. |
| Revoir la promesse résultante | D03 — Promise Revision | Réexamen et modifications autorisées explicites ; résultat distinct d’une affectation de ressources. |

## Conclusion proposée

Aucun espace problématique autonome n’est identifié pour D02 à ce stade. Retirer les deux capacités génériques devient cohérent si la reprise est tracée et les définitions utiles de D01 clarifiées. Ne pas créer une capacité pour chaque opération de modification ou libération. Préserver les identifiants retirés dans un historique et conserver les publications existantes.

Cette analyse est une comparaison interne du JSON, pas une nouvelle vérification de marché. Les correspondances existantes restent disponibles dans les registres ; aucune équivalence externe nouvelle n’est revendiquée. Aucun comportement installé dans les SI ni responsabilité de développement FLOW n’est déduit de cette couverture conceptuelle.


## Décision U145 et application

Laurent demande de supprimer le domaine sans renuméroter les autres. D02 et D02.a/D02.d sont retirés du backlog, ainsi que REL-MEMBER-D02.a, REL-MEMBER-D02.d et REL-UNIVERSE-SUPPLY-D02. Le snapshot `../modeles/backlog/history/pre-U145.json` conserve intégralement l’état précédent. C79 consigne la correction.

D02.b/D02.c restent dans D01 et D02.e dans D03. Aucune définition des capacités d’accueil n’est modifiée : les précisions du tableau ci-dessus restent à instruire. Les passages précédents décrivent l’analyse avant décision ; le retrait est désormais appliqué. Aucune nouvelle comparaison de marché ; aucune release produite.
