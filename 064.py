n = 1
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        c = c + 1
        soma = soma + n
print('''Você digitou {} números
O somatório desses números é {}'''.format(c, soma))