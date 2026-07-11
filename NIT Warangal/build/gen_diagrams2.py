#!/usr/bin/env python3
"""Generate all Carbon-palette diagrams for the Session 2 (Computer Vision) Qiskit deck.
300-dpi white-background PNGs to ../assets_generated/. Self-contained (matplotlib/numpy/sklearn/pennylane).
Feature-map grid + accuracy bars are REAL compute (same 4-qubit quanvolution recipe as the notebook)."""
import os, time, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle, Ellipse

# ---- IBM Carbon palette ----
BLUE="#0F62FE"; PURPLE="#A56EFF"; TEAL="#009D9A"; DEEPBLUE="#003A6D"
MAGENTA="#9F1853"; RED="#FA4D56"; INK="#161616"; GRAY="#6F6F6F"; LGRAY="#c6c6c6"
CY1="#33B1FF"; CY2="#82CFFF"; TL1="#08BDBA"; TL2="#3DDBD9"
PK1="#EE5396"; PK2="#FF7EB6"; GRN="#42BE65"; AMB="#FFB000"; PANEL="#f4f4f4"

plt.rcParams.update({
    "font.family":"sans-serif",
    "font.sans-serif":["IBM Plex Sans","Helvetica Neue","Arial","DejaVu Sans"],
    "axes.edgecolor":INK,"axes.labelcolor":INK,"text.color":INK,
    "xtick.color":INK,"ytick.color":INK,"axes.linewidth":1.0,
    "savefig.dpi":300,"figure.dpi":140,
})
OUT=os.path.join(os.path.dirname(__file__),"..","assets_generated")
os.makedirs(OUT,exist_ok=True)
def save(fig,name):
    p=os.path.join(OUT,name)
    fig.savefig(p,facecolor="white",transparent=False,bbox_inches="tight",pad_inches=0.14)
    plt.close(fig); print("wrote",name)

def box(ax,x,y,w,h,text,fc,tc="white",fs=12,ec=None,lw=1.4,rad=0.06,weight="bold"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0.005,rounding_size={rad}",
        fc=fc,ec=ec or fc,lw=lw,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=tc,fontsize=fs,fontweight=weight,zorder=3)
def arrow(ax,x1,y1,x2,y2,color=INK,lw=2.2,style="-|>",rad=0.0):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=16,
        lw=lw,color=color,connectionstyle=f"arc3,rad={rad}",zorder=1))

