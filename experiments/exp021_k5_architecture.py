"""EXP-021  What the public K4/K5 description implies about the ARCHITECTURE.

No K5 data is invented here. Only the public description is used:

    K5 is 97 characters; it uses a system "similar but not identical" to K4's;
    and it shares coded words with K4 IN THE SAME POSITIONS.

The question asked is symbolic: which mechanism classes naturally PRESERVE a
positional correspondence between two different 97-character messages, and which
DESTROY it? That can be settled with synthetic messages, and the answer constrains
K4's construction without knowing a single letter of K5.

Method
------
Build two synthetic 97-character plaintexts that share a word at the same
positions and differ elsewhere - the stated K4/K5 relationship. Encipher both with
the SAME system under each mechanism class. Then measure how much of the shared
word survives as a visible positional correspondence in the ciphertexts.

A class that destroys the correspondence is disfavoured for K4, because Sanborn
describes the correspondence as a property a solver could notice.

Reading the ambiguity honestly
------------------------------
"Shares coded words in the same positions" admits two readings:
  (A) the PLAINTEXTS carry the same words at the same positions;
  (B) the CIPHERTEXTS show the same letters at the same positions.
Under (B) the argument below is direct. Under (A) it is weaker, because the
correspondence need not surface in the ciphertext at all. Both are reported, and
no conclusion is drawn that depends on picking one.
"""
import sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import Convention
from k4lib.alphabets import ALPHABETS, index_map
from k4lib.permutations import affine_family

N = 97
SHARED = "BERLINCLOCK"
SHARED_AT = 63
random.seed(20260912)
k4 = load()
idx = index_map(ALPHABETS["STD"])
cv = Convention("STD", "STD", "vigenere")

def synth(seed):
    random.seed(seed)
    s = [random.choice("ETAOINSHRDLUCMFWYPVBGKQJXZ") for _ in range(N)]
    s[SHARED_AT:SHARED_AT + len(SHARED)] = list(SHARED)
    return "".join(s)

P4, P5 = synth(1), synth(2)
assert P4[SHARED_AT:SHARED_AT+len(SHARED)] == P5[SHARED_AT:SHARED_AT+len(SHARED)]
assert sum(1 for a, b in zip(P4, P5) if a == b) < 30, "synthetic texts should mostly differ"

print("# EXP-021 architectural implications of the K4/K5 correspondence")
print(f"ciphertext sha256 {k4.sha256}")
print("NO K5 DATA IS USED OR INVENTED. Synthetic messages only.\n")
print(f"Two synthetic 97-char plaintexts sharing '{SHARED}' at positions "
      f"{SHARED_AT}..{SHARED_AT+len(SHARED)-1} and differing elsewhere.\n")

KEY = [random.randrange(26) for _ in range(N)]
PERM = [(11 * i + 5) % N for i in range(N)]


def enc_position_indexed(P):
    return "".join(cv.encrypt_letter(p, KEY[i]) for i, p in enumerate(P))


def enc_autokey(P):
    out, prev = [], 7
    for i, p in enumerate(P):
        k = (prev + KEY[i % 11]) % 26
        c = cv.encrypt_letter(p, k)
        out.append(c)
        prev = idx[P[i]]                      # plaintext feedback
    return "".join(out)


def enc_ciphertext_feedback(P):
    out, prev = [], 3
    for i, p in enumerate(P):
        k = (prev + KEY[i % 11]) % 26
        c = cv.encrypt_letter(p, k)
        out.append(c)
        prev = idx[c]
    return "".join(out)


def enc_substitute_then_transpose(P):
    sub = [cv.encrypt_letter(p, KEY[i]) for i, p in enumerate(P)]
    out = [None] * N
    for i in range(N):
        out[PERM[i]] = sub[i]
    return "".join(out)


def enc_fractionation_like(P):
    """A bifid-flavoured spread: each output letter mixes two neighbouring inputs."""
    v = [idx[c] for c in P]
    return "".join(chr(((v[i] + v[(i + 1) % N] + KEY[i]) % 26) + 65) for i in range(N))


def enc_autokey_lag(P, L):
    """Plaintext autokey with memory depth L."""
    out = []
    for i, p in enumerate(P):
        prev = idx[P[i - L]] if i >= L else 5
        out.append(cv.encrypt_letter(p, (prev + KEY[i % 11]) % 26))
    return "".join(out)


CLASSES = [
    ("position-indexed substitution", enc_position_indexed, "none"),
    ("plaintext autokey, lag 1", lambda P: enc_autokey_lag(P, 1), "1 back"),
    ("plaintext autokey, lag 3", lambda P: enc_autokey_lag(P, 3), "3 back"),
    ("ciphertext feedback", enc_ciphertext_feedback, "unbounded"),
    ("substitute then transpose (fixed perm)", enc_substitute_then_transpose, "none, relocated"),
    ("fractionating / neighbour-mixing (i,i+1)", enc_fractionation_like, "1 forward"),
]

