# REAL Dimensional Consistency — Resolution (Working Draft v0.1)
**Status tier: HYPOTHESIZED where noted. Resolves Pellis's second objection. No dependency on his simulation — fully closeable now.**

---

## 1. The direct check (and a correction to existing material)

REAL = `(E·M·R)/(T·S)` — Energy·Matter·Resonance over Time·Space.

A prior document in the corpus (Talonics, §4.4) asserts: *"Because REAL is a ratio of products, it is dimensionless."* This is checked directly and is **not correct as stated**. Using ordinary physical dimensions:

```
[E] = M·L²·T⁻²      [M] = M      [T] = T      [S] = L

(E·M)/(T·S)  =  (M·L²·T⁻² · M) / (T · L)  =  M²·L·T⁻³
```

That is not dimensionless. "A ratio of products" is not, by itself, a sufficient condition for dimensionlessness — only a ratio in which numerator and denominator dimensions actually cancel is. Pellis's original objection was correct, and the existing internal claim should be retired rather than carried forward into anything sent to him.

---

## 2. The actual fix: REAL is a constructed index, not a literal physical quantity

The resolution is not to find a hidden physical law that makes `(E·M·R)/(T·S)` cancel — it doesn't, and forcing one would be the kind of overclaim Pellis is positioned to catch. The honest fix is the same move used for standard dimensionless numbers in physics (Reynolds number, Mach number, etc.): **each term is a ratio to an explicit reference quantity of the same kind**, so each ratio is dimensionless by construction, and the product of dimensionless ratios is dimensionless.

```
REAL(t) := ( (E(t)/E_ref) · (M(t)/M_ref) · R(t) ) / ( (T(t)/T_ref) · (S(t)/S_ref) )
```

`R(t)` needs no reference scale — it is already dimensionless by construction from Prong 1 (`R(t) = σ(α(t)/α_ref)`, a bounded sigmoid output).

**This is dimensionless by definition, not by discovered law.** That distinction must be stated plainly in anything external: REAL's consistency is a modeling convention — a disciplined choice of how the four reference quantities are fixed — not a derived necessity. Claiming otherwise is exactly the overclaim risk flagged earlier in this work.

---

## 3. A path considered and retracted

An earlier working note proposed that `T_ref` and `S_ref` might not need inventing at all — that they could collapse directly onto Pellis's own renormalization dilation factors (`t → λᶻt`, `x → λx`), which would make the normalization "native" to his theory rather than an ERES-side patch.

This does not actually simplify things, and is retracted as the preferred path, for two reasons:

1. It would only buy invariance under Pellis's *specific* morphogenetic RG flow — not general dimensional consistency. REAL is used as an ERES governance index, not a claim about biological renormalization; tying it to his RG exponents would overstate what REAL is for.
2. "Matter" in REAL has no clean, named counterpart in Pellis's own variables (`ρ`, `P`, `g_ij`) to inherit a scaling dimension from. Forcing one would be invented, not native — the opposite of the intended simplification.

**Conclusion: the reference-ratio normalization (§2) is the adopted resolution.** This section is recorded so the retraction is visible, not silently dropped.

---

## 4. Defining the reference quantities — anchored to existing operational items, not invented fresh

Each reference quantity should be pinned to something already defined or already flagged as an open item in the corpus, rather than created new:

| Term | Reference | Anchor |
|---|---|---|
| `T_ref` | characteristic timescale | the **window length** — already an open item in the BERA spec ("confirm operational default vs. the 30 s test fixture"). Resolving that item *is* defining `T_ref`; this should not be done twice, independently, in two documents. |
| `S_ref` | characteristic spatial scale | a baseline **VLSA deployment tier** (e.g. S0, the smallest/personal tier), per the existing tiered spatial framework. |
| `E_ref` | characteristic energy scale | not yet pinned to an existing defined quantity. Candidate: a baseline coherence-loss rate consistent with `C0` in the `D(t)` definition — but this needs confirmation, not assumption. |
| `M_ref` | characteristic mass/substrate scale | not yet pinned. No existing canonical baseline identified in the corpus to anchor this to. |

`E_ref` and `M_ref` are genuinely open — flagged as such rather than papered over with placeholder values. Inventing numbers here to make the document look complete would reintroduce exactly the kind of unearned precision this whole effort is trying to remove.

---

## 5. What invariance actually means here

Once references are fixed, REAL is invariant under any global rescaling of units **because** numerator and denominator co-scale by definition — e.g., doubling the unit used to measure `E` doubles both `E` and `E_ref` identically, leaving `E/E_ref` unchanged. This is true by construction, not a theorem requiring proof. It should be presented to Pellis exactly that way: a stated convention with a one-line justification, not a result claimed to follow from deeper necessity.

---

## 6. Status

**Resolved, no dependency on Pellis:**
- The original "automatically dimensionless" claim is corrected
- The reference-ratio construction is adopted and stated honestly as convention, not law
- The RG-dilation alternative is considered and explicitly retracted, with reasons recorded
- `T_ref` and `S_ref` are anchored to existing open items rather than invented

**Open, not yet resolved:**
- `E_ref` and `M_ref` have no canonical anchor yet — this needs a decision from you, not from Pellis, before this document is considered closed
- The window-length item (`T_ref`'s anchor) needs its own resolution first, per the existing v2 audit list — this document inherits that dependency rather than duplicating it
