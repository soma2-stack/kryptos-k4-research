# Result record — 2026-09-12 (session 6) — Checkpoint F

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

**Blind experiment intact. No contamination incidents.** `solvekryptos.com` excluded
on every query; no claimed-solution site used; no purported K4 plaintext sought or
seen. Only `EASTNORTHEAST` and `BERLINCLOCK` remain admitted as constraints.

**Outcome: F** — one remaining datum is the sole blocker for the decisive test, and
its exact archival source is now identified. Blockers 2–4 partially closed; a
seventh blocker was discovered that Checkpoint E had missed.

---

## 1 — Blocker 1 could not be closed here, and the reason is now proven

You were right that the official site publishes the complete modern list. It is
still unreachable from this environment, and I verified that at three levels rather
than asserting it:

| Path | Result |
| --- | --- |
| `WebFetch` on `weltzeituhr-berlin.de` (https and http) | `EGRESS_BLOCKED` |
| `curl` through the agent proxy | `connect_rejected — the egress proxy denied the CONNECT (organization policy)` |
| Control: `curl https://pypi.org/` | **HTTP 200** |
| Control: `curl https://en.wikipedia.org/`, `example.com` | HTTP 000 |
| `WebSearch`, bulk enumeration | summaries decline to enumerate |
| `WebSearch`, single-sector queries (e.g. "which cities on the UTC+1 panel") | also declined |

The pypi.org control is the important one: it proves this is a **domain allow-list
policy**, not a network failure. Only package registries are reachable.

**Worth recording:** when pressed for the list, the search summariser explicitly said
it did not have it rather than generating a plausible one. No fabricated list entered
the dataset, which was the real risk here.

---

## 2 — Blockers 2–4: genuinely advanced, using contemporary 1997 reporting

Contemporary Berliner Zeitung and taz coverage from December 1997 yielded more than
the later summaries did.

**Additions (1997)** — 5 of ~20 now documented: **Jerusalem, Tel Aviv, Kapstadt /
Cape Town, Oslo, Seoul**. Fifteen remain unnamed.

**Renames (1997)** — 4 documented, one newly recovered this session:

| from | to | confidence |
| --- | --- | --- |
| Leningrad | Sankt Petersburg | MULTIPLE INDEPENDENT SOURCES |
| Alma-Ata | Almaty | MULTIPLE INDEPENDENT SOURCES |
| **Aschchabad** | **Aschgabat** | SINGLE RELIABLE SOURCE *(new)* |
| Bratislava | Preßburg | MULTIPLE INDEPENDENT SOURCES |

**Zone moves** — only Kiew/Kyiv named; its from- and to-sectors remain UNKNOWN.
**Removals** — UNKNOWN; no source reached documents any.

### The first genuine pre-1997 panel fragment

Contemporary reporting states that after the restoration the name **Preßburg stands
on an aluminium panel between Bern and Belgrad**. Two independent sources carry this.
Since a rename presupposes the prior entry, the pre-1997 UTC+1 panel carried:

> **… Bern, Bratislava, Belgrad …**

This is the first per-sector *content* of the historical clock established in this
project. Its limits are recorded with it: the **adjacency** is sourced; the **band**
(upper or lower) is not; the rest of the sector is not.

### The archival target that would close blockers 2–4 at once

The Senatsbauverwaltung stated publicly in December 1997 that the spellings were
**coordinated with the language service of the Auswärtiges Amt in Bonn and the
Senatskanzlei**. A correspondence file between those bodies would enumerate every
name and spelling decided in 1997 — one document closing three blockers.

---

## 3 — A seventh blocker Checkpoint E missed

Checkpoint E framed the reconstruction as reversing the 1997 changes. That is
**insufficient**. The clock was **also restored in 2015**, and Apia's own UTC offset
changed in 2011 (−11 → +13). So reconstructing 1988–89 from the modern list requires
reversing the **2015** change set as well, which is entirely UNKNOWN.

This also bears on the displayed range. If the published list runs Honolulu → Apia
and Apia now sits at UTC+13, the range is UTC−10…+13 — exactly 24 sectors. But an
alternative reading is UTC−11…+12 with the list wrapping, which also gives 24. Both
are recorded; the matter must be settled from the published list itself, not assumed.

