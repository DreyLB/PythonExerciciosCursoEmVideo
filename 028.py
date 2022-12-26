import random
print('-=' * 10)
print('Pensei num número de 0 a 5')
print('-=' * 10)
num = int(input('Advinhe qual foi o número: '))
adv = random.randint(0, 5)
if adv == num:
    print('Brabooo, conseguiu acertar!!!')
elif adv != num and num < 5:
    print('Caralho kkkkk Burrão, pensei em {}'.format(adv))
elif num > 5:
    print('Larga de ser retardado, é só até 5')