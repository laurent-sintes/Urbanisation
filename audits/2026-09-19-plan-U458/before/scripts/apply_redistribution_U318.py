"""Integrate the two redistribution mechanisms adopted in U318."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from scripts.structured_io import read, dumps
from scripts.lifecycle import value_hash
from scripts.record_tracking_U303 import append

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'audits/2026-09-18-redistribution-behaviors'


def main():
    assert not OUT.exists(), 'U318 already captured; do not replay.'
    assert '## U318\n' not in (ROOT/'connaissance/01-contributions-utilisateur.md').read_text(encoding='utf-8')
    OUT.mkdir()
    for name in ['model','behavior-gap-audit','d05-refactoring']:
        (OUT/f'{name}-before.yaml').write_bytes((ROOT/f'modeles/backlog/{name}.yaml').read_bytes())
    append('connaissance/01-contributions-utilisateur.md','''## U318

**id**

U318

**date**

2026-09-18

**titre**

Validation du rééquilibrage et de la consolidation sous Stock Redistribution Decision

**texte**

Je valide

**contexte et portée**

Accord sur les deux mécanismes présentés sous Stock Redistribution Decision : Rééquilibrage entre sites (« Déplacer du stock vers les lieux qui en ont davantage besoin, en préservant les besoins des donneurs. ») et Consolidation de stocks dispersés (« Regrouper des quantités fragmentées pour leur redonner une utilité ou libérer des sites. »). L’accord couvre les deux cas explicitement soumis : reconstituer des assortiments de tailles dans certains magasins et regrouper les reliquats vers des lieux de destination adaptés. La redistribution ne se limite pas aux pénuries ; la consolidation ne se limite pas aux excédents. Coûts et risques du transfert sont à confronter au bénéfice. Les noms anglais, descriptions détaillées et nouvelle synthèse de capacité rédigés lors de l’intégration restent éditoriaux ; aucune équivalence marché ni pratique installée Beaumanoir déduite. Mise à jour du backlog autorisée ; aucune release demandée.''')
    path=ROOT/'modeles/backlog/model.yaml'; m=read(path); before=deepcopy(m)
    assert not {'BHV024','BHV025'} & {n['id'] for n in m['nodes']}
    parent=next(n for n in m['nodes'] if n['id']=='D05.c')
    now=datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
    def cycle(values, fields, note):
        return dict(state='urbanist_validated',recorded_at=now,recorded_by='Codex',source_refs=['U318'],
            validated_fields=fields,value_sha256={k:value_hash(values[k]) for k in fields},note=note)
    position='U318 adopte deux comportements sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation de stocks dispersés, avec reconstitution d’assortiments de tailles et regroupement des reliquats. Les formulations anglaises Inventory Rebalancing et Stock Consolidation sont éditoriales ; les correspondances produit restent proposées. FLOW décide les transferts intersites ; D04 gère les Orders et D06 l’exécution.'
    for c in parent['fields']['market_comparisons']:
        c['flow_position']=position
        c['source_refs']=list(dict.fromkeys(c['source_refs']+['U318']))
        if c['vendor']=='Nextail':
            c['differences']='Le témoignage documente le bénéfice de consolidation des tailles, pas les règles de calcul ni une taxonomie de comportements. FLOW réunit, selon U318, reconstitution d’assortiments et regroupement des reliquats sous un même mécanisme de consolidation intersites, tout en conservant leurs cas et critères distincts.'
    records=[
      ('BHV024','Inventory Rebalancing','Rééquilibrage entre sites',
       'Déplacer du stock vers les lieux qui en ont davantage besoin, en préservant les besoins des donneurs.',
       '''Mécanisme de décision de transferts intersites : comparer les besoins connus ou prévus, le stock admissible et les apports déjà engagés pour déterminer les quantités, origines, destinations et dates à retenir. Le résultat est une recommandation de redistribution ; le verbe déplacer dans la définition exprime l’effet recherché, pas la réalisation physique par D05.

Préserver les besoins et engagements du site donneur. Le bénéfice peut être de prévenir une rupture, de mieux couvrir une demande prévue ou d’améliorer l’utilisation du stock selon les objectifs retenus ; il n’exige pas une pénurie déjà constatée. Mettre ce bénéfice en regard des coûts, délais et risques, sans imposer une pondération unique.

Exemple fictif : transférer 20 pièces d’un magasin peu demandeur vers un magasin dont les ventes risquent d’épuiser le stock, après vérification que le donneur reste correctement couvert. Si le délai rend le transfert inutile ou son coût disproportionné, retenir une autre réponse ou expliciter l’absence de transfert pertinent.

Coordonner les résultats avec Initial Stocking Decision et Replenishment Decision sans couvrir deux fois le même besoin. D04 gère les Transfer Orders et D06 pilote les prestations. D03 conserve la satisfaction des Orders ; ce comportement vise la répartition du stock, sans affecter à lui seul des ressources à des commandes.''',
       ['Oracle','Nextail']),
      ('BHV025','Stock Consolidation','Consolidation de stocks dispersés',
       'Regrouper des quantités fragmentées pour leur redonner une utilité ou libérer des sites.',
       '''Mécanisme de décision de regroupement intersites : choisir les stocks à réunir, les lieux destinataires, les quantités et les dates selon le bénéfice attendu de leur concentration. Le résultat est une recommandation de transferts, pas une manutention interne d’entrepôt.

Deux cas sont retenus U318. Reconstituer des assortiments de tailles dans certains magasins peut rendre un ensemble de pièces plus utile commercialement que des tailles isolées sur plusieurs sites. Regrouper les reliquats vers des lieux adaptés peut libérer les sites donneurs et préparer une utilisation ultérieure, même sans manque immédiat à destination. Ces cas partagent le mécanisme de concentration mais gardent des critères et résultats distincts ; aucun sous-comportement n’est créé.

Exemples fictifs : réunir des tailles dispersées d’un même modèle dans un magasin où l’assortiment ainsi reconstitué répond aux besoins ; regrouper les reliquats de plusieurs magasins dans un lieu retenu pour leur réemploi. Une fragmentation n’implique pas que chaque quantité soit excédentaire : protéger les besoins locaux et comparer bénéfice, coûts, délais et risques de la concentration.

Le choix d’assortiment commercial reste une entrée ou une contrainte ; la consolidation ne redéfinit pas à elle seule la collection ou la gamme. Ni liquidation commerciale, ni destruction, ni fixation de prix ne sont ajoutées. D04 porte les Orders et D06 les prestations. La consolidation physique de palettes ou d’emplacements dans SAP EWM relève d’un autre périmètre.''',
       ['Oracle','Nextail','SAP'])]
    adopted=[]
    for identifier,name,label,definition,scope,vendors in records:
        fields=dict(name=name,definition=definition,scope=scope,
            market_comparisons=deepcopy([c for c in parent['fields']['market_comparisons'] if c['vendor'] in vendors]))
        note='Définition française et principe du comportement adoptés U318. Nom anglais, périmètre détaillé et comparaisons éditoriaux proposés ; rattachement adopté séparément.'
        n=dict(id=identifier,revision=1,kind='behavior',layer='transactional',fields=fields,
            source_refs=['U317','U318','ELM201','CMP109'],source_locator={'path':'connaissance/01-contributions-utilisateur.md','anchor':'u318'},
            review={'state':'partial','note':note},adoption_ids=[],editorial_basis=note)
        n['lifecycle']=cycle(fields,['definition'],note)
        m['nodes'].append(n)
        r=dict(id='REL-BEHAVIOR-'+identifier,revision=1,type='contains',source_id='D05.c',target_id=identifier,
            source_refs=['U318'],review={'state':'accepted','note':'Les deux comportements ont été présentés directement sous Stock Redistribution Decision et adoptés U318.'})
        r['lifecycle']=cycle(r,['type','source_id','target_id'],r['review']['note'])
        m['relations'].append(r)
        adopted.append(dict(node_id=identifier,label_fr=label,label_fr_sha256=value_hash(label),
            adopted_fields=['definition'],value_sha256=n['lifecycle']['value_sha256'],editorial_name=name,
            parent_id='D05.c',relation_id=r['id']))
    parent['revision']+=1
    parent['fields']['definition']='Déterminer les transferts de stock existant entre sites pour mieux répondre aux besoins, reconstituer des assortiments utiles ou regrouper des stocks dispersés, en tenant compte des coûts et risques.'
    parent['fields']['scope']+='''

U318 : [Inventory Rebalancing](model:BHV024) déplace le stock vers les lieux qui en ont davantage besoin, en préservant les donneurs ; [Stock Consolidation](model:BHV025) concentre des stocks dispersés pour reconstituer des assortiments de tailles ou regrouper des reliquats vers des lieux adaptés. Les deux mécanismes peuvent se combiner, sans séquence imposée ni niveau inférieur. La consolidation n’exige pas un manque immédiat à destination et ne concerne pas exclusivement des excédents. Ces exemples décrivent la cible, pas une pratique Beaumanoir démontrée.

La valeur recherchée intègre disponibilité, immobilisation et risque. Les coûts et contraintes de transfert peuvent conduire à ne rien déplacer. [Initial Stocking Decision](model:D05.g) et Replenishment Decision restent les décisions d’apports de lancement et d’apports continus ; coordonner leurs résultats avec la redistribution du stock existant.'''
    parent['fields']['decomposition_rationale']='Distinguer deux mécanismes aux bénéfices différents : améliorer la couverture des lieux receveurs en préservant les donneurs, ou réduire la fragmentation du stock par concentration, avec reconstitution d’assortiments ou regroupement de reliquats même sans manque immédiat à destination.'
    parent['source_refs']+=['U317','U318','CMP109']
    parent['review']['note']='Deux comportements et cas de consolidation adoptés U318. Nouvelle définition de synthèse, justification rédigée et compléments éditoriaux proposés ; nom de capacité conservé. Définition antérieure et empreinte dans la capture pré-U318.'
    parent['lifecycle']['validated_fields']=['name']
    parent['lifecycle']['value_sha256']={'name':value_hash(parent['fields']['name'])}
    parent['lifecycle']['note']=parent['review']['note']
    parent['lifecycle']['source_refs'].append('U318')
    parent['editorial_basis']+=' U318 : capture de la définition antérieure dans audits/2026-09-18-redistribution-behaviors/model-before.yaml ; aucune validation héritée sur la nouvelle synthèse.'
    path.write_text(dumps(m),encoding='utf-8')
    delta={}
    for collection in ['nodes','relations']:
        old={x['id']:x for x in before[collection]}; new={x['id']:x for x in m[collection]}
        delta[collection]=dict(added={i:value_hash(new[i]) for i in sorted(new.keys()-old.keys())},
            changed={i:value_hash(new[i]) for i in sorted(old.keys()&new.keys()) if old[i]!=new[i]},removed=sorted(old.keys()-new.keys()))
    registry=dict(source_refs=['U318'],state='applied_in_backlog',model_before='audits/2026-09-18-redistribution-behaviors/model-before.yaml',
        model_before_sha256=sha256((OUT/'model-before.yaml').read_bytes()).hexdigest(),model_after_sha256=sha256(path.read_bytes()).hexdigest(),
        delta=delta,behaviors=adopted,adopted_cases=['Reconstituer des assortiments de tailles dans certains magasins.','Regrouper les reliquats vers des lieux de destination adaptés.'],
        validation_scope='Deux mécanismes, définitions présentées et parents adoptés ; noms anglais et détails éditoriaux proposés. Comparaisons marché non validées par adoption du modèle.',
        previous_candidates={'P06':'BHV024 — élargi au-delà de la pénurie constatée','P07':'BHV025 — élargi au-delà des seuls excédents'})
    ap=ROOT/'modeles/backlog/behavior-gap-audit.yaml'; a=read(ap)
    a['implementation_U318']=registry
    a['baseline'].update(sha256=registry['model_after_sha256'],nodes=len(m['nodes']),behaviors=16,relations=len(m['relations']))
    for p in a['candidates']:
        if p['id'] in ['P06','P07']:
            p['status']='implemented_U318'
            p['implemented_as']='BHV024' if p['id']=='P06' else 'BHV025'
            p['review_note']='U318 : mécanisme adopté dans la portée U317 et intégré ; définition initiale ci-dessus conservée comme historique. Lire le comportement courant et sa qualification champ par champ.'
    synth=a['current_synthesis_U298']
    synth['retained_candidate_ids']=[i for i in synth['retained_candidate_ids'] if i not in ['P06','P07']]
    synth['implemented_candidate_ids']=['P06','P07']
    synth['retained_scope']='Cinq candidats restent à instruire ; P06/P07 sont intégrés avec le périmètre révisé U318. Les autres accords et réserves gardent leurs portées.'
    synth['unchanged_basis']='Socle historique U290 ; mises à jour documentées U316 (Initial Stocking) et U318 (redistribution). Le catalogue courant comporte 40 capacités et 16 comportements.'
    synth['next_step']='P01–P03 sur le réassort restent à réexaminer ; poursuivre ensuite les autres mécanismes et frontières ouverts sans décomposition systématique.'
    assessment=next(x for x in a['assessments'] if x['capability_id']=='D05.c')
    assessment.update(existing_behaviors=['BHV024','BHV025'],candidate_ids=[],verdict='deux mécanismes intégrés U318',
        diagnosis='Rééquilibrage et consolidation intersites adoptés ; cette dernière couvre assortiments de tailles et reliquats.',
        recommendation='Éprouver les critères de bénéfice, coûts, protection du donneur et disponibilité à destination. Ne pas créer un troisième niveau ni réduire la consolidation aux excédents.')
    a['existing_behavior_review'] += [dict(behavior_id=x['node_id'],recommendation='Mécanisme et définition française adoptés U318 ; nom anglais et contrats détaillés proposés. '+('Préserver les besoins du donneur et comparer coûts/risques.' if x['node_id']=='BHV024' else 'Distinguer les deux cas validés sans sous-comportement ni confusion avec la consolidation interne EWM.'),market_sources=['S12'],status='adopted_scope_editorial_details_proposed') for x in adopted]
    a['feedback_U317']['superseded_by']='U318 adopte les deux mécanismes et les deux cas de consolidation ; noms anglais éditoriaux.'
    ap.write_text(dumps(a),encoding='utf-8')
    dp=ROOT/'modeles/backlog/d05-refactoring.yaml'; d=read(dp); d['redistribution_U318']=registry; dp.write_text(dumps(d),encoding='utf-8')
    (OUT/'implementation.yaml').write_text(dumps(registry),encoding='utf-8')
    append('marche/comparaisons.md','''Complément U318 à CMP109 — 18 septembre 2026 : deux mécanismes adoptés sous D05.c et intégrés comme BHV024/BHV025. Le rééquilibrage préserve les besoins des donneurs ; la consolidation couvre assortiments de tailles et regroupement de reliquats, au-delà des seuls excédents. Inventory Rebalancing et Stock Consolidation sont des libellés anglais éditoriaux appuyés sur les usages documentés ; le second est explicitement intersites, sans assimilation au Stock Consolidation interne SAP EWM. Comparaisons sur le parent et chaque comportement ; sources consultées U317 toujours applicables. Les équivalences marché restent proposées.''')
    append('JOURNAL.md','''### 2026-09-18 — U318, comportements de redistribution

Deux comportements ajoutés sous Stock Redistribution Decision : rééquilibrage entre sites et consolidation des stocks dispersés. Définitions françaises et parents adoptés ; noms anglais éditoriaux, détails et correspondances proposés. Assortiments de tailles et regroupement des reliquats conservés dans un même comportement sans niveau supplémentaire. Justification de décomposition, audit et comparaisons mis à jour. Aucune release. Capture : audits/2026-09-18-redistribution-behaviors/.''')
    print('U318 intégré : 40 capacités, 16 comportements ; 2 relations contains ajoutées.')


if __name__=='__main__':
    main()
