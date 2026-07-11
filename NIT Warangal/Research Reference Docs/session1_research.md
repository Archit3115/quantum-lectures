# Session 1 — Quantum Unsupervised Learning (Clustering)
### Research & speaker reference · QML-2026 FDP · 11 July 2026, 09:30–11:30

**Audience:** professors, doctorates, university/college teachers (mixed background — some ML, some physics, some neither). **Design principle:** start from first principles, build bottom-up, keep every abstraction anchored to an intuition before the math. **Runtime:** 120 min = ~15 min national open + ~85 min technical + ~10 min demo pointer + ~10 min close/Q&A.

---

## PART A — First principles: what is clustering, and why "unsupervised"?

### A1. The one-sentence definition
**Unsupervised learning finds structure in data that has no labels.** You are not told "this is a cat, that is a dog." You are handed a pile of points and asked: *which of these belong together?*

**Intuition anchor (use this on stage):** Imagine tipping a bag of mixed coins onto a table in the dark. You can't read the denominations, but you can feel size and weight. You sort them into piles by similarity. That sorting — with no labels, using only a notion of "how alike" — is clustering.

### A2. Where it sits in the ML map
- **Supervised:** data + labels → learn a mapping (classification, regression). "Here are 10,000 labelled tumours, predict the next one."
- **Unsupervised:** data only → discover structure (clustering, dimensionality reduction, density estimation). "Here are 10,000 tumours, *are there natural subtypes?*"
- **Why it matters:** labels are expensive, scarce, or impossible. ~80% of real-world data is unlabelled. Clustering is how you make first sense of a new dataset — customer segments, genomic subtypes, anomaly detection, image compression, document topics.

### A3. The three ingredients of any clustering method
1. **A representation** — each object as a vector of features (a point in ℝᵈ).
2. **A similarity / distance** — how we measure "alike" (Euclidean distance, cosine similarity, kernel).
3. **An objective / rule** — what makes a *good* grouping (minimise within-cluster spread; maximise between-cluster separation).

Everything that follows — classical *and* quantum — is a different choice of these three. **Quantum methods mostly change ingredient 2 (the similarity) and how fast we can compute it.** Hold that thought; it is the spine of the whole session.

---

## PART B — Classical clustering, the honest version

### B1. k-means — the workhorse
**Goal:** partition n points into k clusters, each represented by a *centroid* (mean point), minimising total squared distance from points to their centroid.

**Objective (inertia / within-cluster sum of squares):**
> J = Σ_clusters Σ_{x in cluster} ‖x − μ_cluster‖²

**Lloyd's algorithm (the loop):**
1. Initialise k centroids (randomly, or k-means++).
2. **Assign:** each point → nearest centroid. *(This is n×k distance computations — remember this line.)*
3. **Update:** each centroid → mean of its assigned points.
4. Repeat 2–3 until assignments stop changing.

**Strengths:** simple, fast, scales to millions of points. **Weaknesses:** must pick k in advance; assumes round, equal-size, linearly-separable blobs; sensitive to initialisation and outliers; **fails on non-convex shapes** (two interleaved crescents, concentric rings).

### B2. Beyond k-means (so faculty see the landscape)
- **Hierarchical / agglomerative:** build a tree (dendrogram) of merges; no need to fix k up front; O(n²)–O(n³).
- **DBSCAN:** density-based; finds arbitrary shapes and labels outliers; needs a density scale ε.
- **Gaussian Mixture Models (GMM):** soft, probabilistic clusters via Expectation-Maximisation.
- **Spectral clustering:** build a similarity graph, embed using the top eigenvectors of its Laplacian, then k-means in that space. **Handles non-convex clusters** — and its heavy step is *linear algebra on a similarity/kernel matrix.* **Flag this: it is the natural bridge to quantum**, because quantum computers are native linear-algebra machines.

