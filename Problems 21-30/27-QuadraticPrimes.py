consec = 0
maxn = 0
def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while(True):
            if isPrime(n**2 + a*n + b):
                n += 1
            else:
                break
        if n > maxn:
            maxn = n
            consec = a * b
print(consec)