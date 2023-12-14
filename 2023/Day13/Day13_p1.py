def horizontal_symmetry(grid, start_row, max_rows, iter=1):
    low_row = start_row - iter + 1
    high_row = start_row + iter

    if not 0 <= low_row < max_rows or not 0 <= high_row < max_rows:
        return True

    if grid[low_row] != grid[high_row]:
        return False

    return horizontal_symmetry(grid, start_row, max_rows, iter+1)


def col_builder(grid, col, max_rows):
    return [grid[row][col] for row in range(max_rows)]


def vertical_symmetry(grid, start_col, max_rows, max_cols, iter=1):
    low_col = start_col - iter + 1
    high_col = start_col + iter

    if not 0 <= low_col < max_cols or not 0 <= high_col < max_cols:
        return True

    if col_builder(grid, low_col, max_rows) != col_builder(grid, high_col, max_rows):
        return False

    return vertical_symmetry(grid, start_col, max_rows, max_cols, iter+1)


with open("./Day13/Day13_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n\n')

grids = [[[char for char in x] for x in y.split()] for y in file_parse]

output = 0
for grid in grids:
    max_rows = len(grid)
    max_cols = len(grid[0])
    row_output = 0
    col_output = 0

    for row in range(max_rows - 1):
        if horizontal_symmetry(grid, row, max_rows):
            row_output += 100 * (row + 1)

    for col in range(max_cols - 1):
        if vertical_symmetry(grid, col, max_rows, max_cols):
            col_output += col + 1

    output += row_output + col_output

print(output)
