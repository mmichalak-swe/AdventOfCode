with open("./Day05/Day05_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

VOWELS = {'a': True,
          'e': True,
          'i': True,
          'o': True,
          'u': True
          }

NAUGHTY = {'ab': True,
           'cd': True,
           'pq': True,
           'xy': True
           }

def count_vowels(ss, vowels):
    for char in ss:
        if char in VOWELS:
            vowels.append(char)


def is_double(ss):
    return ss == len(ss) * ss[0]


def only_nice(ss):
    return ss not in NAUGHTY


nice_count = 0
for s in file_parse:
    vowels = [char for char in s if char in VOWELS]
    double_letter = False
    nice = True

    for i in range(len(s) - 1):
        ss = s[i:i+2]
        if not double_letter:
            double_letter = is_double(ss)

        nice = only_nice(ss)
        if not nice:
            break

    if len(vowels) >= 3 and double_letter and nice:
        nice_count += 1

print(nice_count)
