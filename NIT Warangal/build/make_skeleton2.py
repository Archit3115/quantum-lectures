#!/usr/bin/env python3
"""Emit skeleton2.json — the fixed backbone of the verbose Session-2 deck
(Classical & Quantum-Enhanced Computer Vision). Same data model + kinds as Session 1.
I own layout/diagrams/numbers/tables/'must' facts; the content workflow writes only
verbose plain-language THIRD-PERSON teaching prose (body blocks + defs + card lines) per slide id."""
import json,os
S=[]
def add(**k): S.append(k)

# ---------------- FRONT ----------------
add(id="title",kind="title",sec=0,title="Quantum-Enhanced Computer Vision")
add(id="agenda",kind="agenda",sec=0,kicker="Contents",title="What this session builds in the next two hours",
    brief="One line per section for a computer-vision arc: what an image is, the CNN, the quantum turn (encoding + quanvolution), the honest picture, and impact. Motivate the spine: computer vision is about learning good representations, and quantum changes the front-end feature extractor.")
add(id="aboutbio",kind="aboutbio",sec=0,kicker="About the speaker",title="Archit Srivastava",
    brief="Verbose spoken bio the presenter reads (same person as Session 1): current role Senior Manager Data Engineering at PUMA Bengaluru; prior o9 Solutions + HPE (quantum PoCs); founder AiQyaM (India's first quantum-hardware community, 2020) and CIRQuIT at RVCE; Senior Research Associate Quantum Computing India; GKQCTP/IQDC with Innogress Ventures; early intern BosonQ Psi. Electronics & Instrumentation background, ~4 yrs industry. Add the Session-2 hook: co-author of a published paper with a real 5-layer CNN vision pipeline AND a quantum-visual-tracking section run on IBM hardware, so today's arc is literally his own research path.")
add(id="aboutresearch",kind="aboutresearch",sec=0,kicker="About the speaker",title="The research behind this talk — first-hand, not abstract",
    brief="Verbose: 5+ papers, 25+ talks across 10+ universities / 200+ faculty, Conf42; research areas span computer vision (a real CNN eye-contact pipeline), quantum visual tracking / quantum image processing, black-hole physics & gravitational waves via quantum+AI, photonic quantum computing, quantum finance. Tie to why today's material is built and run, not abstract. Papers list is rendered from Scholar record.")
add(id="roadmap",kind="roadmap",sec=0,kicker="How this session works",title="Starting from the familiar — one quantum idea at a time",
    brief="Verbose: the design principle (every quantum idea introduced from a classical anchor faculty already teach); the spine sentence computer-vision = learning good representations (local, hierarchical, invariant) and quantum replaces the convolution atom with a quantum feature extractor; note one live PennyLane CPU notebook (quanvolution on digits), no hardware needed.",
    flow=["What an image is\n(grid of numbers)","The CNN\n(convolution, pooling)","The quantum turn\n(encoding, quanvolution)","The honest picture\n(demo + caveats)","Impact\n(industry, India)"])

# ---------------- §1 INTRODUCTION ----------------
add(id="d1",kind="divider",sec=1,num="01",title="Introduction",accent="blue",
    summary="Why should an Indian university invest attention in teaching machines to see — with quantum, now?")
add(id="whynow1",kind="textimg",sec=1,kicker="Section 1 · Introduction",title="2025: the year quantum advantage became measured fact",
    img={"f":"timeline.png","side":"right"},
    brief="Verbose: 2025 moved quantum advantage from promise to measured fact; set up the three peer-reviewed firsts on the timeline; land the faculty point that quantum is now a computational tool students across every discipline — including vision and AI — will be asked about.",
    must=["Willow 105 qubits Nature Dec 2024 below-threshold Λ≈2.14","Quantum Echoes Nature Oct 2025 ~13,000× verifiable","D-Wave Advantage2 Science Mar 2025 (contested)"])
add(id="whynow2",kind="cards",sec=1,kicker="Section 1 · Introduction",title="Three peer-reviewed firsts, one year",
    cards=[{"title":"Google Willow","accent":"blue"},{"title":"Quantum Echoes","accent":"magenta"},{"title":"D-Wave Advantage2","accent":"teal"}],
    brief="For each card write 3-4 verbose lines the presenter reads: what it is, the number, why it matters. Be honest (Willow=first below-threshold QEC; Echoes=first verifiable advantage; D-Wave=useful-problem supremacy but contested).",
    must=["Willow Λ≈2.14, distance-7","Echoes ~13,000× via OTOCs on 65 qubits","Advantage2 4400+ qubits, spin-glass, contested"])
add(id="market1",kind="stats",sec=1,kicker="Section 1 · Introduction",title="The stakes: a commercial tipping point",
    stats=[{"num":"$1.3–2.7T","label":"economic value by 2035 (McKinsey QTM 2026)","accent":"blue"},
           {"num":"$12.6B","label":"quantum start-up investment in 2025 — 6.3× 2024","accent":"teal"},
           {"num":">$1B","label":"quantum-computing revenue 2025 → ~$4.4B by 2028","accent":"purple"},
           {"num":"$450–850B","label":"BCG economic-value estimate by 2040","accent":"magenta"}],
    brief="Verbose framing under the tiles: the discourse moved from 'if' to 'when'; the value is in the algorithm/software/AI layer (the outcomes), not selling processors — India's strength; computer vision, as the most data-heavy branch of AI, is squarely in that value layer.")
