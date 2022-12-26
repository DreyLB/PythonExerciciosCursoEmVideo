valores = []
while True:
    a = int(input('Digite um valor: '))
    if a not in valores:
        valores.append(a)
        print('valor adicionado')
    a = input('Deseja constinuar? [S/N] ').strip().upper()
    if a == 'N':
        break
valores.sort()
print(f'Os números adicionados a lista foram: {valores}')
