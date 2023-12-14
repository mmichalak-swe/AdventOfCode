output = 0


with open('./Day02/Day02_Input.txt','r', encoding="utf-8") as file:

    color_limits = {"red": 12,
                    "green": 13,
                    "blue": 14
    }

    for line in file:
        game_id = int(line.split(": ")[0].split(" ")[1])
        game_turns = line.split(': ')[1].split('; ')
        valid = True
        for turn in game_turns:
            for color_turn in turn.split(', '):
                num_color, color = color_turn.strip().split(' ')
                num_color = int(num_color)

                if num_color > color_limits[color]:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            valid = True
            continue
        else:
            output += game_id

print(output)
