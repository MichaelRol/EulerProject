from math import floor
import time

def findSummations(num):
    if (num == 2):
        return {(1, 1) : 2}
    prevSums = findSummations(num-1)
    newSums = dict()
    for prevSum in prevSums:
        newSums[prevSum + (1,)] = prevSums[prevSum] + 1
    for newSum, sumLen in newSums.copy().items():
        for k in range(2, int(num/2) + 1):
            if sumLen > k and newSum[-k] == 1 and newSum[-(k+1)] != 1:
                newSumTuple = newSum[:sumLen-k] + (k,)
                if k != 2:
                    newSumTuple = tuple(sorted(newSumTuple, reverse=True))
                newSums[newSumTuple] = sumLen - k + 1
    newSums[(num - 1, 1)] = 2
    return newSums

t0 = time.time()
sums = findSummations(100)
t1 = time.time()

print(t1-t0)
print(len(sums))