with open("./Day11/Day11_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')
    grid = [list(line) for line in file_parse]

max_rows = len(grid)
max_cols = len(grid[0])

double_rows = set()
for row in range(max_rows):
    if all(i == '.' for i in grid[row]):
        double_rows.add(row)

double_cols = set()
for col in range(max_cols):
    check = True
    for row in range(max_rows):
        if grid[row][col] != '.':
            check = False
    if check:
        double_cols.add(col)

galaxies = []
for row in range(max_rows):
    for col in range(max_cols):
        if grid[row][col] == '#':
            galaxies.append((row, col))

output = 0
for i, start_galaxy in enumerate(galaxies):
    start_galaxy_row, start_galaxy_col = start_galaxy
    for j in range(i + 1, len(galaxies)):
        end_galaxy_row, end_galaxy_col = galaxies[j]

        rows_between = abs(end_galaxy_row - start_galaxy_row)
        cols_between = abs(end_galaxy_col - start_galaxy_col)

        lower_row = start_galaxy_row if start_galaxy_row < end_galaxy_row else end_galaxy_row
        lower_col = start_galaxy_col if start_galaxy_col < end_galaxy_col else end_galaxy_col
        higher_row = end_galaxy_row if end_galaxy_row > start_galaxy_row else start_galaxy_row
        higher_col = end_galaxy_col if end_galaxy_col > start_galaxy_col else start_galaxy_col

        for extra_row in range(lower_row + 1, higher_row):
            if extra_row in double_rows:
                rows_between += 999999

        for extra_col in range(lower_col + 1, higher_col):
            if extra_col in double_cols:
                cols_between += 999999

        output += rows_between + cols_between

print(output)
