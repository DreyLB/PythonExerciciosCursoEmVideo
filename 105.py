def notas(*n, sit = False):
    d = dict()
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['media'] = sum(n) / len(n)
    if sit:
        if d['media'] >= 7:
            d['situação'] = 'A turma está numa sitação boa'
            print(d)
        if 5 < d['media'] < 7:
            d['situação'] = 'A situação da turma é razoável'
        if 4 <= d['media'] < 5:
            d['situação'] = 'A turma precisa estudar'
        elif d['media'] < 4:
            d['situação'] = 'A turma vai mal'
            print(d)
    else:
        print(d)


notas(8, 6, 7, 5, 10)
