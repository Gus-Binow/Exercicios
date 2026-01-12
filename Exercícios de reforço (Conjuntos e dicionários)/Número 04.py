# Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.
import os
os.system('cls')

#recebe as permissões e as solicitações
permissao = set(input('Permissões principais: ').strip().lower().split(','))
solicitado = set(input('Permissôes solicitadas: ').strip().lower().split(','))

#compara as listas de permissões para ver se é um subconjunto
if solicitado.issubset(permissao):
    print('As permissões solicitadas fazem parte das permissões principais.')
else:
    print('As permissões solicitadas não fazem parte das permissões principais.')


""" Resolução do site:
permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 

permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

for i in range(len(permissoes_principais)):  

    permissoes_principais[i] = permissoes_principais[i].strip() 

for i in range(len(permissoes_solicitadas)):  

    permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 

if eh_subconjunto:  

    print("As permissões solicitadas fazem parte das permissões principais.")  

else:  

    print("As permissões solicitadas não fazem parte das permissões principais.")
"""