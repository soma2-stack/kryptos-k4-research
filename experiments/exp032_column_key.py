"""EXP-032  Key as an arbitrary function of engraving column.

Preregistered in docs/exp032-033-preregistration.md before implementation.

Model: k[i] = f(col(i)), f : {1..31} -> Z26 ANY function, C[i] = conv(P[i], k[i]).
f is never enumerated. All 26^31 functions are decided exactly by consistency: if two
crib positions sharing a column force different key values, no function can exist; if
none do, a consistent partial map extends to a full function. The key alphabet is
absorbed by an arbitrary f and is therefore not a parameter, so the search is 12 cases,
one per committed shift convention.

The corrected NSA geometry (DOCID 4145037) supplies col(i). This experiment also
verifies programmatically the bound stated in the preregistration: because no crib lies
at K4 positions 0-3, the corrected column map and the old isolated-OBKR map agree on
every crib, so the geometry correction cannot change this class of result.
"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions

k4 = load()
CT = k4.ciphertext
cribs = k4.crib_positions()                      # [(pos, plaintext, ciphertext)]
conventions = all_conventions()

# ---------------------------------------------------------------- geometry (grade A)
ROWS = ((25, 0, 4, 28), (26, 4, 35, 1), (27, 35, 66, 1), (28, 66, 97, 1))


def row_col(i):
    for row, lo, hi, first_col in ROWS:
        if lo <= i < hi:
            return row, first_col + (i - lo)
    raise IndexError(i)


def col_old_isolated(i):
    """The withdrawn model: OBKR as its own row occupying columns 1-4."""
    return (1 + i) if i < 4 else row_col(i)[1]


print("# EXP-032 key as an arbitrary function of engraving column")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## Geometry cross-check against the ciphertext (not taken on trust)")
NSA = {25: "ECDMRIPFEIMEHNLSSTTRTVDOHW?OBKR", 26: "UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO",
       27: "TWTQSJQSSEKZZWATJKLUDIAWINFBNYP", 28: "VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"}
checks = [("row 25 is 31 chars ending in OBKR", len(NSA[25]) == 31 and NSA[25].endswith("OBKR")),
          ("row 26 == K4[4:35]", NSA[26] == CT[4:35]),
          ("row 27 == K4[35:66]", NSA[27] == CT[35:66]),
          ("row 28 == K4[66:97]", NSA[28] == CT[66:97]),
          ("cipher side 32 + 27*31 == 869", 32 + 27 * 31 == 869)]
for name, ok in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
assert all(ok for _, ok in checks)
print()

print("## What the correction can and cannot buy, verified not asserted")
positions = [i for i, _, _ in cribs]
same = all(row_col(i)[1] == col_old_isolated(i) for i in positions)
print(f"   cribs at K4 positions 0-3                  : {sum(1 for i in positions if i < 4)}")
print(f"   corrected and old column maps agree on all cribs : {same}")
print("   So the OBKR correction cannot change any crib-constrained position- or")
print("   column-indexed result. It matters only for models using the characters")
print("   physically ABOVE K4 (blocked: see docs/external-evidence-requests.md), for")
print("   transpositions on the ragged engraving grid (EXP-033 F3), or for claims")
print("   about positions 0-3, which carry no crib.")
print()

by_col = collections.defaultdict(list)
for i in positions:
    by_col[row_col(i)[1]].append(i)
collisions = {c: v for c, v in sorted(by_col.items()) if len(v) > 1}
print("## Constraint inventory (fixed before any verdict)")
print(f"   distinct crib columns : {len(by_col)} over {len(positions)} crib positions")
print(f"   column collisions     : {collisions}")
nconstraints = sum(len(v) - 1 for v in by_col.values())
print(f"   independent constraints per case : {nconstraints}")
print(f"   chance survival per case         : 26^-{nconstraints} = {26.0**-nconstraints:.3e}")
print(f"   expected chance-feasible cases   : {12 * 26.0**-nconstraints:.3f}")
print()
print("   Also recorded, per the preregistration: a key that is a function of")
print("   (row, column) is UNTESTABLE here - every crib position has a unique")
print("   (row, column) pair, so the crib set yields zero constraints. That vacuity")
print("   is reported, not hidden, and no such model is claimed eliminated.")
print()


def decide(conv, ct=CT, crib_list=None):
    """Exact feasibility of k[i] = f(col(i)) under one convention."""
    crib_list = crib_list if crib_list is not None else [(i, p) for i, p, _ in cribs]
    forced = {}
    for i, p in crib_list:
        col = row_col(i)[1]
        k = conv.key_index(p, ct[i])
        if col in forced and forced[col][0] != k:
            return False, {"column": col, "positions": [forced[col][1], i],
                           "key_values": [forced[col][0], k]}, forced
        forced.setdefault(col, (k, i))
    return True, None, forced


# ---------------------------------------------------------------- controls
print("## Controls")
import random
rng = random.Random(20260912)
ctrl = {"planted_pass": 0, "planted_total": 0, "adversarial_pass": 0, "adversarial_total": 0}
for conv in conventions:
    f = {c: rng.randrange(26) for c in range(1, 32)}
    PT = ["X"] * 97
    for i, p, _ in cribs:
        PT[i] = p
    synth = "".join(conv.encrypt_letter(PT[i], f[row_col(i)[1]]) for i in range(97))
    ok, witness, forced = decide(conv, ct=synth)
    recovered = all(v[0] == f[c] for c, v in forced.items())
    ctrl["planted_total"] += 1
    ctrl["planted_pass"] += bool(ok and recovered)
    # adversarial: corrupt one crib ciphertext letter that participates in a collision
    bad = list(synth)
    victim = collisions[29][1]
    bad[victim] = chr((ord(bad[victim]) - 65 + 13) % 26 + 65)
    ok2, _, _ = decide(conv, ct="".join(bad))
    ctrl["adversarial_total"] += 1
    ctrl["adversarial_pass"] += (not ok2)
print(f"   planted positives  : {ctrl['planted_pass']}/{ctrl['planted_total']} detected and f recovered")
print(f"   adversarial negatives : {ctrl['adversarial_pass']}/{ctrl['adversarial_total']} correctly rejected")
assert ctrl["planted_pass"] == ctrl["planted_total"]
assert ctrl["adversarial_pass"] == ctrl["adversarial_total"]
print()

# ---------------------------------------------------------------- the real test
print("## THE REAL TEST")
rows_out, feasible = [], []
for conv in conventions:
    ok, witness, _ = decide(conv)
    rows_out.append({"convention": conv.name, "feasible": ok, "witness": witness})
    if ok:
        feasible.append(conv.name)
    w = "" if ok else (f"col {witness['column']} positions {witness['positions']}"
                       f" demand key {witness['key_values'][0]} and {witness['key_values'][1]}")
    print(f"   {'FEASIBLE' if ok else 'CONTRADICTION'}  {conv.name:<34} {w}")
print()
print(f"   cases: 12   feasible: {len(feasible)}   contradictions: {12 - len(feasible)}")
print()
if feasible:
    print("## RESULT: NOT ELIMINATED for " + ", ".join(feasible))
    print("   Recorded as a surviving case, not as a solution: 2 constraints is weak")
    print("   evidence and f still has 31 free values. No tuning follows.")
else:
    print("## RESULT: NEGATIVE - every convention contradicts")
    print("   No function of engraving column alone can produce K4 from a plaintext")
    print("   carrying the public cribs, under any of the 12 committed conventions.")
    print("   This eliminates an infinite family (all 26^31 functions x 12 conventions)")
    print("   from 2 exact constraints, and is strictly stronger in f than EXP-006's")
    print("   periodic and line-reset eliminations, while strictly narrower in indexing.")
print()
print("## Scope")
print("   Conditional on the public cribs and the 12 committed conventions. Says nothing")
print("   about f(row, col) (vacuous here), non-shift combiners, transposition-composed")
print("   models, or any key indexed on anything but the engraving column.")

out = os.path.join(REPO_ROOT, "results", "exp032", "summary.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as fh:
    json.dump({"experiment": "EXP-032", "ciphertext_sha256": k4.sha256,
               "model": "k[i] = f(col(i)), f any function {1..31}->Z26",
               "geometry": "NSA DOCID 4145037, verified against ciphertext",
               "crib_positions": positions, "column_collisions": collisions,
               "constraints_per_case": nconstraints, "cases": 12,
               "feasible": feasible, "controls": ctrl, "results": rows_out}, fh, indent=1)
print(f"\n   wrote {os.path.relpath(out, REPO_ROOT)}")
