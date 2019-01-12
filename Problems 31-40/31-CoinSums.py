coins = [1, 2, 5, 10, 20, 50, 100, 200]
numOfWays = 0

waysToMake = [0] * 201
waysToMake[0] = 1

for i in range(0, len(coins)):
    for j in range(coins[i], 201):
        waysToMake[j] += waysToMake[j - coins[i]]
print(waysToMake[200])