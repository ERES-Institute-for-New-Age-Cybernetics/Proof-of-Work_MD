## Section 6 — N(Z): The Normality-Defect Index ("ZEUS")

**Status: HYPOTHESIZED tier.** Not asserted as isomorphic to any Pellis construct. Proposed as a single bounded dial that gives the existing eigenvector-condition-number / Henrici departure-from-normality discussion (§4) a normalized index, with the rotation (normal-operator) regime and the exceptional-point (defective-operator) regime as its two literal poles.

### 6.1 Motivation

§4 established that the leverage operator $J$ moves between two qualitatively distinct regimes:

- **Normal regime:** $J$ normal ($JJ^{*}=J^{*}J$) — e.g. the pure-rotation case $R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$. Eigenvalues $e^{\pm i\theta}$; eigenvectors $(1,\mp i)/\sqrt2$ — fixed, orthogonal, independent of $\theta$. Eigenvector condition number $\kappa(V)=1$.
- **Defective limit:** $J$ at the exceptional point ($\gamma_1\gamma_2=-(\epsilon-\delta)^2$) — eigenvalues coalesce ($\lambda_+=\lambda_-$), eigenvectors collapse parallel, geometric multiplicity drops to 1, $\kappa(V)\to\infty$.

These are not two arbitrary reference points — they are the two structural poles of operator theory itself (normal vs. maximally non-normal). Naming them as fixed anchors of a bounded index is a definitional move, not a claim that they converge.

### 6.2 Definition

Let $\Delta(J)$ be the Henrici departure-from-normality:

$$\Delta(J) = \sqrt{\|J\|_F^2 - \sum_i|\lambda_i|^2} \;\geq\; 0$$

$\Delta(J)=0$ exactly when $J$ is normal. Define the bounded, signed **N(Z) index**:

$$N(Z) \;=\; 1 \;-\; \frac{2\,\Delta(J)}{\Delta(J) + \|J\|_F} \;\in\; (-1,\,1]$$

| Pole | Operator state | Eigenvector geometry | $\kappa(V)$ | $N(Z)$ |
|---|---|---|---|---|
| $N=+1$ | Normal (rotation regime) | Orthogonal, angle-invariant | $1$ | $+1$ |
| $N\to-1$ | Maximally defective (exceptional point) | Parallel / coalesced | $\to\infty$ | $\to-1$ |

### 6.3 "ZEUS" — naming convention for the index

**Zipper Energy United Spectrum (ZEUS)** names $N(Z)$ as an object, with each term keyed to a specific feature of the operator, not used as independent evidence of a mechanism:

| Term | Referent | Basis |
|---|---|---|
| United **Spectrum** | $\lambda_+=\lambda_-$ at $N\to-1$ — eigenvalues literally coalesce | Exact (derived in §3) |
| **Energy** | $\mathrm{Re}(\lambda)$, dissipation/decay term carried from the REAL mapping (§5) | Hypothesis-tier, inherited |
| **Zipper** | Eigenvector state: orthogonal/distinct at $N=+1$ ("open"), parallel/merged at $N\to-1$ ("closed") | Interpretive label for a derived mechanism — naming convention, not independent proof |

Note the asymmetry: "United Spectrum" names the $N=-1$ pole precisely; it does not separately name the $N=+1$ pole (maximally *split*, orthogonal spectrum). The name foregrounds the collapse end of the dial. This is consistent with naming conventions elsewhere in canon (SIGNET, SCALULAR) and does not affect the validity of $N(Z)$ itself — it is a property of the label, not the index.

### 6.4 Relationship to existing constructs

$N(Z)$ is **not** proposed as a replacement for $\kappa(V)$ or $\Delta(J)$ — both remain the primary, unbounded diagnostic quantities (§4). $N(Z)$ is a normalized presentation layer for communicating where a given instrument's operator sits on the normal↔defective spectrum, bounded for comparison across instruments with different scales of $\|J\|_F$.

**Open items (pending Pellis):**
1. Whether $\Delta(J)$ (vs. $\kappa(V)$ directly) is the correct quantity to normalize for this purpose.
2. Whether $N(Z)=-1$ should be reserved strictly for the exceptional point, or extended to the broader defective neighborhood around it.

---
*Drafted 2026-06-21 for insertion into the ERES–Pellis spectral bridge document, following §5 (Proposed Mapping). HYPOTHESIZED tier throughout, consistent with document-wide status convention.*

## License
This work is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) — Creative Commons Attribution 4.0 International. You may share and adapt this material for any purpose, including commercially, provided appropriate credit is given to the original author(s) per the Credits section below.

## Credits
- **Joseph Allen Sprute (JAS)** — ZEUS naming (Zipper Energy United Spectrum), N=+1/N=−1 dial framing, conceptual direction.
- **Claude (Sonnet 4.6, Anthropic)** — formalization, Henrici departure-from-normality derivation, comparison table.
- **Stergios Pellis** — originating operator-theoretic framework (non-self-adjoint Jacobian, exceptional-point structure) this section extends. No claim of endorsement.

## References
1. Henrici, P. (1962). Bounds for iterates, inverses, spectral variation and fields of values of non-normal matrices. *Numerische Mathematik*, 4(1), 24–40.
2. ERES–Pellis spectral bridge document, §§3–5 (toy model and exceptional-point derivation this section extends), 2026-06-20.
