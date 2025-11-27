#Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta.
#O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
import os
os.system('cls')

conta = float(input('Digite o valor da conta: '))
tip = float(input('Digite a porcentagem de gorjeta: '))

gorjeta = conta * (tip/100)
total = conta + gorjeta

print(f"Valor da gorjeta: R$ {gorjeta:.2f}") 
print(f"Total a pagar: R$ {total:.2f}")