# Result record — 2026-09-12 (session 8) — Checkpoint H

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

**Blind experiment intact. No contamination incidents.** Historical photographs are
admissible object evidence. Only `EASTNORTHEAST` and `BERLINCLOCK` remain admitted
as plaintext constraints. **EXP-024 was neither run nor modified.**

**Outcome: F — one specific acquisition is the sole remaining blocker, and it is far
smaller than Checkpoint G implied.**

---

## 1 — The hard limit, stated first

I **cannot see any of the photographs.** Verified this session:
`commons.wikimedia.org`, `upload.wikimedia.org`, `www.bundesarchiv.de` and
`live.staticflickr.com` all return **HTTP 000** under the egress policy.

So the transcription you supplied (`CHABAROWSK` | `MAGADAN`, `SACHALIN`) is recorded
as **USER-ASSERTED, NOT INDEPENDENTLY VERIFIED HERE** — exactly as you instructed me
not to accept it blindly. I could not re-transcribe it.

**The unblock path is concrete:** images uploaded into the session as files *can* be
read and transcribed here, letter by letter with per-name confidence. That converts
this from an assertion into evidence.

---

## 2 — What your 1989 transcription already proves

Even unverified, it yields real structure.

`Chabarowsk` is UTC+10; `Magadan` and `Sachalin` are UTC+11. So the two adjacent
faces carry **consecutive whole-hour zones**.

**Finding 1 — face order follows UTC order.** Expected of a world clock, but now
*observed* rather than assumed. One adjacency is not the circumference: graded
**SUPPORTED**, needs more.

**Finding 2 — the UTC+11 face may be complete.** Modern UTC+11 contains exactly
`Magadan` and `Sachalin`, and the report names both on one face in that order. Not
proof: 14 of the ~20 1997 additions remain unnamed, so neither can yet be excluded
as an addition.

**Finding 3 — the UTC+10 face is worth a photograph.** It carries five names
(Chabarowsk, Wladiwostok, Sydney, Canberra, Melbourne); only Chabarowsk is placed.

---

## 3 — The result that changes the programme

EXP-027 asked what actually has to be known before EXP-024 may run, and the answer is
much smaller than "reconstruct the drum".

A running-key test needs one contiguous **97-letter window**. Letters per face:

| face | letters |
| --- | --- |
| **UTC+1** | **137** |
| **UTC+3** | **126** |
| **UTC+2** | **108** |

> **Minimum faces needed for one 97-letter window: 1.**

A single fully-transcribed large face suffices. So the threshold is:

**TIER 1 — restricted run permitted:** one contiguous arc of COMPLETE faces (both
bands, order known) totalling ≥ 97 letters. A restricted run must report the fraction
of the preregistered alignment space it covers and may not be presented as full
EXP-024. *Currently 0 complete faces — NOT MET.*

**TIER 2 — full preregistered run:** all 24 faces complete plus the 1997 reversal.
*NOT MET.*

This is a principled **restriction** of the preregistered space, not a modification
of it. EXP-024's 22 procedures are untouched.

---

## 4 — Where photographs are worth most

| face | names | share of remaining layout entropy |
| --- | --- | --- |
| UTC+1 | 19 | **18.6%** |
| UTC+3 | 15 | 13.5% |
| UTC+2 | 15 | 13.5% |
| UTC±0 | 10 | 7.8% |

UTC+1/+2/+3 together: **45.6%**. The August 1989 frame in hand shows UTC+10 and
UTC+11 — between them **3.7%**.

**So the single highest-value acquisition is a legible pre-1997 photograph of the
UTC+1 face** — Berlin's own sector, 19 names, 137 letters, and the side a visitor
photographing the clock is most likely standing in front of. On its own it meets
Tier 1.

---

## 5 — Infrastructure built

- **`data/weltzeituhr_photos.json`** — photographic evidence dataset in the specified
  schema: accession, photographer, date, date-confidence, visible faces, upper/lower
  bands, adjacency, transcription confidence, pre-1997 and 1988–89 flags. It carries
  the **critical geometry rule** as a first-class field: *the hour ring rotates and
  the cylinder is static, so an hour numeral never identifies a face* — sectors are
  assigned from city contents and adjacency only.
- **`k4lib/wz_graph.py`** — the drum adjacency graph. Nodes are physical faces with
  ordered `upper`, `lower` and `unknown`; edges carry provenance and are marked
  **OBSERVED** or **TRANSITIVE**, never conflated. Chains, transitive closure and
  circumference statistics are computed from photographs alone.

Current graph: **2 faces identified, 1 observed edge, 0 complete faces, 8.3% of the
circumference, 0 lower bands, longest chain 2.**

---

## 6 — Archive targets located

Dated and confirmed: `183-1989-0830-028` (30 Aug 1989, Schneider),
`183-1989-0811-023` (11 Aug 1989, Settnik), `183-1984-1419-014` (19 Apr 1984, Junge).

**Seven further Weltzeituhr accessions located this session, not yet dated:**
`183-L0105-0018`, `183-R0729-0017`, `183-U0414-0014`, `183-E1003-0001-001`,
`183-H1218-0025-001`, `183-W0715-0026`, `183-N1005-0011`.

**Accession structure decoded (inferred, with a check):** modern form is
`183-YYYY-MMDD-frame`; older ADN form is `183-<LETTER>MMDD-frame`, the letter encoding
the year. Internal check: `183-H1218-…` is captioned *"Winter"* and H**1218** → 18
December. Consistent. Reading each Commons file page dates all seven at once.

Categories to enumerate: `Urania-Weltzeituhr and Berliner Fernsehturm`,
`Urania-Weltzeituhr` + its *Details* subcategory, `Photographs by Peter Heinz Junge`,
`Commons:Bundesarchiv`.

---

## 7 — Open questions recorded, not guessed

- **Stability 1969–1997: UNTESTED.** Requires the same face read in two well-separated
  dated photographs. If stable, the entire 1970s–80s pool becomes usable for the 1989
  state — the single largest possible expansion of the evidence base. *Do not assume
  1969 layout equals 1989 layout merely because both predate 1997.*
- **Half-hour placement: UNKNOWN.** Marquesas, Teheran, Kabul, Neu-Delhi/Colombo and
  Rangun cannot each own one of 24 whole-hour faces. A photograph of the
  Teheran/Kabul/Delhi region would reveal how the inscription *system* handles them,
  which constrains any reading procedure.

---

## Checkpoint H status

| Measure | Value |
| --- | --- |
| Faces identified | 2 / 24 |
| Faces with upper band transcribed | 2 |
| Faces with lower band transcribed | **0** |
| Faces COMPLETE | **0** |
| Adjacency edges observed | 1 |
| Circumference identified | 8.3% |
| Faces verified by 1988–89 evidence | 2 (both user-asserted) |
| Faces from older photos + demonstrated stability | 0 (stability untested) |
| Tier 1 threshold | **NOT MET** |

**The sole remaining blocker, stated so it can be acted on:** a legible pre-1997
photograph of the **UTC+1 face** (or UTC+2 / UTC+3), showing **both bands** with names
readable in order — **uploaded into the session as a file**, so transcription happens
here rather than being asserted.

**The Weltzeituhr running-key hypothesis is unchanged: PROMISING HYPOTHESIS,
UNTESTABLE WITH CURRENT PUBLIC DATA.** Not advanced, not rescued, not downgraded —
the photographic evidence has not yet contradicted anything.

**K4 remains unsolved. No mechanism claimed, no verifier submission warranted.**
