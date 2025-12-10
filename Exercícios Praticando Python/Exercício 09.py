#Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
import os

atividades = []

def exibir_opcoes(): 
    print('1 - Adicionar tarefa')
    print('2 - Visualizar tarefa')
    print('3 - Remover tarefa')
    print('4 - Sair\n')

def adicionar_atividade():
    acionar = input('\nDigite a tarefa: ')
    print(f'\nA tarefa {acionar} foi adicionada!')
    atividades.append(acionar)
    voltar_ao_menu()

def listar_atividades():
    print('\nListando atividades: ')
    for indice, i in enumerate(atividades):
        print(f'{indice+1} - {i}')
    print
    voltar_ao_menu()

def remover_atividade():
    for indice, atividade in enumerate(atividades):
        print(f'{indice + 1} - {atividade}')

    remo = int(input('\nDigite o número da atividade que deseja remover: '))
    remov = remo - 1  # ajusta para índice da lista

    if 0 <= remov < len(atividades):
        atividade_removida = atividades.pop(remov)
        print(f'\nA atividade {atividade_removida} foi removida com sucesso!\n')
        
        for i, a in enumerate(atividades):
            print(f'{i + 1} - {a}')
    else:
        print('Atividade não encontrada')
    voltar_ao_menu()


def sair_programa(): 
    print('Saindo do gerenciador de tarefas. Até mais!')

def opcao_invalida(): 
    print('Opção invalida! Escolha uma opção entre 1 e 4.')
    voltar_ao_menu()

def voltar_ao_menu(): 
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            adicionar_atividade()
        elif opcao_escolhida == 2:
            listar_atividades()
        elif opcao_escolhida == 3:
            remover_atividade()
        elif opcao_escolhida == 4:
            sair_programa()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()