---

## 4 — The panel evidence matrix, and a guard against future self-deception

`data/weltzeituhr_panels.json` holds one entry per displayed sector with the fields
the brief specifies: modern upper/lower, confirmed pre-1997 upper/lower, names added,
renamed and moved in 1997, unresolved differences, sources, and confidence. The
published order is stored as `modern_names_unsplit` — **table order is not recorded
as physical band placement**, because it is not evidence of it.

`k4lib/wz_panels.build_clock()` **refuses** to produce a historical clock while any
sector is UNKNOWN. Demonstrated in EXP-025: 24 of 24 sectors are missing a pre-1997
band assignment and the call raises. Producing a clock from incomplete data requires
deliberately passing `allow_incomplete=True`, which stamps the output as not
historical.

This guard exists because the failure mode this programme most needs to avoid is a
future session quietly filling UNKNOWN sectors with modern names and reporting the
result as historical.

---

## 5 — EXP-025: why the modern list cannot stand in, measured rather than asserted

With 20 of 146 modern names added in 1997, the probability that a 97-letter keystream
window contains **no** post-1997 name:

| mean name length | names per window | P(window free of 1997 additions) |
| --- | --- | --- |
| 6 | 16 | 0.082 |
| 7 | 14 | 0.114 |
| 8 | 12 | 0.158 |
| 9 | 11 | 0.186 |

**Roughly 85–90% of modern-tape windows are contaminated.** Testing the modern list
as a proxy would be wrong most of the time, and a negative from it would carry almost
no information about the historical clock. Your instruction not to take that shortcut
is now a measured fact rather than a methodological preference.

---

## 6 — Power of the preregistered test, fixed in advance

For a tape of ~146 names × ~7 letters ≈ 1,022 letters, EXP-024 will try about
**1,079,232 alignments**, with an expected false 24/24 count of **1.2 × 10⁻²⁸**. A
single exact hit would therefore be decisive.

The weakness is not power. It is that circular readings of one clock share
substrings, so those alignments are **not independent** — EXP-024's control recovered
one planted key under **three** procedure labels. That dependency must be reported
when the test runs, not corrected away.

**EXP-024 was not altered.** Its 22 reading procedures remain exactly as preregistered
before any historical data existed.

---

## Checkpoint F — status of each blocker

| # | Blocker | Status |
| --- | --- | --- |
| 1 | modern per-sector list | **NOT CLOSED HERE** — published, but denied by egress policy (proven) |
| 2 | ~20 names added 1997 | **PARTIAL** — 5 of 20 |
| 3 | 1997 zone reassignments | **PARTIAL** — Kiew only, from/to unknown |
| 4 | removals/replacements 1997 | UNKNOWN |
| 5 | upper/lower band assignment | UNKNOWN — one adjacency known, without its band |
| 6 | cylinder orientation vs north | UNKNOWN |
| 7 | **2015 change set** *(new)* | UNKNOWN |

**The Weltzeituhr hypothesis is unchanged in standing: PROMISING HYPOTHESIS,
UNTESTABLE WITH CURRENT PUBLIC DATA.** It was not advanced, and it was not rescued.
No preregistered reading has been run, because running it on contaminated data would
produce a result worth ~10% of a real one.

**Next actions, in order:**
1. Supply the modern per-sector list — a browser task, not a research task. With it
   in `data/weltzeituhr_panels.json` via `wz_panels.ingest_modern_list`, the
   remaining work is reversal, not retrieval.
2. Obtain the Senatsbauverwaltung ↔ Auswärtiges Amt Sprachendienst 1997
   correspondence — closes blockers 2, 3 and 4 together.
3. Obtain the 2015 restoration record — blocker 7.
4. Read upper/lower band placement off dated pre-1990 photographs (DDR-Bildarchiv,
   picture-alliance, Getty hold candidates; images are not readable through this
   toolchain).

**K4 remains unsolved. No mechanism claimed, no verifier submission warranted.**
