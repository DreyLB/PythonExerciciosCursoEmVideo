somaidade = 0
qmasculino = 0
qfeminino = 0
maioridademasculino = 0
nomevelho = ''
mulhernova = 0
for c in range(1, 5):
    print('{}ª PESSOA'.format(c))
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    print('__' * 15)

#MÉDIA DAS IDADES
    somaidade = somaidade + idade
    mediaidade = somaidade / c

#SEPARANDO SEXOS E QUANTIFICANDO
    if sexo == 'M':
        qmasculino = qmasculino + 1
    elif sexo == 'F':
        qfeminino = qfeminino + 1

#MAIOR IDADE MASCULINA
    if c == 1 and sexo == 'M':
         maioridademasculino == idade
    if sexo == 'M' and idade > maioridademasculino:
        maioridademasculino = idade
        nomevelho = nome

#FEMININO MENOR DE 20
    if sexo == 'F' and idade < 20:
        mulhernova = mulhernova + 1

#ESCREVENDO
print('Temos aqui {} pessoas do sexo masculino e {} do sexo feminino'.format(qmasculino, qfeminino))
print('A média da idade de todos resulta {:.2f}'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridademasculino, nomevelho))
print('{} mulheres tem idade menor que 20'.format(mulhernova))
