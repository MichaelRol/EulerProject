grid = [[1 for i in range(21)] for j in range(21)]

for x in range(19, -1, -1):
    for y in range(19, -1, -1):
        grid[x][y] = grid[x+1][y] + grid[x][y+1]

print(grid[0][0])