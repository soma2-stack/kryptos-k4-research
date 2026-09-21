# Checkpoint AN — Scheidt steganography-related component

**Date:** 2026-09-21  
**Branch:** `claude/dreamy-archimedes-79k6u0`  
**Classification:** NEW documentary constraint, medium-high confidence  
**Cryptanalytic status:** K4 remains unsolved; no new plaintext letter or exact algorithmic parameter is authenticated.

## Result

A repository-new public statement attributed directly to Ed Scheidt establishes a narrow structural fact:

> “I also stated that there was a piece relating to Stego, but did not state how or in what context.”

The surviving source is John B. Wilson, *John's Collected Kryptos Hints*:
https://scirealm.org/KryptosHints.html

The page explicitly labels the original approximately September 17–18, 2004 talk report as unreliable, then says parts were later confirmed directly and preserves the more cautious Scheidt clarification quoted above.

## Admitted constraint

**K4 contains a steganography-related component.**

The admissible formulation is deliberately narrow:

- a component or “piece” relates to steganography;
- Scheidt explicitly withheld how it operates and in what context.

## What is NOT established

This does **not** establish:

- a separate preprocessing stage;
- whether steganography is before or after encryption;
- whether the steganographic component is the entire masking technique;
- the carrier;
- null insertion or deletion;
- acrostics;
- grille methods;
- binary encoding;
- route selection;
- transposition;
- punctuation use;
- physical-layout use;
- a period;
- a key length;
- an alphabet;
- a reset rule;
- a recurrence;
- an alignment rule.

Do not promote any specific steganographic mechanism from this statement alone.

## Provenance grade

**Medium-high.**

Strengths:
- exact quotation attributed to Scheidt;
- surviving public page distinguishes the unreliable talk notes from Scheidt's later clarification;
- the clarification is materially more cautious than the original reported phrase.

Limitation:
- the original Scheidt email/message/correspondence and its metadata have not been recovered;
- therefore this is not yet a highest-grade primary-document provenance chain.

A recovered original email, header, letter, or other direct correspondence would upgrade provenance.

## Relationship to existing evidence

This sharpens, but does not replace, the already authenticated facts that:

- K4 is more than one stage;
- K4 masks or removes ordinary English-language advantages;
- the exact masking mechanism and stage order remain undisclosed.

The new fact is more specific than generic “masking”: Scheidt identifies a steganography-related component, while explicitly refusing to say how or where it participates.

## Cryptanalytic consequence

This is a **class-level filter**, not yet an experiment selector.

It raises the prior weight of architectures in which one stage or subcomponent performs concealment/steganographic hiding, but the statement supplies no finite carrier, rule, transform, period, or ordering. Therefore it does not by itself justify EXP-044.

Any future candidate that claims to instantiate this evidence must state exactly:
1. what object carries the steganographic relation;
2. why that carrier is independently motivated;
3. how the proposed rule is finitely parameterised and falsifiable by the authenticated evidence.

## Plaintext target status

No new authenticated plaintext character was recovered at zero-based positions
`1, 3, 91, 93, 95, 96`.

## Contamination

No claimed full K4 plaintext, solution method, auction-secret material, or private K5 material is admitted by this checkpoint.
