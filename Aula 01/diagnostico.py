"""A01: complete somente a função. Dados fictícios."""


def itens_disponiveis(equipamentos, limite):
    # TODO: devolver, na ordem original, os nomes com quantidade maior ou igual ao limite.
    # Lacuna intencional: None faz o programa mostrar PENDENTE.
    nomes = []
    for item in equipamentos:
        if item["quantidade"] >= limite:
            nomes.append(item["nome"])
    return nomes


equipamentos = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo", "quantidade": 5},
]

if __name__ == "__main__":
    for registros, limite in [(equipamentos, 1), (equipamentos, 4), ([], 1)]:
        resultado = itens_disponiveis(registros, limite)
        print("Limite", limite, "=>", "PENDENTE" if resultado is None else resultado)