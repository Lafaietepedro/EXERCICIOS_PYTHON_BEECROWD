x = int(input())
z = int(input())
contador = 1
soma = x

while z <= x:
    z = int(input())

while soma < z:
    x += 1
    soma += x
    contador += 1

print(contador)