"""Independent complete-window and score verification; no experiment/k4lib imports."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def read(p):return json.loads((root/p).read_text())
d=read('data/weltzeituhr_checkpoint_J.json');s=read('results/exp031/summary.json')
assert hashlib.sha256((root/'data/weltzeituhr_checkpoint_J.json').read_bytes()).hexdigest()==s['evidence_sha256']
for name in ('windows','scores'):
 assert hashlib.sha256((root/f'results/exp031/{name}.json').read_bytes()).hexdigest()==s[name+'_sha256']
expected={};faces=d['frozen_arc']['faces']
for sd in (1,-1):
 for bands in (['upper','lower'],['lower','upper']):
  blocks=[]
  for face in faces[::sd]:
   for band in bands:
    for line in face[band]:blocks.extend((ch,face['sector']) for ch in line if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  assert len(blocks)==272
  for ld in (1,-1):
   stream=blocks[::ld]
   for offset in range(176):
    part=stream[offset:offset+97]
    assert len(part)==97
    if any(owner!=part[0][1] for ch,owner in part):
     key=''.join(ch for ch,owner in part)
     expected.setdefault(key,[]).append({'sector_direction':sd,'bands':bands,'letter_direction':ld,'start':offset})
actual=read('results/exp031/windows.json')
assert actual==[{'text':k,'aliases':v} for k,v in expected.items()]
assert len(expected)==1216
scores=read('results/exp031/scores.json');k4=read('data/k4.json')
known=[(cr['start']+j,p) for cr in k4['confirmed_cribs'] for j,p in enumerate(cr['plaintext'])]
alph=('ABCDEFGHIJKLMNOPQRSTUVWXYZ','KRYPTOSABCDEFGHIJLMNQUVWXZ')
calculated=[]
for text in expected:
 for keyalpha in alph:
  for operation in ('add','reflect','subtract'):
   for pa in alph:
    for ca in alph:
     got=0
     for i,p in known:
      a,b=pa.index(p),ca.index(k4['ciphertext'][i])
      required=(b-a if operation=='add' else b+a if operation=='reflect' else a-b)%26
      got+=keyalpha.index(text[i])==required
     calculated.append(got)
assert calculated==scores and len(scores)==29184
from collections import Counter
assert dict(Counter(scores))=={int(k):v for k,v in s['histogram'].items()}
assert sum(x==24 for x in scores)==len(s['exact_hits'])
assert s['positive_controls']==384
print('PASS: all 1216 windows/aliases reconstructed independently; all 29184 scores agree; file hashes, complete coverage and exact-hit count verified. Control count recorded as 384 (controls run by experiment).')
