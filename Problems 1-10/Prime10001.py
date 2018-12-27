primes = 0
prime = 0
x = 2
while primes < 10001:
    isPrime = True
    for i in range(2, x):
        if x % i == 0:
            isPrime = False
    if isPrime:
        prime = x
        primes = primes + 1
    x = x + 1

print(prime)
