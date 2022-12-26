dados = dict()
dados['nome'] = input('Digite seu nome: ')
dados['media'] = float(input('Qual sua média? '))
if dados['media'] < 7:
    print('Você está reprovado')
else:
    print(f'Parabéns {dados["nome"]}, você está aprovado!')

