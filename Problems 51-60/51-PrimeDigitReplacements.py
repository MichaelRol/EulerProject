import itertools

prime_cache = set()

def isPrime(x):
    if (x in prime_cache):
        return x
    if x < 2 :
        return False
    if x == 2:
        prime_cache.add(x)
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    prime_cache.add(x)
    return True

def findPrimeReplacementFamily(length):
    for num in range(99999, 9999999, 2):
        if isPrime(num):
            indices = range(len(str(num)))
            numstr = list(str(num))
            for num_indices_to_replace in indices[1:]:
                for indices_to_replace in itertools.combinations(indices, num_indices_to_replace):
                    curstr = numstr.copy()
                    primes = []
                    for x in range(0, 10):
                        for dig in indices_to_replace:
                            curstr[dig] = str(x)
                        constructed_num = int(''.join(curstr))
                        if isPrime(constructed_num) and len(str(num)) == len(str(constructed_num)):
                            primes += [constructed_num]
                        if len(primes) >= length:
                            return primes
                
print(findPrimeReplacementFamily(8))
            
