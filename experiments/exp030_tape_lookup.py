"""EXP-030: see docs/exp030-preregistration.md, committed before this experiment.
Run from any directory. Writes deterministic gzip case certificates and JSON summary.
Only real-input execution occurs in main(); imports are side-effect free.
"""
import gzip, hashlib, json, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from k4lib.data import load, REPO_ROOT
from k4lib.alphabets import ALPHABETS
from k4lib.conventions import all_conventions


def solve(symbols, values):
    """Exact function feasibility; return first contradiction pair or partial map."""
    mapping={};first={}
    for j,(symbol,value) in enumerate(zip(symbols,values)):
        if symbol in mapping and mapping[symbol]!=value:
            return [first[symbol],j],None
        mapping[symbol]=value;first.setdefault(symbol,j)
    return None,mapping


def pairwise(symbols,values):
    return all(symbols[i]!=symbols[j] or values[i]==values[j]
               for i in range(len(symbols)) for j in range(i))


def independent_encrypt(p,k,cv):
    p=ALPHABETS[cv.plain_alpha].index(p)
    if cv.combiner=='vigenere':c=p+k
    elif cv.combiner=='beaufort':c=k-p
    else:c=p-k
    return ALPHABETS[cv.cipher_alpha][c%26]


def controls(tape,cribs):
    count=0
    # Fixed deterministic maps: permutation unlike STD/KRY, and non-injection.
    for mapping in ({c:(7*j+3)%26 for j,c in enumerate(ALPHABETS['STD'])},
                    {c:j%5 for j,c in enumerate(ALPHABETS['STD'])}):
      for step in (0,1,119,2,30):
       for cv in all_conventions():
        text=['X']*97
        for i,p,_ in cribs:text[i]=p
        symbols=[tape[(17+step*i)%120] for i in range(97)]
        ct=''.join(independent_encrypt(p,mapping[s],cv) for p,s in zip(text,symbols))
        sampled=[symbols[i] for i,_,_ in cribs]
        values=[cv.key_index(p,ct[i]) for i,p,_ in cribs]
        witness,got=solve(sampled,values)
        assert witness is None and pairwise(sampled,values)
        assert all(got[s]==mapping[s] for s in got)
        count+=1
    assert solve('AA',[0,1])[0]==[0,1]
    assert not pairwise('AA',[0,1])
    assert solve('AB',[0,0])[0] is None  # allowed function, not a permutation
    return count


def main():
    root=Path(REPO_ROOT); k4=load()
    assert all(ok for _,ok,_ in k4.verify())
    path=root/'data/weltzeituhr_photos.json'
    fr=json.loads(path.read_text())['tier1_frozen_reconstruction']
    tape=''.join(fr['upper']+fr['lower'])
    assert len(tape)==120
    cribs=k4.crib_positions(); positions=[i for i,_,_ in cribs]
    cvs=all_conventions()
    ncontrols=controls(tape,cribs)
    print(f'Planted controls PASS: {ncontrols}; contradictory and non-injective unit cases PASS',flush=True)
    required=[[cv.key_index(p,c) for i,p,c in cribs] for cv in cvs]
    out=root/'results/exp030';out.mkdir(exist_ok=True)
    casepath=out/'cases.jsonl.gz'
    counts=Counter(); seq=Counter(); survivors=[]
    h=hashlib.sha256()
    with casepath.open('wb') as raw:
      with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as fh:
       for offset in range(120):
        for step in range(120):
         symbols=[tape[(offset+step*i)%120] for i in positions]
         for ci,values in enumerate(required):
          witness,mapping=solve(symbols,values)
          feasible=witness is None
          # Independently formulated exact gate for every case.
          assert feasible==pairwise(symbols,values)
          tag='function_feasible' if feasible else 'contradiction'
          counts[tag]+=1
          if step in (1,119):seq[tag]+=1
          row={'offset':offset,'step':step,'convention':ci,'witness':witness}
          if feasible:
           row['mapping']=mapping
           row['bijective_extendable']=len(set(mapping.values()))==len(mapping)
           counts['bijection_feasible']+=int(row['bijective_extendable'])
           survivors.append(row)
          line=(json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode()
          h.update(line);fh.write(line)
    summary={'experiment':'EXP-030','base':'0cb2b38d2b81980d9c7b099c3727423335f9d86e',
      'preregistration_commit':'56ab721','ciphertext_sha256':k4.sha256,
      'photo_dataset_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'tape_sha256':hashlib.sha256(tape.encode()).hexdigest(),'frozen_reconstruction':fr,
      'parameters':{'offset':[0,119],'step':[0,119],'conventions':[c.name for c in cvs],
      'lookup':'all functions A-Z to Z26; bijections also classified'},
      'cases':172800,'controls_passed':ncontrols,'independent_pairwise_checks':172800,
      'counts':dict(counts),'sequential_counts':dict(seq),'survivors':survivors,
      'case_format':'JSONL: zero-based crib-list indices in contradiction witness',
      'case_uncompressed_sha256':h.hexdigest(),
      'case_gzip_sha256':hashlib.sha256(casepath.read_bytes()).hexdigest(),
      'grade':'EXHAUSTIVELY ELIMINATED WITHIN SPECIFIED MODEL' if not survivors else 'FEASIBLE FITS, NOT PREDICTIVE EVIDENCE'}
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:summary[k] for k in ('cases','counts','sequential_counts','grade')},indent=2))

if __name__=='__main__':main()
