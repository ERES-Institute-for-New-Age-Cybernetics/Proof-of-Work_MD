# PSCI-hat: Formal Spectral Bridge Hypothesis (Working Draft v0.1)
**Status tier: HYPOTHESIZED throughout. Closes E1 ("bridge asserted not argued"). Not yet sent to Pellis.**

---

## 1. Scope — which operator, explicitly

Two distinct operators appear in the Pellis framework, with **opposite stability sign conventions**. This document is scoped to exactly one of them, stated up front to avoid the conflation flagged in stress-testing:

| Operator | Source | Flow equation | Stability criterion | Adjoint type |
|---|---|---|---|---|
| `Ĥ_P` | Theorem 10, second variation at equilibrium `U*` | `∂_t δP = −Ĥ_P δP` | stable ⟺ `λₙ > 0 ∀n` | self-adjoint |
| `L̂_P` | Theorem 37, linearization along a trajectory | `∂_t δΦ = L̂_P δΦ` | stable ⟺ `Re(λₙ) < 0 ∀n` | **not** self-adjoint in general |

**This document is scoped to `L̂_P`.** Disease emergence (Theorem 37, eq. 2187) is defined on this operator, and it is the one any physiological/PSCI bridge needs to track.

This matters because the corpus's existing binding term **`V(ψ) = inf Re(λ)`** ("stability functional," retired alias "spectral floor") was calibrated to `Ĥ_P`'s sign convention, where a *positive* infimum is the stable regime. Porting that definition directly onto `L̂_P` would invert the result. For `L̂_P`, the correct stability-margin quantity is the **spectral abscissa**:

```
α(t) := sup_n Re(λₙ(L̂_P(t)))
```

stable ⟺ `α(t) < 0`; criticality ⟺ `α(t) = 0`; disease onset (eq. 2187) ⟺ `α(t) > 0`.

`α(t)` is a standard object in linear stability/control theory (it is the rightmost point of the spectrum) and is the direct, sign-correct analog of `V(ψ)` for this operator.

**This is distinct from Pellis's own `Δ(t)`** (eq. 2188, `min_{i≠j}|Re(λᵢ)−Re(λⱼ)|`, mode-spacing). `α(t)` answers "how close to the instability threshold." `Δ(t)` answers "how close two modes are to each other." Conflating these was the error flagged in stress-testing; they are kept separate here.

---

## 2. Definition: PSCI-hat

`PSCI-hat` occupies the existing, named-but-unfilled slot in the controlled vocabulary ("spectral collapse index, surrogate"). It is **not** a redefinition of `D(t)`; `D(t)` remains purely coherence-defined (`D(t) = [C0−C(t)]/C0`), per the binding spec.

```
PSCI-hat(t) := σ( α(t) / α_ref )
```

where:
- `σ` is any bounded, strictly monotonic function with `σ(0) = 0.5` (e.g. logistic or `(1+tanh(x))/2`) — the specific shape is a **disclosed modeling choice**, not a derived necessity.
- `α_ref` is a reference rate (same units as `α`, i.e. inverse time), required for dimensional consistency and pending reconciliation with the Prong 2 (REAL) reference-scale work.
- `PSCI-hat(t) = 0.5` exactly at `α(t) = 0` — i.e., at Pellis's own disease-onset threshold (eq. 2187), by construction, for any valid `σ` and `α_ref`.

**Assumption stated explicitly:** this requires `L̂_P(t)` to have discrete spectrum (so `sup_n Re(λₙ)` is attained, not merely an unattained supremum). This is not automatic on a non-compact, time-evolving manifold and has not been verified against Pellis's §2 manifold definition. Flagged as an open item, not assumed away.

---

## 3. The bridge hypothesis (closes E1)

```
H_bridge:  D(t) and PSCI-hat(t) share the same critical functional form
           as their respective systems approach threshold, within
           equivalence margin ε_eq.
```

This is the explicit, falsifiable statement that E1 found missing. It is tested by the gates that already exist in the corpus:

- **Q1 (decay-form gate):** does `D(t)`'s approach to breakdown match `PSCI-hat(t)`'s approach to `α(t)=0` in functional shape (not just qualitatively, but in decay/rise form)?
- **Q2 (exponent correspondence gate):** do the two critical exponents match within `ε_eq`?

Q2 is where the exceptional-point finding sharpens the prediction rather than just renaming it.

---

## 4. The exponent prediction (the actual contribution to Pellis's math)

`L̂_P` is non-self-adjoint. Degeneracies of non-self-adjoint operators are **exceptional points**, not the diabolical points / avoided crossings that govern self-adjoint degeneracies — a distinction the paper does not currently draw between Theorem 10 and Theorem 37.

At an exceptional point, eigenvalues *and* eigenvectors coalesce, and the local behavior of the eigenvalue near the degeneracy is a **square-root branch point**: as a control parameter `ε` is swept through its critical value `ε_c`,

```
α(ε) ≈ α_c ± k·√(ε − ε_c)
```

i.e. a critical exponent of **1/2** — sharper than a generic (linear, exponent-1) crossing.

**Falsifiable prediction for his own simulation:** if the degeneracy underlying Theorem 37's bifurcation is genuinely an exceptional point of `L̂_P`, his own **S2 criterion ("exponent recovery within tolerance")** should recover an exponent of `1/2`. If the simulated data instead recovers exponent `1`, the degeneracy is a regular (non-exceptional) crossing, and the EP hypothesis is falsified — which is itself a useful result, not a failure of this document.

This also gives a precise, non-hand-wavy account of why eq. 2186's modal expansion (`δρ = Σ aₖ(t)Ψₖ(x)`) breaks down near `Δ(t)→0`: at an exceptional point, `{Ψₖ}` is not merely closely spaced, it is **defective** — geometric multiplicity falls below algebraic multiplicity, and the basis genuinely fails to span the space. This replaces the earlier, vaguer "degenerate eigenvalues are noisy" framing with a specific, checkable mechanism.

---

## 5. What this resolves vs. what remains open

**Resolved by this document (no dependency on Pellis):**
- E1 — bridge is now a stated hypothesis with a testable functional form, not an assertion
- Operator ambiguity — `L̂_P` named explicitly, sign convention corrected, distinguished from `Ĥ_P`
- `Δ(t)` vs. `α(t)` conflation — separated into two named, non-overlapping quantities
- Vague degeneracy language — replaced with the specific EP mechanism and a numbered exponent prediction

**Still open, dependent on Pellis's simulation (Prong 3 territory):**
- Whether `L̂_P` actually has discrete spectrum on the biological manifold (§2 assumption, unverified)
- The actual numerical value of the recovered exponent (Q2) — this is the test, not something to assume in advance
- Type I/II calibration of any PoR/RCR gate built downstream of `PSCI-hat` — still requires real eigenvalue data to compute

---

## 6. Disclosure note for any external version

If/when this is shared outside this working draft: the `σ` function and `α_ref` choice in §2 must be labeled as a modeling convention, not a derived result, exactly as flagged in §2. The exponent prediction in §4 must be labeled as a hypothesis his own S2 test can confirm or falsify — not as an established correspondence.
