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

count = 0
primes = genPrimes(100)
for one in primes:
    for two in primes:
        if one != two:
            for three in primes:
                if one != three and two != three:
                    for four in primes:
                        if one != four and two != four and three != four:
                            for five in primes:
                                if one != five and two != five and three != five and four != five:
                                    count += 1
print(count)