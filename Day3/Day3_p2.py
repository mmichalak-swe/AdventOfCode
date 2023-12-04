from math import prod
output = 0


with open("./Day3_Input.txt",'r', encoding="utf-8") as file:
    grid = [list(line.strip()) for line in file]

    maxRow = len(grid)
    maxCol = len(grid[0])

    def num_builder(row, col, direction, num_str=''):
        if not 0 <= row < maxRow or not 0 <= col < maxCol:
            return num_str

        s = grid[row][col]

        if not s.isdigit():
            return num_str

        if direction == -1:
            num_str = s + num_str
        else:
            num_str += s

        grid[row][col] = 'X'

        return num_builder(row, col + direction, direction, num_str)


    for i in range(maxRow):
        for j in range(maxCol):

            char = grid[i][j]
            if char == '.' or char.isdigit():
                continue

            nums_found = []

            for idx in range(-1, 2):
                for jdx in range(-1, 2):
                    if idx == 0 and jdx == 0:
                        continue
                    new_row = i + idx
                    new_col = j + jdx
                    if 0 <= new_row < maxRow and 0 <= new_col < maxCol and grid[new_row][new_col].isdigit():
                        num_left = num_builder(new_row, new_col-1, -1)
                        num_right = num_builder(new_row, new_col+1, 1)
                        num_found = int(num_left + grid[new_row][new_col] + num_right)
                        nums_found.append(num_found)
                        grid[new_row][new_col] = 'X'

            if len(nums_found) == 2:
                output += prod(nums_found)

print(output)
