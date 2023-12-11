from collections import deque
import numbers


with open("./Day10/Day10_Input.txt",'r', encoding="utf-8") as file:
# with open("./Day10/Day10_Input_test.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')
    grid = [list(line) for line in file_parse]

max_rows = len(grid)
max_cols = len(grid[0])

looking = {'UP': {'|': 'UP', 'F': 'RIGHT', '7': 'LEFT'},
           'RIGHT': {'-': 'RIGHT', 'J': 'UP', '7': 'DOWN'},
           'DOWN': {'|': 'DOWN', 'L': 'RIGHT', 'J': 'LEFT'},
           'LEFT': {'-': 'LEFT', 'L': 'UP', 'F': 'DOWN'}
           }

moves = {'UP': (-1, 0),
        'RIGHT': (0, 1),
        'DOWN': (1, 0),
        'LEFT': (0, -1)
        }

locations = deque()
stop = False
step_num = 0
for row, line in enumerate(grid):
    for col, char in enumerate(line):
        if char == 'S':
            for direction, deltas in moves.items():
                dx, dy = deltas
                new_row, new_col = row + dx, col + dy

                if not 0 <= new_row < max_rows or not 0 <= new_col < max_cols:
                    continue

                new_char = grid[new_row][new_col]

                if new_char in looking[direction]:
                    locations.append((direction, new_row, new_col))
            grid[row][col] = step_num
            stop = True
            break
    if stop:
        break

step_num += 1
stop = False

while locations:
    for x in range(len(locations)):
        heading, row, col = locations.popleft()
        curr_value = grid[row][col]
        if isinstance(curr_value, numbers.Number):
            stop = True
            break

        new_heading = looking[heading][curr_value]
        dx, dy = moves[new_heading]
        new_row, new_col = row + dx, col + dy

        if not 0 <= new_row < max_rows or not 0 <= new_col < max_cols:
            continue

        new_char = grid[new_row][new_col]
        locations.append((new_heading, new_row, new_col))

        grid[row][col] = step_num
    if stop:
        grid[row][col] = step_num
        break
    step_num += 1

print(step_num)
