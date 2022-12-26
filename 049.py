num = int(input('Digite um número para ver sua tabuada: '))
for t in range(0, 11):
    print('{} x {} = {}'.format(num, t, num * t))