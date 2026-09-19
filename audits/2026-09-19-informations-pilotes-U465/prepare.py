"""Construction éditoriale U465/U466 ; ne pas rejouer après une édition des annexes."""
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed

OUT = ROOT / 'modeles/backlog/information-cards-U465.yaml'
assert not OUT.exists(), 'Annexe déjà créée : modifier le YAML faisant autorité.'


def role(capability, verb, meaning, refs):
    return dict(capability_ref=capability, role=verb, meaning=meaning,
                qualification='proposed_from_current_responsibility', source_refs=refs)


def card(number, pilot, name, label, question, definition, context, elements,
         minimum, separated, roles, example, refs, market, term_choice, definition_choice,
         opens=None, document=None):
    return dict(
        id=f'PINFO-{number:03d}', pilot_ref=pilot, name=name, label_fr=label,
        question=question, definition=definition, context=context,
        essential_elements=elements, granularity_rationale=minimum,
        separate_meanings=separated, capability_roles=roles,
        document_and_fact_boundary=document or 'Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.',
        example=dict(kind='illustrative_not_observed', text=example, source_refs=refs),
        market_comparison=dict(support_ref=market, term_choice=term_choice,
                               definition_choice=definition_choice,
                               status='proposed_not_validated'),
        source_refs=list(dict.fromkeys(['U464', 'U465', *refs, 'CMP184'])),
        open_items=opens or [],
        review=dict(definition='proposed', granularity='proposed',
                    roles='proposed', example='editorial_illustration',
                    limits='Ni identité technique, ni cardinalité, ni autorité installée déduite.'))


