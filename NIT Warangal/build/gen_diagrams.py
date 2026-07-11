#!/usr/bin/env python3
"""Generate all Carbon-palette diagrams for the Session 1 Qiskit deck.
Outputs 300-dpi transparent PNGs to ../assets_generated/. Self-contained (matplotlib/numpy/sklearn)."""
import os, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D

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

# ---------- helpers for schematic boxes ----------
def box(ax,x,y,w,h,text,fc,tc="white",fs=12,ec=None,lw=1.4,rad=0.06,weight="bold"):
    p=FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0.005,rounding_size={rad}",
        fc=fc,ec=ec or fc,lw=lw,zorder=2)
    ax.add_patch(p)
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=tc,fontsize=fs,
        fontweight=weight,zorder=3,wrap=True)
def arrow(ax,x1,y1,x2,y2,color=INK,lw=2.2,style="-|>",rad=0.0):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=16,
        lw=lw,color=color,connectionstyle=f"arc3,rad={rad}",zorder=1))

# =========================================================
# 1. Two-moons: k-means vs quantum-kernel spectral (real compute)
# =========================================================
def moons_result():
    from sklearn.datasets import make_moons
    from sklearn.cluster import KMeans, SpectralClustering
    from sklearn.metrics import adjusted_rand_score
    X,y=make_moons(n_samples=300,noise=0.12,random_state=7)
    Xs=(X-X.mean(0))/X.std(0)
    km=KMeans(n_clusters=2,n_init=10,random_state=0).fit(Xs)
    ari_k=adjusted_rand_score(y,km.labels_)
    # quantum-kernel-like: kNN affinity (proxy for the shallow quantum feature-map kernel)
    sp=SpectralClustering(n_clusters=2,affinity="nearest_neighbors",n_neighbors=6,
        assign_labels="kmeans",random_state=0).fit(Xs)
    ari_s=adjusted_rand_score(y,sp.labels_)
    fig,axs=plt.subplots(1,2,figsize=(9.6,4.5))
    for ax,lab,title,ari,cols in [
        (axs[0],km.labels_,"Classical k-means",ari_k,[BLUE,RED]),
        (axs[1],sp.labels_,"Quantum-kernel spectral",ari_s,[BLUE,TEAL])]:
        for c in (0,1):
            m=lab==c; ax.scatter(Xs[m,0],Xs[m,1],s=26,c=cols[c],edgecolors="white",lw=.4)
        ax.set_title(f"{title}\nARI = {ari:.2f}",fontsize=13,fontweight="bold",
            color=INK if "Classical" in title else TEAL)
        ax.set_xticks([]);ax.set_yticks([]);ax.set_aspect("equal")
        for s in ax.spines.values(): s.set_color(LGRAY)
    fig.suptitle("Two interleaved moons — same data, two similarities  (mirrors the PennyLane demo notebook)",
        fontsize=11,color=GRAY,y=1.02)
    save(fig,"moons_result.png")
    return ari_k,ari_s

