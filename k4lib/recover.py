"""Method recovery from a candidate plaintext.

Reporting around the 2025 archive sale distinguishes the *recovered text* from
the *decryption method*: knowing what K4 says would not by itself reveal how it
was enciphered. That inverts the problem. Given any candidate 97-character
plaintext, the key indices at all 97 positions become forced under each
convention, and the question is no longer "what is the plaintext" but "does the
forced keystream have structure".

`diagnose` runs every structure probe against a full forced keystream and is the
single entry point for testing a candidate plaintext from any source.
"""

from .analysis import (period_consistency, affine_index_fits, index_of_coincidence,
                       first_difference, value_range_required)
from .conventions import all_conventions
from .alphabets import ALPHABETS


def linear_recurrence_fits(ks, order, max_report=4):
    """c with k[i] = sum_j c[j]*k[i-j-1] mod 26 for all i >= order."""
    n = len(ks)
    if n <= order:
        return []
    out = []
    def rec(prefix):
        if len(prefix) == order:
            if all(sum(prefix[j] * ks[i - j - 1] for j in range(order)) % 26 == ks[i]
                   for i in range(order, n)):
                out.append(tuple(prefix))
            return
        for c in range(26):
            # prune on the first position this coefficient can decide
            rec(prefix + [c])
    rec([])
    return out[:max_report]


def diagnose(plaintext, ciphertext, conventions=None, max_period=49):
    """[(convention, findings dict)] for a candidate full plaintext."""
    assert len(plaintext) == len(ciphertext), "length mismatch"
    conventions = conventions or all_conventions()
    report = []
    for cv in conventions:
        ks = [cv.key_index(p, c) for p, c in zip(plaintext, ciphertext)]
        sparse = dict(enumerate(ks))
        periods = []
        for p in range(1, max_period):
            ok, n = period_consistency(sparse, p)
            if ok and n > 0:
                periods.append(p)
        lo, hi, vals = value_range_required(sparse)
        report.append((cv, {
            "keystream": ks,
            "key_std": "".join(ALPHABETS["STD"][k] for k in ks),
            "key_kry": "".join(ALPHABETS["KRY"][k] for k in ks),
            "periods": periods,
            "affine_fits": affine_index_fits(sparse),
            "lin_rec_order1": linear_recurrence_fits(ks, 1),
            "lin_rec_order2": linear_recurrence_fits(ks, 2),
            "range": (lo, hi, len(vals)),
            "key_ioc": index_of_coincidence("".join(ALPHABETS["STD"][k] for k in ks)),
            "first_diff_constant": len(set(first_difference(ks))) == 1,
        }))
    return report


def summarise(report, top=None):
    lines = []
    for cv, f in report:
        verdict = []
        if f["periods"]:
            verdict.append(f"PERIODIC {f['periods'][:4]}")
        if f["affine_fits"]:
            verdict.append(f"AFFINE {f['affine_fits'][:2]}")
        if f["lin_rec_order1"]:
            verdict.append(f"LINREC1 {f['lin_rec_order1']}")
        if f["lin_rec_order2"]:
            verdict.append(f"LINREC2 {f['lin_rec_order2'][:2]}")
        if f["key_ioc"] > 0.055:
            verdict.append(f"KEY_IOC {f['key_ioc']:.4f} (text-like)")
        if verdict:
            lines.append((cv.name, "; ".join(verdict), f["key_std"]))
    return lines if top is None else lines[:top]