cards = [
card(1, 'PILOT-PURCHASE', 'Purchase Requirement', 'Attendu d’achat',
     'Qu’est-ce qui est demandé au fournisseur pour cette partie de l’achat ?',
     'Attendu exprimé envers un fournisseur pour une partie identifiée d’un achat : bien ou prestation, quantité ou résultat attendu, destinataire et conditions de réalisation demandées.',
     'Une partie de Purchase Order dont l’attendu peut être expliqué séparément. Une commande peut en réunir plusieurs ; aucune structure de ligne informatique imposée.',
     ['Commande et partie concernées ; fournisseur sollicité.', 'Bien ou prestation et quantité avec unité, ou résultat attendu si la prestation n’est pas quantifiée.', 'Destinataire, échéance et conditions nécessaires pour comprendre l’attendu.'],
     'Conserver ensemble l’objet demandé, son étendue et ses conditions évite de confondre deux demandes du même bien. Une autre échéance autonome se décrit avec son propre attendu.',
     ['La réponse fournisseur, les conditions acceptées et la réalisation répondent à d’autres questions.', 'Prix ou modalités de paiement ne sont décrits ici que s’ils changent le sens de l’attendu étudié ; aucun dossier achat exhaustif.'],
     [role('D04.j', 'établit et fait évoluer', 'Maintient l’attendu de l’achat selon les changements autorisés.', ['U391', 'U403']),
      role('D07.c', 'utilise', 'Rapproche les résultats de service de ce qui était attendu.', ['U460'])],
     'La partie A de l’achat PO-EXEMPLE-01 demande 100 pièces de la variante V au fournisseur F, livrées au site S vendredi. « 100 » seul ne dit ni quoi, ni pour qui, ni quand.',
     ['U391', 'U403', 'U460'], 'MS-PURCHASE',
     'Purchase Requirement est un libellé descriptif proposé pour l’attendu au sein d’un Purchase Order ; ce n’est ni une Purchase Requisition distincte ni un nom normalisé revendiqué.',
     'La documentation Microsoft distingue commande envoyée et réponse du fournisseur. FLOW en extrait l’attendu métier sans reprendre les états, lignes ou écrans du produit.', ['V0-P03']),
card(2, 'PILOT-PURCHASE', 'Supplier Response', 'Réponse fournisseur',
     'Quelle réponse le fournisseur apporte-t-il à cet attendu d’achat ?',
     'Position reçue d’un fournisseur sur une partie d’achat demandée : acceptation, refus ou proposition de conditions différentes.',
     'Une réponse attribuée à un fournisseur et rattachée à l’attendu auquel elle répond ; ses conditions conservent leurs associations quantité–date.',
     ['Fournisseur répondant et attendu concerné.', 'Position exprimée et conditions proposées ou motif de refus utile.', 'Moment ou contexte permettant de distinguer cette réponse de celles qu’elle réexamine.'],
     'Une réponse peut être reçue et étudiée sans être acceptée. Son sens autonome justifie une fiche distincte de l’engagement accepté.',
     ['Réception d’une réponse ne vaut pas acceptation.', 'Identité des révisions, délai de réponse et pouvoir d’acceptation restent ouverts.'],
     [role('D04.j', 'reçoit et connaît', 'Supplier Confirmation BHV078 explicite les réponses et écarts à l’attendu.', ['U403', 'U460'])],
     'Pour 100 pièces demandées vendredi, F propose 60 vendredi et 40 mardi. La réponse est connue ; aucune acceptation de ces nouvelles conditions n’est supposée.',
     ['U403', 'U460'], 'MS-PURCHASE',
     'Supplier Response conserve le sens métier des vendor responses Microsoft, avec Supplier déjà utilisé dans FLOW. L’information ne se limite pas à une confirmation positive.',
     'Acceptation, refus et changements documentés par Microsoft étayent la séparation entre réponse et conditions retenues. U466 ne valide pas cette séparation côté achats par extension.', ['V0-P03']),
card(3, 'PILOT-PURCHASE', 'Supplier Commitment', 'Engagement fournisseur accepté',
     'Quelles conditions de réalisation de cet achat sont actuellement retenues ?',
     'Conditions de réalisation retenues comme engagement du fournisseur pour une partie identifiée d’un achat, après l’acceptation requise dans ce contexte métier.',
     'Engagement relatif à l’achat fournisseur. Il ne se confond pas avec la promesse faite au bénéficiaire d’une autre commande.',
     ['Fournisseur et partie d’achat concernée.', 'Quantité et unité, ou résultat attendu, associés aux échéances et conditions retenues.', 'Référence au contexte d’acceptation qui permet de distinguer engagement et simple réponse.'],
     'L’engagement peut rester valable pendant l’examen d’une réponse différente. Les preuves et règles permettant de le reconnaître restent à préciser, sans inférer une nouvelle règle d’autorisation.',
     ['Ne désigne pas tout le dossier fournisseur.', 'N’entraîne ni réception, ni nouvelle promesse client, ni réservation automatique.'],
     [role('D04.j', 'maintient', 'Distingue l’attendu initial des conditions fournisseur effectivement acceptées.', ['U403', 'U460']),
      role('D03.n', 'utilise', 'Prend en compte les conditions fournisseur pertinentes pour examiner la promesse de satisfaction, sans copie automatique.', ['U441', 'U460'])],
     'Les 60 pièces vendredi et 40 mardi sont acceptées pour cet achat. Une promesse client de 100 vendredi reste un engagement distinct à réexaminer ; elle n’est pas réécrite silencieusement.',
     ['U403', 'U441', 'U460'], 'MS-PURCHASE',
     'Supplier Commitment reprend le candidat existant en précisant ici « accepté ». Confirmed Purchase Order serait plus documentaire et trop large pour cette partie d’achat.',
     'Microsoft distingue réponse fournisseur et commande confirmée. L’engagement conceptuel proposé ne reprend ni la confirmation automatique du produit ni son modèle de versions.', ['V0-P03']),
card(4, 'PILOT-PURCHASE', 'Purchase Fulfillment Result', 'Réalisation d’achat constatée',
     'Qu’a-t-on constaté comme réalisé pour cet attendu d’achat ?',
     'Résultat de réception d’un bien ou de réalisation d’une prestation, rapproché d’un attendu d’achat et qualifié avec ses éventuels écarts.',
     'Un résultat métier constaté pour une partie d’achat et un moment donnés ; aucune réalisation physique exécutée par la seule cartographie.',
     ['Attendu concerné et bien reçu ou prestation réalisée.', 'Quantité avec unité ou résultat observé, moment et écarts utiles.', 'Document métier identifié qui consigne le fait de gestion correspondant.'],
     'Sans attendu, moment et quantité ou résultat, le constat ne permet pas de dire ce qui a été réalisé. Un autre constat indépendant garde son propre sens.',
     ['Un résultat n’est ni l’engagement fournisseur ni le solde restant.', 'Le lieu de constat, la validation de qualité et les corrections ne sont détaillés que si les règles métier l’exigent.'],
     [role('D07.c', 'rapproche et qualifie', 'Rapproche les réalisations reçues des attendus et qualifie les écarts ; ne devient pas le réceptionnaire physique.', ['U460']),
      role('D04.j', 'utilise', 'Explique la progression de l’achat à partir des réalisations reconnues.', ['U391', 'U461'])],
     'REC-EXEMPLE-01 consigne la réception de 60 pièces sur les 100 attendues. Pour une prestation, un document identifié pourrait consigner le résultat observé ; son type et son auteur restent à établir.',
     ['U391', 'U460', 'U461'], 'MS-RECEIPT',
     'Purchase Fulfillment Result est proposé pour couvrir biens et prestations. Product receipt serait trop étroit ; Receipt Fact reste le cas illustré de réception.',
     'Le document de réception Microsoft fournit un exemple concret de constat documenté. Le lien obligatoire fait–document vient de U461 ; la généralisation aux prestations reste conceptuelle.', ['V0-P03'],
     'Le résultat rend compte d’un fait de gestion. U461 impose un document identifié ; son auteur, le nombre exact de documents, les corrections et les preuves d’acceptation ne sont pas inventés.'),
card(5, 'PILOT-PURCHASE', 'Purchase Fulfillment Balance', 'Reste à réaliser d’achat',
     'Que reste-t-il à réaliser au regard de l’attendu actuellement applicable ?',
     'Part encore attendue d’un achat, expliquée à partir de l’attendu applicable et des réalisations reconnues dans un contexte d’appréciation donné.',
     'Une partie d’achat et une situation de référence explicites ; le reste peut être quantitatif ou exprimé comme résultat restant à atteindre.',
     ['Attendu applicable et contexte d’appréciation.', 'Réalisations reconnues et ajustements métier applicables, lorsqu’ils sont établis.', 'Reste à réaliser, avec unité ou résultat attendu et explication du rapprochement.'],
     'Le solde répond à une question différente du dernier constat. On conserve ses bases d’interprétation pour ne pas confondre restant demandé, accepté et réalisé.',
     ['Aucune formule universelle pour retours, annulations, dépassements ou prestations.', 'Une information calculée n’est pas automatiquement un nouveau fait de gestion.'],
     [role('D04.j', 'connaît et fait évoluer', 'Rend lisible la part restant à réaliser dans le suivi de l’achat.', ['U391', 'U460'])],
     'Dans le cas simple sans autre changement : 100 pièces encore applicables, 60 reconnues reçues, donc 40 restantes. Une annulation autorisée de 10 demanderait une règle explicite ; elle n’est pas déduite de cette soustraction.',
     ['U391', 'U460', 'U461'], 'MS-RECEIPT',
     'Purchase Fulfillment Balance est descriptif et proposé. Le vocabulaire exact d’un solde de réception ERP n’est pas adopté comme terme universel.',
     'Le suivi des réceptions éclaire le besoin ; la fiche FLOW est motivée par la question « que reste-t-il ? ». La source ne prouve pas une information autonome identique pour toutes les prestations.', ['V0-P03']),
card(6, 'PILOT-PRODUCT', 'Product Reference Identity', 'Identité de référence produit',
     'De quelle référence de produit ou variante parle-t-on ?',
     'Identification métier du produit ou de la variante auxquels se rapportent les informations projetées dans Supply, avec les distinctions nécessaires pour les reconnaître.',
     'Une référence partagée de produit ou variante, distincte d’un exemplaire physique et de sa présence dans un catalogue.',
     ['Référence reconnue et nature Produit ou Variante.', 'Pour une variante, produit de rattachement et combinaison de caractéristiques qui la distingue dans ce contexte.'],
     'La référence fournit le sujet des autres informations sans absorber toutes ses caractéristiques. La combinaison distinctive d’une variante est utile à sa reconnaissance, sans prétendre être un fait logique élémentaire.',
     ['Présence dans un catalogue, identifiant commercial et unité physique gardent des sens distincts.', 'Article et Container restent des rôles déjà définis, sans créer ici de nouveaux types de produits.'],
     [role('D08.d', 'reçoit et projette', 'Reconnaît les références externes dans la projection Supply.', ['U460']),
      role('D04.j', 'utilise', 'Désigne la référence concernée par l’achat sans devenir maître de sa définition.', ['U460'])],
     'La variante V « modèle M, bleu, taille 38 » apparaît dans deux catalogues. Il s’agit d’une référence de variante, pas de deux variantes ni d’un exemplaire physique unique.',
     ['U460', 'ELM280', 'ELM282'], 'MS-PRODUCT',
     'Product et Product Variant sont déjà définis dans FLOW et présents chez Microsoft. Product Reference Identity décrit leur reconnaissance ; ce composé n’est pas revendiqué comme standard.',
     'La distinction produit/variante étaye le sujet projeté. La création et l’administration de maîtres décrites par Microsoft restent extérieures à Supply.', ['V0-P02']),
card(7, 'PILOT-PRODUCT', 'Product Characteristic', 'Caractéristique produit',
     'Quelle caractéristique est affirmée pour cette référence dans ce contexte ?',
     'Valeur d’une propriété d’un produit ou d’une variante, reliée à son sujet et au contexte dans lequel cette valeur s’applique.',
     'Une assertion de caractéristique utile aux capacités étudiées. Deux propriétés autonomes ou deux contextes contradictoires ne sont pas fusionnés en une valeur unique.',
     ['Référence concernée et propriété décrite.', 'Valeur et unité lorsqu’elle est nécessaire au sens.', 'Périmètre et période d’application utiles ; origine permettant de qualifier l’affirmation.'],
     '« 0,4 kg » ne porte pas le sens étudié sans sujet et propriété. Couleur et poids répondent à deux questions autonomes ; on ne déclare pas toute la fiche produit insécable.',
     ['Réception récente ne garantit pas validité actuelle.', 'Une propriété n’exige pas un document distinct au titre de U461.'],
     [role('D08.d', 'reçoit et met à jour la projection', 'Conserve les caractéristiques reçues avec le contexte permettant de les interpréter.', ['U460'])],
     'L’émetteur A affirme « poids net de V : 0,4 kg, applicable au lot de fabrication considéré » ; B affirme 0,5 kg dans le même contexte. Les deux assertions sont compréhensibles, mais leur conflit ne se tranche pas par la date de réception seule.',
     ['U460', 'ELM280', 'U464'], 'MS-PRODUCT',
     'Product Characteristic désigne le sens métier commun des propriétés et attributes documentés. Attribute pourrait évoquer un champ de produit ; aucun schéma de champs n’est prescrit.',
     'Microsoft fournit des exemples de propriétés produit. Le choix d’une assertion contextualisée est la proposition de granularité FLOW, pas une équivalence avec son stockage des attributs.', ['V0-P02']),
card(8, 'PILOT-PRODUCT', 'Product Identifier Association', 'Association d’identifiant produit',
     'À quelle référence correspond cet identifiant dans ce système d’identification ?',
     'Correspondance entre un identifiant interprété dans son système ou contexte d’attribution et la référence produit ou variante qu’il désigne.',
     'Identification d’une référence ; aucune unicité mondiale d’un code local ni identification implicite d’un exemplaire.',
     ['Valeur de l’identifiant et système ou contexte d’attribution.', 'Référence désignée et périmètre d’application utile.'],
     'Le même texte de code peut avoir des sens différents selon son émetteur. Sujet désigné et système d’identification sont indispensables à la correspondance.',
     ['Identité métier et code qui la désigne ne sont pas synonymes.', 'Une association GTIN–référence ne prouve pas l’identité d’une unité physique.'],
     [role('D08.d', 'reçoit et projette', 'Conserve les correspondances reçues pour reconnaître les références.', ['U460'])],
     'Le code fournisseur F:123 renvoie à V. Un identifiant de référence partagé par dix exemplaires ne suffit pas à distinguer ces dix unités ; GS1 illustre cette autre question par GTIN et numéro de série.',
     ['U460', 'ELM280', 'ELM282'], 'GS1-IDENTITY',
     'Identifier est établi dans les sources Microsoft/GS1 ; Association explicite ici la correspondance métier. Aucun format d’identifiant FLOW n’est imposé.',
     'La distinction GS1 référence/instance borne le sens de cette fiche. Il ne s’agit ni d’une conformité GS1 ni d’une obligation de sérialiser toutes les unités.', ['V0-P02']),
card(9, 'PILOT-PRODUCT', 'Reference Authority', 'Autorité sur l’information de référence',
     'Quelle autorité fait foi pour cette information dans ce périmètre ?',
     'Attribution d’une autorité métier sur un contenu de référence et un périmètre donnés, permettant d’expliciter à quel titre une information est tenue pour référence.',
     'Autorité sur une information ou un ensemble cohérent de propriétés ; aucune autorité unique sur toute la fiche produit supposée.',
     ['Rôle métier faisant autorité, s’il est établi.', 'Contenu et périmètre couverts par cette autorité.', 'Conditions de reconnaissance de l’autorité, lorsqu’elles sont connues.'],
     'Un nom d’émetteur seul ne dit ni sur quoi il fait foi ni à quel titre. L’autorité a un sens distinct de la réception d’une valeur.',
     ['L’émetteur peut être un intermédiaire.', 'Pas de PIM, d’équipe, de système maître ou d’arbitre Beaumanoir inventé.'],
     [role('D08.d', 'utilise', 'Interprète la projection à la lumière des autorités établies ; ne les attribue pas par simple ingestion.', ['U460'])],
     'Une autorité externe pourrait faire foi sur les dimensions physiques, une autre sur une classification commerciale. Cet exemple illustre la portée d’une autorité ; il ne décrit aucune organisation installée.',
     ['U460', 'U464'], 'FLOW-PROJECTION',
     'Reference Authority est une formulation descriptive proposée de la responsabilité faisant foi. Aucun objet éditeur homonyme n’a été établi dans les sources consultées.',
     'La séparation est motivée par la convention FLOW de projection et par V0-P02. Les références d’architecture soutiennent la description métier ; elles ne désignent pas les autorités locales.', ['V0-P02']),
card(10, 'PILOT-PRODUCT', 'Reference Receipt', 'Réception d’information de référence',
     'Quel contenu de référence a été reçu, de qui et quand ?',
     'Contexte de réception d’un contenu de référence dans la projection Supply : contenu concerné, émetteur et moment de réception, avec l’origine connue utile à son interprétation.',
     'Une réception métier d’information ; pas un message technique ou un journal d’interface. Deux réceptions du même contenu peuvent éclairer sa fraîcheur sans changer sa validité.',
     ['Contenu de référence reçu, identifié sans en recopier tout le dossier.', 'Émetteur et moment de réception.', 'Origine déclarée et contexte de transmission lorsqu’ils sont utiles et connus.'],
     'La fraîcheur de réception est relative à un contenu précis. Une date seule ne dit pas ce qui a été reçu ; une réception ne suffit pas à établir la vérité du contenu.',
     ['Validité du contenu et heure de réception sont distinctes.', 'Le seuil de fraîcheur dépend de l’usage ; aucune règle automatique d’acceptation ou de rejet.'],
     [role('D08.d', 'connaît', 'Conserve le contexte utile de l’information reçue pour expliquer la projection.', ['U460'])],
     'Une caractéristique valable au 1er septembre est reçue le 19 septembre par un distributeur. Sa réception est récente ; sa validité aujourd’hui et l’autorité de son origine restent à examiner.',
     ['U460', 'U464'], 'FLOW-PROJECTION',
     'Reference Receipt décrit la provenance de réception pour les lecteurs métier ; aucun terme standard unique n’est revendiqué. Ce n’est pas Product Receipt, qui concerne les biens.',
     'La séparation réception/validité répond aux cas du pilote. Le besoin de provenance ne prescrit pas un flux, un mécanisme d’intégration ou un journal applicatif.', ['V0-P02'],
     'La fiche décrit le contexte de provenance. Si l’arrivée est également modélisée comme fait de gestion, U461 exige son document identifié ; ce classement et ce document ne sont pas inventés ici.'),
card(11, 'PILOT-COMMITMENT', 'Fulfillment Proposal', 'Proposition de satisfaction',
     'Quelles conditions de satisfaction sont proposées pour cette demande ?',
     'Conditions de satisfaction proposées pour une partie identifiée d’une demande, soumises à confirmation sans valoir à elles seules engagement.',
     'Une proposition relative à une demande. Elle peut concerner un engagement initial ou une révision ; un engagement actuel peut rester valable pendant son examen.',
     ['Demande et partie concernées ; destinataire de la proposition.', 'Quantité avec unité associée à la date et aux conditions proposées.', 'Contexte de proposition ; engagement concerné en cas de réexamen.'],
     'Proposition et engagement ont des sens et effets distincts, adoptés U466. Dans chacun, préserver l’association partie–quantité–date ; un échéancier peut réunir plusieurs parties sans devenir un fait élémentaire unique.',
     ['La proposition n’est pas une réservation ni une affectation.', 'Identités, versions, durée de validité et acceptation partielle restent à préciser.'],
     [role('D03.n', 'établit et révise', 'Promise Proposal BHV021 formalise ce qui peut être proposé sans refaire la décision d’échéancier.', ['U441', 'U443', 'U466']),
      role('D03.l', 'détermine les conditions utilisées', 'Delivery Schedule Decision choisit la distribution quantité–date qui alimente la proposition ; ne la confirme pas pour autant.', ['U441', 'U460'])],
     'L’engagement actuel prévoit 100 pièces vendredi. Une proposition de révision prévoit 60 vendredi et 40 lundi. Tant que le changement n’est pas confirmé selon les règles applicables, l’engagement actuel reste distinct et valable.',
     ['U441', 'U443', 'U466'], 'MARKET-PROMISE',
     'Fulfillment Proposal est proposé en cohérence avec Fulfillment Commitment et Promise Proposal BHV021. Delivery Schedule ne distinguerait pas à lui seul proposition et engagement.',
     'Microsoft et Oracle illustrent les répartitions quantité–date ; U466 fonde la séparation des deux informations. Les sources ne prouvent pas une taxonomie commune à tous les éditeurs.', ['V0-P03', 'V0-A02']),
card(12, 'PILOT-COMMITMENT', 'Fulfillment Commitment', 'Engagement de satisfaction',
     'Quelles conditions de satisfaction sont actuellement promises pour cette demande ?',
     'Conditions de satisfaction confirmées pour une partie identifiée d’une demande : ce qui est promis, à qui, pour quelle quantité et quelle date, sous les conditions métier applicables.',
     'Engagement métier distingué de la capacité homonyme qui le maintient. Une proposition peut préparer sa révision sans le remplacer automatiquement.',
     ['Demande et partie concernées ; bénéficiaire de l’engagement.', 'Quantité avec unité associée à la date et aux conditions confirmées.', 'Contexte de confirmation permettant de reconnaître l’engagement applicable.'],
     'Le même couple quantité–date peut être proposé ou engagé : son effet métier diffère. L’engagement n’inclut pas toute la ressource choisie pour l’honorer.',
     ['N’attribue pas de ressource précise et ne bloque pas les usages concurrents.', 'Les règles de confirmation, correction, remplacement et effets sur d’autres commandes restent ouvertes.'],
     [role('D03.n', 'confirme et fait évoluer', 'Promise Confirmation BHV022 et Promise Revision BHV023 maintiennent les conditions engagées.', ['U441', 'U443', 'U466'])],
     '60 pièces vendredi et 40 lundi sont confirmées. Affecter demain une autre ressource compatible peut conserver exactement cet engagement. Une nouvelle proposition de dates reste une information distincte.',
     ['U441', 'U443', 'U445', 'U436', 'U466'], 'MARKET-PROMISE',
     'Fulfillment Commitment reprend le nom adopté de la capacité U445 pour l’information qu’elle entretient ; la nature Information évite de les confondre.',
     'Le nom et le périmètre restent FLOW. Confirmation de commande chez un éditeur n’est pas une équivalence complète ; l’absence de réservation implicite est la convention U436.', ['V0-P03', 'V0-A02']),
card(13, 'PILOT-ASSIGNMENT', 'Supply Assignment', 'Affectation de ressources',
     'Quelle ressource est affectée à quelle demande, pour quelle part ?',
     'Lien retenu entre une ressource et une partie de demande à satisfaire, avec la quantité et les conditions d’application de cette affectation.',
     'Une affectation identifiée par son sens ressource–demande, distincte du plan qui l’a choisie, de la promesse et du droit de réservation.',
     ['Ressource concernée et demande bénéficiaire.', 'Quantité avec unité et contexte d’application.', 'Conditions particulières de maintien, par exemple un gel, seulement lorsqu’elles sont explicites.'],
     'Ressource seule ou quantité seule ne dit pas à quelle demande elle est affectée. Plusieurs liens peuvent composer un plan sans fusionner leur sens.',
     ['Un gel limite la modification de l’affectation ; il ne réserve pas automatiquement.', 'L’affectation peut changer sans modifier la promesse si les conditions restent compatibles.'],
     [role('D02.e', 'établit et fait évoluer', 'Applique et maintient les liens choisis ; ne décide pas à nouveau le plan.', ['U345', 'U364', 'U436']),
      role('D03.o', 'détermine le choix utilisé', 'Fulfillment Plan Decision choisit le scénario dont découlent les affectations à appliquer.', ['U378', 'U460'])],
     '40 pièces affectées depuis A à la demande L sont réaffectées depuis B. Si la même date et les mêmes conditions sont possibles, la promesse reste inchangée. Sans réservation, ce lien ne bloque pas les usages concurrents.',
     ['U345', 'U364', 'U436', 'U443', 'U460', 'ELM284'], 'MS-ASSIGNMENT',
     'Supply Assignment conserve le vocabulaire FLOW d’affectation. Pegging est un terme produit de rapprochement offre–demande ; Allocation peut désigner d’autres droits ou protections.',
     'La préservation de liens pour une demande confirmée chez Microsoft éclaire le maintien d’une affectation. Son paramétrage ne prescrit ni le gel FLOW ni un blocage implicite.', ['V0-A02']),
card(14, 'PILOT-RESERVATION', 'Reservation', 'Réservation de ressources',
     'Quelle part de ressource est rendue indisponible aux demandes concurrentes, au bénéfice de qui ?',
     'Droit établi pour un besoin bénéficiaire sur une quantité de ressources définies par un périmètre, qui bloque les usages concurrents selon les conditions de réservation applicables.',
     'Périmètre de ressources suffisamment défini pour comprendre ce qui est réservé ; pas nécessairement un lot ou exemplaire déjà affecté.',
     ['Besoin bénéficiaire et périmètre de ressources concerné.', 'Quantité avec unité.', 'Conditions métier de l’opposabilité ; limites de durée seulement lorsqu’elles sont établies.'],
     'Quantité, périmètre et bénéficiaire forment le sens du droit. Un lot précis n’est pas indispensable à toute réservation ; son attribution répond à une autre question.',
     ['Réservation n’est ni mouvement physique ni simple affectation.', 'Expiration, libération, consommation et effets d’une annulation ne sont pas automatisés par la définition.'],
     [role('D02.c', 'établit et fait évoluer', 'Maintient le droit opposable selon les règles métier de réservation.', ['U436', 'U460']),
      role('D02.e', 'utilise', 'Tient compte des droits de réservation lors de l’application d’une affectation.', ['U436', 'U460'])],
     '40 pièces de V sur le périmètre P sont réservées au besoin L, sans lot choisi. Les demandes concurrentes doivent tenir compte de ce droit ; l’annulation de L ne prouve pas à elle seule une règle de libération automatique.',
     ['U436', 'U460', 'ELM283'], 'MS-RESERVATION',
     'Reservation est un terme établi ; FLOW conserve le nom de la capacité et précise son effet métier. Soft reservation est un mécanisme particulier, pas le nom imposé à toute réservation.',
     'Microsoft illustre la diminution de la quantité disponible à réserver sans mouvement de stock. La portée exclusive du blocage dans FLOW vient de U436 ; les options produit d’overselling ou de libération ne sont pas importées.', ['V0-A01', 'V0-A02', 'V0-A06']),
]