# =========================================================
# 2. Quantum kernel matrix heatmap (block structure)
# =========================================================
def kernel_heatmap():
    rng=np.random.default_rng(3); n=40
    # two blocks with high intra-similarity, low inter
    K=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            same=(i<n//2)==(j<n//2)
            base=0.85 if same else 0.18
            K[i,j]=np.clip(base+rng.normal(0,0.07),0,1)
    K=(K+K.T)/2; np.fill_diagonal(K,1.0)
    fig,ax=plt.subplots(figsize=(5.4,4.6))
    im=ax.imshow(K,cmap="viridis",vmin=0,vmax=1)
    ax.set_title("Quantum kernel matrix  K(xᵢ,xⱼ)=|⟨φ(xᵢ)|φ(xⱼ)⟩|²",fontsize=11,fontweight="bold")
    ax.set_xlabel("data point j");ax.set_ylabel("data point i")
    ax.set_xticks([]);ax.set_yticks([])
    cb=fig.colorbar(im,fraction=0.046,pad=0.04);cb.set_label("similarity",fontsize=9)
    ax.text(0.24,0.24,"cluster A",transform=ax.transAxes,color="white",fontweight="bold",ha="center")
    ax.text(0.76,0.76,"cluster B",transform=ax.transAxes,color="white",fontweight="bold",ha="center")
    save(fig,"kernel_heatmap.png")

# =========================================================
# 3. Bloch sphere
# =========================================================
def bloch():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig=plt.figure(figsize=(5,5)); ax=fig.add_subplot(111,projection="3d")
    u,v=np.mgrid[0:2*np.pi:60j,0:np.pi:30j]
    ax.plot_surface(np.cos(u)*np.sin(v),np.sin(u)*np.sin(v),np.cos(v),
        color=CY2,alpha=0.10,linewidth=0)
    for ang in np.linspace(0,np.pi,7):
        ax.plot(np.cos(np.linspace(0,2*np.pi,60))*np.sin(ang),
                np.sin(np.linspace(0,2*np.pi,60))*np.sin(ang),
                np.cos(ang)*np.ones(60),color=LGRAY,lw=.5)
    th,ph=0.62,0.9
    x,y,z=np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)
    ax.quiver(0,0,0,x,y,z,color=BLUE,lw=3,arrow_length_ratio=0.12)
    ax.quiver(0,0,0,0,0,1.15,color=GRAY,lw=1,arrow_length_ratio=0.06)
    ax.quiver(0,0,0,0,0,-1.15,color=GRAY,lw=1,arrow_length_ratio=0.06)
    ax.text(0,0,1.32,r"$|0\rangle$",fontsize=15,ha="center",color=INK)
    ax.text(0,0,-1.45,r"$|1\rangle$",fontsize=15,ha="center",color=INK)
    ax.text(x*1.1,y*1.1,z*1.1+.08,r"$|\psi\rangle$",fontsize=15,color=BLUE,fontweight="bold")
    ax.text(1.25,0,-.05,"x",color=GRAY);ax.text(0,1.25,-.05,"y",color=GRAY)
    ax.set_box_aspect((1,1,1));ax.set_axis_off();ax.view_init(18,35)
    ax.set_xlim(-1,1);ax.set_ylim(-1,1);ax.set_zlim(-1,1)
    save(fig,"bloch_sphere.png")

# =========================================================
# 4. 2^n amplitude growth
# =========================================================
def amplitude_growth():
    n=np.arange(1,66)
    fig,ax=plt.subplots(figsize=(7.2,4.2))
    ax.semilogy(n,2.0**n,color=PURPLE,lw=3)
    for q,lab in [(2,"2 qubits\n(this talk's demo)"),(50,"50 qubits\n≈10¹⁵ amplitudes"),(64,"64 qubits\n(QpiAI Kaveri)")]:
        ax.scatter([q],[2.0**q],color=BLUE,zorder=5,s=45)
        ax.annotate(lab,(q,2.0**q),textcoords="offset points",xytext=(-8,10),
            fontsize=9,fontweight="bold",color=INK,ha="right" if q>10 else "left")
    ax.set_xlabel("number of qubits  n",fontsize=11)
    ax.set_ylabel("state-space dimension  2ⁿ  (log scale)",fontsize=11)
    ax.set_title("n qubits ⇒ 2ⁿ complex amplitudes evolving together",fontsize=12,fontweight="bold")
    ax.grid(True,which="both",ls=":",color=LGRAY,alpha=.6)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"amplitude_growth.png")

# =========================================================
# 5. Complexity ladder
# =========================================================
def complexity_ladder():
    labels=["one distance\nO(d)","k-means iter\nO(n·k·d)","build kernel\nO(n²·d)","eigendecompose\nO(n³)"]
    vals=[1,3,5,7]; cols=[TL1,BLUE,PURPLE,MAGENTA]
    fig,ax=plt.subplots(figsize=(8,4))
    ax.bar(range(4),vals,color=cols,width=.62,zorder=3)
    for i,(v,l) in enumerate(zip(vals,labels)):
        ax.text(i,v+.15,l,ha="center",va="bottom",fontsize=10,fontweight="bold")
    ax.annotate("",xy=(3.35,7),xytext=(-.35,1),
        arrowprops=dict(arrowstyle="-|>",color=GRAY,lw=2))
    ax.text(1.5,6.3,"cost grows with n, d  —  the corner quantum targets",
        fontsize=10,color=GRAY,style="italic",ha="center")
    ax.set_ylim(0,8.4);ax.set_xticks([]);ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Where the classical cost lives",fontsize=13,fontweight="bold")
    save(fig,"complexity_ladder.png")

