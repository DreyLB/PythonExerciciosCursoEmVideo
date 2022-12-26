total = 0
maior = 0
menor = 999999999999999999999999999999999999999
while True:
    #p = str(input('Nome do Produto: '))
    v = float(input('Digite o Valor: R$'))

    total = total + v

    if v > 1000:
        maior = maior + 1

    if v < menor:
        menor = v

    b = str(input('Deseja continuar? [S/N]')).upper().strip()
    if b == 'N':
        break

print(f'''O valor total da compra foi R${total:.2f}
{maior:.0f} produtos custam mais de R$1000
O produto de menor valor custa R${menor:.2f}''')
