#!/usr/bin/env python3
"""Fast, non-destructive repository smoke test.

This is intentionally NOT a full experiment regeneration. It checks canonical data,
machine-readable handoff integrity, current-state guards, modern result artifacts, and
the independent K3 derivation verifier.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
fail = []


def check(label, cond, detail=""):
    mark = "PASS" if cond else "FAIL"
    print(f"[{mark}] {label}" + (f": {detail}" if detail else ""))
    if not cond:
        fail.append(label)


# Canonical K4 data.
sys.path.insert(0, ROOT)
from k4lib.data import load
k4 = load()
for label, ok, detail in k4.verify():
    check(f"k4lib.data::{label}", ok, detail)

# Machine-readable cipher-side state.
rows_path = os.path.join(ROOT, "data", "cipher_side_rows.json")
rows = json.load(open(rows_path))
check("cipher-side total is 869", rows["verification"]["total_characters"] == 869)
check("432-vs-435 issue is prospectively resolved",
      rows["verification"].get("resolved_correction", {}).get("status") == "RESOLVED")
check("stale open_discrepancy key absent", "open_discrepancy" not in rows["verification"])

# Modern result artifacts must exist and parse.
for n in range(30, 44):
    p = os.path.join(ROOT, "results", f"exp{n:03d}", "summary.json")
    check(f"EXP-{n:03d} summary exists", os.path.isfile(p))
    if os.path.isfile(p):
        try:
            obj = json.load(open(p))
            check(f"EXP-{n:03d} summary id", obj.get("experiment") == f"EXP-{n:03d}")
        except Exception as exc:
            check(f"EXP-{n:03d} summary parses", False, repr(exc))

# Current-state guards should exist.
guards = {
    "README.md": "CURRENT STATE — 2026-09-21",
    "docs/research-state.md": "CURRENT-STATE NOTICE — 2026-09-21",
    "docs/next-steps.md": "CURRENT-STATE NOTICE — 2026-09-21",
    "docs/resume-prompt.md": "CURRENT RESUME CONTRACT — 2026-09-21",
    "AUTONOMOUS_SCOUT.md": "HISTORICAL / FROZEN LUNA SCOUT CONTRACT",
}
for rel, needle in guards.items():
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read(4096)
    check(f"{rel} guarded against stale-current use", needle in text)

# Independent K3 derivation verifier; standard library only.
proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "audit", "verify_exp043_k3_derivation.py")],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
print("\n--- verify_exp043_k3_derivation.py ---")
print(proc.stdout.rstrip())
check("independent EXP-043 K3 derivation verifier exits cleanly", proc.returncode == 0)

print()
if fail:
    print("SMOKE: FAIL")
    for x in fail:
        print(" -", x)
    raise SystemExit(1)
print("SMOKE: PASS")
