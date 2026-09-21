"""EXP-034  Text-dependent keys as ARBITRARY functions of one source letter.

Preregistered in docs/exp034-preregistration.md before implementation.

Model:  k[i] = f(S[i - L]),  C[i] = conv(P[i], k[i]),  f : A-Z -> Z26 ANY function.

f is never enumerated; all 26^26 functions are decided exactly by consistency. EXP-008
eliminated this family only in parameter-linear form (k = a*S[i-L] + b and two-tap and
drift variants). This generalises it the way EXP-030 generalised EXP-029.

Cases whose usable constraint count is <= 3 are reported UNDECIDED and are excluded from
the elimination, per the preregistration; that threshold was fixed before any result.
"""
import sys, os, json, gzip, collections, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions

k4 = load()
CT = k4.ciphertext
cribs = k4.crib_positions()
CRIB = {i: p for i, p, _ in cribs}
conventions = all_conventions()
N = 97
MIN_CONSTRAINTS = 4                     # preregistered: <= 3 is UNDECIDED


def sources():
    out = {"ct_fwd": [CT[j] for j in range(N)],
           "ct_rev": [CT[N - 1 - j] for j in range(N)]}
    for m in (2, 3, 5, 7, 11):
        out[f"ct_dec_{m}"] = [CT[(m * j) % N] for j in range(N)]
    out["pt"] = [CRIB.get(j) for j in range(N)]        # None where unknown
    return out


SRC = sources()
print("# EXP-034 text-dependent keys as arbitrary functions of one source letter")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Declared space")
print(f"   sources {len(SRC)}: {', '.join(sorted(SRC))}")
print(f"   lags 1-96, conventions {len(conventions)}  ->  "
      f"{len(SRC) * 96 * len(conventions):,} cases")
print(f"   f is not enumerated; all 26^26 functions decided exactly by consistency")
print(f"   key alphabet is absorbed by an arbitrary f and is NOT a parameter")
print(f"   preregistered threshold: cases with <= {MIN_CONSTRAINTS - 1} usable")
print(f"   constraints are UNDECIDED and excluded from the elimination\n")


def decide(src, lag, conv, ct=CT, crib=None):
    """Exact feasibility. Returns (verdict, constraints, witness, forced map).

    The usable-constraint count is a property of (source, lag) alone and must NOT
    depend on the verdict, so every constrained position is visited before any verdict
    is formed. An earlier draft returned on the first contradiction, which made
    contradicting cases report a small constraint count and be misfiled as UNDECIDED.
    """
    crib = crib if crib is not None else CRIB
    seen = {}
    constraints, witness = 0, None
    for i in sorted(crib):
        j = i - lag
        if j < 0:
            continue
        s = src[j]
        if s is None:
            continue
        k = conv.key_index(crib[i], ct[i])
        if s in seen:
            constraints += 1
            if seen[s][0] != k and witness is None:
                witness = {"source_letter": s, "positions": [seen[s][1], i],
                           "key_values": [seen[s][0], k]}
        else:
            seen[s] = (k, i)
    verdict = "CONTRADICTION" if witness is not None else "FEASIBLE"
    return verdict, constraints, witness, seen


# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(4145037)
ctrl = collections.Counter()
for name in sorted(SRC):
    for lag in (1, 3, 7, 29, 61):
        for conv in (conventions[0], conventions[5], conventions[9]):
            f = {chr(65 + t): rng.randrange(26) for t in range(26)}
            if name == "pt" and rng.random() < 0.5:
                for ch in "AEIOU":                       # deliberately non-injective
                    f[ch] = 0
            PT = ["X"] * N
            for i, p in CRIB.items():
                PT[i] = p
            # synthesise with independent arithmetic, honouring the source definition
            src = SRC[name] if name != "pt" else [PT[j] for j in range(N)]
            synth = list(CT)
            for i in range(N):
                j = i - lag
                if j < 0 or src[j] is None:
                    continue
                synth[i] = conv.encrypt_letter(PT[i], f[src[j]])
            synth = "".join(synth)
            verdict, nc, _, forced = decide(SRC[name] if name != "pt" else
                                            [CRIB.get(j) for j in range(N)],
                                            lag, conv, ct=synth)
            ok = verdict == "FEASIBLE" and all(v[0] == f[s] for s, v in forced.items())
            ctrl["planted_total"] += 1
            ctrl["planted_pass"] += bool(ok)
            # adversarial: corrupt a position that actually PARTICIPATES in a
            # constraint, otherwise the control tests nothing about the detector
            s_used = (SRC[name] if name != "pt" else [CRIB.get(j) for j in range(N)])
            buckets = collections.defaultdict(list)
            for i in sorted(CRIB):
                j = i - lag
                if j >= 0 and s_used[j] is not None:
                    buckets[s_used[j]].append(i)
            shared = [v for v in buckets.values() if len(v) > 1]
            if shared:
                victim = shared[0][-1]
                bad = list(synth)
                bad[victim] = chr((ord(bad[victim]) - 65 + 7) % 26 + 65)
                v2, _, _, _ = decide(s_used, lag, conv, ct="".join(bad))
                ctrl["adv_total"] += 1
                ctrl["adv_pass"] += (v2 == "CONTRADICTION")
