coins = [1, 2, 5, 10, 20, 50, 100, 200]
numOfWays = 0

for coin in coins:
    if 200 % coin == 0:
        numOfWays += 1



print(numOfWays)