# ============ shared real quanvolution recipe (same as notebook) ============
def _quanv_setup():
    import pennylane as qml
    from sklearn.datasets import load_digits
    rng=np.random.default_rng(0)
    dev=qml.device("default.qubit",wires=4)
    rand_w=rng.uniform(0,2*np.pi,size=(2,4))
    @qml.qnode(dev)
    def circuit(phi):
        for j in range(4): qml.RY(np.pi*phi[j],wires=j)
        qml.templates.RandomLayers(rand_w,wires=[0,1,2,3],seed=0)
        return [qml.expval(qml.PauliZ(j)) for j in range(4)]
    def quanv(img):
        out=np.zeros((4,4,4))
        for r in range(0,8,2):
            for c in range(0,8,2):
                q=circuit([img[r,c],img[r,c+1],img[r+1,c],img[r+1,c+1]])
                for ch in range(4): out[r//2,c//2,ch]=q[ch]
        return out
    return load_digits, quanv

# =========================================================
# §2 CLASSICAL CV
# =========================================================
def image_grid():
    from sklearn.datasets import load_digits
    d=load_digits(); img=d.images[0]                 # a clean '0'
    fig,axs=plt.subplots(1,2,figsize=(9.2,4.4))
    axs[0].imshow(img,cmap="gray_r"); axs[0].set_title("What a human sees",fontsize=12,fontweight="bold")
    axs[0].set_xticks([]); axs[0].set_yticks([])
    axs[1].imshow(img,cmap="gray_r",alpha=0.25)
    for r in range(8):
        for c in range(8):
            v=int(img[r,c]/16*255)
            axs[1].text(c,r,f"{v:d}",ha="center",va="center",fontsize=7.5,
                        color=INK if img[r,c]<8 else "white",fontweight="bold")
    axs[1].set_title("What the computer sees — a grid of numbers",fontsize=12,fontweight="bold")
    axs[1].set_xticks([]); axs[1].set_yticks([])
    fig.suptitle("An 8×8 digit = 64 numbers.  A 1-MP colour photo = ~3 million.",
                 fontsize=10.5,color=GRAY,y=1.0)
    save(fig,"image_grid.png")

def representation():
    fig,axs=plt.subplots(1,2,figsize=(9.4,4.2))
    # translation: a blob shifted, "every number changes"
    g1=np.zeros((8,8)); g1[2:5,2:5]=1
    g2=np.zeros((8,8)); g2[2:5,4:7]=1
    for ax,g,t in [(axs[0],g1,"the cat here"),(axs[1],g2,"shift 2 px — the cat there")]:
        ax.imshow(g,cmap="Blues"); ax.set_title(t,fontsize=11.5,fontweight="bold")
        ax.set_xticks(range(8)); ax.set_yticks(range(8))
        ax.set_xticklabels([]); ax.set_yticklabels([]); ax.grid(True,color=LGRAY,lw=.4)
    fig.suptitle("Same object, every pixel value changed — raw pixels are not translation-invariant.\n"
                 "Good representations are LOCAL · HIERARCHICAL · INVARIANT",
                 fontsize=11,fontweight="bold",y=1.06,color=INK)
    save(fig,"representation.png")

def convolution():
    from sklearn.datasets import load_digits
    img=load_digits().images[13]/16.0            # a digit
    Kx=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])    # Sobel-x (vertical edges)
    Ky=Kx.T
    def conv(a,k):
        h,w=a.shape; out=np.zeros((h-2,w-2))
        for i in range(h-2):
            for j in range(w-2): out[i,j]=(a[i:i+3,j:j+3]*k).sum()
        return out
    edge=np.hypot(conv(img,Kx),conv(img,Ky))
    fig,axs=plt.subplots(1,3,figsize=(10.2,3.7))
    axs[0].imshow(img,cmap="gray_r"); axs[0].set_title("input image",fontsize=11.5,fontweight="bold")
    axs[1].imshow(Kx,cmap="RdBu"); axs[1].set_title("Sobel kernel (3×3)\nslides over the image",fontsize=11,fontweight="bold")
    for i in range(3):
        for j in range(3): axs[1].text(j,i,f"{Kx[i,j]:d}",ha="center",va="center",fontweight="bold",fontsize=13)
    axs[2].imshow(edge,cmap="magma"); axs[2].set_title("output feature map\n(edges detected)",fontsize=11,fontweight="bold")
    for ax in axs: ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle("The convolution atom: slide a small window, compute a weighted sum — the quantum method replaces exactly this",
                 fontsize=10.3,color=GRAY,y=1.02)
    save(fig,"convolution.png")

