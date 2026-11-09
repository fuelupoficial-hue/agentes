const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch();
 for(const [c,f] of [['a','feed'],['a','story'],['b','feed'],['b','story']]){
  const h=f==='feed'?1350:1920;
  const p=await b.newPage({viewport:{width:1080,height:h}});
  await p.goto('file://'+__dirname+'/anuncio.html#'+(c==='b'?'b':'')+(f==='story'?'story':''));
  await p.reload(); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(700);
  await p.screenshot({path:`conceito-${c}-${f}.png`});
 }
 await b.close();
})();
