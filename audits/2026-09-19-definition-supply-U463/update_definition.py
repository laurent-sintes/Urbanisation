"""Correction éditoriale U463 ; préserver périmètre, accords et publications."""
from pathlib import Path
from copy import deepcopy
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

def save(path, data):
    write_text_if_changed(ROOT / path, dumps(data))

model = read(ROOT / 'modeles/backlog/model.yaml')
node = next(n for n in model['nodes'] if n['id'] == 'universe-supply')
assert node['fields']['definition'] == 'Univers du pilotage transactionnel de la Supply ; priorité de l’exploration courante.'
assert node['lifecycle']['validated_fields'] == ['name']
node['fields']['definition'] = (
    'Coordonner la satisfaction des demandes Supply : gérer les commandes et les stocks, '
    'établir les engagements de quantités et de dates, optimiser l’usage des ressources '
    'et piloter la réalisation avec les services exécutants.'
)
common = dict(consulted_on='2026-09-19', status='proposed', source_refs=['U373','U455','U456','U463','CMP182'])
node['fields']['market_comparisons'] = [
    dict(deepcopy(common),
        vendor='The Open Group', product='TOGAF Series Guide — Business Capabilities',
        element_name='Defining a Business Capability', element_type='Méthode d’architecture métier',
        relationship='Appui méthodologique',
        similarities='Décrire les aptitudes et résultats métier, en distinguant ce qui est fait de l’organisation et des moyens employés.',
        differences='Le guide traite des capacités ; il ne définit ni l’univers Supply de FLOW ni son périmètre. Aucune conformité de la structure FLOW n’en est déduite.',
        flow_position='La définition de l’univers synthétise les responsabilités de ses domaines. Une qualification technique ne délimite pas ce métier.',
        definition_choice='Commandes, stocks, engagements, optimisation et pilotage de la réalisation rendent explicites les responsabilités déjà présentes. La mention de priorité d’exploration est retirée de la définition métier. Le périmètre demeure inchangé.',
        source_title='Business Capabilities — TOGAF Series Guide',
        source_url='https://governance.foundation/assets/frameworks/togaf/g189%20-%20Business%20Capbility.pdf',
        source_version='G189, juin 2018 ; édition historique',
        source_locator='§2 et §2.1.2, pages imprimées 2–3 (pages PDF 12–13)',
        evidence_limits='Document primaire consulté sur un hébergement tiers, sans redistribution. Le portail officiel TOGAF 9.2 redirige vers une authentification ; aucune vérification de la 10e édition pour ce passage.',
        source_refs=common['source_refs']+['ELM019']),
    dict(deepcopy(common),
        vendor='Microsoft', product='Dynamics 365 Intelligent Order Management',
        element_name='Order orchestration, inventory visibility and fulfillment optimization',
        element_type='Responsabilités documentées dans un produit', relationship='Recouvrement partiel',
        similarities='Coordonner les commandes jusqu’à leur satisfaction, utiliser la visibilité du stock et mobiliser les partenaires et les décisions d’optimisation.',
        differences='La documentation décrit un produit et ses composants. Elle ne couvre ni ne délimite tous les domaines de l’univers FLOW.',
        flow_position='Appui au sens métier de coordination. Aucun composant ou produit Microsoft n’est repris comme niveau de notre cartographie.',
        term_choice='Supply Chain Orchestration conserve le nom adopté : il souligne la coordination. OMS désigne aussi une catégorie de produits dont le périmètre varie ; ce n’est pas un équivalent de l’univers. Aucun intitulé universel couvrant exactement FLOW n’est établi.',
        source_title='Intelligent Order Management overview',
        source_url='https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview',
        source_version='Documentation évolutive ; mise à jour affichée le 30 janvier 2026',
        source_locator='Introduction ; Components ; Orchestration ; Inventory visibility service ; Fulfillment optimization',
        evidence_limits='Texte primaire reconsulté. Recouvrement fonctionnel partiel, sans choix de solution ni preuve de réalisation installée.',
        source_refs=common['source_refs']+['ELM279']),
]
node['fields']['examples'] = [{
    'title':'De l’intention à la réalisation',
    'situation':'Le commerce capte une intention d’achat et sollicite la Supply pour déterminer comment la satisfaire.',
    'outcome':'La Supply établit les engagements et coordonne les prestations logistiques nécessaires. Les faits de réalisation permettent de suivre leur respect et les écarts.',
    'lesson':'Ces responsabilités coopèrent. L’exemple ne crée ni une hiérarchie entre univers ni un parcours obligatoire pour toutes les commandes.',
    'source_refs':['U455','U463'],
}]
node['revision'] += 1
node['source_refs'] += ['U463','C108','ELM019','ELM279','CMP182']
node['review']['note'] += ' U463 corrige la définition héritée du découpage en couches ; reformulation, rapprochements et exemple éditoriaux proposés. Le nom adopté U373 reste inchangé.'
save('modeles/backlog/model.yaml', model)

