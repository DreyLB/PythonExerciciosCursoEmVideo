matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]: ^5}]', end='')
    print()
print(f'O somatório de todos os valores são {soma}')
somter = 0
for l in range(0, 3):
    somter += matriz[l][2]
print(f'O somatório dos números da terceira coluna é {somter}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')


