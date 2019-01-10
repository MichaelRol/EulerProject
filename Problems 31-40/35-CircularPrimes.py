def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def hasEvenDigit(num):
    hasEven = False
    for dig in str(num):
        if int(dig) % 2 == 0:
            hasEven = True
            break
    return hasEven

count = 4
for num in range(11, 1000000, 2):
    allRotPrime = True
    x = num
    if isPrime(x) and hasEvenDigit(x) == False:
        for rep in range(len(str(x))-1):
            strx = str(x)
            hold = strx[len(strx) - 1]
            newx = hold + strx[:-1]
            x = int(newx)
            if isPrime(int(newx)) != True:
                allRotPrime = False
    else:
        allRotPrime = False
    if allRotPrime:
        count += 1
    

print(count)