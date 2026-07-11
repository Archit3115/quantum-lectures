# Session 2 — Deep Research 2026 (Quantum-Enhanced Computer Vision)
*Refreshed, cited facts to ground the Session-2 deck. Companion to `session2_research.md`.
Academic SOTA verified via arXiv/alphaXiv + web (mid-2026). India/market/talent numbers reuse `session1_deep_research_2026.md` + `india_quantum_context.md`.*

---

## PART 1 — Academic state of the art (verified, cited)

### 1. Quanvolutional Neural Networks
- **Original:** Henderson, Shakya, Pradhan, Cook, *"Quanvolutional Neural Networks,"* arXiv:1904.04767 (2019), *Quantum Machine Intelligence* 2,2 (2020). Dataset **MNIST**. Original setup = **3×3 window → 9 qubits, threshold encoding, random (untrained) circuits** feeding a classical CNN.
- **Honest headline:** the paper's own control found the quanvolutional (quantum random circuit) results were **statistically indistinguishable from a classical random non-linear transform** — no measurable quantum edge on MNIST. Teach it as an *architecture idea*, not a demonstrated win.
- **The 2×2 / 4-qubit / angle-encoding version** used in the demo notebook is the **PennyLane tutorial** implementation (pennylane.ai/qml/demos/tutorial_quanvolution), NOT the original paper — cite accordingly.
- Follow-ups: trainable/variational quanvolution (arXiv:2106.07327, 2021 — "no single best encoding, it's application-dependent"); quanvolution for pneumonia chest-X-ray detection (arXiv:2510.23660, 2025); encoding-strategy study (arXiv:2512.12512, 2025).
- ⚠ The widely-quoted "MNIST 92%→93% with quanvolution" is from reimplementations/tutorials, **not** Henderson et al. — do not attribute to the original.

### 2. Quantum Convolutional Neural Networks (QCNN)
- **Original:** Cong, Choi, Lukin, *"Quantum Convolutional Neural Networks,"* **Nature Physics 15, 1273 (2019)**; arXiv:1810.03787. Confirmed: **O(log N) variational parameters** for N qubits; alternating quantum-convolution + quantum-pooling layers (MERA + QEC structure) halve qubits per layer.
- **Native strength = quantum data, not photos:** recognizing 1-D symmetry-protected topological **phases of matter**, and **discovering QEC schemes** that outperform comparable known codes.
- **2026 honesty result:** Bermejo et al., *"Quantum Convolutional Neural Networks are (Effectively) Classically Simulable,"* arXiv:2408.12739, **PRX Quantum 7, 020304 (2026)** — randomly-initialised QCNNs act on low-weight measurements and the standard image benchmarks are "locally easy," so classical shadows **efficiently simulate them → no inherent advantage on those image tasks.** Use in the reality check.
- Applied: QCNN for HEP jet-image classification (arXiv:2408.08701, 2024) — competitive, no advantage claim.

