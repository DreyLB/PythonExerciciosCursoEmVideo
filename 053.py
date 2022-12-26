frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = junta[::-1]
print('''Frase invertida:
{}'''.format(inverso))
if junta == inverso:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndomo')