# Passagem de contexto · Fuel UP (atualizado em 12/11/2026)

Cole no início da nova sessão (Claude Desktop no Mac, com a extensão Claude in Chrome):
> "Leia `agentes/fuel-up/HANDOFF.md`, `agentes/design/SKILL.md` e `agentes/fuel-up/conteudo/README.md` e continue de onde paramos."

## Quem e o quê
- João, dono da Fuel UP (tráfego pago para oficinas, Uberlândia-MG, @fuelupoficial). Marca: preto #0A0A0A, vermelho #E00000, fonte Barlow, logo da onça (Canva: design "LOGO FUEL UP" DAGazv95vN4, asset `MAGa3stlwUo`; Drive: pasta "Identidade Visual - Fuel UP" > PNG > HORIZONTAL/VERTICAL/LOGOTIPO, arquivos BRANCA/PRETA/VERMELHA).
- Regras fixas do João: nada sobreposto, margens 80 px, verificador zero alertas; variar entre carrosséis; avatar novo a cada post; elemento oficial na capa quando houver; checar fatos no dia; headline centralizada e dominante; sem preço, caso ou promessa não confirmados; nunca postar sem "pode postar" explícito; resposta curta e visual.
- Ferramenta de criação: **Canva** (banco de fotos do Canva e modelos; `create-design` com brief página a página; depois `read-design` inteiro para caçar texto inventado; `edit-design` para corrigir; `export-design` JPG; recorte local 1080x1350). Direção visual aprovada: os 2 últimos modelos de "MODELO POSTS FUEL UP" (DAHasZ2rmpM): título gigante, fundo escuro, 1 acento, pílula de @, selo de CTA.
- Reels: motor `gtavi/engine` (skill `narracao-reels` + `voz-natural`), com `"palette": "fuelup"` no script.json. Primeiro reel em `gtavi/reels/fuelup-01-black-friday/`.

## Semana 16 a 22/11 (cronograma proposto, aguardando ok)
| Dia | Pilar | Tema | CTA |
|---|---|---|---|
| Seg 16 | Dor+educação | Desconto não é estratégia (Black Friday sem perder margem) | BLACK |
| Ter 17 | Autoridade | O 13º do seu cliente vai para a oficina ou para o carrinho? (1ª parcela até 30/11) | DÉCIMO |
| Qua 18 | Prova/bastidor | Como a gente enche a agenda antes do feriadão (20 a 22/11) | AGENDA |
| Qui 19 | Opinião | GTA VI lança hoje: a Rockstar levou 13 anos, sua oficina desiste em 13 dias (arte oficial de dia, sem afiliação) | GTA |
| Sex 20 | Dor+educação | Oficina fechada, Instagram aberto: 3 coisas programadas (feriado nacional, só a folga como gancho) | PROGRAMA |
| Sáb 21 | Autoridade | Impulsionar não é tráfego pago | ANÚNCIO |
| Dom 22 | Oferta | Amanhã começa a Black Week: sua oficina entra com anúncio pronto? (oferta a definir com João) | QUERO |

## Estado
- **Seg 16 pronto, não aprovado:** Canva DAHasbnYIy0 (https://www.canva.com/d/ydBachidFzberkW), JPG em `fuel-up/conteudo/2026-11-16-seg-black-friday/post/`. Pendência: trocar fonte dos títulos para Barlow Black no editor (API não troca fonte).
- **Reel 01 pronto, não aprovado:** `gtavi/reels/fuelup-01-black-friday/` (render local: `./engine/make_reel.sh reels/fuelup-01-black-friday/script.json`).
- Falta: posts de Ter a Dom, reels dos demais temas, definição da oferta de domingo, confirmar "13 anos" (GTA V 2013 → GTA VI 2026) antes do post de quinta.
- Stahl Car (Black Friday Meta Ads): rascunhos A3/C3/D3 no Canva do João com fotos reais do Drive; prompt para colar está em `design/canva-briefing.md`.

## O que só funciona no computador do João
- Extensão Claude in Chrome (Google Imagens, Canva no navegador com efeitos de texto, ChatGPT grátis para capas).
- Pasta local `~/fuelup-carrossel-ia` (scripts montar_*.py, checar_layout.py, chave OpenAI). Na nuvem usamos a cópia do zip em `fuelup-carrosseis`.