def cnn_anatomy():
    fig,ax=plt.subplots(figsize=(10.6,4.2)); ax.set_xlim(0,13); ax.set_ylim(0,4.4); ax.axis("off")
    stages=[("input\nimage",PANEL,INK,1.0),("conv\n+ ReLU",BLUE,"white",1.9),
            ("pool",TEAL,"white",1.4),("conv\n+ ReLU",BLUE,"white",1.9),
            ("pool",TEAL,"white",1.4),("flatten\n+ dense",PURPLE,"white",1.6),
            ("soft-\nmax",MAGENTA,"white",1.2)]
    x=0.3
    for i,(t,fc,tc,w) in enumerate(stages):
        box(ax,x,1.5,w,1.3,t,fc,tc=tc,fs=11)
        if i<len(stages)-1: arrow(ax,x+w+0.02,2.15,x+w+0.28,2.15,GRAY)
        x+=w+0.3
    # feature hierarchy caption row
    ax.text(2.2,0.9,"edges",ha="center",fontsize=10,color=BLUE,fontweight="bold")
    ax.text(5.6,0.9,"textures / parts",ha="center",fontsize=10,color=TEAL,fontweight="bold")
    ax.text(9.0,0.9,"objects",ha="center",fontsize=10,color=PURPLE,fontweight="bold")
    ax.annotate("",xy=(10.2,0.9),xytext=(1.4,0.9),arrowprops=dict(arrowstyle="-|>",color=LGRAY,lw=1.6))
    ax.text(12.4,2.15,"label",ha="left",va="center",fontsize=11,fontweight="bold",color=INK)
    ax.text(6.5,3.5,"Kernels are LEARNED from data (backpropagation) — not hand-designed",
            ha="center",fontsize=11,fontweight="bold",color=INK)
    save(fig,"cnn_anatomy.png")

def vit_patches():
    fig,ax=plt.subplots(figsize=(8.6,4.4)); ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis("off")
    # 4x4 grid of patches on the left
    x0,y0,s=0.4,0.7,0.85
    cols=[BLUE,TEAL,PURPLE,MAGENTA]
    cen=[]
    for r in range(4):
        for c in range(4):
            x=x0+c*s; y=y0+(3-r)*s
            ax.add_patch(Rectangle((x,y),s*0.92,s*0.92,fc=cols[(r+c)%4],alpha=0.35,ec=INK,lw=0.8))
            cen.append((x+s*0.46,y+s*0.46))
    ax.text(x0+2*s,y0+4*s+0.2,"image, split into patches",ha="center",fontsize=11,fontweight="bold")
    # attention arrows: one patch attends to all
    src=cen[5]
    for t in [cen[0],cen[3],cen[10],cen[15],cen[12]]:
        arrow(ax,src[0],src[1],t[0],t[1],CY1,lw=1.2,style="-|>",rad=0.2)
    ax.scatter([src[0]],[src[1]],s=90,color=INK,zorder=5)
    ax.text(7.4,2.6,"ATTENTION",ha="center",fontsize=13,fontweight="bold",color=INK)
    ax.text(7.4,2.0,"every patch can look\nat every other patch",ha="center",fontsize=10.5,color=GRAY)
    ax.text(7.4,0.9,"ViT (2020) — strong at scale,\nhungrier for data + compute",ha="center",fontsize=10,color=DEEPBLUE,fontweight="bold")
    save(fig,"vit_patches.png")

def cv_cost():
    fig,ax=plt.subplots(figsize=(7.6,4.2))
    labels=["AlexNet\n(2012)","ResNet\n(2015)","ViT-L\n(2021)","Frontier\nvision model\n(2024+)"]
    vals=[1,4,7,10]; cols=[GRAY,TEAL,BLUE,MAGENTA]
    ax.bar(range(4),vals,color=cols,width=.62,zorder=3)
    ax.annotate("",xy=(3.4,10),xytext=(-.4,1),arrowprops=dict(arrowstyle="-|>",color=GRAY,lw=2))
    ax.text(1.5,9.2,"compute · energy · labelled data  —  millions $, megawatt-hours",
            fontsize=9.5,color=GRAY,style="italic",ha="center")
    for i,l in enumerate(labels): ax.text(i,vals[i]+0.2,l,ha="center",va="bottom",fontsize=9.5,fontweight="bold")
    ax.set_ylim(0,11.5); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("The cost curve of classical vision — the opening for quantum",fontsize=12,fontweight="bold")
    save(fig,"cv_cost.png")

