grid = []

file = open("p067_triangle.txt", "r")
for line in file:
    rowstring = line.replace("\n", "")
    rowstring = line.split(" ")
    row = []
    for val in rowstring:
        row.append(int(val))
    grid.append(row)

for layer in range(98, -1, -1):
    for val in range(0, layer + 1):
        grid[layer][val] = grid[layer][val] + max(grid[layer + 1][val], grid[layer + 1][val + 1])
        
print(grid[0][0])