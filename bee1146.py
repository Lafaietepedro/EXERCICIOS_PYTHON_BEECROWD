# Define a função para imprimir a sequência de 1 a X
def print_sequence(X):
    # Cria uma lista de números de 1 a X
    sequence = list(range(1, X + 1))
    
    # Converte os números em strings
    sequence = [str(num) for num in sequence]
    
    # Junta os números com um espaço e imprime o resultado
    print(" ".join(sequence))

# Lê a entrada do usuário
while True:
    X = int(input())
    
    # Se X for zero, interrompe o loop
    if X == 0:
        break
    
    # Caso contrário, imprime a sequência de 1 a X
    print_sequence(X)
