from random import choice
print('Um aluno será sorteado')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a4, a2, a3, a1]
sorteio = choice(lista)
print('O aluno sorteado foi {}'.format(sorteio))