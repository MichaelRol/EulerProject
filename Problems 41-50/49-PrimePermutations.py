def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

primes = []
for x in range(1001, 10000, 2):
    if isPrime(x):
        primes.append(x)


for prime in primes:
    for x in range(1, 10000):
        if prime + x*2 > 10000:
            break
        if isPrime(prime + x) and isPrime(prime + 2*x):
            print(str(prime)+str(prime+x)+str(prime+2*x)) 
