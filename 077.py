palavra = ('Mesa', 'Braço', 'Computador', 'Teste', 'Carregador', 'Jarro', 'Programa')
for p in palavra:
    print(f'\nNa palavra "{p}" as vogais são: ', end='')
    for vogal in p:
        if vogal in 'aeiou':
            print(vogal, end=' ')
