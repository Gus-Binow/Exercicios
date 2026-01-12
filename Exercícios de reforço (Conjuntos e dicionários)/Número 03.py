"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

-Quais itens apareceram nas duas listas;
-Quais foram exclusivos de Laura;
-Quais foram exclusivos da Ana;

Escreva um programa que solicite as listas e mostre os resultados dessas comparações. 
"""
import os
os.system('cls')

#recebe a lista de compras das duas
listaA = input('Lista da Ana: ').lower().split()
listaL = input('Lista da Laura: ').lower().split()

#criando conjuntos com set()
setA = set(listaA)
setL = set(listaL)

listaComum = setA & setL
exclusivaAna = setA - setL
exclusivaLaura = setL - setA

print(f'\nItens em ambas as listas: {listaComum}')
print(f'Itens exclusivos de Ana: {exclusivaAna}')
print(f'Itens exclusivos de Laura: {exclusivaLaura}\n')