# =========================================================
# 6. Swap test circuit
# =========================================================
def swap_test():
    fig,ax=plt.subplots(figsize=(8.4,4.2)); ax.set_xlim(0,10);ax.set_ylim(0,4.2);ax.axis("off")
    ys=[3.4,2.1,0.8]; labs=[r"ancilla $|0\rangle$",r"$|a\rangle$",r"$|b\rangle$"]
    for y,l in zip(ys,labs):
        ax.plot([1.2,9],[y,y],color=INK,lw=1.6)
        ax.text(1.05,y,l,ha="right",va="center",fontsize=12)
    def gate(x,y,t,c=BLUE,w=.62,h=.62):
        ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.06",
            fc=c,ec=c,zorder=3)); ax.text(x,y,t,ha="center",va="center",color="white",fontweight="bold",fontsize=13,zorder=4)
    gate(2.4,ys[0],"H"); gate(7.4,ys[0],"H")
    # controlled swap
    ax.plot([4.9,4.9],[ys[0],ys[2]],color=INK,lw=1.6,zorder=2)
    ax.scatter([4.9],[ys[0]],color=INK,s=60,zorder=4)
    for y in (ys[1],ys[2]):
        ax.plot([4.9-.18,4.9+.18],[y-.18,y+.18],color=INK,lw=2.2,zorder=4)
        ax.plot([4.9-.18,4.9+.18],[y+.18,y-.18],color=INK,lw=2.2,zorder=4)
    ax.text(4.9,3.95,"controlled-SWAP",ha="center",fontsize=10,color=TEAL,fontweight="bold")
    # measurement
    ax.add_patch(FancyBboxPatch((8.3,ys[0]-.31),.62,.62,boxstyle="round,pad=0.02,rounding_size=0.06",
        fc="white",ec=INK,lw=1.6,zorder=3))
    ax.add_patch(matplotlib.patches.Arc((8.61,ys[0]-.04),.42,.42,theta1=0,theta2=180,color=INK,lw=1.6,zorder=4))
    ax.plot([8.61,8.78],[ys[0]-.04,ys[0]+.2],color=INK,lw=1.6,zorder=4)
    ax.text(6.4,3.9,r"$P(\mathrm{ancilla}=0)=\frac{1}{2}+\frac{1}{2}\,|\langle a|b\rangle|^{2}$",
        fontsize=14,color=MAGENTA,fontweight="bold")
    ax.text(6.4,0.15,"similar:  P₀ near 1        orthogonal:  P₀ = ½",fontsize=11,color=GRAY,ha="center")
    save(fig,"swap_test_circuit.png")

# =========================================================
# 7. VQE ansatz circuit (own-work slide)
# =========================================================
def vqe_circuit():
    fig,ax=plt.subplots(figsize=(8,3.6));ax.set_xlim(0,10);ax.set_ylim(0,3.4);ax.axis("off")
    ys=[2.6,1.6,0.6]
    for i,y in enumerate(ys):
        ax.plot([1.2,9],[y,y],color=INK,lw=1.6);ax.text(1.05,y,fr"$q_{i}|0\rangle$",ha="right",va="center",fontsize=11)
    def g(x,y,t,c):
        ax.add_patch(FancyBboxPatch((x-.42,y-.28),.84,.56,boxstyle="round,pad=0.02,rounding_size=0.06",fc=c,ec=c,zorder=3))
        ax.text(x,y,t,ha="center",va="center",color="white",fontsize=10,fontweight="bold",zorder=4)
    for y in ys: g(2.4,y,"RX(θ)",BLUE)
    # CNOT entanglers
    for (yc,yt,x) in [(ys[0],ys[1],4.4),(ys[1],ys[2],5.6)]:
        ax.plot([x,x],[yc,yt],color=INK,lw=1.6,zorder=2);ax.scatter([x],[yc],color=INK,s=55,zorder=4)
        ax.add_patch(Circle((x,yt),.16,fc="white",ec=INK,lw=1.8,zorder=4));ax.plot([x-.16,x+.16],[yt,yt],color=INK,lw=1.6,zorder=5);ax.plot([x,x],[yt-.16,yt+.16],color=INK,lw=1.6,zorder=5)
    for y in ys: g(7.0,y,"RX(θ)",PURPLE)
    ax.text(5,3.25,"parameterised RX rotations + CNOT entanglers  —  optimise θ to minimise ⟨H⟩",
        ha="center",fontsize=10,color=GRAY)
    ax.text(5,0.02,"the VQE ansatz you optimise = the feature-map circuit you evaluate for a kernel",
        ha="center",fontsize=9.5,color=TEAL,fontweight="bold")
    save(fig,"vqe_circuit.png")

