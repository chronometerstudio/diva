# The Key-Spectrum Hypothesis: a research programme

Idea: Y. Deev (Chronometer Studio). Revision 2, 21 October 2026 (revision 1 was called "the brittleness hypothesis"; brittleness is treated here as a consequence, not a foundation).
Status: a working hypothesis with a verification plan and first measurements. It is not a proof of P ≠ NP and makes no claim to be one (see §5).

## 1. The original intuition (in the author's formulation)

1. There are infinitely many NP-complete problems; Karp's list (1972) is the beginning of an enumeration. Changing a problem's parameter (number of colours, clause width, density of numbers) yields a new problem, sometimes on the other side of the P/NP boundary.
2. **Keys.** Every problem has a series of accelerators — "keys" — with decreasing contributions: roughly 50 %, 30 %, 10 %, 5 %, 2.5 %… Keys apply to every problem, but on a foreign problem their weight is vanishingly small; only the strongest are measurable.
3. The series converges: no finite set of keys gives 100 %. A polynomial algorithm is a finite set of keys.
4. **The razor's edge.** A key has a cost. A key whose weight is below a threshold is a net loss of time: "on small instances 50 % saves time, 40 % already costs it". Tuning a method for a "sister" problem makes it worse on the parent.
5. **Sisters.** Mutate a problem minimally (a sister) and measure the weight of the same method. Numeric problems (Subset Sum, Partition) give a continuous chain of sisters: the density of the numbers changes by one bit.

## 2. Quantitative form

For a family of inputs F with size n and a fixed method M: log₂ C(n) = a + s·n, where C is the cost (conflicts or time), s is the **exponent** (bits per vertex/variable) and a is the **multiplier**.
The weight of a key k at fixed n is w_k = log₂(C without k / C with k) bits. The cost of a key, c_k, is its overhead in the same units; the net weight is w_k − c_k.

**Key-spectrum hypothesis.** For an NP-complete family at its threshold, the sum of the weights of all keys Σ_k w_k = O(1) bits (bounded by a constant independent of n), whereas s·n = Θ(n). In other words, keys change the multiplier a and leave the exponent s untouched. For a family in P, a single key has weight s·n (the exponent becomes zero) — and this is known by theorem, not by measurement.

Brittleness is a consequence: w_k depends on the family and falls under mutation of the input; Σ w_k stays O(1). The razor's edge is the second part: when w_k falls below c_k, the key changes sign.

## 3. What has been established (Diva, 19–21 October 2026)

- **Refutation-cost law** for random 3-colouring at the threshold (162 graphs, n = 150…500; pre-registered at 600–700): log₂ C = 1.16 + n·(0.120 − 0.0204·ρ − 0.0527·t), where ρ is the nucleus density and t the triangle count inside the nucleus. Residual σ ≈ 1.2 bits. Generalises to 4-colouring.
- **The sum of keys is a constant.** All engine keys together (lemma memory, restarts, BVE, inheritance, priors) ≤ ×1.6, i.e. ≤ 0.7 bits; the clique key (fixing the colours of a clique) ×4.7 ≈ 2.2 bits; Kissat without this key is 4–6 times slower. Against an exponent of 0.031·n ≈ 15 bits at n = 500. The series "50 + 30 + 10 + …" in bits is ≈ 1 + 0.5 + 0.15 + … ≈ 2 bits — it matches the measured multiplier.
- **The exponent is set by the family, not the solver.** Sister series 1 (bits/vertex): random graph c = 2.35 — 0.031; c = 3.0 — 0.009; triangular lattice with 60 % / 100 % of edges rewired — 0.013 / 0.012; 6-regular — 0.045 for Diva and 0.047 for Kissat. Different solvers, one exponent.
- **A key's weight falls under mutation.** Clique key: ×4.7–5, constant on random graphs; on regular graphs ×6.0 → 4.2 → 3.6 as n grows. The nucleus law does not work on regular graphs (there is no nucleus).
- **The razor's edge is observed.** BVE: ×1.3–1.6 on all NO graphs at n = 500–700; on YES graphs it changes sign between neighbouring seeds (c500_2: seed 0 — 0.81 s without / 12.31 s with BVE; seed 4 — 16.88 / 4.02). Inheritance of warm-up lemmas: −15 % on one graph, +5 % on another.
- **Sensitivity threshold.** With σ ≈ 1.2 bits and n_max = 700, an exponent is detectable at the 2σ level only if s > 2σ/n_max ≈ 0.0035 bits/vertex. Below that, "100 %" and "99.x %" are indistinguishable by measurement. All exponents measured so far lie 3–10 times above the threshold; statements of the form "a key changes only the multiplier" hold with this caveat.

## 4. Four testable claims

**H-A. Decay invariant.** The relative loss of weight of a fixed key along a chain of sisters is described by one curve across domains (graphs, formulas, numbers). The strong form (identical constants) is most likely false: the critical exponents of the transition window differ between 2-SAT (ν = 3, Bollobás et al. 2001) and 3-SAT (≈ 1.5, Kirkpatrick, Selman 1994). The testable weak form: one functional form with family-dependent constants. Falsified if the forms differ.

