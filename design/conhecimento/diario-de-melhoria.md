# Diário de melhoria · design Stahl Car Black Friday

Regra: a cada rodada, avaliar contra `../checklist.md` e as referências do João; anotar o que falhou, a causa e a mudança da próxima rodada. Continuar até o João aprovar.

## Rodada 1 (09/11/2026) · Canva, 3 variações
A herói disco de freio · B herói óleo e filtro · C herói carro. Links Canva (editáveis, privados):
- A: https://www.canva.com/d/KRzEYqAg1ER7nqR (DAHacRtCV00)
- B: https://www.canva.com/d/YUvh9GbBzTrnhrP (DAHacamrEiw)
- C: https://www.canva.com/d/sI-i67Jc0cO51OE (DAHacci1_Rc)

**Avaliação (checklist):**
- Salto grande sobre o v3: camadas, foto herói, selo, fita, moedas, hierarquia. Textos 100% editáveis.
- A: título só branco/amarelo chapado (falta cromo/ouro 3D); selo "50% OFF" apertado dentro do anel; texto da fita se sobrepõe em parte.
- B: **o rodapé tem asterisco mas a oferta não tem "*"** (erro de conteúdo); selo "VÁLIDO NA BLACK FRIDAY" afirma validade sem data real; frasco sem rótulo (genérico).
- C: texto da fita cortado na borda ("Bl"); carro com **emblema e grade de marca real visível** (risco de parecer parceria); título parcialmente atrás do carro.
- Todas: **não consigo provar que as fotos são fotografias reais**. Têm aparência de imagem sintética (brilho exagerado, objeto sem marca). Conferir no Canva (Detalhes da imagem) antes de aprovar.

**Mudanças da rodada 2:** título cromo+ouro com contorno e sombra 3D; asterisco em todas as ofertas; fita inteira dentro da peça; sem emblema de marca no carro; pedir fotografia real de estúdio; versão story 9:16.

## Rodada 2 (09/11/2026) · Canva
Links:
- A2 (disco de freio): https://www.canva.com/d/1PUo1Hykg5LqDqn (DAHacYQLIyU)
- B2 (óleo e filtro): https://www.canva.com/d/nhm_TZ3M5Sgv412 (DAHacaTrj4w), com **edição em rascunho aguardando aprovação do João** (não gravada)
- C2 (story com carro): **não gerada** (`quota_exceeded`: créditos de IA do Canva esgotados)

**Avaliação:**
- A2: melhor peça até agora. Fita completa, selo com "EM SERVIÇOS*", disco enorme, margens ok. Falta: título ainda branco/dourado chapado (sem cromo 3D); botão com cantos arredondados.
- B2: corrigiu o asterisco, mas o Canva **inventou texto no frasco** ("ÓLEO DE DE MOTOR", "SAE 5W-30", "100% SINTÉTICO", "1L"). Rascunho remove as especificações e deixa "ÓLEO DE MOTOR"; ajusta o espaçamento do selo.
- Lição: **sempre ler `design_content` do design gerado** para achar texto que o Canva inventou (rótulos, specs).
- Lição: gerar no máximo 3 por rodada; 5 gerações esgotaram os créditos.

**Pendências para a rodada 3 (depois que os créditos voltarem ou com edit-design):** título cromo/ouro 3D, versão story, foto real comprovada, logotipo e preço do selo.

## Rodada 3 (09/11/2026) · fotos reais da Stahl Car + Canva Pro
**Desbloqueios:**
- Fotos HEIC do Drive: `download_file_content` salva o base64 em arquivo quando é grande; `motor/heic2jpg.py` e `motor/folha_fotos.py` convertem (pillow-heif) e geram folha de contato. 12 das 33 fotos lidas.
- Upload para o Canva: `create-upload-url` + `curl -X POST --data-binary` com os bytes do JPG → `mediaId`. Funcionou (IMG_4884 = MAHacUUXzbA).
- `copy-design` duplica sem gastar créditos; `edit-design` troca o fundo (`update_fill` no page id) e insere formas (`insert_shape`) para sombra.
- João liberou créditos do Canva Pro.

**A3** (cópia do A2 com foto real IMG_4884, frasco Valvoline na oficina): https://www.canva.com/d/IY0l1wS8thUXS7r (DAHacbZH-Lk). Rascunho aberto, não gravado.
- Lição: forma inserida vai para a frente; usar `layer_element: back`. Degradê = várias camadas de 9% de opacidade, não 3 de 22% (degraus visíveis).
- Pendência: a foto mostra marca Valvoline (produto de terceiro). Confirmar com o cliente se pode aparecer; alternativa é a foto do elevador (IMG_4869/4870).

**Em andamento:** C3 story e D3 feed gerados no Canva para receber as fotos reais IMG_4869/4870/4888.

## 2026-11-12 · Rodada 4 · Carrossel Fuel UP no Canva (Seg 16/11, Black Friday)
- **O que funcionou:** `create-design` com brief completo (7 páginas descritas uma a uma, paleta, moldura @ + contador, fotos reais de oficina) gerou o carrossel em 1 geração, já com fotos do banco do Canva. Direção visual pedida pelo João: os 2 últimos modelos de `MODELO POSTS FUEL UP` (DAHasZ2rmpM): tipografia gigante, objeto-herói, fundo escuro com 1 acento, pílula de @, selo de CTA.
- **Erros do Canva corrigidos via API:** preço inventado (R$ 299,90) no cartão de comparação, palavra "entende?" duplicada, @ com erro de digitação. Regra mantida: ler `design_content` inteiro antes de mostrar.
- **Limites:** a API não troca família de fonte (saiu condensada tipo Anton/Bebas; Barlow precisa ser aplicada no editor). "Instagram Post (Portrait)" sai 1080x1440; recorte central para 1080x1350 feito localmente.
- **Fotos:** Google Imagens, Pexels e Unsplash bloqueiam navegador automatizado (CAPTCHA/Cloudflare). Funcionam: Openverse API (fraco para oficina) e Wikimedia Commons API com User-Agent descritivo (ensaio Shixart1985 CC BY 2.0 de mecânico em elevador). Thumbs do Commons só em larguras listadas (1920px ok) e com pausa entre pedidos (429).
- **Reel:** motor `narracao-reels` do repositório gtavi ganhou paleta `fuelup` (preto/vermelho) via campo `"palette"` no script.json; cenas calendar/countdown/news/counter trocam fundo neon por escuro com brilho vermelho.
