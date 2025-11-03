#Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2).
#Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
import os
os.system('cls')

print('Calculadora de IMC\n')
peso = float(input('Digite seu peso(kg): ').replace(',', '.'))
alt = float(input('Digite sua altura(m): ').replace(',', '.'))

imc = peso / (alt**2)
print(f'\nSeu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está com o peso ideal.')
else:
    print('Você está acima do peso.')