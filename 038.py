n = int(input('Digite um número inteiro: '))
num = int(input('Digite outro número inteiro: '))
if n < num:
    print('O número {} é maior\nO número {} é menor'.format(num, n))
elif n > num:
    print('O número {} é maior\nO número {} é menor'.format(n, num))
