import math

def match(n):
    strN = str(n)
    for x in range(0, 9):
        if strN[x*2] != str(x+1):
            return False
    return True

n = 138902663
for x in range(n, 0, -2):
    if match(x*x):
        print(x*10)
        break