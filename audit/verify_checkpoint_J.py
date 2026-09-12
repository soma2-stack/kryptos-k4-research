"""Frozen evidence guards, no K4 cryptanalytic search."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
EXPECTED=[(['REYKJAVIK','DUBLIN','LONDON','LISSABON','ALGIER','MADEIRA','BISSAU'],['CASABLANCA','CONAKRY','DAKAR','BAMAKO','ACCRA']),(['AMSTERDAM','BERLIN','BRUSSEL','BUDAPEST','MADRID','PARIS','PRAG','STOCKHOLM','WARSCHAU'],['KOPENHAGEN','WIEN','BERN','BELGRAD','ROM','TUNIS','BRAZZAVILLE','KINSHASA','LUANDA']),(['BUKAREST','HELSINKI','SOFIA','ATHEN','NIKOSIA'],['BEIRUT','DAMASKUS','KAIRO','KHARTUM','LUSAKA','MAPUTO'])]
def verify():
 d=json.loads((ROOT/'data/weltzeituhr_checkpoint_J.json').read_text());arc=d['frozen_arc']
 assert arc['face_order_visual_left_to_right']==['UTC+0','UTC+1','UTC+2']
 assert len(arc['faces'])==3 and arc['total_letters']==272
 for f,(u,l) in zip(arc['faces'],EXPECTED):
  assert f['upper']==u and f['lower']==l
  assert f['era']=='1988-89' and f['date']=='1989-11-04'
  assert f['complete_bands']==['upper','lower'] and f['band_ends_visible']
  assert not f['unknown'] and not f['conflicts']
  assert all(n!='UNKNOWN' for n in u+l)
 old=json.loads((ROOT/'data/weltzeituhr_photos.json').read_text())['tier1_frozen_reconstruction']
 assert old['upper']==EXPECTED[1][0] and old['lower']==EXPECTED[1][1] and old['letters']['total']==120
 for im in d['images']:assert hashlib.sha256((ROOT/im['path']).read_bytes()).hexdigest()==im['sha256']
 assert any(c['status']=='UNRESOLVED CONFLICT' for c in d['conflict_ledger'])
 assert all(not o['UTC+3']['complete'] and 'UNKNOWN' in o['UTC+3']['lower'] for o in d['observations'])
 print('PASS: exact three-face order, all lines, era, ends, unchanged CET, image hashes and retained UTC+3 conflict')
if __name__=='__main__':verify()