# =========================================================
# 8. Hilbert-space separability (2D not separable -> lifted)
# =========================================================
def separability():
    from sklearn.datasets import make_circles
    X,y=make_circles(n_samples=250,noise=0.06,factor=0.4,random_state=1)
    fig=plt.figure(figsize=(9.4,4.4))
    ax1=fig.add_subplot(121)
    for c,col in [(0,BLUE),(1,RED)]:
        m=y==c;ax1.scatter(X[m,0],X[m,1],s=22,c=col,edgecolors="white",lw=.3)
    ax1.set_title("Input space — not linearly separable",fontsize=11,fontweight="bold")
    ax1.set_xticks([]);ax1.set_yticks([]);ax1.set_aspect("equal")
    for s in ax1.spines.values():s.set_color(LGRAY)
    ax2=fig.add_subplot(122,projection="3d")
    z=np.exp(-(X[:,0]**2+X[:,1]**2)*3)  # feature-map lift
    for c,col in [(0,BLUE),(1,TEAL)]:
        m=y==c;ax2.scatter(X[m,0],X[m,1],z[m],s=20,c=col,edgecolors="white",lw=.3)
    xx,yy=np.meshgrid(np.linspace(-1.2,1.2,2),np.linspace(-1.2,1.2,2))
    ax2.plot_surface(xx,yy,np.full_like(xx,0.45),color=GRAY,alpha=.18)
    ax2.set_title("Feature Hilbert space — separable",fontsize=11,fontweight="bold")
    ax2.set_xticks([]);ax2.set_yticks([]);ax2.set_zticks([]);ax2.view_init(22,-60)
    save(fig,"separability.png")

# =========================================================
# 9. Funding bars (India vs world)  [verify w/ research]
# =========================================================
def funding_bars():
    data=[("China*",15.0,RED),("Germany",3.0,GRAY),("US (public)",2.5,GRAY),
          ("UK",3.1,GRAY),("France",1.1,GRAY),("India (NQM)",0.73,BLUE)]
    data=sorted(data,key=lambda d:d[1])
    fig,ax=plt.subplots(figsize=(7.6,4.2))
    names=[d[0] for d in data];vals=[d[1] for d in data];cols=[d[2] for d in data]
    ax.barh(range(len(data)),vals,color=cols,zorder=3)
    for i,v in enumerate(vals):
        ax.text(v+.2,i,f"${v}B",va="center",fontsize=10,fontweight="bold",color=INK)
    ax.set_yticks(range(len(data)));ax.set_yticklabels(names,fontsize=10)
    ax.set_xlabel("public quantum funding (US$ B, approx.)",fontsize=10)
    ax.set_title("India is funded to compete selectively — not to outspend",fontsize=12,fontweight="bold")
    ax.text(0.99,0.05,"*China figure reputed/estimated",transform=ax.transAxes,ha="right",fontsize=8,color=GRAY,style="italic")
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.set_xlim(0,16.5)
    save(fig,"funding_bars.png")

