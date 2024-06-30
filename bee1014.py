senhaCorreta = 2002
verifier = False

while verifier == False:
    senhaEntrada = int(input())
    if senhaEntrada == senhaCorreta:
        verifier = True
        print("Acesso Permitido")
    else:
        print("Senha Invalida")