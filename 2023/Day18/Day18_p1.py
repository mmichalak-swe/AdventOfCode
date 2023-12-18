from sys import setrecursionlimit

setrecursionlimit(50000)

with open("./Day18/Day18_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

dig_plan = [x.split(' ') for x in file_parse]

moves = {'R': (0, 1),
         'D': (1, 0),
         'L': (0, -1),
         'U': (-1, 0)
        }

def calc_grid(dig_plan):
    curr_x, curr_y = 0, 0
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for dig in dig_plan:
        direction, steps, color = dig
        for i in range(int(steps)):
            curr_x += moves[direction][0]
            curr_y += moves[direction][1]

            min_x = min(min_x, curr_x)
            max_x = max(max_x, curr_x)
            min_y = min(min_y, curr_y)
            max_y = max(max_y, curr_y)

    return min_x, max_x, min_y, max_y


min_x, max_x, min_y, max_y = calc_grid(dig_plan)
x_range = max_x - min_x
y_range = max_y - min_y

grid = [['.' for i in range(y_range + 1)] for j in range(x_range + 1)]
ROWS = len(grid)
COLS = len(grid[0])

x = abs(min_x)
y = abs(min_y)

for dig in dig_plan:
    direction, steps, color = dig
    for i in range(int(steps)):
        x += moves[direction][0]
        y += moves[direction][1]
        grid[x][y] = '#'


def floodfill(row, col, boundary='#'):
    if not 0 <= row < ROWS or not 0 <= col < COLS:
        return

    char = grid[row][col]
    if char == boundary:
        return

    grid[row][col] = boundary
    for dx, dy in moves.values():
        floodfill(row + dx, col + dy)


floodfill(18, 187) # random point within the lagoon
print(sum([row.count('#') for row in grid]))
