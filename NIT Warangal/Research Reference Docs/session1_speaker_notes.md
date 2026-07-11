# Session 1 — Speaker Notes
## Quantum Unsupervised Learning (Clustering)
**QML-2026 FDP · E&ICT Academy NIT Warangal × NIT Raipur · 11 July 2026, 09:30–11:30 AM**
**Speaker: Archit Srivastava**

> **Format:** 21 slides for a 120-minute slot. Budget ~4–5 min/slide with ~20 min for the live notebook and Q&A buffer. The audience is faculty — pitch to "smart peers in adjacent fields," not undergraduates. Every quantum idea is introduced from a classical anchor they already teach.

---

### Deck timing map
| Block | Slides | Minutes | Purpose |
|---|---|---|---|
| Open + India context | 1–6 (title, about, roadmap, why-now, market, NQM) | ~25 | Hook, credibility, national stakes |
| The idea | 7–8 (unsupervised, three ingredients) | ~12 | First-principles framing |
| Classical tools | 9–11 (k-means, landscape, cost) | ~18 | Anchor + set up the quantum "why" |
| Quantum turn | 12–15 (qubit, encoding, swap test, kernel) | ~28 | Core physics, bottom-up |
| Honest picture | 16–18 (demo, own work, reality) | ~22 | Runnable proof + caveats |
| Close | 19–21 (Viksit, call-to-action, thanks) | ~15 | National vision, faculty action |

---

## Slide-by-slide

**1 · Title — "clustering, reimagined."**
Open warm. "Good morning. Over the next two hours we'll build quantum clustering from the ground up — no black boxes. If you can teach k-means, you'll leave able to teach the quantum version." Set expectations: two live notebooks, all runs on a laptop, nothing needs quantum hardware.

**2 · About me.**
30 seconds, not a CV recital. Land three things: (a) I build quantum systems in industry (o9, HPE PoCs), (b) I founded India's first quantum-hardware community (AiQyaM, 2020) and CIRQuIT at RVCE, (c) I've published on exactly today's topics — quantum finance (Session 1's circuits) and a CNN + quantum-visual-tracking paper (Session 2). Mention the Google Scholar profile is on the last slide.

**3 · Roadmap.**
The spine: *idea → classical tools → quantum turn → honest picture*. Tell them explicitly: "I will always start from something you already know and add exactly one quantum idea at a time."

**4 · Why now (shared).**
2025 was the inflection year. Willow (105 qubits, Nature Dec 2024), D-Wave's 4400+ annealer, and Google's "Quantum Echoes" verifiable-advantage result (13,000× a classical supercomputer). The point for faculty: this is no longer a physics curiosity — it's a computational tool your students will be asked about in interviews next year.

**5 · Global market (shared).**
McKinsey QTM 2026: up to **$2.7T** of economic value by 2035; quantum-tech startup investment hit **$12.6B in 2025** (6.3× YoY). The talent line is the one that lands in a faculty room: **~840,000 quantum jobs needed by 2035 vs ~5,000 qualified people in 2025.** That gap is *their* mandate — this is why an FDP exists.

**6 · India's National Quantum Mission (shared).**
₹6,003.65 cr approved April 2023, horizon 2023–2031, staged 20-50 → 50-100 → 50-1000 physical qubits. Four thematic hubs: Computing (IISc Bengaluru), Communication (IIT Madras + C-DOT), Sensing (IIT Bombay), Materials (IIT Delhi); 152 researchers / 43 institutions / 17 states. Recent: QpiAI "Kaveri" 64-qubit (Nov 2025), Amaravati Quantum Valley with IBM Quantum System Two (Feb 2026), ~1000 km quantum comms. The message: "India is building the hardware; this room builds the people who use it."

**7 · What is unsupervised learning? — "sorting coins in the dark."**
The keystone intuition. Mixed coins on a table in the dark: you can't read denominations (no labels), but you feel size and weight (features) and sort into piles (clusters). Then the ML map: supervised = data + labels; unsupervised = data only. Hammer the practical fact: ~80% of real-world data is unlabelled, so clustering is often the *first* thing you do with a new dataset.

