# Session 2 — Speaker Notes
## Classical & Quantum-Enhanced Computer Vision
**QML-2026 FDP · E&ICT Academy NIT Warangal × NIT Raipur · 11 July 2026, 02:30–04:30 PM**
**Speaker: Archit Srivastava**

> **Format:** 19 slides for a 120-minute slot. Budget ~4–5 min/slide with ~20 min for the live notebook and Q&A. Same shared open/close as Session 1 — if the audience overlaps with the morning, move faster through slides 2–6 and say so ("you saw the national context this morning; the headline is the 840k talent gap").

---

### Deck timing map
| Block | Slides | Minutes | Purpose |
|---|---|---|---|
| Open + India context | 1–6 (title, about, roadmap, why-now, market, NQM) | ~22 | Hook + national stakes (compress if repeat audience) |
| What an image is | 7 (grid of numbers) | ~7 | First-principles framing |
| Classical CV | 8–10 (convolution, CNN, costs) | ~20 | Anchor the whole field |
| Quantum turn | 11–14 (encoding, quanvolution, demo, QCNN) | ~32 | Core, bottom-up, with runnable proof |
| Honest picture | 15–16 (own work, reality) | ~18 | Credibility + caveats |
| Close | 17–19 (Viksit, call-to-action, thanks) | ~15 | National vision, faculty action |

---

## Slide-by-slide

**1 · Title — "teaching machines to see."**
"This afternoon we go from a grid of numbers to a quantum feature map — and I'll show you the exact point where a quantum circuit slots into a pipeline you already teach." Promise: convolution → quanvolution, all runnable in simulation.

**2 · About me.** Same as morning; 30 seconds. Emphasise the Session-2-relevant credential: I co-authored a paper with a real 5-layer CNN eye-contact pipeline *and* a quantum-visual-tracking section run on IBM hardware — so today's arc is literally my own research path.

**3 · Roadmap.** *what an image is → the CNN → the quantum turn → the honest picture.* Same discipline: one quantum idea at a time, always anchored on classical vision.

**4–6 · Why now / Market / NQM (shared).** Identical to Session 1. If repeat audience, compress to 5 min total and foreground the talent gap (840k jobs by 2035 vs ~5,000 qualified) and India's hardware momentum (Amaravati Quantum Valley, QpiAI Kaveri 64-qubit).

**7 · What is an image? — "the computer never sees a cat."**
The keystone. A greyscale image is a matrix of intensities (0–255); colour is three such matrices. A 28×28 digit = 784 numbers; a 1-MP colour photo = 3 million. Why raw pixels are a *terrible* representation: high-dimensional, no built-in locality (neighbouring pixels are just two flat entries), not translation-invariant (shift the cat 2px and every number changes). "Vision is the art of learning good representations — local, hierarchical, invariant."

**8 · The convolution atom.**
Slide a small kernel (e.g. 3×3) over the image; at each stop compute a weighted sum. Different kernels detect different things — Sobel finds edges, a blur kernel averages. (I∗K)(i,j) = Σ I(i+m,j+n)K(m,n). **Plant the flag:** "this slide-a-window-and-combine operation is the atom of all vision — remember it, because the quantum method replaces exactly this atom."

**9 · The CNN.**
AlexNet (2012) halved ImageNet error and started the deep-learning era. Key idea: don't hand-design kernels — *learn* them. Anatomy: conv (learnable kernels → feature maps) → ReLU (non-linearity) → pooling (shrink + translation invariance) → FC + softmax (classify), trained end-to-end by backprop. **The three priors** (say these clearly, they recur in the quantum story): local connectivity, weight sharing (one edge detector, reused everywhere → far fewer params), hierarchy (simple features compose into complex).

**10 · Where classical CV strains.**
Beyond CNNs: Vision Transformers (2020) treat an image as patches + attention — strong at scale, hungrier still. The bill: frontier models cost millions of dollars and megawatt-hours, on oceans of labelled data. The opening for quantum: richer features from fewer parameters, or feature spaces classical nets can't cheaply reach.

**11 · Image encoding — "the real question."**
Data encoding is ~80% of quantum ML for vision. Three schemes as a qubits-vs-cost trade-off: **Basis** (N bits → N qubits, wasteful), **Angle** (N features → N qubits, each feature a rotation Rᵧ(xᵢ); shallow + NISQ-friendly — the star, how real images reach real hardware today), **Amplitude** (N features → ⌈log₂N⌉ qubits, exponential compression but expensive to prepare — QRAM). "Angle encoding turns a small patch into a few rotation angles — that's what makes quanvolution run today; amplitude is the exponential dream, waiting on hardware."

