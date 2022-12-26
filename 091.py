from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': '', 'Jogador 2': '', 'Jogador 3': '', 'Jogador 4': ''}
dados['Jogador 1'] = randint(1, 6)
dados['Jogador 2'] = randint(1, 6)
dados['Jogador 3'] = randint(1, 6)
dados['Jogador 4'] = randint(1, 6)
print('Valores tirados nos dados: ')
for j, n in dados.items():
    print(f'O {j} tirou {n} no dado')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 14)
print(f'{"== RANKING DE JOGADORES ==":^25}')
for j, n in enumerate(ranking):
    print(f'{j + 1}º lugar: O {ranking[j][0]} tirou {ranking[j][1]} no dado')
    sleep(1)

