def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for num in range(11, 99, 2):
    if isPrime(num):
        for dig in range(0, len(str(num))):
            numstr = list(str(num))
            primes = 0
            for x in range(0, 10):
                curstr = numstr
                curstr[dig] = str(x)
                if isPrime(int(''.join(curstr))):
                    primes += 1
            if primes >= 6:
                print(num)
            
            
            