add(id="visionstakes",kind="textimg",sec=1,kicker="Section 1 · Introduction",title="Why computer vision — and why the cost is the opening for quantum",
    img={"f":"cv_cost.png","side":"right"},
    brief="Verbose: vision is the dominant modality of modern AI — cameras in every phone, hospital, satellite, factory line; but frontier vision models are enormous in compute, energy and labelled data; that cost is precisely the pressure point quantum-enhanced methods aim at (richer features from fewer parameters, or feature spaces classical nets cannot cheaply reach). Set up the whole session as: keep the vision you teach, and look at where a quantum circuit slots in.",
    must=["frontier vision training = millions of dollars + megawatt-hours","state-of-the-art vision models are enormous in compute, energy, labelled data"])
add(id="talent",kind="textimg",sec=1,kicker="Section 1 · Introduction",title="The line that lands in a faculty room: talent",
    img={"f":"talent_gap.png","side":"right"},
    brief="Verbose: the talent gap is the whole reason an FDP exists; explain the numbers as spoken narration and land 'that gap is the mandate — and the students' opportunity'; quantum machine learning for vision is a first-principles subject faculty can teach today on a laptop.",
    must=["~250k roles by 2030, ~840k by 2035","~3 openings per qualified hire; ~half of 2025 roles unfilled"])

# ---------------- §2 CLASSICAL COMPUTER VISION ----------------
add(id="d2",kind="divider",sec=2,num="02",title="Classical Computer Vision",accent="teal",
    summary="Bottom-up, from a grid of numbers to the CNN — the field faculty already teach, and where it strains.")
add(id="imagegrid",kind="textimg",sec=2,kicker="Section 2 · Classical CV",title="The computer never sees a cat — it sees a spreadsheet of numbers",
    img={"f":"image_grid.png","side":"right"},
    brief="Verbose keystone: a greyscale image is a grid of pixel intensities (0=black to 255=white); a colour image is three such grids (red, green, blue); a 28x28 digit is 784 numbers, a one-megapixel colour photo is three million numbers; computer vision is the art of turning that spreadsheet of brightness values back into meaning — edge, texture, shape, object, scene.",
    must=["greyscale = one grid 0..255","colour = 3 grids (R,G,B)","28×28 digit = 784 numbers; 1-MP colour photo = ~3 million numbers"])
add(id="rawpixels",kind="textimg",sec=2,kicker="Section 2 · Classical CV",title="Why raw pixels are a terrible representation",
    img={"f":"representation.png","side":"right"},
    brief="Verbose: three problems with feeding raw pixels to a model — (1) high dimensional (hundreds to millions of numbers); (2) no built-in notion of locality (neighbouring pixels are just two entries in a long flat list); (3) not translation invariant (shift the cat two pixels right and every number changes, though it is the same cat). Land the thesis: computer vision is fundamentally about learning good representations — features that are local, hierarchical, and invariant — and that one idea drives everything from hand-crafted filters to CNNs to quantum encodings.")
add(id="convolution",kind="textimg",sec=2,kicker="Section 2 · Classical CV",title="The convolution atom — slide a small window and combine",
    img={"f":"convolution.png","side":"right"},
    brief="Verbose: convolution slides a small matrix (a kernel, e.g. 3x3) over the image and at each stop computes a weighted sum of the pixels under it; different kernels detect different things — a Sobel kernel finds edges, a blur kernel averages; this slide-a-small-window-and-combine operation is the atom of all of vision. Plant the flag clearly: remember this atom, because the quantum method later replaces exactly it. Note the pre-deep-learning era hand-designed these filters (SIFT, HOG, Haar) — powerful but brittle, a human had to invent each one.",
    must=["kernel = small matrix slid over the image","Sobel = edge detector; blur = averaging","convolution is the atom the quantum method replaces"])
add(id="cnn",kind="textimg",sec=2,kicker="Section 2 · Classical CV",title="The CNN — features that learn themselves",
    img={"f":"cnn_anatomy.png","side":"right"},
    brief="Verbose: AlexNet (2012) halved the ImageNet error rate and started the deep-learning era; the key idea is do not hand-design the kernels, learn them from data. Walk the anatomy as spoken narration: convolutional layers (many learnable kernels produce feature maps — early layers learn edges, middle layers textures and parts, deep layers whole objects: a hierarchy of representation); a non-linearity (ReLU keeps positive responses, zeros the rest); pooling (take the max or average over a small window — shrinks the map and buys translation invariance); repeat deeper and more abstract; a fully-connected head plus softmax classifies; training adjusts every kernel by backpropagation and gradient descent to reduce a loss. Note this is the architecture from the speaker's own 2022 paper.",
    must=["AlexNet 2012 halved ImageNet error","conv → ReLU → pooling → fully-connected + softmax","kernels are learned by backpropagation, not hand-designed"])
