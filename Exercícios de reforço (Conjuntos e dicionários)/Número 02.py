#Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles. 
import os
os.system('cls')

#recebendo as frases
frase1 = input('Texto 1:')
frase2 = input('Texto 2:')

#separando as frases em palavras
palavras1 = set(frase1.split())
palavras2 = set(frase2.split())

#pegando as palavras em comum
comuns = palavras1.intersection(palavras2) 

print(f'Palavras em comum: {comuns}') 


""" resposta do site:
texto1 = set(input("Texto 1: ").lower().split()) 

texto2 = set(input("Texto 2: ").lower().split()) 

comuns = texto1.intersection(texto2) 

print(f"Palavras em comum: {comuns}") 
"""