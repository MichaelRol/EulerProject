x = 1
triangle = 0
while True:
    numOfFactors = 0
    triangle = triangle + x
    for factor in range(1, int(triangle ** 0.5) + 1):
        if triangle % factor == 0:
            numOfFactors += 2
    if numOfFactors > 500:
        print(triangle)
        break   
    x = x + 1