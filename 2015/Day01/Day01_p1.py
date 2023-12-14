with open("./Day01/Day01_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read()


def solve(file_parse):

    floor = 0

    for char in file_parse:
        floor = floor + 1 if char == '(' else floor - 1

    return floor

print(solve(file_parse))
