jogador = dict()
gol = []

jogador['nome'] = input('Nome do jogador: ')
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
soma = 0
print('-=' * 20)
for c in range(0, p):
    g = int(input(f'Quantos gols fez na partida {c + 1}? '))
    gol.append(g)
    soma += g
jogador['gols'] = gol
jogador['total'] = soma
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for c, v in enumerate(gol):
    print(f'    => Na partida {c + 1} o jogador fez {v} gols.')
