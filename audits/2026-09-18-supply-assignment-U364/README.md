# Supply Assignment — U364

Trois comportements sous D02.e :

- BHV045 **Supply Assignment Plan Application** : appliquer les affectations d’un plan retenu et signaler les écarts.
- BHV046 **Incremental Supply Assignment** : compléter les besoins non affectés tout en préservant les affectations existantes.
- BHV047 **Supply Reassignment** : réviser les affectations modifiables pour appliquer de nouveaux arbitrages entre commandes.

Les deux politiques rendent visibles stabilité et adaptation. Un plan peut mobiliser l’une ou l’autre ; aucun sous-comportement ni séquence imposée. Les décisions choisissent, Supply Assignment applique ; Freezing limite les révisions autorisées. La politique incrémentale n’impose pas un algorithme de recalcul.

U364 valide la distinction et son rattachement ; U345 avait acquis l’application de plan. Les deux définitions de politique reprennent les formulations présentées ; noms anglais et détails éditoriaux ne sont pas validés globalement. Comparaisons SAP et Microsoft dans les fiches, avec recouvrements et limites, CMP134. Les arbitrages A01/A02 restent ouverts.

[Annexe structurée](../../modeles/backlog/supply-assignment-mechanisms-review.yaml) · [Preuve de migration](implementation.yaml). Backlog uniquement, aucune release.

Vérification : validation du modèle sans erreur ; 11 tests comportements/comparaisons marché réussis ; audit des migrations, définitions adoptées et rattachements réussi ; 125 publications ou preuves figées inchangées. Restitutions régénérées. Catalogue courant : 38 capacités et 43 comportements.
