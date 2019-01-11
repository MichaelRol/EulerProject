pents = []
for n in range(1, 5001):
    pent = n * (3 * n - 1) * 0.5
    pents.append(pent)

found = False
min = 1000000000000
for x in range(0, 5000):
    for y in range(0, 5000):
        if abs(pents[x] - pents[y]) < min:
            if pents[x] + pents[y] in pents and x != y and abs(pents[x] - pents[y]) in pents:
                min = abs(pents[x] - pents[y])
                found = True
        if found == True:
            break
    if found == True:
        break

print(min)