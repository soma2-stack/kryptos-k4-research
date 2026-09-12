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

## Session 6 (Checkpoint F) — clean, no incidents

Historical reconstruction of the Weltzeituhr. `solvekryptos.com` excluded on every
query. No claimed-solution site used. No purported K4 plaintext sought or seen.

Sources used: Berliner Zeitung (Dec 1997) and taz.de contemporary reporting on the
restoration and the Preszburg dispute; German and English encyclopaedia summaries;
Kunsch Metallbau's reference page; DDR-Bildarchiv, picture-alliance and Getty photo
archive listings. All admissible object/historical sources.

Noted for transparency: search summaries were asked repeatedly to enumerate the
146-name list and consistently DECLINED rather than inventing one. That is the
correct behaviour and no fabricated list entered the dataset.

## Session 7 (Checkpoint G) — clean, no incidents

The user supplied `weltzeituhr_modern_146_official.json`, independently retrieved
from the official Weltzeituhr Berlin site because this environment's egress policy
denies that domain. It is **object/history data, not K4 plaintext**, and is
admissible. Provenance (publisher, page title, URL, retrieval date, sha256) is
recorded in `data/weltzeituhr_modern_official.json`, and every record in it is
marked MODERN.

The file was validated before use — count, completeness, contiguity, duplicates —
and cross-checked against five facts this repository had established independently.
No historical field was overwritten with a modern value.

Sources used this session: the supplied official list; taz (July 2015); Tagesspiegel;
Berliner Zeitung; German and English encyclopaedia summaries. `solvekryptos.com`
excluded on every query. No claimed-solution site used. No purported K4 plaintext
sought or seen.

## Session 8 (Checkpoint H) — clean, no incidents

Photographic reconstruction. Historical photographs of the Weltzeituhr are admissible
object evidence. `solvekryptos.com` excluded on every query; no claimed-solution site
used; no purported K4 plaintext sought or seen.

Recorded for transparency: the user supplied a partial transcription of Bundesarchiv
`Bild 183-1989-0830-028` (CHABAROWSK | MAGADAN, SACHALIN) and explicitly asked that it
not be accepted blindly. This environment cannot fetch or view any image
(commons.wikimedia.org, upload.wikimedia.org, www.bundesarchiv.de and
live.staticflickr.com all return HTTP 000), so it could NOT be re-transcribed. It is
stored as USER-ASSERTED, NOT INDEPENDENTLY VERIFIED, and every downstream statement
derived from it carries that grade.

## Session 9 (Checkpoint H continued) — clean, no incidents

Input was `docs/external/checkpoint-H-web-photo-handoff.md`, added to the branch by
the user because this environment cannot reach the image hosts. All of it is
historical object evidence — Bundesarchiv frames, a WELT/akg press photograph, a
Berlin government publication, and one explicitly-modern comparison image.

Handled under the handoff's own rule: every transcription is recorded as an
EXTERNAL-AGENT TRANSCRIPTION, not this agent's visual verification. All image hosts
(commons.wikimedia.org, upload.wikimedia.org, www.bundesarchiv.de,
live.staticflickr.com, img.welt.de) remain unreachable, so nothing was
re-transcribed locally and no external reading was promoted to ground truth.

No claimed-solution site used. No purported K4 plaintext sought or seen.



## Session 10 (Checkpoint H, local visual) — clean, no incidents

Four photographs were pasted into the conversation by the user and read visually by this
agent. All four are historical/contemporary object evidence of a public monument. No
claimed-solution site was used, visited or cited; no purported K4 plaintext was sought,
seen or inferred. The only plaintext constraints in use remain EASTNORTHEAST and
BERLINCLOCK.

Two protocol points worth recording:

- The uploaded ZIP contained no image bytes, and its copy of the modern 146-place list is
  content-identical to the repo copy — so nothing new entered the corpus from it.
- Readings taken from the pasted images are marked LOCAL VISUAL EVIDENCE and supersede
  the EXTERNAL-AGENT handoff for the same faces. The images are conversation attachments
  with no path or hash, so they cannot be re-verified by a later session; that limitation
  is recorded in `data/weltzeituhr_photos.json` rather than being papered over.

A 97-letter coincidence was found on the CET face. It was graded OBSERVATION, NOT
EVIDENCE and explicitly refused as grounds for running EXP-024, precisely because
acting on it would be the failure mode this protocol exists to prevent.

