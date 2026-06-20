# VEILED-Z Gate — Conditioned-Response Suspension Near Spectral Threshold
**Status: HYPOTHESIZED structure, built from standard non-Hermitian physics results, not freshly derived in full here. Flagged where calibration is still open.**

---

## 1. Why this gate exists (the derivation, not just the caution)

The Petermann factor `K = ⟨ψ_L|ψ_L⟩⟨ψ_R|ψ_R⟩ / |⟨ψ_L|ψ_R⟩|²` diverges at an exceptional point (Quantum Criticality paper, eq. 460–461). In non-Hermitian/laser physics this divergence has a known scaling: for a second-order EP, as the system sits a distance `ε` away from criticality,

```
Δλ ~ √ε         (eq. 458, his own result)
K ~ ε^(-1/2)     (standard result for second-order EPs in non-Hermitian systems —
                  not derived fresh here, cited from the established physics, not asserted)
```

So `K` and the eigenvalue splitting share the same `√ε` family, just inverted. Practically: **the same proximity to threshold that makes a spectral reading most diagnostic also makes it least reliable**, by a known, non-arbitrary rate — not a vague "be careful near the edge."

## 2. The trigger — VEILED-Z(t)

Using `Z(t) := α(t)` (the corrected stability functional) as the proxy for distance-to-criticality:

```
VEILED-Z(t) := TRUE  when  |Z(t)| < Z_threshold
```

`Z_threshold` should be set by choosing an acceptable amplification ceiling `K_crit` (e.g., "don't trust a reading once amplification exceeds 10×") and solving for the corresponding `Z`. **This calibration step is not done here** — it needs either simulation data (the same data Prong 3 is already waiting on) or a tighter derivation linking `Z(t)` directly to `K(t)` for the specific operator in use. Until then, treat `Z_threshold` as a placeholder to be set, not a number this document supplies.

## 3. The gate behavior

```
IF VEILED-Z(t) = TRUE:
    SUSPEND any conditioned-response rule that would fire directly off Z(t)
    HOLD execution open, pending one of:
        (a) an independent confirmation signal not subject to the same
            EP-driven amplification, or
        (b) time-averaging sufficient to reduce the amplified noise, or
        (c) explicit deliberate review rather than automatic firing
    DEFAULT (while held): the One-Good baseline action — the option that
        does the least harm if the suspended reading turns out to be wrong
        in either direction
ELSE:
    Normal conditioned-response behavior applies
```

"Held open" means specifically: the system does not act on `Z(t)` as if it were trustworthy, and does not act as if it had no information either — it falls back to a pre-agreed safe default until the zone clears or independent confirmation arrives.

## 4. Where this sits in the existing architecture

This isn't a new category — it's a specific, derivable instance of the **Runtime Containment Requirement (RCR)** already in EAAP: a containment trigger whose firing condition is now tied to a real, named physical mechanism (EP-driven eigenvector non-orthogonality) rather than a general caution principle. Framing it that way keeps it inside the existing gate architecture rather than adding a parallel one.

## 5. Status

**Sound, derivation-backed:**
- The reason the gate is needed (Petermann divergence) is real and correctly attributed
- The qualitative behavior (suspend, hold, default to least-harm) is a standard, well-justified circuit-breaker pattern

**Open:**
- `Z_threshold` is uncalibrated — needs either data or a tighter derivation
- The exact `K(ε)` scaling exponent for *this* operator (cardiac `L̂(t)`, not a generic 2-level laser model) hasn't been independently confirmed — borrowed from the general non-Hermitian-physics result, not re-derived for this specific case