for number in (11, 12):
    cards[number - 1]['review']['adopted_scope'] = {
        'source_ref': 'U466',
        'meaning': 'Deux informations métier reliées ; une proposition peut être examinée pendant que l’engagement actuel reste valable.',
        'excluded': 'Noms anglais, rédaction des définitions, identités, versions, cardinalités et autorisations détaillées.'}


def support(id, refs, urls, observed, common, difference):
    return dict(id=id, source_refs=refs, sources=urls, relationship='semantic_or_methodological_support',
                observed=observed, common_ground=common, flow_difference=difference,
                status='comparison_proposed', author='Codex', as_of='2026-09-19')


def source(title, url, locator, consultation='2026-09-19', limit='Page officielle consultée ; synthèse sans reproduction du contenu.'):
    return dict(title=title, url=url, locator=locator, consulted_on=consultation, limit=limit)


supports = [
support('MS-PURCHASE', ['ELM242'], [source('Microsoft — Vendor collaboration with external vendors',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors',
    'Working with POs ; Confirmation and acceptance ; Changing a PO')],
    'La documentation distingue réponses du fournisseur, acceptation ou changements proposés et confirmation de commande. Une version confirmée peut subsister pendant le traitement d’un changement.',
    'Attendu, réponse et conditions retenues sont compréhensibles séparément.',
    'FLOW propose des informations conceptuelles ; aucun état ERP, mécanisme de confirmation automatique, règle de version ni autorité d’acceptation n’est importé.'),
support('MS-RECEIPT', ['ELM285', 'CMP178'], [source('Microsoft — Record the receipt of goods on the purchase order',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/tasks/record-receipt-goods-purchase-order',
    'Record receipt of goods, étapes 4–7 ; consultation U461, mise à jour indiquée le 1er juillet 2026',
    limit='Appui repris de ELM285/CMP178, consulté pendant U461 le même jour. Une tentative de réouverture U465 n’a pas abouti ; aucun constat nouveau.')],
    'L’exemple produit décrit un document identifié qui rend compte de la réception enregistrée.',
    'Illustre un constat de réception documenté et son rapprochement avec l’achat.',
    'Le lien obligatoire fait–document vient de U461. Les informations conceptuelles de prestation et de solde ne sont pas présentées comme des objets Microsoft identiques.'),
support('MS-PRODUCT', ['ELM280'], [source('Microsoft — Product information overview',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information',
    'Product definition ; Product masters and product variants ; page indiquée mise à jour le 1er juillet 2026')],
    'La documentation distingue produits, variantes, propriétés et identifiants ; les variantes se définissent selon des combinaisons de dimensions.',
    'Aide à distinguer référence concernée et caractéristiques utiles.',
    'Le produit Microsoft inclut l’administration de maîtres. Les référentiels Supply FLOW sont des projections ; leurs autorités externes ne sont pas attribuées ici.'),
support('GS1-IDENTITY', ['ELM282', 'ELM280'], [source('GS1 — Serialisation and unique identification',
    'https://support.gs1.org/support/solutions/articles/43000734238-how-does-serialisation-differ-from-unique-identification-in-the-gs1-system-',
    'FAQ, distinction GTIN et identification sérialisée ; modification indiquée le 28 août 2024',
    limit='FAQ officielle, pas lecture exhaustive des spécifications normatives GS1.')],
    'GS1 illustre l’identification d’une instance par l’association du GTIN et d’un numéro de série.',
    'Un identifiant de référence ne suffit pas toujours à identifier un exemplaire.',
    'Aucun format GS1 imposé aux références FLOW ni obligation de sérialisation de chaque unité.'),
support('FLOW-PROJECTION', ['U460', 'ELM269', 'ELM276', 'CMP183'], [source('TOGAF — Information Mapping, G190',
    'https://governance.foundation/assets/frameworks/togaf/g190%20-%20Information%20Mapping.pdf',
    'Chapitres 1–2 et 4–6 ; lecture U464',
    limit='Document primaire de 2019 sur miroir tiers, relu en U464 ; aucune vérification de toute la 10e édition ni de règle d’autorité locale.')],
    'La cartographie d’information relie concepts métier et capacités indépendamment des réalisations informatiques.',
    'Autorité et provenance rendent la projection intelligible pour ses capacités utilisatrices.',
    'Le découpage Reference Authority / Reference Receipt est une proposition FLOW motivée par les cas U460 ; aucun objet normalisé homonyme ni autorité Beaumanoir prouvée.'),
support('MARKET-PROMISE', ['ELM220', 'ELM248', 'U466'], [
    source('Microsoft — Delivery schedules', 'https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/delivery-schedules',
           'Delivery schedules ; répartition en plusieurs livraisons ; mise à jour indiquée le 7 mai 2025'),
    source('Oracle 26B — What’s a Split Order Line', 'https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/fauom/fulfillment-line-splits.html',
           'Introduction et éclatement selon ressources ou dates')],
    'Microsoft et Oracle documentent des répartitions d’une demande en quantités associées à des dates ou ressources différentes.',
    'Les associations quantité–date doivent conserver leur sens dans une proposition comme dans un engagement.',
    'Ces sources illustrent les échéances ; elles ne démontrent pas deux concepts universels Proposal/Commitment. La distinction est adoptée par U466, avec versions et confirmations encore ouvertes.'),
support('MS-ASSIGNMENT', ['ELM284'], [source('Microsoft — Keep supply for confirmed demand',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand',
    'What data is preserved ; Control how on-hand inventory is pegged ; documentation indiquée le 27 juillet 2026')],
    'Microsoft décrit le maintien de liens de couverture pour les demandes confirmées et un contrôle du pegging du stock disponible.',
    'Un lien ressource–demande peut être maintenu ou réexaminé lors de la planification.',
    'Le mécanisme produit recoupe plusieurs capacités FLOW. Il ne prouve ni équivalence complète avec Supply Assignment ni réservation par une affectation FLOW.'),
support('MS-RESERVATION', ['ELM283', 'U436'], [source('Microsoft — Inventory Visibility reservations',
    'https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations',
    'Introduction ; Sample use case')],
    'La réservation souple affecte la quantité disponible à réserver sans changer la quantité physique. Le service propose aussi des options de comportement.',
    'Le droit de réservation et le mouvement physique restent distincts.',
    'U436 définit l’opposabilité FLOW. Aucune option d’overselling, libération ou consommation Microsoft n’est adoptée ; le fonctionnement installé n’est pas évalué.'),
]


