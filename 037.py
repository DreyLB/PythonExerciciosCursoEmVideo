num = int(input('Digite o número que deseja converter: '))
opcao = int(input('[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\nEscolha para qual deseja converter: '))
bin = bin(num)[2:]
oct = oct(num)[2:]
hex = hex(num)[2:]
if opcao == 1:
    print('O valor {} em binário é {}'.format(num, bin))
elif opcao == 2:
    print('O valor {} em Octal é {}'.format(num, oct))
elif opcao == 3:
    print('O número {} em Hexadecimal é {}'.format(num, hex))