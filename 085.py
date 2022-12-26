lista = [[], []]
for b in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'A sequência de números pares foi {lista[0]}')
print(f'A sequência de números impares foi {lista[1]}')
