from random import randint
from time import sleep
numeros = list()


def sorteio():
    print('-=' * 25)
    print('Foram sorteados os número: ', end='')
    for c in range(0, 5):
        n = (randint(1, 10))
        print(n, end=' ')
        numeros.append(n)
        sleep(0.5)
    print()
    print('-=' * 25)


def somapar():
    soma = 0
    for c, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares resulta: {soma}')


sorteio()
somapar()


