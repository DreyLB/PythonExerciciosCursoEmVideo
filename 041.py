ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria mirim'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e está na categoria infantil'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos e está na categoria junior'.format(idade))
elif 19 < idade <= 20:
    print('O atleta tem {} anos e está na categoria sênior'.format(idade))
elif 20 < idade:
    print('O atleta tem {} anos e está na categoria master'.format(idade))
