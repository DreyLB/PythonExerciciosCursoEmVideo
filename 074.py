from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números gerados foram: {n[0: 5]}')
print(f'O maior valor gerado foi: {max(n)}')
print(f'O menor valor gerado foi: {min(n)}')
