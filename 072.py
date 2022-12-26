numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorte', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
ext = int(input('Digite um número de 0 a 20: '))
while ext < 0 or ext > 20:
    ext = int(input('Tente novamente um número de 0 a 20: '))
print(f'O número {ext} por extenso é {numero[ext]}.')