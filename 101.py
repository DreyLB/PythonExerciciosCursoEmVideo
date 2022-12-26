from datetime import datetime
ano = datetime.now().year
def voto(nasc):
    idade = ano - nasc
    if idade < 16:
        print(f'Com {idade} VOCÊ NÃO POSSUI IDADE DE VOTAR.')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos o voto É OPCIONAL.')
    elif 65 > idade >= 18:
        print(f'Com {idade} anos o voto É OBRIGATÓRIO.')


nasc = int(input('Digite seu ano de nascimento: '))
voto(nasc)
