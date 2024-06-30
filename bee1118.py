def calculaMedia(**args):
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

calculaMedia()

looper = True
while looper:
    y = str(input("novo calculo (1-sim 2-nao)\n"))
    if y == '1':
        calculaMedia()
    elif y == '2':
        looper = False
        break