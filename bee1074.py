n = int(input())
lista = []
i = 0

while i < n:
    x = int(input())
    lista.append(x)
    i = i + 1

for numero in lista:
    if (numero % 2 == 0) and (numero > 0):
        print("EVEN POSITIVE")
    elif (numero % 2 == 0) and (numero < 0):
        print("EVEN NEGATIVE")
    elif (numero % 2 != 0) and (numero > 0):
        print("ODD POSITIVE")
    elif (numero % 2 != 0) and (numero < 0):
        print("ODD NEGATIVE")
    elif numero == 0:
        print("NULL")