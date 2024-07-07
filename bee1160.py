t = int(input())

for _ in range(t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1) / 100
    g2 = float(g2) / 100
    anos = 0

    while pa <= pb:
        pa += int(pa * g1)
        pb += int(pb * g2)
        anos += 1

        if anos > 100:
            print("Mais de 1 seculo.")
            break
    else:
        print("%i anos." %anos)