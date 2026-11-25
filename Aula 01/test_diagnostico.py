"""A01: testes da função itens_disponiveis. Escreva os casos que faltam."""

import copy
import unittest

from diagnostico import itens_disponiveis

DADOS = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo", "quantidade": 5},
]


class ItensDisponiveis(unittest.TestCase):
    def test_limite_um_devolve_os_que_tem_estoque(self):
        self.assertEqual(itens_disponiveis(DADOS, 1), ["Notebook", "Cabo"])

    def test_lista_vazia_devolve_lista_vazia(self):
        self.assertEqual(itens_disponiveis([], 1), [])

    def test_quantidade_igual_ao_limite_entra(self):
        self.assertEqual(itens_disponiveis(DADOS, 3), ["Notebook", "Cabo"])

    def test_nao_altera_lista_recebida(self):
        antes = copy.deepcopy(DADOS)
        itens_disponiveis(DADOS, 1)
        self.assertEqual(DADOS, antes)


if __name__ == "__main__":
    unittest.main()