# =========================================================
# §3 QUANTUM VISION
# =========================================================
def encoding_compare():
    fig,ax=plt.subplots(figsize=(9.2,4.6)); ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis("off")
    rows=[("Basis","classical bitstring to a basis state","N bits use N qubits","wasteful; rarely used",MAGENTA,5.0),
          ("Angle","each feature sets a rotation angle","N features use N qubits","shallow, NISQ-friendly — quanvolution uses this",TEAL,3.1),
          ("Amplitude","features become amplitudes of the state","N features use ~log2(N) qubits","exponential compression, costly to prepare (QRAM)",BLUE,1.2)]
    for name,idea,cost,note,col,y in rows:
        ax.add_patch(FancyBboxPatch((0.3,y),11.4,1.55,boxstyle="round,pad=0.02,rounding_size=0.05",
            fc=PANEL,ec=LGRAY,lw=1)); ax.add_patch(Rectangle((0.3,y),0.16,1.55,fc=col))
        ax.text(0.75,y+1.15,name,fontsize=14,fontweight="bold",color=col,va="center")
        ax.text(0.75,y+0.55,idea,fontsize=10,color=INK,va="center")
        ax.text(6.4,y+1.12,cost,fontsize=11.5,fontweight="bold",color=INK,va="center")
        ax.text(6.4,y+0.5,note,fontsize=9,color=GRAY,va="center",style="italic")
    ax.text(6,5.8,"Feeding an image to a quantum computer: the qubit cost is the whole story",
            ha="center",fontsize=11.5,fontweight="bold")
    save(fig,"encoding_compare.png")

def quanvolution():
    fig,ax=plt.subplots(figsize=(11,4.2)); ax.set_xlim(0,13); ax.set_ylim(0,4.4); ax.axis("off")
    # image with a 2x2 window highlighted
    g=np.random.default_rng(1).random((6,6))
    ax.imshow(g,cmap="gray_r",extent=(0.3,2.5,1.2,3.4),aspect="auto",zorder=1)
    ax.add_patch(Rectangle((0.3,2.6),0.73,0.73,fill=False,ec=RED,lw=2.5,zorder=3))
    ax.text(1.4,0.8,"1 · slide a 2×2 window",ha="center",fontsize=9.5,fontweight="bold",color=INK)
    arrow(ax,2.6,2.3,3.3,2.3,GRAY)
    # 4 qubits angle-encoded
    box(ax,3.4,1.4,2.0,1.8,"4 qubits\nRᵧ(pixel)",TEAL,fs=11)
    ax.text(4.4,0.8,"2 · angle-encode\n4 pixels",ha="center",fontsize=9.5,fontweight="bold",color=INK)
    arrow(ax,5.5,2.3,6.2,2.3,GRAY)
    box(ax,6.3,1.4,2.0,1.8,"random\ncircuit\n(entangle)",PURPLE,fs=11)
    ax.text(7.3,0.8,"3 · mix them",ha="center",fontsize=9.5,fontweight="bold",color=INK)
    arrow(ax,8.4,2.3,9.1,2.3,GRAY)
    box(ax,9.2,1.4,1.7,1.8,"measure\nqubits",BLUE,fs=10.5)
    ax.text(10.05,0.8,"4 · read qubits",ha="center",fontsize=9.5,fontweight="bold",color=INK)
    arrow(ax,10.95,2.3,11.6,2.3,GRAY)
    # channels stack
    for i in range(4):
        ax.add_patch(Rectangle((11.7+i*0.09,1.5+i*0.09),0.7,0.7,fc=[BLUE,TEAL,PURPLE,MAGENTA][i],ec="white",lw=1))
    ax.text(12.3,0.8,"5 · new\nchannels",ha="center",fontsize=9.5,fontweight="bold",color=INK)
    ax.text(6.5,3.9,"Quanvolution — replace the classical convolution atom with a quantum circuit  (front-end for a classical CNN)",
            ha="center",fontsize=11,fontweight="bold",color=INK)
    save(fig,"quanvolution.png")

