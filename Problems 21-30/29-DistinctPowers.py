powers = []

for a in range(2, 101):
    for b in range(2, 101):
        val = a**b
        if val not in powers:
            powers.append(val)

print(len(powers))
