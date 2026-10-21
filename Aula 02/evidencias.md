# A02 — EX04 — Evidências e revisão
Dados exclusivamente sintéticos. Não incluir credenciais, dados pessoais nem caminhos com nome de usuário.

## Entrega
- Briefing: Problema, usuário, resultado, três dúvidas pendentes, escopo definido e amostra com três equipamentos do CSV.
- Requisitos, regras e critérios: Três requisitos funcionais (RF01, RF02, RF03), duas regras de negócio propostas (RN01, RN02) e um requisito de qualidade (RQ01) com cenários de aceite (válido, inválido e fronteira).
- Esboços de telas: Esboço estruturado em texto da Tela 1 (Consulta de Inventário) e Tela 2 (Registro de Saída).
- Backlog e plano de versionamento: Cinco tarefas rastreáveis, papéis alternados entre autor/revisor, estados de quadro e plano de versionamento local.

## Ferramentas
- IDE e pasta de trabalho conferidas: VS Code aberto na pasta nova do projeto de controle de equipamentos.
- Versão de Git observada: Git local via terminal PowerShell.
- Comando executado e resultado (remover caminhos pessoais): `git status --short` (retornou arquivos não rastreados em `docs/`).
- Raiz Git conferida: Confirmada com `git rev-parse --show-toplevel`.
- Instalação pendente ou sucesso confirmado: Sucesso confirmado para o ambiente local básico; sem pendências críticas.

## Simulação em papel
- Critério: CA01 (Registro de saída válido)
- Entrada: Equipamento `EQ-001` (Disponível) e solicitante `P-001`.
- Ação: Acionar o botão "Confirmar Saída".
- Resultado esperado: Status atualizado para "Emprestado" e mensagem de sucesso exibida.
- Resultado da simulação: Comportamento validado com sucesso passo a passo no papel.
- Dúvida encontrada: Como o sistema deve se comportar caso o solicitante não possua cadastro prévio na amostra.

## Revisão por pares
- Trecho antes: "O sistema deve registrar a saída rapidamente."
- Sugestão com justificativa: Transformar em um requisito verificável detalhando a entrada e a ação, evitando termos vagos como "rapidamente".
- Decisão do autor: Aceito. O requisito foi reescrito para especificar o vínculo entre equipamento disponível e solicitante.
- Trecho depois: "O sistema deve permitir registrar a saída de um equipamento selecionado para um solicitante."

## Auditoria
- **Situação 1 (Requisitos vagos):** Escolha: É problema. Justificativa: Termos subjetivos impedem a validação objetiva por outra dupla. Evidência: Ausência de critérios de entrada e saída.
- **Situação 2 (Acessibilidade e Foco):** Escolha: É problema. Justificativa: A remoção de indicadores visuais de foco prejudica a navegação por teclado. Evidência: Teste de navegação sem mouse (Tab).
- **Situação 3 (Dados reais na demonstração):** Escolha: É problema. Justificativa: Violação de privacidade e uso desnecessário de dados reais. Evidência: Presença de informações de identificação pessoal no material.

## Reflexão individual
- O que consigo explicar: A diferença entre um pedido informal de cliente e um requisito verificável, além da importância de separar hipóteses de fatos.
- Em que preciso de apoio: Aprofundar o mapeamento de casos de fronteira complexos em regras de negócio com múltiplas condições.
- Próximo passo para A03 (raciocínio no papel; ambiente virtual e primeiro commit em A04): Estudar a lógica de pseudocódigo e transição de algoritmos para Python para a próxima aula.