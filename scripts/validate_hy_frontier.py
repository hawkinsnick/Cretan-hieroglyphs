"""Replay bounded CH discovery routes without certifying readings or modern holdings."""
import argparse,collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUTS=['research/hy-primary-concordance-2026-10-13.json','research/inscribe-discovery-dispositions-2026-10-13.json','research/dbas-chs-catalogue-leads.json','corpus/chic-catalogue-spine.json','corpus/critical-readings.json','research/inscribe-unmapped-discovery.json']
def load(root,p):return json.loads((root/p).read_text())
def require(ok,msg):
 if not ok:raise ValueError(msg)
def validate(root=ROOT):
 data=load(root,INPUTS[0]);discovery=load(root,INPUTS[1]);leads=load(root,INPUTS[2]);spine=load(root,INPUTS[3]);readings=load(root,INPUTS[4]);old=load(root,INPUTS[5])
 native={r['id']:r for r in spine};prior=set(leads['combined_with_existing_inscribe_context_ids']);rows=data['records'];ids=[r['record_id'] for r in rows]
 require(len(ids)==len(set(ids))==127 and set(ids)==set(native)-prior,'missing, duplicate or fabricated frontier identity')
 require(collections.Counter(native[i]['series'] for i in ids)=={'H':114,'Y':13},'series/selection drift')
 require(len(data['source_receipts'])==4 and {r['printed_page'] for r in data['source_receipts']}=={54,55,56,57},'primary page receipts absent')
 for r in data['source_receipts']:
  require(len(r['image_sha256'])==64 and len(r['page_sha256'])==64 and r['image_bytes']>0 and r['redistributed'] is False,'source hash or rights boundary absent')
 for r in rows:
  require(r['source_id']=='CHIC1996' and r['printed_page'] in {54,55,56,57} and r['locator'] and r['source_url'],'missing primary provenance')
  require(r['document_type_literal'].startswith(native[r['record_id']]['series']),'document series mismatch')
  require(all(r[k] is False for k in ['reading_admitted','physical_identity_certified','independent_review_complete']),'metadata promoted')
  require(r['holding_status'] in {'REPORTED_BY_1996_EDITION_NOT_CURRENT_VERIFICATION','UNKNOWN_AND_LOST_SIGHT_OF_IN_EDITION'},'historical repository promoted')
 unknown=next(r for r in rows if r['record_id']=='CHIC-331')
 require(unknown['museum_abbreviation_literal']=='•' and unknown['catalogue_label_literal']=='<#331>' and unknown['holding_status']=='UNKNOWN_AND_LOST_SIGHT_OF_IN_EDITION','unknown holding/angle qualifier lost')
 require({r['inscribe_discovery_id'] for r in discovery['records']}=={r['id'] for r in old['records']},'discovery membership drift')
 for r in discovery['records']:
  require(r['chic_id'] is None and all(r[k] is False for k in ['reading_admitted','physical_identity_certified','independent_review_complete','images_included']),'unreviewed extension/compared motif admitted')
 vry=discovery['records'][0];require(vry['disposition']=='POST_CHIC1996_DISCOVERY_REFERENCE_ONLY','post-edition discovery misclassified')
 comparisons=vry['primary_text_comparisons'];require([r['face'] for r in comparisons]==['a','b','g','d'],'face-order coverage drift')
 require(all(r['primary_visual_check_complete'] is False for r in comparisons),'text extraction promoted to visual inspection')
 require(comparisons[0]['primary_proposed_literal']=='044-[005]' and comparisons[0]['primary_alternative_literal']=='044-073','Vrysinas side a uncertainty lost')
 require(comparisons[3]['primary_proposed_literal']=='042-[038]' and comparisons[3]['primary_first_sign_alternative'].startswith('036'),'Vrysinas side d uncertainty lost')
 require(len(readings)==13 and len({r['object_id'] for r in readings})==6,'canonical baseline unexpectedly changed')
 return {'schema_version':'1.0','checked':'2026-10-13','status':'PASS_BOUNDED_HY_FRONTIER','scope':{'previous_named_route_identities':len(prior),'new_primary_concordance_identities':len(ids),'new_primary_concordance_by_series':dict(collections.Counter(native[i]['series'] for i in ids)),'named_routes_plus_primary_concordance_identities':len(prior|set(ids)),'remaining_without_these_routes':sorted(set(native)-(prior|set(ids))),'discovery_dispositions':len(discovery['records']),'provisional_primary_text_comparisons':len(comparisons),'canonical_reading_versions':len(readings),'canonical_reading_objects':len({r['object_id'] for r in readings}),'independent_reviews_added':0},'claim_boundary':'Primary catalogue facts do not establish complete reading coverage, current holdings, physical identity, representative sampling, source independence or expert acceptance. Vrysinas text comparisons await primary facsimile collation.','inputs':[{'path':p,'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in INPUTS]}
def replay(root=ROOT):
 actual=validate(root);require(load(root,'analysis/hy-frontier-2026-10-13.json')==actual,'checkpoint receipt drift');return actual
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.write:(ROOT/'analysis/hy-frontier-2026-10-13.json').write_text(json.dumps(validate(),ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(replay()['scope']))
