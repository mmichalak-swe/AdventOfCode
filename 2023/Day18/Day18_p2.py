with open("./Day18/Day18_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

dig_plan = [
        (heading, int(steps), hexcode[2:-1])
        for heading, steps, hexcode in [line.split() for line in file_parse]
        ]

position = 0
res = 0

def get_pos(direction):
    match direction:
        case "R":
            return 1
        case "L":
            return -1
        case "U":
            return -1j
        case "D":
            return 1j


def get_lava_amount(p1, heading, steps):
    p2 = p1 + get_pos(heading) * steps

    area = 0

    # shoelace formula
    area += p1.real * p2.imag
    area -= p2.real * p1.imag

    # include the outline
    area += steps

    return area


curr_pos = 0
res = 0

for _, _, hexcode in dig_plan:
    heading, steps = hexcode[-1].translate(str.maketrans("0123", "RDLU")), int(hexcode[:-1], 16)

    res += get_lava_amount(curr_pos, heading, steps)
    curr_pos += get_pos(heading) * steps

print(int(res / 2) + 1)
