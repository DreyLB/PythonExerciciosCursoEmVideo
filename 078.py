valores = []
print('=' * 50)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('=' * 50)
for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}')
print('=' * 50)
print(f'O maior valor foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor foi {min(valores)} na posição {valores.index(min(valores))}')
print('=' * 50)
