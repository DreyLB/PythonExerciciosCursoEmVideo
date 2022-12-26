listagem = ('Carregador de Notebook', 35,
            'Notebook Lenovo Ideapad S145', 2000,
            'Mouse', 40,
            'Cadeira Gamer', 600)
print('-' * 60)
print(f'{"PREÇO DOS PRODUTOS":^60}')
print('-' * 60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
