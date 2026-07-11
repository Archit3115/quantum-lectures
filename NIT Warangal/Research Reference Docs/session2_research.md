# Session 2 — Classical & Quantum-Enhanced Computer Vision
### Research & speaker reference · QML-2026 FDP · 11 July 2026, 14:30–16:30

**Audience:** professors, doctorates, university/college teachers (mixed background). **Design principle:** first principles, bottom-up, intuition before math. **Runtime:** 120 min = ~15 min national open + ~85 min technical + ~10 min demo pointer + ~10 min close/Q&A.

---

## PART A — First principles: what *is* an image to a computer?

### A1. An image is a grid of numbers
A greyscale image is a matrix of pixel intensities (0 = black … 255 = white). A colour image is three such matrices (R, G, B). A 28×28 MNIST digit = 784 numbers. A 1-megapixel colour photo = 3 million numbers.

**Intuition anchor:** "The computer never sees a cat. It sees a spreadsheet of brightness values. Computer vision is the art of turning that spreadsheet back into meaning — *edge, texture, shape, object, scene.*"

### A2. Why raw pixels are a terrible representation
- **High dimensional:** 784 (tiny) to millions (real).
- **No built-in notion of locality:** pixel (0,0) and (0,1) are neighbours in the image but just two entries in a flat vector.
- **Not translation invariant:** shift the cat two pixels right and every number changes, though it's the same cat.

Computer vision is fundamentally about learning **good representations** — features that are local, hierarchical, and invariant. That single idea drives everything from hand-crafted filters to CNNs to quantum encodings.

---

## PART B — Classical computer vision, bottom-up

### B1. The pre-deep-learning era (hand-crafted features)
- **Convolution with a kernel:** slide a small matrix (e.g. 3×3) over the image; at each position compute a weighted sum. Different kernels detect different things — a **Sobel** kernel finds vertical edges, a blur kernel averages. *This "slide-a-small-window-and-combine" operation is the atom of all of vision — remember it, because the quantum method replaces exactly this atom.*
- **Classic descriptors:** SIFT, HOG, Haar features — clever hand-designed filters. Powerful but brittle; a human had to invent each feature.

### B2. The CNN revolution (features that learn themselves)
**AlexNet (2012)** halved the ImageNet error rate and started the deep-learning era. The key idea: **don't hand-design the kernels — learn them from data.**

**Anatomy of a CNN (build it on stage layer by layer):**
1. **Convolutional layer:** many *learnable* kernels slide over the image producing **feature maps.** Early layers learn edges; middle layers learn textures/parts; deep layers learn objects. **Hierarchy of representation** — the central miracle.
2. **Non-linearity (ReLU):** keeps positive responses, zeros the rest; lets the network model non-linear patterns.
3. **Pooling (downsampling):** take the max/average over a small window — shrinks the map and buys **translation invariance** (the cat can move a little).
4. **Repeat** conv→ReLU→pool, going deeper and more abstract.
5. **Fully-connected head + softmax:** flatten the final features and classify.
6. **Training:** backpropagation + gradient descent on a labelled set adjusts every kernel to reduce a loss.

**Three structural priors that make CNNs work** (worth a slide — they recur in the quantum story):
- **Local connectivity** (a pixel relates to its neighbours),
- **Weight sharing** (the same edge-detector is useful everywhere → far fewer parameters),
- **Hierarchy** (simple features compose into complex ones).

### B3. Where classical CV is today (context)
- **Beyond CNNs:** Vision Transformers (ViT, 2020) treat an image as patches and use attention; strong at scale.
- **The costs:** state-of-the-art vision models are enormous (compute, energy, labelled data). Training a frontier model costs millions and megawatt-hours. **This is the pressure point quantum-enhanced methods aim at — richer features from fewer parameters, or feature spaces classical nets can't cheaply reach.**

---

## PART C — Just enough quantum for vision (first principles)

*(If you gave Session 1, recap fast; if not, this is the standalone quantum primer.)*

### C1. Qubit, superposition, entanglement in one breath
- **Qubit:** |ψ⟩ = α|0⟩ + β|1⟩, |α|²+|β|²=1 — a continuous direction, not a bit.
- **n qubits → 2ⁿ amplitudes** — an exponentially large state space (the resource).
- **Entanglement:** qubits can be correlated so the whole is *not* described by its parts — a correlation structure with no classical analogue. For vision, entangling gates let a quantum filter mix pixel information in ways a linear classical filter cannot.
- **Measurement collapses** the state to classical bits — so we design circuits whose *measured expectation values* are the useful features.

### C2. The real question: how do you feed an image to a quantum computer?
**Data encoding is 80% of quantum ML for vision.** Three schemes (put all three on one comparison slide):

| Encoding | Idea | Qubits for N numbers | Trade-off |
|---|---|---|---|
| **Basis** | classical bitstring → computational basis state | N bits → N qubits | wasteful; rarely used |
| **Angle** | each feature → a rotation angle on a qubit (Rᵧ(xᵢ)) | N features → N qubits | simple, NISQ-friendly, shallow; used in quanvolution |
| **Amplitude** | features → amplitudes of the state vector | N features → ⌈log₂N⌉ qubits | exponential compression; expensive to prepare (QRAM) |

**Speaker line:** "Angle encoding is how we get real images onto real hardware today — one small patch of pixels becomes a few rotation angles. Amplitude encoding is the exponential dream, waiting on hardware."

### C3. The quantum convolution — "quanvolution"
**The single most important idea in Session 2.** (Henderson et al., 2019, *Quanvolutional Neural Networks*.)

