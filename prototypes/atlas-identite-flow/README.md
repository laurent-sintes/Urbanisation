# Proposition d’identité FLOW pour Atlas — U207

**Historique depuis U208, le 15 septembre 2026 :** Laurent a adopté cette proposition. L’identité est désormais intégrée à [Atlas](http://127.0.0.1:8765/#node=universe-supply&view=map), avec images directement dans l’en-tête React et styles dans `app/src/brand.css`. Voir [la documentation de l’intégration](../../app/BRANDING.md). Le serveur temporaire 5174 est arrêté. Les instructions et le bilan ci-dessous décrivent l’essai initial. Le comparateur importe les composants vivants d’Atlas : il ne fige pas l’ancienne interface et n’est plus un comparatif valide après l’intégration. Conserver ce dossier pour les médias, leur extraction et les choix graphiques ; les captures de l’essai restent dans `app/.runtime/branding/`.

Proposition du 15 septembre 2026, à partir du template projet fourni par Laurent. L’interface de production reste celle de `app/`. Cet aperçu importe ses composants React et lit ses API de publication à l’exécution. Il ne contient aucun modèle copié ni nouvelle autorité métier.

## Direction proposée

Un en-tête clair avec l’emblème FLOW à côté de **FLOW Atlas**, et le logo **Groupe Beaumanoir** en signature secondaire. Le vert du template guide les liens, les actions et la sélection ; menthe et lavande allègent les fonds, sable distingue discrètement les référentiels. Le pêche reste un accent ponctuel. Le trait multicolore sous l’en-tête est une adaptation pour l’application, pas une forme extraite du PowerPoint.

Les parcours validés sont conservés : arbre gauche, fiches centrales, recherche, glossaire, liens de capacités dans les domaines et référentiels, navigation des relations. Les statuts gardent leur texte et leurs couleurs propres ; les pastels de marque ne deviennent pas des statuts métier. Aucun inventaire ni rattachement n’est ajouté.

La police du template est Aptos (Aptos Display pour les titres). L’aperçu la demande si elle est installée ; Segoe UI puis Arial assurent le repli. Aucun téléchargement ou embarquement de police Office.

## Palette et source

| Couleur du template | Code | Usage proposé |
| --- | --- | --- |
| Vert profond | `#236159` | Navigation, liens, actions |
| Menthe | `#D9F2EA` | Sélection et surfaces légères |
| Lavande | `#DAE0F2` | Surfaces secondaires |
| Sable | `#EADFCD` | Repère des référentiels |
| Pêche | `#FFD8B2` | Accent graphique ponctuel |
| Blanc cassé | `#FCFDFD` | Fond général |

Sources exactes, opacités et usages observés dans [palette.json](palette.json). Le template garde un thème nommé Office : ses accents génériques ne sont pas la palette appliquée aux formes FLOW. Les oranges `#F26B43` et `#FBAE40` appartiennent uniquement aux guides d’édition et sont exclus de la proposition. Le vert sur blanc présente un contraste calculé de 7,18:1 ; ce calcul ne vaut pas audit complet de l’interface.

Les quatre diapositives ont été rendues pour inspection dans `app/.runtime/branding/template-slide-*.png`. Elles présentent fond blanc, grands aplats pastel discrets, cartouche FLOW et signature Beaumanoir. L’adaptation pour Atlas reprend ces repères sans ajouter les grandes décorations derrière les cartes métier.

## Logos récupérés

- [FLOW original](assets/flow-original.png) : PNG RGB 1024 × 1024 avec signature « Fashion, Logistics, Operations & Workflows » et fond presque blanc.
- [Groupe Beaumanoir original](assets/beaumanoir-original.png) : PNG RGBA 1564 × 605, noir sur fond transparent.

Les fichiers sont extraits à l’identique : empreintes du PPTX et de ses médias dans [assets-provenance.json](assets-provenance.json). Aucun logo n’est redessiné, recoloré ou généré. L’en-tête propose un cadrage CSS du seul emblème FLOW pour rester compact ; le panneau « Palette et logos » montre les fichiers intégraux, téléchargeables. Une éventuelle version de marque compacte officielle pourra remplacer ce cadrage lors de l’intégration.

Extraction reproductible depuis la racine du projet :

```powershell
python prototypes/atlas-identite-flow/extract-assets.py "C:/Users/laure/OneDrive/Documents/Beaumanoir/Template PPT projet.pptx"
```

## Consulter et comparer

Lancer Atlas sur 8765, puis cet aperçu séparé depuis la racine :

```powershell
node app/node_modules/vite/bin/vite.js --config prototypes/atlas-identite-flow/vite.config.mjs
```

[Ouvrir la proposition](http://127.0.0.1:5174/#node=universe-supply&view=map). La barre de comparaison permet de basculer **Actuel / FLOW**, d’ouvrir univers, référentiels et fiche, puis de consulter la palette et les logos. Les données et la navigation proviennent de l’application courante, sans injection de fixtures.

Compiler uniquement l’aperçu :

```powershell
node app/node_modules/vite/bin/vite.js build --config prototypes/atlas-identite-flow/vite.config.mjs
```

Le résultat va dans `app/.runtime/branding/preview-dist/`, séparément de `app/dist/`. Le serveur 5174 est un aperçu de développement local, pas le serveur de production d’Atlas. Les styles proposés résident dans `theme.css`. Les portails React ajoutant les logos et les contrôles de comparaison servent uniquement à la proposition ; une intégration adoptée placera les images directement dans les composants de l’en-tête.

## Vérification

Compilation de l’aperçu, inspection visuelle des logos/couleurs, comparaison des deux habillages et contrôle des parcours réels. Captures et résultats navigateur dans `app/.runtime/branding/`. L’intégration de cette identité graphique reste proposée ; aucune publication métier ni opération Git incluse.
