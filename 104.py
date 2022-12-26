def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Repita novamente\033[m')
        if ok:
            break
    return valor




n = leiaInt('Digite um número: ')
print(f'\033[0;32mVocê acabou de digitar o número {n}\033[m')
