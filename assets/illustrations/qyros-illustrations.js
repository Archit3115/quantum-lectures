/* qyros illustration library · core
   full-figure flat-vector humans + props, ibm-illustration-school, qyros palette.
   two themes only: light (white) and dark (carbon). no indigo.
   consume: QyrosIllustrations.render(id, 'light'|'dark') -> svg string.        */
(function(){
'use strict';

/* ── helpers ─────────────────────────────────────────── */
function shade(hex,p){
  const n=parseInt(hex.slice(1),16);let r=n>>16,g=(n>>8)&255,b=n&255;
  const t=p<0?0:255,a=Math.abs(p);
  r=Math.round(r+(t-r)*a);g=Math.round(g+(t-g)*a);b=Math.round(b+(t-b)*a);
  return '#'+((r<<16|g<<8|b).toString(16).padStart(6,'0'));
}
const S=(d,fill)=>`<path d="${d}" fill="${fill}"/>`;
const L=(d,c,w)=>`<path d="${d}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round"/>`;
const C=(x,y,r,f)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${f}"/>`;
const R8=(x,y,w,h,rx,f)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${f}"/>`;
const G=(tx,ty,sc,inner)=>`<g transform="translate(${tx} ${ty})${sc&&sc!==1?` scale(${sc})`:''}">${inner}</g>`;
const FLIP=(inner)=>`<g transform="scale(-1,1)">${inner}</g>`;
const MONO=`font-family="'IBM Plex Mono',monospace"`;

/* ── themes (light + dark only) ──────────────────────── */
const themes={
  light:{name:'light',bg:'#FFFFFF',floor:'#E9EBEE',wall:'#F4F5F7',ink:'#161616',
    accent:'#01A982',accentSoft:'#B3FFE0',posterBg:'#E6FFF5',posterInk:'#01A982',
    label:'#525252',shadow:'rgba(0,0,0,0.08)',screenLine:'#C9CDD2'},
  dark:{name:'dark',bg:'#161616',floor:'#232527',wall:'#1E2022',ink:'#F4F4F4',
    accent:'#17EBA0',accentSoft:'#0E5C48',posterBg:'#22352D',posterInk:'#17EBA0',
    label:'#A8A8A8',shadow:'rgba(255,255,255,0.06)',screenLine:'#8A8F96'},
};

/* ── hair (side view; head center hx,hy, r15) ────────── */
function hairSide(st,hx,hy,hc){
  const s=shade;
  switch(st){
    case 'short':return S(`M ${hx-13},${hy-6} C ${hx-13},${hy-17} ${hx-5},${hy-21} ${hx+2},${hy-21} C ${hx+10},${hy-21} ${hx+15},${hy-16} ${hx+15},${hy-8} C ${hx+11},${hy-13} ${hx+5},${hy-15} ${hx-1},${hy-14} C ${hx-7},${hy-13} ${hx-11},${hy-10} ${hx-13},${hy-6} Z`,hc);
    case 'grayshort':return hairSide('short',hx,hy,hc);
    case 'buzz':return L(`M ${hx-12},${hy-7} C ${hx-8},${hy-14} ${hx-1},${hy-17} ${hx+6},${hy-17}`,hc,4);
    case 'bun':return hairSide('short',hx,hy,hc)+C(hx-15,hy-9,5.5,hc);
    case 'curly':return C(hx-10,hy-10,6,hc)+C(hx-3,hy-15,6.5,hc)+C(hx+5,hy-15,6.5,hc)+C(hx+12,hy-9,5.5,hc);
    case 'long':return hairSide('short',hx,hy,hc);
    case 'braid':return hairSide('short',hx,hy,hc);
    case 'turban':return S(`M ${hx-14},${hy-4} C ${hx-17},${hy-18} ${hx-8},${hy-26} ${hx+2},${hy-26} C ${hx+12},${hy-26} ${hx+18},${hy-18} ${hx+16},${hy-6} C ${hx+12},${hy-16} ${hx+5},${hy-21} ${hx-2},${hy-20} C ${hx-8},${hy-19} ${hx-12},${hy-12} ${hx-14},${hy-4} Z`,hc)
      +S(`M ${hx-14},${hy-4} C ${hx-15},${hy-14} ${hx-9},${hy-21} ${hx-1},${hy-22} L ${hx+3},${hy-14} C ${hx-4},${hy-14} ${hx-10},${hy-10} ${hx-14},${hy-4} Z`,s(hc,.14));
    case 'beanie':return S(`M ${hx-13},${hy-6} C ${hx-13},${hy-18} ${hx-4},${hy-23} ${hx+3},${hy-23} C ${hx+11},${hy-23} ${hx+16},${hy-17} ${hx+16},${hy-7} C ${hx+10},${hy-11} ${hx-6},${hy-11} ${hx-13},${hy-6} Z`,hc)
      +L(`M ${hx-13},${hy-6} C ${hx-6},${hy-10} ${hx+10},${hy-10} ${hx+15},${hy-7}`,s(hc,-.3),4);
    case 'hijab':return S(`M ${hx+14},${hy-9} C ${hx+12},${hy-21} ${hx+3},${hy-25} ${hx-4},${hy-24} C ${hx-13},${hy-22} ${hx-18},${hy-12} ${hx-17},${hy-2} C ${hx-17},${hy+8} ${hx-13},${hy+15} ${hx-8},${hy+18} C ${hx-11},${hy+7} ${hx-11},${hy-4} ${hx-8},${hy-10} C ${hx-3},${hy-17} ${hx+7},${hy-17} ${hx+14},${hy-9} Z`,hc);
    default:return '';
  }
}
/* behind-torso hair layers (long/braid/hijab drape) */
function hairBack(st,hx,hy,hc){
  if(st==='long')return S(`M ${hx-14},${hy-6} C ${hx-18},${hy+14} ${hx-18},${hy+36} ${hx-16},${hy+52} L ${hx-4},${hy+52} C ${hx-7},${hy+32} ${hx-7},${hy+12} ${hx-5},${hy-4} Z`,hc);
  if(st==='braid')return L(`M ${hx-12},${hy-4} C ${hx-15},${hy+12} ${hx-16},${hy+28} ${hx-15},${hy+46}`,hc,5.5)+C(hx-15,hy+50,3.2,hc);
  if(st==='hijab')return S(`M ${hx-16},${hy-2} C ${hx-19},${hy+16} ${hx-15},${hy+32} ${hx-7},${hy+38} L ${hx+5},${hy+36} C ${hx-3},${hy+24} ${hx-5},${hy+8} ${hx-3},${hy-4} Z`,hc);
  return '';
}
function beardSide(hx,hy,hc){
  return S(`M ${hx+15},${hy+3} C ${hx+14},${hy+12} ${hx+6},${hy+17} ${hx-2},${hy+15} C ${hx+5},${hy+12} ${hx+11},${hy+8} ${hx+15},${hy+3} Z`,hc);
}

/* ── figure poses (ground y=0, faces +x) ─────────────── */
/* p = {skin,hair,hairColor,top,bottom,shoe,earring,beard} */
function head(p,hx,hy){
  let s='';
  s+=`<rect x="${hx-6}" y="${hy+8}" width="12" height="16" fill="${shade(p.skin,-.08)}"/>`;
  /* squared qyros head — rounded-rect, not circle (linework dna, less ibm-round) */
  s+=`<rect x="${hx-13}" y="${hy-15}" width="27" height="30" rx="9" fill="${p.skin}"/>`;
  if(p.beard)s+=beardSide(hx,hy,p.hairColor);
  s+=hairSide(p.hair,hx,hy,p.hairColor);
  if(p.earring)s+=C(hx-7,hy+3,1.8,'#FFFFFF');
  return s;
}
function shoe(x,y,c,rx){return `<ellipse cx="${x}" cy="${y}" rx="${rx||9.5}" ry="5.2" fill="${c}"/>`;}
const torsoStand=(p)=>S(`M -17,-96 L -17,-146 Q -17,-160 -6,-160 L 10,-160 Q 17,-160 17,-148 L 17,-96 Z`,p.top);

const poses={
  stand(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 10,-132 12,-116 12,-102`,p.top,11)+C(12,-98,5.5,p.skin)
      +head(p,5,-184);
  },
  present(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 18,-147 30,-147 40,-153`,p.top,11)+C(44,-155,5.5,p.skin)
      +head(p,5,-184);
  },
  point(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 14,-162 20,-176 24,-190`,p.top,11)+C(25,-194,5.5,p.skin)
      +head(p,5,-184);
  },
  wave(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 15,-143 21,-153 23,-167`,p.top,11)+C(24,-172,5.5,p.skin)
      +head(p,5,-184);
  },
  walk(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C 6,-130 10,-118 12,-106`,shade(p.top,-.22),11)+C(12,-102,5.5,shade(p.skin,-.15))
      +L(`M -4,-96 C -8,-70 -14,-40 -20,-14`,shade(p.bottom,-.18),13)+shoe(-21,-8,shade(p.shoe,-.15))
      +L(`M 5,-96 C 10,-70 14,-40 17,-14`,p.bottom,13)+shoe(19,-8,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 2,-132 -2,-118 -4,-106`,p.top,11)+C(-4,-102,5.5,p.skin)
      +head(p,5,-184);
  },
  kneel(p){
    return hairBack(p.hair,7,-146,p.hairColor)
      +L(`M -4,-116 C 6,-124 16,-132 26,-138`,shade(p.top,-.22),11)+C(29,-140,5.5,shade(p.skin,-.15))
      +L(`M -2,-70 C -10,-46 -15,-28 -16,-12 C -18,-7 -28,-5 -36,-6`,shade(p.bottom,-.18),14)+shoe(-38,-5,shade(p.shoe,-.15),8)
      +L(`M 2,-70 C 12,-62 20,-54 22,-44 C 23,-32 23,-20 23,-10`,p.bottom,14)+shoe(26,-6,p.shoe)
      +S(`M -14,-68 L -16,-104 Q -17,-120 -6,-123 L 8,-122 Q 16,-119 16,-100 L 14,-70 Z`,p.top)
      +L(`M 2,-114 C 12,-120 24,-126 34,-130`,p.top,11)+C(37,-131,5.5,p.skin)
      +`<rect x="0" y="-138" width="11" height="14" fill="${shade(p.skin,-.08)}"/>`
      +`<rect x="-5" y="-160" width="25" height="28" rx="8.5" fill="${p.skin}"/>`
      +(p.beard?beardSide(7,-146,p.hairColor):'')
      +hairSide(p.hair,7,-146,p.hairColor)
      +(p.earring?C(0,-144,1.8,'#FFFFFF'):'');
  },
  sit(p){
    return hairBack(p.hair,4,-138,p.hairColor)
      +L(`M -3,-102 C 5,-96 13,-91 20,-88`,shade(p.top,-.22),10)+C(23,-87,5,shade(p.skin,-.15))
      +L(`M -4,-54 C 4,-55 12,-52 16,-46 C 18,-34 18,-20 17,-10`,shade(p.bottom,-.18),13)+shoe(19,-6,shade(p.shoe,-.15))
      +L(`M 0,-54 C 10,-55 18,-52 22,-48 C 24,-36 24,-22 23,-10`,p.bottom,13)+shoe(25,-6,p.shoe)
      +S(`M -12,-52 L -14,-102 Q -14,-116 -5,-116 L 8,-116 Q 14,-116 14,-106 L 12,-56 Z`,p.top)
      +L(`M 5,-104 C 14,-98 22,-92 30,-88`,p.top,10)+C(33,-87,5,p.skin)
      +`<rect x="-2" y="-126" width="11" height="13" fill="${shade(p.skin,-.08)}"/>`
      +`<rect x="-8" y="-152" width="25" height="28" rx="8.5" fill="${p.skin}"/>`
      +(p.beard?beardSide(4,-138,p.hairColor):'')
      +hairSide(p.hair,4,-138,p.hairColor)
      +(p.earring?C(-3,-136,1.8,'#FFFFFF'):'');
  },
  back(p){
    let hairFull=`<rect x="-10.5" y="-200" width="27" height="30" rx="9" fill="${p.hairColor}"/>`;
    if(p.hair==='bun')hairFull+=C(3,-190,6,p.hairColor);
    if(p.hair==='braid')hairFull+=L(`M 3,-176 C 2,-160 2,-150 2,-140`,p.hairColor,5.5)+C(2,-137,3.2,p.hairColor);
    if(p.hair==='hijab')hairFull=`<rect x="-12" y="-202" width="30" height="32" rx="10" fill="${p.hairColor}"/>`+S(`M -12,-182 C -14,-166 -10,-152 -2,-146 L 10,-148 C 2,-158 -1,-170 0,-182 Z`,p.hairColor);
    if(p.hair==='buzz'||p.hair==='bald')hairFull=`<rect x="-10" y="-199" width="26" height="29" rx="9" fill="${p.skin}"/>`+L(`M -9,-192 C -4,-197 6,-198 12,-194`,p.hairColor,3);
    return L(`M -8,-150 C -11,-132 -12,-116 -12,-102`,shade(p.top,-.12),11)+C(-12,-98,5.5,p.skin)
      +L(`M -7,-96 L -8,-14`,shade(p.bottom,-.12),13)+shoe(-8,-8,shade(p.shoe,-.1),8)
      +L(`M 7,-96 L 8,-14`,p.bottom,13)+shoe(8,-8,p.shoe,8)
      +S(`M -18,-96 L -18,-148 Q -18,-161 -6,-161 L 11,-161 Q 21,-161 21,-148 L 21,-96 Z`,p.top)
      +L(`M 9,-152 C 18,-164 25,-176 29,-188`,p.top,11)+C(30,-192,5.5,p.skin)
      +`<rect x="-3" y="-172" width="12" height="14" fill="${shade(p.skin,-.08)}"/>`
      +hairFull;
  },
  think(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-150 C 16,-144 20,-156 15,-168`,p.top,11)+C(14,-171,5.5,p.skin)
      +head(p,5,-184);
  },
  cheer(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-150 C -7,-164 -12,-178 -15,-190`,shade(p.top,-.22),11)+C(-16,-194,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +L(`M 7,-152 C 14,-166 20,-180 24,-192`,p.top,11)+C(25,-196,5.5,p.skin)
      +head(p,5,-184);
  },
  carry(p){
    return hairBack(p.hair,5,-184,p.hairColor)
      +L(`M 0,-148 C -3,-130 -5,-116 -5,-103`,shade(p.top,-.22),11)+C(-5,-99,5.5,shade(p.skin,-.15))
      +L(`M -6,-96 L -7,-14`,shade(p.bottom,-.18),13)+shoe(-6,-7,shade(p.shoe,-.15))
      +L(`M 6,-96 L 7,-14`,p.bottom,13)+shoe(9,-7,p.shoe)
      +torsoStand(p)
      +`<rect x="8" y="-134" width="28" height="6" rx="1.5" fill="#24272B"/>`
      +`<rect x="10" y="-131" width="24" height="2" fill="#3A3E44"/>`
      +L(`M 7,-150 C 12,-138 17,-130 24,-126`,p.top,11)+C(26,-124,5.5,p.skin)
      +head(p,5,-184);
  },
};

