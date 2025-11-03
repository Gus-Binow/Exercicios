#Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu.
#Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:
import os
os.system('cls')

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print('Projeto ausente')
        continue
    print(projeto)

''' resposta do site
for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)
'''