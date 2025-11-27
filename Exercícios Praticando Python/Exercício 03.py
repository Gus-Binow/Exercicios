#Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
import os
os.system('cls')

def contador_de_vogais(frase):
    contador = 0
    for vogal in frase.lower():
        if vogal in 'aeiouáéíóúãõàèìòùäëïöü':
            contador += 1
    return contador

frase = input('Digite um texto: ')
print(f'O texto contém {contador_de_vogais(frase)} vogais.')