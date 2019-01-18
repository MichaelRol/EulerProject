def factorial(val):
    total = 1
    for x in range(1, val + 1):
        total *= x
    return total 

def ncr(n, r):
    val = factorial(n)/(factorial(r)*factorial(n-r))
    return val

count = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        if ncr(n, r) > 1000000:
            count += 1

print(count)