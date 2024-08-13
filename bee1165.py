n = int(input())

for contagem in range(n):
    lista = []
    x = int(input())
    i = 1

    while i <= x:
        if x % i == 0:
            lista.append(i)
        i += 1
    
    if len(lista) == 2:
        print('%i eh primo' %x)
    else:
        print('%i nao eh primo' %x)