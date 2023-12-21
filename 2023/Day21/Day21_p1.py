from collections import deque

with open("./Day21/Day21_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

garden = [[x for x in line] for line in file_parse]
ROWS, COLS = len(garden), len(garden[0])
plots = deque()
locations = set()

DIRECTIONS = {'RIGHT': (0, 1),
              'DOWN': (1, 0),
              'LEFT': (0, -1),
              'UP': (-1, 0)
              }

def helper(plots, x, y):
    if not 0 <= x < ROWS or not 0 <= y < COLS:
        return
    char = garden[x][y]
    if char == '#':
        return None
    if char == '.':
        return (x, y)


for row in range(ROWS):
    for col in range(COLS):
        if garden[row][col] == 'S':
            plots.append((row, col))
            locations.add((row, col))
            garden[row][col] = '.'
            break

steps = 64

for _ in range(steps):
    for i in range(len(plots)):
        x, y = plots.popleft()
        for dx, dy in DIRECTIONS.values():
            potential_plot = helper(plots, x + dx, y + dy)
            if potential_plot and potential_plot not in locations:
                locations.add(potential_plot)
                plots.append(potential_plot)
    locations = set(plots)

print(len(plots))
