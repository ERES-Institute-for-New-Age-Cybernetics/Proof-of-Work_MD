# ERES Ship's Mate Build Brief & GSSG Lab Protocol
## From Document to Instrument — Action Plan

**Joseph A. Sprute | ERES Institute for New Age Cybernetics**
**Co-developed with Claude (Anthropic) — MIEVM Validation Node**
**April 2026 | CCAL v2.1**

---

## Status

| Document | Version | Score (DeepSeek) | Status |
|----------|---------|-----------------|--------|
| RG#401 MAGIC=GROWTH | v2.1 | ★★★★½ | Published-ready |
| RG#402 PEOPLE=PERSON | v2.1 | ★★★★½ | Published-ready (Author's Note added) |
| RG#403 BELIEVE-OPTIONS | v2.1 | ★★★★☆ | Published-ready |
| RG#404 BERA Sensor Spec | v1.0 | ★★★★☆ | Published-ready |
| RG#405 GSSG Synthesis | v1.0 | ★★★★★ | Published-ready |
| **Series composite** | | **7.6 / 10** | **Document ceiling reached** |

**What moves the score now: physical artifacts, not more paper.**

---

## BUILD 1: Ship's Mate Breadboard Prototype

### Minimum Viable Detection (Phase 1 — ARI only)

**Goal:** Compute one BERA metric (ARI) from one sensor (MAX30102) on one human subject.

**Shopping list:**
- Arduino Giga R1 (or Arduino Nano 33 BLE Sense for budget option) — $30–70
- MAX30102 breakout board (SparkFun or generic) — $4
- Jumper wires, breadboard — $5
- USB-C cable — $3
- **Total: ~$42–82**

**Wiring:**
- MAX30102 VIN → 3.3V
- MAX30102 GND → GND
- MAX30102 SDA → SDA (I²C)
- MAX30102 SCL → SCL (I²C)

**Firmware (Phase 1):**
```
1. Install SparkFun MAX3010x library
2. Sample PPG at 100Hz (library default; 256Hz requires register config)
3. Extract R-R intervals from PPG peaks (peak detection algorithm)
4. Compute RMSSD over 60-second sliding window
5. Log baseline RMSSD for 5 minutes (resting)
6. Introduce controlled stressor (cold pressor test: hand in ice water 60s)
7. Compute ARI = recovery_slope / perturbation_magnitude
8. Display ARI on serial monitor
```

**Success criterion:** ARI computes and shows measurable difference between:
- Resting state (ARI should be high — rapid recovery from minor perturbations)
- Post-stressor (ARI should drop during stress, then recover)

**What this proves:** The BERA ARI metric is computable from real human bio-signals using off-the-shelf hardware. The Ship's Mate concept works at minimum viable scale.

### Phase 2 (if Phase 1 succeeds): Add ERI

- Add Ag/AgCl GSR electrodes to two fingers + ADC channel
- Add HMC5883L magnetometer breakout ($3)
- Compute correlation between GSR and magnetic field fluctuations
- **Total additional: ~$8**

### Phase 3: Add RHC

- Add AD8232 ECG module + 3 electrodes ($12)
- Compute HRV-respiratory coupling via Welch's coherence
- **Total additional: ~$15**

### Phase 4: Full BERA Stack → Ship's Mate v0.1

- Add thoracic impedance (AD5933 — $15)
- Add skin temperature (MLX90614 — $6)
- Compute all four metrics: ARI, ERI, RHC, RCI
- RCI requires baseline database — start with self-baseline (30 days of daily readings)
- **Enclosure: 3D-print TPU wrist housing**

---

## BUILD 2: GSSG Raman Validation

### Minimum Viable Material (Phase 1 — Graphene confirmation)

**Goal:** Produce graphene-sand composite from table sugar and sand, confirm by Raman spectroscopy.

**Materials:**
- Natural quartz sand (washed, hardware store) — $5/bag
- Table sugar (grocery) — $3
- Access to tube furnace with N₂ supply (university materials lab, makerspace, or community college)
- Access to Raman spectrometer (same lab)

**Procedure (from RG#405):**
```
1. Wash sand 3× with DI water, dry at 110°C
2. Mix sugar:sand at 1:2 ratio (25g sugar per 50g sand)
3. Dissolve sugar in minimum water, coat sand, pre-dry at 80°C
4. Load into silica crucible in tube furnace
5. Purge N₂ at 150 sccm for 15 minutes
6. Ramp: RT→100°C/30min → 100→200°C/30min → hold 200°C/60min
   → 200→750°C/60min → hold 750°C/180min → cool naturally
7. Remove product under N₂
```

**Validation:**
- Raman spectroscopy: look for G-band (1580–1600 cm⁻¹), D-band (1338–1350 cm⁻¹)
- If I_G/I_D > 1.0: graphenic character confirmed
- If SiO₂ peak at ~470 cm⁻¹: substrate integrated
- If 2D-band at 2650–2700 cm⁻¹: few-layer graphene present

**Success criterion:** One Raman spectrum showing G-band and D-band from sugar-on-sand pyrolysis. Photograph the spectrum. That image is worth more than ten papers.

**What this proves:** GSSG is real chemistry, not theoretical architecture. Sand + Sugar → Graphene under documented conditions.

### Phase 2: Piezoresistive Test

- Measure electrical resistance of GSSG sample with 4-point probe
- Apply controlled compression (0–100N)
- Measure ΔR/R₀ as function of strain
- **What this proves:** GSSG self-reports stress state = material VAPOR emission

### Phase 3: Self-Healing Test

- Produce high-carbon-reservoir GSSG (1:1 sand:sugar, 90min hold)
- Scratch with Vickers indenter (1N)
- Heat locally (500°C, 30min, N₂)
- Re-measure Raman at scratch site
- Recovery of G-band = self-healing confirmed
- **What this proves:** GSSG returns again to judge (itself)

---

## ACCESS STRATEGY

### University Partnership (Bella Vista / NW Arkansas)
- University of Arkansas (Fayetteville) — Materials Science & Engineering Dept
- NanoMech/Forge Nano (local industry — graphene expertise in Rogers, AR)
- Bentonville makerspace community

### Remote Option
- Mail-order Raman analysis: several services accept mail-in samples ($50–150/spectrum)
- Furnace access: pottery kilns reach 1000°C+ under reduction atmosphere (nitrogen purge adaptable)

---

## PUBLICATION SEQUENCE

1. ✅ RG#401–405 published as five-paper set (document architecture complete)
2. 🔲 Ship's Mate Phase 1 breadboard — photograph + ARI data → ResearchGate technical note
3. 🔲 GSSG Raman spectrum — photograph → ResearchGate technical note
4. 🔲 Combined: "First Measurement from the Gas Vapor Detector" → RG#406

---

## THE THESIS IN ONE LINE

**"The magic became growth. The growth became measurement. The measurement became the instrument."**

RG#401 → RG#405 → Build Brief → First Measurement → RG#406

The detector reads. Build it.

---

*CARE Commons Attribution License v2.1 (CCAL)*