**8 · Three ingredients.**
Every clustering method = (1) a representation (object → vector in ℝᵈ), (2) a similarity (how we measure "alike"), (3) an objective (what makes a grouping good). **Plant the flag here:** "Quantum mostly changes ingredient 2 — the similarity — and how fast we compute it." This single sentence is the thesis of the whole session; repeat it.

**9 · k-means.**
Walk Lloyd's loop: init k centroids → assign each point to nearest → update centroid to the mean → repeat. Objective J = within-cluster sum of squares. Pause on the assign step: "this is n×k distance computations — remember that line, it's where quantum will push." Then the blind spot: "nearest centroid" is a straight-line idea, so k-means fails on non-convex shapes (interleaved crescents, concentric rings). Foreshadow the demo.

**10 · The classical landscape.**
Quick tour: hierarchical (dendrogram, no fixed k), DBSCAN (density, arbitrary shapes + outliers), GMM (soft, EM). Then spend real time on **spectral clustering** — build a similarity graph, take the top eigenvectors of its Laplacian, k-means in that space. It handles non-convex data *and* its heavy step is linear algebra on a similarity matrix. "A quantum computer is a native linear-algebra machine — hold that thought."

**11 · Where the cost lives.**
O(d) per distance → O(n·k·d) per k-means iteration → O(n²d) to build a kernel matrix → O(n³) to eigendecompose it. Everything expensive is *computing similarities between many high-dimensional vectors* and *linear algebra on n×n matrices*. That's precisely the corner quantum targets. "Now we've earned the quantum part."

**12 · The qubit.**
|ψ⟩ = α|0⟩ + β|1⟩, |α|²+|β|²=1. Amplitudes are complex; |α|² is the probability of measuring 0. Superposition = genuinely both before measurement. Bloch sphere: a qubit is a continuous *direction*, not one bit. Then n qubits → 2ⁿ amplitudes; 50 qubits ≈ 10¹⁵ amplitudes evolving together — the resource. **Be honest immediately:** measurement collapses to n classical bits; you can't read all 2ⁿ. The art is *interference* — arrange it so the useful answer is what you measure. This honesty buys credibility with a room full of scientists.

**13 · Encoding + overlap.**
Two primitives. Amplitude encoding: load vector x into amplitudes; a d-dim vector needs ⌈log₂ d⌉ qubits (exponential compression). Overlap = similarity: the natural quantity between states is ⟨a|b⟩, and ‖a−b‖² = 2 − 2⟨a|b⟩ — inner products *are* similarities. Third: a small circuit turns an overlap into a measurable probability. "That circuit is the swap test — next slide."

**14 · The swap test (hero primitive).**
Walk it in words: prepare |a⟩,|b⟩ + ancilla |0⟩ → Hadamard ancilla → controlled-SWAP → Hadamard ancilla → measure. Result: **P(ancilla=0) = ½ + ½|⟨a|b⟩|²**. Similar → near 1; orthogonal → ½. The punchline: this measures the similarity of two *d-dimensional* states with a *constant-size* circuit. Show the real PennyLane circuit on the right. Note this is the seed of Lloyd–Mohseni–Rebentrost quantum k-means (2013).

**15 · The quantum kernel (the NISQ-friendly route).**
Reframe: don't speed up k-means — *change the similarity* to one expensive to fake classically. A quantum feature map φ encodes each point via a parameterised circuit; K(xᵢ,xⱼ) = |⟨φ(xᵢ)|φ(xⱼ)⟩|². Feed K into any kernel method — spectral clustering, kernel k-means. The bet: the feature map reaches a Hilbert space expensive to simulate, so hidden structure becomes separable. Shallow, NISQ-friendly, runs today. **This closes the loop:** spectral clustering (handles non-convex) + quantum kernel (richer similarity) = exactly what the notebook does next.

