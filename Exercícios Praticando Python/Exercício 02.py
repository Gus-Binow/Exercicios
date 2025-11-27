#Crie um programa que peça ao usuário um número de CPF
#e verifique se ele tem 11 dígitos e contém apenas números.
import os
os.system('cls')

def valida_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: o CPF deve conter apenas números.'
    
    elif len(cpf) != 11:
        return 'Erro: O CPF deve possuir 11 números.'
    
    return 'CPF válido'

cpf = input('Digite seu CPF(sem pontos ou traços): ')
print(valida_cpf(cpf))
