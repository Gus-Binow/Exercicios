#Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares.
#O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
import os
os.system('cls')

livros = 5

while livros != 0:
    livros -= 1
    print(f'Venda realizada! Estoque restante: {livros}')

print('Estoque esgotado')