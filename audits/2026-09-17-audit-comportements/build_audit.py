"""Create proposed audit annex/matrix and register consulted sources once."""
from pathlib import Path
from hashlib import sha256
import json
from scripts.structured_io import read, dumps
from scripts.audit_behaviors_U265 import append

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

# ID | recommendation | candidate detail | targeted value/complexity | market support
ROWS = '''D01.f|Conserver|Correction d’un état sur fait tardif, seulement si nécessaire|Distinguer état courant et ressource future ; la distinction état/mouvement est adoptée|S6
D01.g|Conserver|Enregistrement puis correction tracée d’un mouvement|Conserver la justification d’une évolution sans effacer l’événement d’origine ; pas de fusion automatique avec Tracking|S14
D01.c|Conserver sans décomposition immédiate|Fraîcheur, provenance et dimensions dans le périmètre|Une lecture multi-sites ne nécessite pas un comportement par lieu|S6
D01.d|Conserver, décomposition ciblée|Constat de comptage ; traitement des écarts|Un stock compté et un ajustement autorisé sont deux résultats à distinguer ; nature et responsabilité d’autorisation à préciser|non comparé directement dans cette passe
D02.b|Conserver et décomposer en priorité|Validité des protections ; application collective ; modification/libération|Appliquer 2 000 seuils ou quotas avec effets partiels et exceptions ; les décisions de valeur restent en D05|S6,S12
D02.c|Arbitrage de frontière avant déplacement|Engager, modifier, libérer une réservation si capacité maintenue|Identifier l’engagement opposable à un besoin, sa temporalité et ses effets sur les usages concurrents ; ne pas confondre avec une affectation candidate|S6
D03.a|Candidate à devenir comportement|Proposer sous Promise Management, parent nouveau à valider|Aligner la maille d’action sur les autres gestions ; la proposition demeure sans effet de confirmation|S10
D03.b|Candidate à devenir comportement|Confirmer sous Promise Management, parent nouveau à valider|Distinguer quantités proposées, confirmées et non confirmées sans multiplier les capacités du même cycle|S10
D03.c|Candidate à devenir comportement|Réviser sous Promise Management, parent nouveau à valider|Réexaminer une promesse ou un ensemble après aléa ; préserver les modifications autorisées et impacts|S10,S15
D02.e|Conserver, clarifier avec Reservation|Affecter, réaffecter, libérer ; traitement collectif si pertinent|Rendre compte de l’affectation de ressources présentes/futures à plusieurs besoins ; responsabilité d’engagement à trancher|S6,S10
D03.i|Conserver quatre comportements existants|BHV001–BHV004 ; ne pas ajouter un cinquième par simple modalité|Engagements, lieux, temps de mobilisation et futur se combinent ; enrichir les dépendances sans changer la maille|S10
D03.j|Conserver ; décomposition après cas concret|Recherche de possibilités sous adaptation ; consolidation des impacts|Assembler une possibilité faisable sans reprendre les arbitrages de politiques, priorité, échéancier ou service ; détails proposés, non nouvelle décision souveraine|S7,S10
D03.k|Conserver sans décomposition immédiate|Critères économiques et contraintes à préciser dans le périmètre|Résultat autonome : arbitrage économique ; une formule de coût ne justifie pas une capacité ou un comportement supplémentaire|non comparé directement dans cette passe
D03.l|Conserver sans décomposition immédiate|Échéancier unique ou réparti comme conditions|Choisir un échéancier ne se confond pas avec modifier structurellement les lignes d’un Order|S10
D03.m|Conserver ; préciser le périmètre|Priorisation d’un ensemble, conservation ou changement des priorités|Décision relative entre Orders ; les modes de tri ne sont pas chacun un comportement|S10
D04.i|Conserver gestion par type|Amendement partiel et rapprochement du reste à servir si détail utile|Commande 100, livraison 60, reliquat 40 : distinguer demande, promesse et réalisation ; mobiliser Structuring/Lifecycle|S11
D04.j|Conserver gestion par type|Intégration d’une réponse fournisseur modifiant quantité/date|Conserver attente initiale, modification acceptée et reste à recevoir ; aucune négociation d’Agreement absorbée|S8,S14
D04.k|Conserver gestion par type|Suivi séparé du départ, transit et réception|100 autorisées ne signifient pas 100 expédiées ni reçues ; opérations physiques externes|S12,S14
D04.l|Conserver ; arbitrer disposition des retours|Rapprocher attendu/reçu et lien à la vente ; disposition à instruire séparément|Retour 10, réception 6 ; le traitement logistique du produit retourné ne se déduit pas de ce rapprochement|S13
D04.m|Conserver gestion par type|Suivre quantités à renvoyer et prise en charge fournisseur|Retour et remboursement sont distincts ; pas de capacités financières introduites|appui indirect S13, comparaison fournisseur non établie
D04.n|Conserver transverse et décomposer si utile|Scinder ; regrouper ; répartir|Préserver quantités, origines et liens à travers plusieurs types d’Orders ; éviter cinq duplications|appui indirect S12
D04.o|Arbitrer nature puis décomposer|Affermir/lancer ; suspendre/reprendre ; replanifier ; annuler/clôturer|Préciser autorisation et application, unité ou ensemble ; conserver sens propre des transitions et refus|S8,S11,S12
D05.a|Conserver décision fine|Différencier objectifs de sécurité/couverture et seuils uniquement si bénéfice démontré|Résultat : niveaux souhaitables ; ne pas fabriquer un comportement par paramètre ou formule|S7
D05.d|Conserver décision fine|Répartir les droits entre groupes selon contraintes|Résultat de quota distinct de son application en D01 ; préciser critères avant de décomposer|S6
D05.e|Conserver décision fine|Apports nécessaires sous hypothèses ; propositions d’ajustement|Calcul de besoin net déjà intégré ; déclencher/affermir les Orders est une autre responsabilité|S7,S8
D05.c|Conserver décision fine|Rééquilibrage sous protection du site donneur|Transfert d’optimisation et transfert pour honorer un Order n’ont pas la même finalité ; ne pas fusionner avec CTP|S7
D05.f|Conserver et décomposer en priorité|Reconfigurer les hypothèses ; simuler/comparer ; valider un scénario|Tester couverture 10/15 jours et comparer disponibilité, immobilisation, risque ; aucune application automatique déduite de la validation|S7,S9
D06.b|Conserver sans décomposition immédiate|Capacité communiquée par période, contexte et fraîcheur|Information opérationnelle distincte d’un SLA global et de la décision de choix de service|S4,S14
D07.a|Conserver décision fine|Détailler le résultat prestations requises dans le périmètre|Préparation, document et transport sont des besoins ; pas un comportement par catégorie de prestataire|S4,S14
D07.b|Conserver et décomposer|Solliciter/enregistrer réponse ; modifier/annuler ; clôturer|Séparer demande, acceptation, refus ou contre-proposition et résultat ; pas un cycle identique imposé à chaque service|S4,S14,S15
D07.c|Conserver ; décomposition ciblée|Rapprochement partiel ; correction et traitement d’écarts|Imputer 60 préparations sur 100 attendues, puis corriger un fait ; reliquat prestation distinct du reliquat Order|S14
D07.d|Conserver ; décomposition ciblée|Actualiser jalons/estimations ; intégrer faits tardifs ou rectifiés|Ne pas compter deux fois le même résultat et ne pas confondre prévision et fait ; partage avec Reconciliation à préciser|S4,S14
D09.d|Conserver ingestion spécialisée|Identités, rôles et liens corrigés depuis le maître|Éviter un doublon de Party sans devenir administrateur du référentiel ; chargement complet/incrémental seulement si utile|non comparé directement dans cette passe
D11.a|Conserver ingestion spécialisée|Évolution des conditions et validité de la projection|Une version d’Agreement ne réécrit pas un engagement d’Order ; dates d’effet à expliciter|non comparé directement dans cette passe
D08.d|Conserver ingestion spécialisée|Recevoir variantes, rôles et références corrigées|Distinguer Product/Variant, Article/Container et unité ; pas un comportement par attribut|non comparé directement dans cette passe
D12.a|Conserver ingestion spécialisée|Recevoir prix, zones et validité du catalogue|Maintenir une projection applicable sans administrer le catalogue maître|appui analogique S16, catalogue produits distinct
D13.a|Conserver ingestion spécialisée|Évolution des sites et relations de réseau|Une modification de référence ne garantit pas une capacité opérationnelle disponible ; ne pas fusionner avec D06.b|non comparé directement dans cette passe
D06.d|Conserver et décomposer en priorité|Coordonner les dépendances ; propager le plan retenu ; reprendre après incident|Après préparation partielle, n’émettre que les sollicitations applicables ; le choix de variation appartient à D06.f|S4,S14,S15
D14.a|Conserver ingestion spécialisée|Évolutions des SLA configurés et des accès de service|Catalogue reçu d’un maître externe, pas administration du service ni tracking opérationnel|S16
D06.e|Conserver ; fusion courante encore proposée|Admissibilité puis choix de service à expliciter sans nouvelle hiérarchie|Clarifier alternatives et résultat retenu ; ni SLA suffisant seul ni qualification comme terme autonome|S4,S14
D06.f|Conserver décision distincte|Déterminer une variation sous contraintes et effets déjà réalisés|Comparer autre service/date/quantité face à l’aléa ; orchestration applique le plan ; impacts promesse transmis à D03|S15'''

