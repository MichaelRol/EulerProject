count = 0
newden = 2
oldden = 1
newnom = 3
oldnom = 1
for x in range(0, 1000):
    holdden = newden
    newden = newden * 2 + oldden
    oldden = holdden
    holdnom = newnom
    newnom = newnom * 2 + oldnom
    oldnom = holdnom
    if len(str(newnom)) > len(str(newden)):
        count += 1
print(count)