add(id="priors",kind="cards",sec=2,kicker="Section 2 · Classical CV",title="Three structural priors make CNNs work",
    cards=[{"title":"Local connectivity","accent":"blue"},{"title":"Weight sharing","accent":"teal"},{"title":"Hierarchy","accent":"purple"}],
    brief="Each card verbose 3-4 lines — say these clearly because they recur in the quantum story. Local connectivity: a pixel relates first to its neighbours, so a filter only looks at a small patch at a time. Weight sharing: the same edge-detector is useful everywhere in the image, so one kernel is reused across the whole picture, giving far fewer parameters. Hierarchy: simple features (edges) compose into complex ones (textures, parts, objects). Under the cards land that quantum convolution (QCNN) reproduces weight-sharing and hierarchy natively.")
add(id="vit",kind="textimg",sec=2,kicker="Section 2 · Classical CV",title="Beyond CNNs — Vision Transformers",
    img={"f":"vit_patches.png","side":"right"},
    brief="Verbose: Vision Transformers (ViT, 2020) treat an image as a grid of patches (e.g. 16x16 pixels) and use attention — every patch can look at every other patch — instead of a small sliding window; strong at scale, and the basis of today's vision foundation models; but hungrier still for data and compute. Keep it plain: the field's frontier is now huge attention-based models trained on oceans of images.",
    must=["ViT 2020: image as 16×16 patches + attention","basis of modern vision foundation models","stronger at scale, hungrier for data and compute"])
add(id="cvcost",kind="stats",sec=2,kicker="Section 2 · Classical CV",title="The bill classical vision runs up",
    stats=[{"num":"millions $","label":"cost to train a single frontier vision/multimodal model","accent":"blue"},
           {"num":"megawatt-hrs","label":"energy per frontier training run — a real climate cost","accent":"magenta"},
           {"num":"oceans","label":"of hand-labelled images needed to reach top accuracy","accent":"teal"},
           {"num":"billions","label":"of parameters in state-of-the-art vision models","accent":"purple"}],
    brief="Verbose framing (numbers refined by deep research): state-of-the-art vision is enormous in money, energy, labelled data and parameters; this is the opening quantum-enhanced methods target — richer features from fewer parameters, or feature spaces classical nets cannot cheaply reach; be honest that these are the pressure points, not a claim that quantum already beats a CNN.")

# ---------------- §3 QUANTUM-ENHANCED VISION ----------------
add(id="d3",kind="divider",sec=3,num="03",title="Quantum-Enhanced Vision",accent="purple",
    summary="Just enough quantum, from first principles — then the exact point where a circuit slots into a vision pipeline.")
add(id="qmtool",kind="statement",sec=3,accent="purple",title="Data encoding is 80% of quantum machine learning for vision.",
    brief="Verbose supporting sentences: the hard part of quantum vision is not the clever circuit, it is getting an image — a grid of numbers — onto a quantum computer in the first place; how the pixels are loaded decides whether anything useful can happen; keep this as the framing statement for the whole quantum section.")
add(id="qubit",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="A qubit: superposition on the Bloch sphere",
    img={"f":"bloch_sphere.png","side":"right"},
    brief="Verbose recap (fast if audience saw the morning): a qubit is a blend of 0 and 1 with two amplitudes whose squared sizes are the probabilities and must sum to one; superposition means it is genuinely both before measurement; the Bloch sphere pictures it as a continuous direction, not a single bit; measurement collapses it to a classical 0 or 1.",
    must=["|ψ⟩ = α|0⟩ + β|1⟩, |α|²+|β|²=1","measurement collapses to a classical bit"])
add(id="twon",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="n qubits → 2ⁿ amplitudes, and entanglement",
    img={"f":"amplitude_growth.png","side":"left"},
    brief="Verbose: n qubits live in 2 to the n complex amplitudes — an exponentially large space, the resource; entanglement means qubits can be correlated so the whole is not described by its parts, a correlation structure with no classical analogue — for vision, entangling gates let a quantum filter mix pixel information in ways a plain linear classical filter cannot; the honest catch: measurement collapses the state, so circuits are designed so the measured expectation values are the useful features.",
    must=["50 qubits ≈ 10¹⁵ amplitudes","entanglement mixes pixels in ways linear filters can't","measured expectation values are the features"])
add(id="encoding",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="Feeding an image to a quantum computer — three encodings",
    img={"f":"encoding_compare.png","side":"right"},
    brief="Verbose comparison — this is the real question. Basis encoding: a classical bitstring becomes a computational basis state, N bits need N qubits, wasteful and rarely used. Angle encoding: each feature becomes a rotation angle on a qubit, N features need N qubits, simple and shallow and NISQ-friendly — the star, how real image patches reach real hardware today, and exactly what quanvolution uses. Amplitude encoding: features become the amplitudes of the state vector, N features need only about log-base-2 of N qubits, an exponential compression but expensive to prepare (the QRAM problem). Land the speaker line: angle encoding turns a small patch into a few rotation angles — that is what makes quanvolution run today; amplitude encoding is the exponential dream, waiting on hardware.",
    must=["Basis: N bits → N qubits (wasteful)","Angle: N features → N qubits (shallow, NISQ, used in quanvolution)","Amplitude: N features → ⌈log₂N⌉ qubits (exponential compression, expensive)"])
