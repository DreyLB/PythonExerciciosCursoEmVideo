ano = int(input('Digite o ano que você nasceu: '))
bis = ano % 4
if bis == 0:
    print('O ano que você nasceu é bissexto')
else:
    print('Você não nasceu num ano bissexto')
