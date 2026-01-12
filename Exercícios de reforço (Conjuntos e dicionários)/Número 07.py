#Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item específico no estoque.
#Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque. 
import os 
os.system('cls')
 
#declaração do dicionário
estoque = { 
    'caderno universitário': 50, 
    'caneta azul': 120, 
    'borracha branca': 30  
} 

#imprime estoque inicial
for chave, valor in estoque.items():
    print(f'{chave}: {valor}')
print()

#entrada do produto e da quantidade
produto = input('Nome do produto a ser atualizado: ').strip().lower()
nova_quantidade = int(input('Nova quantidade: '))
print()

#verificação se o o produto está no estoque
if produto in estoque:
    estoque[produto] = nova_quantidade

    #imprime estoque atualizado
    for chave, valor in estoque.items():
        print(f'{chave}: {valor}')
    print()

else: 
    print('Produto não encontrado no estoque.\n')