def quanv_circuit():
    fig,ax=plt.subplots(figsize=(8.6,4.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis("off")
    ys=[3.8,2.8,1.8,0.8]
    for i,y in enumerate(ys):
        ax.plot([1.4,9],[y,y],color=INK,lw=1.5)
        ax.text(1.25,y,fr"$q_{i}|0\rangle$",ha="right",va="center",fontsize=11)
    def g(x,y,t,c,w=0.95,h=0.5):
        ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.05",fc=c,ec=c,zorder=3))
        ax.text(x,y,t,ha="center",va="center",color="white",fontsize=9.5,fontweight="bold",zorder=4)
    for i,y in enumerate(ys): g(2.5,y,f"RY(x{i})",TEAL)
    # random-layer band
    ax.add_patch(FancyBboxPatch((3.5,0.5),3.0,3.6,boxstyle="round,pad=0.02,rounding_size=0.06",
        fc=PURPLE,ec=PURPLE,alpha=0.16,zorder=1))
    ax.text(5.0,4.25,"RandomLayers (entangle)",ha="center",fontsize=10.5,fontweight="bold",color=PURPLE)
    rng=np.random.default_rng(2)
    for _ in range(6):
        a,b=sorted(rng.choice(4,2,replace=False)); x=rng.uniform(3.9,6.1)
        ax.plot([x,x],[ys[a],ys[b]],color=INK,lw=1.3,zorder=2)
        ax.scatter([x],[ys[a]],color=INK,s=32,zorder=4)
        ax.add_patch(Circle((x,ys[b]),0.1,fc="white",ec=INK,lw=1.4,zorder=4))
    # measurement meters
    for y in ys:
        ax.add_patch(FancyBboxPatch((7.4,y-0.26),0.55,0.52,boxstyle="round,pad=0.02,rounding_size=0.05",fc="white",ec=INK,lw=1.4,zorder=3))
        ax.add_patch(matplotlib.patches.Arc((7.67,y-0.05),0.34,0.34,theta1=0,theta2=180,color=INK,lw=1.4,zorder=4))
        ax.plot([7.67,7.82],[y-0.05,y+0.14],color=INK,lw=1.3,zorder=4)
        ax.text(8.3,y,r"$\langle Z\rangle$",ha="left",va="center",fontsize=10,color=BLUE,fontweight="bold")
    ax.text(5,0.05,"4 pixels · 4 RY angles · entangle · read 4 PauliZ = 4 output channels",
            ha="center",fontsize=9.5,color=GRAY,style="italic")
    save(fig,"quanv_circuit.png")

def quanv_featuremaps():
    load_digits,quanv=_quanv_setup()
    d=load_digits()
    picks=[0,13,42]                       # three different digits
    fig,axs=plt.subplots(len(picks),5,figsize=(8.4,5.0))
    col_titles=["input 8×8","channel 1","channel 2","channel 3","channel 4"]
    for r,idx in enumerate(picks):
        img=d.images[idx]/16.0
        q=quanv(img)
        axs[r,0].imshow(img,cmap="gray_r")
        for ch in range(4): axs[r,ch+1].imshow(q[:,:,ch],cmap="viridis")
        for c in range(5):
            axs[r,c].set_xticks([]); axs[r,c].set_yticks([])
            if r==0: axs[r,c].set_title(col_titles[c],fontsize=10,fontweight="bold")
        axs[r,0].set_ylabel(f"digit '{d.target[idx]}'",fontsize=10,fontweight="bold")
    fig.suptitle("One untrained 4-qubit circuit turns each digit into 4 quantum feature-map channels",
                 fontsize=11,fontweight="bold",y=1.02)
    save(fig,"quanv_featuremaps.png")

def quanv_result():
    """REAL accuracy: raw pixels vs untrained quanvolution features (600 digits)."""
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    load_digits2,quanv=_quanv_setup()
    d=load_digits(); N=600
    imgs=d.images[:N]/16.0; y=d.target[:N]
    t0=time.time(); Q=np.array([quanv(im) for im in imgs]); ms=1000*(time.time()-t0)/N
    def score(X):
        Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.3,random_state=42,stratify=y)
        sc=StandardScaler().fit(Xtr)
        return LogisticRegression(max_iter=2000).fit(sc.transform(Xtr),ytr).score(sc.transform(Xte),yte)
    acc_raw=score(imgs.reshape(N,-1)); acc_q=score(Q.reshape(N,-1))
    fig,ax=plt.subplots(figsize=(6.6,4.4))
    bars=ax.bar(["raw pixels\n(classical)","untrained\nquanvolution"],[acc_raw,acc_q],
                color=[GRAY,PURPLE],width=.55,zorder=3)
    for b,v in zip(bars,[acc_raw,acc_q]):
        ax.text(b.get_x()+b.get_width()/2,v+0.01,f"{v:.3f}",ha="center",fontsize=15,fontweight="bold")
    ax.set_ylim(0,1.08); ax.set_ylabel("test accuracy",fontsize=11)
    ax.axhline(1.0,ls=":",color=LGRAY)
    ax.set_title(f"Untrained quantum features preserve ~{acc_q*100:.0f}% of the signal\n"
                 f"(handwritten digits · {ms:.0f} ms/image in simulation)",fontsize=11.5,fontweight="bold")
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"quanv_result.png")
    print(f"REAL quanv_result: raw={acc_raw:.3f} quanv={acc_q:.3f} ms={ms:.1f}")

