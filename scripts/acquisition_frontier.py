"""Validate the acquisition frontier without glyph, core or expert admission."""
import argparse,collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p,root=ROOT):return json.loads((root/p).read_text())
def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(raw):return hashlib.sha256(raw).hexdigest()
FILES=['research/stratified-source-context.json','research/representative-acquisition-cohort.json']
EXPECTED={'H':[16,48,58,66,68,85,89,122],'I':[123,124,125,126,127],'S':[180,197,202,207,236,252,313,315],'Y':[316,317,324,328]}
def validate_context(rows,root=ROOT,source_dir=None):
 require(len(rows)==len({r['object_id'] for r in rows})==5 and {r['object_id'] for r in rows}=={'CHIC-123','CHIC-124','CHIC-125','CHIC-126','CHIC-317'},'context membership drift')
 sources={s['id']:s for s in load('bibliography/sources.json',root)}
 leads={r['chic_id']:r for r in load('research/dbas-chs-catalogue-leads.json',root)['records']}
 for r in rows:
  require(r['reading_admitted'] is False and r['independent_review'] is False,'metadata promoted to reading/review')
  require(r['rights']['images_included'] is False and r['rights']['models_included'] is False,'restricted source images/models included')
  require(r['source_id'] in sources and len(r['source_sha256'])==64,'source closure lost')
  fields={a['field']:a for a in r['assertions']};require(len(fields)==len(r['assertions']),'duplicate source fields')
  require(all(a['source_id']==r['source_id'] and a['source_url']==r['source_url'] and a['locator'] and a['status'] in ['source_reported','source_reported_unknown'] for a in r['assertions']),'assertion provenance/qualification drift')
  if r['object_id']=='CHIC-317':
   require(r['source_id']=='CIVITILLO-2021' and r['source_url']==sources['CIVITILLO-2021']['url'],'pithos source drift')
   require({k:a['value'] for k,a in fields.items()}=={'object_type':'pithos','inscription_location':'body','inscription_execution':'incised before firing'},'unsupported new pithos facts')
   require(r['visually_inspected_pdf_pages']==[10],'source inspection scope drift')
   if source_dir:
    raw=(Path(source_dir)/'civitillo2021.pdf').read_bytes();require(raw.startswith(b'%PDF-') and sha(raw)==r['source_sha256'],'primary context source bytes drift')
  else:
   require(r['source_id']=='JASINK-BOMBARDIERI-CHS' and r['source_url']==leads[r['object_id']]['source_url'],'unbound DBAS object join')
   require(set(fields)=={'cms_reference','findplace','object_subtype','material','dimensions_literal','repository'},'uninspected glyph/classification field imported')
   require(fields['object_subtype']['value']=='sealing' and fields['material']['value']=='clay (clay)','generic SEAL heading promoted to object class')
   if source_dir:
    from html.parser import HTMLParser
    class Text(HTMLParser):
     def __init__(self):super().__init__();self.items=[]
     def handle_data(self,s):
      if s.strip():self.items.append(s.strip())
    n=int(r['object_id'].split('-')[1]);raw=(Path(source_dir)/f'chic-{n}.html').read_bytes();require(sha(raw)==r['source_sha256'],'DBAS byte drift');p=Text();p.feed(raw.decode('iso-8859-1'));items=p.items[:p.items.index('FACE A')]
    require(items[items.index('CHIC nr')+1]==': '+str(n),'source CHIC number mismatch')
    for label,key in [('CMS nr','cms_reference'),('place of finding','findplace'),('shape','object_subtype'),('material','material'),('dimensions mm','dimensions_literal'),('place of conservation','repository')]:require(items[items.index(label)+1].removeprefix(': ').strip()==fields[key]['value'],'literal metadata normalization/damage')
 return True
def validate(context,cohort,root=ROOT,source_dir=None):
 rows=context['records'];validate_context(rows,root,source_dir)
 members=cohort['records'];require(len(members)==len({r['id'] for r in members})==25,'cohort membership/duplication drift')
 actual={s:sorted(int(r['id'].split('-')[1]) for r in members if r['series']==s) for s in 'HISY'};require(actual==EXPECTED and cohort['required_strata']=={'H':8,'I':5,'S':8,'Y':4},'stratum selection drift')
 require(cohort['reading_pilot_complete'] is False and cohort['analysis_executed'] is False and cohort['expert_acceptance'] is False,'metadata cohort promoted to analysis/acceptance')
 native={r['id']:r for r in load('corpus/chic-catalogue-spine.json',root)};meta={r['object_id']:r for r in load('corpus/context-assertions.json',root)['records']+rows};readings=load('corpus/critical-readings.json',root)
 for r in members:
  require(native[r['id']]['series']==r['series'] and r['source_context_available'] is True and r['source_url']==meta[r['id']]['source_url'],'source or catalogue stratum mismatch')
  require(r['existing_reading_ids']==[a['reading_id'] for a in readings if a['object_id']==r['id']],'preexisting reading scope drift')
  require(r['source_id']==meta[r['id']]['source_id'] and r['reading_coverage']==('PARTIAL_PREEXISTING_SOURCE_ASSERTIONS' if r['existing_reading_ids'] else 'NO_SOURCE_READING_ENCODED'),'unsupported cohort source/reading status')
  require(r['new_reading_admission'] is False and r['independent_review_complete'] is False,'unsupported cohort admission')
 return dict(context_supplements=5,combined_context_identities=len(meta),cohort_members=25,metadata_strata=dict(collections.Counter(r['series'] for r in members)),cohort_objects_with_preexisting_readings=sum(bool(r['existing_reading_ids']) for r in members),new_readings=0,expert_acceptance=False)

def build(root=ROOT,source_dir=None):
 scope=validate(*(load(p,root) for p in FILES),root=root,source_dir=source_dir)
 return dict(schema_version='1.0',checked='2026-10-12',status='PASS_BOUNDED_ACQUISITION_FRONTIER',scope=scope,inputs=[dict(path=p,sha256=sha((root/p).read_bytes())) for p in FILES])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--source-dir',type=Path);a=p.parse_args();d=build(source_dir=a.source_dir);out=ROOT/'analysis/acquisition-frontier-2026-10-12.json'
 if a.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:require(json.loads(out.read_text())==d,'frontier receipt drift')
 print(json.dumps(d['scope']))
