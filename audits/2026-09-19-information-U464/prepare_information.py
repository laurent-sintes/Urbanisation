"""U464 : proposition méthodologique, sans migration du catalogue métier."""
from pathlib import Path
from copy import deepcopy
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

def save(path, value):
    write_text_if_changed(ROOT/path, dumps(value))

definition = ('Ensemble minimal d’éléments qui, reliés dans un contexte donné, portent un sens métier déterminé '
              'et explicitent ce qu’une capacité connaît, utilise, produit ou fait évoluer.')
boundary = ('L’information est décrite indépendamment de sa représentation informatique. '
            'La cartographie des informations métier ne constitue pas un modèle de données implémentable.')
examples = [
    '« 60 » seul ne précise pas l’information recherchée. « 60 pièces promises pour le 25 septembre sur la ligne L » explicite un engagement, dans le contexte de cette ligne.',
    'Pour une même ligne, 60 pièces promises le 25 septembre et 40 le 28 septembre : les liens quantité–date sont indispensables. Les séparer en deux listes non reliées ferait perdre le sens. L’échéancier rassemble deux échéances ; ce n’est pas un fait élémentaire unique démontré.',
    'Une commande complète regroupe plusieurs informations : quantités demandées, engagements, réalisations. Demande, engagement et réalisation gardent leurs sens distincts même quand un document les rapproche.',
]
refs = ['U464','U456','U461','ELM269','ELM276','ELM289','ELM290','ELM291','CMP183']
term = dict(
    id='MOD012', name='Information', label_fr='Information métier', definition=definition+'\n\n'+boundary,
    role='Expliciter le contenu métier des capacités et de leurs interactions.',
    notes=[
        'Définition proposée pour FLOW, inspirée de notions distinctes ; aucune norme consultée ne donne exactement cette définition d’Information.',
        'Le minimum se juge au regard d’une question métier et d’un contexte explicites. Le sens peut s’appuyer sur d’autres informations identifiées, sans recopier tout leur contenu.',
        'Insécable signifie ici que les éléments et leurs relations nécessaires au sens étudié doivent être conservés. Cela ne prouve ni l’irréductibilité logique d’un fait élémentaire ni l’indivisibilité d’un stockage ou d’une mise à jour.',
        'Si deux parties portent des sens autonomes utiles à des questions distinctes, les décrire comme informations reliées. Une commande, un dossier complet ou une fiche produit ne sont pas déclarés minimaux par leur seul nom.',
        'Le modèle décrit des types d’information ; un exemple chiffré illustre une occurrence. Une valeur isolée n’a pas nécessairement de sens métier sans son contexte.',
        'Information, objet métier, document et fait de gestion ne sont pas des synonymes. Une information décrit quelque chose de pertinent ; le document la formalise ; un fait de gestion rend compte d’un événement métier.',
        'Le fait élémentaire de la logique ou d’ORM n’est pas automatiquement un fait de gestion FLOW. La règle U461 fait–document demeure attachée aux faits de gestion ; elle ne requiert pas un document distinct pour chaque propriété ou proposition.',
        'Les informations sont reliées aux capacités par un rôle explicite : connaître, utiliser, établir, modifier ou constater. Ces verbes pédagogiques ne créent pas de nouveaux types de relation dans le schéma.',
        'Pour une information de référence projetée, préciser l’autorité et l’alimentation métier utiles, sans inventer de maître installé ni transférer sa responsabilité à Supply.',
    ],
    examples=examples,
    granularity_rule='Retenir le plus petit ensemble nécessaire à un sens métier explicite, avec ses liens et son contexte. Écarter les détails sans rôle pour les capacités étudiées ; distinguer les sens autonomes plutôt que regrouper tout le dossier.',
    boundary=boundary,
    analysis_ref='modeles/backlog/information-definition-U464.yaml', source_refs=refs,
    review=dict(state='proposed', requested_scope='U464 demande Information, un sens propre, une maille minimale, un lien aux capacités et l’indépendance d’un modèle implémentable.',
                proposed_scope='Définition, interprétation de l’insécabilité, exemples et règles de granularité. Aucune équivalence normative ni adoption du découpage des informations candidates.'),
)
path='modeles/backlog/modeling-glossary.yaml'
glossary=read(ROOT/path)
assert all(t['id']!='MOD012' for t in glossary['terms'])
glossary['terms'].append(term)
glossary['source_refs'].append('U464')
save(path,glossary)

