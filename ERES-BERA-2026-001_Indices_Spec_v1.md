# BERA — Bio-Ecologic Resonance Architecture
## Indices Reference & Maintenance Specification

| | |
|---|---|
| **Instrument ID** | ERES-BERA-2026-001 |
| **Spec version** | Indices Spec v1 (companion to BERA v1 + v1.1 addendum) |
| **Reference implementation** | `bera_rate.py` v1.2 (rating tier) |
| **License** | CCAL v2.1 (CARE Commons Attribution License) |
| **Author / Lock authority** | Joseph Allen Sprute, ERES Institute for New Age Cybernetics — ORCID 0000-0001-9946-3221 |
| **Method** | H2C2H · MIEVM |
| **Status** | Reader/maintainer reference. Indices marked **PROVISIONAL** require JAS canonical lock before external citation. |

> **How to read this document.**
> - **If you only want to *apply* the indices:** read §1 (the split), §3 (the indices), and §4 (the worked example).
> - **If you want to *understand* why it is built this way:** add §2 (pipeline) and §5 (determinism boundary).
> - **If you will *maintain or extend* it:** §6 (lock status) and §7 (the maintenance contract) are the parts that keep the instrument alive. Do not change anything in §7 without going through the lock authority.

---

## 1. The one axiom you must not break: the gate/rating split

BERA produces a **rating** — a measure of *how resonant* a state is. It never produces an **authorization** — a decision about *whether something is permitted*. Those two functions live on opposite sides of a wall.

- **Gate** — a bounded decision (`BIND` / `REFUSE` / `VEILED`). Deterministic, auditable, legally load-bearing. Implemented by **EAAP** (`eaap_proof.py`), **not** by BERA.
- **Rating** — a continuous, multi-dimensional measure (`RATE`, §3.6). Tuning-tier; governance commentary only. Implemented here.

Two prohibitions follow, and both are SOUND-tier correctness requirements:

1. **A rating must never be silently promoted into a gate decision.** A high score authorizes nothing.
2. **A gate decision must never be derived by thresholding a scalar-collapsed rating.** Authorization comes from the gate's conjunctive factors, not from a number crossing a line.

The failure this prevents is a *score quietly becoming a permission*. BERA exists, in part, to make that failure structurally impossible. The reference implementation enforces it by construction: it imports no gate, defines no gate symbols, and exposes no `resonance` field that a gate could read.

---

## 2. The pipeline at a glance

```
 physiological / ecologic channels        (HRV, EDA, RESP, VOC)
            │
            ▼   per-channel coherence metric        ── float, §1.1 OPEN ──┐
   c_HRV, c_EDA, c_RESP, c_VOC  ∈ [0,1]                                    │  FLOAT
            │                                                              │  (front-end)
            ▼   quantize()  →  milli-units [0,1000]    ══ determinism boundary ══
   c_k  (integer)                                                          │
            │                                                              │  INTEGER
            ├──► aggregate coherence  C(t)  = Σ wₖ·cₖ / W_sum              │  (replayable
            │                                                              │   core)
            ├──► indices  ARI · ERI · RCI · RHC                            │
            │                                                              │
            ▼                                                              │
   D(t) = disruption vs. block-A baseline C0                              ─┘
            │
            ▼
   RATE  =  ⟨ R₁ … R₇ ⟩   (7 dimensions, no scalar collapse)
```

**Observables** (§BERA v1 §4): HRV (cardiac autonomic balance), EDA (sympathetic arousal), Respiration (rate/depth), VOC (the ecologic/odor channel). Sampled over a window (test fixtures use 30 s; operational window length is tunable, **OPEN**).

---

## 3. The indices (the golden eggs)

All indices are oriented the same way: **0 = fully decohered, 1 = maximally coherent** (D(t) is the inverse — see §3.5). The canonical encoding fixes field names and six-decimal, half-even precision.

### Summary

