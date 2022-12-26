p = float(input('Preço do produto: '))
print('O produto que custava {} teve 5% de desconto.'.format(p))
print('Depois do desconto de 5% aplicado: R${:.2f}'.format(p - p * 0.05))
