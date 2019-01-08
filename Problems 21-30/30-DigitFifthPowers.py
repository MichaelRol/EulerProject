total = 0
for x in range(10, 200000):
    sum = 0
    for dig in str(x):
        sum = sum + int(dig)**5
    if x == sum:
        total += x

print(total)