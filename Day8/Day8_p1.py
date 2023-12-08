with open("./Day8/Day8_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

moves = file_parse[0]
str_defs = file_parse[2:]
dict_defs = {}

for s in str_defs:
    element, left_right = s.split(' = ')
    left_right = left_right.strip('(').strip(')')
    left, right = left_right.split(', ')

    dict_defs[element] = {'L': left,
                          'R': right}

runs = 0
curr = 'AAA'

while curr != 'ZZZ':
    for move in moves:
        curr = dict_defs[curr][move]
    runs += 1


print(len(moves) * runs)
