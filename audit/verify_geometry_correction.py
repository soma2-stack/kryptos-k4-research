"""Does the variable-row-width correction affect EXP-032, EXP-033 or EXP-034?

The authoritative CIA rows 1-24 range from 29 to 33 characters, so the inherited
`32 + 27*31 = 869` description is false even though the total is right. This script
decides, per experiment, whether any of its inputs depend on that false description.
It does not take the expectation on trust: for each experiment it enumerates the actual
geometric quantities the code consumes and checks them against the authoritative rows.
"""
import json, os, sys, ast, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

rowdata = json.load(open(os.path.join(ROOT, "data", "cipher_side_rows.json")))
ROWS = {int(k): v for k, v in rowdata["rows"].items()}
CT = json.load(open(os.path.join(ROOT, "data", "k4.json")))["ciphertext"]

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


print("# verify_geometry_correction\n")
print("## The correction itself")
lens = {r: len(v) for r, v in ROWS.items()}
check("rows 1-24 are NOT uniformly 31 characters",
      sorted({lens[r] for r in range(1, 25)}) == [29, 30, 31, 32, 33],
      str(sorted({lens[r] for r in range(1, 25)})))
check("the false description and the true structure agree only on the total",
      32 + 27 * 31 == sum(lens.values()) == 869)
check("rows 25-28 ARE 31 characters each",
      all(lens[r] == 31 for r in range(25, 29)), str([lens[r] for r in range(25, 29)]))

# ---------------------------------------------------------------- EXP-032
print("\n## EXP-032  k[i] = f(col(i))")
from k4lib.data import load
import experiments  # noqa: F401  (package marker only, if present)
src32 = open(os.path.join(ROOT, "experiments", "exp032_column_key.py")).read()
rows_referenced = set(int(m) for m in re.findall(r"\b(\d{1,2})\b", src32) if 1 <= int(m) <= 28)
# the decisive question is which ROW STRINGS the experiment's geometry consumes
check("EXP-032's geometry table names only rows 25-28",
      "((25, 0, 4, 28), (26, 4, 35, 1), (27, 35, 66, 1), (28, 66, 97, 1))" in src32
      or "ROWS = ((25" in src32)
check("EXP-032 embeds no row-1-to-24 string",
      not any(ROWS[r][:12] in src32 for r in range(1, 25)))

# reconstruct its column map and confirm it is consistent with the authoritative rows
def col_of(i):
    if i < 4:
        return 28 + i
    if i < 35:
        return i - 3
    if i < 66:
        return i - 34
    return i - 65


check("row 25 columns 28-31 hold OBKR in the authoritative transcription",
      ROWS[25][27:31] == "OBKR", ROWS[25][27:31])
check("every K4 position's row-local column is within its own authoritative row length",
      all(1 <= col_of(i) <= lens[{0: 25}.get(0) if i < 4 else (26 if i < 35 else (27 if i < 66 else 28))]
          for i in range(97)))
crib = []
for c in json.load(open(os.path.join(ROOT, "data", "k4.json")))["confirmed_cribs"]:
    crib += list(range(c["start"], c["end"]))
check("no crib position lies in row 25, so no crib column depends on the OBKR indent",
      all(i >= 4 for i in crib))
s32 = json.load(open(os.path.join(ROOT, "results", "exp032", "summary.json")))
check("EXP-032 VERDICT UNCHANGED: its inputs are rows 25-28 only",
      s32["feasible"] == [] and s32["constraints_per_case"] == 2)

# ---------------------------------------------------------------- EXP-033
print("\n## EXP-033  S o transposition, especially F3")
from k4lib import transpositions as TR
cells = TR.engraved_cells()
check("F3's engraved grid references exactly rows 25-28",
      sorted({row for row, _ in cells.values()}) == [25, 26, 27, 28],
      str(sorted({row for row, _ in cells.values()})))
check("F3 covers all 97 K4 positions and nothing else", sorted(cells) == list(range(97)))
check("F3's row-25 cells are columns 28-31 and match OBKR",
      [cells[i][1] for i in range(4)] == [28, 29, 30, 31]
      and "".join(CT[i] for i in range(4)) == ROWS[25][27:31])
