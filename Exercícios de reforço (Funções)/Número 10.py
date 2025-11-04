#Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro.
# Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
#Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
import os
os.system('cls')

def soma_recursiva(contador): 
    if contador == 1: 
        return 1 
    return contador + soma_recursiva(contador - 1) 

contador = int(input('Digite um número: '))

print(f'a soma de 1 a {contador} é: {soma_recursiva(contador)}')
