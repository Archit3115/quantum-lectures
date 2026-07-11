#!/usr/bin/env python3
"""Create + RUN the real PennyLane quanvolution vision demo, capture authentic Jupyter-style
cell screenshots (code + real output) → ../assets_generated/nbv_cell{1..4}.png. Session 2."""
import os, io, contextlib
import numpy as _np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

ROOT="/Users/sentry/Work/Lectures"
GEN=os.path.join(ROOT,"NIT Warangal","assets_generated")
NBDIR=os.path.join(ROOT,"NIT Warangal","notebooks")
FONTS=os.path.join(ROOT,"fonts")
os.makedirs(GEN,exist_ok=True); os.makedirs(NBDIR,exist_ok=True)
BLUE=(15,98,254); INK=(22,22,22)
MONO=os.path.join(FONTS,"IBMPlexMono-Regular.ttf"); MONOB=os.path.join(FONTS,"IBMPlexMono-Medium.ttf")

# ---------------- the notebook cells (real, runnable) ----------------
CELLS=[
('''# Quanvolution on handwritten digits — 4 qubits, laptop CPU, no hardware
import pennylane as qml
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

d = load_digits()
images = d.images / 16.0          # 8x8 greyscale, scaled to 0..1 so pixels become rotation angles
y = d.target                      # labels kept ONLY to score the classifier at the end
fig, ax = plt.subplots(1, 6, figsize=(7, 1.5))
for i in range(6):
    ax[i].imshow(images[i], cmap="gray_r"); ax[i].set_title(str(y[i])); ax[i].axis("off")
plt.show()
print("images:", images.shape, "-> each digit is 8x8 = 64 numbers")''', "fig"),

('''n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)
rng = np.random.default_rng(0)
rand_w = rng.uniform(0, 2*np.pi, size=(2, n_qubits))   # fixed, UNTRAINED random weights

@qml.qnode(dev)
def circuit(phi):
    for j in range(4):
        qml.RY(np.pi * phi[j], wires=j)                # angle-encode the four 2x2 pixels
    qml.templates.RandomLayers(rand_w, wires=[0,1,2,3], seed=0)   # entangle / mix
    return [qml.expval(qml.PauliZ(j)) for j in range(4)]          # 4 channels

patch = [images[0][0,0], images[0][0,1], images[0][1,0], images[0][1,1]]
print("one 2x2 patch ->", np.round(circuit(patch), 3))
print("the circuit is UNTRAINED: this is raw representational power, zero learning")''', "text"),

('''def quanv(img):                    # slide the 2x2 window with stride 2: 8x8 -> 4x4x4
    out = np.zeros((4, 4, 4))
    for r in range(0, 8, 2):
        for c in range(0, 8, 2):
            q = circuit([img[r,c], img[r,c+1], img[r+1,c], img[r+1,c+1]])
            out[r//2, c//2, :] = q
    return out

fig, ax = plt.subplots(2, 5, figsize=(7, 3))
for row, idx in enumerate([0, 13]):
    fm = quanv(images[idx])
    ax[row,0].imshow(images[idx], cmap="gray_r"); ax[row,0].set_ylabel(f"'{y[idx]}'")
    for ch in range(4): ax[row,ch+1].imshow(fm[:,:,ch], cmap="viridis")
    for c in range(5): ax[row,c].set_xticks([]); ax[row,c].set_yticks([])
for c,t in enumerate(["input","ch1","ch2","ch3","ch4"]): ax[0,c].set_title(t)
plt.show()
print("each 2x2 patch -> 4 quantum channels; the maps stay structured")''', "fig"),

('''# Honest benchmark: same simple classifier on raw pixels vs untrained quanvolution features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

N = 600
Q = np.array([quanv(im) for im in images[:N]])         # ~40 ms/image in simulation
def score(X):
    Xtr,Xte,ytr,yte = train_test_split(X, y[:N], test_size=0.3, random_state=42, stratify=y[:N])
    sc = StandardScaler().fit(Xtr)
    return LogisticRegression(max_iter=2000).fit(sc.transform(Xtr), ytr).score(sc.transform(Xte), yte)

acc_raw = score(images[:N].reshape(N, -1))
acc_q   = score(Q.reshape(N, -1))
plt.figure(figsize=(3.4,3))
plt.bar(["raw","quanv"], [acc_raw, acc_q], color=["#6f6f6f","#a56eff"]); plt.ylim(0,1.05)
plt.title("test accuracy"); plt.show()
print(f"raw pixels               = {acc_raw:.3f}")
print(f"untrained quanvolution   = {acc_q:.3f}  (preserves ~{acc_q*100:.0f}% of the signal)")''', "both"),
]

# ---------------- execute cells, capture outputs ----------------
ns={}; outputs=[]
for i,(code,ok) in enumerate(CELLS,1):
    buf=io.StringIO(); figpath=os.path.join(GEN,f"_nbvout{i}.png")
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
fm=font(MONO,23); flab=font(MONOB,23)
W=1580; PAD=32; LH=34

def render_cell(idx, code, out_text, out_fig):
    lines=code.split("\n"); code_h=PAD*2 + LH*len(lines)
    out_im=None; out_h=0
    if out_fig:
        out_im=Image.open(out_fig).convert("RGB")
        scale=min(1.0,(W-2*PAD-120)/out_im.width)
        out_im=out_im.resize((int(out_im.width*scale),int(out_im.height*scale))); out_h+=out_im.height+24
    tlines=out_text.split("\n") if out_text else []
    out_h+= (len(tlines)*32+20) if tlines else 0
    if out_h: out_h+=PAD+40
    H=code_h+out_h+20
    img=Image.new("RGB",(W,H),(255,255,255)); dd=ImageDraw.Draw(img)
    dd.rectangle([90,16,W-16,code_h-4],fill=(246,246,246),outline=(226,226,226))
    dd.rectangle([16,16,84,code_h-4],fill=(255,255,255))
    dd.text((18,PAD-4),f"In [{idx}]:",font=flab,fill=BLUE)
    dd.rectangle([90,16,96,code_h-4],fill=BLUE)
    y=PAD
    for ln in lines:
        col=(120,120,120) if ln.strip().startswith("#") else INK
        dd.text((110,y),ln.replace("\t","    "),font=fm,fill=col); y+=LH
    if out_h:
        yo=code_h+10
        dd.text((18,yo+6),f"Out[{idx}]:",font=flab,fill=(178,86,0))
        if out_im is not None: img.paste(out_im,(110,yo)); yo+=out_im.height+18
        for tl in tlines: dd.text((110,yo),tl,font=fm,fill=(38,38,38)); yo+=32
    p=os.path.join(GEN,f"nbv_cell{idx}.png"); img.save(p); print("wrote",p)

for i,((code,ok),(otext,ofig)) in enumerate(zip(CELLS,outputs),1):
    render_cell(i, code, otext, ofig)

for i in range(1,len(CELLS)+1):
    t=os.path.join(GEN,f"_nbvout{i}.png")
    if os.path.exists(t): os.remove(t)
print("DONE")
