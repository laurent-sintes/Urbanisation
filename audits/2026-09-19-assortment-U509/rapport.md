# U509 — Product Catalog et Assortment

Le Go applique la proposition U508 : Product Catalog rend explicite la nature de D12 ; Assortment D16 est une référence distincte dans Authoritative Data ; Agreement peut référencer ou figer la sélection convenue sans composition obligatoire Contract + Assortment.

Le glossaire porte Product Catalog TER049 et Assortment TER087. Les descriptions d’Agreement et d’Authoritative Data sont cohérentes avec cette frontière. Les deux nouvelles capacités Assortment Ingestion et Assortment Visibility sont proposées ; leurs détails ne bénéficient pas d’un accord implicite. Aucun Behavior ni objet Information n’est ajouté. La conception commerciale et les maîtres d’entreprise restent externes.

Les fiches comparent SAP Assortment / Assortment List et Microsoft Assortment management ; Oracle Procurement éclaire les accords avec ou sans détail des produits. CMP206 conserve le positionnement et les limites. Les sources sont localisées dans les fiches et le registre ; deux documents SAP ne sont pas assimilés à un consensus du marché.

## Accords

Les 21 preuves U507 sont préservées dans le registre et dans `before-decision-intents.yaml`. Leur réexamen explicite est documenté dans `intent-reassessment.yaml` : mêmes champs approuvés, mêmes valeurs sauf le nom Product Catalog Visibility adopté U509. Les compléments de périmètre et les nouvelles capacités ne sont pas approuvés par ce réexamen.

Le registre conserve les preuves remplacées et ajoute un lien `supersedes` réservé aux intentions non publiées. Le compilateur refuse les reprises périmées, les extensions de champs, les cibles différentes et le contournement du réexamen d’accords publiés. Une écriture groupée atomique évite de réécrire le registre pour chaque accord.

## Contrôles

- Modèle : 157 éléments, 56 capacités, 7 références, 366 relations ; glossaire : 111 termes. Validation : aucune erreur.
- Python : 71 tests concernés réussis, dont les 8 tests de niveaux rejoués après correction de la fixture du nouveau test d’association.
- Atlas : 43 tests réussis ; TypeScript et build Vite réussis. Les tests ont nécessité de permettre le lancement local du lecteur Python, refusé par le sandbox initial.
- Vue backlog régénérée ; `git diff --check` sans erreur.
- Le contrôle de compilation des intentions vérifie 26 décisions actives et la conservation des 21 anciennes preuves.
- L’index de publication conserve l’empreinte capturée avant intervention. Aucun snapshot publié n’a été modifié ; aucune release, aucun commit ni push.

Le guide de travail reste en version 2026-09-19.5, non publiée. Lors d’une prochaine release demandée, sélectionner explicitement ce guide suivant le parcours maintenu.
