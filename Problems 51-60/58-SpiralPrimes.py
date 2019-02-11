import sys

def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

prime = 0
total = 1
number = 1
add = 0
for loopNum in range(3, 100000, 2):
    add += 2
    for _ in range(0, 4):
        number = number + add
        if isPrime(number):
            prime += 1
        total +=1
    if float(prime)/float(total)< 0.1:
        print(loopNum)
        sys.exit()