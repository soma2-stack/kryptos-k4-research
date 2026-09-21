"""EXP-031. Bounded multi-face running-key test; see docs/exp031-preregistration.md.
Importing this module does not score K4 or run an experiment.
"""
import json,sys,hashlib
from pathlib import Path
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from k4lib.data import load,REPO_ROOT
from k4lib.alphabets import ALPHABETS
from k4lib.conventions import all_conventions
ROOT=Path(REPO_ROOT)

def windows(doc):
    """Yield EVERY labelled legal window; no modulo, no unknowns, crosses a face."""
    faces=doc['frozen_arc']['faces']
    for sector_direction in (1,-1):
      ordered=faces if sector_direction==1 else faces[::-1]
      for bands in (('upper','lower'),('lower','upper')):
        tape='';owners=[]
        for face in ordered:
          s=''.join(''.join(c for c in n if 'A'<=c<='Z') for b in bands for n in face[b])
          tape+=s;owners.extend([face['sector']]*len(s))
        for letter_direction in (1,-1):
          text=tape if letter_direction==1 else tape[::-1]
          labels=owners if letter_direction==1 else owners[::-1]
          for start in range(len(text)-96):
            if len(set(labels[start:start+97]))<2:continue
            yield {'sector_direction':sector_direction,'bands':list(bands),'letter_direction':letter_direction,'start':start},text[start:start+97]

def unique_windows(doc):
    result={}
    for label,text in windows(doc):result.setdefault(text,[]).append(label)
    return result

def score(text,alphabet,cv,cribs):
    return sum(cv.encrypt_letter(p,alphabet.index(text[i]))==c for i,p,c in cribs)

def controls(doc):
    ws=unique_windows(doc); labels=list(windows(doc));k4=load();cvs=all_conventions()
    # Every traversal label's first and last admitted window, all conventions/alphabets.
    groups={}
    for label,text in labels:
      key=(label['sector_direction'],tuple(label['bands']),label['letter_direction'])
      groups.setdefault(key,[]).append(text)
    count=0
    for texts in groups.values():
      for text in (texts[0],texts[-1]):
       for a in ALPHABETS.values():
        for cv in cvs:
         pt=['X']*97
         for i,p,_ in k4.crib_positions():pt[i]=p
         # Independent forward modular arithmetic, not production encrypt_letter.
         pa=ALPHABETS[cv.plain_alpha];ca=ALPHABETS[cv.cipher_alpha]
         ct=[]
         for p,k in zip(pt,text):
          x,y=pa.index(p),a.index(k)
          z=x+y if cv.combiner=='vigenere' else y-x if cv.combiner=='beaufort' else x-y
          ct.append(ca[z%26])
         crib=[(i,p,ct[i]) for i,p,_ in k4.crib_positions()]
         assert text in ws and score(text,a,cv,crib)==24
         count+=1
    return count

def main():
    doc=json.loads((ROOT/'data/weltzeituhr_checkpoint_J.json').read_text())
    from audit.verify_checkpoint_J import verify
    verify()
    n=controls(doc);print('PASS planted controls',n,flush=True)
    ws=unique_windows(doc);cribs=load().crib_positions();rows=[];hist=Counter();hits=[]
    for wid,(text,aliases) in enumerate(ws.items()):
     for ka,a in ALPHABETS.items():
      for cv in all_conventions():
       got=score(text,a,cv,cribs);hist[got]+=1
       row={'window':wid,'key_alphabet':ka,'convention':cv.name,'matches':got}
       rows.append(row)
       if got==24:hits.append(row)
    out=ROOT/'results/exp031';out.mkdir(exist_ok=True)
    (out/'windows.json').write_text(json.dumps([{'text':t,'aliases':a} for t,a in ws.items()],separators=(',',':'))+'\n')
    # Full compact score vector in declared order; no cherry-picked alignments.
    (out/'scores.json').write_text(json.dumps([r['matches'] for r in rows],separators=(',',':'))+'\n')
    summary={'experiment':'EXP-031','evidence_sha256':hashlib.sha256((ROOT/'data/weltzeituhr_checkpoint_J.json').read_bytes()).hexdigest(),'labelled_windows':sum(len(a) for a in ws.values()),'unique_windows':len(ws),'cases':len(rows),'positive_controls':n,'histogram':dict(sorted(hist.items())),'exact_hits':hits,'score_order':'window insertion order, key alphabet STD/KRY, all_conventions() order','windows_sha256':hashlib.sha256((out/'windows.json').read_bytes()).hexdigest(),'scores_sha256':hashlib.sha256((out/'scores.json').read_bytes()).hexdigest(),'limitations':'Only specified 3-face per-sector band concatenations; no full-drum wrap, whole-band-first or non-running-key architecture.'}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
