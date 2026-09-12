# Result record — 2026-09-12 (session 4) — Checkpoint D

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

**Blind-experiment status: intact.** No purported K4 plaintext was sought, fetched
or ingested. One disallowed source used in Checkpoint C was identified and
quarantined; see `docs/contamination-log.md`. The only plaintext used as a
constraint remains `EASTNORTHEAST` and `BERLINCLOCK`.

---

## 0 — Contamination incident, declared and remediated

The 7×14 K4 layout adopted in Checkpoint C came from `solvekryptos.com`, a site
whose primary purpose is publishing a claimed complete K4 plaintext. Under the rule
now in force it is inadmissible.

- **Exposure assessed: none.** No page from that domain was ever fetched; only
  search-result titles and a synthesised summary were seen, containing no plaintext
  beyond the two public cribs.
- The layout is reclassified **DISALLOWED-SOURCE / UNVERIFIED**.
- EXP-018's *result* stands — a negative over a badly motivated grid is still a
  negative for that grid — but its **motivation** is withdrawn.
- A standing exclusion list is now maintained.

---

## 1 — Primary-data gap 1: the carved geometry · **RESOLVED, and it replaces 7×14**

K4's canonical line structure is

```
line 0  OBKR                             positions  0.. 3   ( 4)
line 1  UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO  positions  4..34   (31)
line 2  TWTQSJQSSEKZZWATJKLUDIAWINFBNYP  positions 35..65   (31)
line 3  VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR  positions 66..96   (31)
```

**Self-verified**: the four lines concatenate exactly to the canonical ciphertext,
so the split is internally checked rather than asserted, and it matches the
"31-column geometry" the inherited handoff refers to. Graded **MEDIUM-HIGH as the
transcription structure, MEDIUM as the physical engraving** — because reporting
states the engraved line lengths *vary*, Sanborn having kerned the lettering for
aesthetics rather than using fixed-width spacing.

Two asymmetric facts follow, and they were not visible before:

- `EASTNORTHEAST` (21–33) lies **wholly inside line 1**.
- `BERLINCLOCK` (63–73) **straddles the line-2/line-3 boundary at position 66**.

**A class eliminated by the uneven-engraving fact.** The ciphertext panel is not on
a regular lattice, while the tableau panel is. Any mechanism requiring exact
cell-to-cell physical alignment between the two panels — the "read one object
through another" overlay — is **STRONGLY DISFAVORED**: they are not on the same
grid. Sources also conflict on which half of the screen carries the ciphertext
(graded LOW, unusable until resolved from photographs).

---

## 2 — EXP-020: the carved line structure as the coding geometry · ELIMINATED WITHIN MODEL

**Hypothesis.** Sanborn cut these lines by hand, one at a time. The cheapest hand
procedure for a long message is to work line by line and restart the key at each
line. That predicts phase resets at 4, 35 and 66 — positions supplied by the
object, **not fitted**. The model therefore adds no free parameters beyond the key
itself: exactly the profile a hand-executed construction should have.

Distinct from EXP-006/015, which allowed a *single* reset at one searched boundary.

**Scope.** Key restarting per line (p ≤ 20); per-line additive offset; key advancing
once per line rather than per character; progressive key restarting per line; and
each with OBKR treated either as line 0 or as an indicator with the message
starting at position 4. 12 conventions. **1,344 systems solved exactly, planted
control recovered, zero fits.**

**A sharp prediction, stated before testing, also fails.** Columns 28 and 29 occur
in *both* cribs, so a column-indexed key requires `k[32] = k[63]` and
`k[33] = k[64]` — two independent 1/26 constraints. Satisfied by **0 of 12**
conventions (≈0.018 expected by chance).

`column_key` itself is reported as **UNTESTABLE WITH CURRENT PUBLIC DATA** (31
unknowns against 24 constraints), not as a negative.

---

## 3 — EXP-021: what K5 implies about architecture · **a new diagnostic**

No K5 data invented; only the public description, tested on synthetic messages.

**An earlier draft of this experiment was wrong and is corrected here.** I first
claimed the K4/K5 positional correspondence excludes autokey and fractionation. The
simulation shows it does not: short-memory autokey preserves 10 of 11 shared
letters, and neighbour-mixing preserves 10 of 11. Only *unbounded* ciphertext
feedback destroys the correspondence entirely.

What the simulation actually reveals is better than the claim it refuted. **The
pattern of breakage at the edges of a shared span is a direct measurement of the
cipher's memory:**

| mechanism | span pattern | reading |
| --- | --- | --- |
| position-indexed substitution | `===========` | no memory: key depends on position alone |
| plaintext autokey, lag 1 | `x==========` | 1 leading break → backward memory depth 1 |
| plaintext autokey, lag 3 | `xxx========` | 3 leading breaks → backward memory depth 3 |
| ciphertext feedback | `xxxxxxxxxxx` | all broken → unbounded feedback |
| substitute then transpose | `=xx=xxxxxxx` | scattered → relocation |
| fractionation (i, i+1) | `==========x` | 1 trailing break → forward mixing depth 1 |

**The diagnostic.** If K5's ciphertext is released, the first measurement is not a
cipher search. Line K4 and K5 up, find the agreeing positions, and read the memory
depth and direction off the edges of each shared run. That fixes the architecture
before any key is guessed. This is a concrete protocol derived from public
information alone.

