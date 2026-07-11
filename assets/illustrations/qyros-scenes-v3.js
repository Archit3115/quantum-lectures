/* qyros illustration library · v3 additions
   new poses tiles, environment kit, company-life scenes, animation rig sheets.
   load AFTER qyros-illustrations.js and qyros-scenes.js.                       */
(function(){
'use strict';
const K=window.QyrosIllustrationsCore, Q=window.QyrosIllustrations;
const {themes,fig,props,G,FLIP,C,R8,MONO}=K;
const R=Q.registry;
const reg=(id,kind,w,h,draw)=>{R[id]={id,kind,w,h,draw};};
const sh=(t,x,y,rx)=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="5" fill="${t.shadow}"/>`;
const GY=300,H=340,W=480;
const floor=(t,w,gy)=>`<rect x="0" y="${gy}" width="${w}" height="60" fill="${t.floor}"/>`;

/* new pose tiles */
[['leo','think'],['meera','think'],['amara','cheer'],['zuri','cheer'],['dev','carry'],['jae','carry']].forEach(([id,pose])=>{
  reg(`fig-${id}-${pose}`,'figure',150,250,(t)=>sh(t,75,228,26)+G(75,226,1,fig(id,pose)));
});

/* environment kit tiles */
reg('prop-blackboard','prop',230,180,(t)=>G(15,15,1,props.blackboard(t)));
reg('prop-tv','prop',210,200,(t)=>sh(t,105,190,60)+G(20,186,1,props.tv(t)));
reg('prop-quantum-chip','prop',130,120,(t)=>G(23,14,1,props.quantumChip(t)));
reg('prop-bookshelf','prop',150,210,(t)=>sh(t,75,198,50)+G(20,194,1,props.bookshelf(t)));
reg('prop-sofa','prop',210,120,(t)=>sh(t,105,108,80)+G(20,104,1,props.sofa(t)));
reg('prop-coffee-machine','prop',120,130,(t)=>G(25,118,1,props.coffeeMachine(t)));
reg('prop-water-cooler','prop',90,170,(t)=>sh(t,45,158,26)+G(22,154,1,props.waterCooler(t)));
reg('prop-window','prop',210,170,(t)=>G(20,20,1,props.windowWall(t)));
reg('prop-door','prop',120,220,(t)=>sh(t,60,208,40)+G(22,204,1,props.door(t)));
reg('prop-rug','prop',210,60,(t)=>G(105,44,1,props.rug(t)));
reg('prop-ceiling-light','prop',110,130,(t)=>G(55,8,1,props.ceilingLight(t)));
reg('prop-kanban','prop',210,150,(t)=>G(20,15,1,props.kanban(t)));
reg('prop-monitor-dual','prop',190,100,(t)=>G(20,88,1,props.monitorDual(t)));
reg('prop-plant-tall','prop',110,180,(t)=>sh(t,55,168,30)+G(25,164,1,props.plantTall(t)));
reg('prop-wall-clock','prop',80,80,(t)=>G(40,40,1,props.wallClock(t)));
reg('prop-quantum-cased','prop',170,250,(t)=>sh(t,85,238,52)+G(20,234,1,props.casedQuantum(t)));
reg('prop-glass-panel','prop',210,140,(t)=>{
  /* backdrop shapes so the translucency reads */
  return R8(14,44,92,82,8,t.posterBg)+R8(96,16,100,74,8,'#26282C')
    +G(34,42,1,props.glassPanel(t,150,84));
});

reg('scene-glass-hud','scene',W,H,(t)=>{
  const dotc=t.name==='dark'?'rgba(255,255,255,0.10)':'rgba(0,0,0,0.10)';
  return floor(t,W,GY)
    +`<defs><pattern id="qy-hudd-${t.name}" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.1" fill="${dotc}"/></pattern></defs>`
    +`<rect x="40" y="30" width="400" height="250" fill="url(#qy-hudd-${t.name})"/>`
    +sh(t,368,GY+8,50)+G(310,GY,1,props.casedQuantum(t))
    +sh(t,120,GY+8,28)+G(120,GY,1,fig('meera','point'))
    +G(168,74,1,props.glassPanel(t,160,92))
    +G(232,148,1,props.glassPanel(t,128,74));
});

