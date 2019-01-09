products = []

for x in range(0, 987):
    for y in range(0, 9876):
        prod = x * y
        string = str(prod) + str(x) + str(y)
        if len(string) == 9:
            if '1' in string and '2' in string and '3' in string and '4' in string and '5' in string \
                and '6' in string and '7' in string and '8' in string and '9' in string and prod not in products:
                products.append(prod)
                print(prod, x, y)

total = 0
for prod in products:
    total += prod
    print(prod)

print(total)
        