def main():
    if (ROOT / 'modeles/backlog/behavior-audit.yaml').exists():
        raise SystemExit('Audit exists; update deliberately, do not append twice.')
    model = read(ROOT / 'modeles/backlog/model.yaml')
    nodes = {n['id']:n for n in model['nodes']}
    entries = []
    for line in ROWS.splitlines():
        identifier, recommendation, detail, benefit, market = line.split('|')
        assert nodes[identifier]['kind'] == 'capability'
        entries.append({'capability_id':identifier, 'state':'proposed', 'recommendation':recommendation,
                        'candidate_detail':detail, 'complexity_or_targeted_benefit':benefit,
                        'market_support':market, 'source_refs':['U265','U266','CMP089']})
    assert len(entries) == 41 and len({e['capability_id'] for e in entries}) == 41
    assert {e['capability_id'] for e in entries} == {n['id'] for n in nodes.values() if n['kind']=='capability'}
    annex = {'as_of':'2026-09-17', 'purpose':'Audit de granularité et plan U265/U266 ; propositions hors catalogue actif.',
             'source_refs':['U265','U266','CMP089'], 'state':'proposed',
             'adopted_rule':{'source_refs':['U265'], 'text':'Toute décomposition en comportements est justifiée par une complexité ou un bénéfice ciblé.'},
             'decision_boundary':'Aucune fusion, rétrogradation, nouvelle capacité, nature ou relation proposée n’est adoptée par cet audit.',
             'report':'audits/2026-09-17-audit-comportements/rapport.md',
             'market_sources':'audits/2026-09-17-audit-comportements/marche.md',
             'assessments':entries}
    (ROOT / 'modeles/backlog/behavior-audit.yaml').write_text(dumps(annex),encoding='utf-8')
    lines=['# Matrice de granularité — 41 capacités', '',
           'Dérivée de `behavior-audit.yaml` ; noms lus dans le backlog du 17 septembre 2026. Toutes les recommandations sont proposées. S1–S16 renvoient aux [sources de marché](marche.md). Une mention non comparée ou analogique ne vaut pas absence dans le marché. Chaque ligne précise pourquoi décomposer, ou pourquoi s’abstenir.', '',
           '| Capacité | Recommandation | Comportements / précisions candidates | Complexité ou bénéfice ciblé | Appui marché |',
           '| --- | --- | --- | --- | --- |']
    for e in entries:
        identifier=e['capability_id']
        lines.append('| '+' | '.join([identifier+' — '+nodes[identifier]['fields']['name'], e['recommendation'],e['candidate_detail'],e['complexity_or_targeted_benefit'],e['market_support']])+' |')
    lines += ['', '## Les quatre comportements ATP', '', '| Comportement | Examen |', '| --- | --- |',
              '| BHV001 — Existing Commitment Consideration | Conserver : protège contre le double décompte. Distinguer consultation des engagements et application d’une réservation. |',
              '| BHV002 — Network Stock Availability | Conserver : admissibilité multi-lieux. Un magasin, entrepôt ou darkstore est une condition, pas un enfant supplémentaire. |',
              '| BHV003 — Operational Availability Timing | Conserver : disponibilité réelle dans le temps. Clarifier source du délai article/emplacement ; ne pas déplacer le pilotage physique dans ATP. |',
              '| BHV004 — Future Supply Projection | Conserver : arrivages et engagements concurrents à l’horizon. Fiabilité de l’arrivage reste une condition à expliciter. |', '',
              'Les quatre définitions adoptées U263 restent intactes. Elles ne sont ni quatre maturités successives ni des options exclusives. Leurs noms anglais et justifications éditoriales restent proposés.', '']
    (OUT / 'matrice.md').write_text('\n'.join(lines),encoding='utf-8')
    model['limitations'] = [
        'Les propositions, illustrations et justifications éditoriales ne sont pas validées par leur présence dans le modèle. Consulter les portées par champ et leurs sources.',
        'Le modèle processus Business Services et les objets, documents, événements restent à construire au-delà des illustrations ; absence de détail ne signifie pas absence métier.',
        'Les synthèses de domaines importées sont éditoriales. Les relations manquantes et natures non renseignées restent à instruire, sans inférence depuis les noms ou préfixes.',
        'Les identifiants retirés et accords remplacés restent historiques et ne doivent pas être réutilisés. Chronologie intégrale des anciennes limitations : audits/2026-09-17-audit-comportements/model-before.yaml ; états antérieurs : modeles/backlog/history/ et publications figées.',
        'La revue de granularité U265/U266 est proposée dans modeles/backlog/behavior-audit.yaml ; aucune fusion ou rétrogradation de capacité appliquée. Capacité puis Comportement est la profondeur descriptive terminale ; toute décomposition doit être justifiée.']
    (ROOT / 'modeles/backlog/model.yaml').write_text(dumps(model),encoding='utf-8')
    refs = [
        ('ELM166','MKT14','S1','Business Process Catalog, six niveaux','Documentation évolutive ; page datée du 8 janvier 2026','Métamodèle de contenus/processus, pas six niveaux de capacités'),
        ('ELM167','MKT04','S2','Reference Architecture Content','Cours public, édition non précisée','Hiérarchie métier et liens de réalisation distingués'),
        ('ELM168','MKT14','S6–S8/S11–S13','Allocation, plans, firming, holds, batch transfer release, returns','Dynamics 365 Supply Chain Management, documentation évolutive','Fonctionnalités de produit utilisées pour éprouver les comportements ; pas de couverture complète'),
        ('ELM169','MKT24','S9','Versions and Scenarios','Cours public SAP IBP order-based planning, édition non précisée','Simulation et scénarios comme appui à Inventory Planning'),
        ('ELM170','MKT13','S10','aATP PAC/PAL/BOP/ABC','Cours public SAP S/4HANA, édition non précisée','Fonctions de produit réparties entre plusieurs capacités FLOW'),
        ('ELM171','MKT20','S14/S15','Supply Chain Orchestration et change management','Oracle Cloud SCM 26A et Order Management 25C consultés','Appui à orchestration/adaptation ; périmètre produit plus large que D06'),
        ('ELM172','MKT19','S4/S16','TMFC007 Service Order Management ; TMF633','TMFC007 v1.2.1 / TMF633 v4.0','Composant et API distincts de capacités ; contexte télécom')]
    append('marche/catalogue.md','### Complément U265 — comportements et granularité, 17 septembre 2026\n\nMKT03/04/13/14/19/20/24/25 reconsultés : BIZBOK, SAP RBA/S4/IBP, Microsoft, TM Forum, Oracle et LeanIX. Sources, versions, passages et limites : [comparaison comportements](../audits/2026-09-17-audit-comportements/marche.md). ELM166–172, ELM052/163 reconsultés, CMP089 proposé. Aucune nouvelle référence concurrente ni équivalence de niveaux adoptée.')
    for identifier, mkt, source, title, edition, limit in refs:
        append('marche/elements.md',f'### {identifier}\n\n- Référence : {mkt}. Libellé natif ou famille : {title}.\n- Source : {source} dans [étude U265](../audits/2026-09-17-audit-comportements/marche.md), liens et sections explicites.\n- Édition : {edition}. Consultation : 2026-09-17.\n- Nature / limite : {limit}. Identifiant de capacité native non établi sauf repères documentaires indiqués ; aucun rang FLOW déduit.\n- Usage : CMP089, correspondance proposée par Codex.')
    append('marche/comparaisons.md','''## CMP089

- Objet : granularité des 41 capacités et quatre comportements ATP ; audit U265/U266.
- Sources : ELM166–172 ; ELM052 (BIZBOK) et ELM163 (LeanIX) reconsultés le 17 septembre 2026.
- Relation : appui méthodologique et fonctionnel, plusieurs-à-plusieurs ; aucune équivalence par numéro de niveau.
- Résultat proposé : conserver Capacité → Comportement comme profondeur terminale ; décomposer sélectivement Planning, Protection, Lifecycle et Orchestration ; instruire Promise Management et frontière Reservation/Assignment.
- Catalogue local : aucun déplacement de capacité appliqué. La matrice distingue les appuis directs, analogies et éléments non comparés individuellement.
- Sources, passages, périmètre et limites : [marché](../audits/2026-09-17-audit-comportements/marche.md) ; [matrice](../audits/2026-09-17-audit-comportements/matrice.md).
- Auteur/date/statut : Codex, 2026-09-17, proposé ; aucun valideur ni validation d’équivalence.''')
    append('marche/README.md','Audit U265/U266 — [Capacités, comportements et niveaux marché](../audits/2026-09-17-audit-comportements/marche.md), avec [matrice des 41 capacités](../audits/2026-09-17-audit-comportements/matrice.md). Les rapprochements CMP089 restent proposés.')
    print('41 assessments and 4 behavior checks written; market references registered.')

if __name__ == '__main__': main()
