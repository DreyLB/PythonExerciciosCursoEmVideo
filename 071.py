valor = float(input('Digite um valor de saque: R$'))
print('Quantas notas deseja?')
um = int(input('Quantas notas de R$1: '))
cinco = int(input('Quantas notas de R$5: '))
dez = int(input('Quantas notas de R$10: '))
cinquenta = int(input('Quantas notas de R$50: '))
cem = int(input('Quantas notas de R$100: '))
total = (um * 1) + (cinco * 5) + (dez * 10) + (cinquenta * 50) + (cem * 100)
if total > valor:
    print('O valor excedeu R${}, tente o saque novamente'.format(total - valor))
elif total < valor:
    print('Saque de R${} sendo feito, ainda falta R${}, repita o processo para tirar o resto'.format(total, valor - total))
elif total == valor:
    print('Saque de R${} realizado com sucesso'.format(total))