/* ── identities ──────────────────────────────────────── */
const identities=[
  {id:'amara', skin:'#8D5524',hair:'curly',    hairColor:'#161616',top:'#01A982',bottom:'#30353B',shoe:'#4A4F55',earring:1},
  {id:'meera', skin:'#C68642',hair:'long',     hairColor:'#211A14',top:'#7BE0C2',bottom:'#43484F',shoe:'#8A8F96'},
  {id:'jae',   skin:'#E0AC69',hair:'beanie',   hairColor:'#3B4046',top:'#2A2A2A',bottom:'#5A5F66',shoe:'#4A4F55'},
  {id:'tavleen',skin:'#A96A3C',hair:'turban',  hairColor:'#2E3238',top:'#F4F4F4',bottom:'#30353B',shoe:'#4A4F55',beard:1},
  {id:'noor',  skin:'#C68642',hair:'hijab',    hairColor:'#6F7378',top:'#2E3238',bottom:'#23272C',shoe:'#4A4F55'},
  {id:'leo',   skin:'#F1C27D',hair:'short',    hairColor:'#6B4A2B',top:'#6F6F6F',bottom:'#30353B',shoe:'#8A8F96'},
  {id:'zuri',  skin:'#8D5524',hair:'bun',      hairColor:'#161616',top:'#5E8C7F',bottom:'#43484F',shoe:'#4A4F55',earring:1},
  {id:'petra', skin:'#F1C27D',hair:'grayshort',hairColor:'#C9CDD2',top:'#2A2A2A',bottom:'#5A5F66',shoe:'#8A8F96'},
  {id:'dev',   skin:'#C68642',hair:'short',    hairColor:'#161616',top:'#F4F4F4',bottom:'#30353B',shoe:'#4A4F55'},
  {id:'ines',  skin:'#E0AC69',hair:'braid',    hairColor:'#3A2A1A',top:'#01A982',bottom:'#23272C',shoe:'#4A4F55',earring:1},
  {id:'kofi',  skin:'#8D5524',hair:'buzz',     hairColor:'#161616',top:'#7BE0C2',bottom:'#43484F',shoe:'#4A4F55'},
  {id:'sam',   skin:'#F1C27D',hair:'long',     hairColor:'#B0B0B0',top:'#2E3238',bottom:'#5A5F66',shoe:'#8A8F96'},
];
const byId={};identities.forEach(i=>byId[i.id]=i);
function fig(idName,pose){return poses[pose](byId[idName]);}

