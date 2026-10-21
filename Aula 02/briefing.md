# A02 — EX01 — Briefing da equipe
Use dados inventados. Preencha os campos; não trate lacunas como decisões.
Ferramenta: editor de texto/Markdown. Não há programa para executar.

## Pedido recebido
Precisamos controlar empréstimos de equipamentos, consultar disponibilidade e registrar saídas e devoluções. O cliente pediu rapidez e segurança, ainda sem critérios definidos.

## Problema e resultado desejado
- Problema observado no cenário: Dificuldade em consultar rapidamente o inventário disponivel e rastrear quem está em posse de cada equipamento, gerando risco de perdas ou atrasos. 
- Quem utilizará (papel, não nome real):Operador do sistema de controle/ almoxarife.
- Resultado desejado:Sistema que permita consultar a disponibilidade de forma ágil e registrar com segurança a saída e a devolução dos itens.
- Dentro do escopo inicial:
Consulta de disponibilidade de equipamentos.
Registro de saída de equipamentos para um solicitante.
Registro de devolução dos equipamentos emprestados.
- Fora do escopo inicial:
Criação de banco de dados relacional
Autenticação avançada de usuários e controle de perfis múltiplos.
Relatórios gerenciais e envio de notificações automáticas.


## Perguntas ao cliente
| ID | Pergunta | Impacto da resposta | Resposta ou “a confirmar” |
|---|---|---|---|
| D01 | O que define exatamente se um equipamento está "disposivel"? | Altera os filtros exibidos na consulta do inventário | A confirmar|
| D02 |Quais campos do solicitante são obrigatórios no momento de registrar uma saída?| Define a estrutura de dados necessária para registrar o empréstimo.| A confirmar |
| D03 | Como o sistema deve se comportar caso ocorra uma tentativa de devolução de um item que não consta como emprestado?|Define a regra de validação e a mensagem de erro exibida ao operador. | A confirmar |

## Decisões
| ID | Decisão/hipótese | Estado (proposta/confirmada) | Evidência da confirmação |
|---|---|---|---|
| DEC01 | Utilizar dados estáticos em memória (amostra de três equipamentos do CSV) para validar os fluxos iniciais sem dependência de banco de dados. | proposta |

## Revisão
O revisor consegue separar pedido, hipótese e decisão? Sim. O pedido original foi isolado na seção inicial, as incertezas foram tratadas como dúvidas pendentes marcadas como "a confirmar", e a escolha da amostra foi documentada como hipótese de projeto.

