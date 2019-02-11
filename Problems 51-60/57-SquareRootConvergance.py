count = 0
newden = 3
oldden = 1
for x in range(0, 1000):
    # number =
    hold = newden
    newden = newden * 2 + oldden
    oldden = hold
    print(newden, oldden)
    # # denom = 
    # if len(str(num)) > len(str(den)):
    #     count += 1