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
        for k in range(2, floor(num/2) + 1):
            if newSum.count(1) == k:
                newSumTuple = newSum[:len(newSum)-k] + (k,)
                if k != 2:
                    newSumTuple = tuple(sorted(newSumTuple, reverse=True))
                newSums.add(newSumTuple)
    newSums.add((num - 1, 1))
    return newSums

t0 = time.time()
sums = findSummations(100)
t1 = time.time()

print(t1-t0)
print(len(sums))