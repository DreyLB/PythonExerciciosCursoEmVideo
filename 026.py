frase = str(input('Digite uma frase: \n')).strip().upper()
q = frase.count('A')
ult = frase.rfind('A')+1
pri = frase.find('A')+1
print('Na frase possui {} "A"'.format(q))
print('O primeira está na posição {}'.format(pri))
print('O último da frase está na posição {}'.format(ult))