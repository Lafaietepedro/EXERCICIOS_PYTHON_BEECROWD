valid = True

while valid:
    m,n = map(int, input().split(' '))
    if (m == 0 or n == 0) or (m < 0 or n < 0):
        valid = False
    elif m > n :
        lista = []
        soma = 0
        for i in range(n,m+1):
            soma += i
            sum = ' '
            lista.append(i)
        soma = str(soma)
        sum = 'Sum=%s' % soma
        lista.append(sum)
        print(*lista)
    elif m < n :
        lista = []
        soma = 0
        sum = ' '
        for i in range(m,n+1):
            soma += i
            lista.append(i)
        soma = str(soma)
        sum = 'Sum=%s' % soma
        lista.append(sum)
        print(*lista)
