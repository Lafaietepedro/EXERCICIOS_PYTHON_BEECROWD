def fibonacci(n):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib_sequence = [0, 1]

    # Gera o resto da sequência
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    # Retorna os primeiros n números da sequência de Fibonacci
    return fib_sequence[:n]

# Lê um inteiro N do usuário
N = int(input())  # Substitua este valor pelo número desejado

# Gera e imprime os primeiros N números da sequência de Fibonacci
print(" ".join(map(str, fibonacci(N))))
