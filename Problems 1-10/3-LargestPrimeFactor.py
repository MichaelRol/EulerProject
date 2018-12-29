import math

def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True

n = input("Enter a number: ")
i = 3
val = 0
while i <= n and n != 0:
    if n % i == 0:
        if isPrime(i):
            val = i
            n = n / i
    i = i + 2

print(val)


