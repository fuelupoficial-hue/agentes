// Criativo Black Friday Stahl Car usando o motor de cenas do repo gtavi (engine/engine.js).
// Uso: node render-motor.js [caminho/do/gtavi/engine]
// Tudo desenhado por código (cena "sunset" do motor + texto). Sem imagem pronta, sem IA.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const ENGINE = path.resolve(process.argv[2] || '/home/user/gtavi/engine');
const OUT = __dirname;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  page.on('pageerror', e => console.error('ERRO NA PÁGINA:', e.message));
  await page.goto('file://' + path.join(ENGINE, 'scenes.html'));
  await page.evaluate(async () => {
    await Promise.all(['100px Anton', '900 100px Mont', '700 100px Mont'].map(f => document.fonts.load(f)));
    const dark = '#1a0630';
    S.stahl = (u, d, b) => {
      S.sunset(u, d, { gridSpeed: 0 });
      // marca
      txt('STAHL CAR', W / 2, 262, { size: 70, color: '#fff', spacing: 14, glowPx: 24, glowCol: C.pink });
      g.fillStyle = C.pink; g.fillRect(W / 2 - 70, 312, 140, 6);
      // título
      txt('BLACK', W / 2, 520, { size: 270, color: '#fff', stroke: 22, strokeCol: dark, glowPx: 50, glowCol: C.pink, maxW: 900 });
      txt('FRIDAY', W / 2, 735, { size: 270, color: C.gold, stroke: 22, strokeCol: dark, glowPx: 50, glowCol: C.orange, maxW: 900 });
      // oferta
      txt('DESCONTOS DE ATÉ', W / 2, 880, { size: 52, font: 'Mont', weight: 900, color: '#fff', spacing: 8, stroke: 14, strokeCol: dark, maxW: 900 });
      txt('50%', W / 2, 1132, { size: 340, color: '#fff', stroke: 24, strokeCol: dark, glowPx: 60, glowCol: C.pink, maxW: 820 });
      txt('EM SERVIÇOS*', W / 2, 1292, { size: 90, font: 'Mont', weight: 900, color: C.cyan, spacing: 6, glowPx: 30, glowCol: C.cyan, maxW: 900 });
      // botão
      g.save(); g.translate(W / 2, 1420);
      const gr = g.createLinearGradient(-380, 0, 380, 0); gr.addColorStop(0, C.pink); gr.addColorStop(1, C.purple);
      g.fillStyle = gr; g.shadowColor = C.pink; g.shadowBlur = 40; rr(-380, -64, 760, 128, 64); g.fill(); g.shadowBlur = 0;
      txt('SOLICITE SEU ORÇAMENTO', 0, 4, { size: 52, font: 'Mont', weight: 900, color: '#fff', spacing: 2, maxW: 700 });
      g.restore();
      txt('*Desconto de até 50%, conforme o serviço. Consulte condições com a Stahl Car.', W / 2, 1503, { size: 26, font: 'Mont', weight: 700, color: 'rgba(255,255,255,.88)', stroke: 8, strokeCol: dark, maxW: 960 });
    };
    window.setup({ duration: 1e7, brand: '', beats: [{ start: 0, scene: 'stahl', words: [] }] });
  });
  // quadro com animações de entrada já concluídas; tira o fio de progresso do topo
  await page.evaluate(async () => { await window.frame(1.2, 36, null); g.drawImage(cv, 0, 14, W, 14, 0, 0, W, 14); });
  const png = async (clip, name) => {
    const dataUrl = await page.evaluate(([y, h]) => {
      const c = document.createElement('canvas'); c.width = 1080; c.height = h; c.getContext('2d').drawImage(cv, 0, y, 1080, h, 0, 0, 1080, h); return c.toDataURL('image/png'); }, clip);
    fs.writeFileSync(path.join(OUT, name), Buffer.from(dataUrl.split(',')[1], 'base64'));
  };
  await png([0, 1920], 'story-motor-1080x1920.png');
  await png([185, 1350], 'feed-motor-1080x1350.png');
  await browser.close();
  console.log('ok');
})();
