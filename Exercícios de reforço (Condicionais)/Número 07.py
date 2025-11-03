'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
'''
import os
os.system('cls')

nota1 = float(input('Digite a primeira nota: ').replace(',', '.'))
nota2 = float(input('Digite a segunda nota: ').replace(',', '.'))
nota3 = float(input('Digite a terceira nota: ').replace(',', '.'))

media = (nota1 + nota2 + nota3) / 3
print()
print(f'A média é {media:.2f}')

if media >= 7:
    print('Aprovado.')
elif  5 <= media < 7:
    print('Recuperação.')
else:
    print('Reprovado.')