with open("./Day08/Day08_Input.txt",'r', encoding="utf-8") as file:
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

output = 1
places = [x for x in dict_defs if x[-1] == 'A']

for i, place in enumerate(places):
    runs = 0
    while places[i][-1] != 'Z':
        for move in moves:
            places[i] = dict_defs[places[i]][move]
        runs += 1
    output *= runs

print(len(moves) * output)
