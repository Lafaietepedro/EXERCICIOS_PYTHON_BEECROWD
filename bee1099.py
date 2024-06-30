n = int(input())

for i in range(0,n):
    soma = 0
    x,y = map(int, input().split(' '))
    if x > y:
        for j in range(y+1,x):
            if j % 2 != 0:
                soma += j
    elif x < y:
        for j in range(x+1,y):
            if j % 2 != 0:
                soma += j
    print(soma)