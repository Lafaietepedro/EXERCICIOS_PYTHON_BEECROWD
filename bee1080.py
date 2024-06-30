maior = 0
indexMaior = 0

for i in range(1,101):
    x = int(input())
    if x > maior:
        maior = x
        indexMaior = i
         
print(maior)
print(indexMaior)