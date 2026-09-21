# Checkpoint AF — `ScheidtNova.doc` retrieval attempt and archival route ledger

**Date:** 2026-09-13. **Branch:** `claude/k4-post-j`. **Starting HEAD:** `7fbe7342a9351fb5ae8577b96016429a79317776`.

Documentary evidence recovery only. No cipher experiment, no keyspace search, no EXP-040.

## Outcome, stated plainly

**The `ScheidtNova.doc` payload was NOT recovered.** No faithful mirror was retrieved either.
No transcript content is quoted, paraphrased or inferred anywhere in this note, and none may be
inferred from the filename, the index metadata, or from search-engine snippets.

**This is a retrieval failure, not a finding about the cipher.** Nothing about K4's structure
follows from it.

## Why: the constraint is environmental, not archival

Outbound HTTPS from this session is governed by an organization egress policy. Every external
host tested was refused at the CONNECT stage with a gateway **HTTP 403**, including hosts that
are certainly live and public. The proxy's own status endpoint records these as
`connect_rejected — gateway answered 403 to CONNECT (policy denial or upstream failure)`, and
`/root/.ccr/README.md` instructs that policy denials must be reported rather than retried.

Confirmed blocked at the tunnel, by direct `curl` and by the fetch tool alike:

`elonka.com`, `www.elonka.com`, `web.archive.org`, `archive.org`, `www.pbs.org`, `dipsy.pbs.org`,
`openvault.wgbh.org`, `americanarchive.org`, `kryptosinfo.wordpress.com`, `video.wcmu.org`,
and `www.google.com`.

The only working channel is a search tool that returns **result summaries**, never file payloads.
It therefore cannot retrieve a `.doc`, and its summaries must not be treated as transcript text.

**Consequence: the earlier HTTP 401 observed by the supervisor on the direct link could not be
re-tested or characterised from here.** Whether that 401 reflects a deliberate access control, a
host reconfiguration, or a transient state remains **unresolved**, and this session adds no
evidence either way.

## Route ledger

Classified exactly as instructed. "Blocked" means blocked *from this environment* and says
nothing about public availability.

| # | Route | Classification | Note |
| --- | --- | --- | --- |
| 1 | `https://elonka.com/x/ScheidtNova.doc` (direct) | **BLOCKED / INACCESSIBLE** | gateway 403 at CONNECT; the supervisor separately observed 401 from the origin |
| 2 | `https://www.elonka.com/x/ScheidtNova.doc` | **BLOCKED / INACCESSIBLE** | same |
| 3 | `https://elonka.com/x/videos.html` (index re-check) | **BLOCKED / INACCESSIBLE** | index metadata already recorded at Checkpoint AE and unchanged |
| 4 | Wayback Machine `web.archive.org` | **BLOCKED / INACCESSIBLE** | not a statement about whether a capture exists |
| 5 | Wayback availability API `archive.org/wayback/available` | **BLOCKED / INACCESSIBLE** | returned gateway 403, not an archival answer |
| 6 | Aired PBS/NOVA transcript `3411_sciencen.html` | **BLOCKED / INACCESSIBLE** | content already summarised in the repository from earlier sessions |
| 7 | `dipsy.pbs.org` NOVA Kryptos page | **BLOCKED / INACCESSIBLE** | |
| 8 | GBH Open Vault `openvault.wgbh.org` | **BLOCKED / INACCESSIBLE** | catalog record identified by search only, see below |
| 9 | American Archive of Public Broadcasting | **BLOCKED / INACCESSIBLE** | |
| 10 | `kryptosinfo.wordpress.com` (community transcript pages) | **BLOCKED / INACCESSIBLE** | surfaced in search; payload unreachable |
| 11 | Exact-filename search for `ScheidtNova.doc` mirrors | **SEARCHED — no mirror identified** | no indexed copy of the payload surfaced; absence of a search hit is weak evidence and is **not** "confirmed no payload" |
| 12 | GBH Archives direct outreach | **DELIBERATELY NOT PERFORMED** | a request from the user is already pending; no duplicate outreach was sent |

**Nothing in this ledger is "confirmed no payload."** Every negative is either
*blocked from here* or *not surfaced by one search*.

## New institutional leads recorded (not pursued)

Two concrete records surfaced in search that the repository did not previously hold. Both are
**leads with catalog-level provenance only**; neither payload was retrieved, and neither is
claimed to contain the Scheidt B-roll transcript.

1. **GBH Open Vault catalog record** for the NOVA scienceNOW episode carrying the Kryptos
   segment, identifier `V_3AC501960CC4454A8FD950703CBED5A9`. Useful because it gives the GBH
   request already in flight a precise catalog handle rather than a programme description.
2. **UGA Brown Media Archives / Peabody Awards Collection**, a *physical object* record for
   `Nova scienceNOW [No. 3411, 2007-07-24]`. This is a **genuinely independent custodian** from
   GBH, so it is the strongest unexplored route that does not duplicate the pending request.

Grade for both: **B — catalog-level existence and custody only.** Neither establishes that a
B-roll or logging transcript is held, processed, or releasable.

A search summary rendered the air date as `07/05/2007` against the repository's `24 July 2007`
and the PBS transcript number `3411`. This is recorded as a **search-summary artifact**, not a
finding. Per protocol no date is treated as a cryptographic clue.

## Contamination boundary held

Search results surfaced at least one site advertising a B-roll transcript said to disclose
"actual techniques and concepts about K4", and others in the solution-adjacent cluster. **None
was accessed**, none is cited, and nothing from those summaries entered the analysis. No alleged
full K4 plaintext, leaked or reconstructed solution, auction-secret material or private K5
material was searched for, fetched, quoted or inferred.

## Effect on Checkpoint AE

**None. Checkpoint AE stands unchanged, and no EXP-040 is justified.**

The census blockers are untouched: no source has yet supplied an operational definition of
masking, a stage order, a named structured stage, a parameter-sharing rule, a period or key
length, an inheritance rule from K1–K3, reset/alignment behaviour, or what Sanborn changed.

Request 2 remains split exactly as Checkpoint AE recorded it:

1. **`ScheidtNova.doc` — LOCATED in the public index, CONTENT NOT RETRIEVED.**
2. **Unedited 2005 Zetter/WIRED Scheidt material — NOT LOCATED.**
