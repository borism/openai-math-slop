# Lean checks (added after the subagent reviews)

Run on Lean 4.34.1 with Mathlib `d13f23b` (the revision upstream pins), against openai/math `4eaee8754`.
The lean/OAI and lean/ComparatorChallenges trees were symlinked into a scratch Lake project; only the
import closures of the targets below were built.

- `fingerprint-dump.lean` / `fingerprint-dump-local.lean`: Lean commands that write, for every constant
  in a module (or in the current file), its kind, universe parameters, the hash of its type, and for
  definitions the hash of its value.
- `compare_fingerprints.py`: compares a challenge dump with a solution dump. Definitions, inductives,
  constructors and recursors must agree on type and value; theorems on type only.

This is an independent approximation of Comparator's core check (the statement and every definition
it uses are the same in the challenge and the solution), not a replacement: it compares 32-bit
structural hashes rather than terms, and it is not Comparator or nanoda. The proofs themselves were
checked by the Lean kernel when the solution modules were compiled.
