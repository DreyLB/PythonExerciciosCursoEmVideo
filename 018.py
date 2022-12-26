import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O seno de {:.2f} é {:.2f} \nSeu cosseno {:.2f} \nSua tangente {:.2f}'.format(ang, sen, cos, tg))
