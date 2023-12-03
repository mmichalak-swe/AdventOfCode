output = 0

trie = {"o": {"on": {"one": '!'}},
        "t": {"tw": {"two": '!'},
              "th": {"thr": {"thre": {"three": '!'}}}},
        "f": {"fo": {"fou": {"four": '!'}},
              "fi": {"fiv": {"five": '!'}}},
        "s": {"si": {"six": '!'},
              "se": {"sev": {"seve": {"seven": '!'}}}},
        "e": {"ei": {"eig": {"eigh": {"eight": '!'}}}},
        "n": {"ni": {"nin": {"nine": '!'}}}
}

word_to_number = {"one": 1,
                  "two": 2,
                  "three": 3,
                  "four": 4,
                  "five": 5,
                  "six": 6,
                  "seven": 7,
                  "eight": 8,
                  "nine": 9
}


def word_checker(lookup, test_str, idx=1):
    if idx > len(test_str):
        return -1

    curr = test_str[:idx]
    if curr not in lookup:
        return -1

    if lookup[curr] == '!':
        return curr

    return word_checker(lookup[curr], test_str, idx+1)


with open('./Day1_Input.txt','r', encoding="utf-8") as myfile:
    for line in myfile:
        line = line.strip()
        first_digit = ''
        second_digit = ''

        for i, char in enumerate(line):
            if char.isdigit():
                first_digit = char
                break
            if char in trie:
                check_str = line[i:i+5]
                result = word_checker(trie, check_str)
                if result != -1:
                    first_digit = word_to_number[result]
                    break

        for i in range(len(line) - 1, -1, -1):
            char = line[i]
            if char.isdigit():
                second_digit = char
                break
            if char in trie:
                check_str = line[i:i+5]
                result = word_checker(trie, check_str)
                if result != -1:
                    second_digit = word_to_number[result]
                    break

        output += (int(first_digit) * 10) + int(second_digit)

print(output)