## Session 11 (Checkpoint H, 1974 correction) — clean, no incidents

Input was `docs/external/checkpoint-H-1974-evidence-correction.md`: a WELT press page, an
akg/picture-alliance credit, a Tagesspiegel profile, and a Picture Alliance public
webseries listing. All historical object evidence and archive metadata about a public
monument. No claimed-solution site used or cited; no purported K4 plaintext sought or seen.

The handoff's own visual claim (KOPENHAGEN and WIEN legible in the 1974 frame) is stored as
an EXTERNAL-AGENT TRANSCRIPTION, not as my own reading — I have not seen that image. It was
accepted only for what it refutes, which is an interpretation, not a plaintext.

Worth recording as protocol: this correction cut *against* the programme's preferred
hypothesis, and was incorporated in full. Two of my own session-10 conclusions were
retracted rather than defended.

## Session 12 (Checkpoint H, Tier 1 met) — clean, no incidents

Three 4 Nov 1989 photographs were uploaded and read visually by this agent. Historical press
images of a public monument and a public demonstration. No claimed-solution site used or
cited; no purported K4 plaintext sought or seen. Cribs used: EASTNORTHEAST and BERLINCLOCK only.

Protocol points worth recording:

- The Tier-1 reconstruction was **frozen in the dataset before any test ran**, with its
  confidence grades and stated risk, and EXP-029 cites it verbatim. It cannot be retuned to a
  result after the fact.
- EXP-024 was left unmodified and was not re-run; the restricted run is a separate experiment.
- Two alignments reached 7/24 cribs (Poisson p ≈ 0.03 on a post-hoc maximum). **The external
  verifier was not consulted**, and the blip was recorded rather than pursued.
- The session's main finding is a retraction of the programme's most attractive prior
  observation: the 97-letter coincidence was my own transcription error. It had been graded
  OBSERVATION, NOT EVIDENCE and refused as grounds to run the test, which is the only reason
  nothing downstream was built on it.

## Session 13 (Checkpoint K, branch claude/k4-post-j) — clean, no incidents

Inputs were repository state at the Codex Checkpoint J head and five external Perplexity
research documents. All of it is documentary research about published sources: NSA
declassified PDFs, two 2005 WIRED interviews, a 2009 WIRED feature, and a picture-agency
collection page. No claimed-solution site was used or cited; no alleged K4 plaintext,
solution dump, or private K5 material was sought, accessed or inferred. Cribs used:
EASTNORTHEAST and BERLINCLOCK only.

Two protocol points:

- Two attempts to fetch primary sources (`www.nsa.gov`, `media.defense.gov`) were refused
  by the proxy with 403. The missing material was written up as an exact external evidence
  request in `docs/external-evidence-requests.md` rather than reconstructed from memory —
  specifically the K1–K3 cipher-side transcription, which I do know approximately and
  deliberately did not write down, because an approximate transcription is what produced
  the retracted LONDON misreading at Checkpoint H.
- Preregistrations for EXP-032/033/034 were committed before implementation, and each
  names its prohibited post-hoc expansions. No result was tuned around.

## Session 14 (Checkpoint L, branch claude/k4-post-j) — clean, no incidents

Input was the fulfilled evidence request: the CIA Panel 1 cipher-side text version with NSA
corroboration, supplied in `docs/external/checkpoint-K-nsa-cipher-rows-1-24.md`. This is
public *ciphertext* and public institutional transcription. No claimed-solution site was
used or cited; no alleged K4 plaintext, solution dump, or private K5 material was sought,
accessed or inferred. Cribs used: EASTNORTHEAST and BERLINCLOCK only.

Protocol points:

- The supplied transcription was verified before use rather than accepted, and three
  independent corroborations are recorded in `data/cipher_side_rows.json` alongside one
  discrepancy left explicitly UNRESOLVED.
- The physical alignment model was **parked** rather than rescued with an invented lattice,
  and the reasoning is recorded in the EXP-035 preregistration so it can be checked.
- `k12` (rows 1–14) is flagged in the data and in every verdict that touches it, because of
  the unresolved 432-vs-435 letter count.

## Session 15 (Checkpoint M, branch claude/k4-post-j) — clean, no incidents

