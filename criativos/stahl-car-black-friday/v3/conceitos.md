# Stahl Car · Black Friday · v3 (padrão de designer)

Método adaptado de `meta-ads-generator-skill` (briefing, conceitos, aprovação, render). Direção visual extraída de `awesome-design-md` (Lamborghini, Ferrari): fundo dominante, **uma única cor de destaque**, tipografia condensada em caixa alta com entrelinha apertada, botão de canto reto, ângulo de 12°.

Sem IA de imagem. Tudo por código: Barlow Condensed e Inter (Google Fonts) e um disco de freio em SVG.

## Briefing
- Cliente: Stahl Car. Oferta: até 50% de desconto em serviços. Ação: solicitar orçamento.
- Pendente (não inventei): logotipo, cores da marca, fotos reais da oficina, prazo da campanha, canal de contato.
- Pesquisa de concorrentes e avaliações reais: não feita. Nenhuma "dor do cliente" foi citada porque não há citação real.

## Conceito A · Preto e âmbar (`conceito-a-*.png`)
- Hook: BLACK FRIDAY
- Headline: ATÉ 50% DE DESCONTO EM SERVIÇOS
- CTA: SOLICITE SEU ORÇAMENTO
- Visual: fundo preto, faixa inclinada, disco de freio em tom sobre tom, âmbar só no selo, na palavra "serviços" e no botão.

## Conceito B · Claro e vermelho (`conceito-b-*.png`)
- Mesmo texto. Fundo off-white, texto preto, vermelho de corrida só no selo e em "serviços", botão preto.
- Para feed com muito conteúdo escuro ao redor: o claro se destaca mais.

## Checklist de designer aplicado
- Um foco por peça: o número 50%.
- Leitura em 3 passos: selo, 50%, botão.
- Contraste alto e uma só cor de destaque.
- Zona segura do story (topo 250px, base 330px livre).
- Sem travessão no texto do anúncio.
- Rodapé legal legível, sem prometer garantia nem prazo.

Gerar: `node render.js` nesta pasta (precisa de `playwright` e internet para as fontes).
