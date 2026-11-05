#!/usr/bin/env python3
"""Build issue-3/formalization-yaml.patch.

Usage: python3 -I make_yaml_patch.py UPSTREAM_formalization.yaml OUT_patched.yaml

Annotates the `sources` entries whose Lean formalization covers only a supporting
or weaker result, using fields that the formalization.yaml v0.4 schema already
defines for sources (`relationship`, `location`, `note`; relationship enum:
formalizes | adapts | independently-proves | background | other). Also rewrites
the file-header comment and tags the corresponding `status.main_results` entries
with YAML comments (main_results items have no note field in the schema).
"""
import sys

src, out = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()

P = "../preprints/"
# (paper directory prefix in `id:`, relationship, location, note)
SOURCES = [
    ("Integral-points-on-character-varieties-of-curves-September-25-2026/", "other",
     "Supporting result: the produced marked values satisfy all seam equations (producedMarkedValues_allSeams)",
     "Supporting result only (CharacterVarietiesAllSeamsSupport). The main theorem, potential integral density for SL_r curve character varieties, is not formalized: existence of integral points and Zariski density are not established (docs/027.md)."),
    ("Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/", "other",
     "Supporting result: compactness of closed chart-field retractions (isCompact_closedChartFieldRetraction_cone)",
     "Supporting result only (CartierChartCompactnessSupport). The uniform Cartier-section theorem, bounded klt complements and the companion conclusions are not formalized (docs/066.md)."),
    ("A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/", "other",
     "Supporting result: existence of a 3-dimensional complete Noetherian normal local domain over C with residue field C (candidate_ring_properties)",
     "Supporting result only (SurfaceConeCandidateSupport). The main theorem, that the constructed ring has no nonzero finitely generated module of depth 3, is not formalized. The formalized existential statement is also witnessed by C[[x,y,z]], which is Cohen-Macaulay (docs/195.md)."),
    ("Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/", "other",
     "Imported input, Proposition c:finite(1), first clause: c(1+h)^(-1/4) <= B_h <= C(1+h)^(-1/4) for the strict-bridge mass (finiteBridgeMassEstimate)",
     "Supporting result only (HoneycombBridgeMassSupport). The formalized bound is an input the paper takes from its companion 'Uniform marked-polygon estimates and sharp finite bridge moments' (Theorem 1.1). The paper's main theorem c:main, the R^(4/3+o(1)) prescribed-endpoint chord-length law, and the remaining c:finite and c:renewal inputs are not formalized (docs/237.md)."),
    ("The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/", "other",
     "Supporting result: Section 2 ideal transport (idealOrderIso_finIdeal, idealOrderIso_zeroIdeal, closed_ideal_weight_exists)",
     "Supporting result only (TraceIdealTransportSupport). The classification isomorphism A (x) W (x) K = B (x) W (x) K, existence of the stabilization models, norm uniqueness and the final intertwining are not formalized (docs/301.md)."),
    ("Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/", "other",
     "thm:exponential-shape, differentiability part only, for rate 1: differentiability away from 0, unique supporting lines, C^1 boundary (manuscriptMain)",
     "Partial. Strict convexity of the unit ball, stated in the title and in thm:exponential-shape, is not formalized; neither is thm:gamma-differentiability (docs/212.md)."),
    ("Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/", "other",
     "thm:main with exponent delta^13 in place of the stated delta^5 (the weaker rate noted at the end of the introduction)",
     "Weaker than the headline. The paper's delta^5 rate rests on Song's external conditioning estimate (prop:song-conditioning, ECCC TR26-199), which the Lean neither states nor uses; the Lean proves delta^13 by its own conditioning argument. The distribution-dependent cubic bound (cor:support-threshold) is not formalized (docs/277.md)."),
    ("The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/", "formalizes",
     "thm:main (elementary expansion: attaching an (n+1)-disk along its source n-face is a weak equivalence)",
     "The homotopy hypothesis of the title (cor:homotopy-hypothesis) and the semi-model structure (cor:semimodel) are deduced from Henry 2016 and are not formalized (docs/312.md)."),
    ("Bounded-recovery-for-modular-spectral-averages-September-23-2026/", "other",
     "Section 4, bounded recovery theorem (bounded_recovery)",
     "Partial. The paper's thm:main (trivial bicentralizer for type III_1 factors with separable predual) and thm:rigidity are not formalized. thm:main is deduced from bounded recovery via Section 5 and external results (Houdayer-Isono 2017, AHHM 2020 Thm A, Marrakchi 2020 Thm D) (docs/290.md)."),
]

def once(hay, needle):
    n = hay.count(needle)
    assert n == 1, (needle, n)

for prefix, rel, loc, note in SOURCES:
    for s in (rel, loc, note):
        assert '"' not in s and "\\" not in s, s
    lines = text.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("    id: " + P + prefix)]
    assert len(idx) == 1, (prefix, idx)
    i = idx[0]
    assert lines[i + 1].startswith("    type: "), lines[i + 1]
    new = [f"    relationship: {rel}", f'    location: "{loc}"', f'    note: "{note}"']
    lines[i + 2:i + 2] = new
    text = "\n".join(lines)

# Header comment: the catalogue claim is no longer true for every entry.
old_hdr = "# Catalog of papers with a formalized main result. Paths are relative to lean/.\n"
once(text, old_hdr)
text = text.replace(old_hdr,
    "# Catalog of papers with Lean formalizations. Paths are relative to lean/.\n"
    "# A source without `relationship` has its main result formalized. `relationship: other`\n"
    "# marks a paper for which only a supporting or weaker result is formalized; `location`\n"
    "# says what is formalized and `note` what is not.\n")

# Tag main_results entries (YAML comments; the schema has no note field there).
TAGS = {
    "    - comparator_config: ComparatorChallenges/CharacterVarietiesAllSeamsSupport.json\n":
        "supporting result for 'Integral points on character varieties of curves'; main theorem not formalized",
    "    - comparator_config: ComparatorChallenges/CartierChartCompactnessSupport.json\n":
        "supporting result for 'Uniform Cartier sections for Fano type contractions'; main theorem not formalized",
    "    - comparator_config: ComparatorChallenges/SurfaceConeCandidateSupport.json\n":
        "supporting result for 'A Complete Local Domain without a Small Cohen-Macaulay Module'; main theorem not formalized",
    "    - comparator_config: ComparatorChallenges/HoneycombBridgeMassSupport.json\n":
        "supporting result for 'Critical honeycomb chords with prescribed boundary endpoints'; main theorem not formalized",
    "    - comparator_config: ComparatorChallenges/EntangledGames.json\n":
        "delta^13 rate; the paper's Theorem 1.1 states delta^5 (via Song's external estimate)",
    "    - comparator_config: ComparatorChallenges/PlanarFirstPassage.json\n":
        "differentiability only; strict convexity (paper title, thm:exponential-shape) not formalized",
    "    - comparator_config: ComparatorChallenges/BoundedRecovery.json\n":
        "bounded recovery only; the paper's thm:main (bicentralizer triviality) not formalized",
}
for k, v in TAGS.items():
    once(text, k)
    text = text.replace(k, f"    # {v}\n" + k)
# TraceIdealTransportSupport has three entries; tag only the first.
k = "    - comparator_config: ComparatorChallenges/TraceIdealTransportSupport.json\n"
assert text.count(k) == 3
text = text.replace(k, "    # supporting results (3 entries) for 'The trace cone classifies Razak-Jacelon stabilizations'; main theorem not formalized\n" + k, 1)

open(out, "w", encoding="utf-8").write(text)
print("ok")
