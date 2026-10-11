"""Validate this bounded source transcription, without generalizing its scope."""
import json,pathlib
from jsonschema import Draft202012Validator
R=pathlib.Path(__file__).resolve().parents[1]
KNOWN={('CHIC-036','a'):['X','023-061-019-057'],('CHIC-036','b'):['100'],
       ('CHIC-040','a'):['X','019-070-061','X','072-039'],
       ('CHIC-040','b1'):['X','044-049','2'],('CHIC-040','b2'):['X','068-031','4']}
def validate(readings,report):
    original=readings
    readings=[r for r in original if r['source_id']=='CHIC1996']
    if len(original)!=len(readings):
        from validate_source_expansion import validate_new_readings
        validate_new_readings([r for r in original if r['source_id']!='CHIC1996'])
    schema=json.loads((R/'schemas/critical-reading-v5.schema.json').read_text())
    v=Draft202012Validator(schema)
    if len({r['reading_id'] for r in readings})!=len(readings):raise ValueError('duplicate reading')
    if len(readings)!=5 or {(r['object_id'],r['surface_id']) for r in readings}!=set(KNOWN):
        raise ValueError('source pilot membership drift')
    for r in readings:
        v.validate(r)
        if r['source_id']!='CHIC1996' or r['status']!='source-checked':raise ValueError('source/status drift')
        page=91 if r['object_id']=='CHIC-036' else 93
        if not r['locator'].startswith(f'p. {page}, #{r["object_id"][-3:]}'):raise ValueError('source locator drift')
        if [t['form'] for t in r['tokens']]!=KNOWN[r['object_id'],r['surface_id']]:raise ValueError('literal source transnumeration drift')
        if [t['position'] for t in r['tokens']]!=list(range(1,len(r['tokens'])+1)):raise ValueError('encoding order drift')
    if report['source_checked_readings']!=len(readings) or report['source_checked_objects']!=['CHIC-036','CHIC-040']:
        raise ValueError('pilot count drift')
    if report['external_review_completed'] is not False or report['phonetic_values_asserted']!=0:raise ValueError('unsupported certification')
    if report['reading_ids']!=[r['reading_id'] for r in readings]:raise ValueError('reading references drift')
    return {'status':'PASS','source_checked_objects':2,'source_checked_readings':5,'independent_reviews':0}
if __name__=='__main__':
    print(json.dumps(validate(json.loads((R/'corpus/critical-readings.json').read_text()),json.loads((R/'analysis/chic-primary-pilot-v1.json').read_text()))))
