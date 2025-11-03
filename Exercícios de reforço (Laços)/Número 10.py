'''
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos.
As regras são as seguintes:

- O nome de usuário deve ter pelo menos 5 caracteres.
- A senha deve ter pelo menos 8 caracteres.
- João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos,
o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
'''
import os
os.system('cls')

while True:
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha que deseja utilizar: ')

    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.\n')

    elif len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres.\n')

    else:
        print('Cadastro realizado com sucesso!')
        break

'''Resposta do site
while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break
'''

''' Me distraí e fiz de outro jeito
def cadastrado_de_conta():
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha que deseja utilizar: ')

    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.\n')
        cadastrado_de_conta()
    elif len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteresn.\n')
        cadastrado_de_conta()
    else:
        print('Cadastro realizado com sucesso!')

cadastrado_de_conta()
'''