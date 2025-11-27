#Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras.
#Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
import os
os.system('cls')

def palavra_dez(palavras):
    lista = []
    for palavra in palavras:
        if len(palavra) >= 10:
            lista.append(palavra)
    return lista

texto = input('Digite um texto: ')
palavras = texto.split()

print(f'Palavras longas encontradas: {palavra_dez(palavras)}')
