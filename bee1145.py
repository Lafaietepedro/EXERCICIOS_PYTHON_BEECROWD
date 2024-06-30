X, Y = map(int, input().split())

contador = 0  # Contador para controlar quantos números foram impressos em uma linha

for i in range(1, Y + 1):
    # Imprime o número seguido de um espaço em branco
    print(i, end="")
    contador += 1
    
    # Se o contador for igual a X, significa que X números foram impressos
    # Então, deve passar para a próxima linha e resetar o contador
    if contador == X:
        print()
        contador = 0
    else:
        # Se não for o último número da linha, imprime um espaço em branco
        print(" ", end="")

# Verifica se ainda há números a serem impressos na linha
# Se sim, imprime uma nova linha para garantir que a saída seja formatada corretamente
if contador > 0:
    print()
