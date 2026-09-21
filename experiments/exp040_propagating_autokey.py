"""EXP-040  Propagating text-autokey with a short primer.

Preregistered in docs/exp040-preregistration.md BEFORE implementation.

Distinct from EXP-008. That experiment treated data-dependent keys as local affine
taps k[i] = a*S[i-L] + b, and its plaintext source returned a value only when the
lagged position was itself inside a crib, so it never propagated and never solved
the recursion. Here a primer of m letters determines ALL 97 plaintext letters, so
the unknowns are the m primer letters and nothing else.

Within residue chain r = i mod m the recursion is affine in one unknown x[r]:

    vigenere          P[r+jm] = alt_sum(C) + (-1)^(j+1) * x[r]
    beaufort          P[r+jm] = x[r] - cum_sum(C)
    variant_beaufort  P[r+jm] = cum_sum(C) + x[r]

so every crib position pins its chain's unknown exactly, and two crib positions in
one chain that disagree are a contradiction. No search, no scoring, no language model.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
ALPHA = {"STD": STD, "KRY": KRY}
ROW_STARTS = (0, 4, 35, 66)

CRIB = {}
for _cr in K4["confirmed_cribs"]:
    assert CT[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch

COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
PRIMER_RANGE = range(1, 25)          # frozen: m >= 25 is undecidable, not a survivor
UNDECIDABLE_RANGE = range(25, 30)


def uncombine(c_idx, k_idx, combiner):
    """Recover the plaintext index from a ciphertext index and a key index."""
    if combiner == "vigenere":
        return (c_idx - k_idx) % 26
    if combiner == "beaufort":
        return (k_idx - c_idx) % 26
    return (c_idx + k_idx) % 26      # variant_beaufort


def combine(p_idx, k_idx, combiner):
    if combiner == "vigenere":
        return (p_idx + k_idx) % 26
    if combiner == "beaufort":
        return (k_idx - p_idx) % 26
    return (p_idx - k_idx) % 26


def chain_positions(start, step, reverse, lo, hi):
    """Indices of one residue chain inside [lo, hi), in recursion order."""
    out, i = [], start
    while lo <= i < hi:
        out.append(i)
        i += -step if reverse else step
    return out


def run_chain(cipher_idx, combiner, positions, x0, relabel):
    """Run the autokey recursion along one chain from primer value x0.

    Exact and uniform: it makes no affine assumption, so it stays correct when the
    key alphabet differs from the plaintext alphabet (which re-indexes the fed-back
    letter and makes the recursion non-affine).
    """
    out, key = {}, x0
    for pos in positions:
        p = uncombine(cipher_idx[pos], key, combiner)
        out[pos] = p
        key = relabel[p] if relabel is not None else p
    return out


def segments_for(row_reset):
    return [(0, 4), (4, 35), (35, 66), (66, 97)] if row_reset else [(0, 97)]


def evaluate(source, combiner, plain_alpha, cipher_alpha, key_alpha, m, reverse, row_reset):
    """Exact consistency decision by per-chain enumeration of the 26 primer values."""
    pidx = {ch: i for i, ch in enumerate(ALPHA[plain_alpha])}
    cidx = {ch: i for i, ch in enumerate(ALPHA[cipher_alpha])}
    cipher_idx = [cidx[ch] for ch in CT]
    kidx = {ch: i for i, ch in enumerate(ALPHA[key_alpha])}
    # re-index a plaintext value through the key alphabet
    relabel = None if key_alpha == plain_alpha else \
        [kidx[ALPHA[plain_alpha][v]] for v in range(26)]

    if source == "ciphertext":
        key_src = [kidx[ch] for ch in CT]
        constraints = 0
        for i, ch in CRIB.items():
            j = i + m if reverse else i - m
            if not (0 <= j < 97):
                continue
            constraints += 1
            if uncombine(cipher_idx[i], key_src[j], combiner) != pidx[ch]:
                return "INFEASIBLE", {"position": i, "constraints": constraints}
        return ("FEASIBLE" if constraints else "NO_CONSTRAINTS"), {"constraints": constraints}

    primer, constraints = {}, 0
    for lo, hi in segments_for(row_reset):
        seeds = range(lo, min(lo + m, hi)) if not reverse else range(max(lo, hi - m), hi)
        for seed in seeds:
            positions = chain_positions(seed, m, reverse, lo, hi)
            pinned = [(p, pidx[CRIB[p]]) for p in positions if p in CRIB]
            if not pinned:
                continue
            constraints += len(pinned) - 1
            good = [x for x in range(26)
                    if all(run_chain(cipher_idx, combiner, positions, x, relabel)[p] == v
                           for p, v in pinned)]
            if not good:
                return "INFEASIBLE", {"chain_seed": seed, "pinned": pinned}
            primer[seed] = good
    if constraints == 0:
        return "NO_CONSTRAINTS", {"constraints": 0}
    return "FEASIBLE", {"constraints": constraints,
                        "primer_options": {k: v for k, v in sorted(primer.items())}}


def reconstruct(combiner, plain_alpha, cipher_alpha, key_alpha, m, reverse, primer, row_reset):
    """Rebuild all 97 plaintext letters from a chosen primer, forward through the rule."""
    pidx_alpha = ALPHA[plain_alpha]
    cidx = {ch: i for i, ch in enumerate(ALPHA[cipher_alpha])}
    cipher_idx = [cidx[ch] for ch in CT]
    kidx = {ch: i for i, ch in enumerate(ALPHA[key_alpha])}
    relabel = None if key_alpha == plain_alpha else \
        [kidx[ALPHA[plain_alpha][v]] for v in range(26)]
    plain = [None] * 97
    for lo, hi in segments_for(row_reset):
        seeds = range(lo, min(lo + m, hi)) if not reverse else range(max(lo, hi - m), hi)
        for seed in seeds:
            if seed not in primer:
                return None
            got = run_chain(cipher_idx, combiner, chain_positions(seed, m, reverse, lo, hi),
                            primer[seed], relabel)
            for pos, v in got.items():
                plain[pos] = v
    if any(v is None for v in plain):
        return None
    return "".join(pidx_alpha[v] for v in plain)


def main():
    global CT
    print("# EXP-040  propagating text-autokey with a short primer")
    print(f"prereg: docs/exp040-preregistration.md")
    print(f"ciphertext length {len(CT)}, known plaintext positions {len(CRIB)}\n")

    # ---------------------------------------------------------------- controls
    print("## Controls")
    ok_pos = ok_adv = False

    # positive control: plant a primer, synthesise a ciphertext, recover it
    plant_m, plant_comb = 5, "vigenere"
    plant_primer = [7, 0, 19, 4, 11]
    plant_plain = [(i * 7 + 3) % 26 for i in range(97)]
    synth = [None] * 97
    for i in range(97):
        k = plant_primer[i] if i < plant_m else plant_plain[i - plant_m]
        synth[i] = combine(plant_plain[i], k, plant_comb)
    synth_ct = "".join(STD[v] for v in synth)
    # re-derive the plaintext from the synthetic ciphertext and the planted primer
    rec, prev_chain = [None] * 97, {}
    for seed in range(plant_m):
        prev = plant_primer[seed]
        for pos in chain_positions(seed, plant_m, False, 0, 97):
            p = uncombine(STD.index(synth_ct[pos]), prev, plant_comb)
            rec[pos] = p
            prev = p
    ok_pos = rec == plant_plain
    print(f"  positive control: planted primer {plant_primer} recovered exactly -> "
          f"{'PASS' if ok_pos else 'FAIL'}")

    # Adversarial control. A corruption must STRADDLE two crib positions in the same
    # chain. A corruption downstream of every crib in its chain is absorbed by the
    # primer -- that is a real property of an autokey, not a bug -- so such a control
    # cannot flip the verdict and would be reported "not counted".
    def chain_consistent(ct_string, cribs, m, combiner):
        ci = [STD.index(c) for c in ct_string]
        for seed in range(m):
            positions = chain_positions(seed, m, False, 0, 97)
            pinned = [(p, cribs[p]) for p in positions if p in cribs]
            if len(pinned) < 2:
                continue
            if not any(all(run_chain(ci, combiner, positions, x, None)[p] == v
                           for p, v in pinned) for x in range(26)):
                return False
        return True

    fake_crib = {i: plant_plain[i] for i in sorted(CRIB)}
    clean_ok = chain_consistent(synth_ct, fake_crib, plant_m, plant_comb)
    # position 41 lies in chain 41 % 5 == 1, strictly between crib positions 31 and 66
    straddle = 41
    assert straddle % plant_m == 21 % plant_m and 33 < straddle < 63
    bad = list(synth_ct)
    bad[straddle] = STD[(STD.index(bad[straddle]) + 13) % 26]
    corrupt_ok = chain_consistent("".join(bad), fake_crib, plant_m, plant_comb)
    ok_adv = clean_ok and not corrupt_ok
    print(f"  adversarial control: corruption at {straddle} straddles crib positions in its "
          f"chain")
    print(f"    clean consistent={clean_ok}, corrupted consistent={corrupt_ok} -> "
          f"{'PASS' if ok_adv else 'NOT COUNTED'}")

    # Recorded property, not a defect: a corruption downstream of every crib in its
    # chain IS absorbed by the primer, so it cannot flip the verdict.
    bad2 = list(synth_ct)
    bad2[91] = STD[(STD.index(bad2[91]) + 7) % 26]
    absorbed = chain_consistent("".join(bad2), fake_crib, plant_m, plant_comb)
    print(f"    downstream-only corruption at 91 absorbed by primer: {absorbed} "
          f"(expected True; recorded, not counted as a control)")

    # Non-vacuity control. Plant an autokey message whose plaintext carries the REAL
    # cribs at the REAL positions, then run the actual decision procedure against it.
    # If this recovers the primer and the full plaintext, a true autokey K4 would have
    # been detected, so a negative on the real ciphertext is informative, not empty.
    import random as _random
    _random.seed(20260921)
    nv_plain = [_random.randrange(26) for _ in range(97)]
    for _i, _ch in CRIB.items():
        nv_plain[_i] = STD.index(_ch)
    nv_m, nv_comb = 7, "vigenere"
    nv_primer = [STD.index(c) for c in "KRYPTOS"[:nv_m]]
    nv_ct = [None] * 97
    for seed in range(nv_m):
        prev = nv_primer[seed]
        for pos in chain_positions(seed, nv_m, False, 0, 97):
            nv_ct[pos] = combine(nv_plain[pos], prev, nv_comb)
            prev = nv_plain[pos]
    _real_ct = CT
    CT = "".join(STD[v] for v in nv_ct)
    nv_st, nv_det = evaluate("plaintext", nv_comb, "STD", "STD", "STD", nv_m, False, False)
    nv_primer_rec = {k: v[0] for k, v in nv_det.get("primer_options", {}).items()}
    nv_full = reconstruct(nv_comb, "STD", "STD", "STD", nv_m, False, nv_primer_rec, False)
    CT = _real_ct
    ok_nonvac = (nv_st == "FEASIBLE"
                 and all(nv_primer_rec.get(k) == nv_primer[k] for k in range(nv_m))
                 and nv_full == "".join(STD[v] for v in nv_plain))
    print(f"  non-vacuity control: planted autokey carrying the real cribs -> {nv_st}, "
          f"primer and full plaintext recovered exactly -> "
          f"{'PASS' if ok_nonvac else 'FAIL'}")
    print(f"    ({nv_det.get('constraints')} constraints exercised; a true autokey K4 "
          f"would have been detected)")

    if not (ok_pos and ok_adv and ok_nonvac):
        print("\nCONTROLS FAILED - results not reported")
        return 1
    print()

    # ---------------------------------------------------------------- the sweep
    print("## Sweep (exact consistency decisions, no search)")
    results, feasible = [], []
    cases = 0
    for source in ("plaintext", "ciphertext"):
        for reverse in (False, True):
            for combiner in COMBINERS:
                for pa in ("STD", "KRY"):
                    for ca in ("STD", "KRY"):
                        for ka in ("STD", "KRY"):
                            for m in PRIMER_RANGE:
                                for row_reset in ((False, True) if m <= 3 else (False,)):
                                    cases += 1
                                    st, det = evaluate(source, combiner, pa, ca, ka,
                                                       m, reverse, row_reset)
                                    row = dict(source=source, reverse=reverse,
                                               combiner=combiner, plain_alpha=pa,
                                               cipher_alpha=ca, key_alpha=ka, m=m,
                                               row_reset=row_reset, status=st, detail=det)
                                    results.append(row)
                                    if st == "FEASIBLE":
                                        feasible.append(row)
    tally = {}
    for r in results:
        tally[r["status"]] = tally.get(r["status"], 0) + 1
    print(f"  configurations decided : {cases:,}")
    for k in sorted(tally):
        print(f"    {k:<16} {tally[k]:>6}")

    print(f"\n  FEASIBLE configurations: {len(feasible)}")
    for r in feasible[:20]:
        print(f"    {r}")

    # ------------------------------------------------ undecidable range, reported
    print("\n## Declared-undecidable range (m >= 25), reported, never counted as survivors")
    POS = sorted(CRIB)
    for m in UNDECIDABLE_RANGE:
        occ = len({i % m for i in POS})
        print(f"    m={m}: {24 - occ} constraints -> UNDECIDABLE WITH PRESENT CRIB GEOMETRY")

    out = {"experiment": "EXP-040",
           "prereg": "docs/exp040-preregistration.md",
           "cases": cases, "tally": tally,
           "feasible": feasible,
           "controls": {"positive": ok_pos, "adversarial": ok_adv,
                        "non_vacuity": ok_nonvac}}
    os.makedirs(os.path.join(ROOT, "results", "exp040"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "results", "exp040", "summary.json"), "w"),
              indent=2, sort_keys=True, default=str)
    print(f"\n  wrote results/exp040/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
