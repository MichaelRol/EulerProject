def isPrime(x):
    if x < 2 :
        return False
    if x == 2:
        return True
    for i in range(3,int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

def isPandigital(val):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in range(0, len(str(val))):
        if digits[x] not in str(val):
            return False
    return True

largest = 0
for x in range(1234567, 7654322, 2):
    if isPandigital(x): 
            if isPrime(x) and x > largest:
                largest = x

print(largest)