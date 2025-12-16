#Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma. 
import os
os.system('cls')

notas = []
notas = input('Digite as notas dos alunos separadas por vírgula: ').split(', ')
notas = [float(nota) for nota in notas]

tamanho = len(notas)
media = sum(notas) / tamanho

print(f'Média final da turma: {media:.2f}')