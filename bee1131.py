valid = True
grenais = 0
Inter = 0
Gremio = 0
Empates = 0

while valid:
    interGols,gremioGols = map(int, input().split(' '))
    if interGols > gremioGols:
        Inter += 1
    elif interGols < gremioGols:
        Gremio += 1
    else:
        Empates += 1
    grenais += 1
    repete = str(input("Novo grenal (1-sim 2-nao)\n"))
    if repete == '2':
        break

print("%i grenais" %grenais)
print("Inter:%i" %Inter)
print("Gremio:%i" %Gremio)
print("Empates:%i" %Empates)
if Inter > Gremio:
    print("Inter venceu mais")
elif Inter < Gremios:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")