a = float(input('Digite um número positivo: '))
b = float(input('Digite um outro número positivo: '))
c = float(input('Digite outro número positivo: '))
if a < b + c and b < c + a and c < a + b:
    print('Essas três medidas podem formar um triângulo!')
    if a == b == c:
        print('Formará um triângulo equilátero.')
    elif a != b != c:
        print('Essas retas formam um triângulo escaléno')
    elif a > b and c or b > a and c or c > a and b:
        print('Essas retas podem formar um triângulo isósceles.')
else:
    print('Essas três medidas não podem formar um triângulo')
