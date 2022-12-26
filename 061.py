p = float(input('Digite o primeiro termo da sua P.A.: '))
r = float(input('Digite a razão da sua P.A.: '))
t = -1
while t < 11:
    t = t + 1
    print(p + (r * t), end=', ')