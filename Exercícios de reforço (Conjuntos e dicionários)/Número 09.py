#Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento.
#O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante.
#O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista. 
import os
os.system('cls')

#dicionario de conjuntos de participantes
participantes = { 
    'Workshop_1': {'Alice', 'Bruno', 'Carla', 'Diego'}, 
    'Workshop_2': {'Fernanda', 'Gustavo', 'Helena'}
}

#imprime os participantes do workshop
print('Workshop 1:', ', '.join(participantes['Workshop_1']))
print('Workshop 2:', ', '.join(participantes['Workshop_2']))
print()

#participante que vai ser excluido
excluido = input('Nome do participante a ser removido: ')
print()

#exclui do conjunto que estiver
if excluido in participantes['Workshop_1']:
    participantes['Workshop_1'].discard(excluido)

elif excluido in participantes['Workshop_1']:
    participantes['Workshop_2'].discard(excluido)

else:
    print('Participando não encontrado.')

#imprime os participantes depois da exclusão
print("Lista atualizada de participantes:") 
print('Workshop 1:', ', '.join(participantes['Workshop_1']))
print('Workshop 2:', ', '.join(participantes['Workshop_2']))
print()