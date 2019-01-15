import itertools

pans = list(itertools.permutations('1234567890'))

for pan in range(0, len(pans)):
    pans[pan] = ''.join(pans[pan])
    
pans = sorted(pans)
    

print(pans[999999])