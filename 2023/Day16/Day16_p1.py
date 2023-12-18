from sys import setrecursionlimit

setrecursionlimit(3000)

with open("./Day16/Day16_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

grid = [[char for char in line] for line in file_parse]
ROWS = len(grid)
COLS = len(grid[0])

energized = [[0 for j in range(COLS)] for i in range(ROWS)]

moves = {'RIGHT': (0, 1),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'UP': (-1, 0)
            }

def move(heading):
    return moves[heading]


def turn(heading, char):
    if char == '.':
        return heading
    elif char == '/':
        if heading == 'DOWN':
            return 'LEFT'
        elif heading == 'LEFT':
            return 'DOWN'
        elif heading == 'RIGHT':
            return 'UP'
        elif heading == 'UP':
            return 'RIGHT'
    elif char == '\\':
        if heading == 'UP':
            return 'LEFT'
        elif heading == 'LEFT':
            return 'UP'
        elif heading == 'DOWN':
            return 'RIGHT'
        elif heading == 'RIGHT':
            return 'DOWN'
    elif char == '|':
        if heading in ['UP', 'DOWN']:
            return heading
    elif char == '-':
        if heading in ['LEFT', 'RIGHT']:
            return heading


def recursive_beams(grid, row, col, heading):
    if not 0 <= row < ROWS or not 0 <= col < COLS:
        return

    curr_char = grid[row][col]

    if curr_char in ['-', '|'] and energized[row][col] == 1:
        return

    energized[row][col] = 1

    if curr_char == '|':
        if heading in ['LEFT', 'RIGHT']:
            recursive_beams(grid, row + moves['UP'][0], col + moves['UP'][1], 'UP')
            recursive_beams(grid, row + moves['DOWN'][0], col + moves['DOWN'][1], 'DOWN')
        else:
            new_heading = turn(heading, curr_char)
            recursive_beams(grid, row + moves[heading][0], col + moves[heading][1], new_heading)
    elif curr_char == '-':
        if heading in ['UP', 'DOWN']:
            recursive_beams(grid, row + moves['LEFT'][0], col + moves['LEFT'][1], 'LEFT')
            recursive_beams(grid, row + moves['RIGHT'][0], col + moves['RIGHT'][1], 'RIGHT')
        else:
            new_heading = turn(heading, curr_char)
            recursive_beams(grid, row + moves[new_heading][0], col + moves[new_heading][1], new_heading)
    elif curr_char == '.':
        new_heading = turn(heading, curr_char)
        recursive_beams(grid, row + moves[new_heading][0], col + moves[new_heading][1], new_heading)
    elif curr_char == '/':
        new_heading = turn(heading, curr_char)
        recursive_beams(grid, row + moves[new_heading][0], col + moves[new_heading][1], new_heading)
    elif curr_char == '\\':
        new_heading = turn(heading, curr_char)
        recursive_beams(grid, row +moves[new_heading][0], col + moves[new_heading][1], new_heading)


recursive_beams(grid, 0, 0, 'RIGHT')
print(sum([sum(row) for row in energized]))
