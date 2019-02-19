import itertools

for x in range(0, 1000):
    cubed = x**3
    perms = list(itertools.permutations(str(cubed)))
    count = []
    for perm in perms:
        rooted = int("".join(perm))**(1.0/3)
        rooted = round(rooted)
        if int(rooted**3) == int("".join(perm)):
            if "".join(perm) not in count and perm[0] != "0":
                count.append("".join(perm))
    if len(count) == 4:
        print(x**3, count)
