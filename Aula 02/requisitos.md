# A02 — EX02 — Requisitos, regras e aceite
Objetivo: ligar necessidade a evidência observável. Ferramenta: editor e simulação em papel.
Complete três RF, duas RN e um RQ. Os IDs abaixo são espaços de trabalho, não respostas.
Não há código ou aplicação implementada nesta atividade.

## Requisitos
| ID | Descrição verificável | Necessidade atendida | Prioridade e justificativa | Regra vinculada |
|---|---|---|---|---|
| RF01 | O sistema deve exibir a lista de equipamentos disponíveis com base na amostra fixa.| Consultar disponibilidade rapidamente. | Alta — pré-requisito para qualquer operação de empréstimo.| RN01|
| RF02 |O sistema deve permitir registrar a saída de um equipamento selecionado para um solicitante. | Registrar saídas com segurança.|Alta — núcleo principal do pedido do cliente. | RN01, RN02|
| RF03 | O sistema deve permitir registrar a devolução de um equipamento emprestado, atualizando seu status.| Registrar devoluções e liberar o item. | Média — necessário para fechar o ciclo de empréstimo.| RN02 |
| RQ01 | O fluxo completo de consulta e registro de saída deve poder ser concluído utilizando exclusivamente a navegação por teclado (Tab e atalhos).| Garantir acessibilidade básica no teste guiado. | Garantir acessibilidade básica no teste guiado.| Baixa — restrição de qualidade proposta para validação. |

## Regras do domínio
| ID | Regra proposta | Confirmada ou a confirmar? |
|---|---|---|
| RN01 | Não é permitido registrar a saída de um equipamento cujo status atual já seja "Emprestado". | a confirmar |
| RN02 |O registro de saída exige obrigatoriamente a identificação do solicitante e um equipamento válido da amostra.| a confirmar|

## Critérios e simulações da funcionalidade prioritária
| ID | RF/RQ | Condição inicial | Ação | Resultado esperado | Tipo de caso |
|---|---|---|---|---|---|
| CA01 | RF02 | Equipamento EQ-001 disponível e solicitante P-001 informado.| Operador aciona o botão "Confirmar Saída". | Status atualizado para "Emprestado" e mensagem "Saída registrada com sucesso" exibida. | Válido |
| CA02 | RF02 | Equipamento EQ-002 com status "Emprestado". | Operador tenta acionar o botão "Confirmar Saída". | Sistema bloqueia a operação e exibe mensagem de erro de item indisponível. | Inválido |
| CA03 | RF02| Equipamento EQ-003 disponível, mas campo de solicitante deixado em branco.| Operador aciona o botão "Confirmar Saída". | Sistema bloqueia o registro e alerta que a identificação do solicitante é obrigatória. | Fronteira |

Resultado observado na simulação em papel (não é teste de software):
A simulação permitiu validar que as restrições evitam empréstimos duplicados antes mesmo de existir código implementado.
Ambiguidades descobertas:
Não estava claro se o sistema deveria permitir digitar um novo solicitante na hora ou apenas selecionar de uma lista pré-existente.
Decisão de correção:
Ficou definido provisoriamente que o campo aceitará texto livre para simulação na amostra, registrando como pendência para o cliente.

## Esboço de duas telas
Descreva título, campos, ações, resultado/erro e destino da navegação.
- Tela 1:Consulta de Inventário
Título: Consulta de Disponibilidade (Amostra CSV)

Campos: Tabela exibindo ID, Nome e Status dos equipamentos (ex.: EQ-001, Multímetro, Disponível).

Ações: Botão [Consultar Disponibilidade] e botão [Selecionar para Saída].

Resultado/Erro: Exibe a listagem atualizada ou aviso de lista vazia.

Destino da navegação: Direciona para a Tela de Registro de Saída ao selecionar um item disponível.
- Tela 2:Registro de Saída
Título: Registrar Saída de Equipamento

Campos: Campo de texto para identificação do solicitante e exibição do equipamento escolhido.

Ações: Botão [Cancelar] e botão [Confirmar Saída].

Resultado/Erro: Mensagem de sucesso ao registrar ou mensagem de erro em caso de campos vazios/itens já emprestados.

Destino da navegação: Retorna para a Tela 1 após a confirmação.

## Dados e finalidade
| Campo | Para qual tarefa? | Exemplo sintético | Necessário ou dúvida? |
|---|---|---|---|
| ID do Equipamento | RF01 (Consulta) e RF02 (Saída) | EQ-001 | Necessário |
| Status do Equipamento | RF01 (Consulta de disponibilidade) | Disponível / Emprestado | Necessário |
| Identificação do Solicitante | RF02 (Registro de saída) | P-001 (Carlos Silva) | Necessário |

Critério de conclusão: outra dupla consegue repetir a simulação e localizar os IDs ligados.
Dica: compare entradas válidas, inválidas e exatamente no limite que sua regra definiu.
