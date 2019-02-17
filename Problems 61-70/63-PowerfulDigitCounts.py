count = 0

for x in range(1, 100):
    y = 1
    while len(str(y**x)) <= x:
        if len(str(y**x)) == x:
            count += 1
        y += 1

print(count)