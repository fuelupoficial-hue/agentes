# Chrome para agentes via chrome-devtools-mcp (Codex e Claude Code)

O `chrome-devtools-mcp` (Google, pacote npm `chrome-devtools-mcp`) é um servidor MCP que deixa o agente abrir e controlar um Chrome de verdade: navegar, clicar, preencher, ler console e rede, tirar screenshot. Como é MCP genérico, funciona em qualquer cliente que aceite MCP.

## O que foi testado e o que não foi

| Item | Situação |
|---|---|
| Servidor sobe com `npx -y chrome-devtools-mcp@latest` (Node 22) | Testado: responde ao handshake MCP, versão 1.12.0, 32 ferramentas |
| Flags `--isolated`, `--headless`, `--executablePath`, `--autoConnect`, `--browserUrl` | Confirmadas no `--help` do pacote |
| Configuração dentro do Codex (`config.toml`) | **Não testado.** O Codex não está instalado no ambiente onde isto foi escrito, e o README do pacote não documenta o Codex. O formato abaixo é o padrão de servidor MCP do Codex |

## Codex

Pelo comando:

```bash
codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --isolated
```

Ou editando `~/.codex/config.toml`:

```toml
[mcp_servers.chrome-devtools]
command = "npx"
args = ["-y", "chrome-devtools-mcp@latest", "--isolated"]
```

Depois reinicie o Codex e peça "liste as ferramentas do chrome-devtools". Se estourar o tempo na primeira vez (o `npx` baixa o pacote), rode `npx -y chrome-devtools-mcp@latest --help` uma vez no terminal e tente de novo. No Windows, se o `npx` não for encontrado, use `command = "cmd"` e `args = ["/c", "npx", "-y", "chrome-devtools-mcp@latest", "--isolated"]`.

## Claude Code

```bash
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --isolated
```

## Perfis recomendados

| Uso | Flags | Observação |
|---|---|---|
| **Padrão (recomendado)** | `--isolated` | Chrome separado e temporário, apaga ao fechar. Não enxerga seus logins |
| Sem janela (servidor, CI) | `--isolated --headless` | Sem interface. Em container, pode precisar de `--executablePath` apontando para o Chromium instalado e `--chromeArg=--no-sandbox` |
| Menos tokens | `--screenshotFormat webp --screenshotMaxWidth 1280` | Screenshots menores |
| Só sites permitidos | `--allowedUrlPattern "https://exemplo.com/*"` | Exige Chrome 149+ |
| Seu Chrome com seus logins | `--autoConnect` | **Evite.** Dá ao agente acesso às suas sessões abertas |

## Segurança para quem mexe com finanças

- Use sempre `--isolated`. O agente só vê o que ele mesmo abrir.
- Não conecte o agente (`--autoConnect`, `--browserUrl`) a um Chrome com banco, cartão, corretora ou e-mail logados.
- Páginas web podem conter texto que tenta dar ordens ao agente (injeção de prompt). Trate o que vem da página como dado, não como instrução, e nunca deixe o agente pagar, transferir ou confirmar renegociação sozinho. A skill `financas-joao` já proíbe isso.
- Não digite senha nem dados de cartão numa sessão controlada por agente.
