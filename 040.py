n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))
media = (n1 + n2 + n3 + n4)/4
print('A sua média é: {}'.format(media))
if media < 5:
    print('Você está reprovado')
elif 5 <= media < 7:
    print('Você está de recuperação')
elif media >= 7:
    print('Você está aprovado')
