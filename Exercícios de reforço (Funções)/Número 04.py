#Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str,
#faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:
import os
os.system('cls')

def converter_para_inteiro(lista):
    return[int(telefone) for telefone in lista]

def verificar_inteiro(lista):
    for num in lista:
        if not isinstance(num, int):
            return 'Erro na conversão'
    return 'Todos os números foram convertidos corretamente!' 

telefones = ['11987654321', '21912345678', '31987654321', '11911223344']

telefones_convertidos = converter_para_inteiro(telefones)
print(verificar_inteiro(telefones_convertidos))