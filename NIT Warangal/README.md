# QML-2026 FDP — Expert Session Package
**Archit Srivastava · E&ICT Academy NIT Warangal × NIT Raipur · 11 July 2026**

Two 2-hour expert sessions, built first-principles bottom-up for a faculty audience.
Shared India / Viksit Bharat 2047 opening + closing module across both.

- **Session 1 (09:30–11:30):** Quantum Unsupervised Learning (Clustering)
- **Session 2 (14:30–16:30):** Classical & Quantum-Enhanced Computer Vision

---

## What's in this package

### Slide decks (bespoke HTML engine — HPE-green design system, canvas wave background)
| File | Description |
|---|---|
| `decks/session1_quantum_clustering.html` | Session 1 deck — open in any browser; arrow keys / click zones to navigate, `f` for fullscreen |
| `decks/session1_quantum_clustering.pdf` | Session 1 PDF export (21 pages, one per slide) |
| `decks/session2_quantum_vision.html` | Session 2 deck |
| `decks/session2_quantum_vision.pdf` | Session 2 PDF export (19 pages) |

> The HTML decks are the primary artifact (animated, interactive). The PDFs are a static print/backup version rendered slide-per-page.

### Runnable notebooks (PennyLane, CPU-only, no quantum hardware)
| File | Description |
|---|---|
| `notebooks/qml_clustering_demo.ipynb` | Quantum-kernel spectral clustering on two moons. k-means ARI 0.43 vs quantum-kernel spectral ARI 0.69. 2-qubit data-reuploading feature map. |
| `notebooks/qml_vision_demo.ipynb` | Quanvolution on `load_digits`. Classical conv/Sobel, a 4-qubit 2×2 quanvolution circuit, feature-map viz, honest hybrid comparison (raw 0.978 vs untrained-quanv 0.856). |

**To run:** `pip install pennylane scikit-learn matplotlib` then open in Jupyter and Run All. Both are shipped unexecuted so the audience sees results generate live.

### Research + speaker notes
| File | Description |
|---|---|
| `research/session1_research.md` | Session 1 technical research (clustering first principles → quantum kernels) |
| `research/session2_research.md` | Session 2 technical research (computer vision first principles → quanvolution/QCNN) |
| `research/session1_speaker_notes.md` | Slide-by-slide talk track, timing map, anticipated Q&A |
| `research/session2_speaker_notes.md` | Slide-by-slide talk track, timing map, anticipated Q&A |
| `research/india_quantum_context.md` | Shared India / NQM / Viksit Bharat / global-market research module |
| `research/speaker_own_work.md` | How the speaker's two papers map into each session |

### Figures (`figures/`)
Deck-palette PNGs: clustering result, kernel matrices, swap-test & quanvolution circuits (authentic PennyLane renders), quanvolution feature maps, accuracy bars, global-market projection, India funding comparison.

---

## Design system
Built in the same bespoke HTML engine as the speaker's previous deck (`arcane_17.html`):
HPE-green accent (#01A982 / #17EBA0), Space Grotesk / Outfit / IBM Plex Mono, animated canvas
sine-wave background, staggered fragment reveals, animated counters. India flag rendered as an
inline CSS component in the sovereignty/NQM slides.

## Key numbers (verified against research docs)
- Global: up to **$2.7T** economic value by 2035 (McKinsey QTM 2026); **$12.6B** quantum startup investment in 2025 (6.3× YoY); **~840k** jobs needed by 2035 vs ~5,000 qualified.
- India NQM: **₹6,003.65 cr** (2023–2031), staged 20-50 → 50-100 → 50-1000 qubits, 4 thematic hubs.
- Session 1 demo: k-means ARI **0.43** vs quantum-kernel spectral **0.69** (2 qubits).
- Session 2 demo: raw-pixel acc **0.978** vs untrained-quanvolution acc **0.856** (4 qubits).

## Speaker
Archit Srivastava — Google Scholar: NbPUdWMAAAAJ · architsrivastava3115@gmail.com · Founder, AiQyaM (India's first quantum-hardware community, est. 2020)