Input was `docs/external/checkpoint-L-web-audit-requests-4-5.md`: CIA and NSA primary
transcription and solution material, two WIRED reports, a Library of Congress catalogue
record, and a Smithsonian finding aid. All public documentary evidence. No
claimed-solution site used or cited; no alleged K4 plaintext, solution dump, or private K5
material sought, accessed or inferred. Cribs used: EASTNORTHEAST and BERLINCLOCK only.

Protocol points:

- Both corrections in the handoff were **verified against repository data before use**, and
  both turned out to be corrections of my own errors rather than of the evidence.
- The physical/intended source distinction is now recorded explicitly: the omitted `X`
  Sanborn removed from a K2 line belongs to an *intended pre-aesthetic* source and will
  only ever be tested as a separately preregistered source variant, never inserted
  silently into the physical stream.
- Candidate A (alphabets built from PALIMPSEST/ABSCISSA) was **rejected for lack of
  documentary support**, not tested speculatively — the same gate that admitted EXP-036.

## Session 16 (Checkpoint O, branch claude/k4-post-j) — clean, no incidents

Symbolic audit session. Inputs were the repository's own data and published descriptions of
classical ciphers. No claimed-solution site used or cited; no alleged K4 plaintext, solution
dump, or private K5 material sought, accessed or inferred. Cribs used: EASTNORTHEAST and
BERLINCLOCK only.

Protocol points:

- Two cipher families were closed by exact structural arguments and **no search was run** on
  either, in line with the session's conservative budget rule.
- Where I lacked an authoritative offline definition — Digrafid's block ratio, the ACA
  columnar Gromark alphabet — I said so and routed around it rather than reconstructing a
  "standard" from memory.
- A near-miss was recorded and deliberately not pursued: EASTNORTHEAST fits Fractionated
  Morse exactly at 39 = 13x3, while BERLINCLOCK in the same message fails by 11.

## Session 17 (Checkpoint P, branch claude/k4-post-j) — clean, no incidents

Input was an external evidence handoff citing contemporaneous New York Times reporting, an
NPR interview transcript, and a reporter's public confirmation, all concerning the *positions*
of Sanborn's published clue words. Public reporting about public clues; no alleged K4
plaintext, purported solution, or private K5 material was sought, accessed or inferred beyond
the four already-public clue words this repository has always used.

Protocol points:

- The handoff's positional claims were re-derived against the committed ciphertext before
  acceptance; no crib text or index changed.
- The four clue releases were graded separately rather than flattened; `EAST` is recorded at
  B+ because its position is inferred from "immediately before NORTHEAST".
- The upgrade was propagated only as far as the evidence licenses: the Fractionated-Morse
  rejection was made unconditional against the *published* semantics and explicitly not
  generalised, and the lifted Playfair/reflector contingency was checked against the directly
  numbered spans rather than assumed.

## Session 18 (Checkpoint Q, branch claude/k4-post-j) — clean, no incidents

Pure computation on repository data: the public ciphertext, the public-verified crib
positions, and an ordinary classical-cipher construction. No claimed-solution site used or
cited; no alleged K4 plaintext, purported solution, or private K5 material sought, accessed or
inferred.

Protocol points:

- The family-structure and null figures were computed **without touching the real target
  vectors**, so the information-gain gate was decided before the experiment could see its
  answer; the preregistration was committed before implementation.
- A stale input hash in the first draft of the preregistration was corrected **before
  execution**, with the substitution recorded in the file rather than silently swapped.
- F1 and F2 were admitted together in advance specifically so that a negative on F1 could not
  be followed by adding the affine term as a rescue.

## Incidents 2+ — none recorded.

## Codex Checkpoint I — no plaintext contamination incident

Audited the specified commit and tested only the existing public crib constraints.
Synthetic controls use X filler; no candidate full plaintext was ingested. Exact-ID
archive searches for the three supplied photo targets yielded no usable image.
One archive snippet and unrelated numeric-ID search matches were returned; no
claimed-solution source was accessed and no new historical transcription was added.
No external verifier submission. See codex-image-request.md for the paused evidence task.

## Codex Checkpoint J — clean historical image evidence

Three supplied images inspected. Publisher previews and a larger bpb source were
retrieved only via the exact historical archive links already in the repository.
No modern list, claimed K4 solution, leaked text or extra plaintext assumption was
used. ATHEN absence retracted from direct pixels. Reconstruction and EXP-031
preregistration published before execution; checksum repair of two transferred
JPEGs completed before scoring. 384 synthetic X-filler controls, public cribs only.
No external verifier contacted.
