velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Muito bem, continue dirigindo com segurança.')
elif velocidade > 80:
    print('Você está acima da velocidade permitida de 80Km/h!')
    print('Foi multado em {}'.format(multa))