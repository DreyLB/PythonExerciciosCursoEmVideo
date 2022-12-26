import random

print('Estes são seus números da sorte: ')
while True:
    lista = list()
    for c in range(0, 6):
        sorte = random.randint(1, 60)
        lista.append(sorte)

    print(lista)
    p = input('Deseja mais um? [S/N] ').upper().strip()
    lista.clear()
    if p == 'N':
        break