add(id="featuremap",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="Quantum feature maps → a space hard to fake classically",
    img={"f":"featuremap.png","side":"right"},
    brief="Verbose: a quantum feature map is a small parameterised circuit that encodes each data point into a quantum state, projecting it into an exponentially high-dimensional space (a feature Hilbert space) where structure that is tangled in the original pixels can become easier to separate; the bet of quantum machine learning is that a well-chosen, highly-entangled map reaches a space that is expensive to simulate classically, so the similarity it computes is genuinely hard to fake.")
add(id="quanv1",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="Quanvolution — replace the convolution atom with a quantum one",
    img={"f":"quanvolution.png","side":"right"},
    brief="Verbose HERO slide (Henderson et al. 2019). Walk the six-step recipe as spoken narration: (1) slide a small window, say 2x2, over the image, exactly like classical convolution; (2) angle-encode those four pixels as rotation angles on four qubits; (3) apply a random or trainable quantum circuit whose entangling gates mix the pixel information in a high-dimensional space; (4) measure each qubit to get a set of expectation values; (5) those measured numbers become new feature-map channels, stacked like classical convolution output; (6) feed the resulting feature maps into an ordinary classical CNN or dense network to classify. The honest claim: the quantum circuit produces a non-linear, high-dimensional transformation of each patch that would be expensive to compute classically — it acts as a fixed or trainable feature extractor, a richer front-end. This is the pattern for all near-term quantum vision: quantum front-end, classical back-end.",
    must=["slide a 2×2 window (like classical convolution)","angle-encode 4 pixels on 4 qubits","random/trainable circuit mixes them; measure → new channels","stack channels → feed a classical CNN head"])
add(id="quanv2",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="The quanvolution circuit, in PennyLane",
    img={"f":"quanv_circuit.png","side":"right"},
    brief="Verbose: describe the exact circuit run in the notebook — four qubits, each of the four patch pixels sets a rotation angle (RY), then a random entangling layer (PennyLane's RandomLayers) scrambles them, then each qubit's PauliZ expectation value is read out as one output channel; a single such circuit converts every 2x2 patch of an 8x8 digit into a stack of four small feature maps; it is shallow, runs on PennyLane's default.qubit simulator on a laptop CPU, and needs no quantum hardware.",
    must=["4 qubits: 4 patch pixels → 4 RY rotation angles","RandomLayers entangler; read PauliZ on each qubit","each 2×2 patch → 4 feature-map channels"])
add(id="nb1",kind="notebook",sec=3,kicker="Section 3 · Quantum Vision · Live notebook",title="The notebook, cell by cell — the images",
    imgs=["nbv_cell1.png"],
    lit=[{"t":"lead","x":"qml_vision_demo.ipynb — real PennyLane, laptop CPU, no hardware","b":["qml_vision_demo.ipynb"]},
         {"t":"b","x":"Cell 1: handwritten digits, 8×8 greyscale — each image is 64 numbers","b":["8×8 greyscale"]},
         {"t":"b","x":"Pixels scaled to the 0-to-1 range so they become rotation angles","b":["rotation angles"]},
         {"t":"b","x":"Labels kept only to score the classifier at the end — never used to build features","b":["never used to build features"]},
         {"t":"note","x":"The task: turn each image into features with a quantum circuit, then classify."}])
add(id="nb2",kind="notebook",sec=3,kicker="Section 3 · Quantum Vision · Live notebook",title="The notebook — a 4-qubit quanvolution in PennyLane",
    imgs=["nbv_cell2.png","nbv_cell3.png"],
    lit=[{"t":"lead","x":"Cell 2: a 4-qubit circuit turns every 2×2 patch into 4 numbers","b":["4-qubit circuit"]},
         {"t":"b","x":"Four pixels set four rotation angles; a random entangler mixes them","b":["random entangler"]},
         {"t":"b","x":"Each qubit is measured — four expectation values, four new channels","b":["four new channels"]},
         {"t":"b","x":"Cell 3: apply it across the image → the quantum feature maps","b":["quantum feature maps"]},
         {"t":"b","x":"Each channel is a different learned-by-physics view of the digit","b":["learned-by-physics view"]},
         {"t":"note","x":"The circuit is UNTRAINED — this is raw representational power, zero learning."}])
add(id="nb3",kind="notebook",sec=3,kicker="Section 3 · Quantum Vision · Live notebook",title="The notebook — the honest verdict",
    imgs=["nbv_cell4.png"],
    lit=[{"t":"lead","x":"Cell 4: same simple classifier, two feature sets"},
         {"t":"b","x":"On raw pixels the classifier scores 0.978 accuracy","b":["0.978"]},
         {"t":"b","x":"On the untrained quanvolution features it scores 0.950","b":["0.950"]},
         {"t":"b","x":"An untrained 4-qubit circuit already preserves ~95% of the signal","b":["~95% of the signal"]},
         {"t":"b","x":"Preprocessing was ~39 ms per image, in simulation","b":["~39 ms per image"]},
         {"t":"note","x":"Not 'quantum wins' — a random circuit is a surprisingly strong feature extractor; gains are modest and setting-dependent."}])
