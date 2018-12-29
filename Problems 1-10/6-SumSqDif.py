sumOfSq = 0
sqOfSum = 0

for x in range(1, 101):
    sqOfSum = sqOfSum + x
    sumOfSq = sumOfSq + x * x
print(sqOfSum)
sqOfSum = sqOfSum * sqOfSum
print(sqOfSum)
print(sumOfSq)
result = sumOfSq - sqOfSum
print(result)