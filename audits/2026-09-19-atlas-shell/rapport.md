# Atlas — barre haute compacte

19 septembre 2026. Retour de Laurent : exploiter la barre haute sur grand écran, donner davantage de place au contenu et rendre la signature Groupe Beaumanoir plus discrète.

## Disposition retenue

La barre FLOW passe de 66 à 52 px. Sur grand écran, elle accueille le fil d’Ariane, la copie du lien et l’actualisation. La rangée de navigation précédemment située au-dessus du titre disparaît. Le titre, la description et les onglets conservent leur position fixe ; seule la zone de contenu défile.

Le haut de l’arbre est simplifié, avec Urbanisation puis la recherche. Le logo Beaumanoir, intégral et proportionné, mesure 76 px de large dans le pied de la navigation, près des statistiques. Les octets des deux logos d’origine sont inchangés.

Sur mobile, le bouton d’ouverture de l’arbre rejoint FLOW dans la barre haute. Le fil d’Ariane reste dans une ligne distincte pour conserver sa lisibilité. La signature Beaumanoir est accessible dans le volet de navigation. Copier le lien, actualiser, ouvrir et fermer le volet gardent leurs noms accessibles ; les libellés longs de navigation conservent leur texte complet, avec ellipse visuelle sur grand écran.

## Repères de design

- [Carbon — UI shell header](https://carbondesignsystem.com/components/UI-shell-header/usage/), consulté le 19 septembre 2026, sections Overview, Anatomy et Responsive behavior : en-tête persistant, identité et navigation, actions accessibles, adaptation de la navigation aux petits écrans.
- [Microsoft Fluent 2 — Layout](https://fluent2.microsoft.design/layout), consulté le 19 septembre 2026, sections Spacing and proximity et Global spacing ramp : hiérarchie par l’espacement, proximité des éléments liés et pas de 4 px.

Ces guides motivent l’organisation ; ils ne prescrivent pas le placement du logo Beaumanoir ni ne certifient Atlas. Cette signature secondaire répond au choix de Laurent. Aucun composant tiers ni dépendance ajouté.

## Mesures et contrôles

Comparaison avant/après sur la même vue univers de la publication v012, dans Edge sans fenêtre :

| Fenêtre | Hauteur supplémentaire pour le contenu |
| --- | ---: |
| 1920 × 1080 | 78 px |
| 1440 × 1000 | 78 px |
| 1024 × 768 | 78 px |
| 390 × 844 | 14 px |
| 320 × 568 | 10 px |

Ces mesures concernent la vue univers contrôlée ; le gain peut varier selon les textes et le retour à la ligne. Mesures brutes : [avant](baseline.json), [après](report.json). [Capture desktop](desktop.png), [capture mobile](mobile.png).

82 tests frontend réussis ; compilation TypeScript/Vite réussie. Les 30 contrôles du bandeau fixe passent (vues, niveaux, liens de section, clavier, plein écran, tactile). La recette de la barre passe sur cinq dimensions, avec largeur d’arbre de 240 à 420 px, fil d’Ariane, copie de lien, raccourci de recherche et ouverture/fermeture du volet. Aucun débordement horizontal du document ni erreur JavaScript observé. Captures desktop et mobile examinées visuellement.

Le serveur local sert le nouveau build après rechargement. Aucune release métier ni modification du modèle : le retrait Business Services du backlog attend toujours une publication distincte.
