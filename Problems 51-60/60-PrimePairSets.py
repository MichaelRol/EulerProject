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

lowest = 1000000000000
primes = genPrimes(150)
for one in primes:
    for two in primes:
        if one != two and isPrime(int(str(one) + str(two))) and isPrime(int(str(two) + str(one))):
            for three in primes:
                if one != three and two != three and isPrime(int(str(one) + str(three))) and isPrime(int(str(two) + str(three)))\
                    and isPrime(int(str(three) + str(one))) and isPrime(int(str(three) + str(two))):
                    for four in primes:
                        if one != four and two != four and three != four and two != three and isPrime(int(str(one) + str(four))) and isPrime(int(str(two) + str(four)))\
                            and isPrime(int(str(four) + str(one))) and isPrime(int(str(four) + str(two))) and isPrime(int(str(four) + str(three))) and isPrime(int(str(three) + str(four))):
                            if one + two + three + four < lowest:
                                lowest = one + two + three + four
                            # for five in primes:
                            #     if one != five and two != five and three != five and four != five:
                            #         count += 1
print(lowest)