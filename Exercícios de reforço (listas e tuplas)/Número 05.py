#Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?
import os
os.system('cls')

lista_atual = ['Ana', 'Pedro', 'Carlos']
print(f"Lista atual de convidados: {lista_atual}")
nova_lista = []

nome = input('Digite o nome do novo convidado: ')
pos = int(input('Digite a posição na qual deseja inserir o convidado: '))
posicao = pos - 1

nova_lista = lista_atual
nova_lista.insert(posicao, nome)

print(f'Lista atualizada de convidados: {nova_lista}')
