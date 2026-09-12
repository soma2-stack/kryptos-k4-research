"""EXP-001  Forced keystreams at the 24 confirmed crib positions.

Hypothesis: none. This is the base artifact every later experiment depends on.
For each of 12 shift conventions it computes the key index that is *forced* at
each crib position, then applies structure probes (period, affine-in-index,
arithmetic progression, required value range) and the crib-conflict census.

No search, no fitting: the outputs are determined by data/k4.json alone.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib import analysis as an

k4 = load()
cribs = k4.crib_positions()
seg = {c["plaintext"]: (c["start"], c["end"]) for c in k4.cribs}

print("# EXP-001 forced crib keystreams")
print(f"ciphertext sha256 {k4.sha256}")
print(f"known positions  {len(cribs)} of 97\n")

scd, spd = an.conflicts(cribs)
print("## Crib conflict census")
print(f"same ciphertext letter, different plaintext: {len(scd)} letters")
for c, v in scd:
    print(f"  C={c}: " + ", ".join(f"pos{i}->{p}" for i, p in v))
print(f"same plaintext letter, different ciphertext: {len(spd)} letters")
for p, v in spd:
    print(f"  P={p}: " + ", ".join(f"pos{i}->{c}" for i, c in v))
print()

rows = []
for cv in all_conventions():
    ks = an.sparse_keystream(cv, cribs)
    lo, hi, vals = an.value_range_required(ks)
    periods = []
    for p in range(1, 49):
        ok, n = an.period_consistency(ks, p)
        if ok and n > 0:
            periods.append((p, n))
    affine = an.affine_index_fits(ks)
    rows.append((cv, ks, lo, hi, vals, periods, affine))

print("## Forced key indices (plaintext position -> key index)")
hdr = "convention".ljust(34) + " " + " ".join(f"{i:>3}" for i, _, _ in cribs)
print(hdr)
for cv, ks, *_ in rows:
    print(cv.name.ljust(34) + " " + " ".join(f"{ks[i]:>3}" for i, _, _ in cribs))
print()

print("## Key letters, split by crib (rendered in STD and KRY)")
for cv, ks, *_ in rows:
    out = []
    for name, (s, e) in seg.items():
        idx = [ks[i] for i in range(s, e)]
        out.append(f"{name}: STD={cv.key_letters(idx,'STD')} KRY={cv.key_letters(idx,'KRY')}")
    print(cv.name.ljust(34) + " " + " | ".join(out))
print()

print("## Structure probes")
for cv, ks, lo, hi, vals, periods, affine in rows:
    ap = []
    for name, (s, e) in seg.items():
        isap, step = an.is_arithmetic([ks[i] for i in range(s, e)])
        ap.append(f"{name}:{'AP step '+str(step) if isap else 'no'}")
    print(f"{cv.name.ljust(34)} range={lo}-{hi} distinct={len(vals)} "
          f"periods<=48 consistent={periods if periods else 'none'} "
          f"affine_fits={len(affine)} {' '.join(ap)}")
print()

print("## First differences of the forced key, per crib")
for cv, ks, *_ in rows:
    out = []
    for name, (s, e) in seg.items():
        out.append(f"{name}={an.first_difference([ks[i] for i in range(s,e)])}")
    print(cv.name.ljust(34) + " " + " ".join(out))
