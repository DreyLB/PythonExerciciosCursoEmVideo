p = float(input('Digite o primeiro termo da sua P.A.: '))
r = float(input('Digite a razão da sua P.A.: '))
print('''Os dez primeiros termos de sua progressão aritmética é: ''')
for t in range(0, 10):
    print(p + (r * t), end=', ')
