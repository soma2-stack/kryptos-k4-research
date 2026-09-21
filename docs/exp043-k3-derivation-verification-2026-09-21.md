# EXP-043 K3-derivation verification correction — 2026-09-21

This prospective correction closes the repository-audit gap without rewriting the historical
EXP-043 record.

## What is now independently reproducible

`audit/verify_exp043_k3_derivation.py` imports neither EXP-043 nor `k4lib`. Using only the
repository's declared K3 plaintext and the cipher-side rows, it applies one explicit double-rotation
route:

1. write the 336 plaintext letters row-major into **8 x 42**;
2. read columns left-to-right, each **bottom-to-top**;
3. write that stream row-major into **24 x 14**;
4. again read columns left-to-right, each **bottom-to-top**.

That route reproduces the committed 336-letter K3 ciphertext exactly. Applying the same route to
unique integer position tokens removes all repeated-letter ambiguity and yields a concrete
plaintext-position -> ciphertext-position permutation with:

- successive differences modulo 336 exactly **{191, 192}**;
- cycle type exactly **168 + 168**;
- permutation order **168**;
- not an involution;
- permutation SHA-256
  `c28c37b7c62aa873e60fab9566b76c01e7a2851cc15d9672bc5b6fa4167e01e4`.

These are now directly testable claims in the repository.

## What is no longer load-bearing

The historical EXP-043 report says a scratch search found **12 exact rectangular-route
descriptions** that all induce the same permutation. That scratch route-enumeration procedure was
not committed, so the number 12 is retained as historical reporting but is **not required** for
the EXP-043 motivation or result.

The current load-bearing statement is narrower:

> the repository's declared K3 plaintext/ciphertext pair is reproduced exactly by an explicit
> double-rotation route, and the resulting position permutation has the 191/192 and 168+168
> properties independently verified above.

## Provenance boundary

This does **not** silently upgrade K3 plaintext provenance. `data/mask_sources.json` still marks
`K3_plaintext` as `verified: false`. The verifier deliberately checks and prints that condition.

Therefore EXP-043 should be read in two layers:

1. **Scoped cryptanalytic result:** the registered affine-mod-97 sandwich family is negative.
2. **K3-derived motivation:** reproducible from the repository's declared K3 plaintext, but the
   plaintext string itself still needs a separately frozen primary/public provenance record before
   the motivation can be called primary-source-verified.

K4 remains unsolved.
