# Fractionation frontier audit — named classical constructions

Symbolic audit, done before any experiment number is assigned. Every figure below was
recomputed here from the letter data rather than copied from a handoff. **No family that
can be closed by an exact structural observation receives an experiment number.**

K4 remains unsolved.

## Standing facts this audit uses

- K4 is 97 characters. **97 is prime.**
- K4 contains **all 26 letters**, `J` included (positions 40, 51, 81, 1-indexed) — the
  coverage argument EXP-012 rests on.
- The public cribs are the only plaintext constraints: `EASTNORTHEAST` at [21,34) and
  `BERLINCLOCK` at [63,74), zero-based. `data/k4.json` itself records that these are "the
  canonical working positions used in the inherited research" and asks for verification
  against a primary transcript — that caveat matters in §C below and is not glossed over.

---

## A. Conjugated Matrix Bifid — reduces to EXP-012, no run

The standard construction uses **two 5×5 Polybius squares over a 25-letter alphabet** with
one letter merged (conventionally I/J). Every ciphertext character is therefore read out of
a 25-symbol inventory.

K4 contains `J` at three positions. A 25-cell square that merges I and J cannot emit `J` at
all; any other merge choice fails on whichever letter it drops. **This is exactly EXP-012's
argument, and it applies unchanged.**

> **Verdict: REDUCED TO EXP-012. Excluded on output-alphabet coverage. No Bifid search.**

Explicitly not done, and why: a 6×6 variant carries 36 cells and needs 10 extra symbols
(digits or repeats). That is a **different model** — it changes the emitted inventory and
needs its own motivation — and silently sliding from 5×5 to 6×6 to keep the family alive
would be rescuing rather than testing. EXP-012 already grades 6×6-with-digits as strongly
disfavoured on the same coverage grounds, since roughly a quarter of emitted characters
would be non-letters and none appear.

---

## B. Digrafid — closed by primality, without needing the exact block ratio

Digrafid is a block system over 27-symbol alphabets (26 letters plus a filler such as `#`),
processing plaintext in fixed groups rather than one letter at a time.

**I do not have an authoritative offline definition of its exact block ratio**, and I will
not assert one from memory. That turns out not to matter, because the decisive argument is
ratio-independent:

> Let a block system consume `b > 1` plaintext symbols and emit `c > 1` ciphertext symbols
> per block. A complete ciphertext then has length `c · m` for an integer `m`.
> **97 is prime**, so `c · m = 97` forces `c = 1` or `c = 97`.
> No `c ∈ {2, 3}` — and no `c` at all in `2 … 96` — can produce exactly 97 ciphertext
> symbols.

So standard Digrafid cannot emit a 97-character ciphertext under **any** block ratio greater
than one, without a padding or truncation convention. I am not inventing such a convention,
and I am not dropping or padding a symbol to make it fit.

> **Verdict: STRUCTURALLY INCOMPATIBLE with a 97-character ciphertext, for any block ratio
> c > 1. No search.**

Two disciplined caveats. First, the 27th filler symbol is **not** by itself the rejection —
length is the stronger argument, as it does not depend on whether a filler could have been
avoided by the plaintext. Second, if a documented standard Digrafid convention for handling
an incomplete final block exists, this verdict should be revisited against that citation
rather than against my recollection.

---

## C. Fractionated Morse — the one that deserved real work

This is the named fractionator with a genuine Kryptos connection: the sculpture physically
carries Morse material, and **EXP-023 tested that material only as a running-key letter
tape**, explicitly leaving dot/dash/separator *structural* use open. So this is a real
untested gap, not a catalogue entry.

**Standard construction used:** letters → International Morse; a single `x` between letters;
`xx` between words; the resulting alphabet is `{. - x}`; the stream is grouped in **triples**;
each valid triple maps through a 26-letter keyed alphabet to one ciphertext letter.

### The arithmetic, recomputed here

`n` ciphertext letters cover exactly `3n` ternary symbols. A plaintext segment of `k` letters
needs at minimum `marks + (k − 1)` symbols — minimum because it assumes one separator between
letters, none at the ends, and no word separators.

| segment | letters | Morse marks | min. separators | min. stream | 3n supply | verdict |
|---|---:|---:|---:|---:|---:|---|
| `BERLIN` | 6 | 16 | 5 | **21** | 18 | **impossible, short by 3** |
| `CLOCK` | 5 | 18 | 4 | **22** | 15 | **impossible, short by 7** |
| `BERLINCLOCK` | 11 | 34 | 10 | **44** | 33 | **impossible, short by 11** |
| `NORTHEAST` | 9 | 20 | 8 | **28** | 27 | **impossible, short by 1** |
| `EAST` | 4 | 7 | 3 | 10 | 12 | fits |
| `EASTNORTHEAST` | 13 | 27 | 12 | **39** | **39** | **fits exactly** |

`EASTNORTHEAST` needing exactly 39 = 13 × 3 is a genuine coincidence. It is recorded and
**not pursued**: it requires no word separators and no end padding, and `BERLINCLOCK` in the
same message fails by 11, so no single message can satisfy both.

### The global argument, which does not depend on crib positions at all

