n = (int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')),
     int(input('Digite um valor: ')))


print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu {n.index(3) + 1} vezes')
else:
    print('Não há números 3 na listagem digitada')
print('O números pares foram:', end=' ')

for num in n:
    if num % 2 == 0:
        print(num, end=' ')



