"""Independent verification of the K3 permutation facts used to motivate EXP-043.

This verifier is intentionally separate from experiments/exp043_k3_derived_sandwich.py
and audit/verify_exp043.py.  It does NOT claim primary-source verification of the K3
plaintext transcription; data/mask_sources.json currently marks that plaintext
verified=false.  Instead it answers the narrower reproducibility question:

Given the repository's declared K3 plaintext and Grade-A cipher-side transcription,
does a fixed, explicit double-rotation route reproduce the K3 ciphertext exactly, and
does the resulting permutation have the structural properties cited by EXP-043?

Route checked:
  1. write plaintext row-major into 8 x 42;
  2. read columns left-to-right, each bottom-to-top;
  3. write that stream row-major into 24 x 14;
  4. read columns left-to-right, each bottom-to-top.

No K4 crib data is read.
"""
import collections
import hashlib
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = json.load(open(os.path.join(ROOT, "data", "cipher_side_rows.json")))
MASK = json.load(open(os.path.join(ROOT, "data", "mask_sources.json")))

fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


def route(seq, rows, cols):
    """Write row-major; read columns L->R, each bottom->top."""
    assert len(seq) == rows * cols
    return [seq[r * cols + c] for c in range(cols) for r in range(rows - 1, -1, -1)]


def cycle_lengths(pi):
    seen = set()
    out = []
    for start in range(len(pi)):
        if start in seen:
            continue
        cur = start
        n = 0
        while cur not in seen:
            seen.add(cur)
            n += 1
            cur = pi[cur]
        out.append(n)
    return sorted(out, reverse=True)


sources = {s["id"]: s for s in MASK["sources"]}
p = sources["K3_plaintext"]
plain = p["text"]
check("K3 plaintext provenance remains explicitly non-primary-frozen", p["verified"] is False)
check("declared K3 plaintext length is 336", len(plain) == 336)

# K3 is rows 15..25 up to (but not including) row-25 '?'.
row_stream = "".join(ROWS["rows"][str(i)] for i in range(15, 26))
cipher = row_stream[:row_stream.index("?")]
check("cipher-side K3 length is 336", len(cipher) == 336)
check("plaintext/ciphertext multisets match", collections.Counter(plain) == collections.Counter(cipher))

stage1 = route(list(plain), 8, 42)
out = route(stage1, 24, 14)
check("8x42 -> 24x14 double rotation reproduces K3 exactly", "".join(out) == cipher)

# Derive the exact plaintext-index -> ciphertext-position permutation using index tokens,
# so repeated letters cannot make the mapping ambiguous.
idx = list(range(336))
order = route(route(idx, 8, 42), 24, 14)
pi = [None] * 336
for cpos, ppos in enumerate(order):
    pi[ppos] = cpos

check("derived map is a permutation of 0..335", sorted(pi) == list(range(336)))
diffs = {(pi[i + 1] - pi[i]) % 336 for i in range(335)}
check("successive plaintext positions move by only 191 or 192 mod 336", diffs == {191, 192})
cycles = cycle_lengths(pi)
check("cycle type is exactly 168 + 168", cycles == [168, 168])
check("permutation order is 168", math.lcm(*cycles) == 168)
check("permutation is not an involution", any(pi[pi[i]] != i for i in range(336)))

perm_sha = hashlib.sha256(",".join(map(str, pi)).encode()).hexdigest()
check("permutation SHA-256 matches frozen certificate",
      perm_sha == "c28c37b7c62aa873e60fab9566b76c01e7a2851cc15d9672bc5b6fa4167e01e4")

print()
print("Permutation SHA-256:", perm_sha)
print("Provenance caveat: this verifies the derivation from the repository's declared K3")
print("plaintext; it does not upgrade data/mask_sources.json K3_plaintext verified=false.")
print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
