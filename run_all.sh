#!/usr/bin/env sh
# Regenerate every experiment log. Deterministic: no RNG, no network, no corpus.
set -e
cd "$(dirname "$0")"
mkdir -p results/logs
for f in experiments/exp*.py; do
  name=$(basename "$f" .py)
  echo "running $name"
  python3 "$f" > "results/logs/$name.txt"
done
echo "done; logs in results/logs/"
