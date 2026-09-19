"""Correct the interpretation: business legibility, not functional coverage."""
from hashlib import sha256
from scripts.apply_supplier_return_U387 import ROOT, save, append
from scripts.structured_io import read


def main():
    out=ROOT/'audits/2026-09-18-business-visibility-U394'
    assert not out.exists()
    out.mkdir()
    p='modeles/backlog/order-intent-principles.yaml'
    (out/'order-intent-principles-before.yaml').write_bytes((ROOT/p).read_bytes())
    (out/'AGENTS-before.md').write_bytes((ROOT/'AGENTS.md').read_bytes())
    model=ROOT/'modeles/backlog/model.yaml'; before=sha256(model.read_bytes()).hexdigest()
    append('connaissance/01-contributions-utilisateur.md','''## U394

**id**

U394

**date**

2026-09-18

**titre**

Clarifier le critère de visibilité du métier au travers du design

**texte**

Je ne dis pas que SAP ne sait pas gérer le consignment, je dis que cet aspect n'est pas très visible dans le modèle. C'est d'ailleurs un reproche qu'on lui fait : on ne voit pas le processus dans les données et les transactions. Donc mon opinion est que microsoft, arrivé après a corrigé ce pb de design et de "visibilité du métier au travers du design"

**contexte et portée**

Correction de l’interprétation de Codex : Laurent compare la lisibilité des intentions et processus dans les objets, données et transactions, pas la présence des fonctions de consignation. Sa préférence Microsoft est une appréciation de design métier. L’hypothèse selon laquelle son arrivée ultérieure lui a permis de corriger intentionnellement SAP est conservée comme opinion historique, sans la transformer en fait établi. Critère à appliquer aux choix FLOW ; aucun nouveau nom ni élément de catalogue adopté.''')
    append('connaissance/04-corrections.md','''## C103

**id**

C103

**sources**

U394

**constat**

La réponse à U393 répondait à la préférence architecturale de Laurent en rappelant la couverture fonctionnelle SAP et sa capacité à piloter selon les besoins. Elle déplaçait ainsi le débat vers « savoir faire » au lieu de « rendre le métier visible dans le design ».

**correction**

Ne plus attribuer à Laurent une contestation de la capacité SAP à gérer la consignation. Son critère est la lisibilité du processus, des intentions et des engagements à travers objets, données, transactions et liens. Microsoft rend explicitement distincts apport en consignation et acquisition par ses objets ; SAP conserve ces distinctions dans une catégorie et des effets d’un document commun. L’appréciation de meilleure lisibilité Microsoft sur cet exemple est argumentée ; l’explication historique de cette différence reste une opinion non vérifiée. Appliquer ce critère à FLOW, indépendamment de la couverture fonctionnelle et sans imposer une table physique par intention.''')
    clarification=dict(source_refs=['U394','C103'],criterion='Visibilité du métier au travers du design',rule='Rendre identifiables dans les concepts, noms, relations, états et événements l’intention de la demande, les parties, leurs engagements et la progression métier. Ne pas obliger à reconstruire le sens du processus à partir des seules transactions ou d’un paramétrage implicite.',distinction='Évaluer la lisibilité sémantique séparément de la couverture fonctionnelle ; savoir exécuter un processus ne prouve pas que son sens est visible dans le modèle.',application=['Pouvoir distinguer une demande d’apport en consignation d’un engagement d’achat et relier leur évolution éventuelle.', 'Montrer le lien entre intention, accord, demande, exécution et résultat, sans confondre modèle métier et schéma physique.', 'Une réalisation commune est possible si elle conserve ces intentions explicites ; une table par intention ou la multiplication des objets ne sont pas des exigences.'],market_judgment='Préférence Microsoft sur la lisibilité des intentions d’apport et d’acquisition dans le cas étudié ; pas un déni de couverture SAP.',historical_opinion='Laurent estime que Microsoft, arrivé après, a corrigé cette faiblesse de design. La causalité et l’intention historique ne sont pas établies par les documentations fonctionnelles consultées.')
    for rel in [p,'modeles/backlog/consignment-inventory-review.yaml','modeles/backlog/nonpurchase-supply-order-review.yaml']:
        d=read(ROOT/rel)
        d['source_refs']=list(dict.fromkeys(d['source_refs']+['U394','C103']))
        d['business_visibility_U394']=clarification
        for c in d.get('market_comparisons',[]):
            if c.get('comparison_ref')=='CMP149':
                c['difference']='U394 précise le critère : les intentions apport/acquisition sont plus directement identifiables dans les objets Microsoft du cas étudié ; SAP les distingue au sein d’un document commun. La comparaison porte sur la lisibilité métier, indépendamment de la couverture fonctionnelle.'
                c['flow_position']='Priorité à la visibilité du métier dans le design FLOW : intentions, parties, engagements, progression et résultats explicites. Préférence locale Microsoft argumentée ; causalité historique non démontrée.'
        if rel==p:
            d['review']['adopted_scope']+=' U394 précise que le critère porte sur la visibilité du métier dans le design, pas sur la couverture fonctionnelle SAP.'
            d['analysis_grid'].append('L’intention et la progression métier se lisent-elles dans les concepts et leurs liens sans reconstituer le processus depuis les transactions ?')
        save(rel,d)
    agents=ROOT/'AGENTS.md';text=agents.read_text(encoding='utf-8')
    old='- **Demandes par intention (U393)** :'
    assert old in text
    text=text.replace(old,'- **Demandes par intention et lisibilité métier (U393/U394)** :',1)
    needle='Les documents ERP et mouvements ne dictent pas le découpage métier.'
    text=text.replace(needle,needle+' Rendre intentions, relations, engagements et progression métier lisibles dans les concepts et leurs liens ; évaluer cette lisibilité séparément de la couverture fonctionnelle. La préférence Microsoft discutée concerne ce critère, pas une incapacité SAP à gérer la consignation (C103).',1)
    agents.write_text(text,encoding='utf-8')
    append('marche/elements.md','''### Relecture ELM238 — U394

18 septembre 2026 : Microsoft Set up consignment et SAP Learning Exploring the Supplier Consignment (2LG) Scenario ouverts de nouveau, mêmes URL que OI-S1/OI-S2 dans order-intent-principles.yaml. Les passages décrivent respectivement une demande d’apport distincte du Purchase Order et une catégorie de ligne Consignment au sein du Purchase Order. Ils permettent de comparer la représentation explicite des intentions ; ils ne prouvent ni incapacité fonctionnelle SAP ni causalité historique de la conception Microsoft.''')
    append('marche/comparaisons.md','''### Clarification CMP149 — U394 / C103

Le critère de Laurent est la visibilité du métier dans les objets, données et transactions. Le rappel de la couverture SAP en réponse à U393 était hors du point discuté. La séparation Microsoft donne, sur le cas étudié, une expression plus directe des intentions apport/acquisition ; c’est une appréciation architecturale argumentée par ELM238, pas une preuve de fonction absente chez SAP. FLOW retient ce critère explicite de design. L’opinion « Microsoft, arrivé après, a corrigé le problème » est conservée comme telle, sans causalité historique documentée.''')
    append('JOURNAL.md','''## 2026-09-18 — U394 : visibilité métier du design

C103 corrige le déplacement du débat vers la couverture fonctionnelle SAP. Principe et annexes précisent la lisibilité des intentions/processus dans les concepts et liens ; AGENTS.md actualisé. ELM238 reconsulté et CMP149 précisé. Opinion historique distinguée du constat de représentation ; catalogue métier inchangé.''')
    assert sha256(model.read_bytes()).hexdigest()==before
    (out/'README.md').write_text('# U394 — correction de lecture\n\nC103 distingue lisibilité métier et couverture fonctionnelle. Instructions et annexes actualisées ; état précédent conservé ici. Catalogue métier inchangé : `'+before+'`.\n',encoding='utf-8')
    print('U394/C103 recorded; business catalog unchanged.')


if __name__=='__main__':
    main()
