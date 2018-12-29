longestStart = 0
longestChainLength = 0
for starting in range(1000000, 13, -1):
    val = starting
    length = 0
    while val != 1:
        length = length + 1
        if val % 2 == 0:
            val = val * 0.5
        else:
            val = 3 * val + 1
        if length > longestChainLength:
            longestChainLength = length
            longestStart = starting
            continue
print(longestStart)