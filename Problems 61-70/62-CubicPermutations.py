import itertools

def genCubes(num):
    cubes = []
    for x in range(1, num+1):
        cubes.append(list(str(x**3)))
    return cubes

# cubes = genCubes(500)
for x in range(1000, 1100):
    cubed = x**3
    perms = list(itertools.permutations(str(cubed)))
    count = []
    # compare = 1
    # while (len(str(compare**3)) <= len(str(cubed))):
    #     if list(str(compare**3)) in perms:
    #         count.append(compare**3)
    #     compare += 1
    for perm in perms:
        strperm = "".join(perm)
        rooted = int(strperm)**(1.0/3)
        rooted = round(rooted)
        # if perm in cubes:
        #     count.append("".join(perm))
        if int(rooted**3) == int(strperm):
            if strperm not in count and perm[0] != "0":
                count.append(strperm)
    if len(count) == 5:
        print(x**3, count)
