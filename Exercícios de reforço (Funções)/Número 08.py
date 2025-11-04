#Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio
#técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
#Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador
#matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
import os
os.system('cls')

soma = lambda a, b: a + b
sub = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Erro: divisão por zero"

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
escolha = input('Escolha a operação (| + | - | * | / |): ')

if escolha == '+':
    print(f'O resultado é: {soma(num1, num2)}')
elif escolha == '-':
    print(f'O resultado é: {sub(num1, num2)}')
elif escolha == '*':
    print(f'O resultado é: {mult(num1, num2)}')
elif escolha == '/':
    print(f'O resultado é: {div(num1, num2)}')
else:
    print('Opção inválida')