add(id="demo",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="Reading the demo — a feature extractor, not a magic boost",
    img={"f":"quanv_result.png","side":"left"},
    brief="Verbose: state the honest result up front — on the digits, a simple classifier on raw pixels gets 0.978 accuracy and the same classifier on the untrained random quanvolution features gets 0.950; the point is not that quantum wins, it is that an untrained four-qubit circuit already preserved about 95% of the signal and the feature maps are structured and meaningful; this is the honest teaching frame — quanvolution is a feature extractor, today's gains are modest and setting-dependent, and a fair comparison always benchmarks against a strong classical baseline.",
    must=["raw pixels 0.978 vs untrained quanvolution 0.950","~39 ms/image in simulation","quanvolution = feature extractor, not an accuracy magic-boost"])
add(id="qcnn",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="The QCNN — the fully-quantum cousin",
    img={"f":"qcnn.png","side":"right"},
    brief="Verbose (Cong, Choi & Lukin 2019): a Quantum Convolutional Neural Network mirrors the CNN structure natively — a quantum convolution is the same two-qubit unitary applied across neighbouring qubits (weight sharing, natively); a quantum pooling measures some qubits and conditions rotations on the outcome (dimensionality reduction); repeat until few qubits remain, then measure to classify. The beautiful property: a QCNN has only about log-of-n parameters, is trainable, and unlike deep generic variational circuits is relatively resistant to barren plateaus. Its native use case is classifying quantum states and phases of matter — where the image is quantum data and there is no classical shortcut; for classical images it still needs an encoding step first.",
    must=["quantum conv = 2-qubit unitary across neighbours (weight sharing)","quantum pool = measure + conditioned rotation","O(log n) parameters, resists barren plateaus","native use: quantum states / phases of matter"])
add(id="hybrid",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="The hybrid sandwich — the pattern to remember",
    img={"f":"hybrid_sandwich.png","side":"right"},
    brief="Verbose: every practical near-term quantum vision system is one sandwich — a classical image, then an encode step, then a quantum layer (quanvolution or a QCNN block), then a measure step, then a classical CNN head, then the label; the quantum slice buys a feature space, the classical slices do the heavy lifting of loading the data and making the decision; this hybridity is the honest, runnable-today shape of quantum computer vision, and it is exactly what the notebook implements.")
add(id="ownwork",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="From the speaker's own work — classical CNN to a measured NISQ wall",
    img={"f":"qft_hardware.png","side":"right"},
    brief="Verbose first-person-in-third-person (strict third person): Srivastava co-authored a 2022 paper (J. Phys.: Conf. Ser. 2161, 012038, IOP) that built a real computer-vision pipeline — face detection, eye-region segmentation on the Columbia Gaze dataset, and a five-layer CNN (batch-norm, ReLU, dropout) for eye-contact detection in an autism-therapy application; the paper then reached to the quantum frontier: it argued N classical bits encode in log-base-2 of N qubits (the amplitude-encoding claim, first-hand) and ran a Quantum Fourier Transform — the crucial step of Quantum Visual Tracking — on real IBM hardware; the measured result: a three-qubit input state |5⟩ returned the 010 outcome with probability 0.688, matching theory, with error growing as circuit depth grows. Land it: this is a first-hand NISQ-noise result, and Quantum Visual Tracking is the natural step past quanvolution — the direction Srivastava's research points.",
    must=["2022 paper: 5-layer CNN eye-contact pipeline (Columbia Gaze)","QFT on real IBM hardware: input |5⟩ → 010 at probability 0.688","error grows with circuit depth — a first-hand NISQ wall"])
add(id="reality1",kind="textimg",sec=3,kicker="Section 3 · Quantum Vision",title="Reality check — no advantage on natural images yet",
    img={"f":"advantage_quadrant.png","side":"right"},
    brief="Verbose honest: say it plainly — on MNIST and CIFAR, well-tuned classical CNNs still win on accuracy-per-effort, and quanvolution's reported gains are modest and setting-dependent (the original 2019 paper found its quantum random circuit statistically indistinguishable from a classical random transform); a 2026 result even proved the common trainable-QCNN image benchmarks are classically simulable; the encoding cost can eat any speedup (loading a megapixel image hits the same QRAM bottleneck as any quantum ML); NISQ noise plus shot noise mean expectation values need many measurements, and today's qubits are few and noisy, so demos run in simulation or on tiny patches; faculty respect this candor.",
    must=["classical CNNs still win on natural images (MNIST/CIFAR) in 2026","2026: common trainable-QCNN image benchmarks proven classically simulable","encoding/QRAM cost + NISQ noise cap real demos at tiny images"])
