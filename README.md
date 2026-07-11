# Quantum Lectures — Archit Srivastava

Central repository for quantum-computing lecture material. Each lecture/event lives in its own folder.

## Contents

| Folder | Event | What's inside |
|---|---|---|
| **[NIT Warangal](NIT%20Warangal/)** | **QML-2026 FDP** — E&ICT Academy, NIT Warangal × NIT Raipur (11 Jul 2026) | **Session 1** *Quantum Unsupervised Learning (Clustering)* — deck (62 slides) + executed quantum-kernel clustering notebook. **Session 2** *Quantum-Enhanced Computer Vision* — deck (56 slides) + executed quanvolution notebook. Both editable Qiskit-template decks, one reproducible build pipeline (`build/`), diagrams, logos, research + deep-research notes |
| **[ICQIA-2026](ICQIA-2026/)** | ICQIA-2026 | Earlier `arcane` deck (HTML + PDF) |
| `Templates - IBM Qiskit Advocate/` | — | IBM Qiskit slide template (`.pptx`) used to build the decks |
| `assets/`, `fonts/` | — | Brand assets, illustrations, IBM Plex / Telegraf fonts |

## Key files
**Session 1 — Quantum Unsupervised Learning (Clustering)**
- Deck: [`NIT Warangal/session1_quantum_clustering_qiskit.pptx`](NIT%20Warangal/session1_quantum_clustering_qiskit.pptx)
- Notebook (executed, standalone): [`qml_clustering_demo.ipynb`](NIT%20Warangal/notebooks/qml_clustering_demo.ipynb) · [HTML](NIT%20Warangal/notebooks/qml_clustering_demo.html)

**Session 2 — Quantum-Enhanced Computer Vision**
- Deck: [`NIT Warangal/session2_quantum_vision_qiskit.pptx`](NIT%20Warangal/session2_quantum_vision_qiskit.pptx)
- Notebook (executed, standalone): [`qml_vision_demo.ipynb`](NIT%20Warangal/notebooks/qml_vision_demo.ipynb) · [HTML](NIT%20Warangal/notebooks/qml_vision_demo.html)

Shared build pipeline: [`NIT Warangal/build/`](NIT%20Warangal/build/) — `make_skeleton{,2}.py` → content workflow → `gen_diagrams{,2}.py` → `build_v2.py [session1|session2]` → `verify.py [session]`.

## Rebuild a deck
```bash
cd "NIT Warangal/build"
pip install python-pptx matplotlib numpy scikit-learn pennylane==0.38.0 "autoray==0.6.12"
# Session 1
python3 make_skeleton.py  && python3 build_v2.py           && python3 verify.py
# Session 2
python3 make_skeleton2.py && python3 gen_diagrams2.py && python3 build_v2.py session2 && python3 verify.py session2
```

## Project context
See [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) for the full build pipeline, content-style rules, environment gotchas, and how to build the next session.

> Note: the 97 MB Keynote template (`.key`) is intentionally untracked (`.gitignore`). Use Git LFS to track it if needed.
