# Checkpoint M — two of my own claims retracted; the K1/K2-over-K3 hybrid closed

Branch `claude/k4-post-j`. Base for this checkpoint:
`806ee4d78e8bc1669074e5056f1e55bcced5f273`; preregistration at `2087785`; HEAD is this
checkpoint's commit. `main`, `codex/k4-continuation` and `claude/dreamy-archimedes-79k6u0`
untouched. **K4 remains unsolved.** No plaintext candidate, no verifier submission, no
claimed mechanism.

## 1. Request 5 — FULFILLED, and the error was mine

Verified against `data/cipher_side_rows.json`, not accepted on assertion:

| span | physical characters | letters | `?` |
|---|---|---|---|
| K1 = rows 1–2 | 63 | 63 | 0 |
| K2 = rows 3–14 | 372 | 369 | 3 |
| rows 1–14 | **435** | **432** | 3 |

`63 + 372 = 435` is a count of **physical ciphertext characters**. Checkpoint L compared
432 **letters** against it as though the units matched. **There is no transcription
discrepancy on this basis**, and it is no longer carried as open.

Kept separate, and not mixed in: NSA DOCID 4050989's early working convention (K2 as 373,
three solved sections 773, total 870, 97 unresolved), and Sanborn's report to WIRED (2006)
that he deleted an `X` from the end of a K2 line for aesthetic balance. Those concern an
**intended pre-aesthetic cryptographic source**, which is a different object from the
**physical engraved source**. If the restored-`X` stream is ever tested it will be a
separately preregistered source variant, never inserted silently. **EXP-035 tested the
physical engraved 869-character source and its interpretation and result are unchanged:
43,824 decided cases, 0 feasible, 0 undecided.**

## 2. Request 4 — still OPEN, and the new evidence points the same way as parking it

The audit found official CIA photographs, a Library of Congress Carol M. Highsmith record
(`LC-DIG-highsm-13337` / `LC-HS503-2081`, derivatives to an 83 MB TIFF, no known
publication restrictions), and the Smithsonian Jim Sanborn papers — but **no public image
proven orthographic enough** to establish a common character-centre lattice. The CIA text
rendering left-aligns variable-length rows but is a presentation rendering, not a survey;
the CIA close-up is too oblique to show the right edge.

Exact archival target now recorded: **Jim Sanborn papers, Archives of American Art,
Series 3 Commission Files, Box 6 Folder 10, `Pre-Production and Notes, 1990–1999`** — a
punch layout or fabrication drawing would settle this far more cleanly than any angled
photograph. Secondary: the Highsmith TIFF at full resolution, inspected for a ragged
versus flush right edge.

Also new and pointing the same way: Sanborn removed an `X` from a K2 line **for aesthetic
balance**. That is direct evidence the engraved line lengths were artistically adjusted
rather than treated as inviolable blocks. The physical same-column-above architecture
stays **PARKED**, and cryptanalysis was not blocked on it.

## 3. My Checkpoint-L "alphabet frontier" does NOT survive audit — retracted

Checkpoint L said the negative corpus was conditional on an alphabet set that omitted the
K1/K2 mixed alphabet, and promoted a robustness search on that basis. **That was wrong,
and I retract it.**

Verified here rather than assumed: rebuilding the KRYPTOS keyword-mixed sequence
independently from the keyword — write `KRYPTOS`, then the unused letters in order — gives
exactly `KRYPTOSABCDEFGHIJLMNQUVWXZ`, which is `k4lib/alphabets.py`'s `KRY`. And
`all_conventions()` already enumerates all four plaintext × ciphertext combinations of
{STD, KRY} across three combiners:

| | C = STD | C = KRY |
|---|---|---|
| **P = STD** | ✓ | ✓ |
| **P = KRY** | ✓ | ✓ |

NSA DOCID 4050988 gives, for **both** K1 and K2, plain component *and* cipher component as
keyword-mixed sequences based on KRYPTOS. **So the historically demonstrated K1/K2
component alphabet has been in every experiment that uses `all_conventions()` all along.**

`PALIMPSEST` and `ABSCISSA` are **repeating keys** in the primary source, not
component-alphabet keywords. Building mixed alphabets from them would be a new speculative
architecture with no documentary support, not a robustness fix for a known omission.

**Candidate A is therefore rejected.** It would add free parameters nobody has evidence
for, and a negative would eliminate nothing anyone had reason to believe. The frontier also
bites: arbitrary mixed alphabets on both sides plus an arbitrary key make the model an
arbitrary 26×26 table, which is unfalsifiable.

## 4. Chosen architecture — EXP-036, and why

