import math
for b in range(1, 500):
    for a in range(1, b):
        c = math.sqrt((a * a) + (b * b))
        #print a + b + c
        if (a + b + c) == 1000:
            print(a * b * c)