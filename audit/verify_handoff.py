"""Bounded independent audit; never imports EXP-024/029 executable modules."""
import hashlib, json, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from k4lib.data import load, REPO_ROOT
from k4lib.alphabets import ALPHABETS
from k4lib.conventions import all_conventions
from k4lib.weltzeituhr import procedures, synthetic_clock
from k4lib.wz_graph import DrumGraph, load_from_photos
from k4lib.wz_panels import build_clock, ReconstructionIncomplete

k4 = load()
assert all(ok for _,ok,_ in k4.verify())
fr=json.loads((Path(REPO_ROOT)/'data/weltzeituhr_photos.json').read_text())['tier1_frozen_reconstruction']
u,l=(''.join(fr[b]) for b in ('upper','lower'))
assert (len(u),len(l)) == (62,58)
tapes=[u+l,l+u]
assert tapes[1] == tapes[0][62:]+tapes[0][:62]
positions=[i for i,_,_ in k4.crib_positions()]

def encrypt(p,k,cv):
    a=ALPHABETS[cv.plain_alpha];b=ALPHABETS[cv.cipher_alpha]
    v=a.index(p)
    return b[({'vigenere':v+k,'beaufort':k-v,'variant_beaufort':v-k}[cv.combiner])%26]

# Exhaustive primitive checks, independent arithmetic versus library.
for cv in all_conventions():
 for p in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
  for key in range(26):
   c=encrypt(p,key,cv)
   assert cv.encrypt_letter(p,key)==c
   assert cv.decrypt_letter(c,key)==p and cv.key_index(p,c)==key
print('12 x 26 x 26 independent arithmetic checks PASS')

# Synthetic EXP-024 source components only: no historical test and no large search.
procs=procedures(synthetic_clock(seed=1),berlin_sector=13)
t=procs['cw/start0/ul']; cv=all_conventions()[0]
ct={i:encrypt(p,ALPHABETS['STD'].index(t[(137+i)%len(t)]),cv) for i,p,_ in k4.crib_positions()}
assert all(cv.key_index(p,ct[i])==ALPHABETS['STD'].index(t[(137+i)%len(t)]) for i,p,_ in k4.crib_positions())
print('EXP-024 synthetic planted construction arithmetic PASS (full search not rerun)')

# Independent direct encryption, not the derived-key scorer used in EXP-029.
def scan(cribs):
 hist=Counter(); bounded=Counter(); unique=set()
 for ti,t in enumerate(tapes):
  for ka,a in ALPHABETS.items():
   for d in (1,-1):
    for o in range(120):
     keys=[a.index(t[(o+d*i)%120]) for i in range(97)]
     for cv in all_conventions():
      score=sum(encrypt(p,keys[i],cv)==c for i,p,c in cribs)
      hist[score]+=1
      unique.add((tuple(keys),cv.name))
      if 0<=o+d*96<120: bounded[score]+=1
 return hist,bounded,len(unique)

# Boundary controls verify legal full windows, in both band orders and directions.
for t in tapes:
 for d,offsets in ((1,(0,23)),(-1,(96,119))):
  for o in offsets:
   for cv in all_conventions():
    keys=[ALPHABETS['STD'].index(t[o+d*i]) for i in range(97)]
    ct=[encrypt('X',k,cv) for k in keys]
    assert all(cv.decrypt_letter(c,k)=='X' for c,k in zip(ct,keys))
print('96 nonwrapping endpoint controls PASS')
h,b,n=scan(k4.crib_positions())
assert h==Counter({0:4668,1:4186,2:1870,3:646,4:134,5:14,7:2})
assert sum(h.values())==11520 and n==5760 and sum(b.values())==2304 and h[24]==b[24]==0
print(json.dumps({'legacy_histogram':dict(sorted(h.items())), 'distinct_full_stream_conventions':n,'nonwrapping_histogram':dict(sorted(b.items()))},sort_keys=True))

# Conflict controls: current data remain complete; contradictory future inputs fail closed.
for mode in ('complete_order','partial_order','partial_extra','no_completeness'):
 g=DrumGraph()
 if mode=='no_completeness':g.add_face('f',upper=['A'],lower=['B'])
 else:
  g.add_face('f',upper=['A','B'],lower=['C'],complete_bands=('upper','lower'))
  if mode=='complete_order':g.add_face('f',upper=['B','A'],complete_bands=('upper',))
  elif mode=='partial_order':g.add_face('f',upper=['B','A'],partial_bands=('upper',))
  else:g.add_face('f',upper=['D'],partial_bands=('upper',))
 assert not g.face_complete('f'),mode
 if mode!='no_completeness': assert g.faces['f']['upper']==['A','B'] and g.faces['f']['conflicts']
g,doc=load_from_photos()
assert g.face_complete('UTC+1 @1988-89')
assert not any(f['conflicts'] for f in g.faces.values())
try:build_clock()
except ReconstructionIncomplete:pass
else:raise AssertionError('incomplete historical clock accepted')
print('Graph conflict controls, actual frozen graph, historical completeness guard PASS')
print('Audit PASS; no photograph or exact date independently verified.')
