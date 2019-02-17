def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def genPrimes(x):
    primes = [2]
    numOfPrimes = 1
    num = 3
    while numOfPrimes <= x:
        if isPrime(num):
            numOfPrimes += 1
            primes.append(num)
        num += 2
    return primes

def phi(n):
    primes2n = genPrimes(n)
