with open("./Day02/Day02_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')


def solve(file_parse):

    surface_area = 0

    for box in file_parse:
        L, W, H = [int(x) for x in box.split('x')]
        surface_area += (2*L*W + 2*W*H + 2*H*L) + min(L*W, W*H, H*L)

    return surface_area

print(solve(file_parse))