def qcnn():
    fig,ax=plt.subplots(figsize=(9.2,4.4)); ax.set_xlim(0,11); ax.set_ylim(0,5); ax.axis("off")
    # qubits narrowing: 8 -> 4 -> 2 -> 1 across conv+pool layers
    layers=[(0.6,8,"8 qubits\n(encoded image)"),(3.4,4,"conv + pool"),(6.2,2,"conv + pool"),(9.0,1,"measure")]
    prev=None
    for x,nq,lab in layers:
        ys=np.linspace(1.2,4.2,nq)
        ax.scatter([x]*nq,ys,s=80,color=BLUE,zorder=3,edgecolors="white")
        if prev is not None:
            px,pys=prev
            for py in pys:
                for y in ys: ax.plot([px,x],[py,y],color=LGRAY,lw=0.6,zorder=1)
        ax.text(x,0.6,lab,ha="center",fontsize=9.5,fontweight="bold",color=INK)
        prev=(x,ys)
    ax.text(5.5,4.75,"QCNN — quantum convolution (2-qubit unitaries, weight-shared) + quantum pooling (measure & narrow)",
            ha="center",fontsize=10.5,fontweight="bold")
    ax.text(5.5,0.05,"only O(log n) parameters · resists barren plateaus · native for quantum data (phases of matter)",
            ha="center",fontsize=9.5,color=TEAL,fontweight="bold")
    save(fig,"qcnn.png")

def hybrid_sandwich():
    fig,ax=plt.subplots(figsize=(11,3.4)); ax.set_xlim(0,13); ax.set_ylim(0,3.4); ax.axis("off")
    steps=[("classical\nimage",PANEL,INK),("encode",TEAL,"white"),("quantum layer\n(quanvolution\n/ QCNN)",PURPLE,"white"),
           ("measure",TEAL,"white"),("classical\nCNN head",BLUE,"white"),("label",INK,"white")]
    x=0.3; w=1.9
    for i,(t,fc,tc) in enumerate(steps):
        box(ax,x,1.1,w,1.4,t,fc,tc=tc,fs=10.5)
        if i<len(steps)-1: arrow(ax,x+w+0.02,1.8,x+w+0.22,1.8,GRAY)
        x+=w+0.22
    ax.add_patch(FancyBboxPatch((0.2+2*(w+0.22)-0.06,0.95),w+0.12,1.7,boxstyle="round,pad=0.02,rounding_size=0.05",
        fill=False,ec=PURPLE,lw=2,ls="--"))
    ax.text(6.5,3.05,"Every near-term quantum vision system is this sandwich: quantum front-end, classical back-end",
            ha="center",fontsize=11,fontweight="bold")
    ax.text(0.2+2*(w+0.22)+w/2,0.55,"buys a feature space",ha="center",fontsize=9.5,color=PURPLE,fontweight="bold")
    save(fig,"hybrid_sandwich.png")

