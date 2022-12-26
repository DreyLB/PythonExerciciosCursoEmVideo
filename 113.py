def leiaInt(msg):
    while True:
        try:
            ni = int(input('Digite um número inteiro: '))
        except Exception as erro:
            print(f'\033[0;31mErro com {erro.__class__}\033[m')
        else:
            return ni


def leiaReal(msg):
    while True:
        try:
            nr = float(input('Digite um número real: '))
        except Exception as erro:
            print(f'\033[0;;31mErro devido a {erro.__class__}\033[m')
        else:
            return nr


ni = leiaInt('Digite um número inteiro: ')
nr = leiaReal('Digite um número real: ')
print(f'O número inteiro digitado foi {ni} e o número real foi {nr}')
