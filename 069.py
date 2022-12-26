idade = 0
h = 0
m = 0
while True:
    p = int(input('Digite a idade: '))
    s = str(input('Qual o sexo? [M/F]')).upper().strip()

    if p > 18:
        idade = idade + 1

    if s == 'M':
        h = h + 1

    if s == 'F' and p > 20:
        m = m + 1

    f = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if f == 'N':
        break

print(idade)
print(h)
print(m)