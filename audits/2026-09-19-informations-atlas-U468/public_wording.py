"""Public wording only; internal evidence and pilot captures are preserved."""
from pathlib import Path
import sys, re
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.structured_io import read, dumps, write_text_if_changed
p = ROOT/'modeles/backlog/model.yaml'
m = read(p)
replacements = {
 'Aucun fait de gestion nouveau n’est qualifié par cette fiche. Le lien U461 s’applique dès qu’un fait de gestion est décrit ; il n’exige pas un document propre à chaque propriété.': 'Cette information n’est pas, à elle seule, un fait de gestion. Tout fait de gestion s’appuie sur un document métier identifié ; chaque propriété descriptive n’exige pas son propre document.',
 'Le résultat rend compte d’un fait de gestion. U461 impose un document identifié ; son auteur, le nombre exact de documents, les corrections et les preuves d’acceptation ne sont pas inventés.': 'Le résultat rend compte d’un fait de gestion et s’appuie sur un document métier identifié. Les modalités d’attestation et de correction dépendent du métier concerné.',
 'Une propriété n’exige pas un document distinct au titre de U461.': 'Une propriété descriptive n’exige pas un document métier distinct.',
 'La fiche décrit le contexte de provenance. Si l’arrivée est également modélisée comme fait de gestion, U461 exige son document identifié ; ce classement et ce document ne sont pas inventés ici.': 'Cette information décrit le contexte de provenance. Une arrivée décrite comme fait de gestion s’appuie en complément sur un document métier identifié.',
 'des sens et effets distincts, adoptés U466': 'des sens et effets distincts',
 'une proposition FLOW motivée par les cas U460 ; aucun objet normalisé homonyme ni autorité Beaumanoir prouvée': 'un choix de description FLOW : recevoir une information ne suffit pas à faire autorité sur elle. Les sources ne définissent pas d’objet normalisé homonyme ni les autorités propres à l’entreprise',
 'La distinction est adoptée par U466, avec versions et confirmations encore ouvertes.': 'FLOW distingue ces deux sens pour permettre d’étudier une proposition pendant que l’engagement actuel reste valable.',
 'U436 définit l’opposabilité FLOW. Aucune option d’overselling, libération ou consommation Microsoft n’est adoptée ; le fonctionnement installé n’est pas évalué.': 'Dans FLOW, seule la réservation bloque les usages concurrents. Les options d’overselling, de libération et de consommation du produit ne définissent pas les règles métier de l’entreprise.',
 'descriptif proposé pour': 'descriptif pour',
 ' U466 ne valide pas cette séparation côté achats par extension.': '',
 'reprend le candidat existant en précisant ici « accepté »': 'explicite les conditions acceptées par les parties',
 'L’engagement conceptuel proposé': 'L’engagement conceptuel',
 'est proposé pour couvrir': 'couvre',
 'Le lien obligatoire fait–document vient de U461': 'FLOW rattache tout fait de gestion à un document métier identifié',
 ' ; consultation U461, mise à jour': ' ; mise à jour',
 'Appui repris de ELM285/CMP178, consulté pendant U461 le même jour. Une tentative de réouverture U465 n’a pas abouti ; aucun constat nouveau.': 'Exemple de réception de biens dans un produit ; la source ne définit pas une norme générale pour les prestations.',
 'est descriptif et proposé': 'est un libellé descriptif',
 'formulation descriptive proposée': 'formulation descriptive',
 'par la convention FLOW de projection et par V0-P02': 'par la convention FLOW de projection et par le besoin de distinguer qui fait autorité de qui reçoit l’information',
 ' ; lecture U464': '',
 'Document primaire de 2019 sur miroir tiers, relu en U464': 'Document primaire de 2019 disponible sur un miroir tiers',
 'est proposé en cohérence avec Fulfillment Commitment et Promise Proposal BHV021': 'est cohérent avec Fulfillment Commitment et le comportement Promise Proposal',
 ' ; U466 fonde la séparation des deux informations': ' ; FLOW distingue la proposition de l’engagement afin de permettre leur coexistence pendant une révision',
 'reprend le nom adopté de la capacité U445': 'reprend le nom de la capacité',
 'est la convention U436': 'est une convention FLOW',
 'dans FLOW vient de U436': 'est une convention FLOW',
}
def transform(x):
    if isinstance(x, dict):
        return {k: v if k in ('source_refs','review') else transform(v) for k,v in x.items()}
    if isinstance(x, list): return [transform(v) for v in x]
    if isinstance(x, str):
        for a,b in replacements.items(): x=x.replace(a,b)
    return x
m['information_catalog'] = transform(m['information_catalog'])
write_text_if_changed(p, dumps(m))
def inspect(x, path=''):
    if isinstance(x,dict):
        for k,v in x.items():
            if k not in ('source_refs','review'): inspect(v,path+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): inspect(v,path+'/'+str(i))
    elif isinstance(x,str) and re.search(r'U\d{3}|V0-|ELM\d|adopt|candidat',x): print(path, ':', x)
sys.stdout.reconfigure(encoding='utf-8')
inspect(m['information_catalog'])