def link(n, start, end, meaning, condition, effect, refs, adopted=False):
    return dict(id=f'PILINK-{n:02d}', from_ref=f'PINFO-{start:03d}', to_ref=f'PINFO-{end:03d}',
                meaning=meaning, condition=condition, effect=effect, source_refs=refs,
                review='principle_adopted_U466_wording_proposed' if adopted else 'proposed')


links = [
link(1, 2, 1, 'répond à l’attendu d’achat', 'La réponse désigne l’attendu auquel elle se rapporte.', 'Rend l’écart demandé/proposé intelligible, sans modifier la demande.', ['U403', 'U460']),
link(2, 3, 2, 'retient des conditions issues d’une réponse fournisseur', 'Une acceptation selon les règles applicables est établie ; son autorité reste ouverte.', 'Distingue les conditions retenues de celles encore examinées ; aucune confirmation automatique.', ['U403', 'U460']),
link(3, 3, 1, 'précise les conditions acceptées pour l’attendu d’achat', 'Les deux informations concernent la même partie d’achat.', 'Permet de comparer demandé et engagé sans effacer la demande initiale.', ['U403', 'U460']),
link(4, 4, 1, 'rend compte d’une réalisation de l’attendu', 'Le résultat est rapproché de l’attendu ; le fait de gestion dispose de son document identifié.', 'Explique une réalisation partielle, complète ou un écart sans confondre engagement et fait.', ['U460', 'U461']),
link(5, 5, 1, 's’apprécie par rapport à l’attendu applicable', 'La situation de référence et les modifications autorisées sont connues.', 'Explique le restant ; aucune formule universelle déduite.', ['U391', 'U460']),
link(6, 5, 4, 'tient compte des réalisations reconnues', 'Les réalisations concernées sont qualifiées et rattachées au même attendu.', 'Le solde est expliqué par les faits retenus ; il n’est pas le dernier constat recopié.', ['U460', 'U461']),
link(7, 3, 12, 'peut alimenter le réexamen d’un engagement de satisfaction', 'Un lien métier entre cet achat et la demande promise est établi ; tous les achats ne sont pas dédiés.', 'Une réponse ou un changement fournisseur ne réécrit pas automatiquement la promesse.', ['U441', 'U460']),
link(8, 7, 6, 'décrit une caractéristique de la référence', 'Sujet et contexte d’application sont identifiés.', 'La valeur est interprétable sans assimiler toute la fiche produit à une information unique.', ['U460', 'U464']),
link(9, 8, 6, 'désigne la référence dans un système d’identification', 'Le système et le périmètre de l’identifiant sont connus.', 'Permet la reconnaissance de la référence sans désigner automatiquement une unité physique.', ['U460', 'ELM282']),
link(10, 9, 7, 'qualifie l’autorité sur un contenu de référence', 'Une autorité et sa portée sont effectivement établies ; elles peuvent rester inconnues.', 'Éclaire à quel titre une caractéristique fait référence ; n’attribue pas ce droit à l’émetteur par défaut.', ['U460']),
link(11, 10, 7, 'situe la réception d’un contenu de référence', 'Le contenu reçu et son émetteur sont identifiés.', 'Distingue date de réception et validité de la caractéristique ; aucune autorité déduite.', ['U460']),
link(12, 11, 12, 'peut donner lieu à un engagement de satisfaction', 'Les conditions proposées sont confirmées selon les règles métier applicables, encore à préciser.', 'L’engagement est distingué de la proposition ; ni réservation ni cardinalité un-à-un déduite.', ['U466', 'U436'], True),
link(13, 11, 12, 'peut proposer la révision d’un engagement existant', 'La proposition vise un engagement actuel ; la révision n’est pas encore confirmée.', 'L’engagement actuel peut rester valable pendant l’examen de la proposition.', ['U466'], True),
link(14, 13, 12, 'peut contribuer à honorer l’engagement', 'Ressource affectée et conditions promises sont compatibles ; leur rattachement à la demande est établi.', 'L’affectation peut changer à promesse constante ; un retard peut nécessiter une nouvelle proposition sans réaffectation.', ['U436', 'U443', 'U460']),
link(15, 14, 13, 'contraint l’utilisation des ressources lors de l’affectation', 'Les périmètres se recoupent ; le bénéficiaire et les droits concurrents sont connus.', 'La réservation bloque les usages concurrents ; l’affectation ne crée pas ce droit et n’est pas nécessairement déjà établie.', ['U436', 'U460']),
]

