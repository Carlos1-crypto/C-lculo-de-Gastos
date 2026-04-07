from Gastos import *
import matplotlib.pyplot as plt

def calculos():
    print("Bem-vindo ao calculador de gastos!")
    while True:
        salario = (input("Por favor, digite o salário: "))
        try:
            salario = float(salario)
            break
        except ValueError:
            print("Por favor, ingresse um número válido para o salário.\n")
            return
        
    gastos()
    for g in gastos_list:
        salario -= g.valor

    if salario < 0:
        print(f'\nInfelizmente o seu saldo está NEGATIVO: {salario:.2f}')
        print("\nSeus gastos foram:")
        for g in gastos_list:
            print(f'{g.nome}: R${g.valor:.2f}')
            gastos_totais = sum(g.valor for g in gastos_list)
        print(f"O total de seus gastos foi {gastos_totais:.2f}")
    else:    
        print(f'\nFelizmente o seu saldo está POSITIVO final é: {salario:.2f}')
        print("\nSeus gastos foram:")
        for g in gastos_list:
            print(f'{g.nome}: R${g.valor:.2f}')
            gastos_totais = sum(g.valor for g in gastos_list)
        print(f"O total de seus gastos foi {gastos_totais:.2f}")
        plt.pie([g.valor for g in gastos_list], labels=[g.nome for g in gastos_list], autopct='%1.1f%%')
        plt.title('Distribuição dos Gastos')
        plt.axis('equal')
        plt.show()

if __name__ == "__main__":
    calculos()