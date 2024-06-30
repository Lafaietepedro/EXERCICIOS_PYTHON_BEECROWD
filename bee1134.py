alcool = 0
gasolina = 0
diesel = 0

valid = True

while valid:
    x = str(input())
    if x == "1":
        alcool += 1
    elif x == "2":
        gasolina += 1
    elif x == "3":
        diesel += 1
    elif x == "4":
        valid = False
        break

print("MUITO OBRIGADO")
print("Alcool: %i" %alcool)
print("Gasolina: %i" %gasolina)
print("Diesel: %i" %diesel)