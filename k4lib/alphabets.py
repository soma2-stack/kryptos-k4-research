"""Alphabets and index conventions used across K4 experiments."""

STANDARD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRYPTOS = "KRYPTOSABCDEFGHIJLMNQUVWXZ"

ALPHABETS = {"STD": STANDARD, "KRY": KRYPTOS}


def index_map(alphabet):
    """Map letter -> position in `alphabet`."""
    return {ch: i for i, ch in enumerate(alphabet)}


def pos(alphabet, letter):
    return index_map(alphabet)[letter]


def vigenere_tableau(alphabet=KRYPTOS, row_alphabet=None):
    """Rows of a Vigenere tableau.

    Row r is `alphabet` rotated left by r. `row_alphabet` labels the rows; the
    Kryptos sculpture's tableau labels rows with the keyed alphabet itself.
    """
    row_alphabet = row_alphabet or alphabet
    return {row_alphabet[r]: alphabet[r:] + alphabet[:r] for r in range(26)}
