# Ferramentas e o que cada uma faz (testado em 09/11/2026)

## Canva (conectado)
| Ferramenta | Para que serve | Observação testada |
|---|---|---|
| `create-design` | Gera um design editável a partir de um briefing | **Testado.** Com briefing detalhado (cores em hex, textos exatos, ordem e hierarquia, "sem foto, sem ilustração, sem IA") entregou uma peça fiel: fundo preto, faixa diagonal, selo âmbar, 50% gigante, botão e rodapé. Levou ~40s. Texto sai em camadas editáveis. A fonte é aproximada, não é exatamente Barlow Condensed. |
| `read-design` | Lê texto, páginas e miniatura | Usar para conferir o que foi gerado. |
| `edit-design` | Ajusta texto, cor, posição, formas | Abre transação; só salva (`commit`) com aprovação do João. |
| `resize-design` | Cria versões em outros tamanhos | Para feed → story e outros formatos. |
| `export-design` | Baixa PNG, PDF etc. | Conferir formatos com `get-export-formats`. |
| `list-brand-kits` | Kit de marca (cores, fontes, logotipo) | **Vazio hoje.** Pendência: cadastrar Stahl Car e FUEL UP. |
| `search-designs` | Busca nos designs do próprio usuário | **Não** busca a biblioteca pública de modelos do Canva. |
| `import-design-from-url` | Importa HTML/PDF de URL pública | Não usar com arquivo gerado por nós: exigiria hospedar em site de terceiros. |
| `generate-image` | Imagem por IA | **Proibido nesta skill.** |

Como usar o Canva na nossa skill: o motor de código (`motor/`) é a fonte de verdade visual. Para versão editável, use `create-design` com um briefing que descreva a peça do motor (textos exatos, hex, hierarquia). Sempre conferir com `read-design` e comparar com o PNG do motor.

## Adobe (conectado)
- `search_design`: templates do Adobe Express (referência de layout e cor; ver `referencias/`).
- `asset_search` (Stock) + `asset_license_and_download_stock`: **fotos reais licenciadas**, licença comercial paga. Preferir a foto da própria oficina.
- Fontes: `font_recommend`, `font_search` (ajuda a escolher tipografia).
- Evitar: recursos generativos (Firefly etc.).
- Exige iniciar com `adobe_mandatory_init` uma vez por conversa.

## Motor de código (`motor/`)
Playwright + HTML/CSS + SVG. Fontes Barlow Condensed e Inter (Google Fonts). Sem IA. Gera PNG em `clientes/<cliente>/saida/`.

## Outros do ecossistema
- `gtavi/engine`: motor de cenas animadas (vídeo de 6 a 8s com contagem do 50%).
- `awesome-design-md`: direção visual de marcas automotivas.
- `meta-ads-generator-skill`: só o método (briefing, conceitos, aprovação). Sem licença; não copiar código.

## Fluxo de foto real (Drive → Canva), testado em 09/11/2026
1. `search_files` no Drive (`parentId = '<pasta do cliente>'`) lista as fotos.
2. `download_file_content` em cada foto: quando é grande, a resposta é **salva em arquivo** JSON (base64) em `tool-results/`, sem estourar a conversa.
3. `python3 motor/folha_fotos.py <tool-results> <saida>` converte tudo (HEIC inclusive, via pillow-heif), corrige rotação EXIF, limita a 2000px e gera `_folha.png` para escolher.
4. `create-upload-url` no Canva + `curl -X POST -H "Content-Type: application/octet-stream" --data-binary @foto.jpg <url>` → `{"mediaId": ...}`.
5. `copy-design` do layout aprovado (não gasta crédito) → `read-design` com `open_transaction` → `edit-design`: `update_fill` com `locator_id` = id da página troca o fundo; `delete_element` tira a imagem gerada; `insert_shape` + `layer_element: back` cria sombra atrás do texto (várias camadas de ~9%).
6. Mostrar ao João; só então `finalize: commit`.

Limites: `read_file_content` não lê HEIC nem devolve JPG como imagem; arquivos pequenos voltam inline (não dá para salvar). Fotos com marca de terceiros (ex.: Valvoline) precisam de aval do cliente.
