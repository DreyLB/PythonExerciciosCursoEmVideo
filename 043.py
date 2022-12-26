peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura) ** 2
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e você está com peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é {:.2f} e você tem obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e você está com obesidade morbida'.format(imc))
