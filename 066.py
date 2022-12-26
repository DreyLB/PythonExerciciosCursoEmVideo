cont = 0
soma = 0
while True:
    p = int(input('Digite um número(PARA TERMINAR DIGITE 999): '))
    if p == 999:
        break
    soma = soma + p
    cont = cont + 1
print(f'''Foram digitados {cont} números.
O Somatório entre eles é {soma}.''')