add(id="reality2",kind="cards",sec=3,kicker="Section 3 · Quantum Vision",title="Where the quantum-vision advantage is genuine",
    cards=[{"title":"Quantum-native data","accent":"teal"},{"title":"Rich features, few parameters","accent":"blue"},{"title":"The honest one-liner","accent":"purple"}],
    brief="Cards verbose: (1) Quantum-native data — states from sensors, chemistry and physics experiments, where a QCNN classifies phases with no classical encoding needed, and structured or scientific imaging where a quantum kernel is provably hard to simulate. (2) Rich features from few parameters — a QCNN's about-log-n parameter count is attractive for data-scarce scientific domains and mitigates barren plateaus that limit naive deep variational vision circuits. (3) The honest one-liner: quantum-enhanced vision today will not beat a ResNet on a webcam — teach it as the front-end feature extractor of the future, running hybrid with the classical vision faculty already know.")

# ---------------- §4 INDUSTRY + APPLICATIONS ----------------
add(id="d4",kind="divider",sec=4,num="04",title="Industry & Applications",accent="magenta",
    summary="Where quantum-enhanced vision is being tried now — clinics, satellites, factories, and the biggest cameras ever built.")
add(id="turning",kind="stats",sec=4,kicker="Section 4 · Industry & Applications",title="2025–26: from lab curiosity to commercial pilots",
    stats=[{"num":"300+","label":"enterprises now engaged in quantum (McKinsey 2026)","accent":"blue"},
           {"num":"6.3×","label":"jump in start-up investment 2024→2025","accent":"teal"},
           {"num":"~90%","label":"of that investment to quantum computing","accent":"purple"},
           {"num":"$4.4B","label":"projected QC revenue by 2028","accent":"magenta"}],
    brief="Verbose: the discourse shifted from 'if' to modelling 'when' quantum touches each sector; for vision the common pattern is high-dimensional image data where a richer feature space or a hybrid quantum front-end is worth testing; healthcare imaging, earth observation and manufacturing are the vanguard, and mega-science runs the hardest versions. Refresh numbers from deep research where available.")
add(id="medical",kind="cards",sec=4,kicker="Section 4 · Industry & Applications",title="Medical imaging — the highest-value target",
    cards=[{"title":"Radiology & pathology","accent":"blue"},{"title":"Quantum-enhanced classifiers","accent":"teal"},{"title":"Data-scarce advantage","accent":"purple"}],
    brief="Cards verbose, grounded by deep research. Radiology & pathology: CNNs already read X-rays, CT, MRI and histopathology slides; these are exactly the high-stakes images where richer features and data efficiency matter. Quantum-enhanced classifiers: hybrid quantum-classical models and quantum kernels have been tested on medical-image tasks (report any cited accuracy at parity). Data-scarce advantage: medical datasets are small and expensive to label — the regime where a few-parameter quantum feature extractor is most defensible; be honest that results are early and mostly at parity.")
add(id="remote",kind="textimg",sec=4,kicker="Section 4 · Industry & Applications",title="Earth observation — satellites make more images than anyone can label",
    img={"f":"remote_sensing.png","side":"right"},
    brief="Verbose, grounded by deep research: satellites and radio telescopes generate torrents of unlabelled imagery; quantum machine learning has been tested for land-use and scene classification on benchmark satellite datasets (e.g. EuroSAT) and by space agencies exploring quantum image classification; report any cited accuracy (typically at parity with classical today). Frame it as a natural fit — huge unlabelled image streams, and a hybrid quantum front-end that can be studied now in simulation.",
    must=["EuroSAT / land-use scene classification is a common quantum-ML image benchmark","space agencies (e.g. ESA) explore quantum image classification","results largely at parity with classical today"])
add(id="industry2",kind="cards",sec=4,kicker="Section 4 · Industry & Applications",title="Factories, roads and the companies building it",
    cards=[{"title":"Manufacturing defect detection","accent":"teal"},{"title":"Autonomous perception","accent":"blue"},{"title":"Who is building it","accent":"magenta"}],
    brief="Cards verbose, grounded by deep research. Manufacturing: visual inspection for defects on production lines is a bounded, high-value vision task where hybrid quantum-classical pilots have been reported. Autonomous perception: object detection and segmentation for driving and robotics are compute-bound, another stated target for quantum-enhanced feature extraction. Who is building it: name real players from research (e.g. IBM Qiskit, NVIDIA CUDA-Q for hybrid QML, and quantum-software firms such as Terra Quantum / Multiverse) — keep it honest about pilot-stage maturity.")
add(id="qimage",kind="textimg",sec=4,kicker="Section 4 · Industry & Applications",title="Quantum image processing — encoding pictures as quantum states",
    img={"f":"qimage.png","side":"right"},
    brief="Verbose, grounded by deep research: beyond quanvolution, a research line represents whole images directly as quantum states — schemes called FRQI (Flexible Representation of Quantum Images) and NEQR (Novel Enhanced Quantum Representation) store pixel positions and intensities in qubits, enabling quantum edge detection and image operations in principle; explain plainly what they do and be candid that they hit the same loading and NISQ walls, so demonstrations use tiny images. Define FRQI and NEQR in the KEY TERMS box.",
    must=["FRQI: 2ⁿ×2ⁿ image in 2n+1 qubits (colour in an amplitude/angle)","NEQR: 2n+q qubits (colour in a basis register; exact readout)","limited today by loading cost + NISQ noise → tiny images"])
