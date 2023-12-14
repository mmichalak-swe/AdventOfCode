def horizontal_symmetry(grid, start_row, max_rows, max_cols, iter=1, score=0):
    if score > 1:
        return score

    low_row = start_row - iter + 1
    high_row = start_row + iter

    if not 0 <= low_row < max_rows or not 0 <= high_row < max_rows:
        return score

    score += sum(grid[low_row][col] != grid[high_row][col] for col in range(max_cols))

    return horizontal_symmetry(grid, start_row, max_rows, max_cols, iter+1, score)


def vertical_symmetry(grid, start_col, max_rows, max_cols, iter=1, score=0):
    if score > 1:
        return score

    low_col = start_col - iter + 1
    high_col = start_col + iter

    if not 0 <= low_col < max_cols or not 0 <= high_col < max_cols:
        return score

    score += sum(grid[row][low_col] != grid[row][high_col] for row in range(max_rows))

    return vertical_symmetry(grid, start_col, max_rows, max_cols, iter+1, score)


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
        if horizontal_symmetry(grid, row, max_rows, max_cols) == 1:
            row_output += 100 * (row + 1)
            break

    for col in range(max_cols - 1):
        if vertical_symmetry(grid, col, max_rows, max_cols) == 1:
            col_output += col + 1
            break

    output += row_output + col_output

print(output)
