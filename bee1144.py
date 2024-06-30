x = 1

contador = int(input())

if 1<contador<1000:
    for i in range(0,contador):
        print("%i %i %i" %(x,(x**2),(x**3)))
        print("%i %i %i" %(x,(x**2)+1,(x**3)+1))
        x += 1