#!/usr/bin/env python3
"""Create + RUN a real PennyLane quantum-kernel clustering notebook, capture authentic
Jupyter-style cell screenshots (code + real output), and write the runnable .ipynb."""
import os, io, sys, contextlib, textwrap
import numpy as _np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

ROOT="/Users/sentry/Work/Lectures"
GEN=os.path.join(ROOT,"NIT Warangal","assets_generated")
NBDIR=os.path.join(ROOT,"NIT Warangal","notebooks")
FONTS=os.path.join(ROOT,"fonts")
os.makedirs(GEN,exist_ok=True); os.makedirs(NBDIR,exist_ok=True)
BLUE=(15,98,254); TEAL=(0,157,154); INK=(22,22,22); GRAY=(111,111,111)
MONO=os.path.join(FONTS,"IBMPlexMono-Regular.ttf"); MONOB=os.path.join(FONTS,"IBMPlexMono-Medium.ttf")

# ---------------- the notebook cells (real, runnable) ----------------
CELLS=[
('''# Quantum-kernel clustering on two interleaved moons — 2 qubits, laptop CPU
import pennylane as qml
from pennylane import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt

X, y = make_moons(n_samples=120, noise=0.12, random_state=7)
X = (X - X.mean(0)) / X.std(0)          # standardise; y is kept ONLY to score, never used to cluster
plt.figure(figsize=(4,3)); plt.scatter(X[:,0], X[:,1], c="#6f6f6f", s=14)
plt.title("120 unlabelled points — two moons"); plt.xticks([]); plt.yticks([]); plt.show()
print("data:", X.shape, "-> the model must find the two crescents with NO labels")''', "fig"),

('''n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

def feature_map(x, scale=0.7):
    "Angle-encode the 2-D point into a 2-qubit state (2 layers)."
    for _ in range(2):
        qml.RY(scale * x[0], wires=0)
        qml.RY(scale * x[1], wires=1)
        qml.CNOT(wires=[0, 1])
        qml.RY(scale * x[1], wires=0)
        qml.RY(scale * x[0], wires=1)
        qml.CNOT(wires=[0, 1])

@qml.qnode(dev)
def overlap(x1, x2):
    feature_map(x1)
    qml.adjoint(feature_map)(x2)      # U(x1) then U(x2)^dagger
    return qml.probs(wires=range(n_qubits))

def kernel(x1, x2):
    return overlap(x1, x2)[0]         # |<phi(x1)|phi(x2)>|^2

print("k(x0, x0) =", round(float(kernel(X[0], X[0])), 3), "(a point with itself -> 1.0)")
print("k(x0, x5) =", round(float(kernel(X[0], X[5])), 3),
      " k(x0, x60) =", round(float(kernel(X[0], X[60])), 3), "(two other pairs)")''', "text"),

('''# Build the full quantum kernel (Gram) matrix K[i,j] = |<phi(xi)|phi(xj)>|^2
K = np.array([[kernel(a, b) for b in X] for a in X])
plt.figure(figsize=(4,3.4)); plt.imshow(K, cmap="viridis"); plt.colorbar(label="similarity")
plt.title("Quantum kernel matrix K"); plt.xticks([]); plt.yticks([]); plt.show()
print("K shape:", K.shape, "-> a physically-computed similarity for every pair of points")''', "fig"),

('''# Spectral clustering wants a LOCAL graph, so from the quantum kernel keep
# each point's 14 most-similar neighbours, then symmetrise the matrix.
import numpy as onp
def knn_graph(K, k=14):
    A = onp.zeros_like(K)
    for i in range(len(K)):
        for j in onp.argsort(-K[i])[:k + 1]:
            A[i, j] = K[i, j]
    return onp.maximum(A, A.T)

affinity = knn_graph(K, k=14)
km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X)
sp = SpectralClustering(n_clusters=2, affinity="precomputed",
                        assign_labels="discretize", random_state=0).fit(affinity)
ari_k = adjusted_rand_score(y, km.labels_)
ari_q = adjusted_rand_score(y, sp.labels_)

fig, ax = plt.subplots(1, 2, figsize=(7, 3))
ax[0].scatter(X[:,0], X[:,1], c=km.labels_, cmap="coolwarm", s=14)
ax[0].set_title(f"k-means   ARI = {ari_k:.2f}")
ax[1].scatter(X[:,0], X[:,1], c=sp.labels_, cmap="winter", s=14)
ax[1].set_title(f"quantum kernel   ARI = {ari_q:.2f}")
for a in ax: a.set_xticks([]); a.set_yticks([])
plt.show()
print(f"classical k-means ARI        = {ari_k:.2f}   (cuts through the crescents)")
print(f"quantum-kernel spectral ARI  = {ari_q:.2f}   (recovers the two moons)")''', "both"),
]

