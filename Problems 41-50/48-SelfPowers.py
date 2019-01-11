total = 0

for x in range(1, 1001):
    total += x**x

string = str(total)
print(string[len(string)-10:])