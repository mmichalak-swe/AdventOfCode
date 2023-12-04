output = 0


with open("./Day4_Input.txt",'r', encoding="utf-8") as file:
    for line in file:
        clean_line = line.split(': ')[1].strip()
        first_half, second_half = [line.strip() for line in clean_line.split(' | ')]

        card = {int(x): True for x in first_half.split()}
        winning_nums = [int(x) for x in second_half.split()]

        matches = 0

        for num in winning_nums:
            if num in card:
                matches += 1

        if matches > 0:
            output += 2**(matches - 1)

print(output)
