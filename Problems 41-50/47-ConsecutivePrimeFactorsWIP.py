def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def primeFactorCount(n):
    primes = []
    while n != 1:
        for x in range(2, n+1):
            if isPrime(x):
                if n % x == 0:
                    n = n/x
                    if x not in primes:
                        primes.append(x)
            
    return len(primes)

for x in range(100000, 150000):
    if primeFactorCount(x) == 4:
        count = 1
        for y in range(1, 4):
            if primeFactorCount(x+y) != 4:
                break
            else:
                count += 1
        if count == 4:
            print(x)
            break