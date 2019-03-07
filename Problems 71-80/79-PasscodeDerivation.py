numbers = []
rightof = [[], [], [], [], [], [], [], [], [], []]
attempts = open("p079_keylog.txt", "r")
for attempt in attempts:
    for index in range(0, 3):
        if attempt[index] == "\n":
            continue
        if int(attempt[index]) not in numbers:
            numbers.append(int(attempt[index]))
        if index == 0:
            if int(attempt[1]) not in rightof[int(attempt[0])]:
                rightof[int(attempt[0])].append(int(attempt[1]))
            if int(attempt[2]) not in rightof[int(attempt[0])]:
                rightof[int(attempt[0])].append(int(attempt[2]))
        if index == 1:
            if int(attempt[2]) not in rightof[int(attempt[1])]:
                rightof[int(attempt[1])].append(int(attempt[2]))

keycode = [0] * len(numbers)

for number in numbers:
    keycode[len(rightof[number])] = number

keycode = keycode[::-1]
        

print(keycode)