/* company-life scenes */
reg('scene-brainstorm-wall','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(56,58,1,props.kanban(t))
  +sh(t,148,GY+8,28)+G(145,GY,1,fig('petra','back'))
  +sh(t,330,GY+8,28)+G(330,GY,1,FLIP(fig('ines','point'))));
reg('scene-lab-blackboard','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(240,0,1,props.ceilingLight(t))
  +G(110,56,1,props.blackboard(t))
  +sh(t,368,GY+8,28)+G(368,GY,1,FLIP(fig('leo','think'))));
reg('scene-chip-reveal','scene',W,H,(t)=>
  floor(t,W,GY)
  +R8(196,214,120,86,3,'#E4E4E7')+R8(206,206,100,10,2,'#D6D6DA')
  +G(214,116,1,props.quantumChip(t))
  +`<text x="256" y="330" ${MONO} font-size="11" fill="${t.label}" text-anchor="middle">qyros q1 · 128 qubits</text>`
  +sh(t,110,GY+8,30)+G(110,GY,1,fig('amara','cheer')));
reg('scene-office-lounge','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(240,44,1,props.windowWall(t))
  +G(150,70,1,props.wallClock(t))
  +G(150,GY,1,props.rug(t))
  +sh(t,140,GY+6,80)+G(55,GY,1,props.sofa(t))
  +sh(t,420,GY+8,30)+G(395,GY,1,props.plantTall(t)));
reg('scene-demo-day','scene',W,H,(t)=>
  floor(t,W,GY)
  +sh(t,150,GY+8,60)+G(65,GY,1,props.tv(t))
  +sh(t,320,GY+8,30)+G(320,GY,1,FLIP(fig('noor','present')))
  +sh(t,408,GY+8,26)+G(408,GY,1,FLIP(fig('kofi','stand'))));
reg('scene-coffee-chat','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(64,GY,1,props.coffeeMachine(t))
  +sh(t,196,GY+8,24)+G(172,GY,1,props.waterCooler(t))
  +sh(t,290,GY+8,26)+G(290,GY,1,fig('sam','wave'))
  +sh(t,404,GY+8,26)+G(404,GY,1,FLIP(fig('tavleen','stand'))));
reg('scene-night-ops','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(286,42,1,props.windowWall(t))
  +G(120,0,1,props.ceilingLight(t))
  +sh(t,155,GY+8,40)
  +G(70,GY,1,props.chair(t))+G(98,GY,1,fig('jae','sit'))
  +G(56,GY,1,props.desk(t))+G(96,GY-80,1,props.monitorDual(t)));
reg('scene-launch-day','scene',W,H,(t)=>
  floor(t,W,GY)
  +G(60,54,1,props.posterWall(t))
  +sh(t,180,GY+8,28)+G(180,GY,1,fig('amara','cheer'))
  +sh(t,285,GY+8,28)+G(285,GY,1,FLIP(fig('meera','cheer')))
  +sh(t,390,GY+8,28)+G(390,GY,1,fig('kofi','cheer')));
reg('scene-library-corner','scene',W,H,(t)=>
  floor(t,W,GY)
  +sh(t,120,GY+8,52)+G(65,GY,1,props.bookshelf(t))
  +G(300,GY,1,props.rug(t))
  +sh(t,300,GY+8,26)+G(300,GY,1,fig('dev','carry'))
  +G(420,76,1,props.wallClock(t)));
reg('scene-doorway-welcome','scene',W,H,(t)=>
  floor(t,W,GY)
  +sh(t,128,GY+8,40)+G(90,GY,1,props.door(t))
  +sh(t,250,GY+8,26)+G(250,GY,1,fig('zuri','wave'))
  +sh(t,392,GY+8,28)+G(368,GY,1,props.plantTall(t)));

/* animation rig sheets · davinci-resolve-ready
   units: 1 unit = 1px at 100% · origin = figure ground-center · y up = negative.
   ease → resolve custom curve: expo = (0.16, 1.00, 0.30, 1.00) · inout = ease-in-out.
   export: render each layer group to png@2x (or copy svg per layer), parent at anchor. */
