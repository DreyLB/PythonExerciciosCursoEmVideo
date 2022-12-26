a = float(input('Digite um número positivo: '))
b = float(input('Digite um outro número positivo: '))
c = float(input('Digite outro número positivo: '))
if a < b + c and b < c + a and c < a + b:
    print('Essas três medidas podem formar um triângulo!')
else:
    print('Essas três medidas não podem formar um triângulo')