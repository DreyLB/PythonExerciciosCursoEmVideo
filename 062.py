p = float(input('Digite o primeiro termo da sua P.A.: '))
r = float(input('Digite a razão da sua P.A.: '))
t = -1
c = -1
while t < 9:
    t = t + 1
    pa = p + (r * t)
    print(pa, end=', ')

y = str(input('\nDeseja continuar? [S/N] ')).strip().upper()

while y == 'S':
    c = int(input('Quantos primeiros termos a mais deseja? '))
    for x in range(1, c + 1):
        t = t + 1
        pa = p + (r * t)
        print(pa, end=', ')
    y = str(input('\nDeseja continuar? [S/N] ')).strip().upper()
print('FIM')
