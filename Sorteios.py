import random
from time import sleep

print('####Sistema de Sorteios####')

lista_candidatos = []
loop = True
print('Para prosseguir digite o nome do canditado\n ou digite "x" para Finalizar a inserção de nomes.')

while loop:
    nome = input('Digite o nome do fedelho:\t')
    if nome == "x" or nome == "X":
        print('Inserção finalizada!')
        sleep(2)
        print('Processando.')
        sleep(2)
        print('Processando..')
        sleep(2)
        print('Processando...')
        sleep(2)
        loop = False
        break
    else:
        lista_candidatos.append(nome)
        continue
size_list = len(lista_candidatos)
i = (random.randint(0, size_list))-1

escolhido = lista_candidatos[i]

print('O escolhido para se fuder dessa vez será:\t{}'.format(escolhido))

