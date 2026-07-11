/* qyros illustration library · scenes + registry + render api
   requires qyros-illustrations.js (QyrosIllustrationsCore).                    */
(function(){
'use strict';
const K=window.QyrosIllustrationsCore;
const {themes,fig,props,G,FLIP,C,R8,MONO}=K;
const R={};let uid=0;
function reg(id,kind,w,h,draw){R[id]={id,kind,w,h,draw};}
const sh=(t,x,y,rx)=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="5" fill="${t.shadow}"/>`;

/* ── figure tiles (24) ─────────────────────────────── */
const figPoses={amara:['stand','point'],meera:['present','walk'],jae:['wave','stand'],
  tavleen:['present','stand'],noor:['present','point'],leo:['walk','wave'],
  zuri:['point','stand'],petra:['present','walk'],dev:['stand','wave'],
  ines:['point','present'],kofi:['walk','stand'],sam:['wave','present']};
Object.entries(figPoses).forEach(([id,pp])=>{
  pp.forEach(pose=>{
    reg(`fig-${id}-${pose}`,'figure',150,250,(t)=>sh(t,75,228,26)+G(75,226,1,fig(id,pose)));
  });
});

/* ── prop tiles (14) ───────────────────────────────── */
reg('prop-chandelier','prop',150,210,(t)=>G(75,12,0.95,props.chandelier(t)));
reg('prop-quantum-panel','prop',340,350,(t)=>sh(t,170,338,120)+G(20,334,1,props.quantumPanel(t)));
reg('prop-server-rack','prop',130,240,(t)=>sh(t,65,228,44)+G(20,226,1,props.serverRack(t)));
reg('prop-desk','prop',250,120,(t)=>sh(t,125,108,90)+G(20,104,1,props.desk(t)));
reg('prop-chair','prop',120,150,(t)=>sh(t,55,138,40)+G(30,134,1,props.chair(t)));
reg('prop-laptop','prop',110,80,(t)=>G(23,68,1,props.laptop(t)));
reg('prop-screen-chart','prop',260,170,(t)=>G(15,15,1,props.wallScreenChart(t)));
reg('prop-screen-call','prop',260,170,(t)=>G(15,15,1,props.wallScreenCall(t)));
reg('prop-whiteboard','prop',230,170,(t)=>G(15,15,1,props.whiteboard(t)));
reg('prop-podium','prop',130,180,(t)=>sh(t,65,168,42)+G(17,164,1,props.podium(t)));
reg('prop-poster','prop',120,140,(t)=>G(17,16,1,props.posterWall(t)));
reg('prop-globe-code','prop',280,230,(t)=>G(10,10,1,props.globeCode(t)));
reg('prop-plant','prop',100,120,(t)=>sh(t,50,110,26)+G(20,106,1,props.plant(t)));
reg('prop-terminal','prop',180,130,(t)=>G(15,15,1,props.terminalWindow(t)));

/* ── scenes (14) ───────────────────────────────────── */
const GY=300, H=340, W=480;
const floor=(t,w,gy)=>`<rect x="0" y="${gy}" width="${w}" height="60" fill="${t.floor}"/>`;

reg('scene-hardware-maintenance','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(90,GY,1,props.quantumPanel(t))
  +sh(t,215,GY+8,42)
  +G(212,GY,1,fig('amara','kneel')));

reg('scene-quantum-inspect','scene',W,H,(t)=>
  floor(t,W,GY)
  +R8(255,0,150,26,0,'#55585C')
  +G(330,24,1.05,props.chandelier(t))
  +sh(t,185,GY+8,30)
  +G(185,GY,1,fig('dev','point')));

reg('scene-leadership-talk','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(330,66,1,props.posterWall(t))
  +sh(t,245,GY+8,34)
  +G(245,GY,1,FLIP(fig('noor','present')))
  +G(150,GY,1,props.podium(t)));

reg('scene-collaboration-desk','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(200,58,1,props.posterWall(t))
  +sh(t,180,GY+8,40)+sh(t,398,GY+8,28)
  +G(128,GY,1,props.chair(t))
  +G(155,GY,1,fig('tavleen','sit'))
  +G(112,GY,1,props.desk(t))
  +G(205,GY-80,1,props.laptop(t))
  +G(398,GY,1,FLIP(fig('jae','stand'))));

reg('scene-whiteboard-planning','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(135,58,1,props.whiteboard(t))
  +sh(t,238,GY+8,28)
  +G(235,GY,1,fig('ines','back')));

reg('scene-remote-call','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(85,56,1.2,props.wallScreenCall(t))
  +sh(t,405,GY+8,28)
  +G(405,GY,1,FLIP(fig('leo','stand'))));

reg('scene-data-center','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(65,GY,1,props.serverRack(t))+G(172,GY,1,props.serverRack(t))+G(279,GY,1,props.serverRack(t))
  +sh(t,420,GY+8,30)
  +G(420,GY,1,FLIP(fig('zuri','walk'))));

reg('scene-globe-network','scene',W,H,(t)=>
  G(110,62,1,props.globeCode(t)));

reg('scene-pair-programming','scene',W,H,(t)=>
  floor(t,W,GY)
  +sh(t,175,GY+8,36)+sh(t,315,GY+8,36)
  +G(126,GY,1,props.chair(t))
  +G(152,GY,1,fig('meera','sit'))
  +G(358,GY,1,FLIP(props.chair(t)))
  +G(332,GY,1,FLIP(fig('kofi','sit')))
  +G(122,GY,1,props.desk(t))
  +G(200,GY-80,1,props.laptop(t))
  +G(295,GY-80,1,FLIP(props.laptop(t))));

reg('scene-onboarding','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(285,66,1,props.posterWall(t))
  +sh(t,205,GY+8,28)
  +G(205,GY,1,fig('sam','wave')));

reg('scene-solo-focus','scene',W,H,(t)=>
  floor(t,W,GY)
  +sh(t,190,GY+8,38)
  +G(140,GY,1,props.chair(t))
  +G(167,GY,1,fig('petra','sit'))
  +G(125,GY,1,props.desk(t))
  +G(215,GY-80,1,props.laptop(t))
  +sh(t,385,GY+8,26)
  +G(355,GY,1,props.plant(t)));

reg('scene-keynote-metric','scene',W,H,(t)=>
  floor(t,W,GY)
  +R8(240,56,190,140,10,'#1B1E22')
  +R8(240,56,190,24,10,'#26282C')+R8(240,70,190,10,0,'#26282C')
  +C(254,68,3.4,'#5A5F66')+C(268,68,3.4,'#5A5F66')+C(282,68,3.4,t.accent)
  +`<text x="335" y="150" ${MONO} font-size="46" font-weight="300" fill="${t.accent}" text-anchor="middle">8ms</text>`
  +`<text x="335" y="178" ${MONO} font-size="13" fill="#8A8F96" text-anchor="middle">median solve · opal</text>`
  +sh(t,155,GY+8,30)
  +G(150,GY,1,fig('amara','present')));

reg('scene-team-standup','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(58,58,1,props.whiteboard(t))
  +sh(t,150,GY+8,26)+sh(t,300,GY+8,26)+sh(t,405,GY+8,26)
  +G(148,GY,1,fig('dev','back'))
  +G(300,GY,1,FLIP(fig('meera','stand')))
  +G(405,GY,1,FLIP(fig('kofi','point'))));

/* wide composite — the "full illustration" */
reg('scene-control-room','scene-wide',1440,420,(t)=>{
  const gy=380;
  let s=floor(t,1440,gy);
  s+=G(56,64,1.15,props.wallScreenChart(t));
  s+=sh(t,335,gy+8,32)+G(335,gy,1,FLIP(fig('noor','present')))+G(238,gy,1,props.podium(t));
  s+=G(620,52,1,props.posterWall(t));
  s+=sh(t,540,gy+8,38);
  s+=G(505,gy,1,props.chair(t))+G(532,gy,1,fig('tavleen','sit'))+G(490,gy,1,props.desk(t))+G(585,gy-80,1,props.laptop(t));
  s+=sh(t,742,gy+8,28)+G(742,gy,1,fig('jae','stand'));
  s+=G(800,56,1,props.whiteboard(t))+sh(t,878,gy+8,28)+G(875,gy,1,fig('ines','back'));
  s+=G(1085,gy,0.98,props.quantumPanel(t))+sh(t,1205,gy+8,40)+G(1202,gy,1,fig('amara','kneel'));
  return s;
});

/* ── render api ────────────────────────────────────── */
function render(id,themeName){
  const a=R[id];if(!a)return '';
  const t=themes[themeName]||themes.light;uid++;
  const rx=Math.min(22,a.h*0.07);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${a.w} ${a.h}">`
    +`<defs><clipPath id="qyilc${uid}"><rect width="${a.w}" height="${a.h}" rx="${rx}"/></clipPath></defs>`
    +`<g clip-path="url(#qyilc${uid})"><rect width="${a.w}" height="${a.h}" fill="${t.bg}"/>${a.draw(t)}</g></svg>`;
}
window.QyrosIllustrations={
  themes,registry:R,render,
  list:(kind)=>Object.values(R).filter(a=>!kind||a.kind===kind||(kind==='scene'&&a.kind==='scene-wide')),
};
})();
