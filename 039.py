data = int(input('Digite o ano que vôce nasceu: '))
idade = 2020 - data
if idade == 18:
    print('Você precisa se alistar no Exército Brasileiro ainda este ano')
elif idade < 18:
    print('Você ainda não precisa se alista no Exército Brasileiro')
    print('Falta(am) {} ano(s) para você se alistar'.format(18 - idade))
else:
    print('Você já passou do tempo para se alistar no Exército Brasileiro')
    print('Já passou {} ano(s) do tempo de se alistar'.format(idade - 18))
