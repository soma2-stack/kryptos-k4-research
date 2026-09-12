"""Generalised shift-cipher conventions.

Every family here is a *shift* family: a plaintext letter P at position i and a
key index k[i] determine the ciphertext letter C. What varies is (a) which
alphabet indexes the plaintext, (b) which alphabet indexes the ciphertext, and
(c) how the key combines with the plaintext.

    vigenere          c = (p + k) mod 26
    beaufort          c = (k - p) mod 26
    variant_beaufort  c = (p - k) mod 26

Inverted for cryptanalysis, the *derived key* at a known-plaintext position is:

    vigenere          k = (c - p) mod 26
    beaufort          k = (c + p) mod 26
    variant_beaufort  k = (p - c) mod 26

`plain_alpha`/`cipher_alpha` select the indexing alphabet on each side, which is
what distinguishes a plain Vigenere from the Quagmire-style constructions used
in K1 and K2 (keyed KRYPTOS alphabet on one or both sides).
"""

from .alphabets import ALPHABETS, index_map

COMBINERS = ("vigenere", "beaufort", "variant_beaufort")


def derive_key_index(p_idx, c_idx, combiner):
    if combiner == "vigenere":
        return (c_idx - p_idx) % 26
    if combiner == "beaufort":
        return (c_idx + p_idx) % 26
    if combiner == "variant_beaufort":
        return (p_idx - c_idx) % 26
    raise ValueError(combiner)


def apply_key_index(p_idx, k_idx, combiner):
    if combiner == "vigenere":
        return (p_idx + k_idx) % 26
    if combiner == "beaufort":
        return (k_idx - p_idx) % 26
    if combiner == "variant_beaufort":
        return (p_idx - k_idx) % 26
    raise ValueError(combiner)


class Convention:
    """One (plain alphabet, cipher alphabet, combiner) triple."""

    def __init__(self, plain_alpha="STD", cipher_alpha="STD", combiner="vigenere"):
        self.plain_alpha = plain_alpha
        self.cipher_alpha = cipher_alpha
        self.combiner = combiner
        self._pi = index_map(ALPHABETS[plain_alpha])
        self._ci = index_map(ALPHABETS[cipher_alpha])
        self._cA = ALPHABETS[cipher_alpha]
        self._pA = ALPHABETS[plain_alpha]

    name = property(lambda self: f"{self.combiner}/P={self.plain_alpha}/C={self.cipher_alpha}")

    def __repr__(self):
        return f"<Convention {self.name}>"

    def key_index(self, p_letter, c_letter):
        return derive_key_index(self._pi[p_letter], self._ci[c_letter], self.combiner)

    def encrypt_letter(self, p_letter, k_idx):
        return self._cA[apply_key_index(self._pi[p_letter], k_idx, self.combiner)]

    def decrypt_letter(self, c_letter, k_idx):
        c = self._ci[c_letter]
        if self.combiner == "vigenere":
            p = (c - k_idx) % 26
        elif self.combiner == "beaufort":
            p = (k_idx - c) % 26
        else:
            p = (c + k_idx) % 26
        return self._pA[p]

    def decrypt(self, ciphertext, key_indices):
        return "".join(self.decrypt_letter(c, k) for c, k in zip(ciphertext, key_indices))

    def derive_keystream(self, pairs):
        """pairs: iterable of (plaintext_letter, ciphertext_letter)."""
        return [self.key_index(p, c) for p, c in pairs]

    def key_letters(self, key_indices, alphabet="STD"):
        A = ALPHABETS[alphabet]
        return "".join(A[k] for k in key_indices)


def all_conventions():
    return [Convention(p, c, m)
            for m in COMBINERS
            for p in ("STD", "KRY")
            for c in ("STD", "KRY")]
