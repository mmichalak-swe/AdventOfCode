output = 0


def increasing_check(report):
    for i in range(1, len(report)):
        if not 1 <= report[i] - report[i - 1] <= 3:
            return False
    return True


def decreasing_check(report):
    for i in range(1, len(report)):
        if not 1 <= report[i - 1] - report[i] <= 3:
            return False
    return True


with open('./Day02/Day02_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        report = [int(x) for x in line.strip().split(" ")]

        if increasing_check(report) or decreasing_check(report):
            output += 1

print(output)
