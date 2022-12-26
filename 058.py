from random import randint
print('==' * 15)
print('''Pensei num número
TENTE ADVINHAR!''')
print('==' * 15)
pensando = randint(1, 10)
n = 0
while n != pensando:
    n = int(input('Digite um número: '))
print('Acertou!! Parabéns, também pensei em {}'.format(n))