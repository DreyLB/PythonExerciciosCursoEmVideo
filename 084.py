info = list()
galera = list()
while True:
    info.append(input('Nome: '))
    info.append(input('Peso: '))
    if len(galera) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]
    galera.append(info[:])
    p = input('Deseja continuar? [S/N] ').strip().upper()
    info.clear()
    if p == 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso cadastrado foi {maior}')
print(f'O menor peso cadastrado foi {menor}')
