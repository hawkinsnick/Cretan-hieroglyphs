"""Validate bounded source-growth views; do not certify ancient objects or readings."""
import argparse,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path):return json.loads((ROOT/path).read_text())
def require(ok,message):
 if not ok:raise ValueError(message)
def digest(raw):return hashlib.sha256(raw).hexdigest()
def nonadmission(row):
 require(row['reading_admitted'] is False and row['images_included'] is False,'unsupported reading/image admission')

FILES=['research/dbas-chs-catalogue-leads.json','research/inscribe-unmapped-discovery.json']
def validate(leads,discovery,source_dir=None):
 rows=leads['records'];ids={r['id'] for r in rows};chic={r['chic_id'] for r in rows}
 require(len(rows)==len(ids)==len(chic)==leads['published_result_count']==193,'source-local duplicate or CHIC collision')
 native={r['id'] for r in load('corpus/chic-catalogue-spine.json')};require(chic<=native,'source join outside bounded catalogue')
 for r in rows:
  nonadmission(r);require(r['physical_identity_certified'] is False,'unsupported object identity')
  require(r['id']=='DBAS-CHS-'+r['source_local_id'],'source-local identity drift')
  require(r['chic_label_literal']=='Nr. '+str(int(r['chic_id'].split('-')[1])),'literal/canonical catalogue mismatch')
  require(r['source_url'].startswith('https://www.aegean-museum.it/dbas/pub/CMpro/chs/seal.php?idseal='+r['source_local_id']+'&'),'unbound source locator')
 require(sorted(chic)==leads['covered_chic_ids'],'source discovery coverage drift')
 prior={r['object_id'] for r in load('corpus/context-assertions.json')['records']}
 require(sorted(chic|prior)==leads['combined_with_existing_inscribe_context_ids'],'overlap or source coverage drift')
 require(len(discovery['records'])==3 and len({r['id'] for r in discovery['records']})==3,'unmapped page loss/collision')
 require(discovery['source_index_object_links']==29 and discovery['existing_context_links']==26,'index snapshot scope drift')
 for r in discovery['records']:
  nonadmission(r);require(r['chic_id'] is None and r['independent_review_complete'] is False,'motif or sign number promoted to object join')
  require(r['fields']['Script'] in ['-','Cretan Hieroglyphic'],'source script qualifier lost')
  require(r['classification_status']==('SOURCE_LABELLED_CRETAN_HIEROGLYPHIC' if r['fields']['Script']=='Cretan Hieroglyphic' else 'SOURCE_DASH_NOT_A_SCRIPT_IDENTIFICATION'),'unknown script promoted')
 if source_dir:
  raw=(Path(source_dir)/'chs-results.html').read_bytes();require(digest(raw)==leads['source_response_sha256'],'DBAS source byte drift')
  from html.parser import HTMLParser
  class Text(HTMLParser):
   def __init__(self):super().__init__();self.parts=[]
   def handle_data(self,text):self.parts.append(text)
  from urllib.parse import urljoin,parse_qs,urlsplit
  parsed=[]
  for block in re.findall(r'<table border="1".*?</table>',raw.decode('iso-8859-1'),re.S):
   p=Text();p.feed(block);text=' '.join(' '.join(p.parts).split());m=re.search(r'chic:\s*Nr\. (\d+)\s*place of finding:',text)
   if m is None:
    require(text=='Item found: 193 Item percentage: 100 %','unparsed result block');continue
   link=re.search(r'href="(\./seal\.php\?idseal=\d+&nrff=0&nrfs=0)"',block).group(1);url=urljoin(leads['query_url'],link)
   parsed.append((parse_qs(urlsplit(url).query)['idseal'][0],'CHIC-'+m.group(1).zfill(3),re.search(r'cms:\s*(.*?)\s*chic:',text).group(1),url))
  require(parsed==[(r['source_local_id'],r['chic_id'],r['cms_label_literal'],r['source_url']) for r in rows],'DBAS catalogue pair replay drift')
  for r in discovery['records']:
   name=r['source_url'].rsplit('/',1)[1]+'.html';require(digest((Path(source_dir)/name).read_bytes())==r['source_sha256'],'INSCRIBE source byte drift')
 return {'catalogue_lead_rows':193,'new_unmapped_pages':3,'chic_identities_with_either_named_route':len(chic|prior),'reading_admissions':0,'independent_review_complete':False}

def build(source_dir=None):
 result=validate(*(load(p) for p in FILES),source_dir=source_dir)
 return dict(schema_version='1.0',checked='2026-10-12',status='PASS_BOUNDED_SOURCE_GROWTH',scope=result,inputs=[{'path':p,'sha256':digest((ROOT/p).read_bytes())} for p in FILES])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--source-dir',type=Path);a=p.parse_args();d=build(a.source_dir);path=ROOT/'analysis/source-growth-2026-10-12.json'
 if a.write:path.write_text(json.dumps(d,indent=2)+'\n')
 else:require(json.loads(path.read_text())==d,'source-growth audit drift')
 print(json.dumps(d['scope']))
