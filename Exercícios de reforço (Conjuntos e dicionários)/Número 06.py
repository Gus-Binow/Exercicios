#O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.
import os
os.system('cls')

#cria um dicionário para os produtos
produtos = {}

#cria um loop de 3 itens
for i in range(3):
    #recebe o nome do produto
    nome = input('Digite o nome do produto: ')

    #recebe o valor do produto
    valor = int(input('Digite o valor do produto: '))
    print()
    
    #associa o valor do produto com o nome
    produtos[nome] = valor 

#imprime o dicionário
print(f'Dicionário de produtos: {produtos}') 

    