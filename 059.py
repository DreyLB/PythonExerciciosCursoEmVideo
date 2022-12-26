n = 0
while n != 5:
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    n = int(input('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números 
[ 5 ] Sair do Programa
Diga o que deseja: '''))

    # Opção 1
    if n == 1:
        print('{} + {} = {}'.format(x, y, x + y))

    # Opção 2
    if n == 2:
        print('{} x {} = {}'.format(x, y, x * y))

    # Opção 3
    if n == 3:
        if x > y:
            print('O maior número é {}'.format(x))
        else:
            print('O maior número é {}'.format(y))
    print('==' * 10)
print('Fim')