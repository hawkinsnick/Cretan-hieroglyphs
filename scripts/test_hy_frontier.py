"""Reject false completeness, stripped uncertainty and unsupported object joins."""
import copy,json,shutil,tempfile,unittest
from pathlib import Path
from validate_hy_frontier import ROOT,replay
class FrontierTests(unittest.TestCase):
 def test_native_replay(self):self.assertEqual(replay()['scope']['named_routes_plus_primary_concordance_identities'],331)
 def test_hostile_mutations(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)
   for p in ['research','corpus','analysis']:shutil.copytree(ROOT/p,root/p)
   def reject(path,mutate):
    f=root/path;raw=f.read_bytes();x=json.loads(raw);mutate(x);f.write_text(json.dumps(x))
    try:
     with self.assertRaises((ValueError,KeyError,StopIteration)):replay(root)
    finally:f.write_bytes(raw)
   p='research/hy-primary-concordance-2026-10-13.json'
   reject(p,lambda x:x['records'].pop())
   reject(p,lambda x:x['records'].append(copy.deepcopy(x['records'][0])))
   reject(p,lambda x:x['records'][0].update(reading_admitted=True))
   reject(p,lambda x:x['records'][0].update(holding_status='CURRENTLY_CERTIFIED'))
   reject(p,lambda x:next(r for r in x['records'] if r['record_id']=='CHIC-331').update(catalogue_label_literal='#331'))
   p='research/inscribe-discovery-dispositions-2026-10-13.json'
   reject(p,lambda x:x['records'][1].update(chic_id='CHIC-041'))
   reject(p,lambda x:x['records'][0]['primary_text_comparisons'][0].update(primary_proposed_literal='044-005'))
   reject(p,lambda x:x['records'][0]['primary_text_comparisons'][0].update(primary_visual_check_complete=True))
   reject(p,lambda x:x['records'][0]['primary_text_comparisons'][3].pop('primary_first_sign_alternative'))
   reject('analysis/hy-frontier-2026-10-13.json',lambda x:x['scope'].update(canonical_reading_objects=331))
if __name__=='__main__':unittest.main()
