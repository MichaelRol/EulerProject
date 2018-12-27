i = 1
while(True):
    all = True
    for x in range(1, 21):
        if i % x != 0:
            all = False
            i = i + 1
    if all:
        print(i)
        break