### B3. The computational pressure point
The recurring cost in clustering is **computing distances / similarities between many high-dimensional vectors**, and **linear algebra on n×n similarity matrices** (spectral, kernel methods). For n points in d dimensions:
- one Euclidean distance = O(d)
- one k-means iteration = O(n·k·d)
- a kernel/similarity matrix = O(n²·d) to build, O(n³) to eigendecompose

**This is exactly the corner where quantum offers leverage** — distance/inner-product estimation and high-dimensional feature spaces. Now we earn the quantum part.

---

## PART C — Just enough quantum (first principles, no hand-waving)

### C1. The qubit — a coin that is every angle at once
A classical bit is 0 or 1. A **qubit** is a unit vector in a 2-D complex space:
> |ψ⟩ = α|0⟩ + β|1⟩,  with |α|² + |β|² = 1

- α, β are **amplitudes** (complex numbers). |α|² = probability of measuring 0.
- **Superposition:** before measurement the qubit genuinely holds a weighted combination of both.
- **Bloch sphere intuition:** picture the qubit state as a point on a globe. |0⟩ = north pole, |1⟩ = south pole, everything else = a direction. A single qubit carries a *continuous* direction, not one bit.

### C2. Why n qubits are powerful — 2ⁿ amplitudes
n qubits live in a space of **2ⁿ complex amplitudes**. 50 qubits → 2⁵⁰ ≈ 10¹⁵ amplitudes evolving *together*. This exponential state space is the resource. **But there is a catch (be honest):** measurement collapses the state and returns only n classical bits. You cannot read out all 2ⁿ amplitudes. The art of quantum algorithms is arranging **interference** so the useful answer is what you measure with high probability.

### C3. Three primitives you need for clustering
1. **Amplitude / state encoding** — load a classical vector **x** into the amplitudes of a quantum state |x⟩. A d-dimensional vector needs only ⌈log₂ d⌉ qubits. *This is the "exponential compression" that makes high-dimensional inner products cheap in principle.*
2. **Inner product ↔ overlap** — the natural quantity a quantum computer gives you between two states |a⟩, |b⟩ is their **overlap** ⟨a|b⟩. Inner products *are* similarities. This is the whole game.
3. **Interference + measurement** — a small circuit turns an overlap into a measurable probability.

### C4. The Swap Test — the heart of quantum clustering
**What it does:** estimates |⟨a|b⟩|² — the squared overlap (a similarity) between two quantum states — using one extra "ancilla" qubit.

**Circuit (say it in words on stage):**
1. Prepare states |a⟩ and |b⟩ on two registers; an ancilla in |0⟩.
2. Hadamard on the ancilla (put it in superposition).
3. **Controlled-SWAP:** the ancilla conditionally swaps the two registers.
4. Hadamard on the ancilla again; measure it.

**Result:**
> P(ancilla = 0) = ½ + ½·|⟨a|b⟩|²

So: **similar states → P₀ near 1; orthogonal states → P₀ = ½.** Run it many times, estimate P₀, invert the formula, and you have the similarity. From similarity you get **Euclidean distance** via ‖a−b‖² = 2 − 2·⟨a|b⟩ (for normalised vectors).

**Why faculty should care:** the swap test computes an overlap of two *d-dimensional* (⌈log d⌉-qubit) states with a **constant-size** circuit. The distance evaluation that costs O(d) classically can, in principle, be done on exponentially compressed representations — this is the seed of the Lloyd–Mohseni–Rebentrost **quantum k-means** speedup (O(log(nd)) per distance under strong assumptions).

### C5. Quantum k-means — assemble the pieces
Same Lloyd's loop as B1, but the **assign** step (the n×k distances) uses the swap test / quantum distance estimation on amplitude-encoded points and centroids. Under ideal data-loading (QRAM) the per-distance cost scales like **O(log(nd))** instead of O(nd) — an *exponential* improvement in the dimension/count, on paper.

### C6. Quantum kernel clustering — the NISQ-friendly route
Instead of speeding up k-means, **change the similarity to one that is hard classically.** A **quantum feature map** φ encodes each data point x into a quantum state |φ(x)⟩ via a parameterised circuit. The **quantum kernel** is the overlap:
> K(xᵢ, xⱼ) = |⟨φ(xᵢ)|φ(xⱼ)⟩|²

