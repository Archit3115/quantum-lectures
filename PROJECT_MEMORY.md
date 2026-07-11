# Lectures — Project Memory (reusable across sessions)
*Persistent context for the QML-2026 FDP lecture decks. Read this first when resuming.
Last updated: 2026-07-11 (both sessions built). To build a queryable knowledge graph, run `graphify .` with an LLM key set (GEMINI/ANTHROPIC/OPENAI) — the docs need semantic extraction; a key was not available at authoring time.*

## Who / what
- **Speaker:** Archit Srivastava — **Senior Manager, Data Engineering @ PUMA, Bengaluru** (current); prior o9 Solutions + HPE (quantum PoCs); early intern BosonQ Psi. Founder **AiQyaM** (India's first quantum-hardware community, 2020) & **CIRQuIT** (RVCE); Sr Research Associate, Quantum Computing India; GKQCTP/IQDC with Innogress. B.E. Electronics & Instrumentation, RVCE. Google Scholar **NbPUdWMAAAAJ** (6 papers incl. *Quantum Computing and LIGO*, IAC-20; *Quantum Finance—An Overview*, EasyChair 6071, 2021, Qiskit+PennyLane VQE). Speaks Conf42 QC 2023+2024. Email architsrivastava3115@gmail.com.
- **Event:** QML-2026 FDP, E&ICT Academy **NIT Warangal × NIT Raipur**, **11 Jul 2026**. Session 1 (09:30–11:30) = Quantum Unsupervised Learning (Clustering) — **done (62 slides)**. Session 2 (14:30–16:30) = Classical & Quantum-Enhanced Computer Vision — **done (56 slides)**.

## Deliverables
- **Session 1:** `NIT Warangal/session1_quantum_clustering_qiskit.pptx` — **62 slides**. Sections: Title · Contents · About(×2) · Roadmap · §1 Introduction · §2 Classical · §3 Quantum (incl. 3 live-notebook slides) · §4 Industry & Mega-Science · §5 India · §6 Future · Thanks. Notebook `notebooks/qml_clustering_demo.ipynb` (quantum-kernel clustering, ARI 0.42 vs 0.69).
- **Session 2:** `NIT Warangal/session2_quantum_vision_qiskit.pptx` — **56 slides**. Sections: Title · Contents · About(×2) · Roadmap · §1 Introduction · §2 Classical Computer Vision · §3 Quantum-Enhanced Vision (incl. 3 live-notebook slides) · §4 Industry & Applications (incl. mega-science imaging) · §5 India · §6 Future · Thanks. Notebook `notebooks/qml_vision_demo.ipynb` (4-qubit quanvolution on digits, raw 0.978 vs untrained-quanv 0.950).

## Build pipeline (`NIT Warangal/build/`)
Run order: `make_skeleton.py` → (content workflow) → `gen_diagrams.py` → `fetch_logos.py` → `notebook_demo.py` → `build_v2.py` → `verify.py`.
- **`make_skeleton.py`** → `skeleton.json`: the fixed backbone I own — per-slide `id, kind, kicker, title, img{f,side}, stats, table, cards, flowV, must` facts, diagram assignments, stat numbers. **Layout/diagrams/numbers live here.**
- **Content workflow** (Workflow tool, 9 section-agents, grounded by reading the research docs) → returns per-slide `{body[], defs[], cards[]}`; extract from the run's `journal.jsonl` into **`content.json`**. Agents write ONLY prose + definitions.
- **`gen_diagrams.py`** → `../assets_generated/*.png` (26 matplotlib figures, IBM Carbon palette, **white background** so they read on any slide). Two-moons demo is really computed (k-means ARI 0.42 vs quantum-kernel spectral 0.69).
- **`fetch_logos.py`** → `../template_assets/logos/*.png` (21 brand marks via **DuckDuckGo favicon API** `icons.duckduckgo.com/ip3/<domain>.ico` + Google favicon fallback; Clearbit is dead). `LOGOS` dict in build_v2 maps slide id → logo names.
- **`notebook_demo.py`** → runs a real 2-qubit **PennyLane** quantum-kernel clustering notebook, composes authentic Jupyter cell screenshots `../assets_generated/nb_cell{1..4}.png`, writes `../notebooks/qml_clustering_demo.ipynb`.
- **`build_v2.py`** → the renderer (data-driven from skeleton+content). `build_session1_pptx.py` is the OLD v1 (ignore).
- **`anim.py`** → per-paragraph/per-element entrance animations (`add_entrance_anims`) + `add_transition` (page fade).
- **`verify.py`** → slide count, leftover-template-text, out-of-bounds, **estimated text overflow**, voice check.

## Environment gotchas (save time next session)
- **PennyLane 0.38 needs `autoray==0.6.12`** (0.8.x → `NumpyMimic` AttributeError). `pip install --force-reinstall --no-deps autoray==0.6.12`.
- IBM Qiskit template is a **DARK** master (all clrMap `bg1=dk1`). Content slides force a **white** background (`set_bg(slide,"FFFFFF")`); diagrams are white-bg so they work on both. Section dividers + a few feature slides stay dark.
- Delete template example slides via `prs.part.drop_rel(sldId r:id)` (NOT just removing sldId → duplicate-partname corruption). **`strip_ph(slide)`** removes empty placeholders (kills the "Double-click to edit" ghost in Keynote).
- **Fonts:** deck uses IBM Plex Sans/Mono — installed to `~/Library/Fonts` (from `Lectures/fonts/` + IBM/plex v6.4.0). Any preview on this Mac renders serif substitution; PowerPoint/Keynote render correctly. Quit Keynote fully after installing fonts.
- **No local renderer** (no LibreOffice). Visual-verify trick: reorder a target slide to front in a throwaway copy, then `qlmanage -t -s 1500 -o <dir> file.pptx` renders slide 1 to PNG.

## CONTENT STYLE RULES (hard-won from user feedback — apply to Session 2)
1. **Verbose, plain-language, ~80% general audience** (assume non-physicists). Explain like Feynman. NOT terse fragments, NOT dense paragraphs — a short lead + detailed **complete-sentence bullets** + `head` sub-labels. Keep the full depth, structured as points.
2. **Light on equations.** No raw formulas/Greek symbols in body text — explain what a quantity means in words. Formulas live in the diagrams only.
3. **Strict THIRD PERSON.** Never `you / your / we / our / us / I / my / me / let`. Speaker's own work in third person ("Srivastava's 2021 paper…"). `verify.py` audits this.
4. **KEY TERMS definition box on every jargon slide** — each technical term/acronym gets a plain one-sentence definition (`defs:[{term,def}]`). Renderer places it: right-column under a side diagram/flow/table, or a 2-col bottom strip for full-width layouts.
5. **Real logos** on industry/mega-science/India slides (small chips, top-right rule-row or per layout).
6. **Strict margins:** `MX=0.55" left, RX=12.78" right, CT=1.66" top, CB=7.02" bottom`; two-column `LW=6.0"` + right col. Everything aligns to this grid.
7. Animations: per-paragraph fade + card/image fly-in + page fade transitions. Entrance only (no exit — would hide read-aloud text).

## Session 2 (computer vision) — BUILT (how it was done, for future edits)
Same `build/` pipeline, session-2 variants. **Build:** `python3 make_skeleton2.py && python3 gen_diagrams2.py && python3 build_v2.py session2 && python3 verify.py session2`.
- **`make_skeleton2.py`** → `skeleton2.json` (56-slide CV backbone; image-as-grid, convolution atom, CNN anatomy + 3 priors, ViT, encodings, quanvolution hero, QCNN, hybrid sandwich, own-work QFT, industry incl. mega-science imaging).
- **`gen_diagrams2.py`** → 16 new CV diagrams (white-bg Carbon). Real compute: `quanv_featuremaps.png` (3 digits × 4 quantum channels) + `quanv_result.png` (bars). Reuses S1 diagrams: timeline, talent_gap, nqm_targets, funding_bars, bloch_sphere, amplitude_growth, advantage_quadrant, featuremap.
- **Content workflow** = `scratchpad/content_workflow_s2.js` (Workflow tool, **8 section-agents**, `agentType:'general-purpose'`, grounded in `session2_research.md` + `session2_deep_research_2026.md` + `speaker_own_work.md`); each writes `c2_<sec>.json`, merged → `content2.json` (47 content slides; dividers + notebook slides need none). Cap defs to 6/slide; side-image defbox renders `cols=2` when >3 defs.
- **`build_v2.py`** now takes a session arg (default `session1`); per-session config in the `DECKS` dict (skeleton/content/out/title/agenda/divfoot/thanks_session/logos). `verify.py session2` too (+ added a strict 3rd-person voice audit).
- **Notebook:** `build_vision_notebook.py` → executed standalone `qml_vision_demo.ipynb`(+HTML); `notebook_demo2.py` → cell shots `nbv_cell{1..4}.png`. 4-qubit quanvolution (RY angle-encode + RandomLayers + PauliZ), sklearn digits, **raw 0.978 vs untrained-quanv 0.950, ~39 ms/img**.
- **Honesty spine (from deep research):** NO demonstrated quantum advantage on natural images in 2026 (Henderson's own random-vs-quantum tie; QCNN image benchmarks proven classically simulable, PRX Quantum 2026). Frame quantum vision as an early hybrid front-end feature extractor. Real industry results are hybrid/at-parity (IBM pathology GNN, ESA EuroSAT, Honda Scenes 72-qubit >90%, Multiverse×Ikerlan). India edge = imaging-data fuel (NISAR ~80 TB/day) + talent, not quantum-CV today.
- **Logos:** `fetch_logos.py` extended (nvidia, esa, multiverse, terraquantum, nasa…); favicon API is flaky — if it clears the dir and some fail, restore committed ones from git (`git show HEAD:.../logos/X.png`). esa/tcs currently absent (graceful fallback).
- Shared India/Viksit-Bharat + market/talent modules reused from `session1_deep_research_2026.md` + `india_quantum_context.md`.

## Key files
- Research: `NIT Warangal/Research Reference Docs/` — session1_research.md, Quantum Unsupervised Learning Research Guide.md, india_quantum_context.md, **session1_deep_research_2026.md** (refreshed 2026 numbers + mega-science LIGO/CERN/ITER/SKA/DUNE), **archit_bio_research.md**, speaker_own_work.md, session{1,2}_speaker_notes.md.
- Assets: `NIT Warangal/assets_generated/` (diagrams+nb cells), `NIT Warangal/template_assets/` (Qiskit spheres, graphs, wordmark, **logos/**), `assets/` (Qyros brand, founder photo, illustrations), `fonts/`.
- Template: `Templates - IBM Qiskit Advocate/Qiskit_Foundations_QAP.pptx`.
