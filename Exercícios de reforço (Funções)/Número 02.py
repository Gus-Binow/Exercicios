#Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
#Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
import os
os.system('cls')

def tamanho_palavra(palavra):
    return len(palavra)

tamanho = input('Digite uma palavra: ')
print(f'A palavra tem {tamanho_palavra(tamanho)} caracteres.')
