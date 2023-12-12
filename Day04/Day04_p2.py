table = {}


with open("./Day04/Day04_Input.txt",'r', encoding="utf-8") as file:
    for i, line in enumerate(file):
        clean_line = line.split(': ')[1].strip()
        first_half, second_half = [line.strip() for line in clean_line.split(' | ')]

        card = {int(x): True for x in first_half.split()}
        winning_nums = [int(x) for x in second_half.split()]

        card_num = i + 1
        matches = 0
        table[card_num] = table.get(card_num, 0) + 1

        for num in winning_nums:
            if num in card:
                matches += 1

        for j in range(card_num + 1, card_num + 1 + matches):
            table[j] = table.get(j, 0) + table[card_num]

print(sum(table.values()))
