valor = float(input('Digite o valor do produto: R$'))
print('''[ 1 ]Dinheiro/Cheque
[ 2 ]Cartão Débito/Crédito (À vista)
[ 3 ]2x no Cartão de Crédito
[ 4 ]A partir de 3x no Cartão de Crédito''')
pag = int(input('Digite a forma de pagamento: '))
if pag == 1:
    print('''A forma de pagamento Dinheiro/Cheque lhe dá um desconto de 10%
    O valor total a se pagar é de R${}'''.format(valor - (valor * 0.1)))
elif pag == 2:
    print('''A forma de pagamento Cartão de Débito/Crédito (à vista) lhe dá um desconto de 5%
        O valor total a se pagar é de R${}'''.format(valor - (valor * 0.05)))
elif pag == 3:
    print('''A forma de pagamento 2x no Cartão de Crédito não possui acréscimo no valor
        O valor total a se pagar é de R${}'''.format(valor))
elif pag == 4:
    print('''A partir de 3x no Cartão de Crédito você pagará 20% de juros
        O valor total a se pagar é de R${}'''.format(valor + (valor * 0.2)))
else:
    print('CÓDIGO INVÁLIDO!!!')