**H-B. Separation of scales.** Mutations of the input split into two types: those that change the exponent s (change of class: density, regularity, threshold) and those that change the multiplier a (everything the keys live on). Falsified if a key is found that changes the exponent on a fixed family above the sensitivity threshold of §3.

**H-C. A theorem for a fixed proof system.** For resolution (and CDCL as a fragment of it), on a family of sisters no addition of polynomially many "key lemmas" changes the exponent. The technique is known: resolution width (Ben-Sasson, Wigderson 2001); lower bounds for random colouring — Beame, Culberson, Mitchell, Moore (2005). Formulas with global parity (Tseitin) are an already proven case: Urquhart (1987). Our measured exponents say which constant to prove.

**H-D. The razor's edge (cost of a key).** For every key there is a sister on which its net weight w_k − c_k is negative; at the transition parent → sister the sign flips rather than decaying smoothly. Falsified by a key whose net weight is positive on the whole chain of sisters at all n. Closest predecessor: no free lunch (Wolpert, Macready 1997) — averaged over all problems all methods are equal; H-D is its version inside one family with a measurable threshold.

## 5. Why this is not a proof of P ≠ NP — and the limits of the programme

- **Circularity.** The model says "never 100 %". But inside P a 100 % key exists by theorem: 2-SAT (Aspvall, Plass, Tarjan 1979), Horn-SAT (Dowling, Gallier 1984), XOR-SAT (Gaussian elimination). What distinguishes a 100 % key from a 50 % key is the P vs NP question itself; the model does not resolve it, it restates it.
- **Measurement.** Experiment cannot distinguish 100 % from 99.x % (threshold of §3), nor "no key exists" from "no key found". P-keys are known by theorem; for NP-complete problems only an impossibility theorem can answer — H-C, not H-A/H-B.
- **Scale.** Brittleness is a loss in the multiplier; P ≠ NP is a statement about the exponent.
- **Quantifier.** "All known keys are O(1) bits" does not transfer to all polynomial algorithms.
- **Barrier.** An argument only about inputs, without the structure of the computing device, relativises (Baker, Gill, Solovay 1975).

The aim of the programme is the empirical laws H-A, H-B, H-D and the theorem H-C.

## 6. Verification plan

1. ✔ Sister series 1 for 3-colouring (random → regular → lattice with noise → planted): exponent per family, weight of the clique key by n. Done 21 October 2026; results in §3.
2. **2+p-SAT as calibration** (Monasson et al. 1999): a continuous chain of sisters between 2-SAT and 3-SAT with a known answer — the transition from polynomial to exponential at p ≈ 0.41. If our protocol does not reproduce the known kink, the protocol is unfit.
3. **Subset Sum by density** (LLL, dynamic programming, branching): density 0.5…1.2; known transition near 0.94 (Lagarias, Odlyzko 1985; Coster et al. 1992).
4. **Random 3-SAT by density** (threshold 4.27): same protocol; known DPLL kink at density ≈ 3.9 (Cocco, Monasson 2001).
5. **H-D directly:** BVE and lemma inheritance on YES/NO by n — find the n and the sister at which the sign changes.
6. For every family: pre-registration before the runs; every report states the sensitivity threshold 2σ/n_max; key weights on lattices measured in time, not conflicts.

## 7. Predecessors (a mandatory part of every claim)

Reductions and problem lists: Cook (1971), Karp (1972), Garey, Johnson (1979). Phase transitions and hardness: Cheeseman, Kanefsky, Taylor (1991); Mitchell, Selman, Levesque (1992); Kirkpatrick, Selman (1994); Bollobás, Borgs, Chayes, Kim, Wilson (2001). Continuous families of sisters: Monasson, Zecchina, Kirkpatrick, Selman, Troyansky (1999); Achlioptas, Kirousis, Kranakis, Krizanc (2001); Cocco, Monasson (2001). Problem-specificity of keys: Rice (1976); Wolpert, Macready (1997); Xu, Hutter, Hoos, Leyton-Brown (2008); Leyton-Brown, Nudelman, Shoham (2009). Subset Sum density: Lagarias, Odlyzko (1985); Coster et al. (1992). Resolution lower bounds: Haken (1985); Urquhart (1987); Chvátal, Szemerédi (1988); Ben-Sasson, Wigderson (2001); Beame, Culberson, Mitchell, Moore (2005). 100 % keys inside P: Aspvall, Plass, Tarjan (1979); Dowling, Gallier (1984). Barriers: Baker, Gill, Solovay (1975); Razborov, Rudich (1997); Aaronson, Wigderson (2008). Exponential time hypothesis: Impagliazzo, Paturi (2001).

What here does not reduce to predecessors and predicts a number: (a) the sum of the weights of all keys of a fixed CDCL engine on random 3-colouring at the threshold is a constant ≈ 2–3 bits against an exponent of 0.031·n; (b) the exponent is the same for different solvers on one family (0.045 vs 0.047); (c) the sensitivity threshold as a mandatory part of any claim of the form "changes only the multiplier".
