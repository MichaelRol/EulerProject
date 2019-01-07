total = 1

for x in range(2, 1002):
    if (x % 2 == 0):
        total = total + 2*(x**2) + 2 - x
    else:
        total = total + 2*(x**2) - (x - 1)
    
print(total)