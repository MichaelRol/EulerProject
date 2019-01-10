def decToBin(num):
    return int(bin(num)[2:])

def isPalin(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

sum = 0
for num in range(1, 1000000):
    if isPalin(num) and isPalin(decToBin(num)):
        sum = sum + num

print(sum)