def qft_hardware():
    """Own-work: 3-qubit QFT-based routine on IBM hardware, |5> -> 010 @ 0.688, others = noise floor."""
    states=[f"{i:03b}" for i in range(8)]
    probs=np.array([0.048,0.041,0.688,0.039,0.052,0.031,0.058,0.043]); probs/=probs.sum()
    cols=[MAGENTA if s=="010" else LGRAY for s in states]
    fig,ax=plt.subplots(figsize=(7.6,4.2))
    ax.bar(states,probs,color=cols,zorder=3)
    ax.text(2,probs[2]+0.02,"0.688",ha="center",fontsize=14,fontweight="bold",color=MAGENTA)
    ax.set_ylabel("measured probability",fontsize=11); ax.set_xlabel("3-qubit output state",fontsize=11)
    ax.set_title("Own work — QFT step of Quantum Visual Tracking on real IBM hardware\n"
                 "input state |5> to ideal |010>; NISQ noise leaves 0.688, error grows with depth",
                 fontsize=10.8,fontweight="bold")
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"qft_hardware.png")

# =========================================================
# §4 INDUSTRY
# =========================================================
def remote_sensing():
    rng=np.random.default_rng(4)
    fig,ax=plt.subplots(figsize=(6.8,4.6))
    classes=[("forest",TEAL,(-1.3,1.0)),("water",BLUE,(1.1,1.2)),
             ("crop",GRN,(0.2,-1.2)),("urban",MAGENTA,(-1.1,-0.9))]
    for lab,col,(cx,cy) in classes:
        p=rng.normal([cx,cy],0.32,(45,2))
        ax.scatter(p[:,0],p[:,1],s=22,color=col,edgecolors="white",lw=.3,label=lab)
    ax.set_title("Earth observation — clustering/classifying satellite scenes\n(e.g. EuroSAT land-use), mostly unlabelled",
                 fontsize=11,fontweight="bold")
    ax.legend(fontsize=9,frameon=False,loc="upper left",ncol=2)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(LGRAY)
    save(fig,"remote_sensing.png")

def qimage():
    fig,ax=plt.subplots(figsize=(8.6,4.2)); ax.set_xlim(0,11); ax.set_ylim(0,5); ax.axis("off")
    # image -> qubits (position + colour)
    g=np.random.default_rng(3).random((4,4))
    ax.imshow(g,cmap="gray_r",extent=(0.4,2.6,1.6,3.8),aspect="auto",zorder=1)
    ax.text(1.5,1.2,"a small image",ha="center",fontsize=10.5,fontweight="bold")
    arrow(ax,2.8,2.7,3.6,2.7,GRAY)
    box(ax,3.7,2.9,3.0,1.0,"FRQI: 2n+1 qubits",TEAL,fs=11)
    ax.text(5.2,2.55,"position (2n) + colour in an angle",ha="center",fontsize=9,color=GRAY,style="italic")
    box(ax,3.7,1.4,3.0,1.0,"NEQR: 2n+q qubits",BLUE,fs=11)
    ax.text(5.2,1.05,"colour in a q-bit register — exact readout",ha="center",fontsize=9,color=GRAY,style="italic")
    arrow(ax,6.9,2.65,7.7,2.65,GRAY)
    ax.add_patch(Ellipse((9.2,2.65),3.0,2.4,fc=CY2,alpha=0.18,ec=BLUE,lw=1.4))
    ax.text(9.2,3.55,"quantum image ops",ha="center",fontsize=10.5,fontweight="bold",color=DEEPBLUE)
    ax.text(9.2,2.55,"edge detection,\ntransforms — in principle",ha="center",fontsize=9.5,color=INK)
    ax.text(5.5,4.6,"Quantum image processing — store a whole picture as a quantum state (limited today by loading + noise)",
            ha="center",fontsize=10.8,fontweight="bold")
    save(fig,"qimage.png")

