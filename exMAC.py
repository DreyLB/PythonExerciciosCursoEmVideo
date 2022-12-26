cont = 0
soma = [x + y + z for x in range(14) for y in range(14) for z in range(14)]
result = [c for c in soma if c == 13]
print(sorted(soma))
print(len(result))