print('Você receberá um aumento')
salario = float(input('Qual o seu salário? R$'))
if salario >= 1250:
    print('Seu aumento será de 10%\n'
          'De {} você passará receber R${}'.format(salario, salario + (salario * 0.1)))
else:
    print('Você recebeu um aumento de 15%\n'
          'De {} você receberá R${}'.format(salario, salario + (salario * 0.15)))
