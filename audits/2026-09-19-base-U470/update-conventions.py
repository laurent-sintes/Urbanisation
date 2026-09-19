from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.structured_io import read,dumps,write_text_if_changed

updates={
'AGENTS.md':'''\n\n## Lecture et références — U470/U471

Commencer les fiches par le service concret rendu, compréhensible sans connaissance du domaine. Expliquer le jargon utile, illustrer par un cas et relier les mots clés au glossaire avec infobulle. Consigner et appliquer les règles éditoriales de `CONVENTIONS-MODELE.md`.

Dès qu’une fiche présente des rapprochements marché, l’étayer par au moins deux documents primaires distincts et pertinents, conformément à `marche/methode.md`. Justifier le nom et le périmètre de la fiche à son propre niveau ; pour un univers, ne pas résumer les choix de ses capacités. Deux documents d’un éditeur ne prouvent pas un consensus.

U470 : masquer temporairement le catalogue Informations métier dans Atlas (navigation, fiches, recherche et liens directs), sans supprimer le travail interne ni modifier les publications historiques. La consolidation de la base reste prioritaire ; ne pas étendre ce catalogue.
''',
'CONVENTIONS-MODELE.md':'''\n\n## Rédaction autoportante — U470/U471

Une fiche commence par le service rendu : ce que l’entreprise organise, fournit ou décide, pour qui et dans quel but. Éviter les abstractions seules en première phrase. Expliquer les termes spécialisés dès leur première utilisation utile et proposer un exemple concret, explicitement illustratif lorsqu’il ne décrit pas l’existant. Une définition courte n’autorise pas à laisser implicite le sens du domaine.

Relier les mots clés définis dans le glossaire avec la syntaxe `[terme](glossary:IDENTIFIANT)` ; l’infobulle donne la définition et le clic ouvre le terme dans la même publication. Choisir les occurrences utiles, sans liens sur chaque répétition ni rapprochement automatique d’homonymes. La fiche et l’infobulle doivent rester compréhensibles au clavier et sans navigation préalable.

La fiche d’un univers justifie son propre nom et sa frontière dans « Marché & choix ». Pour Supply Chain Orchestration, rappeler que le SCM professionnel est plus large : les applications externes restent sources de vérité des référentiels ; les projections Supply sont reçues par ingestion, sans administration des maîtres. La coordination des commandes, stocks, engagements et services ne reprend pas l’exécution physique. Le nom est documenté dans le marché ; son périmètre FLOW est un choix explicite, pas une nomenclature universelle.

Chaque rapprochement marché est situé au bon niveau, étayé par au moins deux documents primaires pertinents par fiche, avec les raisons du terme, de la définition et leurs limites. Cette règle ne transforme pas une ressemblance de mots en équivalence. Les fiches sans comparaison restent signalées comme telles, sans source de remplissage. U471 demande la reprise immédiate des 47 fiches à source unique ; ce lot documentaire ne rouvre pas U431.
''',
'marche/methode.md':'''\n\n## Deux références pertinentes par fiche — U470/U471

Dès qu’une fiche comporte des références marché, présenter au moins deux documents primaires distincts effectivement consultés. Deux ancres, traductions ou liens de suivi vers le même document ne constituent pas deux références. Rechercher une diversité d’organismes lorsque pertinente ; deux documents d’un même éditeur restent recevables mais ne prouvent pas un consensus interéditeurs. Conserver titre, édition ou absence d’édition, passage, date, proximité et différences pour chaque appui. Un exemple partiel doit être nommé comme tel ; ne pas ajouter un lien générique pour atteindre le nombre.

Le nom et le périmètre d’un univers se comparent à des définitions et périmètres de même portée, pas à une addition d’exemples de ses capacités. Distinguer la terminologie établie, un usage propre à un produit et l’adaptation FLOW. L’absence d’équivalent exact ne démontre aucune innovation.

Le marqueur `market_reference_policy: two_primary_sources` active le contrôle de pluralité sur les nœuds non illustratifs, relations et termes du glossaire des nouvelles préparations. Les snapshots historiques gardent leur contrat. Le contrôle compte les documents, pas leur qualité : la pertinence et la nature primaire restent une vérification éditoriale. Le catalogue Informations métier, conservé en interne et masqué par U470, n’est pas étendu par ce lot.
''',
'app/README.md':'''\n\n## Allègement de la revue — U470

Le catalogue Informations métier est temporairement masqué : pas de bouton de navigation, de section dans les fiches, de résultat ni de filtre de recherche. Un ancien lien `view=information` revient à la fiche de son nœud, ou à la carte, dans la même version. Les données publiées et le travail interne sont conservés ; ce masquage n’est pas un contrôle d’accès à l’API locale. Les composants internes sont conservés sans point d’entrée public.

Les mots clés explicitement reliés au glossaire ouvrent une infobulle au survol et au focus clavier. Elle donne priorité à la définition complète, plutôt qu’au résumé court. U470 ajoute ces liens dans l’univers Supply ; leur disponibilité publique dépend du snapshot publié, sans repli backlog.
''',
'modeles/README.md':'''\n\n## Pluralité des sources marché — U470/U471

Le champ racine optionnel `market_reference_policy: two_primary_sources` exige au moins deux documents distincts pour chaque nœud non illustratif, relation ou terme comportant des comparaisons. `validate_models.py` et la préparation de publication l’appliquent ; les URL ne deviennent pas distinctes par changement d’ancre ou ajout de paramètres. Les fiches sans comparaison ne reçoivent aucun appui fictif. La qualité primaire et la pertinence sont contrôlées éditorialement. La politique participe à l’empreinte du modèle et laisse les snapshots historiques sans marqueur inchangés.

U470 masque temporairement le catalogue Informations métier dans Atlas sans supprimer ses données du modèle. Aucune extension n’est engagée pendant cette consolidation.
'''
}
for name,extra in updates.items():
    p=ROOT/name
    assert extra.strip() not in p.read_text(encoding='utf-8'),name
    with p.open('a',encoding='utf-8',newline='') as f:f.write(extra)
r=read(ROOT/'modeles/backlog/v0-readiness.yaml')
# Keep the follow-up next to its predecessor without depending on outer section names.
def add_followup(value):
    if isinstance(value,dict):
        if 'follow_up_U469' in value:
            value['follow_up_U470_U471']={'report':'audits/2026-09-19-base-U470/rapport.md','scope':'Univers Supply autoportant, liens glossaire, catalogue Informations métier masqué, 47 fiches à source unique complétées.','market_policy':'Deux documents primaires distincts par fiche comparée ; pertinence documentée, sans équivalence forcée.','publication':'Backlog corrigé ; nouvelle release distincte nécessaire pour publier les contenus.','remaining':'Poursuivre la revue pas à pas et instruire les fiches encore non comparées dans leur périmètre ; aucune extension information ni réouverture U431.'}
        else:
            for v in value.values():add_followup(v)
add_followup(r)
write_text_if_changed(ROOT/'modeles/backlog/v0-readiness.yaml',dumps(r))
