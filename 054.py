totmaior = 0
totmenor = 0
for c in range(0, 7):
    ano = int(input('Digite o ano que você nasceu: '))
    idade = 2020 - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('{} desses ainda não atingiram a maioridade'.format(totmenor))
