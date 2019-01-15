def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

primes = []
for x in range(1001, 10000, 2):
    if isPrime(x):
        primes.append(x)

def arePerms(val, add):
    strval = str(val)
    strval1 = str(val + x)
    strval2 = str(val + 2*x)

    for dig in range(0, len(strval)-1):
        if strval[dig] in strval1 and strval[dig] in strval2:
            strval1 = strval1.replace(strval[dig], '')
            strval2 = strval2.replace(strval[dig], '')
        else:
            return False
    if strval1 == '':            
        return True
    return False

for prime in primes:
    for x in range(1, 10000):
        if prime + x*2 > 10000:
            break
        if arePerms(prime, x):
            if isPrime(prime + x) and isPrime(prime + 2*x):
                print(str(prime)+str(prime+x)+str(prime+2*x)) 
