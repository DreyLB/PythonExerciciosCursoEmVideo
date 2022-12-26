nome = str(input('Digite seu nome completo: ')).strip()
pri = nome.split()
print('O seu primeiro nome é: {} \nO seu último nome é: {}'.format(pri[0], pri[len(pri) - 1]))
