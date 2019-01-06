import math

val = input("Calculate factorial: ")

def factorial(num):
    val = 1
    for x in range(1, num + 1):
        val = val * x
    return val

count = 0
num = factorial(val)
digits = math.ceil(math.log(num, 10))

for x in range (0, int(digits)):
    count = count + ((num % (10 ** (x + 1)) - num % 10 ** x)/10 ** x)

print(count)