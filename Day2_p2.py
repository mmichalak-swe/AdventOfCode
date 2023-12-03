output = 0


with open('./Day2_Input.txt','r', encoding="utf-8") as file:
    for line in file:
        game_power = 0
        game_turns = line.split(':')[1].split(';')
        minimums = {"red": float('-inf'),
                    "green": float('-inf'),
                    "blue": float('-inf')
        }

        for turn in game_turns:
            for text in turn.split(','):
                color_turn = text.strip(' ')
                num_color, color = int(color_turn.split()[0]), color_turn.split()[1]
                minimums[color] = max(minimums[color], num_color)
            
        power = 1
        for val in minimums.values():
            power *= val
        
        output += power

print(output)
