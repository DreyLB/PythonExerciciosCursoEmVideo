salario = float(input('Digite seu salário por hora: R$ '))
horas = int(input('Quantas horas você trabalha por dia? '))
mes = (horas * 30) * salario
ir = mes - (mes * 0.11)
inss = ir - (ir * 0.08)
sindicato = inss - (inss * 0.05)
print('Seu salário bruto é de R${}'.format(mes))
print('Descontando IR fica: R${}'.format(ir))
print('Descontando INSS fica: R${}'.format(inss))
print('Descontando Sindicato fica: R${}'.format(sindicato))
print('No final seu salário líquido é R${}, um total de {:.2f}% descontado do seu bruto.'.format(sindicato, 100 - ((100 * sindicato) / mes)))