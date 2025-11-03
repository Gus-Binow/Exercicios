'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
import os
'''
import os
os.system('cls')

dist = float(input('Digite a distância percorrida (em Km): '))

if dist <= 100:
    print('Valor do pedágio: R$ 10,00')
elif 100 < dist <= 200:
    print('Valor do pedágio: R$ 20,00')
else:
    print('Valor do pedágio: R$ 30,00')