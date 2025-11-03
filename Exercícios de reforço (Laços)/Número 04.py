#Você está recebendo uma lista de valores representando os produtos de sua loja virtual
#e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
import os
os.system('cls')

valores = [10, 20, 30, 40, 50]

total = 0

for valor in valores:
    total += valor
print(f'A soma total das receitas é: {total}')

#forma mais simples de resolver o problema
#print(f'A soma total das receitas é: {sum(valores)}')