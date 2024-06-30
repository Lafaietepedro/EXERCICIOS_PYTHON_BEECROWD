i = 0
soma = 0

while i < 2:
    x = float(input())
    if 0 <= x <= 10:
        soma += x
        i += 1
    else:
        print("nota invalida")
        
print('media = %.2f' %(soma/2))

