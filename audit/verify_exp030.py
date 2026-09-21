"""Independent certificate verifier: no k4lib or experiment imports."""
import gzip,hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
summary=json.loads((root/'results/exp030/summary.json').read_text())
raw=(root/'results/exp030/cases.jsonl.gz').read_bytes()
assert hashlib.sha256(raw).hexdigest()==summary['case_gzip_sha256']
blob=gzip.decompress(raw)
assert hashlib.sha256(blob).hexdigest()==summary['case_uncompressed_sha256']
k4=json.loads((root/'data/k4.json').read_text())
assert hashlib.sha256(k4['ciphertext'].encode()).hexdigest()==summary['ciphertext_sha256']
pdata=root/'data/weltzeituhr_photos.json'
assert hashlib.sha256(pdata.read_bytes()).hexdigest()==summary['photo_dataset_sha256']
fr=json.loads(pdata.read_text())['tier1_frozen_reconstruction']
tape=''.join(fr['upper']+fr['lower'])
assert hashlib.sha256(tape.encode()).hexdigest()==summary['tape_sha256']
cribs=[(cr['start']+j,p) for cr in k4['confirmed_cribs'] for j,p in enumerate(cr['plaintext'])]
alph={'STD':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','KRY':'KRYPTOSABCDEFGHIJLMNQUVWXZ'}
convs=[(m,p,c) for m in ('vigenere','beaufort','variant_beaufort') for p in ('STD','KRY') for c in ('STD','KRY')]

def value(ci,j):
    m,pa,ca=convs[ci];i,p=cribs[j]
    pv=alph[pa].index(p);cv=alph[ca].index(k4['ciphertext'][i])
    return (cv-pv if m=='vigenere' else cv+pv if m=='beaufort' else pv-cv)%26

count=0
for count,line in enumerate(blob.splitlines(),1):
    row=json.loads(line);o,s,ci=row['offset'],row['step'],row['convention']
    assert (o,s,ci)==((count-1)//1440,((count-1)//12)%120,(count-1)%12)
    a,b=row['witness']
    assert 0<=a<b<24
    i,j=cribs[a][0],cribs[b][0]
    assert tape[(o+s*i)%120]==tape[(o+s*j)%120]
    assert value(ci,a)!=value(ci,b)
assert count==172800
assert summary['counts']=={'contradiction':count}
assert summary['survivors']==[]
print('PASS: 172800/172800 contradiction witnesses verified independently; complete parameter coverage and input/result hashes verified.')
