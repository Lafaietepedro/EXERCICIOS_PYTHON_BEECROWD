soma = 0
media = 0
contador = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma += idade
        contador += 1

media = soma/contador
print("%.2f" %media)