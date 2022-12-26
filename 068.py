import random
v = 0
while True:
    print('Vamos brincar de Par ou Ímpar')
    pc = random.randint(1, 10)
    n = int(input('Digite um valor de 0 a 10: '))
    escolha = ' '
    resultado = pc + n
    par = resultado % 2
    while escolha not in 'PI':
        escolha = str(input('Escolha par ou ímpar: [P/I] ')).upper().strip()
    print(f'O computador escolheu {pc} e o total é {resultado}')

    if escolha == 'P':
        if resultado % 2 == 0:
            print('Venceu')
            v = v + 1
        else:
            print('Perdeu')
            break

    if escolha == 'I':
        if resultado % 2 == 1:
            print('Venceu')
            v = v + 1
        else:
            print('Perdeu')
            break
    print('=-'*20)
    print('Vamos jogar novamente')
    print('=-' * 20)

print(f'Você venceu {v} vezes')