| Index | Canonical name | Measures | Status |
|---|---|---|---|
| **ARI** | *Autonomic Resonance Index* | autonomic channel (HRV + EDA) | **PROVISIONAL** — JAS lock required |
| **ERI** | *Ecologic Resonance Index* | bio-ecologic coupling (VOC) | **PROVISIONAL** — JAS lock required |
| **RCI** | *Respiratory Coherence Index* | respiratory channel | **PROVISIONAL** — JAS lock required |
| **RHC** | *Resonant Harmony Cycle* | cyclic coherence across all channels | **LOCKED name** (never "…Cybernetics"); expansion locked as geometric mean |
| **D(t)** | *Disruption index* | coherence loss vs. baseline | **LOCKED form** (v1.1 §1.3) |
| **RATE** | seven-dimensional rating vector | the composite record | **LOCKED principle** (no scalar collapse); dimension map working/OPEN |

> **PROVISIONAL means PROVISIONAL.** ARI, ERI, and RCI carry working expansions below so the instrument is runnable, but those expansions are *proposals*. They must not appear in an external citation until the lock authority confirms them. This is ordinary ERES lock discipline, not a placeholder you may quietly promote.

### 3.1 ARI — Autonomic Resonance Index *(PROVISIONAL)*

Resonance of the autonomic channel, weighting the cardiac signal above electrodermal.

```
ARI = (2·c_HRV + 1·c_EDA) / 3          range [0,1]
```

Working weighting (2:1) is provisional. Computed in integer micro-units in the reference implementation.

### 3.2 ERI — Ecologic Resonance Index *(PROVISIONAL)*

Coupling to the bio-ecologic / environmental channel.

```
ERI = c_VOC                             range [0,1]
```

### 3.3 RCI — Respiratory Coherence Index *(PROVISIONAL)*

Coherence of the respiratory channel.

```
RCI = c_RESP                            range [0,1]
```

### 3.4 RHC — Resonant Harmony Cycle *(name LOCKED)*

Cyclic coherence **across all four channels simultaneously** — the harmonic, not the average. Defined as the geometric mean, so a collapse in any single channel pulls the whole cycle down (a property the arithmetic mean would hide).

```
RHC = (c_HRV · c_EDA · c_RESP · c_VOC) ^ (1/4)      range [0,1]
```

Computed as an **integer fourth root** (two exact `isqrt` calls), never `float ** 0.25` — see §5.
Reference check: channels (0.8, 0.7, 0.6, 0.5) → **RHC = 0.640217** on every platform.

> The name is locked: **Resonant Harmony Cycle**. It is *never* "Resonant Harmony Cybernetics." Maintainers: reject any change that expands RHC to "Cybernetics."

### 3.5 D(t) — disruption index *(form LOCKED, v1.1 §1.3)*

A time-resolved index of *coherence loss from baseline*. This is the inverse-oriented quantity: **0 = at or above baseline (resonant), 1 = collapse.**

```
                ⎧ 0                          if C(t) ≥ C0
        D(t) =  ⎨
                ⎩ clamp_[0,1]( (C0 − C(t)) / C0 )   otherwise
```

where:
- **C(t)** = aggregate coherence at time *t* = `Σ wₖ·cₖ(t) / W_sum`, integer weights, integer cross-multiplication.
- **C0** = baseline aggregate coherence = mean of C over the **resting block (block A)** of the ERES–PELLIS A–B–A–B–A–B design.

**The block-A rule is load-bearing.** C0 comes from the *resting* block, established **once, before** any stressed window is measured. A common implementation error is to baseline on the same window you are measuring — that pins D(t) to 0 forever, because C(t) ≥ C0 always holds against itself. Establish baseline from block A; measure block B against it.

**Disruption onset** (v1.1 §1.4): onset time *t\** is the first *t* where a smoothed-rate condition holds —

```
dD/dt |_smoothed ≥ θ_D    AND    D(t) ≥ D_min
```

θ_D (rate threshold) and D_min (floor) are **tunable parameters, not constants** (OPEN). D(t) is rating-tier: an onset crossing may *inform tuning* of gate parameters, but it never authorizes anything by itself.

### 3.6 RATE — the seven-dimensional vector *(no-collapse LOCKED)*

The indices compose into `RATE`, a seven-dimensional vector. **Scalar collapse of RATE is PROHIBITED** — reducing it to one number discards the dimensional structure the gate/rating split depends on (§1, prohibition 2).

Working dimension assignment (formal R₁…R₇ lock is an **OPEN** item, §6):

