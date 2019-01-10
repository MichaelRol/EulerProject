def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def leftTrunc(num):
    for _ in range(0, len(str(num)) - 1):
        num = int(str(num)[1:])
        if isPrime(num) == False:
            return False
    return True

def rightTrunc(num):
    for _ in range(0, len(str(num)) - 1):
        num = int(str(num)[:-1])
        if isPrime(num) == False:
            return False
    return True

prime = 11
trunc = []

while(len(trunc) < 11):
    if isPrime(prime) and rightTrunc(prime) and leftTrunc(prime):
        trunc.append(prime)
    prime = prime + 2

sum = 0

for val in trunc:
    sum += val

print(sum)