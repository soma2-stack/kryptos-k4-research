# Checkpoint U1 — 2025 primary-source provenance repair

Date: 2026-09-13
Branch: `claude/k4-post-j`
Parent checkpoint: Checkpoint U (`a96aeb2ef41a2c71c618bb5195cad2c2e4b1bdd2`)

## Purpose

Checkpoint U correctly separated the K4 problem into:

- **Layer A** — the 97-character plaintext-to-ciphertext transformation; and
- **Layer B** — the instruction/riddle conveyed by the recovered plaintext.

However, Checkpoint U's own environment could not fetch several primary/public sources and therefore graded all 2025 material no higher than C+/B- and marked the August 2025 WIRED claim (U9) unverified.

A subsequent independent verification session obtained the actual public sources. This note repairs that provenance prospectively. Historical Checkpoint U is not rewritten.

## Verified source 1 — WIRED, 14 August 2025

Source:
`https://www.wired.com/story/jim-sanborn-auctions-kryptos-key/`

Steven Levy, WIRED, 14 August 2025, *The Kryptos Key Is Going Up for Sale*.

The article explicitly reports that:

1. Sanborn had indicated that the text of K4 is **an instruction for how to solve it**.
2. The instruction may involve **other parts of the installation** besides the encrypted copper screen.
3. Sanborn directly told Levy that attaining the complete solution **does not require physical access to CIA grounds**.
4. The article quotes Sanborn's August statement that even when K4 has been solved, its riddle will persist as K5.

This directly resolves Checkpoint U's U9 provenance gap. The August 2025 WIRED item exists and supports the incoming brief's core claim.

### Grade

- Article existence/date/authorship: **A/B public-source provenance**.
- Levy's direct report of what Sanborn told him about physical access: **B+ direct attributed reporting**.
- Levy's wording that Sanborn had indicated the plaintext is an instruction: **B secondary reporting**, not a verbatim Sanborn quotation.

## Verified source 2 — WIRED Sanborn Q&A, January 2005

Source:
`https://www.wired.com/2005/01/questions-for-kryptos-creator/`

The published Q&A is explicitly a partial transcript edited for length and organization.

It directly asks whether a solver must be on CIA grounds to solve Kryptos. Sanborn answers **No**.

He then distinguishes this from a possible physical consequence/referent of the decrypted text: a solver can solve from the published text, while what the plaintext refers to may require going to the agency to observe or find something.

The same Q&A also states that Scheidt supplied historical/contemporary encoding systems and ways to modify them, while Sanborn says he modified systems and developed his own.

### Consequence

There is **no 2005-versus-2025 reversal on remote solvability**. Checkpoint U's apparent contradiction came from over-reading the later sentence about deciphering and then going to the agency while missing the explicit preceding Q&A that says physical presence is not required to solve the cryptography.

The correct reconciliation is:

> **Layer A can be solved remotely; Layer B may refer to, affect, or require interpretation of a physical feature at the installation.**

This strengthens rather than weakens the two-layer model.

## Verified source 3 — Sanborn August 2025 open letter

Source:
`https://www.elonka.com/kryptos/OpenLetterAug2025.html`

This page reproduces Jim Sanborn's August 2025 open letter. It contains the public clue language concerning secrecy/power and states that K4's riddle persists into K5.

The direct-authored/open-letter material therefore should not be treated merely as an unattributed search-result paraphrase.

### Grade

**B+/A- documentary provenance for the public letter text as reproduced by the long-running Kryptos archive**, while preserving that the hosting page is not Sanborn's own domain.

## What changes from Checkpoint U

1. **U9 is no longer UNVERIFIED.** The August 2025 WIRED article is real and supports the proposition that K4's plaintext functions as an instruction and that complete solution does not require physical access to CIA grounds.
2. The two-layer model becomes **stronger**:
   - decrypting K4 is Layer A;
   - executing/interpreting the recovered instruction is Layer B.
3. The 2005 material is not evidence that Layer A requires CIA-site access. It explicitly says the opposite.
4. Artistic/physical referents remain poor Layer A key-source evidence. Their natural role is increasingly Layer B unless a source explicitly connects one to the encryption transform.
5. The negative results of EXP-002/018/023/024/029/031/035 remain unchanged.
6. No new position-specific K4 plaintext letter is supplied.
7. No source identifies a transform, key schedule, key source, or composition order.

## EXP-040 gate

The provenance repair improves evidence quality but does **not** create a bounded Layer A architecture.

- documentary support for the Layer A/Layer B separation: strengthened;
- exact transform: absent;
- bounded parameter space: absent;
- new crib power: absent.

**NO EXP-040 JUSTIFIED.**

## Contamination

No 2025 plaintext-discovery article, reconstructed plaintext, claimed solution, auction-secret material, private K5 plaintext/ciphertext, or quarantined solver material was used in this repair.

K4 remains unsolved.