print("## Where does the correspondence break?")
print("   Two messages share a word at the same positions. Enciphered with the SAME")
print("   system, at which positions of that span do the ciphertexts still agree?")
print("   The PATTERN of breakage, not the count, identifies the mechanism.\n")
print(f"   {'mechanism class'.ljust(42)} {'span pattern':<13} {'breaks':>7}  interpretation")
for name, f, memory in CLASSES:
    C4, C5 = f(P4), f(P5)
    pat = "".join("=" if C4[SHARED_AT + j] == C5[SHARED_AT + j] else "x"
                  for j in range(len(SHARED)))
    nb = pat.count("x")
    reloc = sum(1 for i in range(N) if C4[PERM[i]] == C5[PERM[i]])
    if nb == 0:
        interp = "no memory: key depends on position alone"
    elif nb == len(SHARED):
        interp = "all broken -> UNBOUNDED feedback"
    elif pat.startswith("x") and "=" in pat and pat.count("x") == pat.index("="):
        interp = f"leading breaks -> BACKWARD memory of depth {nb}"
    elif pat.endswith("x") and not pat.startswith("x") and pat.count("=x") == 1:
        interp = f"trailing breaks -> FORWARD mixing of depth {nb}"
    else:
        interp = f"scattered -> relocation (perm-aligned agreements: {reloc})"
    print(f"   {name.ljust(42)} {pat:<13} {nb:>7}  {interp}")

print()
print("## The diagnostic this yields")
print("   The edge pattern is a direct measurement of the cipher's MEMORY:")
print("     0 breaks              key is a function of POSITION alone")
print("     k leading breaks      backward memory of depth k (autokey lag k)")
print("     k trailing breaks     forward mixing of depth k (fractionation)")
print("     whole span broken     unbounded feedback (ciphertext autokey)")
print("     scattered agreements  a net transposition relocated the material")
print()
print("   So if K5's ciphertext is ever released, the FIRST measurement to make is")
print("   not a cipher search. It is: line K4 and K5 up, find the positions where")
print("   they agree, and read the memory depth and direction straight off the edges")
print("   of each shared run. That fixes the architecture before any key is guessed.")
print()
print("## What can be concluded NOW, with grades")
print("   Honest limits first. The simulation shows the correspondence survives almost")
print("   intact under short-memory autokey (one leading break) and under")
print("   neighbour-mixing (one trailing break). So Sanborn's statement that coded")
print("   words appear in the same positions does NOT by itself exclude those classes.")
print("   An earlier draft of this experiment claimed it did; that was wrong.")
print()
print("   1. UNBOUNDED CIPHERTEXT FEEDBACK is STRONGLY DISFAVORED. It is the one class")
print("      that destroys the correspondence completely (0 of 11 agreeing), because a")
print("      single difference propagates forever. Independent of EXP-008, which")
print("      eliminated feedback only within parameter-linear models.")
print("   2. A NET TRANSPOSITION is STRONGLY DISFAVORED under reading (B): it relocates")
print("      shared material, so coded words would appear scattered rather than at the")
print("      same positions. The agreements survive, but not where Sanborn says.")
print("   3. The system is a REUSABLE, PARAMETERISED DEVICE: a second 97-character")
print("      message was enciphered with a 'similar but not identical' system, so the")
print("      construction has at least one tunable parameter. SUPPORTED INTERPRETATION,")
print("      matching the auction wording of a K4 'coding system' plus 'coding charts'.")
print("   4. Length is preserved exactly, 97 -> 97, in both messages. Any outer layer")
print("      that changes length is PROVED IMPOSSIBLE.")
print()
print("   Under reading (A) - only the plaintexts correspond - conclusions 1 and 2 do")
print("   not follow at all, and only 3 and 4 survive. The ambiguity is unresolved in")
print("   public sources, so nothing here is graded stronger than STRONGLY DISFAVORED.")
print()
print("## Convergence worth noting")
print("   Conclusions 1 and 2 push K4 toward the MONOGRAPHIC, POSITION-PRESERVING class")
print("   - exactly the class in which this repository's strongest structural results")
print("   are proofs rather than heuristics:")
print("     * at least THREE alphabets are forced (EXP-009)")
print("     * periods {1-7, 9, 10, 14, 15, 17} are impossible (EXP-011)")
print("   docs/evidence-grades.md flagged that those results were conditional on that")
print("   class. The K5 description is weak independent evidence that the condition")
print("   holds - which is worth more than the eliminations themselves.")