pilots = read(ROOT / 'modeles/backlog/information-pilots-U458.yaml')
case_refs = [[1,4,5], [1,2,3], [1,3,4,5], [6,8], [7,9,10], [7,10], [11,12], [12,13], [11,12,13], [13,14], [13,14], [13,14], [13,14], [14], [13,14]]
readings = [
    'Le constat documenté de 60 et le reste de 40 sont deux informations, rattachées au même attendu de 100.',
    'La réponse 60/40 reste distincte des conditions d’achat acceptées ; qui accepte reste ouvert.',
    'L’attendu peut décrire une prestation et son résultat ; les règles de reconnaissance de la prestation restent à préciser.',
    'L’identité de référence n’est pas multipliée par le nombre de catalogues ou de codes qui la désignent.',
    'Deux assertions contradictoires se décrivent avec leur origine ; la règle d’autorité n’est pas inventée.',
    'Réception récente et validité du contenu répondent à deux questions distinctes.',
    'La proposition est distincte de l’engagement ; U466 permet leur coexistence sans confirmation implicite.',
    'Un lien d’affectation peut évoluer à conditions promises constantes.',
    'Une nouvelle proposition peut viser l’engagement sans changement de la ressource affectée ; la règle de confirmation reste ouverte.',
    'Le lien d’affectation est connu, le droit opposable n’est pas établi par ce seul lien.',
    'Le gel qualifie le maintien de l’affectation ; seul le droit de réservation bloque la concurrence.',
    'Un nouveau plan propose d’autres affectations ; appliquer, maintenir ou libérer les droits existants demande des règles explicites.',
    'Le droit peut porter sur un périmètre de ressources avant le choix du lot.',
    'L’information explique l’échéance connue ; elle n’invente pas ce que produit son dépassement.',
    'La demande bénéficiaire annulée et ses droits doivent être rapprochés ; libération, consommation ou réaffectation ne sont pas déduites.'
]
coverage = []
for old, refs, reading in zip(pilots['review_U460']['cases'], case_refs, readings, strict=True):
    coverage.append(dict(case_ref=old['id'], pilot_ref=old['pilot'], title=old['title'],
                         information_refs=[f'PINFO-{n:03d}' for n in refs], reading=reading,
                         prior_status=old['status'], open_items=deepcopy(old['open_items']),
                         assessment='documentary_explanation_not_human_acceptance'))

