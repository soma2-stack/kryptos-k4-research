#!/usr/bin/env sh
# FULL historical regeneration. This can be expensive and overwrites results/logs/*.txt.
# For onboarding/CI use: python smoke.py  (or ./run_smoke.sh)
set -e
cd "$(dirname "$0")"

if [ "${K4_FULL_REGEN:-0}" != "1" ]; then
  echo "Refusing full EXP-001..EXP-043 regeneration by default."
  echo "Run 'python smoke.py' for the safe integrity suite."
  echo "If you intentionally want every experiment, run: K4_FULL_REGEN=1 ./run_all.sh"
  exit 2
fi

mkdir -p results/logs
for f in experiments/exp*.py; do
  name=$(basename "$f" .py)
  echo "running $name"
  python3 "$f" > "results/logs/$name.txt"
done
echo "done; logs in results/logs/"
