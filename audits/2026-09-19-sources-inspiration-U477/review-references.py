from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.structured_io import read, dumps, write_text_if_changed
from scripts.market_comparison import validate_comparisons, validate_inspiration

root=Path(__file__).parent
path=root/'references-output.yaml'
data=read(path)
rows={x['id']:x for k in ('nodes','terms') for x in data[k]}
changes=[]

def rename(id,old,new,why):
    row=rows[id]
    c=next(c for c in row['market_comparisons'] if c['concept_name']==old)
    c['concept_name']=new
    c['element_name']=new
    changes.append(dict(id=id,field='market_comparisons/concept_name + element_name',before=old,after=new,reason=why,source_url=c['source_url']))
    trace='Relecture indépendante U477 : intitulé rapproché du vocabulaire effectivement présent dans la source ; périmètre et responsabilités inchangés.'
    if trace not in row.get('editorial_notes',''):
        row['editorial_notes']=(row.get('editorial_notes','')+' '+trace).strip()

rename('D08.d','Product master data exchange','Product master data','Le titre de rubrique et le texte Microsoft nomment les données produit ; exchange décrivait ici l’approche.')
rename('D13.a','Site and warehouse reference data','Site / Warehouse','Microsoft nomme sites et warehouses ; le reste était une description reconstruite du référentiel.')
rename('D07.a','Work order requirements','Work Order / Resource Requirement','Deux notions nommées explicitement dans Work order architecture.')
rename('D14.a','Service catalog lifecycle','Service Catalog','La notice TMF633 distingue le catalogue et le cycle qui lui est appliqué.')
rename('D14.a','Catalog service / Work order service','Product Catalog / Work Order','Les intitulés sont présents dans la page Microsoft ; les prestations sont leur contenu décrit.')
rename('D06.f','Orchestration policies and flows','Orchestration','Nom de la rubrique Microsoft ; les politiques et parcours restent décrits dans l’approche.')
rename('BHV079','Warehouse progress feedback','Progress data and business events','Nom de rubrique Microsoft pour les retours de progression.')
rename('TER050','Reference data exchange','Master and reference data','Nom de rubrique Microsoft, qui contient les références reçues.')
rename('TER054','Fulfillment network across partners','Fulfillment network','Le réseau est nommé ainsi chez Microsoft ; across partners décrivait son utilisation.')

for id in ('D14','D14.a'):
    row=rows[id]
    for container in (row['market_comparisons'],row['market_inspiration']['examples']):
        for record in container:
            if 'tmf633-service-catalog-api-rest-specification-r18-5-0' in record['source_url']:
                old=record['source_title']
                record['source_title']='TMF633 Service Catalog API REST Specification R18.5.1'
                if 'source_version' in record:
                    record['source_version']='Archive R18.5.1 ; notice version 4.0.1, modifiée le 8 avril 2019'
                changes.append(dict(id=id,field='source_title / source_version',before=old,after=record['source_title'],reason='Titre et métadonnées de la notice primaire effectivement lus ; son URL historique reste en r18-5-0.',source_url=record['source_url']))

errors=[]
for row in rows.values():
    errors+=validate_comparisons(row['market_comparisons'],row['id'])
    errors+=validate_inspiration(row['market_inspiration'],row['market_comparisons'],row['id'])
assert not errors,errors
write_text_if_changed(path,dumps(data))
write_text_if_changed(root/'references-review.yaml',dumps(dict(source='U477',reviewer='source_science',date='2026-09-19',scope='Lecture éditoriale des 58 choix, synthèses, lignes comparatives et exemples ; vérification documentaire ciblée des noms et passages à risque.',checked_count=len(rows),contract_errors=errors,changes=changes,findings=[dict(result='Aucun écart de responsabilité repéré',detail='Maîtres externes, autorisation distincte du mouvement, décision distincte de l’application, services documentaires et limites du catalogue sont préservés.'),dict(result='Portée des sources visible',detail='TMF633 reste une notice consultée et non une prétendue lecture du corps ; les pages GS1 bloquées restent qualifiées par leur consultation indexée.'),dict(result='Rapprochements partiels explicites',detail='Pour réseau, ingestion et SLA, les sources éclairent les notions et leurs différences sans prétendre fournir une capacité FLOW équivalente.')],document_checks=[dict(url='https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/wms-only-mode-exchange-data',passages='Master and reference data ; Inbound and outbound shipment order messages ; Progress data and business events'),dict(url='https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview',passages='Components ; Orchestration'),dict(url='https://camunda.com/process-orchestration/',passages='What is process orchestration ; Processes with complex logic, dont Exception handling'),dict(url='https://learn.microsoft.com/en-us/dynamics365/field-service/field-service-architecture',passages='Created ; Scheduled to resources ; Performed by field technicians'),dict(url='https://www.tmforum.org/resources/specification/tmf633-service-catalog-api-rest-specification-r18-5-0/',passages='Notice primaire indexée, titre, description et General Information'),dict(url='https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/Historic/TMF641_Service_Ordering/3.0.0/user_guides/TMF641_Service_Ordering_Management_API_user_guides_18.5.1.pdf',passages='Introduction p.5 ; ServiceOrderRelationship et dépendances p.12 ; dates de commande'),dict(url='https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard',passages='Texte primaire indexé : §3.1 CTE ; §3.5 scénarios ; tableau de partage Despatch Advice/Receiving Advice')],follow_up='Reporter le titre documentaire TMF633 R18.5.1 dans le registre de sources parent. Aucun autre fichier de lot ni builder parent modifié.')))
print(f'REFERENCES: {len(rows)} entries reviewed; {len(changes)} targeted corrections; actual validators: 0 errors')
