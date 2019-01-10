
numOfSol = 0
valP = 0
for p in range(1, 1001):
    solutions = 0
    for a in range(1, p/2 + 1):
        for b in range(1, p/2 + 1):
            if (a + b + ((a ** 2) + (b ** 2)) ** 0.5) == p:
                solutions += 1
    if solutions > numOfSol:
        numOfSol = solutions
        valP = p

print(valP)