#À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
#Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

import os
os.system('cls')

voluntarios_registrados = []

def listar_voluntarios():
    while True:
        nome = input('Digite o nome do voluntário (ou sair para encerrar): ')
        if nome == 'sair':
            break
        voluntarios_registrados.append(nome.title())
        
listar_voluntarios()
print()

for i, voluntario in enumerate(voluntarios_registrados, 1):
    print(f'{i} -> {voluntario}')
