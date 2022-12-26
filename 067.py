while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    for t in range(0, 11):
        print('{} x {} = {}'.format(num, t, num * t))
    print('-=' * 20)
    p = input('Deseja continuar? [S/N]: ').upper()
    print('-=' * 20)
    if p == 'N':
        break
print('O programa terminou')