**Conclusions, graded.**
1. **Unbounded ciphertext feedback: STRONGLY DISFAVORED** — the one class that
   destroys the correspondence completely. Independent of EXP-008, which eliminated
   feedback only within parameter-linear models.
2. **A net transposition: STRONGLY DISFAVORED** under the reading that the
   *ciphertexts* show the correspondence — a transposition relocates shared
   material, so coded words would appear scattered, not at the same positions.
3. **The system is a reusable, parameterised device: SUPPORTED INTERPRETATION.** A
   second 97-character message was enciphered with a "similar but not identical"
   system, so the construction has at least one tunable parameter. This matches the
   auction wording of an original K4 "coding system" plus separate "coding charts".
4. **Length is preserved exactly, 97 → 97.** Any length-changing outer layer is
   **PROVED IMPOSSIBLE**.

Sanborn's phrase admits two readings — that the *plaintexts* correspond, or that
the *ciphertexts* do. Under the first, conclusions 1 and 2 do not follow. Nothing
here is graded above STRONGLY DISFAVORED, and the ambiguity is the reason.

**Convergence worth more than the eliminations.** Conclusions 1 and 2 push K4 into
the **monographic, position-preserving** class — which is exactly the class in
which this repository's strongest results are proofs rather than heuristics (≥3
alphabets forced, periods {1–7, 9, 10, 14, 15, 17} impossible).
`docs/evidence-grades.md` flagged those as conditional on that class; the K5
description is independent evidence that the condition holds.

---

## 4 — EXP-022: is the forced keystream text-like? · HEURISTIC NEGATIVE

The surviving architecture implies a long keystream *read off something*. That class
cannot be tested by enumerating sources — with a free tape any ciphertext fits — but
it makes a prediction: under the correct convention the 24 forced key letters should
look like text, and uniform under every wrong one.

**Result: no signal.** Best convention p = 0.0178 uncorrected, **0.428 after
correcting for 24 tests**; 2 of 24 below p < 0.05 against 1.2 expected.

**Graded HEURISTIC NEGATIVE, not an elimination.** The calibration in the log shows
that at n = 24 the test cannot reliably separate an English sample from a uniform
one, and a key read off **proper nouns** — city names on a clock drum — need not
follow ordinary English letter frequencies at all. It does not touch keystreams read
off a chart, a tableau, or a numeric structure rather than prose.

---

## 5 — Primary-data gap 2: the historical Weltzeituhr · **NOT RESOLVED**

Searched in English and German across general and Berlin-specific sources.

**Recovered, with grades:** the 24-sided cylinder carrying the city names is
**static** and an **hour ring rotates inside it** — this *corrects* the earlier note
in `data/physical.json` describing the drum as rotating. Driven by a converted
Trabant gearbox; an orrery turns above; the rotunda also displays the date line;
built in ~9 months by 124 volunteers; opened 30 September 1969.

**Counts conflict and are recorded unresolved:** 80 cities in 1969 (one source);
146 cities and regions (another); 148 (a third); 20 cities the GDR omitted for
political reasons — Tel Aviv, Cape Town, Seoul among them — added in the 1997
renovation. If ~146 today and 20 were added in 1997, the 1988–89 configuration held
roughly 126 names, but that is an inference across conflicting sources, not a datum.

**The ordered per-segment city list as it stood in 1988–89 is not published in any
source reached. It is recorded as UNKNOWN and was not guessed.**

---

## Checkpoint D — what was achieved

- **(D) Historically reliable physical data that changes the viable mechanism
  space.** The carved line structure replaces the disallowed 7×14; the uneven
  engraving strongly disfavours the panel-overlay class; the Weltzeituhr's drum is
  static with an internal rotating hour ring, correcting an earlier error.
- **(C) A new invariant/diagnostic.** The edge-breakage pattern of a shared span
  measures a cipher's memory depth and direction directly — a protocol for the
  moment K5 appears, derived entirely from public information.
- **(B) A physically motivated class eliminated within a specified model.** The
  line-by-line hand-encipherment family, whose reset positions come from the object
  rather than from fitting.
- **(E) The dominant blocker, sharpened to one specific item.** Three independent
  lines now converge:
  - EXP-019: the key must be **long but low-entropy and externally sourced**;
  - EXP-021: **position-indexed**, no net transposition, no unbounded feedback;
  - EXP-006/008/015/016/018/020: every short or structured position-indexed key is
    eliminated.

  What survives is a **keystream read off an external object, position by
  position** — and the `BERLINCLOCK` crib names that object. A city-name tape from
  the Weltzeituhr is ~900–1000 letters, ordered by the object, hand-readable by an
  artist, requires no mathematics, and would be applied position by position to a
  97-character message. It fits every constraint this repository has established.

  **It cannot be tested, because the 1988–89 city list is not public.** That is the
  blocker, and it is specific rather than general. Existing evidence cannot
  distinguish it from any other low-entropy external source: EXP-022 shows the cribs
  cannot even tell a text-derived keystream from a uniform one at n = 24.

  Where to look: GDR-era photographs of the drum at readable resolution; Erich
  John's design documentation; Berlin municipal or Stadtmuseum archives; DDR Museum
  holdings; 1997 restoration records documenting what was changed.

**K4 remains unsolved. No candidate mechanism is claimed, and no verifier
submission is warranted.**
