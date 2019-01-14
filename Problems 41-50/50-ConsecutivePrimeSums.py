def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True

primes = [2]
for x in range(3, 1000000, 2):
    if isPrime(x):
        primes.append(x)

longestSumLength = 0
longestSumVal = 0
for goal in range(0, len(primes) - 1 -1):
    for start in range(0, goal):
        sum = 0
        for prime in range(start, goal - 1):
            sum = sum + primes[prime]
            if sum == primes[goal] and prime - start > longestSumLength:
                longestSumLength = prime - start
                longestSumVal = sum

print(longestSumVal)
        