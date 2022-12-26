lista = []
c = 0
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    p = input('Deseja continuar? [S/N]: ').upper().strip()
    c = c + 1

    if n == 5:
        cont = cont + 1
    if p == 'N':
        break
print(f'Foram digitados {c} valores')
lista.sort(reverse=True)
print(f'Os valores da lista ordenado de trás pra frente: {lista}')
if 5 not in lista:
    print('Não há o número 5 na lista')
else:
    print(f'O número 5 aparece {cont} vezes na lista')