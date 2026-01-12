#Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições. 
import os
os.system('cls')

convidados = set()

while True:
    nome = input('Digite o nome do convidado ou "sair" para encerrar: ')

    if nome.lower() == 'sair':
        break

    convidados.add(nome)

print(f'Convidados confirmados: {', '.join(convidados)}') 