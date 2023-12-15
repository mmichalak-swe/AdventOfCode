def hash_algo(lens):
    label = 0
    for char in lens:
        label += ord(char)
        label *= 17
        label %= 256
    return label


with open("./Day15/Day15_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split(',')

boxes = {x: dict() for x in range(256)}
output = 0

for seq in file_parse:
    label, focal_length = None, None
    remove_op, add_op = False, False

    if '-' in seq:
        remove_op = True
        label, focal_length = seq.split('-')
    else:
        add_op = True
        label, focal_length = seq.split('=')

    box_num = hash_algo(label)

    if add_op:
        boxes[box_num][label] = int(focal_length)
    else:
        if label in boxes[box_num]:
            del boxes[box_num][label]

for box_num, box in boxes.items():
    count = 1
    for focal_length in box.values():
        output += (box_num + 1) * count * focal_length
        count += 1

print(output)
