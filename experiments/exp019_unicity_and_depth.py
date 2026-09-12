"""EXP-019  Unicity: how long a key can K4 possibly give up, and what K5 would buy.

Why this experiment
-------------------
Sessions 1-3 eliminated short-key and structured-key models on a large scale and
found nothing. That pattern is itself evidence, and it has a quantitative
explanation that no amount of further searching can escape.

A ciphertext can only determine a key whose entropy is smaller than the redundancy
the ciphertext carries. Shannon's unicity distance makes this exact:

    spurious solutions  ~  2^( H(key) - n * D )

with n the ciphertext length and D the redundancy of the plaintext language. For
English, D = log2(26) - H_English, with H_English commonly estimated at 1.0-1.5
bits per letter, so D is about 3.2-3.7.

K4 has n = 97. That is a hard ceiling on how long a key can be recovered from it,
and the ceiling is low.

The 24 crib letters raise the ceiling, and a second message in depth - which is
exactly what K5 is - collapses the problem entirely. Both are quantified here, and
the depth claim is validated by simulation rather than asserted.
"""
import sys, os, math, random, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import Convention

N = 97
NCRIB = 24
LOG2_26 = math.log2(26)
k4 = load()

print("# EXP-019 unicity distance and the value of depth")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## Part 1 - the longest key K4 could possibly determine")
print(f"   ciphertext length n = {N}, log2(26) = {LOG2_26:.3f} bits per letter\n")
print("   H_Eng  D=log2(26)-H_Eng   redundancy n*D   max key length L*")
print("   (bits/letter)                    (bits)     with H(K)=L*log2(26)")
for h_eng in (1.0, 1.2, 1.5, 2.0):
    D = LOG2_26 - h_eng
    nD = N * D
    Lmax = nD / LOG2_26
    print(f"    {h_eng:.1f}          {D:.2f}            {nD:6.1f}          {Lmax:5.1f} letters")
print()
print("   Reading: with the usual English estimate H_Eng ~ 1.2 bits/letter, K4 can")
print("   uniquely determine a key of at most about 76 letters. A key as long as the")
print("   message - a running key or a one-time pad - carries 97*4.70 = 456 bits,")
print(f"   far above the {N*(LOG2_26-1.2):.0f} bits of redundancy available.")
print()
print("   IMPORTANT NUANCE - a long key is not automatically fatal. What matters is")
print("   the key's ENTROPY, not its length. Compare, against the ~340 bits of")
print("   redundancy a 97-letter English plaintext carries:\n")
for name, bits in [
        ("random 97-letter key (true one-time pad)", 97 * LOG2_26),
        ("97-letter running key drawn from English text", 97 * 1.2),
        ("key read off a physical object (which object + how)", 30.0),
        ("keyword of length 12", 12 * LOG2_26),
        ("keyword of length 22", 22 * LOG2_26)]:
    verdict = "AMBIGUOUS - unbreakable from ciphertext alone" if bits > N * 3.5 \
        else "in principle recoverable"
    print(f"     {name.ljust(50)} {bits:6.0f} bits   {verdict}")
print()
print("   So the correct conclusion is narrower than 'long keys are hopeless':")
print("     * a long RANDOM key makes K4 information-theoretically ambiguous, and")
print("       no method recovers it - not cleverness, not compute;")
print("     * a long STRUCTURED key - a running key from natural text, or a")
print("       keystream read off a physical object - has low entropy and IS")
print("       recoverable in principle, but only once you guess the right source.")
print()
print("   That is exactly where the surviving hypothesis space now sits, and it")
print("   explains the whole pattern of this repository's results: short and")
print("   structured keys are eliminated at scale, while the remaining candidates")
print("   differ from one another only in WHICH EXTERNAL SOURCE supplied the key.")
print("   The cribs cannot distinguish those; only knowing the source can.\n")

