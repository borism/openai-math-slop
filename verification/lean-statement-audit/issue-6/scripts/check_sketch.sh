#!/usr/bin/env bash
# Elaborate ReducedPolynomialSketch.lean against the real challenge definitions
# without building the OAI tree: inline lines 1-75 of the upstream challenge
# (everything through `main_result ... sorry`) and append the sketch body.
# Usage: check_sketch.sh <upstream-lean-dir> <lean-project-with-Mathlib> <scratch-dir>
set -euo pipefail
UP=$1; PROJ=$2; OUT=$3; HERE=$(cd "$(dirname "$0")/.." && pwd)
F=$OUT/ReducedInlined.lean
{ head -n 75 "$UP/ComparatorChallenges/HyperbolicCones.lean"; echo
  sed -n '/^-- BEGIN BODY$/,/^-- END BODY$/p' "$HERE/ReducedPolynomialSketch.lean"
  printf '\nend Paper256\n\nend\n\nend OAI\n'; } > "$F"
cd "$PROJ" && timeout 900 lake env lean "$F"
