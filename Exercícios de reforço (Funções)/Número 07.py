#Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços.
# Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
#Crie um programa que junte as listas e exiba o resultado no formato produto: preço
import os
os.system('cls')

produtos = input('Digite os produtos separados por vírgula: ').split(',')
valores = input('Digite os preços separados por vírgula: ').split(',')
print()

lista_produtos = [str(produto.strip()) for produto in produtos]
lista_precos = [float(preco.strip()) for preco in valores]

lista = dict(zip(lista_produtos, lista_precos))
print(lista)
