"""Record discussion and market evidence, without changing the active catalogue."""
from pathlib import Path
from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash

ROOT = Path(__file__).resolve().parents[1]

def append(path, text):
    with (ROOT/path).open('a', encoding='utf-8') as stream:
        stream.write('\n\n' + text.strip() + '\n')

def main():
    path = ROOT/'modeles/backlog/behavior-gap-audit.yaml'
    a = read(path)
    assert 'feedback_U303' not in a, 'Already recorded'
    contributions = [
        ('U301', 'Execution Tracking : audit de toutes les opérations numériques et physiques',
         "Execution tracking comprend la logistics visibility mais aussi la visibility de tout ce qui se passe dans le système d'information : on doit pouvoir auditer la totalité des opérations : numériques et physiques.",
         'Périmètre explicitement exprimé : visibilité logistique incluse dans Execution Tracking et audit de toutes les opérations numériques et physiques. Ne pas réduire le numérique aux seuls statuts de prestations.'),
        ('U302', 'Accord sur l’analyse du périmètre de tracking',
         'Je suis donc d\'accord avec ton analyse.',
         'Accord dans le contexte U301. Le message suivant U303 réouvre explicitement la granularité du comportement Logistics Visibility ; ne pas figer son niveau sur la base de cet accord.'),
        ('U303', 'Challenger la granularité de Logistics Visibility',
         "Néanmoins, je trouve du coup Logistics Visibility trop agrégeant pour un niveau comportement. est-ce qu'il ne faudrait pas séparer le concept en Transportation Visibility + <tout ce qu'il se passe avant le transport> Visibility + <tout ce qui se passe après le transport> Visibility ?",
         'Question de décomposition à comparer au marché. Le périmètre global de tracking reste acquis ; le nom Logistics Visibility adopté U297 ne suffit pas à imposer un comportement unique. Aucun nouveau découpage adopté par cette question.'),
        ('U304', 'Visibilité de la mise en rayon après transport',
         "Une mise en rayon après le transport, ce sont des opérations aval du transport sur lesquelles je veux de la visibilité. Comment ça s'appelle ?",
         'Cas métier explicite : suivre les opérations magasin après livraison, notamment la mise en rayon. Comparer le vocabulaire de marché ; aucune nouvelle décomposition adoptée par la question.')]
    # Record the user evidence before interpreting it.
    for ref, title, quote, scope in contributions:
        append('connaissance/01-contributions-utilisateur.md', f'## {ref}\n\n**id**\n\n{ref}\n\n**date**\n\n2026-09-17\n\n**titre**\n\n{title}\n\n**texte**\n\n{quote}\n\n**contexte et portée**\n\n{scope}')
    sources = [
        ('S42', 'Microsoft', 'Manage Dataverse auditing', 'https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing', 'Power Platform / Dataverse ; page évolutive mise à jour le 21 avril 2026', 'Introduction, supported operations et activity logging', 'Audit des modifications de données et accès ; journalisation complémentaire pour certaines activités.', 'Activation et couverture configurées ; ne garantit pas la totalité des opérations du SI. Dataverse ne constitue pas un modèle de capacités Supply.'),
        ('S43', 'Camunda', 'Audit log', 'https://docs.camunda.io/docs/components/audit-log/overview/', 'Camunda 8.9', 'About ; Impact on secondary storage', 'Historique des opérations sur processus, identités et tâches, avec auteur, date et entités concernées.', 'Par défaut, les opérations utilisateur sont suivies, pas les opérations client. Périmètre de produit, pas audit universel de tous les systèmes.'),
        ('S44', 'SAP', 'Learning about the SAP EWM Solution', 'https://learning.sap.com/courses/cloud-onboarding-for-sap-ewm-for-sap-s-4hana-cloud-private-edition-extra-stack/learning-about-the-sap-ewm-solution', 'EWM for SAP S/4HANA Cloud Private Edition, extra stack ; cours sans numéro de release', 'Introduction ; Goods Receipt ; Storage & Operations ; Conclusion', 'EWM distingue les opérations entrantes, internes et sortantes : déchargement, rangement, préparation et chargement, avec suivi des unités logistiques et intégration TM.', 'Appui au périmètre sur site ; ne prescrit pas deux ou trois comportements FLOW ni un libellé canonique Warehouse Visibility.'),
        ('S45', 'Oracle', 'Warehouse Management', 'https://www.oracle.com/scm/logistics/warehouse-management/', 'Oracle Fusion Cloud Warehouse Management ; page produit sans édition figée', 'Manage complex fulfillment processes ; Consumer goods ; Third-party Logistics', 'La présentation couvre les flux entrants et sortants, le cross-docking et les opérations sur des sites allant de l’entrepôt au magasin.', 'Présentation commerciale, pas contrat exhaustif de collecte des événements ni nomenclature de comportements métier.')]
    for sid, vendor, label, url, edition, locator, fact, limit in sources:
        a['sources'].append(dict(id=sid, vendor=vendor, native_label=label, native_id=None, url=url, edition=edition, consulted_on='2026-09-17', locator=locator, nature='documentation produit' if sid != 'S45' else 'présentation produit', access='Texte primaire consulté', observed_fact=fact, limits=limit, reuse='Synthèse sélective et lien ; aucune reproduction substantielle.'))
    rule = contributions[0][2]
    a['tracking_scope_U301'] = dict(state='adopted_in_stated_scope', source_refs=['U301', 'U302'], rule=rule, validated_fields=['rule'], value_sha256={'rule':value_hash(rule)}, qualification='Périmètre adopté ; granularité de Logistics Visibility réouverte U303. Les opérations restent sous la responsabilité de leurs domaines ; leur traçabilité est transverse.', market_sources=['S42','S43'], catalog_changed=False)
    f = dict(status='proposed', source_refs=['U301','U302','U303','CMP104'], market_sources=['S35','S44','S45'],
        conclusion='Proposer Warehouse Visibility et Transportation Visibility directement sous Execution Tracking ; conserver Logistics Visibility comme notion englobante, sans ajouter un niveau entre capacité et comportement.',
        reasoning='Une plateforme est après un transport et avant le suivant. Réception et expédition sont relatives à un site ; elles ne constituent pas deux extrémités fixes du parcours. Un comportement distingue un mécanisme et un bénéfice, pas seulement une position dans une séquence.',
        warehouse_scope='Suivre la progression des marchandises et unités logistiques dans les opérations sur site : réception, manutention, préparation, conditionnement, cross-docking et chargement. Applicable aux opérations correspondantes en entrepôt, plateforme, magasin ou darkstore.',
        warehouse_benefit='Retrouver les quantités malgré les fractionnements, regroupements et changements de contenant ; comprendre leur avancement et leur disponibilité pour la prochaine étape.',
        transportation_scope='Suivre les acheminements entre lieux, leurs étapes, leur position connue, leurs estimations d’arrivée et leurs écarts, jusqu’à la remise au destinataire, dernier kilomètre compris.',
        transportation_benefit='Maintenir la continuité entre trajets et transporteurs, anticiper les arrivées et identifier les ruptures de progression.',
        boundaries='Une arrivée transport et une réception sur site sont des faits distincts, éventuellement liés à une même preuve. Inventory Visibility décrit quantités et états ; ces comportements expliquent le déroulement des opérations. Un événement partagé ne doit pas être dupliqué artificiellement.',
        example='Préparation entrepôt → transport → cross-docking plateforme → transport → réception magasin : Warehouse Visibility s’applique sur trois sites, Transportation Visibility aux deux acheminements.',
        market_limit='SAP et Oracle étayent les périmètres warehouse/transport et inbound/internal/outbound ; ils ne normalisent pas notre hiérarchie. Warehouse Visibility est le libellé proposé pour cette spécialisation, pas un intitulé universel attesté de capacité.',
        digital_scope='Le périmètre numérique et l’audit de toutes les opérations restent requis par U301/U302. Cette proposition ne décompose que la partie logistique et ne prétend pas achever la décomposition du parent.',
        open='Valider deux comportements sur site/transport ou démontrer un bénéfice différenciant exigeant un suivi séparé de réception et préparation. Ne pas créer des comportements avant/après transport par simple séquencement.',
        catalog_changed=False)
    a['feedback_U303'] = f
    for sid, vendor, label, url, fact, limit in [
        ('S46', 'Blue Yonder', 'What is Blue Yonder Store Execution Inventory Management?', 'https://info.blueyonder.com/order-management-commerce/what-is-blue-yonder-store-execution-inventory-management', 'Store Execution désigne notamment les opérations de réception et de fiabilisation du stock en magasin ; la page décrit une réception directe en rayon et le résultat de disponibilité en rayon.', 'FAQ produit évolutive sans édition ; Store Execution est attesté, mais le composé Store Execution Visibility reste notre proposition de nom de comportement.'),
        ('S47', 'RELEX', 'Automatic replenishment system', 'https://www.relexsolutions.com/solutions/automatic-replenishment-system/', 'La page emploie direct-to-shelf replenishment et on-shelf availability, en reliant livraisons, capacité des rayons et manutention en magasin.', 'Page commerciale évolutive sans édition ; la planification du réassort ne prouve pas le suivi de chaque mise en rayon effectivement réalisée.')]:
        a['sources'].append(dict(id=sid, vendor=vendor, native_label=label, native_id=None, url=url, edition='Page produit évolutive sans édition figée', consulted_on='2026-09-17', locator='Présentation et processus magasin', nature='présentation produit', access='Texte primaire indexé consulté', observed_fact=fact, limits=limit, reuse='Synthèse sélective et lien.'))
    a['feedback_U304'] = dict(status='proposed', source_refs=['U304','CMP104'], market_sources=['S46','S47'],
        conclusion='La mise en rayon relève de Shelf Replenishment ; le périmètre plus large est Store Execution ou In-Store Execution. Proposer Store Execution Visibility pour le suivi des opérations logistiques en magasin, en précisant que ce composé est une formulation FLOW appuyée sur le vocabulaire marché.',
        scope='Réception magasin, passage en réserve, acheminement vers la surface de vente, mise en rayon et réassort du rayon. Distinguer livraison reçue, marchandise en réserve et quantité effectivement accessible en rayon.',
        rationale='Le bénéfice différenciant est de révéler une rupture en rayon malgré un stock présent en magasin, et le délai entre livraison et accessibilité effective au client.',
        recommendation='Réexaminer la proposition à deux comportements U303 : Warehouse Visibility pour les opérations des entrepôts/plateformes, Transportation Visibility pour les acheminements et Store Execution Visibility pour les opérations logistiques magasin. Trois spécialisations directement sous Execution Tracking, à valider ; aucune hiérarchie supplémentaire.',
        limits='Store Replenishment peut désigner l’approvisionnement du magasin depuis l’extérieur. On-Shelf Availability est un résultat de disponibilité, pas le suivi de toutes les opérations. Store Execution est plus large que le seul périmètre logistique retenu ici ; pas d’extension automatique à toutes les activités commerciales du magasin.',
        catalog_changed=False)
    f['superseded_by'] = 'U304 : le cas de mise en rayon justifie de proposer une spécialisation Store Execution Visibility distincte ; voir feedback_U304.'
    a['positioning_U300']['status'] = 'granularity_reopened_U303'
    a['positioning_U300']['supersession_note'] = 'La proposition de comportement logistique unique est réexaminée U303 ; périmètre parent étendu U301/U302. Voir feedback_U303.'
    a['current_synthesis_U298']['next_step'] = 'Arbitrer la granularité logistique selon feedback_U304 : entrepôt/transport/opérations magasin, en préservant le mandat numérique et physique U301/U302.'
    a['current_synthesis_U298']['adopted_name']['open'] = 'Le nom reste adopté ; son utilisation comme comportement unique est réexaminée U303.'
    assessment = next(x for x in a['assessments'] if x['capability_id']=='D07.d')
    assessment['diagnosis'] = 'U301/U302 : rendre auditables toutes les opérations physiques et numériques. U303 : Logistics Visibility jugé trop agrégé pour un comportement unique.'
    assessment['recommendation'] = a['feedback_U304']['recommendation'] + ' Conserver les règles de non-doublon P10. Le catalogue audité reste inchangé.'
    assessment['market_sources'] = ['S35','S42','S43','S44','S45']
    path.write_text(dumps(a), encoding='utf-8')
    append('marche/elements.md', '### ELM196\n\n- Sources S42–S45 de behavior-gap-audit.yaml : Microsoft Dataverse (distinct de Dynamics Supply Chain), Camunda 8.9, SAP EWM, Oracle Warehouse Management. Consultation : 17 septembre 2026.\n- URL, éditions, passages, faits et limites conservés individuellement dans l’annexe. Documentation produit et présentation commerciale distinguées ; aucun identifiant natif de capacité inventé.\n- Appuis : audit numérique des données/processus ; distinction des opérations sur site et des acheminements. Aucun produit ne démontre ici un audit universel du SI ni une hiérarchie native équivalente à FLOW.')
    append('marche/comparaisons.md', '## CMP104\n\n- Objet : U301–U303, périmètre transversal d’Execution Tracking et granularité de la visibilité logistique. Catalogue U290 inchangé.\n- Sources : ELM196, S42–S45 ; S35 pour Transportation Visibility. Relation : appui sémantique et recouvrement partiel des périmètres.\n- Analyse : Dataverse/Camunda documentent des audits numériques complémentaires et configurables ; SAP/Oracle couvrent réception, opérations internes et expédition sur les sites. Avant/après transport n’est pas une partition stable des réseaux à plusieurs étapes.\n- Proposition Codex : Warehouse Visibility et Transportation Visibility directement sous D07.d ; Logistics Visibility comme notion englobante sans nouveau niveau. Les deux noms/périmètres ne sont pas déclarés taxonomie universelle du marché.\n- Statut : périmètre numérique/physique exprimé U301 et accord U302 ; décomposition réouverte U303 et nouvelle proposition non validée. Aucun déploiement Beaumanoir démontré.')
    append('JOURNAL.md', '## 2026-09-17 — U301–U303 : tracking numérique/physique et granularité logistique\n\nPérimètre utilisateur enregistré avant interprétation : audit de toutes les opérations numériques et physiques. Accord U302 conservé ; U303 réouvre la maille de Logistics Visibility. Comparaison Microsoft/Camunda/SAP/Oracle et proposition sur site/transport dans l’annexe d’audit. Aucun nœud ou rattachement créé pendant cet arbitrage ; catalogue et publications préservés.')
    append('marche/elements.md', 'Complément U304 à ELM196 : S46 Blue Yonder Store Execution (MKT27), S47 RELEX direct-to-shelf replenishment (MKT29). Présentations officielles consultées le 17 septembre 2026 ; sources, passages et limites dans l’annexe. Aucun nouveau nom normalisé de comportement prétendu.')
    append('marche/comparaisons.md', 'Complément U304 à CMP104 : le cas de mise en rayon motive une spécialisation magasin. Store Execution est un usage de marché ; Store Execution Visibility est proposé pour FLOW avec un périmètre logistique limité. Bénéfice : distinguer stock reçu, stock en réserve et marchandise accessible au client. La proposition à deux comportements U303 est réexaminée au profit de trois spécialisations entrepôt/transport/magasin, non adoptées.')

if __name__ == '__main__':
    main()
