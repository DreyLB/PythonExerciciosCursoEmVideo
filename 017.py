import math
op = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateo adjacente: '))
hip = math.hypot(op, adj)
print('A hipotenusa vale: {}'.format(hip))
