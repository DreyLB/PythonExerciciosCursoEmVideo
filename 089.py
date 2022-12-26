lista = list()
cont = 0
while True:
    nome = input('Digite o nome: ')
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    p = input('Deseja continuar? [S/N] ').strip().upper()
    cont += 1
    if p == 'N':
        break
print('-=' * 30)
print(f'{"No":<4} {"NOME": <10} {"NOTA 1":<10} {"NOTA 2":<10} {"MEDIA":>8}')
print('-' * 50)
for i, a in enumerate(lista):
    print(f'{i + 1:<4} {a[0]:<10} {a[1][0]:<10} {a[1][1]:<10} {a[2]:>8}')


