#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais.
#Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate
import os
os.system('cls')

macas = int(input('Digite a quantidade de maçãs vendidas esse mês: '))

bananas = int(input('Digite a quantidade de bananas vendidas esse mês: '))

if bananas > macas:
    print('As bananas tiveram mais vendas.')
elif macas > bananas:
    print('As maçãs tiveram mais vendas.')
else:
    print('As maçãs e bananas tiveram a mesma quantidade de vendas>')