| Dim | Content |
|---|---|
| R₁ | ARI |
| R₂ | ERI |
| R₃ | RCI |
| R₄ | RHC |
| R₅ | D(t) |
| R₆ | reserved → **VEILED-R** |
| R₇ | reserved → **VEILED-R** |

A dimension whose evidence is **unresolvable in context** is held as **VEILED-R** — never coerced to a numeric value (cf. CyberRAVE: *Cybernetic Ratings Abolishing Veiled Exchanges*). RATE always reports across all seven dimensions.

---

## 4. Worked end-to-end example

Using the reference implementation's own run (integer milli-/micro-units shown so you can reproduce exactly).

**Step 1 — Block A (resting) → baseline.** Three resting windows give aggregate coherences whose integer mean is:

```
C0 = 771 milli  (= 0.771)
```

**Step 2 — Block B (stressed) → quantized channel coherences.**

```
c_HRV = 1000   c_EDA = 609   c_RESP = 0   c_VOC = 780     (milli-units)
```

**Step 3 — Aggregate coherence** with weights w = (HRV 4, EDA 2, RESP 2, VOC 0), W_sum = 8:

```
C(t) = (4·1000 + 2·609 + 2·0 + 0·780) / 8
     = (4000 + 1218) / 8  =  5218 / 8  =  652 milli   (= 0.652, floor)
```

**Step 4 — D(t)** against the block-A baseline:

```
D(t) = (771 − 652) · 1e6 // 771  =  119000000 // 771  =  154345 micro  (= 0.154345)
```

