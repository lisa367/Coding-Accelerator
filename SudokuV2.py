import sys
fichier = str(sys.argv[1])

grid = []
with open(fichier) as sudoku:
    lignes = sudoku.readlines()
    for line in lignes:
        grid.append(line)


lines = []
columns = []
for i in range(11):
    lines.append(grid[i])

for i in range(11):
    column = ""
    for line in lines:
        column += line[i]
    columns.append(column)


def grid_solver(x,y):
    for index in range(1,10):
        if lines[x].count(str(index)) == 0 and columns[y].count(str(index)) == 0:
            grid[x] = grid[x][:y] + str(index) + grid[x][y+1:]
            break
        else:
            continue
    #print(grid[x][y])

print("SOLUTION:\n")

for line in range(len(lines)):
    for column in range(len(columns)):
        if grid[line][column] == "_" :
            grid_solver(line,column)
        else:
            continue
    print(grid[line])    
