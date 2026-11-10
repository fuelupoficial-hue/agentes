# Agentes da FUEL UP

Agentes de IA da FUEL UP, agência de tráfego pago para oficinas mecânicas (Uberlândia-MG).

| Pasta | Conteúdo |
|---|---|
| [`fuel-up/SKILL.md`](fuel-up/SKILL.md) | **Agente geral**: cuida de prospecção, vendas, campanhas, atendimento, conteúdo, financeiro e rotina. |
| [`design/SKILL.md`](design/SKILL.md) | **Skill de design**: pesquisa de referências antes de tudo, modelos de anúncio para oficina (motor de código e Canva), checklist de designer. |
| [`financas/SKILL.md`](financas/SKILL.md) | **Skill de finanças do João** (`financas-joao`): triagem, plano de quitação com simulador (`financas/scripts/quitacao.py`), negociação, orçamento por envelopes, revisão semanal, caixa PF × PJ e reserva. Modelos em `financas/modelos/`. |
| [`configuracao/chrome-devtools-mcp.md`](configuracao/chrome-devtools-mcp.md) | Como ligar o Chrome ao Codex e ao Claude Code via MCP, com perfil seguro. |
| [`criativos/`](criativos/) | Criativos já feitos (Stahl Car, Black Friday), versões v1 a v3. |
| [`contexto/empresa.md`](contexto/empresa.md) | Dados da empresa que o agente lê antes de agir. Preencher os campos "A PREENCHER". |
| [`contexto/financeiro.md`](contexto/financeiro.md) | Os 5 números e as dívidas do João, lidos pela skill de finanças. Sem senha, CPF ou número de cartão. |

Agentes relacionados:
- [`mentalidade-aroldo`](https://github.com/fuelupoficial-hue/mentalidade-aroldo): mentor de prosperidade (mentalidade, dívidas, disciplina).

## Como usar

**No Claude:** copie `fuel-up/SKILL.md` para uma skill (`~/.claude/skills/fuel-up-geral/SKILL.md`) ou cole o conteúdo, sem o cabeçalho, nas instruções de um Projeto. Anexe `contexto/empresa.md` como conhecimento.

**No ChatGPT:** crie um GPT, cole o corpo de `fuel-up/SKILL.md` nas instruções e suba `contexto/empresa.md` como arquivo.

## Próximos passos

1. Preencher `contexto/empresa.md`.
2. Criar especialistas quando houver volume: prospecção, copy de anúncios, relatórios.
3. Ligar ferramentas (agenda, e-mail, CRM) para o agente executar, não só sugerir.
