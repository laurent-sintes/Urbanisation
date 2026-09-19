# Release U452 — Urbanisation v010

**v010 / 2026-09-19.3 publiée et activée le 19 septembre 2026 à 07:41:05 UTC.** [Descripteur](../../modeles/release/urbanisation-v010-2026-09-19-074105.yaml), [note de release figée](../../modeles/release/2026-09-19.3/release-notes.md). Atlas sert exactement le candidat contrôlé.

## Contenu publié

Les **47 capacités** et les **76 comportements** sont typés. La publication intègre les dix types de capacités complétés en U449 et les 76 formes de comportements définies en U451. Les icônes de comportements utilisent les sept formes propres au méta modèle. Les capacités des référentiels conservent leurs icônes spécifiques ; les décisions restent en fin de domaine, avec séparation légère.

L’édition méthodologique `2026-09-19.1` est explicitement associée à v010 par le workflow de publication. Les six repères de **Comprendre le méta modèle** et les deux glossaires restent accessibles : 100 termes métier et 21 termes méthodologiques. Les réserves et informations de validation restent internes à la présentation.

Le catalogue reste à 138 nœuds, six domaines, 47 capacités, 76 comportements, 338 relations et 110 termes TER figés. Aucun ajout ou retrait de nœud, aucune modification de nom, définition ou rattachement. Les relations gardent leurs valeurs exactes ; leur ordre de stockage reprend le rangement du backlog U449.

## Accords et intégrité

172 décisions antérieures compatibles sont reprises. Pour les révisions modifiées, 73 transcriptions contrôlées reprennent 118 valeurs approuvées exactement identiques à leurs preuves v009. Les décisions historiques demeurent conservées ; les nouveaux types restent proposés. [Réexamen par champ](../2026-09-19-atlas-U450/transcription-review.json), [rapport de comparaison](report.json).

**242 fichiers historiques sont inchangés octet par octet.** Les index ont été capturés avant activation ; seuls le nouveau descripteur courant et l’association méthodologique de destination ont été ajoutés. Les sources, modèles, décisions et glossaires des anciennes publications restent intacts.

## Contrôles et disponibilité

- Candidat préparé depuis le backlog courant avec la source d’autorisation U452, puis publié après contrôle des empreintes et contrats.
- Validation finale : **0 erreur**. Restitutions générées et serveur contrôlé, frontend disponible.
- API Atlas : version `2026-09-19.3`, nœuds, relations et glossaire identiques au snapshot figé. Serveur FLOW Atlas du projet sur le port 8765, PID 24916 ; aucun redémarrage nécessaire.
- Navigateur : v010 en suivi courant, sept formes et icônes sur les données réellement publiées, décisions en fin de domaine, guide et deux glossaires accessibles. Aucune erreur JavaScript. v009 reste consultable en version fixe sans récupération des nouveaux types.

[Vérification d’intégrité](verification.json), [vérification navigateur](browser-verification.json), [capture ATP avec comportements typés](v010-atp.png). Aucun commit ni push Git.
