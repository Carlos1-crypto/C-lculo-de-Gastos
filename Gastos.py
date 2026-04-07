class gasto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

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
            print("Por favor, ingrese un número válido.")