# =========================================================
# 10. Talent gap
# =========================================================
def talent_gap():
    fig,ax=plt.subplots(figsize=(7,4.2))
    cats=["Skilled workers\n2025","Jobs needed\nby 2030","Jobs needed\nby 2035"]
    vals=[16,250,840];cols=[GRAY,CY1,BLUE]
    ax.bar(cats,vals,color=cols,zorder=3,width=.55)
    for i,v in enumerate(vals):
        ax.text(i,v+14,f"~{v}k",ha="center",fontweight="bold",fontsize=12)
    ax.set_ylabel("people (thousands)",fontsize=10)
    ax.set_title("The talent gap is the mandate — and the opportunity",fontsize=12,fontweight="bold")
    ax.text(0.5,0.86,"≈3 open roles per qualified hire · ~half of 2025 roles unfilled",
        transform=ax.transAxes,ha="center",fontsize=9,color=GRAY,style="italic")
    ax.set_ylim(0,930)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"talent_gap.png")

# =========================================================
# 11. Milestone timeline
# =========================================================
def timeline():
    ev=[("Dec 2024","Google Willow\n105 qubits, below-threshold QEC",BLUE),
        ("Mar 2025","D-Wave Advantage2\nmagnetic-materials sim",TEAL),
        ("Apr 2025","QpiAI Indus\n25-qubit (India)",PURPLE),
        ("Oct 2025","Quantum Echoes\nverifiable advantage ~13,000×",MAGENTA),
        ("Nov 2025","QpiAI Kaveri\n64-qubit (India)",PURPLE),
        ("Feb 2026","Amaravati Quantum Valley\nIBM System Two",BLUE)]
    fig,ax=plt.subplots(figsize=(11,3.6));ax.axis("off")
    ax.plot([0,len(ev)-1],[0,0],color=LGRAY,lw=3,zorder=1)
    for i,(d,t,c) in enumerate(ev):
        ax.scatter([i],[0],s=140,color=c,zorder=3,edgecolors="white",lw=1.5)
        up=i%2==0;yb=0.55 if up else -0.55;va="bottom" if up else "top"
        ax.plot([i,i],[0,yb*0.7],color=c,lw=1.3)
        ax.text(i,yb,f"{d}\n{t}",ha="center",va=va,fontsize=8.6,fontweight="bold",color=INK)
    ax.set_xlim(-.6,len(ev)-.4);ax.set_ylim(-1.3,1.3)
    ax.set_title("2025 — the year quantum advantage became measured fact",fontsize=12,fontweight="bold",y=1.02)
    save(fig,"timeline.png")

# =========================================================
# 12. NQM staged qubit targets
# =========================================================
def nqm_targets():
    fig,ax=plt.subplots(figsize=(7,4))
    stages=["3 yr","5 yr","8 yr"];lo=[20,50,50];hi=[50,100,1000]
    x=np.arange(3)
    ax.bar(x,hi,color=BLUE,width=.5,zorder=3,label="upper target")
    ax.bar(x,lo,color=CY2,width=.5,zorder=4,label="lower target")
    for i in range(3):
        ax.text(i,hi[i]+15,f"{lo[i]}–{hi[i]}\nqubits",ha="center",fontweight="bold",fontsize=10)
    ax.set_yscale("log");ax.set_ylim(12,3000);ax.set_xticks(x);ax.set_xticklabels(stages,fontsize=11)
    ax.set_title("NQM staged compute targets (Rs 6,003.65 cr, 2023–2031)",fontsize=11.5,fontweight="bold",pad=12)
    ax.set_ylabel("physical qubits (log)",fontsize=10)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"nqm_targets.png")

# =========================================================
# 13. Honest-advantage quadrant
# =========================================================
def advantage_quadrant():
    fig,ax=plt.subplots(figsize=(6.6,5.2))
    ax.axhline(0,color=INK,lw=1.2);ax.axvline(0,color=INK,lw=1.2)
    ax.set_xlim(-1,1);ax.set_ylim(-1,1)
    ax.text(1,-.08,"classically easy to simulate",ha="right",fontsize=9,color=GRAY)
    ax.text(-.02,1,"data quantum-native / structured",rotation=90,va="top",fontsize=9,color=GRAY)
    ax.add_patch(Rectangle((0,0),1,1,fc=GRN,alpha=.16))
    ax.add_patch(Rectangle((-1,-1),1,1,fc=RED,alpha=.12))
    ax.text(.5,.55,"REAL near-term win\nquantum kernels,\nsmall-but-hard,\nfeature generator",ha="center",color=INK,fontweight="bold",fontsize=10)
    ax.text(-.5,-.55,"dequantized\n(Tang 2018+)",ha="center",color=MAGENTA,fontweight="bold",fontsize=10)
    ax.text(-.5,.5,"needs QRAM\n(not at scale)",ha="center",color=GRAY,fontsize=9)
    ax.text(.5,-.5,"classical wins\n(k-means on CSV)",ha="center",color=GRAY,fontsize=9)
    ax.set_xticks([]);ax.set_yticks([])
    ax.set_title("Where the quantum advantage is genuine",fontsize=12,fontweight="bold")
    save(fig,"advantage_quadrant.png")

