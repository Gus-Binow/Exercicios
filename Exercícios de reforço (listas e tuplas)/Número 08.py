#Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.
import os
os.system('cls')

pedidos = []
pedidos = input('Pedidos feitos (separados por vírgula): ').split(', ')

tamanho = len(pedidos)
pedidos.pop(tamanho-1)

print(f'Pedidos finais')