97 ciphertext letters ⇒ 291 ternary symbols. For a plaintext of `n` letters (internal
separators only), `291 = Σ marks + (n − 1)`, so `Σ marks = 292 − n`:

| plaintext length n | required mean Morse marks / letter |
|---:|---:|
| 69 | 3.23 |
| 80 | 2.65 |
| **97** | **2.01** |

The unweighted mean over A–Z is **3.15**. So a 97-letter plaintext would need a mean of
2.01 marks — a wildly dot-light text. **Standard Fractionated Morse is neither
length-preserving nor position-preserving**: ciphertext position `i` does not correspond to
plaintext position `i`, because each ciphertext letter absorbs three ternary symbols that
straddle variable-length Morse letters.

### The semantic check, stated honestly

The repository's crib model is `P[i] ↔ C[i]` — length- and position-preserving. Under that
reading, Fractionated Morse is rejected twice over: by the per-segment table above and by the
global mean-marks requirement.

**I cannot verify the primary clue wording offline**, and `data/k4.json` flags the crib
positions as inherited-canonical rather than primary-verified. So, precisely:

- **If** the public clues mean cipher positions 63–73 decrypt to `BERLINCLOCK` at plaintext
  positions 63–73, then standard Fractionated Morse is **structurally rejected**, and no
  keyed alphabet can repair it — a keyword permutes which triple maps to which letter and
  changes no length.
- **If** the clues do not establish local position preservation, then a Fractionated-Morse
  reading would have to restate every one of the 24 crib constraints: define how ciphertext
  position 63 indexes into the variable-length ternary stream, define what "plaintext
  position 63" means when plaintext letters occupy 1–4 symbols plus separators, and show how
  the disclosed segments are recovered from stream offsets rather than letter indices. That
  reformulation is a different research programme, and **no crib is to be slid to a new
  position to make it work.**

> **Verdict: STANDARD Fractionated Morse is structurally rejected under the repository's
> position-preserving crib model. No keyword search — not `KRYPTOS`, not `PALIMPSEST`, not
> `ABSCISSA`, not `BERLINCLOCK`, not dictionary keys.**

### What this closes in EXP-023, and what it does not

EXP-023's open gap — Morse used as *structure* rather than as a letter tape — is now closed
**only for standard Fractionated Morse**. Morse-derived systems with different grouping,
different separator handling, or a non-length-changing encoding remain untested. `docs/negative-results.md`
records EXP-023's tape result as a HEURISTIC NEGATIVE resting on community transcriptions;
nothing here upgrades that.

---

## Frontier conclusion

CM Bifid reduces to EXP-012; Digrafid is closed by the primality of 97; standard Fractionated
Morse is closed by Morse length arithmetic. With EXP-012 (sub-26 output alphabets) and
EXP-013 (Trifid at its decidable periods) already on record:

> **The obvious named classical fractionation candidates are substantially exhausted under
> the public evidence.**

This is **not** "K4 is not fractionated." A custom fractionator that emits all 26 letters,
preserves length, and preserves position could still exist. But at that point it is a
**speculative architecture with no name, no documentary support and free parameters**, and it
does not automatically inherit the next session's budget. Before any such construction gets a
number it must be written as equations, checked against the reduction rule for duplication,
and have its crib constraint density and null derived **from the construction itself**.

---

## Appendix: Gromark, audited in the same pass and rejected

Standard Gromark — Gronsfeld with a mixed alphabet and a running key from a five-digit primer
expanded by chained addition mod 10 — was checked against the same kind of exact gate before
any primer search.

**The gate:** Gromark key values are **digits 0–9**, so every crib pair must need a shift
inside that set. Computed across the evidenced component pairs, and across both digit
conventions:

| plain / cipher | shifts in 0–9 | shifts in 1–10 |
|---|---:|---:|
| STD / STD | **15 of 24 crib pairs rejected** | 14 rejected |
| STD / KRY | 15 rejected | 16 rejected |
| KRY / STD | 14 rejected | 15 rejected |
| KRY / KRY | **11 rejected** (best case) | 12 rejected |

Example rejections under STD/STD: position 22 `A→L` needs 11; position 23 `S→R` needs 25;
position 27 `R→P` needs 24.

> **Verdict: the direct position-preserving Gromark family is structurally impossible under
> every evidenced component-alphabet pair. The 100,000-primer search was not run and
> EXP-038 was not assigned.**

**What I did not do, and why.** I did not derive an ACA columnar-transposition Gromark
alphabet from `KRYPTOS`, for two reasons. First, I have no authoritative offline source for
that exact construction and will not invent a "standard" from memory. Second, and more
importantly, it would not be evidence: a random mixed alphabet passes the 24-crib digit gate
with probability `(10/26)²⁴ ≈ 1.1 × 10⁻¹⁰`, which over 26! alphabets still leaves on the
order of **10¹⁶ alphabets that pass by chance**. Searching for an alphabet that admits the
cribs would therefore be *fitting*, not testing — and no primary source names a Gromark
alphabet for Kryptos at all. Gromark is graded **speculative, with no Sanborn or Scheidt
evidence**, and is demoted.

Not attempted, deliberately, and reserved for a future session only with independent
motivation: transposition-composed Gromark, reversed recurrence, alternate modulus, primer
offsets, resets, longer secret state, or additional keywords.
