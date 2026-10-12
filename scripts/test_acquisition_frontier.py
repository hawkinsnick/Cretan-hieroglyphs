import copy,unittest
from acquisition_frontier import load,validate,FILES
class FrontierGuards(unittest.TestCase):
 def setUp(self):self.data=[load(p) for p in FILES]
 def reject(self,mutate):
  d=copy.deepcopy(self.data);mutate(d)
  with self.assertRaises((ValueError,KeyError)):validate(*d)
 def test_actual_views(self):validate(*self.data)
 def test_duplicate_row(self):self.reject(lambda d:d[0]['records'].append(copy.deepcopy(d[0]['records'][0])))
 def test_metadata_as_reading(self):self.reject(lambda d:d[0]['records'][0].update(reading_admitted=True))
 def test_stratum_loss(self):self.reject(lambda d:d[1]['records'].pop())
 def test_source_glyph_import(self):self.reject(lambda d:d[0]['records'][0]['assertions'].append(dict(field='transnumeration',value='made-up',source_id='JASINK-BOMBARDIERI-CHS',source_url=d[0]['records'][0]['source_url'],locator='fake',status='source_reported')))
 def test_ui_heading_as_object_type(self):self.reject(lambda d:d[0]['records'][0]['assertions'][2].update(value='seal'))
 def test_cohort_accepted(self):self.reject(lambda d:d[1].update(reading_pilot_complete=True))
