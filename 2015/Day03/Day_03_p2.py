def make_delivery(homes, x, y):
    homes[(x, y)] = homes.get((x, y), 0) + 1


with open("./Day03/Day03_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read()

moves = {'^': (0, 1),
         '>': (1, 0),
         'v': (0, -1),
         '<': (-1, 0)
}

santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
homes = {}
delivery_person = 's'

for char in file_parse:
    if delivery_person == 's':
        make_delivery(homes, santa_x, santa_y)
        santa_x += moves[char][0]
        santa_y += moves[char][1]
        make_delivery(homes, santa_x, santa_y)
    else:
        make_delivery(homes, robo_x, robo_y)
        robo_x += moves[char][0]
        robo_y += moves[char][1]
        make_delivery(homes, robo_x, robo_y)

    delivery_person = 'r' if delivery_person == 's' else 's'

print(len(homes))
