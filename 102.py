def fatorial(n = 1, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (OPCIONAL) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    fac = 1
    print(f'O fatorial de {n} é: ', end='')
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        fac *= c
    return fac


n = int(input('Digite um número inteiro: '))
print(fatorial(n, show=True))
