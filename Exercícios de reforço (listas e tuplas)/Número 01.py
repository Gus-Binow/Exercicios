#Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado
import os
os.system('cls')
import unicodedata

compras = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Ovos', 'Pão', 'Açúcar', 'Café']

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def lista_compras(item):
    item_normalizado = remover_acentos(item).lower()

    for produto in compras:
        produto_normalizado = remover_acentos(produto).lower()

        if item_normalizado == produto_normalizado:
            print(f'O item {produto} está disponível na despensa.')
            return

    print(f'O item {item} precisa ser comprado.')


item = input('Digite o item que você quer verificar: ')
lista_compras(item)

