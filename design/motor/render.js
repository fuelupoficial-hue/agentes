// Uso: node render.js <cliente> [paleta a|b] [modelos separados por vírgula]
// Lê ../clientes/<cliente>/config.json e grava PNGs em ../clientes/<cliente>/saida/
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [cliente = 'stahl-car', paleta = 'a', lista] = process.argv.slice(2);
const dir = path.join(__dirname, '..', 'clientes', cliente);
const cfg = JSON.parse(fs.readFileSync(path.join(dir, 'config.json'), 'utf8'));
const modelos = (lista || 'headline,countdown,servicos,carrossel').split(',');
(async () => {
  const b = await chromium.launch();
  const jobs = [];
  for (const m of modelos) for (const f of ['feed', 'story']) {
    if (m === 'carrossel') { if (f === 'feed') for (let s = 1; s <= 4; s++) jobs.push([m, f, s]); }
    else jobs.push([m, f, 1]);
  }
  for (const [m, f, s] of jobs) {
    const p = await b.newPage({ viewport: { width: 1080, height: f === 'feed' ? 1350 : 1920 } }); p.on('pageerror', e => console.error('ERRO NA PÁGINA:', e.message));
    await p.addInitScript(`window.CFG=${JSON.stringify(cfg)}`);
    await p.goto(`file://${__dirname}/modelos.html#m=${m}&p=${paleta}&f=${f}&s=${s}`);
    await p.reload(); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
    const nome = `${m}${m === 'carrossel' ? '-' + s : ''}-${f}-${paleta}.png`;
    await p.screenshot({ path: path.join(dir, 'saida', nome) }); console.log(nome); await p.close();
  }
  await b.close();
})();
