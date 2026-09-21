"""Independent assertions for the Checkpoint AI transcription dataset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "tableau_checkpoint_AI.json").read_text(encoding="utf-8"))

assert data["ideal_tableau"]["alphabet"] == "KRYPTOSABCDEFGHIJLMNQUVWXZ"
assert data["ideal_tableau"]["alphabet_length"] == 26
assert len(data["rows"]) == 28
assert [r["ideal_length"] for r in data["rows"]] == [30] + [31] * 26 + [30]
assert data["counts"] == {
    "ideal": 866,
    "official_textual": 867,
    "official_minus_ideal": 1,
    "verified_physical": None,
    "textual_extras": 1,
    "textual_omissions": 0,
    "textual_substitutions": 0,
}
assert len(data["differences"]) == 1
d = data["differences"][0]
assert (d["row_zero_based"], d["column_zero_based"], d["expected"], d["official"]) == (14, 31, None, "L")
n = data["rows"][14]
assert n["label"] == "N" and n["official"] == n["ideal"] + "L"
assert data["extra_terminal_L"]["physical_presence"] == "UNKNOWN"
assert data["extra_terminal_L"]["meaning_HILL"] == "NOT FORCED"
assert all(c["photograph_visible_symbol"] is None for r in data["rows"] for c in r["cells"])
assert data["decision"]["exp040_justified"] is False
print("PASS: 28 rows, 866 ideal chars, 867 CIA-text chars, one textual-only terminal L; no photo cell inferred")
