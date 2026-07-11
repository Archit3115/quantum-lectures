# Session 1 — Deep-Research Notes (July 2026)
### Refreshed & mega-science material for the Qiskit-template deck
*Compiled from 3 parallel researcher passes (primary sources: arXiv, Nature/Science/PRX, DST/PIB, McKinsey/BCG, IBM/Google/CERN/LIGO/ITER). Every non-obvious figure carries a source. Items flagged UNVERIFIED must not be asserted as fact on slides.*

---

## A. Global market & the 2025 inflection (verified)
- **McKinsey Quantum Technology Monitor 2026:** quantum-computing economic value **$1.3T–$2.7T by 2035** (present as a range, "up to $2.7T"). Internal market **$60–100B by 2035** (QC = $43–71B). QC companies **>$1B revenue in 2025 → ~$4.4B by 2028**. Start-up investment **$12.6B in 2025 = 6.3× 2024**, ~90% to quantum computing. 300+ enterprises engaged; 33% spend >$10M/yr. (McKinsey, Feb 2026)
- **BCG (Jul 2024, still current):** **$450–850B** economic value by 2040; **$90–170B** provider market. Phasing: NISQ→2030, broad advantage 2030–2040, full FT after 2040.
- **Talent (reframed, honest):** ~**250,000 roles by 2030, ~840,000 by 2035** (McKinsey 2026). Supply: QED-C counts **16,482 pure-play workers, 8,261 new openings in 2025**; McKinsey framing **≈3 openings per qualified hire, ~half of 2025 roles unfilled.** *(Use this framing, not the old "5,000 vs 10,000" pair.)*
- **2025 hardware firsts:**
  - **Google Willow** — 105 qubits, Nature 9 Dec 2024, first **below-threshold** surface-code QEC, distance-7 memory, **Λ = 2.14 ± 0.02**.
  - **D-Wave Advantage2** — Science 12 Mar 2025, spin-glass/magnetic-materials dynamics beat ORNL Frontier (minutes vs ~1M yr); 4,400+ qubits. *(Label "contested" — classical tensor-network rebuttals.)*
  - **Google "Quantum Echoes"** — Nature 22 Oct 2025, first **verifiable** quantum advantage **~13,000×**, via **OTOCs**, on 65 of Willow's 105 qubits. *(Also drew classical rebuttal — call "claimed/verifiable-advantage.")*

## C-future. Where the field goes (verified)
- **IBM Starling (2029):** 200 logical qubits, 100M gates, qLDPC codes; interim Loon(2025)→Kookaburra(2026)→Cockatoo(2027); successor **Blue Jay = 2,000 logical qubits / 1B ops**.
- **Google:** useful error-corrected machine ~2029; end-state ~1M physical qubits (on Milestone 3).
- **Quantinuum:** Helios (Nov 2025, ~100 physical qubits, real-time QEC) → Sol(2027) → **Apollo (2029)**, universal FT by 2030.
- **PsiQuantum:** photonic million-qubit target; Omega chipset (GlobalFoundries); Brisbane+Chicago sites; $1B Series E (Sep 2025).
- **AI × Quantum — AlphaQubit** (Google DeepMind, Nature Nov 2024): transformer neural decoder for surface code, 6%→30% decoding improvement, tested to 241 qubits.
- **QRAM / data-loading bottleneck:** the real Achilles heel of QML speedups. Zhejiang Univ. first superconducting **bucket-brigade QRAM** demo (Jun 2026): 4-bit/8-bit addressing at ~81%/~60% fidelity (proof-of-concept). Jaques & Rattew (2025): cheap passive scalable QRAM unlikely under current proposals.

---

