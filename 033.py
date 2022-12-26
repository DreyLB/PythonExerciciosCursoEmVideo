a = int(input('Digite um número: '))
b = int(input('Digite um outro número: '))
c = int(input('Digite outro número: '))
#Analisando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Analisando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
