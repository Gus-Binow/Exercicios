#Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?
import os
os.system('cls')

corredores = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda']

errado = input('Digite o nome incorreto: ')
certo = input('Digite o nome correto: ')

if errado in corredores:
    pos = corredores.index(errado)
    corredores[pos] = certo
else:
    print('Nome não encontrado!')
    
print(corredores)
