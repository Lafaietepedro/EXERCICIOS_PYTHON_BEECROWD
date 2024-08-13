# Criando uma lista para armazenar os 10 valores do vetor
X = []

# Lendo os valores de entrada
for i in range(10):
    valor = int(input(f"Digite o valor para X[{i}]: "))
    if valor <= 0:  # Se o valor for nulo ou negativo, substitui por 1
        valor = 1
    X.append(valor)

# Mostrando o vetor X
for i in range(10):
    print(f"X[{i}] = {X[i]}")