add(id="megaintro",kind="statement",sec=4,accent="ink",title="The biggest cameras ever built are unsupervised-vision machines.",
    img={"f":"data_deluge.png","side":"right"},
    brief="Verbose (white text on dark): the largest scientific instruments are, in effect, enormous cameras — the LHC photographs particle collisions, DUNE builds three-dimensional images of neutrino tracks in liquid argon, the SKA images the radio sky, LIGO reads a four-kilometre ruler; all of it is extreme-dimensional, mostly unlabelled image data — CNN, clustering and unsupervised-representation territory, and the hardest proving ground for quantum-enhanced vision.")
add(id="megasci",kind="cards",sec=4,kicker="Section 4 · Mega-Science",title="Vision at the frontier of physics",
    cards=[{"title":"LIGO — glitch images","accent":"blue"},{"title":"CERN / LHC — collision images","accent":"teal"},{"title":"DUNE — 3-D neutrino images","accent":"purple"}],
    brief="Cards verbose. LIGO: Gravity Spy turns detector noise into spectrogram images and a CNN sorts them into 23 glitch classes with tens of thousands of citizen scientists (image classification at scale), and quantum anomaly-detection ideas are being explored on the readout. CERN/LHC: collision events are images of particle tracks; convolutional and graph networks reconstruct them, and CERN's Quantum Technology Initiative has shown a quantum anomaly-detection regime that outperformed classical on real hardware in the LHC latent space (Commun. Phys. 2024). DUNE: each neutrino interaction is a 3-D image in liquid argon, reconstructed by CNNs and graph nets, with quantum kernels and QCNNs tested to classify track versus shower on IBM hardware at parity.")
add(id="sensing",kind="textimg",sec=4,kicker="Section 4 · Mega-Science",title="Quantum sensing — a new class of imaging instruments",
    img={"f":"sensing_sensitivity.png","side":"right"},
    brief="Verbose: quantum sensing creates imaging that classical instruments cannot reach — sub-shot-noise and quantum-illumination microscopy, ghost imaging, NV-diamond magnetic imaging, and squeezed-light readout that already sharpens LIGO; each of these is a new source of ultra-precise, mostly-unlabelled image streams that themselves become machine-learning problems; land that quantum touches vision from both ends — new cameras and new feature extractors.")
add(id="megasyn",kind="statement",sec=4,accent="deep",title="Mega-science pattern: extreme unlabelled imagery = machine vision's home turf.",
    brief="Verbose (dark): the largest experiments emit extreme-dimensional, mostly-unlabelled image data — machine vision's home turf; quantum helps from both ends, as a feature extractor or kernel embedding the images (mostly at parity today, with a genuine unsupervised win reported by CERN) and as a new class of quantum sensors that generate images no classical instrument can; honest caveat: most quantum-ML vision results are at parity, not yet superior — the value today is teaching the pattern and being ready.")

# ---------------- §5 INDIA ----------------
add(id="d5",kind="divider",sec=5,num="05",title="The Indian Landscape",accent="deep",
    summary="India is building the hardware and holds a vast imaging-data footprint. This room builds the people who will use both.")
add(id="nqm1",kind="textimg",sec=5,kicker="Section 5 · India",title="The National Quantum Mission",
    img={"f":"nqm_targets.png","side":"right"},
    brief="Verbose: Rs 6,003.65 crore approved 19 Apr 2023, running 2023–2031 (about $0.73B); staged compute targets of 20–50 qubits by year three, 50–100 by year five, and 50–1000 by year eight, on superconducting and photonic platforms; 152 researchers across 43 institutions in 17 states — a national footprint relevant to every college in the room.")
add(id="nqm2",kind="cards",sec=5,kicker="Section 5 · India",title="Four thematic hubs — hub-and-spoke",
    cards=[{"title":"Computing — IISc Bengaluru","accent":"blue"},{"title":"Communication — IIT Madras + C-DOT","accent":"teal"},{"title":"Sensing & Metrology — IIT Bombay","accent":"purple"},{"title":"Materials & Devices — IIT Delhi","accent":"magenta"}],
    brief="Each hub card 2-3 verbose lines on its mandate (indigenous processors and the 20-to-1000 qubit targets; secure quantum communication and satellite links; magnetometers, atomic clocks and quantum imaging/sensing — directly relevant to vision; qubit materials and cryogenic devices). Note each is a Section-8 company, operational since Oct 2024.")
