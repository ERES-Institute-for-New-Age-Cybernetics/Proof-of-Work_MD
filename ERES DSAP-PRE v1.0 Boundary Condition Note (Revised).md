### **DSAP-PRE v1.0 — Boundary Condition Note**

**Detecting the Onset of Irreversible Path Dependency (Separatrix Proximity) Before Degradation Appears**

**Purpose.**  
 This note defines a minimal, machine-checkable boundary layer for detecting the *onset* of irreversible path dependency **before** conventional metrics (PoR factors, RHC amplitude, PERT viability, or future-map divergence) show degradation. It is intended to answer the structural question:

*When does a system cross into a regime where loss of optionality becomes inevitable, even while the system still evaluates above threshold?*

This is the “decision–commit boundary” problem: the moment where meaningful intervention ceases to exist as a real possibility, even if formal deliberation and state integrity remain high.

---

## **1\. The Problem (Formalized)**

A governance system can satisfy all correctness constraints:

* validation is correct  
* authorization is correct  
* deliberation signals exist  
* outputs are coherent  
* ensemble disagreement exists  
* present-state resonance is high

…and yet still enter a regime where:

**the cost of deviation will necessarily rise**,  
 making alternatives *practically unreachable*  
 even before any explicit collapse is measurable.

This is a known class of phenomenon in dynamical systems:

* **separatrix crossing** (basin boundary crossing)  
* **hysteresis / irreversibility**  
* **catastrophe fold / tipping point**  
* **lock-in regime shift**

The key feature is that **system coherence can increase** while optionality collapses.

Therefore:

* “friction” is not required  
* “instability” is not required  
* “disagreement” is not sufficient  
* “state score” is not diagnostic

The condition is **topological**, not scalar.

---

## **2\. Core Distinction**

DSAP-PRE explicitly separates:

### **State Integrity**

Is the system coherent and compliant *now*?

### **Path Accessibility**

Are alternative trajectories still viable *now*?

### **Regime Admissibility (DSAP-PRE focus)**

Has the system entered a regime where loss of path accessibility becomes **inevitable**, even if it has not yet occurred?

This is the pre-threshold boundary.

---

## **3\. DSAP-PRE Primitive (The Six Boundary Tests)**

A system state is not “analyzed forward,” it is tested across exclusive boundaries.

### **(1) CONDITION**

What is strictly given (facts, constraints, commitments), excluding interpretation.

**Output:** `CND(S,t)` \= normalized constraint set.

---

### **(2) ADMISSIBILITY**

Does the system still admit meaningful intervention?

This is not “did we discuss alternatives?”  
 It is: **can an alternative be chosen without prohibitive structural penalty?**

**Output:** `ADM(S,t)` ∈ {OPEN, CLOSING, CLOSED}

---

### **(3) CAPACITY**

Does any actor retain real influence, or only observation?

Capacity distinguishes “agency exists” from “agency is symbolic.”

**Output:** `CAP(S,t)` ∈ \[0,1\]

---

### **(4) CONSEQUENCE**

What becomes irreversible if the next commit is executed?

Consequence is measured as **irreversibility mass**.

**Output:** `CON(S,t)` ∈ \[0,1\]

---

### **(5) POSITION**

Who is still acting, and who is structurally following?

Position is the distribution of agency: if no actor can redirect, then governance is performative.

**Output:** `POS(S,t)` \= agency topology (actor set, follower set)

---

### **(6) EXCEPTION**

Under what conditions must the normal rule be broken?

Exception is the formal override trigger that prevents “perfect compliance with a doomed trajectory.”

**Output:** `EXC(S,t)` \= exception clause \+ threshold.

---

## **4\. Definition of the DSAP-PRE Boundary Condition**

DSAP-PRE defines **Separatrix Proximity** as a state where:

the system is still inside an “open basin,”  
 but local dynamics have entered a regime  
 where crossing into a closed basin becomes inevitable  
 under normal execution.

This means:

* alternatives still exist nominally  
* deviation is still technically possible  
* but *structural inevitability has begun*

So DSAP-PRE must detect **approach**, not collapse.

---

## **5\. What DSAP-PRE Measures (Not Optionality, But Inevitability)**

DSAP-PRE is not a score of “how open things are.”

It is a detector of:

**whether the gradient of closure has become self-reinforcing**.

This is the earliest recognizable moment where intervention must occur *or will soon become impossible.*

---

