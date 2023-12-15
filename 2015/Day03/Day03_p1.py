with open("./Day03/Day03_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read()

moves = {'^': (0, 1),
         '>': (1, 0),
         'v': (0, -1),
         '<': (-1, 0)
}

x, y = 0, 0
houses = {}

for char in file_parse:
    houses[(x, y)] = houses.get((x, y), 0) + 1
    x += moves[char][0]
    y += moves[char][1]
    houses[(x, y)] = houses.get((x, y), 0) + 1

print(len(houses))
