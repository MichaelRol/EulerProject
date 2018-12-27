import math
def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    prime = True
    for i in range(2, int(math.ceil(x/2))):
        if x % i == 0:
            prime = False

    return prime

sum = 0
for x in range (2, 2000000):
    if isPrime(x):
        sum = sum + x

print(sum)