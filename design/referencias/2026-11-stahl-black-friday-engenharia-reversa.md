# Engenharia reversa · 3 anúncios de Black Friday de oficina/autopeças (referências do João)

Imagens enviadas pelo João (anúncios de terceiros: uma live de varejo, Lima's Centro Automotivo, Pneus Planalto). Não ficam no repositório. Aqui só os princípios, nunca o layout, texto, marca ou imagem de ninguém.

## Veredito do João sobre o nosso v3
"Fundo preto e fonte limpa" parece **IA/básico**. Padrão esperado: arte **em camadas**, com elementos, **fotos reais** dos equipamentos e de um **carro real**, **fonte estilizada** e **texto desenhado**.

## O que os três têm em comum (as camadas)
| Camada | O que é |
|---|---|
| 1. Fundo | Escuro, com textura (fibra de carbono, listras diagonais) e **luz laranja** vindo de baixo |
| 2. Título | "BLACK FRIDAY" em **letra 3D**: face cromada (prata) e dourada, contorno preto grosso, extrusão e brilho |
| 3. Foto real | Peças e produtos reais recortados (disco de freio, filtro, óleo, amortecedor, mola), grandes, com sombra e reflexo no chão |
| 4. Selo de oferta | Anel neon, círculo ou moeda com preço ("R$ 239,90") ou "ATÉ 20% OFF" bem grande |
| 5. Selos auxiliares | Moedas de "%" laranja, "10x" em etiqueta, flocos de brasa/chamas |
| 6. Fita de alerta | Faixa amarela/preta com "BLACK FRIDAY »" repetido, cruzando a peça |
| 7. Assinatura | Logotipo da oficina, rodapé legal pequeno e validade da campanha |
| 8. Paleta | Preto + laranja/âmbar + amarelo + branco/cromo. Alto contraste, saturada |

## Princípios
- Mais denso que o v3, mas **com hierarquia**: título → oferta → produto → assinatura.
- O produto real é o herói; a letra 3D dá o impacto de "Black Friday".
- Elementos repetidos em tamanhos diferentes (moedas, chamas) criam ritmo.
- Preço fechado ("a partir de R$ X") e prazo ("campanha válida até") dão credibilidade.

## O que dá para fazer em código (sem IA)
Fundo texturizado, luz, letra 3D cromada/dourada (gradiente + contorno + extrusão), fita, selos, moedas, anéis neon, faíscas. Teste: `../arte/kit-titulo.html`.

## O que depende de foto real
Disco de freio, óleo e filtro, mola/amortecedor, carro, equipe e a própria oficina. Fonte: foto do cliente (melhor) ou Adobe Stock com licença (candidatos `isGenTech:false`).