The real gap is narrower and much better motivated. K1 and K2 are **periodic
polyalphabetic** substitutions over KRYPTOS-mixed components with repeating keys of length
**10** and **8**; K3 is a **transposition** Sanborn implemented himself; Scheidt describes
a fourth, different, better-masking process. The obvious hybrid is *both* — and it sits
exactly between two existing experiments:

- **EXP-003** tested this precise gate, both composition orders, but only over the
  affine-mod-97 family (9,312 permutations) and small routes.
- **EXP-033** expanded the transposition frontier to 175 M permutations but composed it
  with **one fixed monoalphabetic substitution**.

The intersection was untested. Preregistered at `2087785` **before implementation**.

### Decidability computed before naming the experiment

This is what made it viable rather than a brute-force fantasy. Because both crib runs are
contiguous, occupied residue classes saturate and the constraint count stays high right
across the range — constraints `= 24 − |{j mod p}|`:

| p | 2 | 5 | 8 | 10 | 13 | 15 | 17 | 20 | 23 | **24** |
|---|---|---|---|---|---|---|---|---|---|---|
| constraints | 22 | 19 | 16 | 14 | 11 | 9 | 7 | 11 | 7 | **5** |

Preregistered admission rule `N · 26⁻ᶜ < 0.01` admits **p = 2…23** for both orders and
**excludes p = 24 in advance** (5 constraints, 1.36 expected chance survivors at
N = 16.15 M) — which is precisely why the declared range stops at 23.

### The key is decided, not enumerated — and here is exactly what that absorbs

| degree of freedom | absorbed? |
|---|---|
| plaintext component alphabet | **NO** — carried as STD or KRY |
| ciphertext component alphabet | **NO** — carried as STD or KRY |
| numerical / index key | **yes** — decided existentially as `p` free values in Z26 |
| key-derivation source letters | not applicable — no external source in this model |
| repeating key **word** | **yes** — any word of length `p` is one point in Z26^p, so `PALIMPSEST` (p = 10) and `ABSCISSA` (p = 8) are covered as special cases with no added parameters |
| tableau row labels | **yes** — relabelling permutes which key value is selected |

## 5. EXP-036 result — NEGATIVE

| | |
|---|---|
| **total declared cases decided** | **4,313,878,272** |
| order A (`C[σ(j)] = conv(P[j], k[j mod p])`), T1 widths 2–10, all column orders | 4,264,035,072 |
| order B (`C[i] = conv(P[σ(i)], k[i mod p])`), T1 widths 2–8, all column orders | 48,820,992 |
| T2 rectangle routes (all widths) + T3 ragged engraving routes, both orders | 1,022,208 |
| **FEASIBLE** | **0** |
| order-B cases excluded as UNDECIDED (< 7 constraints) | 4,091,520 |
| distinct T2/T3 permutations after deduplicating 548 duplicates | 1,936 |
| runtime | 251 s (order A) + 98 s (order B) |

Order A's residue partition is σ-independent so all 22 periods share one pass; order B's
grouping is σ-dependent and costs ~`p` reductions per case per period, which is why its
declared family is narrower. **That asymmetry was declared in the preregistration with its
compute reason, not chosen after seeing results.**

Order-B per-case constraint counts were recorded across the full range (1 → 12+), not
collapsed to the threshold, and counted **before** any verdict was formed — the EXP-034
invariant.

**Honest statement of the chance figure.** The preregistered rule is per (period, family,
order) and is satisfied everywhere. Aggregated over all 22 periods × 12 conventions, the
expected number of chance survivors across the order-A sweep is **0.073** — not 0.01.
Still far below 1, so zero survivors is a genuine negative rather than an expected
outcome, but the aggregate is the number to quote, and it is larger than the
per-combination bound.

### Controls

- **Planted positives 72/72** across both orders, widths, periods and all 12 conventions,
  including keys with repeated values: each detected FEASIBLE at the planted
  (σ, p, convention) **and** the key recovered on every constrained residue class.
- **Adversarial 72/72**, every one *capable* of flipping the verdict by construction — the
  corrupted position is drawn from a residue class holding at least two constrained
  positions, and classes with no such pair are reported "not counted" rather than counted
  as passes. Zero were not counted.
- **Period discrimination 72/72**: each plant is rejected at some other admissible period,
  with a mean of **19.6 of the 21 other periods** rejecting. The period parameter is doing
  real work rather than being absorbed.

### Independent verification

