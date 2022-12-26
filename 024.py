cidade = input('Digite o nome de uma cidade: ').strip()
parte = cidade.split()
seg = parte[0].upper()
print('O nome da cidade começa com Santo? {}'.format('SANTO' in seg))