def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

val = 7
while(val < 6000):
    val += 2
    found = False
    if isPrime(val) != True:
        for x in range(2, val):
            if isPrime(x):
                isSq = (val - x)/2
                if(float(isSq) ** 0.5) % 1 == 0:
                    found = True
                    break
        if not found:
            break
        
                    
print(val)