sources = [
 dict(id='ELM289', reference='MKT51', name='Information / Data / Data element', version='ISO/IEC 15944-1:2025 ; ISO 20691:2022',
      url='https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso-iec:15944:-1:ed-3:v1:en',
      locator='§3.13, §3.15–3.16, §3.29 ; renvois ISO/IEC 2382:2015 et 11179-1:2023',
      observed='Information : signification en contexte ; données : représentation. Un élément de données peut être déclaré indivisible dans un contexte.',
      difference='Ne définit pas un bloc minimal de cartographie métier.',
      limits='Entrées publiques officielles consultées ; aucune lecture intégrale de 2382 ou 11179 prétendue. Sens sectoriel Open-edi non adopté.',
      complementary_url='https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso:20691:ed-1:v1:en',
      complementary_locator='§3.8–3.10 ; note sur la divisibilité contextuelle du numéro de téléphone'),
 dict(id='ELM290', reference='MKT52', name='Elementary fact / fact type is elementary in conceptual schema', version='OMG SBVR 1.5, octobre 2019',
      url='https://www.omg.org/spec/SBVR/1.5/PDF', locator='§24.2.1, page imprimée 222 ; §24.2.2.1, page imprimée 255',
      observed='L’élémentarité signifie l’impossibilité de décomposer en faits plus simples conservant collectivement le même sens dans le schéma considéré.',
      difference='Critère logique plus exigeant que la cohérence d’un ensemble utile à une capacité.',
      limits='Passages lus, pas de conformité SBVR ni de formalisation logique FLOW déduite.'),
 dict(id='ELM291', reference='MKT53', name='What Is An Elementary Fact?', version='Terry Halpin, article original 1993, réédition légèrement modifiée sur le site ORM',
      url='https://www.orm.net/pdf/ElemFact.pdf', locator='Introduction ; pages 2–3 et 6–8',
      observed='Les contraintes connues conditionnent la décomposition ; le regroupement intuitif ne démontre pas l’élémentarité.',
      difference='La carte Atlas ne vise pas la normalisation complète en faits élémentaires.',
      limits='Article de recherche historique ; la date d’indexation web n’est pas la date de publication. Aucune adoption du formalisme ORM.'),
 dict(id='ELM276', reference='MKT01', name='Information Concept / Information Map', version='TOGAF Series Guide G190, avril 2019',
      url='https://governance.foundation/assets/frameworks/togaf/g190%20-%20Information%20Mapping.pdf', locator='Chapitres 1–2 et 4–6 ; pages imprimées 1–2 et 4–7',
      observed='Les concepts d’information relient vocabulaire métier et capacités, sans dépendre des structures des systèmes.',
      difference='Un concept comme Client ou Produit n’est pas nécessairement minimal ou élémentaire.',
      limits='Document primaire sur miroir tiers ; édition historique, pas contrôle complet de la 10e édition.'),
 dict(id='ELM269', reference='MKT03', name='Information Concept', version='Business Architecture Metamodel Guide v3.0, septembre 2024',
      url='https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/Business_Architecture_Metamo.pdf', locator='§5.3–5.3.1, pages imprimées 20–22',
      observed='Les capacités utilisent et modifient des concepts d’information ; une carte d’information ne se remplace pas par un modèle IT.',
      difference='FLOW ne reprend pas la correspondance complète objets–capacités de cette méthode.',
      limits='Guide méthodologique consulté, sans adoption de toute sa taxonomie ni lecture intégrale du BIZBOK.'),
]
for source in sources: source['consulted_on']='2026-09-19'
analysis=dict(id='INFORMATION-DEFINITION-U464', as_of='2026-09-19', status='proposed_definition_and_granularity',
    source_refs=refs, canonical_term='modeles/backlog/modeling-glossary.yaml#MOD012',
    conclusion='Aucune définition unique consultée ne réunit exactement information, groupe minimal insécable et rôle dans une capacité. FLOW peut expliciter cette convention sans la présenter comme une citation ou une équivalence normative.',
    sources=sources,
    proposal=dict(term='Information', definition=term['definition'], boundary=boundary,
                  granularity=term['granularity_rule'], examples=examples),
    alternatives=[
      dict(name='Information Concept', fit='Très bon ancrage pour une carte métier et ses liens aux capacités.', limit='Ne garantit pas la maille minimale demandée.'),
      dict(name='Elementary Fact', fit='Critère théorique précis d’insécabilité logique.', limit='Granularité parfois trop fine ; une information composite utile au métier n’est pas toujours un fait élémentaire. Le mot fait risquerait aussi de brouiller U461.'),
      dict(name='Information — convention FLOW', fit='Nom demandé ; sens, contexte et minimum utile explicités.', limit='Recommandation locale, sans équivalence normative. Les découpages concrets doivent être éprouvés sur les pilotes.', recommendation=True),
    ],
    selection_checks=[
      'Formuler la question métier à laquelle l’information répond et donner une occurrence compréhensible.',
      'Identifier sujet, sens des valeurs et contexte indispensables ; rendre explicites les relations qui portent ce sens.',
      'Écarter les éléments sans rôle pour cette question et séparer les sens autonomes ; ne pas descendre à chaque champ technique.',
      'Nommer les capacités qui connaissent, utilisent ou font évoluer l’information ; ne pas inférer un propriétaire exclusif.',
      'Distinguer demande, hypothèse, proposition, engagement, règle et constat selon le cas, sans leur imposer un cycle universel.',
    ],
    preserved=['Objet métier, Information, document et fait de gestion distincts.',
               'Convention U461 limitée aux faits de gestion, pas à tout fait au sens de la logique.',
               'Capacité → Comportement reste la décomposition terminale ; Information ne la prolonge pas.',
               'Pas de schéma de tables, classes, messages ou API prescrit ; une représentation ultérieure reste possible.',
               'Aucune correspondance 1:1 Information/table, Information/document ou Information/capacité imposée.'],
    next_step='Éprouver cette règle sur les cinq pilotes ; arbitrer les frontières concrètes avant d’étendre le schéma ou le catalogue métier.',
    report='audits/2026-09-19-information-U464/recherche.md')
