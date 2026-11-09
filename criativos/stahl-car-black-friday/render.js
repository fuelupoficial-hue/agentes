const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch(); 
 for (const [name,h,hash] of [['feed-1080x1350',1350,''],['story-1080x1920',1920,'#story']]){
  const p=await b.newPage({viewport:{width:1080,height:h},deviceScaleFactor:1});
  await p.goto('file://'+__dirname+'/criativo.html'+hash); await p.reload();
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
  await p.screenshot({path:name+'.png'}); 
 }
 await b.close();
})();