### 3. Image encoding (qubit cost is the whole story)
- **Basis:** 1 qubit/bit — wasteful.
- **Angle:** 1 qubit/feature, feature→rotation angle — shallow, NISQ-friendly; what quanvolution uses per window.
- **Amplitude:** d-dim vector → **log₂(d) qubits** (exponentially compact) BUT arbitrary state prep ≈ **O(2ⁿ) gates** → the qubit saving is repaid as depth; the **data-loading bottleneck** that cancels most theoretical speedups (survey arXiv:2606.05387, 2026). Needs **QRAM** (not built at scale).
- **FRQI** (Le, Dong, Hirota, *Quantum Inf. Process.* 10,63 (2011)): a 2ⁿ×2ⁿ image in **2n+1 qubits** = 2n position + 1 colour qubit (grayscale in the colour qubit's amplitude/angle); probabilistic readout.
- **NEQR** (Zhang et al., *Quantum Inf. Process.* 12,2833 (2013)): grayscale in a **q-qubit basis register** → **2n+q qubits**; vs FRQI gives quadratic-faster prep, ~1.5× better compression, **deterministic (exact) readout.**

### 4. Quantum Vision Transformers / quantum attention
- **Cherrat, Kerenidis et al., *"Quantum Vision Transformers,"* arXiv:2209.08167, Quantum 8, 1265 (2024).** 12 MedMNIST (28×28). Quantum variants **match** classical (e.g. RetinaMNIST AUC 0.729 quantum vs 0.736 classical) and **beat classical on 7/12** datasets; claimed **quadratic asymptotic speedup** of attention. Hardware runs limited to **4–6 qubits** (IBM 16q/27q) and "too noisy" beyond that.
- Follow-ups (all simulated / efficiency-metric): quantum self-attention cutting params **O(n²)→O(n)** (arXiv:2503.07294, 2025 — RetinaMNIST 56.5% with ~1K params vs 14.5M); HQViT (arXiv:2504.02730, 2025); end-to-end QViT (arXiv:2402.18940, 2024).

### 5. Barren plateaus & trainability
- Generic deep random circuits: gradient variance **vanishes exponentially** in qubit count (McClean 2018; review arXiv:2405.00781) → untrainable at scale.
- **QCNNs escape it:** Pesah et al., *"Absence of Barren Plateaus in QCNNs,"* **PRX 11, 041011 (2021)** — gradient variance "vanishes no faster than polynomially"; cause = the shallow, hierarchical, O(log n)-depth conv+pool structure.
- Two sides of one coin: the same shallowness that kills plateaus is what makes QCNNs classically simulable (§2). Say both.

### 6. Honest reality — advantage on natural images in 2026?
- **Survey:** Kuete Meli et al., *"Quantum-enhanced Computer Vision: Going Beyond Classical Algorithms,"* arXiv:2510.07317 (Oct 2025) — emerging field, "high potential," but "specialised and fundamentally new algorithms must be developed"; quantum helps only where non-quantum methods can't solve in reasonable time → **no established advantage on mainstream/natural-image tasks.**
- Theory limit: *Nature Comms* (2025, arXiv:2503.20879) — advantage proofs exist for *specific structured* distributions; **none for arbitrary distributions** (real images live in the no-guarantee zone).
- Empirical skepticism: arXiv:2605.27923 (2026), multi-dataset — QML doesn't consistently beat classical.
- **Bottom line:** as of mid-2026, **no demonstrated, hardware-realised quantum advantage on natural (photographic) images.** Reported "wins" are simulated, on tiny 28×28 medical images, or are parameter-efficiency metrics.

### Deck-claim checks
- Quanvolution 2×2/4-qubit/angle/random → 4 channels into classical CNN = **correct as the PennyLane demo** (cite the demo, not Henderson's 3×3/9-qubit original).
- QCNN O(log n) params = **confirmed** (Nature Physics 2019).
- Speaker's QFT-on-IBM result (|5⟩→010 @ 0.688, error grows with depth) = **physically plausible** under the recovery/inverse reading (ideal output a single basis state, degraded to ~0.6–0.7 by NISQ decoherence; peak erodes with depth).

---

## PART 2 — Classical-CV cost + quantum-vision industry + India (verified, cited)

### 1. Classical CV compute & energy (the pressure point)
- **ViT-22B** (Google, Feb 2023): **22B params**, largest dense Vision Transformer (5.5× ViT-e's 4B); trained on ~4B images on **~1,024 TPU-v4 chips** (arXiv:2302.05442). Use as the vision-specific compute proxy.
- **Labelled-data treadmill:** DINOv2 (2023) curated **142M images** for a ~1.1B-param ViT-g; **DINOv3** (Meta, Aug 2025) jumped to **~1.7B images** and a **7B-param** ViT — includes a SAT-493M satellite-pretrained variant. ImageNet-1k ≈ 1.28M labelled images; ImageNet-21k ≈ 14M.
- **ImageNet SOTA plateau ~91%** top-1 (CoCa 91.0% fine-tuned, 2022) — diminishing returns for exploding cost.
- **$ / energy (frontier AI broadly — LLM/multimodal, NOT pure vision; label as such):** GPT-4 ≈ **$78M** compute, Gemini Ultra ≈ **$191M** (Stanford AI Index 2025); **GPT-3 = 1,287 MWh / ~552 tCO₂e** (Patterson 2021 — the canonical single-run energy figure); GPT-4 ≈ 5,184 tCO₂e; Llama 3.1 ≈ 39.3M H100-hrs / ~30 GWh. AI Index projects >$1B runs by 2027.
- **Honest framing:** clean $/MWh numbers are LLM/multimodal; vendors don't disclose per-run cost for ViT-22B-class vision. The vision-specific pressure = the labelled-data + pretraining-compute treadmill (142M→1.7B images in two years) against a ~91% accuracy ceiling.

### 2. Vision Transformers, 2025-26
- **ViT** (Dosovitskiy et al., 22 Oct 2020, arXiv:2010.11929): image → **16×16 patches** as tokens + a standard Transformer, no convolutions; matches/beats CNNs "with substantially fewer resources" when pretrained at scale.
- 2025-26 frontier = **scale + self-supervision + foundation models**, not raw ImageNet %: **SAM 2** (Meta, Jul 2024, 6× more accurate than SAM 1, SA-V = 35.5M masks); **DINOv3** label-free frozen features. CNNs (ConvNeXt V2, EfficientNetV2) still win at limited compute/data.

### 3. Industry quantum-CV — real named work (all hybrid, small/downscaled, no proven advantage)
- **Medical:** IBM hybrid quantum-classical **graph NN for tumour classification in digital pathology** (IEEE QCE 2024, "at par" with classical GNN); **HQCNN on PathMNIST** (colorectal histopathology) **93.40% acc / 99.59% AUC** (arXiv:2509.14277, Sep 2025); MedMNIST inference on **real 127-qubit IBM hardware** (arXiv:2502.13056, Feb 2025).
- **Earth observation:** **ESA Φ-lab QC4EO** program (first quantum-enhanced ViTs for EO); **EuroSAT hybrid QCNN** "outperformed classical counterparts" (Sebastianelli/Le Saux, arXiv:2109.09484); **hybrid quantum satellite classification 83%→87%** vs ResNet50 on IBM processors, "consistent 2-3% gains" (arXiv:2602.18350, Feb 2026); neural quantum kernels up to 8 qubits (arXiv:2409.20356).
- **Manufacturing:** **Multiverse Computing × Ikerlan** — casting-defect detection on **2,727 X-ray images** of auto parts, QSVM + QBoost on NISQ (arXiv:2208.04988).
- **Autonomous driving:** **Honda Scenes** on **72 qubits** (Quantinuum H-2 + IBM Heron), **>90% test accuracy** — "largest quantum image-classification experiment to date" (arXiv:2504.10595, Apr 2025).
- **Companies:** Terra Quantum (HQNN-Parallel **99.21% MNIST, 8× fewer params**, simulation-scale, arXiv:2304.09224), Multiverse, IBM, **NVIDIA CUDA-Q** (QPU-agnostic hybrid QML platform, GPU-accelerated).
- **Honest framing:** active, credibly-funded exploration (ESA, IBM, Multiverse, Terra Quantum, NVIDIA) — not production, not proven advantage; "wins" are 2-3% or at-par, often in simulation.

### 4. India — CV + quantum
- **NQM:** ₹6,003.65 cr (~$730M+), approved 19 Apr 2023, healthcare diagnostics named as an application area.
- **India's real strength = the imaging-data fuel, not quantum-CV today:** **NISAR** (NASA-ISRO SAR) launched **30 Jul 2025**, **~80 TB/day**, **~140 PB over the 3-yr mission** (more than any current NASA EO mission; EOSDIS archive ~116 PB Feb 2024); **ISRO/NRSC Bhoonidhi** = data from 47 satellites since 1986; **SVAMITVA** drone-mapped **~238,000 villages** by 31 Mar 2023; healthcare imaging — India has **~15,000 radiologists for 1.4B people**, AI-in-medical-diagnostics market **$12.87M (2024) → $44.87M (2030)** (CAGR 23.1%); Qure.ai, Niramai, Predible domestic leaders.
- **Honest framing:** India-specific quantum-CV pilots are **thin/absent**; the credible India story is huge + growing imaging data + strong ML talent + funded NQM — positioned to contribute, not running quantum-CV today. (⚠ Do NOT cite the "ISRO 28 PB archive" figure — it traces to an AI-generated wiki; use NISAR/EOSDIS instead.)

### 5. Quantum image-processing milestones on real hardware, 2024-26
- Largest to date: **Honda Scenes, 72 qubits, >90%** (Apr 2025). MedMNIST on **127-qubit IBM** (Feb 2025). Satellite **83%→87%** on IBM (Feb 2026). The 2024-26 shift is **hardware scale** (72-127 qubits, real error mitigation), **not** accuracy — competitive accuracy on hard full-resolution CV is not yet demonstrated.

**Global caveat for the whole deck: no published quantum-CV result demonstrates advantage over classical CV.** Every improvement is small, hybrid, on reduced-scale data. Frame quantum CV as early-stage exploration with credible institutional backing + India-relevant data abundance — never as solved or winning.
