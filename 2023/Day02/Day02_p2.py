output = 0


with open('./Day02/Day02_Input.txt','r', encoding="utf-8") as file:
    for line in file:
        game_power = 0
        game_turns = line.split(': ')[1].split('; ')
        minimums = {"red": float('-inf'),
                    "green": float('-inf'),
                    "blue": float('-inf')
        }

        for turn in game_turns:
            for color_turn in turn.strip().split(', '):
                num_color, color = color_turn.split(' ')
                num_color = int(num_color)
                minimums[color] = max(minimums[color], num_color)

        power = 1
        for val in minimums.values():
            power *= val

        output += power

print(output)
