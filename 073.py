tabela = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
          'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará', 'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco',
          'Goiás', 'Coritiba', 'Botafogo')
cont = 0
tab = -1
for cont in range(0, 5):
    cont = cont + 1
    tab = tab + 1
    print(f'O {cont}º colocado é {tabela[tab]}')
print('=' * 30)

print('Os últimos colocados são:')
for cont in range(1, 5):
    print(tabela[-cont])
print('=' * 30)

ordem = sorted(tabela)
print('A tabela em ordem é:')
for posicao in ordem:
    print(posicao)
print('=' * 30)
t = tabela.index('Ceará') + 1
print(f'O Ceará está em {t}º lugar')
