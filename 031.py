distancia = float(input('Digite a distância da sua viagem em Km: '))
if distancia > 200:
    print('Sua viagem de {}Km custará R${:.2f}'.format(distancia, distancia * 0.45))
else:
    print('Sua viagem de {}Km e custará R${:.2f}'.format(distancia, distancia * 0.5))