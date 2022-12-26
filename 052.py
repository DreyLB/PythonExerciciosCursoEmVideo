n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[32m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
if tot > 2:
    print('\n{} não é primo'.format(n))
else:
    print('\n{} é um número primo'.format(n))