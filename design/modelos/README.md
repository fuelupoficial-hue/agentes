# Catálogo de modelos (oficina)

Origem das ideias: `../referencias/adobe-express-black-friday.md`. Implementação: `../motor/modelos.html`.

| Modelo | Origem (Adobe) | Uso | Campos do `config.json` |
|---|---|---|---|
| `headline` | Bold headline poster | Peça principal: oferta gigante | `marca`, `oferta`, `rodape`, `cta` |
| `countdown` | Countdown poster | Teaser e contagem final | + `countdown.numero`, `countdown.unidade` |
| `servicos` | Classic discount flyer | Mostra o que entra no desconto | + `servicos[]` |
| `carrossel` | Value-driven carousel | 4 slides: oferta, serviços, como pedir, CTA | + `passos[]`, `contato` |

Formatos: `feed` 1080×1350 (4:5) e `story` 1080×1920 (9:16). O carrossel sai em feed (4 PNGs).
Paletas: `a` preto e âmbar · `b` claro e vermelho. Troque as cores em `:root` e `body.b` de `modelos.html` para a marca do cliente.

## Como criar um modelo novo
1. Escolha uma ideia pendente (🧱) da lista de referências e levante os dados que faltam com o cliente.
2. Adicione uma função em `modelos.html` e um ramo no `if(M===...)`.
3. Rode o render, abra os PNG e passe o `checklist.md`.
