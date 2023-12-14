with open("./Day01/Day01_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read()


def solve(file_parse):

    count_up = 0
    count_down = 0

    for step, char in enumerate(file_parse):
        if char == '(':
            count_up += 1
        else:
            count_down += 1

        if count_up - count_down == -1:
            return step + 1

print(solve(file_parse))
