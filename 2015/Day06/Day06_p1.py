with open("./Day06/Day06_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

def change_state(d, start, end, action):
    start_row, end_row = start[0], end[0]
    start_col, end_col = start[1], end[1]

    for i in range (start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if action == 'toggle':
                d[(i, j)] = True if d[(i, j)] is False else False
            elif action == 'on':
                d[(i, j)] = True
            elif action == 'off':
                d[(i, j)] = False


lights = {}

for i in range(999):
    for j in range(999):
        lights[(i, j)] = False

for line in file_parse:
    instruction = line.split(' ')
    action = 'toggle' if instruction[0] == 'toggle' else ''
    if not action:
        action = 'on' if instruction[1] == 'on' else 'off'

    start_str = instruction[-3].split(',')
    end_str = instruction[-1].split(',')

    start = (int(start_str[0]), int(start_str[1]))
    end = (int(end_str[0]), int(end_str[1]))

    change_state(lights, start, end, action)

print(sum(lights.values()))
