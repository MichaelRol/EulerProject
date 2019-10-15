count = 0
for x in range(2, 10000000):
    sum = x
    while(1):
        digits = [int(d) for d in str(sum)]
        sum = 0
        for num in digits:
            sum += num*num
        y = sum
        if sum == 89:
            count += 1
            break
        if sum == 1:
            break
print(count)