divisors = [2, 3, 5, 7, 11, 13, 17]
sum = 0

def isPandigital(val):
    string = str(val)
    if '1' in string and '2' in string and '3' in string and '4' in string and '5' in string \
        and '6' in string and '7' in string and '8' in string and '9' in string:
        return True
    return False


for x in range(123456789, 398765421):
    if isPandigital(x):
        print(x)
        if int(str(x)[3]) % 2 != 0:
            break
        if int(str(x)[5]) % 5 != 0:
            break
        if int(str(x)[2:5]) % 3 == 0 and int(str(x)[4:7]) % 7 == 0 and int(str(x)[5:8]) % 11 == 0 and int(str(x)[6:9]) % 13 == 0 and int(str(x)[7:10]) % 17 == 0:
            sum = sum + x

print(sum)