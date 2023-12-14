from copy import deepcopy


def swap(grid, r1, c1, r2, c2):
    grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]


def rotate_cw(grid):
    return [list(r) for r in list(zip(*grid[::-1]))]


def tilt(grid, ROWS, COLS, direction):
    for row in range(ROWS):
        for col in range(COLS):
            char = grid[row][col]
            if char == 'O':
                curr_row = row
                curr_col = col
                next_row = row + direction[0]
                next_col = col + direction[1]
                while 0 <= next_row < ROWS and 0 <= next_col < COLS:
                    next_char = grid[next_row][next_col]
                    if next_char in {'#', 'O'}:
                        break
                    else:
                        swap(grid, curr_row, curr_col, next_row, next_col)
                        curr_row += direction[0]
                        curr_col += direction[1]
                        next_row += direction[0]
                        next_col += direction[1]


def score(grid, ROWS, COLS):
    total = 0
    points = ROWS
    for row in range(ROWS):
        num_chars = ''.join(grid[row]).count('O')
        total += points * num_chars
        points -= 1
    return total


with open("./Day14/Day14_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

grid = [[char for char in line] for line in file_parse]
ROWS = len(grid)
COLS = len(grid[0])
GRIDS = []
grid_num = 0

for cycle in range (1000000000):
    for _ in range(4):
        tilt(grid, ROWS, COLS, (-1, 0))
        grid = rotate_cw(grid)
    if grid not in GRIDS:
        GRIDS.append(deepcopy(grid))
        continue
    ind = GRIDS.index(grid)
    cycle_length = cycle - ind
    remaining = 999999999 - cycle
    offset = remaining % cycle_length
    grid_num = ind + offset
    break

output = score(GRIDS[grid_num], ROWS, COLS)
print(output)