extra = [
    dict(id='CASE-U465-01', information_refs=['PINFO-011','PINFO-012'],
         title='Révision proposée, engagement encore valable',
         example='100 vendredi reste engagé pendant l’examen d’une proposition 60 vendredi / 40 lundi.',
         expected_reading='Deux informations reliées ; l’existence de la proposition ne remplace pas l’engagement.', source_refs=['U466']),
    dict(id='CASE-U465-02', information_refs=['PINFO-007','PINFO-009','PINFO-010'],
         title='Émetteur intermédiaire et autorité distincts',
         example='Un distributeur transmet une caractéristique dont l’autorité déclarée est un autre rôle externe.',
         expected_reading='Transmission, autorité et validité ont des sens distincts. Le cas ne prouve aucune source installée.', source_refs=['U460']),
    dict(id='CASE-U465-03', information_refs=['PINFO-006','PINFO-008'],
         title='Référence partagée, exemplaires distincts',
         example='Dix exemplaires de la même variante portent le même identifiant de référence.',
         expected_reading='La correspondance à la référence ne suffit pas à identifier chacun des dix exemplaires.', source_refs=['U460','ELM282']),
    dict(id='CASE-U465-04', information_refs=['PINFO-011','PINFO-012'],
         title='Préserver les associations quantité–date',
         example='60 vendredi et 40 lundi ne signifient pas la même chose que 40 vendredi et 60 lundi.',
         expected_reading='Le lien quantité–date est indispensable ; cela ne prouve pas qu’un échéancier complet est un fait élémentaire unique.', source_refs=['U464','ELM220','ELM248']),
]

