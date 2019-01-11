hexes = []
pents = []
for num in range(0, 100000):
    hex = num * (2 * num - 1)
    hexes.append(hex)

for num in range(0, 100000):
    pent = num * (3 * num - 1) * 0.5
    pents.append(pent)

val = 286
while(True):
    t = val * (val + 1) * 0.5
    if t > 100000 * (200000-1):
        break
    if t in hexes and t in pents:
        print(t)
        break
    val = val + 1