add(id="eco",kind="cards",sec=5,kicker="Section 5 · India",title="Indigenous ecosystem — shipping, not slideware",
    cards=[{"title":"QpiAI (Bengaluru)","accent":"blue"},{"title":"Amaravati Quantum Valley","accent":"teal"},{"title":"Academic + startups","accent":"purple"}],
    brief="Cards verbose. QpiAI: Indus 25-qubit (Apr 2025), Kaveri 64-qubit (Nov 2025, commercial late 2026), $65.6M raised, roadmap to 1000 qubits by 2030. Amaravati Quantum Valley: launched 7 Feb 2026 (IBM + TCS + Andhra Pradesh), an IBM Quantum System Two with a 156-qubit Heron processor — India's largest — commissioning about Sept 2026, L&T infrastructure. Academic and startups: IISER Pune 20-qubit ion-trap by end-2026, a national post-quantum-cryptography roadmap (Feb 2026), and a growing startup base (QNu Labs, Dimira, Quanastra, Prenishq and more).")
add(id="funding",kind="textimg",sec=5,kicker="Section 5 · India",title="The honest funding number — and India's real edge",
    img={"f":"funding_bars.png","side":"left"},
    brief="Verbose: India's about $0.73B over eight years sits against China's roughly $15B, the US at $2.5B and more, the UK's £2.5B over ten years and Germany's €2–3B; India is funded to compete selectively, not to outspend anyone; its edge is algorithms, software and a vast talent pool — the value-capturing layer — which is exactly what quantum machine learning and quantum-enhanced vision are; faculty respect the candor.")
add(id="viksit",kind="textimg",sec=5,kicker="Section 5 · India",title="Quantum vision and Viksit Bharat 2047",
    img={"f":None,"side":"right"},cards=[{"title":"India's imaging-data advantage","accent":"deep"}],
    brief="Verbose left column: Viksit Bharat @ 2047 is the goal of a fully developed India by the centenary; India already took Aadhaar, UPI and Digital India to population scale, proving it can run frontier technology at planet scale; a coordinated deep-tech stack (NQM, IndiaAI, Semicon India, the ANRF one-lakh-crore RDI fund) aims to move India from the world's back office to an innovation engine; sovereignty means indigenous hardware and secure systems, not renting foreign quantum cloud. Card 'India's imaging-data advantage': India's strengths in IT services plus an enormous imaging footprint — healthcare (population-scale screening), agriculture (crop and soil imaging), and earth observation (ISRO's remote-sensing archives) — make hybrid quantum-classical vision a natural applied bet, if the talent exists; every faculty member is a lever; Viksit Bharat 2047 will be built by the cohort in the room's classrooms right now.")

# ---------------- §6 FUTURE ----------------
add(id="d6",kind="divider",sec=6,num="06",title="The Future",accent="ink",
    summary="Convolution to quanvolution is a first-principles story — and the bottleneck is people who can teach it. Faculty are the lever.")
add(id="future1",kind="cards",sec=6,kicker="Section 6 · The Future",title="Where quantum vision goes next",
    cards=[{"title":"Fault-tolerance & scale","accent":"blue"},{"title":"AI × Quantum","accent":"teal"},{"title":"Quantum Visual Tracking","accent":"purple"}],
    brief="Cards verbose. Fault-tolerance & scale: IBM Starling by 2029 (200 logical qubits), Google's useful error-corrected machine around 2029, PsiQuantum's photonic million-qubit ambition — as qubits grow and error falls, amplitude-encoding whole images and deeper vision circuits become feasible. AI × Quantum: neural decoders like DeepMind's AlphaQubit already improve quantum error correction, and trainable quanvolution / quantum attention are active research merging the two fields. Quantum Visual Tracking: the natural step past quanvolution — tracking objects that exist in superposition, the direction the speaker's own quantum-vision research points; today it is a research horizon, honestly labelled as such.")
add(id="talent2",kind="textimg",sec=6,kicker="Section 6 · The Future",title="The bottleneck is people — faculty are the lever",
    img={"f":"talent_gap.png","side":"left"},cards=[{"title":"Call to action for faculty","accent":"blue"}],
    brief="Verbose: the single largest global bottleneck is people who understand this stack; about 250k roles by 2030 and 840k by 2035 against a tiny qualified supply; every course seeded and student pointed at quantum machine learning is India's comparative advantage compounding. Card 'Call to action for faculty': convolution to quanvolution is teachable from first principles with no hardware; add one quanvolution notebook to a deep-learning or computer-vision elective; frame quantum vision honestly as a front-end feature extractor, not a magic accuracy boost; use the notebook (any laptop, CPU only); and route strong students to NQM hubs and quantum-vision research.")
add(id="thanks",kind="thanks",sec=6,title="Thank you.",
    brief="Verbose closing line + contact block: Archit Srivastava, Founder AiQyaM; email architsrivastava3115@gmail.com; Google Scholar NbPUdWMAAAAJ; the notebook runs on any laptop; invite collaboration on quantum visual tracking and bringing students to the next cohort.")

out=os.path.join(os.path.dirname(__file__),"skeleton2.json")
json.dump(S,open(out,"w"),indent=1,ensure_ascii=False)
print(f"wrote {out}  ({len(S)} slides)")
for sec in range(7):
    print(f"  sec {sec}: {sum(1 for s in S if s['sec']==sec)} slides")
