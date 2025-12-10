#Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.

import os
os.system('cls')
import random
 
def adivinhar_numero():
    computador = random.randint(1, 100)
 
    while True:
        try:
            escolha = int(input('Tente adivinhar o número (1-100): '))
 
            if not 1 <= escolha <= 100:
                raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100.')
 
            if escolha < computador:
                print('Muito baixo! Tente novamente.')
            elif escolha > computador:
                print('Muito alto! Tente novamente.')
            else:
                print(f'Parabéns! Você acertou o número {computador}')
                break
 
        except ValueError as computador:
            print(f'Entrada inválida: {computador}')

adivinhar_numero()