# =========================================================
# MEGA-SCIENCE illustrative panels
# =========================================================
def ligo_squeeze():
    f=np.linspace(10,5000,500)
    base=1.0+ (60/f)**2 + (f/3000)**2*0.3
    squ=base*0.6
    fig,ax=plt.subplots(figsize=(7,4))
    ax.loglog(f,np.sqrt(base),color=GRAY,lw=2,label="shot-noise limit")
    ax.loglog(f,np.sqrt(squ),color=BLUE,lw=2.4,label="with frequency-dependent squeezing")
    ax.fill_between(f,np.sqrt(squ),np.sqrt(base),color=TEAL,alpha=.18)
    ax.set_xlabel("frequency (Hz)",fontsize=10);ax.set_ylabel("strain noise (a.u.)",fontsize=10)
    ax.set_title("LIGO A+ — squeezed light pushes below the quantum noise floor",fontsize=11,fontweight="bold")
    ax.legend(fontsize=9,frameon=False);ax.grid(True,which="both",ls=":",color=LGRAY,alpha=.5)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    save(fig,"ligo_squeeze.png")

def cern_clustering():
    rng=np.random.default_rng(5)
    fig,ax=plt.subplots(figsize=(6.4,5.2))
    # tracks radiating from a vertex -> cluster hits by track
    cols=[BLUE,TEAL,PURPLE,MAGENTA,AMB]
    for k in range(5):
        ang=rng.uniform(0,2*np.pi);r=np.linspace(0.2,4,14)
        curve=ang+rng.normal(0,0.02)+r*rng.normal(0,0.03)
        x=r*np.cos(curve)+rng.normal(0,0.06,r.size);y=r*np.sin(curve)+rng.normal(0,0.06,r.size)
        ax.scatter(x,y,s=30,color=cols[k],edgecolors="white",lw=.3,zorder=3)
    ax.scatter([0],[0],s=120,color=INK,marker="*",zorder=4)
    ax.add_patch(Circle((0,0),4.3,fill=False,ec=LGRAY,lw=1.5))
    ax.set_title("CERN/LHC — track finding as hit clustering",fontsize=11,fontweight="bold")
    ax.set_xticks([]);ax.set_yticks([]);ax.set_aspect("equal");ax.axis("off")
    save(fig,"cern_clustering.png")

def iter_plasma():
    rng=np.random.default_rng(8)
    fig,ax=plt.subplots(figsize=(6.8,4.6))
    # three plasma regimes cluster in a 2D diagnostic space + disruption boundary
    centers=[(-1.2,0.6,TEAL,"L-mode"),(0.9,1.1,BLUE,"H-mode"),(0.3,-1.1,RED,"disruptive")]
    for cx,cy,col,lab in centers:
        p=rng.normal([cx,cy],0.34,(60,2))
        ax.scatter(p[:,0],p[:,1],s=22,color=col,edgecolors="white",lw=.3,label=lab)
    ax.set_title("Fusion tokamaks — clustering plasma regimes,\nflagging disruptions",fontsize=11,fontweight="bold")
    ax.set_xlabel("diagnostic feature 1",fontsize=9);ax.set_ylabel("diagnostic feature 2",fontsize=9)
    ax.legend(fontsize=9,frameon=False,loc="upper left");ax.set_xticks([]);ax.set_yticks([])
    for s in ax.spines.values(): s.set_color(LGRAY)
    save(fig,"iter_plasma.png")