print(f"   planted positives     : {ctrl['planted_pass']}/{ctrl['planted_total']}"
      " detected and f recovered on every constrained letter")
print(f"   adversarial corruption: {ctrl['adv_pass']}/{ctrl['adv_total']} flipped to contradiction")
assert ctrl["planted_pass"] == ctrl["planted_total"], "positive control failed"
print()

# ---------------------------------------------------------------- the real test
print("## THE REAL TEST")
rows, feasible, undecided, contra = [], [], [], 0
cdist = collections.Counter()
for name in sorted(SRC):
    src = SRC[name]
    for lag in range(1, 97):
        for conv in conventions:
            verdict, nc, witness, _ = decide(src, lag, conv)
            cdist[nc] += 1
            rec = {"source": name, "lag": lag, "convention": conv.name,
                   "constraints": nc, "verdict": verdict}
            if nc < MIN_CONSTRAINTS:
                rec["verdict"] = "UNDECIDED"
                undecided.append(rec)
            elif verdict == "FEASIBLE":
                feasible.append(rec)
            else:
                contra += 1
            rows.append(rec)
total = len(rows)
decided = total - len(undecided)
print(f"   cases                     : {total:,}")
print(f"   decided (>= {MIN_CONSTRAINTS} constraints) : {decided:,}")
print(f"   UNDECIDED (too few)       : {len(undecided):,}")
print(f"   CONTRADICTION             : {contra:,}")
print(f"   FEASIBLE among decided    : {len(feasible)}")
print()
print("   constraint-count distribution over all cases:")
for k in sorted(cdist):
    print(f"      {k:>2} constraints : {cdist[k]:>6,} cases"
          + ("   <- UNDECIDED" if k < MIN_CONSTRAINTS else
             f"   chance survival 26^-{k} = {26.0**-k:.1e}"))
print()
per_source = collections.Counter()
for r in rows:
    if r["verdict"] == "FEASIBLE":
        per_source[r["source"]] += 1
print("## Per source")
for name in sorted(SRC):
    d = sum(1 for r in rows if r["source"] == name and r["verdict"] != "UNDECIDED")
    u = sum(1 for r in rows if r["source"] == name and r["verdict"] == "UNDECIDED")
    print(f"   {name:<10} decided {d:>4}  undecided {u:>4}  feasible {per_source[name]}")
print()

if not feasible:
    print("## RESULT: NEGATIVE on every decided case")
    print("   No key that is an arbitrary function of one declared source letter at one")
    print("   fixed lag can produce K4 from a plaintext carrying the public cribs, under")
    print("   the 12 committed conventions. Because f was decided rather than enumerated,")
    print("   this covers every key alphabet and every non-injective letter map, and it")
    print("   strictly generalises EXP-008, which tested only parameter-linear taps.")
else:
    print("## FEASIBLE CASES RECORDED - not tuned around, not a solution")
    for r in feasible[:20]:
        print(f"   {r}")
    print("   A feasible case fixes f on at most a handful of letters and leaves the")
    print("   other plaintext positions free. Any follow-up needs a new preregistration.")
print()
print("## Scope")
print(f"   {len(undecided):,} cases are UNDECIDED for lack of constraint and are NOT")
print("   claimed eliminated. Untouched: two-tap functions, position-dependent f,")
print("   resets, external running keys, non-shift combiners, and every")
print("   transposition-composed or fractionating architecture.")

out = os.path.join(REPO_ROOT, "results", "exp034")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "summary.json"), "w") as fh:
    json.dump({"experiment": "EXP-034", "ciphertext_sha256": k4.sha256,
               "model": "k[i] = f(S[i-L]), f any A-Z -> Z26, decided exactly",
               "prereg": "docs/exp034-preregistration.md",
               "min_constraints": MIN_CONSTRAINTS,
               "sources": sorted(SRC), "lags": [1, 96], "conventions": len(conventions),
               "cases": total, "decided": decided, "undecided": len(undecided),
               "contradiction": contra, "feasible": feasible,
               "constraint_distribution": dict(cdist), "controls": dict(ctrl),
               "rows_file": "rows.jsonl.gz", "rows_count": len(rows)}, fh, indent=1)
with gzip.open(os.path.join(out, "rows.jsonl.gz"), "wt", compresslevel=9) as fh:
    for _r in rows:
        fh.write(json.dumps(_r, sort_keys=True, separators=(",", ":")) + "\n")
print(f"\n   wrote results/exp034/summary.json")
