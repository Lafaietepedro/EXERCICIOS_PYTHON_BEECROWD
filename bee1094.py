n = int(input())
total = 0
totalCoelhos = 0
totalRatos = 0
totalSapos = 0

for i in range(0,n):
    q,t = input().split(' ')
    total += int(q)
    if t == 'C':
        totalCoelhos += int(q)
    elif t == 'R':
        totalRatos += int(q)
    elif t == 'S':
        totalSapos += int(q)

porcentCoelhos = totalCoelhos/total * 100
porcentRatos = totalRatos/total * 100
porcentSapos = totalSapos/total * 100

print('Total: %i cobaias' %total)
print('Total de coelhos: %i' %totalCoelhos)
print('Total de ratos: %i' %totalRatos)
print('Total de sapos: %i' %totalSapos)

print('Percentual de coelhos: %.2f %%' %porcentCoelhos)
print('Percentual de ratos: %.2f %%' %porcentRatos)
print('Percentual de sapos: %.2f %%' %porcentSapos)