casa = float(input('Qual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual sua renda mensal? R$'))
tempo = int(input('Deseja pagar a dívida em quantos anos? '))
mes = tempo * 12
prestacao = casa / mes
if prestacao > salario * 0.3:
    print('Seu emprétimo não foi aprovado, pois o valor das parcelas excedem 30% da sua renda mensal')
    print('A dívida ficaria em R${:.2f} mensais, e sua renda mensal é de R${:.2f}'.format(prestacao, salario))
elif prestacao <= salario * 0.3:
    print('Parabéns! Você realizará o sonho da casa própria!')
    print('O valor mensal a se pagar será de R${:.2f}'.format(prestacao))