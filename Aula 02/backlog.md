# A02 — EX03 — Organização do trabalho

## Backlog e quadro
Estados: A fazer / Em andamento / Em revisão / Concluído.
Prioridade expressa valor/urgência; dependência indica o que precisa existir antes.

| ID | Ação pequena | Requisito | Prioridade | Depende de | Responsável | Revisor | Estado | Evidência de conclusão |
|---|---|---|---|---|---|---|---|---|
| T01 | Redigir o briefing inicial com escopo, dúvidas e restrições. | Briefing | Alta | Nenhuma | Autor da Dupla | Revisor da Dupla | Concluído | Arquivo `briefing.md` revisado e sem lacunas tratadas como fatos. |
| T02 | Escrever requisitos funcionais, regras e cenários de aceite (válido, inválido e fronteira). | RF01, RF02, RF03 | Alta | T01 | Autor da Dupla | Revisor da Dupla | Concluído | Arquivo `requisitos.md` preenchido e simulado no papel. |
| T03 | Criar o esboço estruturado de telas em texto (consulta e registro de saída). | RQ01 | Média | T02 | Revisor da Dupla | Autor da Dupla | Em revisão | Esboços contendo título, campos, ações e mensagens validados pelo par. |
| T04 | Mapear os campos sintéticos necessários e justificar sua finalidade. | Dados | Média | T02 | Autor da Dupla | Revisor da Dupla | A fazer | Tabela de dados preenchida sem uso de informações reais. |
| T05 | Inicializar repositório local e estruturar pastas (`docs/`, `src/`, `testes/`). | Git / Infra | Baixa | T01 | Revisor da Dupla | Autor da Dupla | A fazer | Execução bem-sucedida de `git init` e verificação da raiz limpa. |

## Plano de versionamento
- **Pasta nova de trabalho e raiz Git (sem expor nome de usuário):** Pasta isolada do projeto de controle de equipamentos, verificada com `git rev-parse --show-toplevel`.
- **Ferramenta/versão observada:** Git local via terminal PowerShell integrado no VS Code.
- **Arquivos que serão revisados antes do primeiro commit em A04:** Documentos de planejamento em `docs/` (`briefing.md`, `requisitos.md`, `backlog.md`, `evidencias.md`).
- **Arquivos que não devem entrar no histórico:** Dados sensíveis, arquivos temporários de sistema, pastas de IDE locais ou planilhas com dados reais.
- **Como conferir estado e alterações:** Utilizar os comandos `git status --short` e `git diff` no terminal.
- **Quem revisa e qual evidência deve existir:** O colega da dupla audita os arquivos modificados antes de registrar qualquer versão.
- **Pendência de instalação/permissão, se houver:** Nenhuma pendência crítica identificada no ambiente local padrão.
- **Plano de cópia de segurança autorizado pela instituição (Git local não substitui backup):** Cópia manual periódica da pasta de trabalho para o diretório de documentos autorizado pelo aluno.