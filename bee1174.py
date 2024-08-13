vetor = []

for i in range(100):
    valor = float(input())
    vetor.append(valor)

for i in range(100):
    if vetor[i] <= 10:
        print('A[%i] = %f' %(i,vetor[i]))