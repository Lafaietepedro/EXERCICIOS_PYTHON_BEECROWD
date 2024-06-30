n = int(input())
soma = 0
contador = 0

for i in range(1,n+1):
    x,y = map(int, input().split(' '))
    while contador < y:
        if x % 2 == 0:
            soma += x
            contador += 1
            x += 1
        else:
            x += 1
    print(soma)
