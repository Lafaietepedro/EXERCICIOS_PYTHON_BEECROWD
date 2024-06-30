valid = True

while valid:
    x,y = map(int, input().split(' '))
    if x == y:
        valid = False
        break
    elif x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")