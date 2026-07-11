/* qy monoline · the qyros custom display alphabet
   formalized stroke-font: a-z, 0-9, punctuation. 40-unit grid.
   consume: QyMonoline.text('building the unknown',{size:64,weight:'bold',color:'#01A982'})
   returns a standalone <svg> string. metrics in QyMonoline.metrics.            */
(function(){
'use strict';
const P=(d)=>`<path d="${d}"/>`;
const CIR=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}"/>`;
const DOT=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="currentColor" stroke="none"/>`;
const G={
  'a':{w:22,m:CIR(11,-14,11)+P('M22,-25 L22,0')},
  'b':{w:24,m:P('M2,-40 L2,0')+CIR(13,-14,11)},
  'c':{w:22,m:P('M19.4,-21.1 A11,11 0 1 0 19.4,-6.9')},
  'd':{w:24,m:CIR(11,-14,11)+P('M22,-40 L22,0')},
  'e':{w:22,m:CIR(11,-14,11)+P('M2,-14 L20,-14')},
  'f':{w:21,m:P('M12,0 L12,-31 Q12,-40 21,-40')+P('M4,-27 L19,-27')},
  'g':{w:24,m:CIR(11,-14,11)+P('M22,-25 L22,3 Q22,12 12,12 Q6,12 3,8')},
  'h':{w:24,m:P('M2,-40 L2,0')+P('M2,-15 Q2,-26 12,-26 Q22,-26 22,-15 L22,0')},
  'i':{w:8,m:P('M4,-27 L4,0')+DOT(4,-36,2.4)},
  'j':{w:14,m:P('M10,-27 L10,3 Q10,12 1,12')+DOT(10,-36,2.4)},
  'k':{w:23,m:P('M2,-40 L2,0')+P('M20,-27 L2,-11')+P('M8,-16 L21,0')},
  'l':{w:11,m:P('M4,-40 L4,-5 Q4,0 9,0')},
  'm':{w:34,m:P('M2,0 L2,-27')+P('M2,-16 Q2,-27 10,-27 Q17,-27 17,-16 L17,0')+P('M17,-16 Q17,-27 25,-27 Q32,-27 32,-16 L32,0')},
  'n':{w:24,m:P('M2,0 L2,-27')+P('M2,-15 Q2,-27 12,-27 Q22,-27 22,-15 L22,0')},
  'o':{w:24,m:CIR(12,-14,11.5)},
  'p':{w:24,m:P('M2,-27 L2,12')+CIR(13,-14,11)},
  'q':{w:24,m:CIR(11,-14,11)+P('M22,-27 L22,12')},
  'r':{w:22,m:P('M2,0 L2,-27')+P('M2,-15 Q2,-26 11,-27 Q17,-27 21,-23')},
  's':{w:24,m:P('M20,-23 Q20,-28 12,-28 Q4,-28 4,-22 Q4,-16 12,-15 Q21,-14 21,-7 Q21,0 12,0 Q3,0 3,-6')},
  't':{w:19,m:P('M9,-38 L9,-7 Q9,0 17,0')+P('M2,-27 L17,-27')},
  'u':{w:22,m:P('M2,-27 L2,-11 Q2,0 11,0 Q20,0 20,-11 L20,-27')+P('M20,-27 L20,0')},
  'v':{w:22,m:P('M2,-27 L11,0 L20,-27')},
  'w':{w:30,m:P('M2,-27 L8,0 L15,-19 L22,0 L28,-27')},
  'x':{w:22,m:P('M2,-27 L20,0')+P('M20,-27 L2,0')},
  'y':{w:22,m:P('M2,-27 L11,-3')+P('M20,-27 L9,6 Q6,12 0,12')},
  'z':{w:23,m:P('M3,-27 L20,-27 L3,0 L20,0')},
  '0':{w:24,m:`<ellipse cx="12" cy="-20" rx="10" ry="19"/>`},
  '1':{w:22,m:P('M5,-32 Q10,-34 13,-40 L13,0')+P('M4,0 L21,0')},
  '2':{w:24,m:P('M3,-31 Q3,-40 12,-40 Q21,-40 21,-31 Q21,-24 14,-16 L3,0 L21,0')},
  '3':{w:25,m:P('M4,-36 Q8,-40 13,-40 Q21,-40 21,-31 Q21,-23 13,-21 Q22,-19 22,-9 Q22,0 13,0 Q6,0 3,-4')},
  '4':{w:26,m:P('M17,0 L17,-40 L3,-11 L23,-11')},
  '5':{w:24,m:P('M20,-40 L6,-40 L4,-22 Q8,-25 13,-25 Q21,-24 21,-12 Q21,0 12,0 Q5,0 3,-5')},
  '6':{w:24,m:P('M19,-37 Q15,-41 10,-39 Q3,-35 3,-21 L3,-11 Q3,0 12,0 Q21,0 21,-11 Q21,-20 12,-20 Q5,-20 3,-14')},
  '7':{w:24,m:P('M3,-40 L21,-40 L10,0')},
  '8':{w:24,m:CIR(12,-30,8.5)+CIR(12,-9.5,9.5)},
  '9':{w:24,m:P('M5,-3 Q9,1 14,-1 Q21,-5 21,-19 L21,-29 Q21,-40 12,-40 Q3,-40 3,-29 Q3,-20 12,-20 Q19,-20 21,-26')},
  '.':{w:6,m:DOT(3,-2.5,2.6)},
  ',':{w:6,m:P('M4,-3 Q4,3 1,6')},
  '-':{w:18,m:P('M2,-13 L16,-13')},
  '·':{w:6,m:DOT(3,-13,2.4)},
  '/':{w:18,m:P('M2,4 L16,-40')},
  '→':{w:30,m:P('M2,-13 L26,-13')+P('M19,-21 L28,-13 L19,-5')},
  ' ':{w:14,m:''},
};
const metrics={upm:40,cap:40,xHeight:28,ascender:44,descender:12,
  weights:{light:2,regular:3,bold:4.5},defaultSpacing:6};
function text(str,o={}){
  o=o||{};
  const wname=o.weight||'regular';
  const sw=typeof wname==='number'?wname:(metrics.weights[wname]||3);
  const sp=(o.spacing===0||o.spacing)?o.spacing:metrics.defaultSpacing;
  const col=o.color||'currentColor';
  let x=0,parts=[];
  for(const ch of String(str).toLowerCase()){
    const g=G[ch]||G[' '];
    if(g.m)parts.push(`<g transform="translate(${x} 0)">${g.m}</g>`);
    x+=g.w+sp;
  }
  const w=Math.max(1,x-sp),asc=metrics.ascender,desc=metrics.descender;
  const s=(o.size||40)/40;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 ${-asc} ${w+4} ${asc+desc}" width="${(w+4)*s}" height="${(asc+desc)*s}" style="color:${col}"><g fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${parts.join('')}</g></svg>`;
}
window.QyMonoline={glyphs:G,metrics,text};
})();
