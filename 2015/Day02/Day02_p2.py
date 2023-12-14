with open("./Day02/Day02_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')


def solve(file_parse):

    ribbon = 0

    for box in file_parse:
        L, W, H = [int(x) for x in box.split('x')]
        small_side, mid_side, large_side = sorted([L, W, H])
        ribbon += 2*small_side + 2*mid_side + L*W*H

    return ribbon

print(solve(file_parse))
