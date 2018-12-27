import math
def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2, int(math.ceil(x/2))):
        if x % i == 0:
            return False
    return True

sum = 2
for x in range (3, 2000000, 2):
    if isPrime(x):
        sum = sum + x

print(sum)