print("## Part 2 - what the 24 crib letters buy, and what they leave")
print("   The cribs pin the key at 24 of 97 positions. Under a fully aperiodic key")
print("   the remaining 73 key letters stay free, so the surviving plaintext space is")
print("   every English string that fits the 73 unknown positions:")
for h_eng in (1.0, 1.2, 1.5):
    bits = (N - NCRIB) * h_eng
    print(f"     H_Eng={h_eng}: ~2^{bits:.0f} = 10^{bits*math.log10(2):.0f} plausible completions")
print("   The cribs constrain the MECHANISM, which is why they eliminate structured")
print("   models so effectively, but they do not constrain a long key at all.\n")

print("## Part 3 - depth: what K5 would give, validated by simulation")
print("   Sanborn confirmed K5 is 97 characters, uses a 'similar but not identical'")
print("   system, and shares coded words with K4 in the same positions.")
print("   If two messages share a keystream, the key cancels exactly:")
print("       C1[i] - C2[i] = P1[i] - P2[i]   for every i\n")

random.seed(20260912)
cv = Convention("STD", "STD", "vigenere")
def fit(s):
    return (s + "X" * N)[:N]
# Two different messages that, like K4 and K5, share coded words at the SAME
# positions. The shared span starts at index 40 in both.
P1 = fit("BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHT" + "EASTNORTHEASTXBERLINCLOCK")
P2 = fit("ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLETHE" + "EASTNORTHEASTXBERLINCLOCK")
assert len(P1) == len(P2) == N, (len(P1), len(P2))
key = [random.randrange(26) for _ in range(N)]          # worst case: a true OTP
C1 = "".join(cv.encrypt_letter(p, k) for p, k in zip(P1, key))
C2 = "".join(cv.encrypt_letter(p, k) for p, k in zip(P2, key))
a = [(ord(C1[i]) - ord(C2[i])) % 26 for i in range(N)]
b = [(ord(P1[i]) - ord(P2[i])) % 26 for i in range(N)]
print(f"   simulation with a genuinely random 97-letter key (an OTP):")
print(f"     C1-C2 equals P1-P2 at all {N} positions: {a == b}")
same = [i for i in range(N) if C1[i] == C2[i]]
shared = [i for i in range(N) if P1[i] == P2[i]]
print(f"     positions where C1[i]==C2[i]: {len(same)}")
print(f"     positions where P1[i]==P2[i]: {len(shared)}  -> identical sets: {same == shared}")
print("     So shared plaintext words at shared positions are DIRECTLY VISIBLE in")
print("     the ciphertexts, with no cryptanalysis at all.")
print()
# crib-drag: knowing a word in one message reads the other off, key-free
# Drag across a region where the two plaintexts DIFFER, so the recovery is real
# rather than trivially reproducing a shared word.
pos, ln = 0, 24
drag = P1[pos:pos + ln]
read = "".join(chr(((ord(drag[j]) - 65) - a[pos + j]) % 26 + 65) for j in range(ln))
print(f"   crib-drag demonstration (no key knowledge used, differing region):")
print(f"     knowing P1[{pos}:{pos+ln}] = {drag}")
print(f"     gives   P2[{pos}:{pos+ln}] = {read}")
print(f"     actual  P2[{pos}:{pos+ln}] = {P2[pos:pos+ln]}")
print(f"     correct: {read == P2[pos:pos+ln]}")
print()
print("   The same 24 crib letters that cannot dent a long key on ONE message")
print("   propagate into the other message for free once there is depth.")
print()
print("## Part 4 - what this means for where effort should go")
print("   Ranked by information gained per unit of effort:")
print("     1. K5's ciphertext. 97 characters in depth with K4 would very likely")
print("        break both, even against a one-time pad, by the mechanism above.")
print("        It is withheld until K4 is solved - a deliberate circular lock.")
print("     2. The K4 plaintext. Found Sept 2025 in the Smithsonian donation,")
print("        not published, sealed 50 years. With it, k4lib.recover.diagnose")
print("        reads the method off directly (EXP-005 validates the harness).")
print("     3. More crib letters. EXP-011 quantifies: 3 to 35 more re-open every")
print("        family currently beyond reach.")
print("     4. Further searching of short-key models. Bounded above by Part 1:")
print("        if the key is long, this cannot succeed however long it is run.")
