# Speaker's Own Work — how to weave Archit's papers into both sessions

**Google Scholar:** https://scholar.google.com/citations?user=NbPUdWMAAAAJ&hl=en
*(record for bio slide + references; use as the "my own research" anchor)*

These two published papers let Archit say "this is not abstract — I have built and run these things." Each maps onto one session as a **credibility + continuity slide** placed right before the "reality check."

---

## Paper A → **Session 1** (Clustering / QML — the optimization & framework thread)

**Citation:** C. H. Renumadhavi, **Archit Srivastava**, Ashutosh Kumar Singh, Anushka Mittal, *"Quantum Finance — An Overview,"* EasyChair Preprint No. 6071 (2021). Dept. of Electronics & Instrumentation Engineering, **RV College of Engineering, Bengaluru.**

**What it did (facts to quote):**
- Mapped a **Mean-Variance Portfolio Optimization** problem (4 assets) to a **QUBO → Ising Hamiltonian** (constraint folded in as a penalty term), then solved it with a **Variational Quantum Eigensolver (VQE)**.
- **Implemented the same problem in BOTH Qiskit (IBM) and PennyLane (Xanadu)** and compared — directly relevant to an FDP where faculty must choose a teaching framework.
- **Qiskit result:** optimal asset selection **[0 1 0 1]** with probability **0.9434**.
- **PennyLane result:** VQE converged to optimal state **[1 0 1]** (3-qubit ansatz: RX rotations + CNOT entanglers, COBYLA/gradient optimizer).

**Why it belongs in Session 1 (talking point):**
- Portfolio optimization *is* an unsupervised structure-finding problem in disguise — grouping/selecting assets by a covariance (similarity) matrix. It shares the exact machinery of the session: **encode data → build a Hamiltonian/kernel → let a variational circuit find structure.**
- The **VQE ansatz** (parameterised RX + CNOT circuit) is the *same species* as the **quantum feature map** used for quantum-kernel clustering in the notebook — one slide can show "the circuit you optimise for VQE is the circuit you evaluate for a quantum kernel."
- **Qiskit vs PennyLane** is a natural aside: "In my 2021 work we ran it on both; today's notebook is PennyLane because it's the cleanest for teaching kernels and quanvolution. Both reach the same physics."

**Suggested placement:** slide between "Quantum kernel clustering" and "Reality check" — titled *"From my own work: variational quantum optimization, two frameworks."*

---

## Paper B → **Session 2** (Computer Vision — classical CNN + the quantum-vision horizon)

**Citation:** Ananya Ananth Rao, [**Archit Srivastava** et al.], *"Autism Spectrum Disorder Therapy: Analysis of Artificial Intelligence integrated Robotic Approach,"* **J. Phys.: Conf. Ser. 2161 (2022) 012038**, IOP Publishing (AICECS 2021). DOI 10.1088/1742-6596/2161/1/012038.

**What it did (facts to quote):**
- Built a real **computer-vision pipeline**: webcam feed → **Viola-Jones face detection + MOSSE tracker** → **eye-region segmentation** (Columbia Gaze dataset, 5,880 images, 56 subjects) → **CNN eye-contact classifier**.
- **CNN architecture:** final model **5 convolutional layers**, each with **max-pooling + batch-normalisation**, then dropout, flatten, dense head; **ReLU** activations, **sigmoid** output; categorical/binary cross-entropy; **Adam** optimizer. A textbook CNN — perfect for the Session 2 "CNN anatomy" build.
- Honest result reported: overfitting past 600 epochs dropped accuracy to ~68% — a candid, teachable engineering lesson.
- **Section 5 — Quantum Visual Tracking & Quantum Image Processing (the forward-looking part):** argues N classical bits encode in **log₂N qubits**; notes quantum simulation cost grows exponentially with qubits; implemented a **Quantum Fourier Transform (QFT)** — "the most crucial step of Quantum Visual Tracking" — as the runnable proxy for full QVT.
- **QFT run on real IBM Quantum hardware (Stockholm):** 3-qubit input, Hilbert space of 8; input state **|5⟩** returned the **010** state with probability **0.688**, matching theory; other outcomes attributed to gate/qubit error growing with circuit depth — a real NISQ-noise observation.

**Why it belongs in Session 2 (talking point):**
- Paper B *is* the arc of the whole session in one artifact: **classical CNN vision → the quantum-vision frontier.** "I built the classical CNN; then I looked at what quantum offers for vision — and hit exactly the encoding and NISQ-noise walls we discussed."
- The **log₂N encoding** claim in the paper is the **amplitude encoding** slide (Part C2). Use it verbatim.
- The **QFT-on-hardware noise result** (0.688 vs ideal, error grows with depth) is a genuine, first-hand version of the Session 2 "Reality check" — far more persuasive than a citation to someone else's experiment.
- **Quantum Visual Tracking** as future work is the perfect closing horizon: "the natural next step past quanvolution — tracking objects in superposition — is where my own research points."

**Suggested placement:** two touches — (1) the **CNN anatomy** slide can note "this is the architecture from my 2022 paper"; (2) a dedicated slide before the Session 2 "Reality check" titled *"From my own work: classical CNN → Quantum Visual Tracking, and the NISQ wall I measured."*

---

## One-line framing for the bio slide (both sessions)
"Co-author of published work on **quantum finance / variational optimization** (Qiskit vs PennyLane) and on **AI computer vision with a quantum-visual-tracking outlook** — so today's material is drawn from methods I've actually built and run on real quantum hardware." (Scholar: NbPUdWMAAAAJ)
