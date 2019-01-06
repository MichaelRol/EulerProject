def nameScore(name):
    score = 0
    for x in name:
        if x == "A":
            score += 1
        elif x == "B":
            score += 2
        elif x == "C":
            score += 3
        elif x == "D":
            score += 4
        elif x == "E":
            score += 5
        elif x == "F":
            score += 6
        elif x == "G":
            score += 7
        elif x == "H":
            score += 8
        elif x == "I":
            score += 9
        elif x == "J":
            score += 10
        elif x == "K":
            score += 11
        elif x == "L":
            score += 12
        elif x == "M":
            score += 13
        elif x == "N":
            score += 14
        elif x == "O":
            score += 15
        elif x == "P":
            score += 16
        elif x == "Q":
            score += 17
        elif x == "R":
            score += 18
        elif x == "S":
            score += 19
        elif x == "T":
            score += 20
        elif x == "U":
            score += 21
        elif x == "V":
            score += 22
        elif x == "W":
            score += 23
        elif x == "X":
            score += 24
        elif x == "Y":
            score += 25
        elif x == "Z":
            score += 26
    return score

with open("22_names.txt", "r") as file:
    data = file.readlines()

for line in data:
    names = line.split("\",\"")
names[0] = names[0][1:]
names[len(names)-1] = names[len(names)-1][:-1]

sorted = []
for new in range(0, len(names)):
    sorted.append(names[new])
    for x in range(len(sorted) - 1, 0, -1):
        if sorted[x] < sorted[x-1]:
            swap = sorted[x]
            sorted[x] = sorted[x-1]
            sorted[x-1] = swap

total = 0    
for x in range(0, len(sorted)):
    total = total + ((x + 1) * nameScore(sorted[x]))

print(total)