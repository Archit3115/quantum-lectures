# Lectures — Project Contract (auto-loaded every session in this folder)

**Read `PROJECT_MEMORY.md` (repo root) at the start of every session** — it holds the full reusable context: speaker bio, the deck build pipeline, environment gotchas, and the content style rules.

## What this repo is
QML-2026 FDP lecture decks for **Archit Srivastava** (Senior Manager Data Engineering @ PUMA; founder AiQyaM). Two sessions, 11 Jul 2026, NIT Warangal × NIT Raipur. Built on the **IBM Qiskit template** via a Python pipeline in `NIT Warangal/build/`.

## Non-negotiable content style (learned from user feedback — apply to every slide)
1. **Verbose but plain-language**, ~80% general/non-physicist audience. Short lead + detailed complete-sentence **bullets** + `head` sub-labels. Keep depth; structure as points, not walls of prose, not terse fragments.
2. **Light on equations** — explain quantities in words; formulas live only in diagrams.
3. **Strict THIRD PERSON** — never `you/your/we/our/us/I/my/me/let`; speaker's work in third person. `build/verify.py` audits it.
4. **KEY TERMS box** defining every technical term in plain language on the slide.
5. **Real company/org logos** on industry/mega-science/India slides.
6. **Strict margins** (MX 0.55" / RX 12.78" / CT 1.66" / CB 7.02"); everything aligns.
7. Entrance animations (per-paragraph fade + fly-in) + page fade transitions.

## Build/verify
`cd "NIT Warangal/build"` then `python3 make_skeleton.py && python3 build_v2.py && python3 verify.py`. Content prose/definitions come from the Workflow tool (9 section-agents grounded in `Research Reference Docs/`), extracted into `content.json`. Diagrams: `gen_diagrams.py`. Logos: `fetch_logos.py`. Notebook: `notebook_demo.py`. Fonts (IBM Plex) already installed to `~/Library/Fonts`. **PennyLane 0.38 requires `autoray==0.6.12`.**

## Session 2 (computer vision) — BUILT
`session2_quantum_vision_qiskit.pptx` — **56 slides**, same pipeline + style rules. Build: `cd "NIT Warangal/build"` then `python3 make_skeleton2.py && python3 gen_diagrams2.py && python3 build_v2.py session2 && python3 verify.py session2`. Content in `content2.json` (from the `content_workflow_s2.js` Workflow, 8 section-agents grounded in `session2_research.md` + `session2_deep_research_2026.md` + `speaker_own_work.md`). Notebook: `build_vision_notebook.py` → executed `notebooks/qml_vision_demo.ipynb` (+HTML); cell shots `notebook_demo2.py` → `nbv_cell{1..4}.png`. Real quanvolution demo: raw-pixel classifier 0.978 vs untrained 4-qubit quanvolution 0.950 on sklearn digits. `build_v2.py` takes a session arg (`session1` default / `session2`); `verify.py` too.

## Outputs
Editable `.pptx` on the Qiskit template is the deliverable. Do not overwrite `session1_quantum_clustering_qiskit.pptx` or `session2_quantum_vision_qiskit.pptx` without rebuilding from the scripts.
