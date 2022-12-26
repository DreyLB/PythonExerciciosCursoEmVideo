from time import sleep
def contador(i, f, p):
    print(f'Iniciando contador {i} até {f} de {p} em {p}:')
    sleep(2.5)
    print('-=' * 25)
    cont = i
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.5)
        print('Fim')
        print('-=' * 25)
    else:
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)
        print('Fim')
        print('-=' * 25)


contador(1, 10, 1)
contador(10, 1, 2)
print('Sua vez de escolher')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('De quanto em quanto: '))
contador(a, b, c)
