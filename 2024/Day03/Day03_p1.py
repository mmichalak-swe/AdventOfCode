output = 0


with open('./Day03/Day03_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        line = line.split("mul(")

        for segment in line:
            comma_split = segment.split(",")

            if len(comma_split) == 1 or not comma_split[0].isdigit():
                continue

            first_num = int(comma_split[0])

            close_paren_split = comma_split[1].split(')')
            if len(close_paren_split) == 1 or not close_paren_split[0].isdigit():
                continue

            second_num = int(close_paren_split[0])
            output += first_num * second_num

print(output)
