# Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas.
# Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.
# Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?
import os
os.system('cls')

estoque_1 = tuple(input('Digite os itens do primeiro estoque (separados por vírgula): ').split(', '))
estoque_2 = tuple(input('Digite os itens do segundo estoque (separados por vírgula): ').split(', '))

estoque_combinado = estoque_1 + estoque_2

print(estoque_combinado)