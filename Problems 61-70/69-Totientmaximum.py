def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def phi(n):
    count = 1
    for x in range(2, n):
        if gcd(n, x) == 1:
            count += 1
    return count

max = 0
value = 0
count = 0
for n in range(1000000, 0, -1):
    nphin = float(n)/float(phi(n))
    if nphin > max:
        count = 0
        max = nphin
        value = n
    else:
        count += 1
    if count > 100:
        break

print(n)