/* ── props (anchored: ground/left origin unless noted) ─ */
/* the approved v3 qyros mark — 8-petal vesica mandala (same geometry as brand-logo card) */
function qyMark(cx,cy,sc,col){
  const petal='M0 -42 C 12.6 -26, 12.6 -10, 0 -2 C -12.6 -10, -12.6 -26, 0 -42 Z';
  let g=`<g transform="translate(${cx} ${cy}) scale(${sc})" fill="none" stroke="${col}" stroke-width="${(2.2/sc).toFixed(2)}" stroke-linecap="round">`;
  for(let a=0;a<360;a+=45)g+=`<path d="${petal}" transform="rotate(${a})"/>`;
  g+=(sc>=0.5?`<circle r="2.2" fill="${col}" stroke="none"/>`:'')+`</g>`;
  return g;
}

const props={
  chandelier(t){ /* draws downward from origin top-center, ~w110 h180 · unapologetic gold */
    let s='';
    s+=R8(-36,0,72,14,2,'#C9A227')+R8(-24,14,48,10,2,'#8C6D1F');
    s+=R8(-5,10,10,152,0,'#6B5416');
    [[30,34],[72,26],[112,18]].forEach(([y,half])=>{
      s+=R8(-half-6,y,(half+6)*2,8,2,'#D9B23A');
      [-1,1].forEach(dir=>{
        for(let i=1;i<=2;i++){
          const x=dir*(10+i*11);
          s+=R8(x-1.8,y+8,3.6,20-i*4,0,'#E3C05C');
          s+=R8(x-3.5,y+26-i*4,7,7,1,'#8C6D1F');
        }
      });
      s+=R8(-9,y-6,18,20,2,'#5C4813');
    });
    s+=R8(-24,152,10,20,2,'#8C6D1F')+R8(-6,150,12,26,2,'#6B5416')+R8(13,152,10,20,2,'#8C6D1F');
    return s;
  },
  casedQuantum(t){ /* closed-case quantum computer · ground origin · w130 h212 */
    let s='';
    s+=R8(15,-212,100,12,3,'#4A4F55');
    s+=R8(55,-200,20,16,2,'#6F7378');
    s+=`<rect x="10" y="-184" width="110" height="158" rx="26" fill="#EDEDEF"/>`;
    s+=`<rect x="10" y="-184" width="110" height="158" rx="26" fill="none" stroke="#C9CDD2" stroke-width="1.5"/>`;
    s+=`<path d="M 42,-178 V -36 M 88,-178 V -36" stroke="#DCDCDF" stroke-width="1.5" fill="none"/>`;
    s+=R8(24,-62,82,26,11,'#D8DADD');
    s+=C(65,-49,3,t.accent);
    s+=qyMark(65,-128,0.32,'#4A4F55');
    return s;
  },
  quantumPanel(t){ /* cabinet wall, origin bottom-left, w300 h up 320 */
    let s='';
    s+=S('M 0,-320 L 300,-320 L 300,0 L 0,0 Z','#EDEDEF');
    s+=S('M 0,-320 L 300,-320 L 296,-286 L 4,-286 Z','#F7F7F8');
    [[8,66],[74,66],[226,66],[160,0]].forEach(()=>{});
    s+=R8(14,-276,52,252,4,'#E4E4E7')+R8(22,-266,36,232,3,'#DBDBDE');
    s+=R8(234,-276,52,252,4,'#E4E4E7')+R8(242,-266,36,232,3,'#DBDBDE');
    s+=`<line x1="72" y1="-320" x2="72" y2="0" stroke="#DCDCDF" stroke-width="2"/><line x1="228" y1="-320" x2="228" y2="0" stroke="#DCDCDF" stroke-width="2"/>`;
    s+=R8(86,-272,128,212,2,'#D6D6DA');
    s+=G(150,-262,0.92,props.chandelier(t));
    return s;
  },
  serverRack(t){
    let s=R8(0,-210,90,210,6,'#26282C');
    for(let i=0;i<7;i++){
      const y=-198+i*27;
      s+=R8(8,y,74,17,2,'#33363B');
      s+=C(74,y+8.5,2.6,t.accent);
      s+=R8(14,y+5,34,2.5,1,'#4A4E54')+R8(14,y+10,24,2.5,1,'#4A4E54');
    }
    return s;
  },
  desk(t){
    return S('M 24,-68 L 54,-68 L 46,-6 L 30,-6 Z','#DCDEE1')
      +S('M 156,-68 L 186,-68 L 178,-6 L 162,-6 Z','#DCDEE1')
      +R8(0,-80,210,12,3,'#B7BCC2')+R8(0,-80,210,4,2,'#CDD2D8');
  },
  chair(t){
    let s='';
    s+=R8(44,-110,11,56,5,'#9BA8B4')+R8(44,-110,11,10,5,shade('#9BA8B4',-.15));
    s+=R8(-2,-62,56,11,4,'#9BA8B4');
    s+=R8(22,-51,7,28,2,'#4A4F55');
    [[-16,0],[6,4],[28,4],[50,0]].forEach(([dx])=>{ s+=L(`M 25,-24 L ${25+dx>25?25+ (dx-25)/1:dx+25-25||0},-8`,'#4A4F55',0);});
    s+=L('M 25,-24 L 3,-8','#4A4F55',5)+L('M 25,-24 L 47,-8','#4A4F55',5)+L('M 25,-24 L 25,-8','#4A4F55',5);
    s+=C(3,-7,4,'#33363B')+C(47,-7,4,'#33363B')+C(25,-7,4,'#33363B');
    return s;
  },
  laptop(t){ /* origin at surface line, opens facing -x (screen back at +x) */
    return S('M 8,-42 L 56,-42 L 60,-1 L 4,-1 Z','#24272B')
      +R8(11,-37,42,31,2,'#15171A')
      +R8(16,-32,22,3,1,t.accent)+R8(16,-26,30,3,1,'#7BE0C2')+R8(16,-20,18,3,1,'#8A8F96')
      +S('M 0,0 L 64,0 L 58,5 L 6,5 Z','#2E3237');
  },
  wallScreenChart(t){ /* origin top-left, w230 h140 */
    let s=R8(0,0,230,140,8,'#26282C')+R8(9,9,212,110,4,'#101214');
    s+=`<path d="M 22,52 L 208,52" stroke="#4A4E54" stroke-width="2" stroke-dasharray="5 4"/>`;
    s+=`<polyline points="22,44 50,40 78,46 106,38 134,42 162,34 190,36 208,30" fill="none" stroke="${t.accent}" stroke-width="2.5"/>`;
    [[22,44],[78,46],[134,42],[190,36]].forEach(([x,y])=>s+=C(x,y,2.6,t.accent));
    s+=`<polyline points="22,92 50,88 78,94 106,90 134,84 162,88 190,82 208,84" fill="none" stroke="#C9CDD2" stroke-width="2.5"/>`;
    for(let i=0;i<4;i++)s+=R8(14+i*38,126,30,8,4,'#33363B');
    return s;
  },
  wallScreenCall(t){ /* w230 h140 */
    let s=R8(0,0,230,140,8,'#26282C');
    s+=R8(9,9,138,122,4,'#101214');
    s+=`<polyline points="20,64 44,58 68,66 92,56 116,62 138,52" fill="none" stroke="${t.accent}" stroke-width="2.5"/>`;
    s+=`<polyline points="20,96 44,92 68,98 92,90 116,94 138,88" fill="none" stroke="#C9CDD2" stroke-width="2"/>`;
    s+=R8(16,18,52,8,3,'#33363B');
    const tiles=[['#F1C27D','#B0B0B0','#6F6F6F'],['#C68642','#161616','#01A982'],['#A96A3C','#2E3238','#7BE0C2']];
    tiles.forEach((tt,i)=>{
      const y=9+i*42;
      s+=R8(153,y,68,38,4,'#33363B');
      s+=C(187,y+18,9,tt[0]);
      s+=S(`M 172,${y+38} C 174,${y+28} 181,${y+24} 187,${y+24} C 193,${y+24} 200,${y+28} 202,${y+38} Z`,tt[2]);
      s+=S(`M 178,${y+12} C 181,${y+8} 193,${y+8} 196,${y+13} C 192,${y+10} 182,${y+10} 178,${y+12} Z`,tt[1]);
    });
    return s;
  },
  whiteboard(t){ /* origin top-left w200 h140 */
    let s=R8(0,0,200,140,4,'#B9BEC4')+R8(5,5,190,130,2,'#FBFBFC');
    const st=[[30,26,t.accent],[52,20,'#9BA8B4'],[74,30,t.accent==='#17EBA0'?'#0FA57A':'#B3FFE0'],[96,24,'#C9CDD2'],[58,48,t.accent],[84,54,'#B3FFE0'],[110,46,'#9BA8B4'],[126,70,t.accent],[100,80,'#C9CDD2'],[148,88,'#B3FFE0']];
    st.forEach(([x,y,c])=>s+=R8(x,y,14,14,1.5,c));
    s+=L('M 118,30 C 134,32 144,40 146,54','#8A8F96',2.5)+S('M 143,50 L 148,60 L 151,49 Z','#8A8F96');
    s+=L('M 138,74 C 152,80 158,92 158,104','#8A8F96',2.5)+S('M 154,100 L 159,110 L 163,99 Z','#8A8F96');
    return s;
  },
  podium(t){ /* origin bottom-left w96 h150 */
    return S('M 10,0 L 86,0 L 79,-150 L 17,-150 Z','#F0F0F2')
      +S('M 10,0 L 26,0 L 30,-150 L 17,-150 Z','#D8DADD')
      +R8(34,-140,40,64,4,'#26282C')
      +qyMark(54,-108,0.29,t.posterInk)
      +L('M 62,-150 C 66,-158 72,-162 78,-163','#4A4F55',3)+C(79,-163,3,'#26282C');
  },
  posterWall(t){ /* origin top-left w86 h108 */
    let s=R8(0,0,86,108,6,t.posterBg);
    [[8,8],[78,8],[8,100],[78,100]].forEach(([x,y])=>s+=C(x,y,2,'#7D8288'));
    s+=qyMark(43,50,0.40,t.posterInk);
    s+=R8(24,82,38,4,2,t.posterInk);
    return s;
  },
  globeCode(t){ /* origin top-left w260 h210 · qyros dot-lattice globe · qpu network */
    const dot=t.name==='dark'?'#5A5F66':'#B9BEC4';
    const ink=t.name==='dark'?'#8A8F96':'#4A4F55';
    let s='';
    s+=`<defs><pattern id="qy-glbdot-${t.name}" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="${dot}"/></pattern></defs>`;
    s+=`<circle cx="116" cy="112" r="76" fill="url(#qy-glbdot-${t.name})"/>`;
    s+=`<circle cx="116" cy="112" r="76" fill="none" stroke="${ink}" stroke-width="1.25"/>`;
    s+=`<ellipse cx="116" cy="112" rx="76" ry="25" fill="none" stroke="${ink}" stroke-width="0.9" stroke-dasharray="3 3"/>`;
    s+=`<ellipse cx="116" cy="112" rx="25" ry="76" fill="none" stroke="${ink}" stroke-width="0.9" stroke-dasharray="3 3"/>`;
    /* routes: dashed carbon = planned, one solid green = active (with arrowhead) */
    s+=`<path d="M 70,75 C 96,46 148,50 170,86" fill="none" stroke="${ink}" stroke-width="1" stroke-dasharray="4 3"/>`;
    s+=`<path d="M 70,75 C 86,118 118,148 160,140" fill="none" stroke="${t.accent}" stroke-width="1.6"/>`;
    s+=`<path d="M 152,134 l 10,6 -8,7" fill="none" stroke="${t.accent}" stroke-width="1.6" stroke-linecap="round"/>`;
    /* site nodes = square terminals; active site green */
    s+=R8(66,71,8,8,0,ink)+R8(166,82,8,8,0,ink)+R8(156,136,8,8,0,t.accent);
    /* wire from node up to docked qyros terminal window */
    s+=`<path d="M 170,86 L 170,66 L 196,66" fill="none" stroke="${ink}" stroke-width="1"/>`;
    s+=G(158,4,0.62,props.terminalWindow(t));
    s+=`<text x="6" y="204" ${MONO} font-size="9" fill="${t.label}">qpu network · 3 sites · one active route</text>`;
    return s;
  },
  plant(t){
    return `<ellipse cx="30" cy="-52" rx="7" ry="20" fill="#2F7A63" transform="rotate(-24 30 -52)"/>`
      +`<ellipse cx="30" cy="-56" rx="7" ry="22" fill="#3F9478"/>`
      +`<ellipse cx="30" cy="-52" rx="7" ry="20" fill="#256652" transform="rotate(24 30 -52)"/>`
      +S('M 14,-34 L 46,-34 L 41,-2 L 19,-2 Z','#6F7378')+R8(12,-38,36,6,2,'#5A5F60');
  },
  /* ── environment kit (v3 additions) ── */
  blackboard(t){ /* top-left, w200 h140 */
    let s=R8(0,0,200,140,3,'#4A4F55')+R8(6,6,188,128,2,'#22262A');
    s+=`<g stroke="${t.name==='dark'?'#17EBA0':'#2FD9A5'}" stroke-width="1.6" fill="none" stroke-linecap="round" opacity="0.9">`
      +`<path d="M18 30 C 30 24, 44 34, 58 28"/><path d="M18 46 C 36 40, 52 50, 74 44"/>`
      +`<path d="M96 28 h44 M104 28 v22 M132 28 v22 M96 50 h44"/><circle cx="118" cy="39" r="7"/>`
      +`<path d="M20 76 C 40 70, 60 82, 84 74"/><path d="M20 96 C 46 90, 70 100, 96 92"/>`
      +`<path d="M120 78 l16 16 M136 78 l-16 16"/><path d="M150 92 c 6 -12, 18 -12, 24 0"/>`
      +`</g>`;
    s+=R8(60,140,80,6,2,'#4A4F55');
    return s;
  },
  tv(t){ /* ground origin, w170 */
    let s=L('M 70,-8 L 85,-72','#4A4F55',5)+L('M 100,-8 L 85,-72','#4A4F55',5)+R8(40,-10,90,6,2,'#4A4F55');
    s+=R8(0,-170,170,100,6,'#26282C')+R8(8,-162,154,84,3,'#101214');
    s+=`<polyline points="20,-104 46,-112 72,-102 98,-118 124,-108 150,-122" fill="none" stroke="${t.accent}" stroke-width="2.4"/>`;
    s+=`<polyline points="20,-90 46,-94 72,-88 98,-96 124,-90 150,-98" fill="none" stroke="#C9CDD2" stroke-width="1.8"/>`;
    s+=R8(16,-152,44,6,2,'#33363B');
    return s;
  },
  quantumChip(t){ /* top-left w84 h84 */
    let s=R8(0,0,84,84,5,'#26282C')+R8(14,14,56,56,3,'#33363B');
    for(let i=0;i<3;i++){s+=R8(22,22+i*16,40,2,0,'#4A4E54');s+=R8(22+i*16,22,2,40,0,'#4A4E54');}
    [[8,8],[68,8],[8,68],[68,68]].forEach(([x,y])=>s+=R8(x,y,8,8,1.5,t.accent));
    for(let i=0;i<4;i++){s+=R8(20+i*14,-6,4,8,0,'#6F7378');s+=R8(20+i*14,82,4,8,0,'#6F7378');}
    return s;
  },
  bookshelf(t){ /* ground, w110 h180 */
    let s=R8(0,-180,110,180,3,'#B7BCC2')+R8(6,-174,98,168,2,'#E7E9EC');
    [[-168,'#'],[-116,'#'],[-64,'#']].forEach(([y],i)=>{
      const cols=[['#4A4F55',10],['#6F7378',8],[t.accent,7],['#9BA8B4',12],['#3A3E44',9],['#8A8F96',8]];
      let x=12;s+=R8(6,y+46,98,6,1,'#B7BCC2');
      cols.slice(0,4+(i%2)).forEach(([c,w],j)=>{s+=R8(x,y+8+(j%2?4:0),w,38-(j%2?4:0),1,c);x+=w+4;});
    });
    return s;
  },
  sofa(t){ /* ground, w170 */
    return R8(0,-86,170,34,8,'#9BA8B4')
      +R8(0,-60,170,34,8,shade('#9BA8B4',-.12))
      +R8(-8,-70,22,48,8,'#8A97A3')+R8(156,-70,22,48,8,'#8A97A3')
      +R8(8,-26,10,20,2,'#4A4F55')+R8(152,-26,10,20,2,'#4A4F55');
  },
  coffeeMachine(t){ /* ground on counter-line, w70 */
    return R8(0,-100,70,72,4,'#33363B')+R8(10,-92,50,20,2,'#101214')
      +R8(26,-64,18,10,1,'#4A4F55')
      +R8(24,-40,22,14,2,'#F0F0F2')+L('M 46,-38 C 52,-38 52,-30 46,-30','#F0F0F2',3)
      +C(35,-96,2.5,t.accent)
      +R8(-6,-28,82,4,2,'#B7BCC2');
  },
  waterCooler(t){ /* ground, w46 */
    return `<path d="M 8,-140 h30 v18 h-30 z" fill="${t.name==='dark'?'#2E4A40':'#CDEDE2'}" stroke="none"/>`
      +R8(4,-122,38,94,4,'#E7E9EC')+R8(4,-122,38,10,4,'#C9CDD2')
      +R8(14,-98,18,4,2,'#9BA8B4')+C(23,-86,3,t.accent)
      +R8(8,-28,30,6,2,'#B7BCC2');
  },
  windowWall(t){ /* top-left, w170 h130 */
    const sky=t.name==='dark'?'#1E2A33':'#E8F3EE';
    let s=R8(0,0,170,130,3,'#B7BCC2')+R8(6,6,158,118,2,sky);
    s+=t.name==='dark'?C(130,34,12,'#C9CDD2')+C(124,30,10,sky):C(132,32,13,'#F5D66B');
    s+=`<path d="M20 96 l22 -20 16 12 24 -24 20 14" fill="none" stroke="${t.name==='dark'?'#3A4A54':'#C3D9CF'}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>`;
    s+=R8(82,6,6,118,0,'#B7BCC2')+R8(6,62,158,6,0,'#B7BCC2');
    return s;
  },
  door(t){ /* ground, w76 h190 */
    return R8(0,-190,76,190,2,'#B7BCC2')+R8(7,-183,62,183,1,'#E7E9EC')
      +R8(14,-176,48,80,1,'#D8DBDE')+R8(14,-86,48,74,1,'#D8DBDE')
      +C(58,-96,3.5,'#4A4F55');
  },
  rug(t){
    return `<ellipse cx="0" cy="-4" rx="88" ry="14" fill="${t.name==='dark'?'#26282B':'#E4E7EA'}"/>`
      +`<ellipse cx="0" cy="-4" rx="62" ry="9" fill="none" stroke="${t.name==='dark'?'#33363B':'#CDD2D8'}" stroke-width="2"/>`;
  },
  ceilingLight(t){ /* hangs from y=0 downward */
    return L('M 0,0 L 0,54','#4A4F55',2)
      +`<path d="M -26,78 L 26,78 L 16,54 L -16,54 Z" fill="#33363B"/>`
      +`<ellipse cx="0" cy="80" rx="20" ry="5" fill="${t.name==='dark'?'#17EBA0':'#F5D66B'}" opacity="0.5"/>`;
  },
  kanban(t){ /* top-left, w170 h120 */
    let s=R8(0,0,170,120,3,'#B7BCC2')+R8(5,5,160,110,2,'#FBFBFC');
    ['todo','doing','done'].forEach((h,i)=>{
      const x=12+i*52;
      s+=R8(x,12,44,10,2,i===1?t.accent:'#C9CDD2');
      const rows=[3,2,4][i];
      for(let r=0;r<rows;r++)s+=R8(x+4,30+r*20,36,14,1.5,r===0&&i===1?'#B3FFE0':'#E4E7EA');
    });
    return s;
  },
  monitorDual(t){ /* sits on surface line y=0, w150 */
    let s='';
    [[0,'#101214'],[78,'#101214']].forEach(([x])=>{
      s+=R8(x,-64,72,46,3,'#26282C')+R8(x+5,-59,62,36,2,'#101214');
      s+=R8(x+10,-52,30,3,1,t.accent)+R8(x+10,-45,44,3,1,'#8A8F96')+R8(x+10,-38,24,3,1,'#8A8F96');
      s+=R8(x+31,-18,10,12,1,'#4A4F55')+R8(x+22,-6,28,4,2,'#4A4F55');
    });
    return s;
  },
  plantTall(t){ /* ground, taller ficus */
    return L('M 30,-36 C 28,-70 32,-100 30,-124','#6B4A2B',4)
      +`<ellipse cx="18" cy="-118" rx="14" ry="22" fill="#2F7A63" transform="rotate(-18 18 -118)"/>`
      +`<ellipse cx="42" cy="-126" rx="13" ry="20" fill="#3F9478" transform="rotate(16 42 -126)"/>`
      +`<ellipse cx="30" cy="-142" rx="12" ry="20" fill="#256652"/>`
      +S('M 14,-38 L 46,-38 L 41,-2 L 19,-2 Z','#6F7378')+R8(12,-42,36,6,2,'#5A5F60');
  },
  wallClock(t){ /* centered origin */
    return C(0,0,17,'#F4F5F7')+`<circle cx="0" cy="0" r="17" fill="none" stroke="#4A4F55" stroke-width="2.5"/>`
      +L('M 0,0 L 0,-10','#161616',2)+L('M 0,0 L 7,4','#161616',2)+C(0,0,1.8,t.accent);
  },
  glassPanel(t,w,h){ /* liquid-glass hud card · origin top-left · translucent, specular top, hairline */
    w=w||150;h=h||96;
    const gid=`qy-glassg-${t.name}-${w}x${h}`;
    const fill=t.name==='dark'?'rgba(255,255,255,0.09)':'rgba(255,255,255,0.55)';
    const brd=t.name==='dark'?'rgba(255,255,255,0.28)':'rgba(255,255,255,0.95)';
    const edge=t.name==='dark'?'rgba(255,255,255,0.12)':'rgba(0,0,0,0.10)';
    const ink=t.name==='dark'?'#F4F4F4':'#161616';
    let s=`<defs><linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="${t.name==='dark'?0.22:0.8}"/><stop offset="0.42" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient></defs>`;
    s+=`<rect width="${w}" height="${h}" rx="14" fill="${fill}"/>`;
    s+=`<rect width="${w}" height="${h}" rx="14" fill="url(#${gid})"/>`;
    s+=`<rect x="0.75" y="0.75" width="${w-1.5}" height="${h-1.5}" rx="13" fill="none" stroke="${brd}" stroke-width="1.4"/>`;
    s+=`<rect width="${w}" height="${h}" rx="14" fill="none" stroke="${edge}" stroke-width="1"/>`;
    s+=R8(12,12,Math.min(56,w*0.38),5,2.5,t.name==='dark'?'#8A8F96':'#7D8288');
    s+=`<text x="12" y="${Math.round(h*0.52)}" ${MONO} font-size="15" font-weight="300" fill="${ink}">8ms</text>`;
    s+=`<polyline points="12,${h-16} ${Math.round(12+(w-24)*0.25)},${h-24} ${Math.round(12+(w-24)*0.5)},${h-18} ${Math.round(12+(w-24)*0.75)},${h-30} ${w-12},${h-22}" fill="none" stroke="${t.accent}" stroke-width="2" stroke-linecap="round"/>`;
    return s;
  },
  terminalWindow(t){ /* origin top-left w150 h100 */
    let s=R8(0,0,150,100,8,'#1B1E22')+R8(0,0,150,18,8,'#26282C')+R8(0,10,150,8,0,'#26282C');
    s+=C(12,9,3,'#5A5F66')+C(24,9,3,'#5A5F66')+C(36,9,3,t.accent);
    s+=R8(12,28,58,4,1.5,t.accent)+R8(12,40,92,4,1.5,'#8A8F96')+R8(12,52,74,4,1.5,'#8A8F96')+R8(12,64,100,4,1.5,'#7BE0C2')+R8(12,76,44,4,1.5,'#8A8F96');
    return s;
  },
};

window.QyrosIllustrationsCore={themes,shade,S,L,C,R8,G,FLIP,MONO,identities,byId,fig,poses,props,qyMark};
})();
