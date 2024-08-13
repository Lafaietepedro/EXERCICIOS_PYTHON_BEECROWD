vetor = []

valor = int(input())
vetor.append(valor)

for i in range(9):
    valor *= 2
    vetor.append(valor)

for i in range(10):
    print('N[%i] = %i' %(i,vetor[i]))