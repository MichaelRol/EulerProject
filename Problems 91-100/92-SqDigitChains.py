import itertools
import math


def multinomcoef(number):
    numDigits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(number)):
        numDigits[number[i]] += 1

    result = math.factorial(len(number))
    for i in range(0, len(numDigits)):
        result /= math.factorial(numDigits[i])
    return result

nums = list(itertools.combinations_with_replacement("0123456789", 7))
count = 0
numbers = 0
for x in nums:
    sum = int(''.join(x))
    if sum == 0:
        continue
    while(1):
        digits = [int(d) for d in str(sum)]
        sum = 0
        for num in digits:
            sum += num*num
        if sum == 89:
            toSend = [int(d) for d in x]
            count += multinomcoef(toSend)
            numbers += 1
            break
        if sum == 1:
            break
print(count)

#TRY LIST OF COMBINATIONS