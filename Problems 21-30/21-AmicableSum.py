
def d(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
             sum = sum + x
    return(sum)

total = 0
for a in range(1, 10001):
    b = d(a)
    if d(a) == b and d(b) == a and a != b and b != 1 and b < 10000:
        print(a, b)
        total = total + a
    
print(total)