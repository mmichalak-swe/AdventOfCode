def swap(grid, r1, c1, r2, c2):
    grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]


def tilt(grid, row, col, ROWS, COLS, direction):
    next_row = row + direction[0]
    next_col = col + direction[1]
    while 0 <= next_row < ROWS and 0 <= next_col < COLS:
        next_char = grid[next_row][next_col]
        if next_char in {'#', 'O'}:
            break
        else:
            swap(grid, row, col, next_row, next_col)
            row += direction[0]
            col += direction[1]
            next_row += direction[0]
            next_col += direction[1]


def score(grid, ROWS, COLS):
    total = 0
    points = ROWS
    for row in range(ROWS):
        for col in range(COLS):
            char = grid[row][col]
            if char == 'O':
                total += points
        points -= 1
    return total


with open("./Day14/Day14_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

grid = [[char for char in line] for line in file_parse]
ROWS = len(grid)
COLS = len(grid[0])

for row in range(ROWS):
    for col in range(COLS):
        char = grid[row][col]
        if char == 'O':
            tilt(grid, row, col, ROWS, COLS, (-1, 0))

output = score(grid, ROWS, COLS)
print(output)
