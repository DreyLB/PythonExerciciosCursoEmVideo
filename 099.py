from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os números passados...')
    print('-=' * 30)
    if len(num) > 0:
        for valor in num:
            print(valor, end=' ')
            sleep(0.5)
            if cont == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor
            cont += 1
        print('FIM')
        print(f'Foram digitados {cont} valores')
        print(f'O maior dentre os valores é o {maior}')

    if len(num) == 0:
        print('Não há nenhum valor')


maior(1, 6, 8, 9, 10, 3, 2)
maior(3, 5, 1, 4, 6)
maior(2, 1, 8)
maior(6)
maior()

