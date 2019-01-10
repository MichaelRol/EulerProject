
largest = 0

for val in range(1, 100000):
    for mult in range(2, 10):
        string = ""
        for x in range(0, mult):
            string = string + str(val * (x + 1))
        if len(string) == 9:
            if '1' in string and '2' in string and '3' in string and '4' in string and '5' in string \
                and '6' in string and '7' in string and '8' in string and '9' in string and int(string) > largest:
                largest = int(string)

print(largest)