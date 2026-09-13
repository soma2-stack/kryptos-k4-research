"""Independent scalar verification of AH statistics and exact crib facts.
The scalar oracle imports no project cryptographic code. It compares its own
definitions with the vectorized audit on K4 and 43 fixed diagnostic controls.
No cipher-family feasibility search is performed.
"""
from collections import Counter
from itertools import combinations
import importlib.util
import json
import math
from pathlib import Path
import random
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ah", ROOT/"audit/checkpoint_AH.py")
ah = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ah)
saved = json.loads((ROOT/"results/checkpoint_AH.json").read_text())


def collisions(seq):
    return sum(n*(n-1)//2 for n in Counter(seq).values())


def scalar(seq):
    n = len(seq)
    h = Counter(seq)
    q = 1/26
    lags = [sum(seq[i] == seq[i+d] for i in range(n-d)) for d in range(1,n)]
    periods = []
    for p in range(2,49):
        pairs = [(i,j) for i,j in combinations(range(n),2) if i%p == j%p]
        matches = sum(seq[i] == seq[j] for i,j in pairs)
        periods.append((matches-len(pairs)*q)/math.sqrt(len(pairs)*q*(1-q)))
    diffmax, translated = [], []
    for alpha in (ah.STD, ah.KRY):
        nums = [alpha.index(x) for x in seq]
        diff = [(b-a)%26 for a,b in zip(nums,nums[1:])]
        diffmax.append(max(Counter(diff).values()))
        translated.append(collisions(list(zip(diff,diff[1:]))))
    row = 0
    for s,e in ah.ROWS:
        rh = Counter(seq[s:e])
        for x,v in h.items():
            expected = (e-s)*v/n
            row += (rh[x]-expected)**2/expected
    return [len(h),collisions(seq),collisions([seq[i:i+2] for i in range(n-1)]),
            collisions([seq[i:i+3] for i in range(n-2)]),lags[0],
            max((lags[d-1]-(n-d)*q)/math.sqrt((n-d)*q*(1-q)) for d in range(1,49)),
            max(periods),*diffmax,*translated,row]


rng = random.Random(141413)
controls = [ah.C,"A"*97,("AB"*49)[:97],(ah.STD*4)[:97]]
controls += ["".join(rng.choices(ah.STD,k=97)) for _ in range(20)]
controls += ["".join(rng.sample(ah.C,len(ah.C))) for _ in range(20)]
for text in controls:
    observed = ah.features(np.array([[ah.STD.index(x) for x in text]]))[0]
    assert np.allclose(observed,scalar(text),rtol=0,atol=1e-9)
orig = scalar(ah.C)
for null in saved["statistics"].values():
    for j,name in enumerate(ah.NAMES):
        assert abs(null[name]["observed"]-orig[j]) < 1e-9
        item = null[name]
        assert abs(item["p_two_sided"]-min(1,2*min(item["p_lower"],item["p_upper"]))) < 1e-12
        assert abs(item["p_bonferroni_24"]-min(1,24*item["p_two_sided"])) < 1e-12
renaming = dict(zip(ah.STD,rng.sample(ah.STD,26)))
renamed = scalar("".join(renaming[x] for x in ah.C))
for j in (0,1,2,3,4,5,6,11):
    assert abs(orig[j]-renamed[j]) < 1e-9
assert sum(saved["raw"]["crib_pair_counts"].values()) == math.comb(24,2)
assert saved["raw"]["crib_pair_counts"] == {"P0C0":253,"P0C1":10,"P1C0":12,"P1C1":1}
assert ah.C.count("E") == 2 and list(ah.P.values()).count("E") == 3
assert len(set(ah.C)) == 26
assert saved["raw"]["block_repeats"]["2"] == [{},{}]
assert all(not x for size in ("4","5") for x in saved["raw"]["block_repeats"][size])
assert [saved["raw"]["period_constraints_1_96"][str(p)] for p in range(24,30)] == [5,3,1,0,0,0]
assert saved["raw"] == ah.raw()
print("PASS: 44 sequences x 12 independent scalar statistics; saved observations,")
print("p-value arithmetic, relabeling invariants, and exact raw/crib records verified.")
