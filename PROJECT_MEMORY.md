# Lectures — Project Memory (reusable across sessions)
*Persistent context for the QML-2026 FDP lecture decks. Read this first when resuming or starting Session 2.
Last updated: 2026-07-11. To build a queryable knowledge graph, run `graphify .` with an LLM key set (GEMINI/ANTHROPIC/OPENAI) — the docs need semantic extraction; a key was not available at authoring time.*

## Who / what
- **Speaker:** Archit Srivastava — **Senior Manager, Data Engineering @ PUMA, Bengaluru** (current); prior o9 Solutions + HPE (quantum PoCs); early intern BosonQ Psi. Founder **AiQyaM** (India's first quantum-hardware community, 2020) & **CIRQuIT** (RVCE); Sr Research Associate, Quantum Computing India; GKQCTP/IQDC with Innogress. B.E. Electronics & Instrumentation, RVCE. Google Scholar **NbPUdWMAAAAJ** (6 papers incl. *Quantum Computing and LIGO*, IAC-20; *Quantum Finance—An Overview*, EasyChair 6071, 2021, Qiskit+PennyLane VQE). Speaks Conf42 QC 2023+2024. Email architsrivastava3115@gmail.com.
- **Event:** QML-2026 FDP, E&ICT Academy **NIT Warangal × NIT Raipur**, **11 Jul 2026**. Session 1 (09:30–11:30) = Quantum Unsupervised Learning (Clustering) — **done**. Session 2 (14:30–16:30) = Classical & Quantum-Enhanced Computer Vision — **not yet built** (same pipeline applies).

## Deliverable (Session 1)
`NIT Warangal/session1_quantum_clustering_qiskit.pptx` — **62 slides**, editable, built on the IBM Qiskit template. Sections: Title · Contents · About(×2) · Roadmap · §1 Introduction · §2 Classical · §3 Quantum (incl. 3 live-notebook slides) · §4 Industry & Mega-Science · §5 India · §6 Future · Thanks.

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

## For Session 2 (computer vision) — reuse
- Same `build/` pipeline. Session-2 research already in `Research Reference Docs/session2_*.md` + `speaker_own_work.md` (Paper B: CNN + Quantum Visual Tracking, QFT on IBM hardware — the CV credibility anchor).
- Write a `skeleton.json` for CV (CNN anatomy, convolution, pooling, quanvolution, QCNN, amplitude encoding, the vision demo `qml_vision_demo.ipynb`), run the same content workflow with the SAME style rules above, generate CV diagrams, build.
- Shared India/Viksit-Bharat + market/talent modules can be reused verbatim from `session1_deep_research_2026.md` + `india_quantum_context.md`.

## Key files
- Research: `NIT Warangal/Research Reference Docs/` — session1_research.md, Quantum Unsupervised Learning Research Guide.md, india_quantum_context.md, **session1_deep_research_2026.md** (refreshed 2026 numbers + mega-science LIGO/CERN/ITER/SKA/DUNE), **archit_bio_research.md**, speaker_own_work.md, session{1,2}_speaker_notes.md.
- Assets: `NIT Warangal/assets_generated/` (diagrams+nb cells), `NIT Warangal/template_assets/` (Qiskit spheres, graphs, wordmark, **logos/**), `assets/` (Qyros brand, founder photo, illustrations), `fonts/`.
- Template: `Templates - IBM Qiskit Advocate/Qiskit_Foundations_QAP.pptx`.