**12 · Quanvolution (hero idea).**
Henderson et al., 2019. Recipe: slide a 2×2 window (exactly like classical convolution) → angle-encode the 4 pixels on 4 qubits → apply a random/trainable entangling circuit (mixes pixels in a 16-D Hilbert space) → measure each qubit → new feature-map channels → stack → feed a classical CNN head. **This is the pattern for all near-term quantum vision: quantum front-end, classical back-end.** Show the real PennyLane quanvolution circuit on the right.

**13 · Live demo.** *(Switch to `qml_vision_demo.ipynb` — budget ~10 min.)*
One 2×2 quantum circuit turns each digit patch into 4 feature-map channels. Show the feature-map grid: three digits × (input + 4 quantum channels) — each channel is a different learned-by-physics view. **Honest result up front:** on `load_digits`, a simple classifier on raw pixels gets **0.978** accuracy; the same classifier on the *untrained, random* quanvolution features gets **0.856**. The point is *not* "quantum wins" — it's that an untrained 4-qubit circuit already preserved ~86% of the signal, and the feature maps are structured and meaningful. Preprocessing was ~21 ms/image in simulation. This is the honest teaching frame: quanvolution is a feature extractor, and today's gains are modest and setting-dependent.

**14 · The QCNN (native cousin).**
Cong, Choi & Lukin (2019). Quantum convolution = the same two-qubit unitary applied across neighbouring qubits (weight sharing, natively). Quantum pooling = measure some qubits, condition rotations on the outcome (dimensionality reduction). Payoff: only O(log n) parameters, trainable, relatively resistant to barren plateaus. The *native* use case: classifying quantum states / phases of matter — where the "image" is quantum data and there's no classical shortcut. For classical images it still needs encoding first.

**15 · From my own work.**
J. Phys.: Conf. Ser. 2161 (2022) 012038. A real CV pipeline: face detection → eye segmentation → a 5-layer CNN (batch-norm, ReLU, dropout) for eye-contact detection (autism-therapy application, Columbia Gaze dataset). Then the quantum frontier: N classical bits encode in log₂N qubits (amplitude-encoding claim, first-hand), and we ran a **Quantum Fourier Transform on real IBM hardware** — the core step of Quantum Visual Tracking. The measured wall: input |5⟩ → measured 010 with probability **0.688**, matching theory, with error *growing as depth grows*. "This is a first-hand NISQ-noise result — and Quantum Visual Tracking is the natural step past quanvolution, which is where my research points."

**16 · Reality check.**
Say it plainly: on MNIST/CIFAR, tuned classical CNNs still win — quanvolution's gains are modest and setting-dependent. Encoding cost can eat the speedup (a megapixel image hits the same QRAM wall). NISQ + shot noise → expectation values need many measurements; demos run in simulation or on tiny patches. Where the promise is genuine: quantum-native data (QCNN classifies phases with no encoding), structured/scientific imaging where a quantum kernel is hard to simulate, feature richness from O(log n) params for data-scarce scientific domains. "Teach it as the front-end feature extractor of the future — running hybrid with the vision you already know."

**17 · Viksit Bharat 2047 (shared).** Same as Session 1. For a CV audience, add: India's strengths in IT services + a huge imaging/healthcare/agriculture data footprint make hybrid quantum-classical vision a natural applied bet — if the talent exists.

**18 · Call to action (shared).**
"Convolution to quanvolution is a first-principles story — the demo runs in simulation on a laptop." Asks: add a quanvolution notebook to a deep-learning or CV elective; frame quantum vision honestly (front-end feature extractor, not a magic accuracy boost); route strong students to NQM hubs and quantum-CV research.

**19 · Thank you.** Contact + Google Scholar (NbPUdWMAAAAJ) + AiQyaM. Offer both notebooks and the decks; invite collaboration on quantum visual tracking.

---

## Anticipated questions (keep these ready)
- **"Does quanvolution beat a CNN?"** Not on standard benchmarks today. Its value is as a *feature extractor* and on quantum-native/structured data. I show the honest 0.978 vs 0.856 number precisely so no one leaves overselling it.
- **"Why measure PauliZ on each qubit?"** It gives a real-valued expectation per qubit — a natural, differentiable scalar to use as a feature-map channel. You can measure other observables for more channels.
- **"Random vs trainable quanvolution circuit?"** The demo uses a *random* circuit to show the raw representational power with zero training. Making the circuit trainable (parameters learned by backprop through the hybrid model) is the next step and can improve results.
- **"How does this connect to real hardware?"** Angle encoding + shallow circuits are exactly what runs on today's NISQ devices; my QFT-on-IBM-hardware result shows both that it works and that depth-driven error is the current wall.
- **"QCNN vs quanvolution — which should I teach?"** Quanvolution first (it's the gentlest bridge from classical convolution). QCNN once students are comfortable with parameterised circuits and want a fully-quantum model for quantum data.
- **"Can I run the demo offline?"** Yes — PennyLane `default.qubit` simulator, `scikit-learn` digits, CPU only.
