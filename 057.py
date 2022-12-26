sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Erro, digite novamente:')).strip().upper()
if sexo == 'M':
    print('Você é do sexo Masculino')
elif sexo == 'F':
    print('Você é do sexo Feminino')