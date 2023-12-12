from math import floor
import time

def findSummations(num):
    if (num == 2):
        return set([(1, 1)])
    prevSums = findSummations(num-1)
    newSums = set()
    for prevSum in prevSums:
        newSums.add(prevSum + (1,))
    for newSum in newSums.copy():
        for k in range(2, int(num/2) + 1):
            sumLen = len(newSum)
            if sumLen > k and newSum[-k] == 1 and newSum[-(k+1)] != 1:
                newSumTuple = newSum[:sumLen-k] + (k,)
                if k != 2:
                    newSumTuple = tuple(sorted(newSumTuple, reverse=True))
                if newSumTuple not in newSums:
                   newSums.add(newSumTuple)
    if (num - 1, 1) not in newSums:
        newSums.add((num - 1, 1))
    return newSums

t0 = time.time()
sums = findSummations(70)
t1 = time.time()

print(t1-t0)
print(len(sums))