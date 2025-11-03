#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto.
#Se algum valor for negativo, mostre uma mensagem informando o erro.
import os
os.system('cls')

atividade_a = int(input('Informe os dias para a atividade A: '))

atividade_b = int(input('Informe os dias para a atividade B: '))

atividade_c = int(input('Informe os dias para a atividade C: '))

dias_totais = atividade_a + atividade_b + atividade_c

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print('Os dias não podem ser negativos')
else:
    print(f'\nO total de dias é de {dias_totais} dias.')

''' usando and no lugar de or 
if atividade_a >= 0 and atividade_b >= 0 and atividade_c >= 0:
    print(f'\nO total de dias é de {dias_totais} dias.')
else:
    print('Os dias não podem ser negativos')
'''