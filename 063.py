n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
c = 2
print('{}, {}'.format(t1, t2), end=', ')
while c != n:
    t3 = t1 + t2
    print(t3, end=', ')
    t1 = t2
    t2 = t3
    c = c + 1
print('Acabou')