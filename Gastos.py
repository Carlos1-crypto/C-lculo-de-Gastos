from dataclasses import dataclass

@dataclass
class gasto:
    nome: str
    valor: float

gastos_list = []

def gastos():
    while True:
        nome = input("Digite o nome do gasto (ou 'sair' para terminar): ")
        if nome.lower().strip() == 'sair':
            break
        try:
            valor = float(input("Digite o valor do gasto: "))
            gastos_list.append(gasto(nome, valor))
            print(f"Gasto adicionado com sucesso \n")
        except ValueError:
            print("Por favor, digite um número válido.")