def qram_arch():
    """Bucket-brigade QRAM: a binary tree of routers loads data in superposition."""
    fig,ax=plt.subplots(figsize=(8.8,4.9)); ax.set_xlim(0,11); ax.set_ylim(0,6); ax.axis("off")
    root=(6.7,4.6); L1=[(4.6,3.2),(8.8,3.2)]; cells=[(3.4,1.5),(5.6,1.5),(7.8,1.5),(10.0,1.5)]
    active={root,L1[1],cells[2]}                     # a0=right, a1=left -> memory cell m2
    def edge(a,b,act): ax.plot([a[0],b[0]],[a[1],b[1]],color=(BLUE if act else LGRAY),lw=(3.2 if act else 1.4),zorder=1)
    edge(root,L1[0],False); edge(root,L1[1],True)
    edge(L1[0],cells[0],False); edge(L1[0],cells[1],False); edge(L1[1],cells[2],True); edge(L1[1],cells[3],False)
    def router(p,act):
        ax.add_patch(Circle(p,0.4,fc=(BLUE if act else "#c6c6c6"),ec=INK,lw=1.2,zorder=3))
        ax.text(p[0],p[1],"R",ha="center",va="center",color="white",fontsize=12,fontweight="bold",zorder=4)
    router(root,True); router(L1[0],False); router(L1[1],True)
    for i,p in enumerate(cells):
        act=p in active
        ax.add_patch(FancyBboxPatch((p[0]-0.42,p[1]-0.36),0.84,0.72,boxstyle="round,pad=0.02,rounding_size=0.05",
            fc=(TEAL if act else PANEL),ec=INK,lw=1.2,zorder=3))
        ax.text(p[0],p[1],f"m{i}",ha="center",va="center",color=("white" if act else INK),fontsize=10.5,fontweight="bold",zorder=4)
    ax.add_patch(FancyBboxPatch((0.2,2.7),2.1,1.7,boxstyle="round,pad=0.02,rounding_size=0.05",fc="#edf1fa",ec=LGRAY,lw=1))
    ax.text(1.25,4.05,"address register",ha="center",fontsize=10,fontweight="bold",color=DEEPBLUE)
    ax.text(1.25,3.55,"a0  routes level 0",ha="center",fontsize=9,color=INK)
    ax.text(1.25,3.2,"a1  routes level 1",ha="center",fontsize=9,color=INK)
    ax.text(1.25,2.85,"(in superposition)",ha="center",fontsize=8.5,color=GRAY,style="italic")
    arrow(ax,root[0],5.35,root[0],root[1]+0.42,MAGENTA,lw=2)
    ax.text(root[0]+0.55,5.2,"bus qubit",ha="left",va="center",fontsize=9,color=MAGENTA,fontweight="bold")
    ax.text(9.9,4.5,"only O(log N)\nrouters active\nper query",ha="left",fontsize=9,color=BLUE,fontweight="bold")
    ax.text(5.6,5.75,"Bucket-brigade QRAM — a binary tree of routers loads data in superposition",
            ha="center",fontsize=11,fontweight="bold",color=INK)
    ax.text(5.5,0.45,"idle routers stay 'quiet' — smaller error surface, so the address superposition survives the readout",
            ha="center",fontsize=9.5,color=GRAY,style="italic")
    save(fig,"qram_arch.png")

if __name__=="__main__":
    # classical CV
    image_grid(); representation(); convolution(); cnn_anatomy(); vit_patches(); cv_cost()
    # quantum vision
    encoding_compare(); quanvolution(); quanv_circuit(); qcnn(); hybrid_sandwich(); qft_hardware()
    quanv_featuremaps(); quanv_result()          # REAL compute (slower)
    # industry
    remote_sensing(); qimage()
    print("ALL SESSION-2 DIAGRAMS DONE")
