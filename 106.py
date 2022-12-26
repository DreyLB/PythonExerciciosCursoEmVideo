from time import sleep
c = ('\033[m',           # 0 - sem cores
       '\033[0;30;41m',  # 1 - vermelho
       '\033[0;30;42m',  # 2 - verde
       '\033[0;30;43m',  # 3 - amarelo
       '\033[0;30;44m',  # 4 - azul
       '\033[0;30;45m',  # 5 - roxo
       '\033[7;30m'      # 6 - branco
       )

def ajuda(p):
    print(c[5])
    help(p)
    print(c[0])


def titulo(msg, cor):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    p = input('Função ou Biblioteca > ')
    resp = p.upper().strip()
    if resp == 'FIM':
        break
    titulo(f'Acessando a biblioteca {p}...', 4)
    sleep(2)
    ajuda(p)
    sleep(1)
print()
titulo('FIM DO PROGRAMA', 1)
