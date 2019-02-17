array = []

file = open("p067_triangle.txt", "r")
for line in file:
    rowstring = line.replace("\n", "")
    rowstring = line.split(" ")
    row = []
    for val in rowstring:
        row.append(int(val))

    array.append(row)

print(array)