Replace B1's classical convolution atom with a quantum one:
1. Slide a small window (e.g. 2×2) over the image — **exactly like classical convolution.**
2. **Encode** those 4 pixels as rotation angles on 4 qubits (angle encoding).
3. Apply a **random (or trainable) quantum circuit** — entangling gates mix the pixel information in a high-dimensional Hilbert space.
4. **Measure** each qubit → a set of expectation values.
5. Those measured numbers become **new feature-map channels**, stacked like classical conv output.
6. Feed the resulting feature maps into an ordinary classical CNN/dense network for classification.

**Why it can help (the honest claim):** the quantum circuit produces a **non-linear, high-dimensional transformation** of each patch that would be expensive to compute classically. It acts as a fixed (or trainable) *feature extractor* — a richer front-end. Henderson et al. reported modestly higher accuracy and faster convergence vs a purely classical baseline on MNIST in some settings. **It is a hybrid: quantum front-end, classical back-end.** That hybridity is the practical pattern for *all* near-term quantum vision.

### C4. Quantum CNNs (QCNN) — the fully-quantum cousin
Cong, Choi & Lukin (2019): a **QCNN** mirrors the CNN structure natively —
- **Quantum convolution** = the same two-qubit unitary applied across neighbouring qubits (weight sharing!),
- **Quantum pooling** = measure some qubits and condition rotations on the outcome (dimensionality reduction),
- repeat until few qubits remain, then measure to classify.

**Beautiful property:** a QCNN has only **O(log n)** parameters, is trainable, and (unlike deep generic variational circuits) is relatively **resistant to barren plateaus.** Native use cases: classifying **quantum states / phases of matter** — where the "image" is quantum data and there's no classical shortcut. For classical images it needs encoding (C2) first.

### C5. The hybrid pipeline (the pattern to remember)
> classical image → **[encode]** → quantum layer (quanvolution / QCNN) → **[measure]** → classical CNN head → label

Every practical near-term quantum vision system is this sandwich. The quantum slice buys a feature space; the classical slices do the heavy lifting of loading and decision.

---

## PART D — Reality check (slide it; earns credibility)

- **No demonstrated advantage on natural images yet.** On MNIST/CIFAR, well-tuned classical CNNs still win on accuracy-per-effort. Quanvolution's reported gains are modest and setting-dependent.
- **Encoding cost can eat the speedup** — loading a megapixel image is the same QRAM bottleneck as Session 1.
- **NISQ noise + shot noise** — expectation values need many measurements; today's qubits are few and noisy. Demos run in *simulation* or on tiny patches.
- **Where the promise is genuinely differentiated:**
  - **quantum-native data** (states from sensors, chemistry, physics experiments) — QCNN classifies phases with no classical encoding needed;
  - **structured/scientific imaging** where a quantum kernel is provably hard to simulate;
  - **feature richness from few parameters** (O(log n)) — attractive for data-scarce scientific domains.
- **Barren plateaus** limit naive deep variational vision circuits; QCNN's structure mitigates this.

**Speaker framing:** "Quantum-enhanced vision today is not going to beat a ResNet on your webcam. Its real target is (1) scientific/quantum data where classical nets have no encoding, and (2) rich features from tiny, trainable circuits. Teach it as the *front-end feature extractor of the future*, running as a hybrid with the classical vision you already know."

---

## PART E — Board-ready math sketches (for slides)
- Convolution: (I∗K)(i,j) = Σₘ Σₙ I(i+m, j+n)·K(m,n)
- Angle encoding: |x⟩ = ⊗ᵢ Rᵧ(xᵢ)|0⟩
- Amplitude encoding: |x⟩ = (1/‖x‖) Σᵢ xᵢ|i⟩, needs ⌈log₂N⌉ qubits
- Quanvolution: patch p → measure U(p)|0⟩ → channels
- QCNN parameter count: O(log n)

---

## PART F — Suggested slide sequence (Session 2)
1. Shared national open (context module) — 15 min
2. What is an image to a computer? (spreadsheet-of-brightness)
3. Why raw pixels fail → representation learning
4. Classical convolution atom (slide-a-window)
5. CNN anatomy (conv/ReLU/pool/FC), the 3 priors
6. Where classical CV is (ViT, and the compute/energy cost)
7. Quantum primer (qubit/superposition/entanglement/measurement)
8. **Encoding an image** — basis vs angle vs amplitude (the comparison slide)
9. **Quanvolution** (the hero slide) — replace the atom
10. QCNN (native, O(log n), phases of matter)
11. The hybrid sandwich pattern
12. Reality check / where the advantage is real
13. Live demo pointer (notebook)
14. Industry + India impact (context module)
15. Shared close + Q&A

---

## Key references
- Henderson et al., *Quanvolutional Neural Networks* (2019).
- Cong, Choi, Lukin, *Quantum Convolutional Neural Networks*, Nature Physics (2019).
- Havlíček et al., *Supervised learning with quantum-enhanced feature spaces*, Nature (2019) — encoding/feature maps.
- Schuld, Bocharov, Svore, Wiebe, *Circuit-centric quantum classifiers*, PRA (2020).
- Krizhevsky, Sutskever, Hinton, *ImageNet Classification with Deep CNNs* (AlexNet, 2012).
- Dosovitskiy et al., *An Image is Worth 16×16 Words* (ViT, 2020).
- Cerezo et al., *Variational quantum algorithms*, Nat. Rev. Phys. (2021) — barren plateaus.
- PennyLane tutorials — *Quanvolutional Neural Networks*, *Quantum kernels*.
