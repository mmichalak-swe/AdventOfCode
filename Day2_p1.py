output = 0


with open('./Day2_Input.txt','r', encoding="utf-8") as file:

    color_limits = {"red": 12,
                    "green": 13,
                    "blue": 14
    }

    for line in file:
        game_id = ''

        for char in line:
            if char == ':':
                break
            elif char.isdigit():
                game_id += char

        game_id = int(game_id)
        game_turns = line.split(':')[1].split(';')

        stop = False
        for turn in game_turns:
            for text in turn.split(','):
                color_turn = text.strip(' ')
                num_color, color = int(color_turn.split()[0]), color_turn.split()[1]

                if num_color > color_limits[color]:
                    stop = True
                    break
            if stop:
                break

        if stop:
            stop = False
            continue
        else:
            output += game_id

print(output)
