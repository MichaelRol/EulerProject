import numpy as np

abu = []
perf = [6, 28, 496, 8128]
def d(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
             sum = sum + x
    return(sum)

for x in range(1, 28124): 
    if d(x) > x:
        abu.append(x)

numbersThatCanBe = np.zeros((28124), dtype=bool)
for num1 in range(0, len(abu)):
    for num2 in range(num1, len(abu)):
        if abu[num1] + abu[num2] <= 28123:
            #print(abu[num1] + abu[num2])
            numbersThatCanBe[abu[num1] + abu[num2]] = True
        else:
            break
sum = 0

for i in range(1, 28124):
    if numbersThatCanBe[i] == False:
        sum = sum + i
    

print(sum)