n = int(input())

for i in range(0,n):
    x,y = map(float, input().split(' '))
    if y == 0:
        print('divisao impossivel')
    elif x == 0:
        print('0.0')
    else:
        print(x/y)