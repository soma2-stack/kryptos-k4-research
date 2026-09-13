# Checkpoint AE follow-up — Request 2: `ScheidtNova.doc` public location identified

**Date:** 2026-09-13  
**Branch:** `claude/k4-post-j`  
**Starting HEAD:** `827b3743502cce0144cbd5f8144e62175e5717da`

This is an evidence-location note only. No cryptanalytic experiment was run and no K4 plaintext or solution material was accessed.

## Finding

`ScheidtNova.doc` is not merely an internal GBH filename. Elonka Dunin's public Kryptos media archive explicitly lists:

- `ScheidtNova.doc`
- filmed: 2005
- description: **PBS B-roll transcript of the 2006 NOVAscienceNOW segment: Interview with Ed Scheidt**
- size: **140K**
- posted: **2009-02-13**

Archive index:

`https://elonka.com/x/videos.html`

Direct file target:

`https://elonka.com/x/ScheidtNova.doc`

The archive index also lists the companion `SanbornNova.doc` as a 220K PBS B-roll transcript from the same production context.

## Retrieval status

The archive index is publicly visible and independently searchable, so the document's existence, filename, description, approximate size, and posting date are established.

However, in the present environment the direct `.doc` request returns HTTP 401. Therefore **the full contents have not yet been retrieved here** and must not be quoted or inferred from the filename alone.

Request 2 should now be split into two states:

1. **`ScheidtNova.doc` — LOCATED, CONTENT NOT YET RETRIEVED.**
2. **Unedited 2005 Kim Zetter / WIRED Scheidt interview material — still NOT LOCATED.**

The email request already sent to GBH remains useful because GBH may be able to supply the production transcript or source media even if the old public `.doc` link no longer serves directly.

## Public corroboration from the aired NOVA transcript

PBS still hosts the aired July 24, 2007 NOVA scienceNOW transcript. It confirms that the production used Scheidt interview material and includes, among other lines:

- Scheidt explaining that he "set the codes out" for Sanborn;
- Scheidt describing classical cryptography in terms of substitution and transposition;
- Scheidt stating that the first challenge is determining what **masking technique** was used.

Public PBS transcript:

`https://www.pbs.org/wgbh/nova/transcripts/3411_sciencen.html`

These aired excerpts are documentary background only. They do **not** substitute for the full B-roll transcript, because the whole point of Request 2 is to recover material omitted from the edited broadcast/article.

## Additional public mirror evidence

A large public interview/article compilation on Scribd contains the full Sanborn NOVA B-roll transcription and the aired NOVA transcript. It corroborates the production context, but no claim is made here that it contains the complete Scheidt B-roll transcript.

## Why this matters after Checkpoint AE

Checkpoint AE found that no presently open architecture is both documentary-motivated and decisively testable with the 24 published crib letters. The missing information needed to turn the census into a finite experiment is unusually specific:

- a statement naming a **structured stage whose parameters are shared across positions**, or
- a **period / key-length / inheritance rule**.

Generic statements such as "masked", "custom", "complex", "modern", or "different" are not enough.

Therefore, if `ScheidtNova.doc` is recovered, the first pass should be narrow and documentary:

1. preserve the transcript verbatim;
2. distinguish interviewer wording from Scheidt's exact words;
3. extract only explicit statements about process structure, period/key reuse, parameter sharing, ordering of stages, or inheritance from K1-K3;
4. do not mine casual wording, timestamps, numbers, or prose as hidden clues;
5. do not launch an experiment unless the statement actually narrows the Checkpoint AE census to a finite, preregisterable family.

## Contamination boundary

Safe: public interview transcripts, broadcast material, production metadata, and explicit historical/process statements.

Excluded: alleged K4 plaintext, purported solution dumps, private K5 material, or solution-adjacent claims.

K4 remains unsolved.