doc = dict(
    id='information-cards-U465', as_of='2026-09-19', status='pilot_proposals_with_bounded_U466_adoption',
    source_refs=['U464','U465','U466','U436','U460','U461','CMP183','CMP184'],
    scope='Cinq pilotes métier ; quatorze types d’information proposés pour éprouver la maille MOD012. Ces fiches ne constituent ni le catalogue exhaustif ni un modèle de données implémentable.',
    authority='Annexe YAML du backlog ; les identifiants PINFO/PILINK sont propres au pilote, sans insertion dans les nœuds ou relations canoniques.',
    review_boundary='U466 adopte seulement deux informations reliées, proposition et engagement de satisfaction, avec coexistence possible. Les rédactions, autres découpages, rôles et comparaisons restent proposés.',
    reading_rules=[
        'Lire la question métier avant les éléments essentiels ; ces derniers décrivent le sens, pas des colonnes obligatoires.',
        'Le minimum est relatif à la question et aux capacités. Il n’établit ni normalisation de données ni irréductibilité logique SBVR/ORM.',
        'Les liens décrivent une signification, ses conditions et son effet ; leur flèche n’est ni un flux technique ni une séquence imposée.',
        'Les rôles des capacités décrivent leur contribution ; aucun propriétaire exclusif, acteur installé ou architecture de composants n’est inféré.',
        'Objet, information, document et fait restent distincts. Les documents peuvent formaliser plusieurs informations ; tout fait de gestion a son document identifié U461.',
        'Les exemples sont illustratifs et contextualisés à partir des échanges ; aucune observation installée ni validation humaine des scénarios.',
    ],
    cards=cards, links=links, market_support=supports, case_coverage=coverage,
    additional_examples=extra,
    recommendation=dict(
        result='Les cinq pilotes permettent de distinguer des sens autonomes sans ajouter de niveau à Univers/Domaine/Capacité/Comportement.',
        next_step='Préparer le contrat minimal de catalogue et la lecture métier dans Atlas à partir de ces fiches : question, définition, contexte, liens, usages, exemples et marché. Conserver les règles non établies comme inconnues explicites, sans inventer de réalisation.',
        human_review='Faire relire les frontières et les mots par PO et experts ; cet exercice documentaire ne remplace pas leur revue.',
        open_business_rules=['V0-P02 : autorités des projections, conflits, fraîcheur par usage.', 'V0-P03 : acceptation fournisseur et confirmation/révision des engagements ; reconnaissance des prestations.', 'V0-A01/V0-A02/V0-A06 : coordination des affectations et droits, expiration, consommation et libération.'],
        excluded='Pas de généralisation à tout le modèle, schéma implémentable, réouverture de l’audit des comportements ou publication implicite.'),
)
write_text_if_changed(OUT, dumps(doc))