save('modeles/backlog/information-definition-U464.yaml',analysis)

path='modeles/backlog/modeling-guide-U458.yaml'
guide=read(ROOT/path)
guide['source_refs'].append('U464')
guide['sources'].append(dict(id='U464',title='Définir les informations métier indépendamment de leur implémentation',
    excerpt="Prochaine étape : la data. Ou plutot les informations métier. Il faut définir la notion d'Information dans le méta modèle et dire que ce n'est pas un modèle de données implémentable, une information est groupe de données insécables minimum, portant son propre sens et explicitant les capacités.\nRecherche dans la théorie des données la définition exacte et limpide de cette notion",
    scope='Demande et intention ; la définition proposée et l’interprétation précise de la maille minimale ne sont pas adoptées par anticipation.'))
guide['glossary']['terms'].append({k:deepcopy(term[k]) for k in ['id','name','label_fr','definition','role','examples']})
lesson=next(l for l in guide['lessons'] if l['id']=='business-objects')
lesson['explanation'] += ' Une Information explicite le sens métier utile à une capacité, avec les éléments et le contexte nécessaires. Sa maille minimale se juge sur ce sens ; la cartographie ne prescrit pas de modèle de données implémentable.'
lesson['contributor']['scope'] += ' U464 : notion Information et règle de granularité proposées, sans assimiler tout fait logique à un fait de gestion.'
lesson['contributor']['source_refs'].append('U464')
save(path,guide)

path='modeles/backlog/information-pilots-U458.yaml'
pilots=read(ROOT/path)
pilots['source_refs'].append('U464')
pilots['conventions']['information_definition_proposal'] = dict(
    term_ref='MOD012',analysis_ref='modeles/backlog/information-definition-U464.yaml',
    status='proposed_not_applied_to_all_candidates',
    rule='Éprouver la maille des informations candidates par leur sens et leurs usages. Product, Order ou un dossier entier ne sont pas déclarés insécables par défaut. Les candidats existants restent conservés, sans nouveau nœud canonique.')
save(path,pilots)
path='modeles/backlog/v0-readiness.yaml'
readiness=read(ROOT/path)
readiness['execution_U458']['follow_up_U464']=dict(
    report='audits/2026-09-19-information-U464/recherche.md',
    term_ref='MOD012', status='methodological_definition_proposed',
    remaining='Confirmer la convention de granularité et l’éprouver sur les cinq pilotes avant d’étendre le contrat ; pas de modèle de données implémentable ni de publication implicite.')
save(path,readiness)
print('MOD012 proposé ; analyse, guide futur et suivi des pilotes actualisés. Catalogue métier et schéma conservés.')
