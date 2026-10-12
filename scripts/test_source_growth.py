import copy,unittest
from source_growth import load,validate,FILES
class SourceGrowthGuards(unittest.TestCase):
 def setUp(self):self.data=[load(p) for p in FILES]
 def reject(self,mutator):
  d=copy.deepcopy(self.data);mutator(d)
  with self.assertRaises((ValueError,KeyError)):validate(*d)
 def test_native_views(self):validate(*self.data)
 def test_duplicate_source_id(self):self.reject(lambda d:d[0]['records'].append(copy.deepcopy(d[0]['records'][0])))
 def test_reading_admission(self):self.reject(lambda d:d[0]['records'][0].update(reading_admitted=True))
 def test_image_admission(self):self.reject(lambda d:d[0]['records'][0].update(images_included=True))
 def test_object_join_from_sign_number(self):self.reject(lambda d:d[1]['records'][1].update(chic_id='CHIC-041'))
 def test_source_label_drift(self):self.reject(lambda d:d[0]['records'][0].update(chic_label_literal='Nr. 999'))
 def test_script_dash_promotion(self):self.reject(lambda d:d[1]['records'][1].update(classification_status='SOURCE_LABELLED_CRETAN_HIEROGLYPHIC'))
