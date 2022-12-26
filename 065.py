p = ''
cont = 0
n = 0
maior = 0
menor = 99999999999999999
while p != 'N':
    num = int(input('Digite um número: '))
    p = str(input('Deseja continuar? [S/N]')).upper()
    cont = cont + 1
    n = n + num
    media = n / cont
    if num > maior:
        maior = num
        if num < menor:
            menor = num
print('''Foram lidos {} números
A média entre todos os números é {}
O maior número é {}
O menor número é {}'''.format(cont, media, maior, menor))
