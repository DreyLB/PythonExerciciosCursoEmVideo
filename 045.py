import random
print('-=' * 5)
print('Jo Ken Po')
print('-=' * 5)
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Escolha: '))
pensando = random.randint(0, 2)
print('-=' * 15)
print('Computador jogou {}'.format(itens[pensando]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 15)
# PESANDO EM PEDRA
if pensando == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')
# PESANDO EM PAPEL
if pensando == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    elif jogador == 0:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')
# PESANDO EM TESOURA
if pensando == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')