for pilot in pilots['pilots']:
    pilot['information_card_refs'] = [c['id'] for c in cards if c['pilot_ref'] == pilot['id']]
    pilot['refinement_U465'] = {
        'catalogue_ref': 'modeles/backlog/information-cards-U465.yaml',
        'status': 'proposed_granularity',
        'preservation': 'Les information_candidates antérieurs restent conservés comme matériau du pilote ; les fiches séparent leurs sens sans convertir les objets/documents en informations canoniques.'}
    if pilot['id'] == 'PILOT-COMMITMENT':
        pilot['source_refs'].append('U466')
        pilot['refinement_U465']['adopted_U466'] = doc['review_boundary']
pilots['source_refs'] = list(dict.fromkeys([*pilots['source_refs'], 'U465', 'U466']))
pilots['conventions']['established'].append('U466 : proposition et engagement de satisfaction sont deux informations métier reliées ; une proposition peut être examinée pendant que l’engagement actuel reste valable.')
pilots['conventions']['information_definition_proposal']['status'] = 'exercised_on_five_pilots_not_globally_adopted'
pilots['review_U465'] = dict(catalogue_ref='modeles/backlog/information-cards-U465.yaml',
    report='audits/2026-09-19-informations-pilotes-U465/rapport.md',
    qualification='Examen documentaire de la granularité ; aucun résultat de recette humaine.',
    adopted_scope=doc['review_boundary'],
    refinement_map={
        'PILOT-PURCHASE': 'Purchase Order reste un objet, Purchase Order Document et Receipt Document des documents. Ses attendus, réponses, engagements, réalisations et reste à réaliser portent cinq sens ; Receipt Fact reste associé à son document.',
        'PILOT-PRODUCT': 'Product Reference rassemble identité, caractéristiques et correspondances d’identifiants. Reference Origin distingue autorité et réception ; Reference Validity devient contexte d’application des contenus, distinct du moment de réception.',
        'PILOT-COMMITMENT': 'Le candidat réunissant proposé/confirmé est affiné en deux informations reliées conformément à U466.',
        'PILOT-ASSIGNMENT': 'Le candidat est précisé à la maille du lien ressource–demande, sans droit concurrent implicite.',
        'PILOT-RESERVATION': 'Le candidat est précisé à la maille du droit sur un périmètre de ressources pour un bénéficiaire, sans lot nécessaire.'})
write_text_if_changed(ROOT / 'modeles/backlog/information-pilots-U458.yaml', dumps(pilots))

meta = read(ROOT / 'modeles/backlog/modeling-glossary.yaml')
term = next(t for t in meta['terms'] if t['id'] == 'MOD012')
term['examples'].append('U466 : « 100 pièces vendredi » reste engagé pendant l’étude d’une proposition « 60 vendredi et 40 lundi ». Proposition et engagement de satisfaction sont deux informations métier reliées ; une nouvelle proposition ne remplace pas automatiquement l’engagement.')
term['source_refs'].extend(['U465','U466'])
term['pilot_catalogue_ref'] = 'modeles/backlog/information-cards-U465.yaml'
term['review']['adopted_scope_U466'] = 'Distinct de la définition générale encore proposée : proposition et engagement de satisfaction sont deux informations métier reliées, pouvant coexister.'
write_text_if_changed(ROOT / 'modeles/backlog/modeling-glossary.yaml', dumps(meta))

guide = read(ROOT / 'modeles/backlog/modeling-guide-U458.yaml')
guide_term = next(t for t in guide['glossary']['terms'] if t['id'] == 'MOD012')
guide_term['examples'] = deepcopy(term['examples'])
guide['source_refs'].append('U466')
guide['sources'].append(dict(id='U466', title='Distinguer proposition et engagement de satisfaction',
    excerpt='Deux informations métier reliées (recommandé)',
    scope='Réponse au choix entre deux informations reliées et une seule information à versions proposées/confirmées. Adopte la distinction et leur coexistence possible, sans valider les détails des fiches.'))
write_text_if_changed(ROOT / 'modeles/backlog/modeling-guide-U458.yaml', dumps(guide))

ready = read(ROOT / 'modeles/backlog/v0-readiness.yaml')
ready['source_refs'] = list(dict.fromkeys([*ready['source_refs'], 'U465','U466']))
execution = ready['execution_U458']
execution['follow_up_U465'] = dict(report='audits/2026-09-19-informations-pilotes-U465/rapport.md',
    catalogue='modeles/backlog/information-cards-U465.yaml',
    status='five_pilots_granularity_exercised_U466_distinction_adopted',
    remaining='Revue des autres découpages et préparation du contrat minimal ; règles métier encore inconnues conservées explicitement. Aucune publication des fiches.')
for lot in execution['lots']:
    if lot['lot'] == 3:
        lot['status'] = 'fourteen_information_cards_prepared_for_review'
        lot['remaining'] = 'Relecture PO/expert des quatorze fiches, quinze cas repris et quatre exemples supplémentaires. U466 adopte la seule distinction proposition/engagement ; autorités et règles détaillées restent ouvertes.'
    elif lot['lot'] == 4:
        lot['status'] = 'minimal_contract_prepared_by_pilot_annex_not_implemented'
        lot['remaining'] = 'Formaliser le contrat et la vue métier des informations à partir de l’annexe U465 ; aucun nouveau type de nœud ou mécanisme de publication encore implémenté.'
write_text_if_changed(ROOT / 'modeles/backlog/v0-readiness.yaml', dumps(ready))
print(f'{len(cards)} fiches, {len(links)} liens, {len(coverage)} cas repris, {len(extra)} exemples supplémentaires.')
