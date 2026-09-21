# Checkpoint AF — prospective periodic-family scope clarification

**Date:** 2026-09-13

This note supersedes only the **scope reading** of Checkpoint AE's periodic-family language. It does not rewrite AE's historical text and changes no numerical result.

Checkpoint AE uses generic notation `C[i] = F(P[i], k[i mod p])`. The statement that periodic schedules at `p <= 23` are already closed applies only to the declared shift/combiner families actually tested:

- the 12 committed Vigenere / Beaufort / variant-Beaufort conventions across STD/KRY plaintext and ciphertext alphabets;
- EXP-036 compositions with the declared transposition families;
- Quagmire I-III and Gronsfeld reductions;
- EXP-037 standard Porta.

It is **not** a theorem eliminating every arbitrary periodic combiner.

An arbitrary fixed 26x26 table is census class L. Under the present crib geometry it receives zero constraints at key periods 8, 10, 13 and 26 because no `(plaintext, key)` input pair repeats. A short period alone therefore does not make an arbitrary combiner falsifiable.

**No cryptanalytic conclusion changes. No EXP-040 is justified.**

This is a prospective correction. The historical Checkpoint AE result and census wording remain preserved as originally committed.
