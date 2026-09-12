"""Loading and integrity-checking of data/k4.json."""

import hashlib
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4_PATH = os.path.join(REPO_ROOT, "data", "k4.json")

# Recorded on 2026-09-12 from data/k4.json as committed. Any change to the
# ciphertext must change this constant in the same commit.
CIPHERTEXT_SHA256 = "eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab"


class K4:
    """The fixed inputs, with zero-based half-open crib spans."""

    def __init__(self, path=K4_PATH):
        with open(path) as fh:
            raw = json.load(fh)
        self.raw = raw
        self.ciphertext = raw["ciphertext"]
        self.kryptos_alphabet = raw["kryptos_alphabet"]
        self.cribs = raw["confirmed_cribs"]

    @property
    def sha256(self):
        return hashlib.sha256(self.ciphertext.encode()).hexdigest()

    def verify(self):
        """Return a list of (check, ok, detail). Empty failures == clean load."""
        out = []
        c = self.ciphertext
        out.append(("length_97", len(c) == 97, f"len={len(c)}"))
        out.append(("declared_length", len(c) == self.raw["length"], str(self.raw["length"])))
        out.append(("alphabetic", c.isalpha() and c.isupper(), "A-Z uppercase only"))
        out.append(("sha256", self.sha256 == CIPHERTEXT_SHA256, self.sha256))
        out.append(
            ("kryptos_alphabet_is_permutation",
             sorted(self.kryptos_alphabet) == list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
             self.kryptos_alphabet))
        for crib in self.cribs:
            p, s, e = crib["plaintext"], crib["start"], crib["end"]
            seg = c[s:e]
            out.append((f"crib_{p}_span", len(seg) == len(p) == e - s, f"{s}:{e}"))
            out.append((f"crib_{p}_segment", seg == crib["ciphertext_segment"], seg))
        spans = [(cr["start"], cr["end"]) for cr in self.cribs]
        overlap = any(a[0] < b[1] and b[0] < a[1] for i, a in enumerate(spans) for b in spans[i + 1:])
        out.append(("cribs_disjoint", not overlap, str(spans)))
        return out

    def crib_positions(self):
        """[(index, plaintext_letter, ciphertext_letter)] over all confirmed cribs."""
        out = []
        for crib in self.cribs:
            for k, ch in enumerate(crib["plaintext"]):
                i = crib["start"] + k
                out.append((i, ch, self.ciphertext[i]))
        return out


def load(path=K4_PATH):
    return K4(path)
