def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

primeSums = [2]
for x in range(3, 1000000, 2):
    if x + primeSums[len(primeSums) - 1] > 1000000:
         break
    if isPrime(x):
        primeSums.append(x + primeSums[len(primeSums) - 1])

longestumVal = 0
longestSumLength = 0

for goal in range(len(primeSums) - 1, 0, -1):
    for start in range(0, goal):
        if goal - start > longestSumLength:
            if isPrime(primeSums[goal] - primeSums[start]):
                longestSumLength = goal - start
                longestumVal = primeSums[goal] - primeSums[start]
                break

print(longestumVal)


# def calcLongestSum(goal, longestSum):
#     for start in range(0, goal):
#         sum = 0
#         if goal - start < longestSum[0]:
#             break
#         for prime in range(start, goal - 1):
#             sum = sum + primeSums[prime]
#             if sum == primeSums[goal] and prime - start > longestSum[0]:
#                 longestSum[0] = prime - start
#                 longestSum[1] = sum
#                 return longestSum
#             if sum > primeSums[goal]:
#                 break
#     return 

# longestSum = [0, 0]
# for goal in range(len(primeSums) -1, 0, -1):
#     hold = calcLongestSum(goal, longestSum)
#     if hold[1] > longestSum[1]:
#         longestSum = hold
#         print(longestSum)

    
        