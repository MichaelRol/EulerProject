def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

primes = []
for x in range(0, 20000):
    if isPrime(x):
        primes.append(x)

def primeFactorCount(n):
    primeFactors = []
    for x in range(0, len(primes) - 1):
        if n % primes[x] == 0:
            n = n/primes[x]
            if primes[x] not in primeFactors:
                primeFactors.append(primes[x])
            if n == 1:
                break
            x = x - 1
            
    return len(primeFactors)


for x in range(1, 150000):
    if primeFactorCount(x) == 4:
        count = 1
        for y in range(1, 4):
            if primeFactorCount(x+y) != 4:
                x = x + y
                break
            else:
                count += 1
        if count == 4:
            print(x)
            break
