# Diva — 3-colouring / SAT solver (research prototype): public benchmark record

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23499372.svg)](https://doi.org/10.5281/zenodo.23499372)

Archived on Zenodo: https://doi.org/10.5281/zenodo.23499372 (release v2026-10-20.1, 20 Oct 2026).

**Source code is not published.** This repository fixes the date and content of the solver by a hash commitment:
`SOURCE_SHA256.txt` holds the SHA-256 of the complete source archive (`diva_2026-10-20.tgz`, kept privately).
Anyone can later verify that a released archive matches this commitment.

What is public here:
- `bin/diva-linux-x86_64`, `bin/tabu-linux-x86_64` — statically linked Linux builds (single-core engine; the 2-core dispatcher is withheld);
- `graphs/` — the exact random graphs used (G(n, m = 2.35 n), n = 500, 600, 700), format: `n m` then one edge per line;
- `mkcnf.py` — graph → DIMACS CNF (3 colours), optional greedy-clique fixing (`fix`);
- `prereg_2026-10-19.json` / `prereg_2026-10-19_result.txt` — pre-registered predictions of the refutation-cost law on fresh graphs, and the outcomes.

See also [HYPOTHESIS.md](HYPOTHESIS.md) — the brittleness hypothesis as a research programme (in Russian): three testable claims and the verification plan.

## What Diva is (and is not)
Diva is a **CDCL SAT solver** (conflict-driven clause learning with restarts, lemma-database management and bounded variable elimination), the same family as Kissat and CaDiCaL — not a local-search or tabu solver.
Every **N** answer is a complete refutation produced by clause learning: the run ends only when the empty clause is derived (in the 2-core mode, when every cube is refuted). No answer is ever decided by a timeout or a probabilistic criterion; a timeout prints **T**.
Every **Y** answer is verified against the original formula before it is printed.
`tabu` is an auxiliary local-search probe used by the (withheld) 2-core dispatcher to order the cubes; it never decides an answer. The engine's own walker (`w` option) only seeds variable phases.
What is specialised: Diva detects "exactly one" groups and the "different" relation in the CNF and fixes colours on a greedy clique (symmetry breaking). In the comparison table below Kissat is given the same clique fixing in the CNF; without it Kissat is 4–6× slower on the same graphs. Conflict counts are reported alongside times because both solvers are CDCL and the counts are comparable.

## Verify on fresh graphs (no possibility of tuning to the published instances)
    python3 gengraph.py 600 2.35 <any seed> > fresh.txt
    python3 mkcnf.py fresh.txt fix > fresh.cnf
    ./bin/diva-linux-x86_64 1800 gvwuGB < fresh.cnf
The binary takes an arbitrary DIMACS CNF; nothing in it refers to the files in `graphs/`.

## Scope
Exact decision of 3-colourability for random graphs at the colourability threshold (c = m/n ≈ 2.35), n = 500–700 — instances on which proof size grows exponentially and general CDCL solvers need minutes to hours. This is not a tool for colouring large industrial graphs far from the threshold (those are easy for greedy heuristics and are not the subject here). Pre-registered laws and timings here are claims about this regime only.

## Reproduce a single-core run
    python3 mkcnf.py graphs/t_600_0.txt fix > c600s_0.cnf
    ./bin/diva-linux-x86_64 600 gvwuGB < c600s_0.cnf
    # output: "N <seconds> конфликтов <conflicts> ..."   (N = not 3-colourable, Y = colourable, T = time limit; "конфликтов" is the Russian word for "conflicts" printed by the binary)

## Comparison with Kissat 4.0.4 (built from https://github.com/arminbiere/kissat), same CNF with the clique fixed, single core, CPU seconds, 19–20 Oct 2026
| graph | Diva | Kissat |
|---|---|---|
| 500 #0 | 4.5 | 5.9 |
| 500 #1 | 0.41 | 0.57 |
| 500 #3 | 1.43 | 1.79 |
| 600 #0 | 3.9 | 4.4 |
| 600 #1 | 5.2 | 7.2 |
| 600 #2 | 28.5 | 34.8 |

700-vertex series, 2 cores (dispatcher, withheld), wall seconds, 20 Oct 2026: #0 Y 34, #1 Y 22, #2 Y 105, #3 N 157, #4 N 14, #5 Y 501, #6 N 519, #7 N 243.
Kissat on the same 700 graphs with the same clique fixing, 1 h limit: #6 N 987 s, #7 N 861 s.

Hardware: 2-core cloud VM (x86-64). Timings vary by machine; conflict counts for N answers are deterministic for fixed options.

## Empirical laws (3-colouring at the threshold, NO instances)
Refutation cost in conflicts, fitted on 162 random graphs n = 150…500 (c = 2.30), R² = 0.92:
    log2 C = 1.16 + n · (0.120 − 0.0204·ρ − 0.0527·t)
ρ = density (2m/|S|) of the densest subgraph S on 12–32 % of the vertices ("nucleus"), t = triangles inside S per nucleus vertex.
Pre-registered check on 9 fresh NO graphs (n = 600, 700): mean error −0.3 bits, σ ≈ 1.2.

## Sealed files

`SOURCE_SHA256.txt`, `PREREG_SHA256.txt` and `PRIORITY_SHA256.txt` hold SHA-256 hashes of files kept by the author: the solver source, the pre-registered predictions of ongoing experiment series, and the research note on the witness-edge law (v0.1 sealed and embargoed on 2026-10-21; v0.2 published 2026-10-22: https://doi.org/10.5281/zenodo.23550288; the concept DOI https://doi.org/10.5281/zenodo.23539230 resolves to the latest version). The hashes let any later release of those files be checked against the dates of the commits here.
