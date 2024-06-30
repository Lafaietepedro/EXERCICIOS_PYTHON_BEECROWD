s = 0
d = 1

for i in range(1,101,2):
    s += i/d
    d = d*2

print("%.2f" %s)