Q.anim={
  'pose:stand':{anchors:{chest:[0,-130]},rig:['idle breath: torso+head scale 1→1.012→1 @chest, 3.2s inout loop','hold ≥3s between any other move']},
  'pose:walk':{anchors:{pelvis:[0,-96],shoulder:[4,-150]},rig:['legs rotate ±14° @pelvis, 0.45s per step inout, opposite phase','arms counter-swing ±10° @shoulder, phase-locked to opposite leg','body+head bob y 0→−2→0 each step','travel ≈ 60px/s at 100% scale']},
  'pose:wave':{anchors:{elbow:[16,-146]},rig:['forearm+hand rotate −12°→+14° @elbow, 0.5s inout ×3, settle at +2°','head tilt 2° toward wave on first beat']},
  'pose:present':{anchors:{shoulder:[7,-150]},rig:['arm raises −30°→0° @shoulder over 0.5s expo (6% overshoot)','micro-drift ±1.5° 3s inout loop while speaking']},
  'pose:point':{anchors:{shoulder:[7,-150]},rig:['arm sweeps up 40° @shoulder 0.4s expo, hold 1.2s, return 0.3s','target highlight lands +0.15s after arm settles']},
  'pose:kneel':{anchors:{shoulder:[0,-118]},rig:['both arms raise 10° @shoulder 0.6s expo on start','hands jitter y ±1px 0.2s ×4 when adjusting hardware','head tilt up 4° while reaching']},
  'pose:sit':{anchors:{elbows:[10,-96]},rig:['hands bob y ±2px alternating 0.25s (typing)','screen type-on 30ms/char in sync','chair sway: whole fig rotate ±0.6° @ground 4s inout loop']},
  'pose:back':{anchors:{shoulder:[9,-152]},rig:['raised arm taps: rotate +4°/−4° @shoulder 0.35s ×2 per sticky-move','weight shift: hips x ±2px 2.8s inout loop']},
  'pose:think':{anchors:{elbow:[18,-150]},rig:['hand taps chin: forearm rotate ±3° @elbow 0.8s inout loop','head nod −2° every 2.4s; realisation = +4° pop 0.3s expo']},
  'pose:cheer':{anchors:{shoulderL:[0,-150],shoulderR:[7,-152]},rig:['both arms 0°→raised @shoulders 0.4s expo, overshoot 1.1, settle','tiny hop: whole fig y 0→−6→0, 0.45s, once','optional: 3 green 4px squares rise 40px + fade 0.8s from hands']},
  'pose:carry':{anchors:{pelvis:[0,-96]},rig:['walk cycle at 0.5s/step; laptop arm locked','laptop counter-bobs y ±1px opposite body bob']},
  'prop:chandelier':{rig:['bottom cylinders opacity 0.85→1→0.85 2s, stagger 200ms','whole unit sway ±0.4° @top-mount 5s inout — barely visible']},
  'prop:screens':{rig:['chart polyline draws left→right 0.8s expo (dashoffset→0)','code lines type-on 30ms/char, block cursor blink 1s steps(1)']},
  'prop:ceiling-light':{rig:['glow opacity 0.45→0.55 2.4s inout loop','scene start: flicker 0/1 ×2 in 0.2s then settle']},
  'prop:plant':{rig:['leaves rotate ±1.5° @stem-base 3.2s inout, per-leaf phase +0.4s']},
  'prop:glass-panel':{rig:['entrance: scale 0.98→1 + opacity 0→1, 400ms expo (glass-in)','float: whole panel y ±3px 4s inout loop; stacked panels offset phase 1s','specular: white gradient band sweeps top-left→bottom-right once on entrance, 600ms','content: sparkline draws after panel lands (+150ms, 500ms expo)']},
  'scene:build-order':{rig:['1 · floor fades in 200ms','2 · props rise 8px + fade 300ms expo, stagger 90ms left→right','3 · figures slide in 12px 300ms expo','4 · the one green accent draws last (600ms expo)','exits reverse at 0.7× duration']},
};
})();
