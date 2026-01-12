#Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas.
#Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.
import os
os.system('cls')

#Recebe as tarefas do time A
team_A = {
    tarefa.strip().lower()
    for tarefa in input('Tarefas da equipe A: ').split(',')
}

#Recebe as tarefas do time B
team_B = {
    tarefa.strip().lower()
    for tarefa in input('Tarefas da equipe B: ').split(',')
}

#união das duas tarefas
tarefas = team_A | team_B

#impressão das duas tarefas
print(f'Tarefas finais: {sorted(tarefas)}\n')

#recebe uma tarefa a ser removida
arrancar = {
    tarefa.strip().lower()
    for tarefa in input('Tarefa(s) a ser(em) removida(s): ').split(',')
}

#remoção de uma tarefa desejada
tarefa_final = tarefas - arrancar

#impressão da lista final de tarefas
print(f'Tarefas finais: {sorted(tarefa_final)}')