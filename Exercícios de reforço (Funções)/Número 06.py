#Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa 
#filtrar apenas os valores pares de uma lista de números informada pelo usuário.
#Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
import os
os.system('cls')

def par(num):
    return int(num) % 2 == 0

numeros = input('Digite os números separados por espaço: ').split()
pares = filter(par, numeros)

print(list(pares))