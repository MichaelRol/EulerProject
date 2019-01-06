import math

count = 0
num = 2 ** 1000
digits = math.ceil(math.log(num, 10))

for x in range (0, int(digits)):
    count = count + ((num % (10 ** (x + 1)) - num % 10 ** x)/10 ** x)
print(count)