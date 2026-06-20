# PSCI-hat: Formal Spectral Bridge Hypothesis (v0.2 — rebuilt on source material)
**Supersedes v0.1, which was built against a generic stand-in operator. This version uses the actual operator from the paper already cited in the BERA spec, and Pellis's own exceptional-point theorem rather than an independently-derived one.**
**Status tier: HYPOTHESIZED where noted. Closes E1. No dependency on Pellis's simulation for the structural parts — the falsifiable test still needs his data.**

---

## 1. The correct source, and what changes

v0.1 was scoped to `L̂_P`, a linearized operator from the *morphogenesis* paper (Theorem 37). That was the wrong anchor. The BERA spec's own citation already names the actual source: **"Spectral–Fractal Phase Transitions in Cardiac Dynamics from ECG Operator Flows," §2.7.** That paper defines its own operator directly:

```
d/dt ψ(t) = L̂(t)ψ(t)        (eq. 66)
```

`L̂(t)` is stated explicitly as **non-self-adjoint** by construction (not inferred — Pellis says so directly, multiple times, in this paper). The stability criterion is given as:

```
stable:        sup_{λ∈σ(L̂(t))} Re(λ) < 0     (eq. 69)
onset:         sup_{λ∈σ(L̂(t))} Re(λ) → 0⁺    (eq. 70)
```

This is exactly the spectral-abscissa quantity v0.1 constructed independently (`α(t) = sup Re(λ)`) — it isn't a guess anymore, it's Pellis's own stated criterion in the paper this bridge is supposed to connect to.

---

## 2. A real inconsistency found in the source paper, worth naming precisely

Section 2.7 of the same paper defines the critical manifold differently:

```
M_c = { ψ ∈ H | min_i Re(λ_i(L̂(ψ))) → 0 }     (eq. 99)
V(ψ) = inf_{λ∈σ(L̂(ψ))} Re(λ)                   (eq. 100)
M_c = { ψ | V(ψ) = 0 }                          (eq. 101)
```

`min`/`inf` is the **opposite** aggregation from §2.5's `sup`. The infimum of `Re(λ)` is the *most stable* mode, not the one closest to crossing zero — using it to define the critical manifold doesn't match the stability criterion four pages earlier in the same paper. Either eq. 99 has a sign/aggregation typo (likely `max` was intended), or there's a convention shift between sections that isn't stated. I can't resolve which from the text alone — it's worth being precise that this is a finding, not a correction I'm asserting confidently.

**This matters beyond the source paper.** The ERES BERA spec's own controlled vocabulary already adopted `V(ψ) = inf Re(λ)` as the canonical "stability functional" — taken, apparently, directly from this paper's eq. 100. That term is also what Prong 2 used to anchor `E_ref` to `C0`. If eq. 100 is the erroneous half of an internal inconsistency, the corpus inherited the error, not just the term. **This needs a decision before Prong 2's anchoring is treated as final**, separate from anything involving Pellis. Recommend using `sup Re(λ)` (consistent with eq. 69–70, and with how the math actually behaves) and either correcting the BERA spec's vocabulary table or explicitly noting the deviation from it.

---

## 3. PSCI-hat, rebuilt on the actual operator

```
α(t) := sup_{λ∈σ(L̂(t))} Re(λ)        — Pellis's own stability margin, eq. 69–70
PSCI-hat(t) := σ(α(t)/α_ref)          — same construction as v0.1, now correctly grounded
```

`σ` and `α_ref` remain disclosed modeling choices (per v0.1 §2's honesty requirement) — that part doesn't change. What changes is that `α(t)` is no longer a stand-in; it's the literal quantity the cited paper already uses to define cardiac instability onset.

The bridge hypothesis (`H_bridge`, closing E1) is unchanged in form but now anchored to a real paper:

```
H_bridge: D(t) (coherence-based, measured) and PSCI-hat(t) (built on α(t) from
          L̂(t)) share the same critical functional form near threshold.
```

One honest gap: the ECG paper's own treatment of "coherence breakdown" is wavelet-energy-based (scalogram divergence, eq. 5.7), not the same cross-channel coherence `C(t)` the BERA spec's `D(t)` is built from. The bridge between *those two specific quantities* is still a hypothesis to test, not something the source paper hands us pre-connected. That's the part Q1/Q2 still need to check — this rebuild makes the spectral side rigorous, it doesn't manufacture the empirical link.

---

## 4. The exceptional-point claim — now Pellis's own derivation, not an independent one

This is the more significant correction. The EP note sent to Pellis derived the square-root exponent independently. He's already derived it, more completely, in *Spectral Collapse as a Universal Mechanism for Quantum Criticality* (§11.3–11.4):

```
ρ(λ) ~ |λ - λc|^(-ν),  0 < ν < 1        (eq. 456, general branch exponent)
ν = 1/2 for the canonical (second-order) exceptional point     (eq. 455)
Δλ ~ ε^(1/k)  →  Δλ ~ √ε  for k=2        (eq. 457-458)
```

He also defines the **Petermann factor**:
```
K = ⟨ψ_L|ψ_L⟩⟨ψ_R|ψ_R⟩ / |⟨ψ_L|ψ_R⟩|²       (eq. 460)
```
which diverges at the exceptional point (eq. 461) — a standard, measurable non-Hermitian sensitivity metric (used in real laser/sensing physics), and a sharper falsifiable target than "exponent ≈ 1/2 or 1." It gives a second, independent signature to check: not just the exponent, but whether `K` is growing as the system approaches `M_c`.

He also gives the precise mechanism for why a modal expansion breaks down near an EP — not "the basis becomes noisy," but a derived growth law:
```
‖ψ(t)‖² ~ e^(2 Re(λc) t) · t^(k-1)         (eq. 463)
```
the polynomial prefactor `t^(k-1)` is the actual signature of non-diagonalizability (a Jordan block), distinct from ordinary exponential growth.

**What this means for the falsifiable test:** rather than proposing a prediction Pellis hasn't checked, the honest framing is — *does the cardiac operator's approach to `M_c` (his own eq. 99–101) exhibit his own EP signature (eq. 455–463) from the other paper, or not?* That's a real, still-open question — he derived the general EP theory and the cardiac critical-manifold definition in two different papers and, as far as this review found, hasn't yet connected them. Confirming or ruling that out is exactly what his own simulation work (S2) could settle. The contribution is the cross-paper connection, not the math itself.

---

## 5. Status

**Resolved, no dependency on Pellis:**
- Operator corrected to the actual cited source (`L̂(t)` from the ECG paper), replacing the generic stand-in
- A real internal inconsistency in the source paper identified and stated precisely (§2.5 vs. §2.7 aggregation)
- Downstream effect on the BERA spec's own `V(ψ)` vocabulary entry and Prong 2's `E_ref` anchor flagged
- EP claim reattributed correctly to Pellis's own derivation (exponent, Petermann factor, Jordan growth law) rather than presented as independently discovered

**Open:**
- Whether the cardiac critical manifold (eq. 99–101) actually exhibits EP structure is unconfirmed — this is the real falsifiable question, and it needs his simulation data
- The §2.5/§2.7 aggregation inconsistency needs Pellis's own clarification, not an assumption on our side
- The `V(ψ)` correction in the BERA spec's controlled vocabulary needs a decision from you before it's treated as resolved
