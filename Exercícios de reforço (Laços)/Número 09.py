#Crie um programa que ajude Ana a exibir somente os livros que
#possuem estoque disponível,no formato: 'Livro disponível: '.
import os
os.system('cls')

livros = [
    {'nome': '1984', 'estoque': 5},
    {'nome': 'Dom Casmurro', 'estoque': 0},
    {'nome': 'O Pequeno Príncipe', 'estoque': 3},
    {'nome': 'O Hobbit', 'estoque': 0},
    {'nome': 'Orgulho e Preconceito', 'estoque': 2}
]

for livro in livros:
    if livro['estoque'] == 0:
        continue
    print(f'Livro disponível: {livro['nome']}')