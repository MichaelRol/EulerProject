def isPalin(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

def isLycrel(number):
    num = number
    for _ in range(0, 50):
        if isPalin(int(str(num)) + int(str(num)[::-1])):
            return True
        num = int(str(num)) + int(str(num)[::-1])
    return False
        
count = 0
for x in range(1, 10001):
    if not isLycrel(x):
        count += 1


print(count)