# Checkpoint AM — attempted primary-audio authentication of the disputed 2015 "periodic" exchange

**Branch:** `claude/dreamy-archimedes-79k6u0`
**Date:** 2026-09-21

## VERDICT

`UNRESOLVED`

**Periodicity is NOT promoted into the K4 constraint set.** It remains inadmissible, exactly as before this checkpoint.

The classification must be read precisely. This is **not** "we listened and the audio was ambiguous." It is:

> **UNRESOLVED — PRIMARY SOURCE NOT REACHABLE FROM THIS ENVIRONMENT.**

No audio was obtained, so no audio was assessed. Every one of the four open points
(exact wording, referent of "it", speaker identity, polarity of the answer) is
untouched by this checkpoint and remains open.

## 1. What was attempted

Target: YouTube `25YFYKKKkDo`, interval ~46:50–48:30. Listening aid: `sK6w9rpgrJ4`.

| Channel | Result |
|---|---|
| `curl https://www.youtube.com/watch?v=25YFYKKKkDo` | `CONNECT tunnel failed, 403` |
| `yt-dlp --write-auto-sub` (installed successfully from PyPI) | all 3 retries `403 Forbidden` at the proxy |
| `WebFetch` on the same URL | `EGRESS_BLOCKED: www.youtube.com` |
| `youtu.be` | unreachable (`000`) |
| `WebFetch` Cipherbrain/Schmeh transcript page (`scienceblogs.de`) | `EGRESS_BLOCKED` |
| `web.archive.org`, `inteltoday.org`, `thekryptosproject.com` | all unreachable (`000`) |
| public repo `doranchak/kryptos` (cloned, grepped, deleted) | contains **no** workshop transcript |

The agent proxy's own status endpoint records the denial:

```
"kind": "connect_rejected",
"detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
"host": "www.youtube.com:443"
```

This is a deliberate network egress policy, not a transient failure. Retrying it
in a future session on the same environment will produce the same 403.

## 2. Two independent blockers, not one

Even had the audio been reachable, a second blocker applies and must be recorded
so that a future worker does not mistake "get the file" for "solve the problem":

1. **Egress.** The audio cannot be downloaded here.
2. **Perception.** This agent has no audio input channel. Authenticating voice
   timbre, cadence, microphone position and turn-taking — which is what the
   speaker-attribution question actually requires — is not something a
   text-only agent can do at all. An offline ASR model would substitute a
   *second machine transcript* for the first, which is precisely the evidence
   class the supervisor has already ruled insufficient; and in any case
   `huggingface.co` is likewise blocked, so no weights can be fetched.

**Resolving blocker 1 alone would not resolve this question.** Speaker
attribution needs a human ear, or a source that carries authenticated speaker
labels.

## 3. What remains unestablished

All four, unchanged:

1. that the question is audible as "Would you consider it periodic?";
2. that "it" denotes K4's cipher mechanism (and not the mask, one stage, or
   — the live confusion — the *punctuation* sense of "period" that the same
   conversation demonstrably uses at ~46:23–46:40);
3. that Ed Scheidt is the respondent;
4. that the answer is affirmative.

Checkpoint X already recorded that the environment "could identify and source the
original video, but could not stream or directly inspect the audio track." That
limitation is re-confirmed, now with explicit proxy-level evidence.

## 4. Standing instruction for future workers

- Do **not** re-run this audio pass on this environment. The block is policy-level
  and the perception blocker is structural. Repeating it burns budget and
  returns this same page.
- Do **not** treat the machine transcript's "Would you consider it periodic?" /
  "Yeah." as evidence of anything. It has no authenticated speaker labels and it
  sits inside a gap in the only human-prepared transcript (Richard Bean /
  Cipherbrain, which runs to ~47:35 and resumes ~48:16).
- The block lifts only on a **genuinely better source**, which means one of:
  - a network environment whose egress policy permits the recording, **plus a
    human listener**; or
  - a human-prepared transcript that covers 47:35–48:16 **with speaker labels**; or
  - a direct statement from a workshop participant identifying who said what.

## 5. Consequence for the constraint set

`KNOWN_STATE.md` is unchanged with respect to periodicity. "K4 is periodic" is
**not** authenticated evidence. The authenticated 2015 workshop content remains
what Checkpoint X established: K4 is **more than one stage**, and masking is part
of Layer A. Nothing about a period, a period value, a reset rule or a schedule is
licensed by this recording.
