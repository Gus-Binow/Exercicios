#Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
#Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

import os
os.system('cls')

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2


def calculadora():
    try:
        num1 = float(input('Digite o primeiro número: '))
        escolha = input('Escolha a operação (+, -, *, /): ')
        num2 = float(input('Digite o segundo número: '))

        if escolha == '+':
            resul = (soma(num1, num2))
        elif escolha == '-':
            resul = (sub(num1,num2))
        elif escolha == '*':
            resul = (mult(num1,num2))
        elif escolha == '/':
            resul = (div(num1, num2))
        else:
            print('Escolha inválida!')
            return
        
        print(f'O resultado é: {resul:.2f}')

    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')

calculadora()


