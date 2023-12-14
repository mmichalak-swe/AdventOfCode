output = 0


with open('./Day01/Day01_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        first_digit = ''
        second_digit = ''

        for char in line:
            if char.isdigit():
                first_digit = char
                break

        for char in line[::-1]:
            if char.isdigit():
                second_digit = char
                break

        output += (int(first_digit) * 10) + int(second_digit)

print(output)