**16 · Live demo.** *(Switch to `qml_clustering_demo.ipynb` — budget ~10 min.)*
Two interleaved moons. Classical k-means gets ARI **0.43** — it slices straight through the crescents. Quantum-kernel spectral clustering gets ARI **0.69** — it recovers them. The kernel: a 2-qubit data-reuploading feature map (SCALE=2.5, REPS=2), kNN-sparsified (k=6), fed to SpectralClustering. Emphasise: **2 qubits, runs on this laptop, no hardware.** If time: open the kernel-matrix heatmap and show the block structure the quantum kernel exposes. **Teaching honesty:** this is a curated example where the geometry favours the quantum kernel — say so.

**17 · From my own work.**
Tie to *Quantum Finance — An Overview* (EasyChair 6071, 2021). Mapped mean-variance portfolio optimization → QUBO → Ising → solved with a VQE, implemented in **both Qiskit and PennyLane** (the framework choice this room faces). Qiskit: optimal selection [0 1 0 1] at prob 0.94; PennyLane VQE → [1 0 1]. The bridge: the VQE ansatz (RX/RY + CNOT) is the *same species of circuit* as today's quantum feature map. "There we optimised it to minimise a Hamiltonian; here we evaluate it to measure similarity. Same physics, two jobs."

**18 · Reality check.**
Say the caveats out loud — faculty respect this. (1) Data loading is the bottleneck; the exponential k-means speedup assumes QRAM, which doesn't exist at scale. (2) Dequantization (Ewin Tang, 2018+) matched several "exponential" QML speedups classically under the same assumptions. (3) NISQ noise → keep circuits shallow (hence shallow kernels). (4) Barren plateaus → deep variational maps can have vanishing gradients. Where the advantage is *genuine*: quantum-native/structured data, small-but-hard kernels a classical machine can't simulate, and as a *feature generator* feeding the classical methods they already teach. "Not 'k-means but faster on your CSV' — a new kind of similarity you can run now."

**19 · Viksit Bharat 2047 (shared).**
Connect to the national frame: quantum + AI as pillars of a developed India by 2047. The NQM is the infrastructure; the faculty in this room are the multiplier — each trains hundreds of students. Frame quantum literacy as a sovereignty issue (secure comms, indigenous hardware, not renting foreign quantum cloud).

**20 · Call to action (shared).**
"Clustering, kernels and the swap test are teachable from first principles — no hardware required." Concrete asks: add one quantum-ML module to an existing ML course; use these notebooks (they run on any laptop); point strong students at the NQM hubs and QpiAI/BosonQ internships.

**21 · Thank you.**
Contact + Google Scholar (NbPUdWMAAAAJ) + the AiQyaM community. Invite them to bring students to the next cohort. Leave the meet link and offer to share both notebooks.

---

## Anticipated questions (keep these ready)
- **"Is there a proven exponential speedup for clustering?"** Not unconditionally. HHL-style speedups assume QRAM + well-conditioned matrices; dequantization narrowed many. The honest near-term value is the *quantum kernel* as a new similarity, not asymptotic speedup.
- **"Qiskit or PennyLane?"** Both are excellent; PennyLane is more autodiff/ML-native and hardware-agnostic, Qiskit has the deepest IBM-hardware tooling. My finance paper used both — I'd start students on PennyLane for QML.
- **"How many qubits do I need to do something useful?"** For teaching and kernel demos, 2–8 in simulation is plenty. For advantage on real data, the field isn't there yet — that's the honest answer.
- **"Why did the quantum kernel actually win on the moons?"** The feature map's geometry makes the two crescents more separable in Hilbert space; on a dataset that already suits k-means, it won't help. Always benchmark against a strong classical baseline.
- **"Can students run this without a GPU/quantum hardware?"** Yes — everything today runs in PennyLane's `default.qubit` simulator on a CPU.
