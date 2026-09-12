# Contamination log

**Rule.** The only plaintext admitted as a cryptanalytic constraint is the publicly
confirmed crib material: `EASTNORTHEAST` (positions 21–33) and `BERLINCLOCK`
(positions 63–73), both already in `data/k4.json`. Purported full or partial K4
plaintexts — leaked, reconstructed, or claimed — must not be ingested, searched
for, used, optimised against, or allowed to influence any parameter, position,
theme or mechanism choice. The goal is an independent derivation.

**Operational practice adopted 2026-09-12 (session 4):**

1. Never issue a web query whose purpose is to obtain K4 plaintext.
2. Exclude sites whose primary purpose is publishing a claimed complete K4
   solution from the search domain list, and never fetch their pages.
3. Prefer institutional and primary sources (NSA FOIA, CIA, museum, archival
   photography) for physical facts.
4. Record every incident below, including near-misses, at the time it happens.
5. If purported plaintext is exposed accidentally, quarantine it: do not use those
   words, positions, semantic themes, or any parameter derived from them.

---

## Incident 1 — 2026-09-12, session 3 (Checkpoint C). Disallowed source used for geometry.

**What happened.** While closing the physical-geometry gap I ran a web search for
the K4 copper-plate layout. The result summaries attributed the "7 tiers × 14
lanes, 98 cells, one blank at tier 7 lane 13" layout to `solvekryptos.com`. I
recorded it in `data/physical.json` at MEDIUM confidence, noting the site's K4
solution claim is disputed by Sanborn, and used 14×7 and 7×14 among the
pre-registered grids in EXP-018.

**Why it is a problem.** `solvekryptos.com` exists primarily to publish a claimed
complete K4 plaintext. Under the rule now in force it is not admissible as
evidence, regardless of whether the specific fact taken from it was plaintext.

**Exposure assessment.** No page from that domain was ever fetched. Only
search-result titles and a synthesised summary were seen. The summary contained
no plaintext beyond the two public cribs, which the same reporting attributes to
the Smithsonian scraps and which are public. Titles seen included the phrase
"Reconstructed Plaintext" but no reconstructed text.
**Assessed exposure to non-public plaintext: none.**

**Action taken.**
- The 7×14 layout is reclassified in `data/physical.json` from MEDIUM confidence to
  **DISALLOWED-SOURCE / UNVERIFIED**, and is not to be treated as established.
- EXP-018's result is *unaffected in validity*: it is a negative, and a negative
  over a badly motivated grid is still a negative for that grid. What is weakened
  is the **motivation** for having chosen 14×7, not the elimination itself. The
  experiment's docstring is annotated accordingly.
- Independent verification is attempted from institutional sources; see EXP-020.
- Domain added to the standing exclusion list below.

## Standing exclusion list

Sites not to be used as evidence and not to be fetched:

- `solvekryptos.com` — primary purpose is publishing a claimed complete K4 plaintext.
- any site, blog, gist or video whose headline claims a complete K4 solution,
  "reconstructed plaintext", or "the answer to K4".

## Session 5 (Checkpoint E) — clean, no incidents

Historical research on the Weltzeituhr. `solvekryptos.com` was excluded on every
query. No claimed-solution site was used as a historical source. No purported K4
plaintext was sought, seen, or ingested.

Sources used for historical facts were: German and English encyclopaedia summaries,
Kunsch Metallbau's own reference page, Berlin tourism and local-history sites, and
long-running Kryptos *research* sites (Elonka Dunin mirror, rumkin, kryptosfan) for
the K0 Morse transcriptions only. The last three are research archives, not
solution-claim publishers, and were used only for text that has been public since
the 1990s.

One judgement call recorded for transparency: the K0 Morse fragments are community
transcriptions of publicly visible copper plates, not plaintext of any K section.
They are admissible. They are nonetheless graded below primary and EXP-023's result
is graded HEURISTIC NEGATIVE partly because of that.

## Incidents 2+ — none recorded.
