lista = []
listum = []
listdois = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listum.append(n)
    else:
        listdois.append(n)
    p = input('Deseja continuar? [S/N]: ').upper().strip()
    if p == 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista apenas com números pares é: {listum}')
print(f'A lista apenas com valores impares é: {listdois}')
