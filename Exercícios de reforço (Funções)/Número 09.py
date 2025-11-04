#Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
#Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.
import os
os.system('cls')

def valor(preco):
    def desconto(desc):
        return preco * ((100 - desc) / 100)
    return desconto

compra = int(input('Digite o valor da compra: ')) 
porcentagem = int(input('Digite a porcentagem de desconto: ')) 

calcula_desconto = valor(compra)

print(f'\nPreço final com desconto: {calcula_desconto(porcentagem):.2f}')