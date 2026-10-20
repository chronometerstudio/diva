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

## Reproduce a single-core run
    python3 mkcnf.py graphs/t_600_0.txt fix > c600s_0.cnf
    ./bin/diva-linux-x86_64 600 gvwuGB < c600s_0.cnf
    # output: "N <seconds> конфликтов <conflicts> ..."   (N = not 3-colourable, Y = colourable, T = time limit)

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