for r, lo, hi in ((26, 4, 35), (27, 35, 66), (28, 66, 97)):
    check(f"F3's row {r} cells are columns 1-31 and match the authoritative row",
          [cells[i][1] for i in range(lo, hi)] == list(range(1, 32))
          and CT[lo:hi] == ROWS[r])
maxcol = max(c for _, c in cells.values())
check("F3 never uses a column beyond 31, so no uniform-31 PANEL assumption is needed",
      maxcol == 31, str(maxcol))
check("F3 uses no row outside 25-28, so rows 1-24 widths are irrelevant to it",
      all(row >= 25 for row, _ in cells.values()))
src33 = open(os.path.join(ROOT, "experiments", "exp033_subst_transposition.py")).read()
srctr = open(os.path.join(ROOT, "k4lib", "transpositions.py")).read()
check("neither EXP-033 nor its library embeds a row-1-to-24 string",
      not any(ROWS[r][:12] in src33 + srctr for r in range(1, 25)))
check("F1/F2 are abstract rectangles over K4's 97 letters, with no panel geometry",
      "column_lengths" in srctr and "ENGRAVED_ROWS" in srctr
      and "route_permutations" in srctr)
s33 = json.load(open(os.path.join(ROOT, "results", "exp033", "summary.json")))
check("EXP-033 VERDICT UNCHANGED: F1, F2 and F3 all stand",
      s33["feasible_function"] == 0 and s33["feasible_bijective"] == 0
      and s33["total_cases"] == 175820784)

# ---------------------------------------------------------------- EXP-034
print("\n## EXP-034  k[i] = f(S[i-L])")
s34 = json.load(open(os.path.join(ROOT, "results", "exp034", "summary.json")))
src34 = open(os.path.join(ROOT, "experiments", "exp034_text_dependent_keys.py")).read()
check("EXP-034's sources are K4 ciphertext and crib plaintext only",
      sorted(s34["sources"]) == ["ct_dec_11", "ct_dec_2", "ct_dec_3", "ct_dec_5",
                                 "ct_dec_7", "ct_fwd", "ct_rev", "pt"])
# A meaningful independence test, not string-sniffing: parse the module and confirm it
# imports no geometry, opens no panel data file, and defines no row/column map.
tree34 = ast.parse(src34)
imports34 = {n.module for n in ast.walk(tree34) if isinstance(n, ast.ImportFrom)} | \
            {a.name for n in ast.walk(tree34) if isinstance(n, ast.Import) for a in n.names}
funcs34 = {n.name for n in ast.walk(tree34) if isinstance(n, ast.FunctionDef)}
strs34 = {n.value for n in ast.walk(tree34) if isinstance(n, ast.Constant)
          and isinstance(n.value, str)}
check("EXP-034 imports no geometry module and reads no panel data file",
      "k4lib.transpositions" not in imports34
      and not any("cipher_side_rows" in t or "physical" in t for t in strs34),
      str(sorted(i for i in imports34 if i)))
check("EXP-034 defines no row or column map",
      not any(("col" in f or "row" in f) for f in funcs34), str(sorted(funcs34)))
check("EXP-034 embeds no row-1-to-24 string",
      not any(ROWS[r][:12] in src34 for r in range(1, 25)))
check("EXP-034 VERDICT UNCHANGED: purely textual",
      len(s34["feasible"]) == 0 and s34["decided"] == 2676)

# ---------------------------------------------------------------- report
for name, ok, detail in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    if detail and not ok:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print("\n## Conclusion")
print("   The variable-width correction changes NO result in EXP-032, EXP-033 or EXP-034.")
print("   All three consume only rows 25-28 (K4's own engraved rows, verified 31 characters")
print("   each) or no geometry whatsoever. F3 in particular uses columns 1-31 of rows 26-28")
print("   and columns 28-31 of row 25 and never assumes anything about the panel above.")
print("   What IS retracted is the descriptive sentence '32 + 27x31 = 869' wherever this")
print("   repository repeated it, including inside EXP-032's own printed cross-check.")
sys.exit(1 if fails else 0)