# ---------------- execute cells, capture outputs ----------------
ns={}
outputs=[]   # (kind, payload)  kind in fig/text/both
for i,(code,ok) in enumerate(CELLS,1):
    buf=io.StringIO()
    figpath=os.path.join(GEN,f"_nbout{i}.png")
    with contextlib.redirect_stdout(buf):
        exec(compile(code,f"<cell{i}>","exec"), ns)
    fig=None
    if plt.get_fignums():
        f=plt.gcf(); f.savefig(figpath,dpi=150,bbox_inches="tight",facecolor="white"); plt.close("all"); fig=figpath
    outputs.append((buf.getvalue().rstrip(), fig))
    print(f"cell {i} ran. stdout={buf.getvalue().strip()[:60]!r} fig={'yes' if fig else 'no'}")

# ---------------- compose Jupyter-style cell screenshots ----------------
def font(path,size):
    try: return ImageFont.truetype(path,size)
    except Exception: return ImageFont.load_default()
fm=font(MONO,23); fmb=font(MONOB,23); flab=font(MONOB,23)
W=1580; PAD=32; LH=34
def measure(draw,txt,f):
    b=draw.textbbox((0,0),txt,font=f); return b[2]-b[0],b[3]-b[1]

def render_cell(idx, code, out_text, out_fig):
    lines=code.split("\n")
    code_h=PAD*2 + LH*len(lines)
    # output image scaled
    out_im=None; out_h=0
    if out_fig:
        out_im=Image.open(out_fig).convert("RGB")
        scale=min(1.0,(W-2*PAD-120)/out_im.width);
        out_im=out_im.resize((int(out_im.width*scale),int(out_im.height*scale)))
        out_h+=out_im.height+24
    tlines=out_text.split("\n") if out_text else []
    out_h+= (len(tlines)*32+20) if tlines else 0
    if out_h: out_h+=PAD+40
    H=code_h+out_h+20
    img=Image.new("RGB",(W,H),(255,255,255)); d=ImageDraw.Draw(img)
    # code area bg (light gray, jupyter input)
    d.rectangle([90,16,W-16,code_h-4],fill=(246,246,246),outline=(226,226,226))
    d.rectangle([16,16,84,code_h-4],fill=(255,255,255))
    d.text((18,PAD-4),f"In [{idx}]:",font=flab,fill=BLUE)
    d.rectangle([90,16,96,code_h-4],fill=BLUE)
    y=PAD
    for ln in lines:
        col=(120,120,120) if ln.strip().startswith("#") or ln.strip().startswith('"') else INK
        d.text((110,y),ln.replace("\t","    "),font=fm,fill=col); y+=LH
    # output
    if out_h:
        yo=code_h+10
        d.text((18,yo+6),f"Out[{idx}]:",font=flab,fill=(178,86,0))
        if out_im is not None:
            img.paste(out_im,(110,yo)); yo+=out_im.height+18
        for tl in tlines:
            d.text((110,yo),tl,font=fm,fill=(38,38,38)); yo+=32
    p=os.path.join(GEN,f"nb_cell{idx}.png"); img.save(p); print("wrote",p); return p

for i,((code,ok),(otext,ofig)) in enumerate(zip(CELLS,outputs),1):
    render_cell(i, code, otext, ofig)

# ---------------- write the runnable .ipynb ----------------
try:
    import nbformat
    from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
    nb=new_notebook()
    nb.cells.append(new_markdown_cell("# Quantum-kernel clustering demo (Session 1 · QML-2026)\n"
        "A 2-qubit PennyLane quantum kernel fed to spectral clustering, on two interleaved moons. "
        "Runs on a laptop CPU — no quantum hardware. `pip install pennylane scikit-learn matplotlib`."))
    for code,_ in CELLS: nb.cells.append(new_code_cell(code))
    nbformat.write(nb, os.path.join(NBDIR,"qml_clustering_demo.ipynb"))
    print("wrote qml_clustering_demo.ipynb")
except Exception as e:
    print("ipynb write skipped:", e)

# clean temp fig files
for i in range(1,len(CELLS)+1):
    t=os.path.join(GEN,f"_nbout{i}.png")
    if os.path.exists(t): os.remove(t)
print("DONE")
