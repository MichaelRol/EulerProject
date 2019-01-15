import itertools

pans = list(itertools.permutations('1234567890'))

sum = 0 
for pan in pans:
    panstr = ''.join(pan)
    if pan[0] == '0':
        continue
    if int(panstr[3]) % 2 != 0:
        continue
    if int(panstr[5]) % 5 != 0:
        continue
    if int(panstr[2:5]) % 3 == 0 and int(panstr[4:7]) % 7 == 0 and int(panstr[5:8]) % 11 == 0 and int(panstr[6:9]) % 13 == 0 and int(panstr[7:10]) % 17 == 0:
        sum = sum + int(panstr)
print(sum)