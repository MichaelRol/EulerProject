
def gcd(a, b):
    gcd = 0
    for num in range(1, a+1):
        if a % num == 0 and b % num == 0:
            gcd = num
    return gcd 

nom = 1
den = 1
for x in range(10, 99):
    for y in range(10, 99):
        if x/y < 1.00:
            strx = str(x)
            stry = str(y)
            if strx[0] == stry[1] and float(strx[1])/float(stry[0]) == float(x)/float(y):
                nom *= x
                den *= y
            elif strx[1] == stry[0] and stry[1] != '0' and float(strx[0])/float(stry[1]) == float(x)/float(y):
                nom *= x
                den *= y
            elif strx[1] == stry[1] and strx[1] != '0' and float(strx[0])/float(stry[0]) == float(x)/float(y):
                nom *= x
                den *= y

print(den/gcd(nom, den))