`audit/verify_exp036.py` imports neither the experiment nor `k4lib` and uses no numpy. It
rebuilds the conventions from the three combiner formulas, rebuilds permutations by
**explicit grid simulation** instead of the closed-form column arithmetic, and:
**17/17 checks pass.** It re-decided **1,841,664** cases exhaustively for widths 2–6 across
every period, convention and both orders, sampled 6,000 cases at widths 7–10, found zero
feasible, reproduced the decidability table, confirmed the `N·26⁻ᶜ` rule and that p = 24
would fail it, **confirmed order A and order B are genuinely inequivalent** (not each
other under inversion), checked that constraint counts are verdict-independent, verified
that `KRY` is the rebuilt KRYPTOS keyword-mixed sequence, and replanted its own positives.

### Exact model-limited conclusion

**K4 is not any transposition from the declared families composed with a periodic
polyalphabetic substitution of period 2–23 over STD or KRYPTOS plaintext and ciphertext
components, under the three committed combiners, in either composition order.** Because
the key was decided existentially, this covers every key value, every repeating key word
of those lengths — `PALIMPSEST` and `ABSCISSA` included — and every tableau row labelling,
at once.

**Not eliminated:** keyed columnar widths above the declared limits (11+ order A, 9+ order
B), period ≥ 24, aperiodic / progressive / reset keys, non-shift combiners, component
alphabets outside {STD, KRY}, double transposition, fractionation, and every
physically-aligned model. Case counts are not counts of independent tests.

## 6. Surviving architectures, re-ranked

| rank | architecture | change | falsifiable now? |
|---|---|---|---|
| 1 | **Non-shift combiner over a small motivated table family** — the last structural assumption shared by *every* experiment here is that the combiner is Vigenère / Beaufort / variant Beaufort | **new, promoted.** Six sessions have varied the key, the source, the permutation and the alphabet, but never the combiner | Only with a precommitted table family; a free 26×26 table is unfalsifiable |
| 2 | A specific named **full-26 fractionating** construction (fractionate on one grid, recombine on another) | unchanged — EXP-012's coverage argument does not reach it | Yes, once the construction is named before searching |
| 3 | **Double transposition**, or keyed columnar width ≥ 12 from a precommitted key family | unchanged | Yes, as a small precommitted family |
| 4 | Long key from a still-unidentified external source | unchanged; its best identified candidate died in EXP-035 | No — needs evidence naming a source |
| 5 | Aperiodic / progressive / reset keys over the EXP-033 transposition family | **new**, the natural residue of EXP-036 | Compute constraint density first — resets destroy the collisions this test relies on |
| 6 | Physical panel-alignment models | parked | Blocked on Request 4 / AAA Box 6 Folder 10 |
| 7 | Clock-as-index, semantic inner layer | unchanged | No — no mechanism stated |
| — | **Additional keyword-derived component alphabets** | **rejected this session** — no documentary support; KRY already covers the evidenced case | — |

## 7. Highest-information next step

**Rank 1: vary the combiner, which no experiment here has ever done.** Every one of
EXP-001…036 uses the same three shift combiners. The whole corpus is conditional on that,
and unlike the alphabet claim I retracted above, this one is real: NSA identifies K1/K2's
*components* and *keys*, but a "fourth, different process" that masks English better than
the first three is exactly where a non-shift combiner would live.

The discipline it needs, and the reason it is not trivially runnable: a free 26×26 table
is unfalsifiable, so the family must be a **precommitted small set of structured tables**
with a reason to exist — for example Quagmire-type constructions with a shifted mixed
tableau, or Porta-type reciprocal tables, each generated by a declared rule rather than
fitted. Before implementing I will compute, per table family, the crib constraint density
and the expected chance survival, and drop any family whose failure would teach nothing —
the same gate that killed Candidate A this session and admitted EXP-036.

## 8. External evidence requests

- **Request 4 — OPEN.** AAA Series 3, Box 6 Folder 10 (`Pre-Production and Notes,
  1990–1999`) for a punch layout or fabrication drawing; secondarily the LOC Highsmith
  TIFF at full resolution for a ragged-versus-flush right edge. Not blocking.
- **Request 5 — FULFILLED**, no discrepancy; the error was mine.
- **Request 1 — FULFILLED** at Checkpoint L.
- Requests 2 and 3 (unedited 2005 Zetter/Scheidt material; a target-era Weltzeituhr frame
  from a different bearing) carried forward, still lower priority.

## 9. Reproduce this checkpoint only

```sh
python experiments/exp036_transposition_periodic.py   # ~6 min, needs numpy
python audit/verify_exp036.py                          # ~2 min, pure standard library
```

EXP-024 remains frozen. EXP-029 through EXP-035 were not rerun and nothing here depends on
reproducing them.