A fresh *resting* window measured against the same baseline gives D(t) ≈ 0.060 — so the stressed block is **2.6× more disrupted** than rest. (The prior draft, self-baselining, returned 0.000 here; that was the bug this spec's block-A rule prevents.)

**Step 5 — RATE vector** (RHC = 0 because c_RESP = 0 collapses the geometric mean — exactly the harmonic behavior RHC is meant to show):

```
RATE = ⟨ ari 0.869666, eri 0.780000, rci 0.000000, rhc 0.000000,
         d_t 0.154345, R₆ VEILED-R, R₇ VEILED-R ⟩
```

> Note the metric-validity caveat this example surfaces: the provisional HRV proxy maps high RR variability to high coherence, so a stressed actor reads c_HRV = 1.0. That keeps stressed D(t) modest. The *direction* of the HRV metric is an OPEN sub-spec (§1.1) — a lock candidate, not a settled result.

---

## 5. The determinism boundary (why maintainers care)

BERA's rating record must be **bit-identical across platforms** so two parties replaying the same inputs get the same `RATE`, byte for byte. That guarantee has a precise boundary:

- **Upstream of `quantize()` — float, and OPEN.** The per-channel coherence metrics (§1.1) are the sensor front-end. They are the *only* floating-point stage and are explicitly swappable lock candidates.
- **From the quantized coherence vector forward — integer only.** C(t), the indices, RHC, and D(t) are computed in integer fixed-point. `quantize()` maps each coherence to milli-units `[0,1000]` with half-even rounding; everything after that is integer arithmetic.

Two rules make this real, and both are in the maintenance contract:
- **RHC uses an integer fourth root** (`isqrt(isqrt(·))`), never `x ** 0.25`. `math.isqrt` is exact and platform-independent; float exponentiation is not.
- **C(t) and D(t) use integer cross-multiplication and floor division**, never floating-point accumulation.

---

## 6. Lock status — what is settled, what is open

| Item | Status | Authority |
|---|---|---|
| Gate/rating split + two prohibitions (§1) | **LOCKED** | canonical axiom |
| RHC name = "Resonant Harmony Cycle" | **LOCKED** | canonical |
| RHC expansion = 4-channel geometric mean | **LOCKED** (v1.2 impl) | JAS |
| D(t) functional form (§3.5) | **LOCKED** (v1.1 §1.3) | JAS |
| D(t) as rating-tier (non-gating) | **LOCKED** | canonical |
| Onset condition *shape* (§3.5) | **LOCKED** | JAS |
| RATE = 7-D, scalar collapse prohibited | **LOCKED** | canonical |
| VEILED-R for unresolvable dimensions | **LOCKED** | canonical |
| ARI / ERI / RCI canonical expansions | **OPEN — PROVISIONAL** | JAS |
| Integer weight vector wₖ (currently VOC = 0) | **OPEN** | JAS |
| θ_D, D_min, early-warning estimator window | **OPEN** | JAS |
| Per-channel coherence metric sub-specs (§1.1) | **OPEN** | JAS |
| Operational window length (30 s = test fixture) | **OPEN** | JAS |
| Formal R₁…R₇ dimension map | **OPEN** | JAS |
| BERA–PSO cross-domain correspondence (§8) | **HYPOTHESIZED** | Pellis sign-off gate |

---

## 7. The maintenance contract — how not to kill the goose

These invariants are what make BERA an asset rather than a one-off document. **Changing any of them is a lock-authority action, not a maintainer action.** A reviewer should reject a pull request that violates any of them.

- **I1 — Split.** A rating never authorizes. A gate decision never derives from a thresholded, scalar-collapsed rating. The rating module must import no gate, define no gate symbols, and expose no field a gate would read as a decision input.
- **I2 — No collapse.** `RATE` is always reported across all seven dimensions. No code path reduces it to a scalar.
- **I3 — D(t) bounds.** D(t) ∈ [0,1] for all inputs, and D(t) = 0 exactly when C(t) ≥ C0.
- **I4 — Determinism boundary.** Float lives only upstream of `quantize()`. RHC uses the integer fourth root; C(t)/D(t) use integer cross-multiplication. No float in the post-quantization core.
- **I5 — RHC name.** Resonant Harmony **Cycle**. Never "Cybernetics."
- **I6 — VEILED-R discipline.** An unresolvable dimension is held VEILED-R, never coerced to a number.
- **I7 — Block-A baseline.** C0 is established from the resting block before any stressed window is measured. Never self-baseline.
- **I8 — Provisional ≠ canonical.** Indices marked PROVISIONAL/OPEN do not appear in external citations until the lock authority confirms them.
- **I9 — Hypothesis tag.** The BERA–PSO correspondence stays tagged HYPOTHESIZED wherever it appears; any deposit touching it is gated on Pellis sign-off.

**Extending the instrument (the safe path).** The architecture is deliberately built so the *open* parts can change without touching the *locked* core:
- Replacing a coherence metric (§1.1) or the weight vector affects only the front-end and the integer weights; the determinism boundary, D(t) form, and RATE structure are untouched.
- Locking an index expansion (ARI/ERI/RCI) is a JAS action: confirm the expansion, move its row in §6 from OPEN to LOCKED, update §3, and only then is it externally citable.
- Adding a channel or a RATE dimension is a dimension-map change (§3.6) and must preserve I2 and I6.

Every change should be replay-verified (same inputs → identical `RATE` tuple) and, ideally, fuzz-checked against I1–I7 before merge.

---

## 8. The cross-domain hypothesis (clearly fenced)

> **HYPOTHESIZED — conceptual, not engineered.** The working hypothesis (the **BERA–PSO correspondence**) is that the functional form of D(t) as a physiological system approaches coherence breakdown shares its shape with spectral collapse near a disruption in a confined fusion plasma. The proposed shared mechanism is critical-transition early-warning theory (critical slowing down): rising lag-1 autocorrelation and rising variance of the coherence residual `C(t) − C0` preceding onset *t\**.
>
> This is **a hypothesis to be tested under the ERES–PELLIS protocol, not a demonstrated result.** It was previously a SOUND-tier failure to describe this correspondence as "directly engineered"; it is a conceptual hypothesis only. BERA's architecture *supports the test* (it defines D(t) and the observation protocol); it does **not** assert the correspondence holds. Any deposit touching this correspondence is gated on Pellis sign-off.

---

## 9. Position in the ERES instrument stack

1. **Deterministic reference implementation (EAAP gate)** — legally load-bearing (Daubert-relevant).
2. **MIEVM-LLM ensemble** — governance commentary only.
3. **BERA (this instrument)** — governance tuning only.

Consequence-bearing authorization flows through tier 1. BERA tunes and describes; it does not authorize. Any claim placing BERA in a load-bearing decision role is out of specification.

---

*Three Governing Principles (operationally binding): Don't hurt yourself. Don't hurt others. Build for generations to come.*

*BERA — Bio-Ecologic Resonance Architecture · ERES-BERA-2026-001 · CCAL v2.1*
