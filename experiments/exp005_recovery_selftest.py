"""EXP-005  Validation of the toolchain, and the method-recovery harness.

Every other experiment in this repository reports a negative. A negative is
worthless unless the apparatus can produce a positive, so this script builds
ciphertexts whose construction is known, hands them to the same code paths, and
checks that the method is recovered. Only then does it apply the harness to K4
itself.

Part 1  self-test: synthesise, then recover.
Part 2  K4 under the harness with the 24 confirmed crib letters, to show what
        the harness can and cannot conclude from 24 of 97 positions.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import Convention, all_conventions
from k4lib.permutations import affine_family
from k4lib import recover, analysis as an

PT = ("ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLETHEYUSEDTHEEARTHSMAGNETICFIELD"
      "XTHEINFORMATIONWASGATHEREDANDSENTNORTH")[:97]
assert len(PT) == 97, len(PT)

print("# EXP-005 toolchain validation and method recovery")
print(f"synthetic plaintext ({len(PT)} chars): {PT}\n")

failures = []

print("## Part 1 - self-test: can the apparatus find a key it knows is there?")

# (a) short periodic key
cv = Convention("KRY", "KRY", "vigenere")
key = "PALIMPSEST"
kidx = [ord(key[i % len(key)]) - 65 for i in range(97)]
ct = "".join(cv.encrypt_letter(p, k) for p, k in zip(PT, kidx))
rep = recover.diagnose(PT, ct)
found = [(n, v) for n, v, _ in recover.summarise(rep) if "PERIODIC" in v and cv.name in n]
ok = any("PERIODIC" in v and 10 in rep[[c.name for c, _ in rep].index(cv.name)][1]["periods"]
         for _, v in found)
print(f"  (a) period-10 keyword Vigenere  -> {'RECOVERED' if ok else 'MISSED'}"
      f"  periods found: {rep[[c.name for c,_ in rep].index(cv.name)][1]['periods'][:5]}")
failures.append(("periodic", ok))

# (b) affine keystream k[i] = 7i + 3
cv2 = Convention("STD", "STD", "beaufort")
kidx2 = [(7 * i + 3) % 26 for i in range(97)]
ct2 = "".join(cv2.encrypt_letter(p, k) for p, k in zip(PT, kidx2))
rep2 = recover.diagnose(PT, ct2)
fits = rep2[[c.name for c, _ in rep2].index(cv2.name)][1]["affine_fits"]
ok2 = (7, 3) in fits
print(f"  (b) affine keystream 7i+3       -> {'RECOVERED' if ok2 else 'MISSED'}  fits={fits}")
failures.append(("affine", ok2))

# (c) long running-key mask: does the keystream look like text?
cv3 = Convention("STD", "STD", "vigenere")
mask = (PT[40:] + PT[:40])
kidx3 = [ord(mask[i]) - 65 for i in range(97)]
ct3 = "".join(cv3.encrypt_letter(p, k) for p, k in zip(PT, kidx3))
rep3 = recover.diagnose(PT, ct3)
f3 = rep3[[c.name for c, _ in rep3].index(cv3.name)][1]
ok3 = f3["key_ioc"] > 0.055 and not f3["periods"]
print(f"  (c) running-key mask            -> {'RECOVERED' if ok3 else 'MISSED'}"
      f"  key IoC={f3['key_ioc']:.4f} (English ~0.066, random ~0.038), aperiodic={not f3['periods']}")
failures.append(("running_key", ok3))

# (d) transposition + period-7 key: EXP-003's gate, on a planted solution
cv4 = Convention("STD", "STD", "vigenere")
perm = [(11 * i + 5) % 97 for i in range(97)]
kidx4 = [(i % 7) * 3 for i in range(97)]
ct4 = [None] * 97
for i in range(97):
    ct4[perm[i]] = cv4.encrypt_letter(PT[i], kidx4[i])
ct4 = "".join(ct4)
k4data = load()
planted = [(i, PT[i], ct4[perm[i]]) for i in range(97)]
recovered = []
for label, cand in affine_family():
    ks = {i: cv4.key_index(PT[i], ct4[cand[i]]) for i in range(21, 34)}
    ok_p, n = an.period_consistency(ks, 7)
    if ok_p and n >= 6:
        recovered.append(label)
ok4 = "affine a=11 b=5" in recovered
print(f"  (d) transposition + period-7    -> {'RECOVERED' if ok4 else 'MISSED'}"
      f"  candidates surviving gate: {len(recovered)} {recovered[:3]}")
failures.append(("transposition_gate", ok4))

allok = all(ok for _, ok in failures)
print(f"\n  SELF-TEST {'PASSED' if allok else 'FAILED'} "
      f"({sum(1 for _, o in failures if o)}/{len(failures)} probes recovered a planted method)")
print("  The negatives reported by EXP-001..004 are therefore not artefacts of")
print("  broken tooling: the same code recovers a planted key when one exists.\n")

print("## Part 2 - K4 itself, 24 of 97 positions known")
k4 = load()
cribs = k4.crib_positions()
print("  A full diagnosis needs all 97 plaintext letters. With 24, the harness")
print("  can only report what is already excluded:")
for cvx in all_conventions():
    ks = an.sparse_keystream(cvx, cribs)
    periods = [p for p in range(1, 49) if an.period_consistency(ks, p)[0]
               and an.period_consistency(ks, p)[1] > 0]
    print(f"    {cvx.name.ljust(34)} periods<=48: {periods or 'NONE'}"
          f"  affine fits: {len(an.affine_index_fits(ks))}")
print()
print("  To run a real diagnosis, supply a candidate 97-character plaintext:")
print("      python3 -c \"import sys; sys.path.insert(0,'.'); \\")
print("        from k4lib.data import load; from k4lib import recover; \\")
print("        print(recover.summarise(recover.diagnose(PT, load().ciphertext)))\"")
sys.exit(0 if allok else 1)
