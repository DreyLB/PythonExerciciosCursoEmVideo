dicionario = dict()
lista = list()
listf = list()
somidade = 0
while True:
    dicionario['nome'] = input('Digite o nome: ')
    while True:
        dicionario['sexo'] = input('Digite o sexo [M/F]: ').strip().upper()
        if dicionario['sexo'] == 'M' or 'F':
            break
        else:
            print('ERRO! SÓ PODE SER UTILIZADO M OU F.')

    dicionario['idade'] = int(input('Digite a idade: '))
    somidade += dicionario['idade']

    while True:
        p = input('Deseja continuar? [S/N] ').upper().strip()
        if p == 'S' or 'N':
            break
        else:
            print('ERRO! SÓ PODE SER UTILIZADO S OU N.')
    lista.append(dicionario.copy())
    if dicionario['sexo'] == 'F':
        listf.append(dicionario.copy())
    if p == 'N':
        break
media = somidade / len(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idades é {media}')
print('As mulheres cadastradas são: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=', ')

print('\nAs pessoas com idade acima da média são: ', end='')
for c in lista:
    if c['idade'] > media:
        print(f'{c["nome"]}', end=', ')

