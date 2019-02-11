def digitalSum(num):
    sum = 0
    for x in range(0, len(str(num))):
        sum = sum + int(str(num)[x])
    return sum

largest = 0
for a in range(1, 100):
    for b in range(1, 100):
        test = digitalSum(a**b)
        if test > largest:
            largest = test

print(largest)