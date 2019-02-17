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

lowest = 120000000000000000000000000
primes = genPrimes(1200)
onedex = 0
twodex = 0 
threedex = 0
fourdex = 0
fivedex = 0
for one in range(0, 10):
    for two in range(one + 1, 800):
        if isPrime(int(str(primes[one]) + str(primes[two]))) and isPrime(int(str(primes[two]) + str(primes[one]))):
            for three in range(two + 1, 900):
                if isPrime(int(str(primes[one]) + str(primes[three]))) and isPrime(int(str(primes[two]) + str(primes[three])))\
                    and isPrime(int(str(primes[three]) + str(primes[one]))) and isPrime(int(str(primes[three]) + str(primes[two]))):
                    for four in range(three + 1, 1000):
                        if isPrime(int(str(primes[one]) + str(primes[four]))) and isPrime(int(str(primes[two]) + str(primes[four])))\
                            and isPrime(int(str(primes[four]) + str(primes[one]))) and isPrime(int(str(primes[four]) + str(primes[two]))) and isPrime(int(str(primes[four]) + str(primes[three]))) and isPrime(int(str(primes[three]) + str(primes[four]))):
                                for five in range(four + 1, 1200):
                                    if isPrime(int(str(primes[one]) + str(primes[five]))) and isPrime(int(str(primes[two]) + str(primes[five])))\
                                        and isPrime(int(str(primes[five]) + str(primes[one]))) and isPrime(int(str(primes[five]) + str(primes[two]))) and isPrime(int(str(primes[four]) + str(primes[five])))\
                                            and isPrime(int(str(primes[five]) + str(primes[three]))) and isPrime(int(str(primes[five]) + str(primes[four]))) and isPrime(int(str(primes[three]) + str(primes[five]))):
                                        if primes[one] + primes[two] + primes[three] + primes[four] + primes[five] < lowest:
                                            lowest = primes[one] + primes[two] + primes[three] + primes[four] + primes[five]

print(lowest)