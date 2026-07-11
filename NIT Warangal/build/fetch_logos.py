import os, urllib.request, io
from PIL import Image
DST="/Users/sentry/Work/Lectures/NIT Warangal/template_assets/logos"
os.makedirs(DST,exist_ok=True)
for f in os.listdir(DST):
    if f.endswith(".png"): os.remove(os.path.join(DST,f))
COMPANIES={
 "ibm":"ibm.com","google":"google.com","deepmind":"deepmind.google","dwave":"dwavesys.com",
 "quantinuum":"quantinuum.com","psiquantum":"psiquantum.com","jpmorgan":"jpmorganchase.com",
 "qcware":"qcware.com","totalenergies":"totalenergies.com","algorithmiq":"algorithmiq.fi",
 "qpiai":"qpiai.tech","tcs":"tcs.com","lt":"lntecc.com","qnu":"qnulabs.com",
 "mckinsey":"mckinsey.com","bcg":"bcg.com","cern":"home.cern","iter":"iter.org",
 "skao":"skao.int","fermilab":"fnal.gov","caltech":"caltech.edu","iisc":"iisc.ac.in",
 "iitmadras":"iitm.ac.in","nitw":"nitw.ac.in",
}
def fetch(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    return urllib.request.urlopen(req,timeout=20).read()
ok=[];fail=[]
for name,dom in COMPANIES.items():
    got=None
    for url in (f"https://icons.duckduckgo.com/ip3/{dom}.ico",
                f"https://www.google.com/s2/favicons?domain={dom}&sz=128"):
        try:
            data=fetch(url)
            im=Image.open(io.BytesIO(data)).convert("RGBA")
            if im.width>=24: got=im; break
        except Exception: continue
    if got is not None:
        # upscale small favicons a touch for crisper placement
        if got.width<96:
            s=96/got.width; got=got.resize((96,int(got.height*s)),Image.LANCZOS)
        got.save(os.path.join(DST,f"{name}.png")); ok.append(name)
    else: fail.append(name)
print(f"logos ok ({len(ok)}):", " ".join(ok))
print(f"failed ({len(fail)}):", " ".join(fail))