## B. India — NQM & ecosystem (verified, with corrections)
- **NQM:** approved 19 Apr 2023; **₹6,003.65 cr**; 2023-24→2030-31 (8 yr); ~$0.73B. Staged qubits **20–50 (yr3) → 50–100 (yr5) → 50–1000 (yr8)** (superconducting + photonic). **152 researchers / 43 institutions / 17 states (+2 UTs) / 14 technical groups.**
- **4 T-Hubs:** Computing = **IISc Bengaluru**; Communication = **IIT Madras + C-DOT**; Sensing & Metrology = **IIT Bombay**; Materials & Devices = **IIT Delhi**. (Operational since Oct 2024.) *(IIT Kanpur as overall coordinator = UNVERIFIED — do not assert.)*
- **Indigenous hardware:** QpiAI **"Indus" 25-qubit** (World Quantum Day, 14 Apr 2025; 1q fidelity 99.7%, 2q 96%); QpiAI **"Kaveri" 64-qubit** (3 Nov 2025; commercial late 2026). IISER Pune **20-qubit ⁴⁰Ca⁺ ion-trap due end-2026** (25 ions already trapped).
- **Amaravati Quantum Valley** launched **7 Feb 2026** (MoU/launch). *(CORRECTED:)* the machine is an **IBM Quantum System Two with a 156-qubit IBM Heron** (India's largest), **commissioning ~Sept 2026**. Partners **IBM + TCS + Govt. of Andhra Pradesh**; **L&T** infrastructure; 50+ partners.
- **~1,000 km quantum comms** demonstrated **8 Apr 2026** (indigenous **QNu Labs ARMOS QKD**, VIAVI-validated) — ahead of the 2,000 km/2031 target.
- **National PQC / quantum-safe roadmap** (Feb 2026); Critical Information Infrastructure to begin PQC migration by 2027.
- **NQM startups:** 8 selected (~₹30 cr / ~$3.5M each): **QNu Labs, QpiAI, Dimira, Prenishq, QuPrayog, Quanastra, Pristine Diamonds, Quan2D** *(NOT "QUTE")*; pool since **expanded to 17**.
- **Funding comparison (approx / estimates):** India ~$0.73B/8yr · China ~$15B (reputed) · UK £2.5B/10yr (+£2B Mar 2026) · US $2.5B+ cumulative (NQI) · Germany ~€2–3B · France PROQCIMA 128 logical qubits by 2030 (→2,048 by 2035). *India's edge = algorithm/software/talent layer, not spend.*

---

## §4 MEGA-SCIENCE — quantum ML & quantum sensing (the required Section 4 core)

### LIGO / gravitational waves
- **Frequency-dependent squeezing (A+):** broadband quantum-noise reduction **4.0 dB (Hanford) / 5.8 dB (Livingston)** via new **300 m filter cavities**; extends range **15–18%**, boosting **detection rate up to 65%** in O4. Beats the standard quantum limit across tens of Hz–kHz. (Phys. Rev. X 13, 041021, 2023)
- **Gravity Spy** (citizen science + ML) glitch classification: **22→23 glitch classes**, **>30,000 volunteers, >7M classifications**; new O4 multi-view fusion CNN **94.1% accuracy, AUC 0.965**. (arXiv:2401.12913)
- **Quantum ML on GW data:** "quantum variational rewinding" treats interferometer readings as anomalies in background noise — **linear-time** vs quasilinear matched filtering; recovered all confirmed events in noiseless sim. (Quantum Machine Intelligence, 2025)
- **LIGO-India:** groundbreaking **23 Apr 2026**, Aundha (Hingoli, Maharashtra), 174 acres, two **4 km arms**, target ~**2030**, ≈₹2,600 cr.

### CERN / LHC (CERN Quantum Technology Initiative, est. 2020)
- **Unsupervised quantum clustering — the headline win:** "Quantum anomaly detection in the latent space of LHC collision events" runs **QK-means / QK-medians + a quantum kernel** on autoencoder latent features for new-physics searches, and found a regime where the **quantum model *significantly outperforms* classical** on real hardware. (Woźniak, Vallecorsa et al., **Commun. Phys. 7, 334, 2024**; arXiv:2301.10780)
- **Track reconstruction as QUBO** on **D-Wave 2X** over TrackML (33 logical qubits, ~500 tracks); annealing-inspired classical (QAIA) then gave **~4 orders-of-magnitude speed-up**, scaling toward HL-LHC. (Quantum Mach. Intell. 2021; EPJ 2024)
- **QSVM for Higgs (ttH):** matched classical SVM/BDT at up to **20 qubits / 50,000 events**; ran on IBM 15-qubit hardware. A second study: 4–6-qubit QSVM **AUC ≈ 0.68**, at parity with classical. (PRResearch 3, 033221, 2021)
- **Data driver:** HL-LHC (2029–2042) collects **>10×** current data; storage enters the **exabyte** regime; compute ~**50–100×** today's.

### ITER / magnetic-confinement fusion
- **DeepMind × EPFL (TCV):** deep-RL directly controlled tokamak magnetic coils to sculpt/sustain varied plasma shapes — first RL magnetic control on a real tokamak. (Nature 602, 414, 2022)
- **Disruption avoidance (DIII-D):** RL controller forecasts tearing instabilities **up to 300 ms ahead** and steers actuators to stay stable. (Nature 626, 746, 2024)
- **Cross-machine disruption prediction (FRNN):** trained on DIII-D+JET, first reliable predictions on an untrained machine — crucial for ITER (needs ~30 ms warning). (Nature 568, 526, 2019)
- **Quantum for fusion:** quantum algorithms mapped to plasma simulation / turbulence / transport; QAOA for stability; hybrid QC-PIC prototypes. NV-center diamond magnetometry toward radiation-hard diagnostics (ODMR to ~1.2 T).
- **ITER new baseline (2024):** first-plasma-2025 dropped; DT phase **2039**, **Q ≥ 10 in 2044**.

### SKA / radio astronomy
- **Scale:** ~**8 Tbit/s** to signal processors; each SDP ~135 PFLOPS; archive **>700 PB/yr → ~8.5 EB**; SKAO says the arrays generate **>100× current global internet traffic** (order-of-magnitude). SKA-Low = 131,072 antennas; SKA-Mid = 197 dishes.
- **Unsupervised pipelines:** convolutional-autoencoder + nearest-latent-neighbour novelty detection flags **RFI without labels**; DBSCAN groups false positives. (MNRAS 516:5367, 2022). Anomaly-detection + active learning on MeerKAT surfaces rare transients (MNRAS 538:1397, 2025).
- **Quantum-ML pilot:** quantum-kernel SVM for galaxy morphology (spiral vs elliptical), **ROC AUC 0.946**, statistically identical to classical SVM; on IBM hardware AUC 0.83. (RASTI 2:752, 2023)
- **Status:** SKA-Low first image Mar 2025 — **85 galaxies in 25 deg² with <1% of antennas**; SKA-Mid "first fringes" Jan 2026.

### DUNE / neutrinos
- **Scale:** 4 LArTPC modules ~1.5 km underground, **70 kt LAr (≥40 kt fiducial)**; **30–60 PB/yr**. Each event = a high-res 3D image of tracks → CNN/graph-net reconstruction; clustering separates overlapping tracks/showers.
- **Quantum ML:** Neural Projected Quantum Kernels + QCNN classify **track (νμ) vs cascade** in IceCube-like data, **~80% accuracy at 1–100 TeV**, validated on **IBM Strasbourg 127-qubit** hardware — at parity with classical. (arXiv:2506.16530, 2025). VQC on LHC data AUC 0.81. (J. Phys. G 48:125003, 2021)
- **Status:** cryostat steel lowered underground 2026; FD2 cryostat 2026, FD1 2027.

### Cold-atom quantum sensing (mega-science instrumentation)
- **Gravimeters/gradiometers:** cold-atom gravimeter **2.2 µGal·Hz⁻¹ᐟ²** (vs ~5 for classical); operated **500 m underground** (LSBB). Birmingham **quantum gravity gradiometer made the first outdoor detection of a buried tunnel ~1 m down** (Nature 602, 590, 2022) → ~10× faster surveys; used for **CO₂-plume monitoring** at carbon-storage sites (signals 0–16 µGal).
- **Optical clocks:** JILA Sr lattice clock **8.1 × 10⁻¹⁹** systematic uncertainty; single-ion near **1 × 10⁻¹⁹**; **~10⁻¹⁶/metre** enables cm-level chronometric levelling (18 digits on Tokyo Skytree). (PRL 133:023401, 2024; Nat. Photonics 14:411, 2020)
- **Magnetometers:** SERF OPM **~4.5 fT·Hz⁻¹ᐟ²**, surpassing SQUIDs at low frequency. (2024)
- **Large-scale:** **MAGIS-100** (Fermilab, 100 m Sr interferometer), **AION** (10 m→100 m→1 km, mid-band 0.01–few Hz between LISA and LIGO), **AEDGE** (space). Ultralight-dark-matter + GW.

### Synthesis (for the closing Section-4 slide)
Every mega-science program emits **extreme-dimensional, mostly UNLABELLED** data — SKA's petascale visibility cubes, DUNE's sparse 3D argon images, LIGO's noisy strain series — far beyond hand-tuning. That is exactly **clustering / anomaly-detection / unsupervised-representation** territory (why autoencoders, DBSCAN, active learning dominate today's pipelines). Quantum offers leverage from **both ends**: quantum **kernels/annealers** embed the data in exponentially large Hilbert spaces (so far parity on galaxies/neutrinos, but a *significant* win for CERN's unsupervised latent-space anomaly detection on real hardware), and quantum **sensors** (atom interferometers, optical clocks, SERF magnetometers, squeezed light) generate a new class of ultra-precise measurements that themselves become fresh unlabelled data streams.

> **Honest caveat to carry:** across astronomy/neutrino/GW domains, most quantum-ML results are **at parity** with classical, not yet superior — the clearest *outperformance* on real hardware to date is CERN's unsupervised quantum clustering of LHC latent-space events (Commun. Phys. 2024).
