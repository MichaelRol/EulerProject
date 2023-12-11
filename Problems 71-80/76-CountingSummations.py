from math import floor


def findSummations(num):
    if (num == 2):
        return [[1, 1]]
    prevSums = findSummations(num-1)
    newSums = []
    for prevSum in prevSums:
        newSums.append(prevSum + [1])
    for newSum in newSums:
        for k in range(2, floor(num/2) + 1):
            allEndInone = True
            for x in range(2, k + 1):
                allEndInone = allEndInone and newSum[-x] == 1
            if allEndInone:
                sumCopy = newSum.copy()
                for _ in range(k):
                    sumCopy.remove(1)
                sumCopy.append(k)
                sumCopy.sort(reverse=True)
                if sumCopy not in newSums:
                    newSums.append(sumCopy)
    if [num - 1, 1] not in newSums:
        newSums.append([num - 1, 1])
    return newSums

sums = findSummations(37)
print(sums)
print(len(sums))