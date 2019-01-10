def factorial(num):
    val = 1
    for x in range(1, num + 1):
        val *= x
    return val

grand = 0
for x in range(3, 1000000):
    total = 0
    for dig in str(x):
        total += factorial(int(dig))
    if total == x:
        grand += x

print(grand)
    