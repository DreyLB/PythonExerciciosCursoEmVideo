from datetime import datetime
info = dict()
while True:
    info['nome'] = input('Digite seu nome: ')

    nasc = int(input('Digite a data de nascimento: '))
    if (datetime.now().year - nasc) < 18:
        print('Você ainda não pode ter carteira de trabalho')
        break
    else:
        info['idade'] = (datetime.now().year - nasc)

    info['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
    if info['CTPS'] == 0:
        break

    info['contrato'] = int(input('Ano de contratação: '))
    info['salario'] = int(input('Salário: R$'))
    info['aposentadoria'] = (info['contrato'] - nasc) + 30
    break

print('-=' * 15)
for k, v in info.items():
    print(f'  - {k} tem valor {v}')