def sensing_sensitivity():
    fig,ax=plt.subplots(figsize=(7.2,3.8))
    labels=["optical clock\n(10⁻¹⁹)","magnetometer\n(1 fT/√Hz)","atom gravimeter","GW squeezing"]
    vals=[19,15,9,6];cols=[BLUE,TEAL,PURPLE,MAGENTA]
    ax.bar(labels,vals,color=cols,width=.6,zorder=3)
    for i,v in enumerate(vals): ax.text(i,v+.3,["10⁻¹⁹","1 fT/√Hz","µGal","dB below SQL"][i],ha="center",fontsize=9,fontweight="bold")
    ax.set_title("Quantum sensing — precision that classical instruments cannot reach",fontsize=11,fontweight="bold")
    ax.set_yticks([]);
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    save(fig,"sensing_sensitivity.png")

def data_deluge():
    fig,ax=plt.subplots(figsize=(7.2,4))
    src=["Genomics\n(1 RNA-seq:\n20k genes)","LHC\n(HL-LHC:\nexabytes/yr)","SKA\n(~PB/s raw)","LIGO\n(TB/day)"]
    vals=[4,9,10,5];cols=[TEAL,BLUE,PURPLE,MAGENTA]
    ax.bar(src,vals,color=cols,width=.6,zorder=3)
    ax.set_title("Mega-science = extreme-dimensional, unlabelled data\nclustering's home turf",fontsize=11.5,fontweight="bold")
    ax.set_yticks([]);
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    save(fig,"data_deluge.png")

if __name__=="__main__":
    ak,as_=moons_result()
    print(f"ARI k-means={ak:.2f}  spectral={as_:.2f}")
    kernel_heatmap(); bloch(); amplitude_growth(); complexity_ladder()
    swap_test(); vqe_circuit(); separability(); funding_bars(); talent_gap()
    timeline(); nqm_targets(); advantage_quadrant()
    ligo_squeeze(); cern_clustering(); iter_plasma(); sensing_sensitivity(); data_deluge()
    print("ALL DIAGRAMS DONE")

# ---------- added for verbose deck v2 ----------
def kmeans_fail():
    from sklearn.datasets import make_moons
    from sklearn.cluster import KMeans
    X,y=make_moons(n_samples=300,noise=0.09,random_state=7)
    Xs=(X-X.mean(0))/X.std(0)
    km=KMeans(n_clusters=2,n_init=10,random_state=0).fit(Xs)
    fig,ax=plt.subplots(figsize=(6.6,4.6))
    for c,col in [(0,BLUE),(1,RED)]:
        m=km.labels_==c; ax.scatter(Xs[m,0],Xs[m,1],s=26,c=col,edgecolors="white",lw=.4)
    # draw the straight decision boundary between the two centroids
    ctr=km.cluster_centers_; mid=ctr.mean(0); d=ctr[1]-ctr[0]
    perp=np.array([-d[1],d[0]]); perp=perp/np.linalg.norm(perp)*3
    ax.plot([mid[0]-perp[0],mid[0]+perp[0]],[mid[1]-perp[1],mid[1]+perp[1]],"--",color=INK,lw=2)
    ax.scatter(ctr[:,0],ctr[:,1],marker="X",s=180,c=INK,edgecolors="white",lw=1.5,zorder=5)
    ax.set_title("k-means slices STRAIGHT through the crescents\n(nearest-centroid = a straight-line idea)",fontsize=12,fontweight="bold")
    ax.set_xticks([]);ax.set_yticks([]);ax.set_aspect("equal")
    for s in ax.spines.values(): s.set_color(LGRAY)
    save(fig,"kmeans_fail.png")

def curse():
    d=np.arange(1,120)
    rng=np.random.default_rng(0)
    ratio=[]
    for dim in d:
        X=rng.random((200,dim)); c=X[0]
        dist=np.sqrt(((X[1:]-c)**2).sum(1))
        ratio.append(dist.min()/dist.max())
    fig,ax=plt.subplots(figsize=(7.2,4.2))
    ax.plot(d,ratio,color=MAGENTA,lw=2.6)
    ax.axhline(1,ls=":",color=GRAY)
    ax.set_xlabel("number of dimensions  d",fontsize=11)
    ax.set_ylabel("nearest / farthest distance ratio",fontsize=11)
    ax.set_title("Curse of dimensionality: in high-D, every point is\nnearly equidistant — 'proximity' dissolves",fontsize=12,fontweight="bold")
    ax.set_ylim(0,1.05)
    for s in ("top","right"): ax.spines[s].set_visible(False)
    ax.grid(True,ls=":",color=LGRAY,alpha=.5)
    save(fig,"curse.png")