glossary = read(ROOT / 'modeles/backlog/glossary.yaml')
terms = {t['id']:t for t in glossary['terms']}
oms = terms['TER034']
oms['definition'] = 'Dans le vocabulaire fonctionnel FLOW, prise en charge des parcours liés à la vente et coordination des contributions de la Supply pour satisfaire les demandes.'
oms['short_description'] = 'Prise en charge des parcours liés à la vente, en coopération avec la Supply.'
oms['context'] = 'Sens fonctionnel local, distinct de la catégorie de produits OMS. Il ne désigne pas un univers supérieur à [Supply Chain Orchestration](model:universe-supply).'
oms['notes'] = 'U54/U55 décrivaient les parcours et leur articulation avec la Supply selon l’ancien découpage. U373 distingue le nom de l’univers de la catégorie de produits OMS ; U455/U463 remplacent la hiérarchie par la coopération de responsabilités. La définition reste une convention locale, sans équivalence avec tout produit OMS ni adoption de nouveaux domaines.'
oms['source_refs'] += ['U54','U55','U373','U455','U463','C108']
oms['review']['note'] += ' U463 : reformulation proposée sans couche supérieure ; formulation antérieure préservée dans les sources, publications et la capture avant modification.'
supply = terms['TER035']
supply['definition'] = 'Périmètre métier qui coordonne et optimise la satisfaction des demandes en mobilisant commandes, stocks, engagements et services exécutants.'
supply['short_description'] = 'Coordination et optimisation métier de la satisfaction des demandes Supply.'
supply['context'] = 'Sens fonctionnel local porté par [Supply Chain Orchestration](model:universe-supply), distinct du côté ressources [Supply](glossary:TER083) et du système étendu [Supply Chain](glossary:TER084).'
supply['notes'] = 'Les formulations U56–U58 et U367 sont conservées dans les sources et les publications historiques. U455/U463 remplacent la lecture en couches par des domaines et univers en interaction. Le périmètre fonctionnel FLOW ne couvre pas par déduction toute la Supply Chain ; les services exécutants conservent la responsabilité de leurs opérations. [Fulfillment](glossary:TER085) désigne la satisfaction des commandes.'
supply['source_refs'] += ['U373','U455','U456','U463','C108']
supply['review']['note'] += ' U463 remplace la formulation héritée après U455 ; reformulation proposée à périmètre constant. La clarification historique U367 est préservée dans la capture avant modification.'
glossary['source_refs'] += ['U455','U463','C108']
save('modeles/backlog/glossary.yaml', glossary)

path = 'modeles/backlog/domain-interactions-U455-U456.yaml'
interactions = read(ROOT / path)
interactions['source_refs'] += ['U463','C108','CMP182']
interactions['migration']['follow_up_U463'] = {
    'report':'audits/2026-09-19-definition-supply-U463/rapport.md',
    'scope':'Définition de universe-supply et termes TER034/TER035 alignés sur les responsabilités métier ; deux rapprochements sourcés et exemple U455 sur la fiche de l’univers.',
    'limits':'Retrait de la qualification transactionnelle du périmètre et de la hiérarchie OMS/Supply. Les citations historiques et les mécanismes techniques documentés restent conservés ; aucune suppression lexicale générale ni nouveau découpage.',
}
save(path, interactions)
path = 'modeles/backlog/v0-readiness.yaml'
readiness = read(ROOT / path)
readiness['execution_U458']['follow_up_U463'] = {
    'report':'audits/2026-09-19-definition-supply-U463/rapport.md',
    'remaining':'Définition de l’univers et glossaire corrigés dans le backlog ; intégration à la prochaine publication distincte.',
}
save(path, readiness)
print('U463 : un univers et deux termes corrigés ; deux comparaisons et un exemple ajoutés.')
