t = int(input('digite: '))
c = 0
r = 0

while r <= t:
    a = r + 1
    b = a + 1
    c = b + 1
    d = a*b*c
    if d == t:
        print(a)
        print(b)
        print(c)
    else:
        print('Não')