def featuremap():
    fig,ax=plt.subplots(figsize=(8,4.2));ax.set_xlim(0,10);ax.set_ylim(0,4.2);ax.axis("off")
    # data x -> circuit -> Hilbert space blob
    box(ax,0.3,1.7,1.6,0.9,"classical\ndata  x",TL1,fs=12)
    arrow(ax,2.0,2.15,3.0,2.15,INK)
    # circuit box
    box(ax,3.0,1.2,3.2,1.9,"",PANEL,tc=INK,ec=LGRAY,lw=1.2)
    ax.text(4.6,2.85,"parameterised circuit  φ",ha="center",fontsize=11,fontweight="bold",color=INK)
    for i,yy in enumerate([2.35,1.95,1.55]):
        ax.plot([3.25,6.0],[yy,yy],color=INK,lw=1.2)
        ax.add_patch(FancyBboxPatch((3.5+i*0.35,yy-0.14),0.28,0.28,boxstyle="round,pad=0.01",fc=BLUE,ec=BLUE))
        ax.add_patch(FancyBboxPatch((4.7,yy-0.14),0.28,0.28,boxstyle="round,pad=0.01",fc=PURPLE,ec=PURPLE))
    arrow(ax,6.3,2.15,7.2,2.15,INK)
    # hilbert space
    from matplotlib.patches import Ellipse
    ax.add_patch(Ellipse((8.5,2.1),2.6,2.6,fc=CY2,alpha=0.18,ec=BLUE,lw=1.5))
    ax.text(8.5,3.45,"high-dim Hilbert space",ha="center",fontsize=10.5,fontweight="bold",color=DEEPBLUE)
    rng=np.random.default_rng(2)
    a=rng.normal([8.0,1.9],0.28,(12,2)); b=rng.normal([9.1,2.5],0.28,(12,2))
    ax.scatter(a[:,0],a[:,1],s=26,c=BLUE,edgecolors="white",lw=.3,zorder=3)
    ax.scatter(b[:,0],b[:,1],s=26,c=TEAL,edgecolors="white",lw=.3,zorder=3)
    ax.text(4.6,0.5,"|φ(x)⟩ = state that encodes x — structure invisible classically becomes separable",
            ha="center",fontsize=10,color=GRAY,style="italic")
    save(fig,"featuremap.png")

def ml_map():
    fig,ax=plt.subplots(figsize=(8.4,4.4));ax.set_xlim(0,10);ax.set_ylim(0,4.4);ax.axis("off")
    box(ax,3.6,3.4,2.8,0.8,"Machine Learning",INK,fs=14)
    kids=[("Supervised","data + labels\npredict",TEAL,1.0),
          ("Unsupervised","data only\ndiscover structure",BLUE,4.0),
          ("Reinforcement","learn from reward\ncontrol",PURPLE,7.0)]
    for t,d,c,xx in kids:
        arrow(ax,5.0,3.35,xx+1.3,2.55,LGRAY,lw=1.6)
        big = t=="Unsupervised"
        box(ax,xx,1.2,2.6,1.3,"",c if big else PANEL,ec=c if big else LGRAY,lw=1.4)
        ax.text(xx+1.3,2.15,t,ha="center",fontsize=12.5,fontweight="bold",color="white" if big else INK)
        ax.text(xx+1.3,1.6,d,ha="center",fontsize=9.5,color="white" if big else GRAY)
    ax.text(5.3,0.55,"~80% of real-world data lives on the middle branch — no labels to learn from",
            ha="center",fontsize=10.5,color=GRAY,style="italic")
    save(fig,"ml_map.png")

if __name__ in ("__main__","builtins"):
    pass
