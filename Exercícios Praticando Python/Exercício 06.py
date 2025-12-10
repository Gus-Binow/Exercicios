#Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:
#    Pedra ganha de Tesoura (Pedra quebra Tesoura);
#    Tesoura ganha de Papel (Tesoura corta Papel);
#    Papel ganha de Pedra (Papel cobre Pedra);
#    Se ambos escolherem a mesma opção, é um empate.
import os
import random
os.system('cls')

escolha = ['pedra', 'papel', 'tesoura']
jokenpo = input('Escolha: pedra, papel ou tesoura: ').lower()
computador = random.choice(escolha)

if jokenpo not in escolha:
    print('Escolha inválida!')
    exit()

print(f'O computador escolheu: {computador}')


if jokenpo == computador:
    print('Empate!')
elif (
    (jokenpo == 'pedra' and computador == 'tesoura') or \
    (jokenpo == 'tesoura' and computador == 'papel') or \
    (jokenpo == 'papel' and computador == 'pedra')
):
    print('Você venceu!')
else:
    print('Você perdeu!')