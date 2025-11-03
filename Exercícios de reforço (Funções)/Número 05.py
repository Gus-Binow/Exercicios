#Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
#As vendas são informadas em uma única linha separadas por espaços.
#Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
import os
os.system('cls')

def vendas(valores):
    return sum(valores) 

entradas = input('Digite os valores das vendas: ').split()

soma = [int(entrada) for entrada in entradas]

print(f'O total das vendas é: {vendas(soma)}')

#resposta do site
''''
valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 
'''