Feed this K into any kernel-based classical method — **spectral clustering, kernel k-means.** The bet: the quantum feature map reaches a **Hilbert space that is expensive to simulate classically**, so structure invisible to classical kernels becomes separable. This is the **near-term, runnable** approach — it's what the notebook demonstrates — and it connects straight back to B2's spectral clustering.

---

## PART D — Reality check (put this on a slide; faculty will trust you more)

- **Data loading is the bottleneck.** The exponential k-means speedup assumes QRAM to load classical data in superposition efficiently. Practical QRAM does not yet exist at scale. *State the assumption every time you claim a speedup.*
- **Dequantization (Ewin Tang, 2018→).** Several "exponential" QML speedups (recommendation systems, some clustering/PCA) were matched by classical algorithms once you allow the same sampling assumptions. **The honest advantage lives where the quantum feature map is genuinely hard to simulate.**
- **NISQ noise.** Today's devices are noisy and shallow. Quantum-kernel methods are attractive precisely because they are shallow and can tolerate some noise.
- **Where the near-term win is real:** structured/quantum-native data, small-but-hard kernels, and as a *feature generator* feeding classical clustering — not as a drop-in replacement for k-means on your laptop's CSV.
- **Barren plateaus:** deep variational feature maps can have vanishing gradients — keep circuits shallow / structured.

**Speaker framing:** "Quantum clustering is not 'k-means but faster on your data today.' It is (1) a rigorous *asymptotic* speedup waiting on hardware + QRAM, and (2) a *new kind of similarity* — the quantum kernel — that you can run on real hardware now and feed into the classical methods you already teach."

---

## PART E — Board-ready math sketches (for slides)

- Qubit: |ψ⟩ = α|0⟩ + β|1⟩, |α|²+|β|² = 1
- n-qubit state space: dimension 2ⁿ
- k-means objective: J = Σ_k Σ_{x∈C_k} ‖x − μ_k‖²
- Distance ↔ overlap (normalised): ‖a−b‖² = 2 − 2⟨a|b⟩
- Swap test: P(0) = ½ + ½|⟨a|b⟩|²
- Quantum kernel: K(xᵢ,xⱼ) = |⟨φ(xᵢ)|φ(xⱼ)⟩|²

---

## PART F — Suggested slide sequence (Session 1)
1. Shared national open (from india_quantum_context.md) — 15 min
2. What is unsupervised learning? (coins-in-the-dark) 
3. Clustering = representation + similarity + objective
4. Classical k-means (Lloyd's loop, the distance-count line)
5. The classical landscape + the non-convex failure (rings) → spectral bridge
6. The computational pressure point (where cost lives)
7. Qubits & superposition (Bloch, 2ⁿ)
8. Encoding data + overlap = similarity
9. The Swap Test (the hero slide)
10. Quantum k-means (assemble)
11. Quantum kernel clustering (NISQ route) 
12. Reality check / dequantization / honest advantage
13. Live demo pointer (notebook)
14. Industry + India impact (from context module)
15. Shared close + Q&A

---

## Key references
- Lloyd, Mohseni, Rebentrost, *Quantum algorithms for supervised and unsupervised machine learning* (2013) — quantum k-means / distance estimation.
- Havlíček et al., *Supervised learning with quantum-enhanced feature spaces*, Nature (2019) — quantum kernels/feature maps.
- Schuld & Killoran, *Quantum ML in feature Hilbert spaces*, PRL (2019).
- Tang, *A quantum-inspired classical algorithm for recommendation systems* (2018) — dequantization.
- Biamonte et al., *Quantum machine learning*, Nature (2017) — survey.
- Cerezo et al., *Variational quantum algorithms*, Nature Reviews Physics (2021) — barren plateaus, NISQ.
- PennyLane & Qiskit Machine Learning documentation — swap test, quantum kernels.