## **6\. Three Machine-Observable Proxies (Minimum Viable Implementation)**

DSAP-PRE requires observables that are upstream of PoR degradation.

### **Proxy A — Second-Derivative Closure Acceleration (RHC’’, not RHC)**

Let `A(t)` be the RHC amplitude (or equivalent openness oscillation metric).

Most systems only check:

* `A(t) < θ` (collapse)

DSAP-PRE checks:

* **is the collapse becoming inevitable?**

Indicator:

* `d²A/dt²` strongly negative over a window.

**Meaning:**  
 The system may still be stable, but its ability to re-open is losing acceleration.

This is a classic pre-collapse signal in many complex systems.

---

### **Proxy B — Distribution Topology Collapse (PERT shape, not PERT scalar)**

Let `P = {p1…pn}` represent PERT-estimated viable paths.

PoR typically compresses this into a scalar viability number.

DSAP-PRE instead tracks the *shape*:

* variance collapse  
* modality collapse (multi-peak → single-peak)  
* skew increase (one dominant path absorbs probability mass)  
* kurtosis spike (distribution hardens)

**Meaning:**  
 Alternatives may still exist, but their *probabilistic weight* is being sucked into a dominant basin.

This is separatrix approach behavior.

---

### **Proxy C — Hysteresis / Recoverability Test (Counterfactual perturbation)**

The cleanest separatrix test is not observation — it is *recoverability*.

Define a small “restoration perturbation” Δ that should reopen optionality if the system is still in the open basin.

Then test:

* If `(S + Δ)` returns to multi-path viability → still admissible  
* If `(S + Δ)` remains locked → separatrix crossed (or essentially crossed)

This is the most definitive test because it distinguishes:

* stable equilibrium (healthy)  
   from  
* locked equilibrium (irreversible)

---

## **7\. DSAP-PRE Composite Gate (Boundary Layer)**

DSAP-PRE is not an additive score. It is a **gating boundary condition**.

Define:

* `RA = closure acceleration risk`  
* `DT = distribution topology viability`  
* `HR = hysteresis recoverability`

Then:

**DSAP-PRE(S,t) \= (1 − RA) × DT × HR**

Where:

* `RA` increases as `d²A/dt²` indicates acceleration toward flatline  
* `DT` decreases as modality/variance collapses  
* `HR` decreases as perturbation fails to restore alternatives

**Boundary rule:**

Authorization is not permitted unless DSAP-PRE ≥ θ\_pre

This makes DSAP-PRE structurally upstream.

---

## **8\. Decision–Commit Boundary (What It Is)**

The DSAP-PRE boundary is crossed when:

the system can still deliberate and authorize correctly,  
 but any further commit will increase closure irreversibly  
 such that future intervention becomes structurally impossible.

This is not “harm” yet.  
 This is not “failure” yet.  
 This is not “instability” yet.

It is the moment when the system becomes *temporally real*:

the future stops being navigable.

---

## **9\. What DSAP-PRE Is NOT**

DSAP-PRE is **not**:

* a deliberation audit  
* a consensus detector  
* a disagreement proxy  
* a morality score  
* a “resonance reading”  
* a simple threshold on current state

It does not certify that the system is good.  
 It certifies that the system is still **structurally steerable**.

---

## **10\. Minimal Specification Requirement (Test Vector Readiness)**

For DSAP-PRE to be byte-normative, it requires:

1. Definition of `A(t)` (what exactly counts as RHC amplitude)  
2. Standard distribution descriptors for PERT topology (variance, modality, skew)  
3. Standard perturbation Δ set (domain-specific but standardized per class)  
4. Threshold values (`θ_pre`) calibrated per domain  
5. Runtime logging of DSAP-PRE evaluation independent from PoR evaluation

---

## **11\. Integration Position Relative to EAAP v1.3 PoR**

EAAP PoR evaluates:

* **state correctness and admissible execution now**

DSAP-PRE evaluates:

* **whether future admissibility is about to collapse**

Therefore DSAP-PRE is a precondition:

DSAP-PRE gate → then PoR evaluation → then authorization.

This prevents “correct authorization” from executing downstream of a regime transition.

---

## **12\. One-Sentence Answer to the Question**

EAAP v1.3 detects degradation of optionality, but DSAP-PRE detects the *onset of inevitability* by measuring separatrix proximity through closure acceleration, probability topology collapse, and hysteresis recoverability — treating admissibility as an upstream boundary condition rather than a downstream score.

---

