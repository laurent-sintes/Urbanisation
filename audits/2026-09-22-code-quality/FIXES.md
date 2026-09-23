# Correctifs de l’audit — 22 septembre 2026

Les quatre défauts F1–F4 du rapport ont été corrigés à la demande de Laurent. Le rapport initial et ses preuves restent conservés ; ses scripts de reproduction décrivent l’état antérieur, tandis que les tests de régression maintenus vérifient les correctifs.

| Défaut | Correctif | Régression |
| --- | --- | --- |
| F1 : preuve figée manquante | Inventaire `decision_registry_files` dans les nouvelles publications, indépendant de staging. Pour les publications préparées antérieures, lecture de l’inventaire après vérification de l’empreinte du manifeste de préparation. Contrôle partagé par validation, préparation et migration. | Registre figé supprimé, fragment altéré, inventaire invalide et manifeste historique absent/modifié sont rejetés ; la publication suivante fonctionne après suppression du staging d’une nouvelle publication. |
| F2 : résumé de prédécesseur désynchronisé | Relecture et validation de la capture immuable désignée par `supersedes` avant l’enregistrement. | Un résumé qui ajoute un champ non approuvé est rejeté avant toute écriture de fragment ou d’index. |
| F3 : recherche Unicode bloquante | Fonction pure `sourceMatches`, garde après normalisation, positions ramenées au texte original et fonction commune au compteur/surlignage. | Requêtes vides, espaces, accents combinants seuls, accents décomposés, emoji et correspondances successives. |
| F4 : sortie Windows non Unicode | Sortie standard du CLI d’inspection explicitement configurée en UTF-8. | Sous-processus avec `PYTHONIOENCODING=ascii:strict` ; sortie JSON décodable sans perte. Commande réelle de l’audit relancée avec succès. |

La compatibilité avec les anciennes publications est préservée sans modifier leurs octets. Leur manifeste de préparation doit être conservé lorsqu’il est l’inventaire historique authentifié. Les fixtures de publication ont été complétées pour inclure cette preuve auparavant omise.

Aucune publication réelle, modification d’accord, commit ou push n’a été effectué.

Validation finale : 114 tests Python concernés vérifiés avec succès après reprise ciblée de deux cas (assertion adaptée à la présence du manifeste historique dans la fixture ; erreur Windows ponctuelle de renommage, disparue au rejeu). Les 97 tests JS et le build Atlas réussissent. La validation du modèle courant rapporte zéro erreur, et la commande CLI réelle qui échouait sur U+2192 produit maintenant son JSON. Les logs de travail sont conservés sous `.runtime/audit-fixes-*`.
