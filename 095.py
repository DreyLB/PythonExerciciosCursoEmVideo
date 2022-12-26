jogadores = list()
jogador = dict()
gol = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidas jogadas? '))
    gol.clear()
    for c in range(0, tot):
        gol.append(int(input(f'Quantos gols no jogo {c + 1}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    jogadores.append(jogador.copy())
    while True:
        p = input('Deseja continuar? [S/N] ').upper().strip()
        if p == 'S' or 'N':
            break
        else:
            print('ERRO! SÓ PODE SER UTILIZADO S OU N.')
    if p == 'N':
        break
print('-=' * 30)
print(f'{"No":<5} {"NOME":<10} {"GOLS":<10} {"TOTAL":<10}')
print('-=' * 30)
for k, v in enumerate(jogadores):
    print(f'{k:<5}', end=' ')
    for d in v.values():
        print(f'{str(d):<10}', end=' ')
    print()
print('-=' * 30)
while True:
    resp = int(input('Mostrar dados de qual jogador? (Digite 999 para parar): '))
    if resp == 999:
        break
    if resp >= len(jogadores):
        print(f'ERRO! NÃO EXISTE O JOGADOR COM CÓDIGO {resp}')
    else:
        print(f'O levantamento do jogador {jogadores[resp]["nome"]} é: ')
        for k, v in enumerate(jogadores[resp]['gols']):
            print(f'Na partida {k + 1} ele fez {v} gols')
    print('-' * 60)
print('  << VOLTE SEMPRE >>  ')
