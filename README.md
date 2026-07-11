# Quantum Lectures — Archit Srivastava

Central repository for quantum-computing lecture material. Each lecture/event lives in its own folder.

## Contents

| Folder | Event | What's inside |
|---|---|---|
| **[NIT Warangal](NIT%20Warangal/)** | **QML-2026 FDP** — E&ICT Academy, NIT Warangal × NIT Raipur (11 Jul 2026) | Session 1 *Quantum Unsupervised Learning (Clustering)* — editable Qiskit-template deck (62 slides), executed PennyLane demo notebook, reproducible build pipeline (`build/`), diagrams, logos, research + deep-research notes |
| **[ICQIA-2026](ICQIA-2026/)** | ICQIA-2026 | Earlier `arcane` deck (HTML + PDF) |
| `Templates - IBM Qiskit Advocate/` | — | IBM Qiskit slide template (`.pptx`) used to build the decks |
| `assets/`, `fonts/` | — | Brand assets, illustrations, IBM Plex / Telegraf fonts |

## Session 1 — key files
- Deck: [`NIT Warangal/session1_quantum_clustering_qiskit.pptx`](NIT%20Warangal/session1_quantum_clustering_qiskit.pptx)
- Notebook (executed, standalone): [`NIT Warangal/notebooks/qml_clustering_demo.ipynb`](NIT%20Warangal/notebooks/qml_clustering_demo.ipynb) · [HTML](NIT%20Warangal/notebooks/qml_clustering_demo.html)
- Build pipeline: [`NIT Warangal/build/`](NIT%20Warangal/build/) — `make_skeleton.py` → content workflow → `gen_diagrams.py` → `build_v2.py` → `verify.py`

## Rebuild a deck
```bash
cd "NIT Warangal/build"
pip install python-pptx matplotlib numpy scikit-learn pennylane==0.38.0 "autoray==0.6.12"
python3 make_skeleton.py && python3 build_v2.py && python3 verify.py
```

## Project context
See [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) for the full build pipeline, content-style rules, environment gotchas, and how to build the next session.

> Note: the 97 MB Keynote template (`.key`) is intentionally untracked (`.gitignore`). Use Git LFS to track it if needed.
