from collections import defaultdict

with open("./Day19/Day19_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n\n')

w, _ = file_parse[0].split('\n'), file_parse[1].split('\n')
workflows = {}
rinputs = False
inputs = []
bnds = defaultdict(set)

for line in w:
    if line == "":
        rinputs = True
        continue
    if rinputs:
        parts = line[1:-1].split(",")
        d = {}
        for part in parts:
            a, b = part.split("=")
            d[a] = int(b)
        inputs.append(d)
    else:
        name, p = line.split("{")
        answers = []
        for part in p[:-1].split(","):
            if ":" in part:
                cond, val = part.split(":")
                sign = ">"
                if "<" in cond:
                    sign = "<"
                    nam, num = cond.split("<")
                else:
                    nam, num = cond.split(">")
                answers.append((sign, nam, int(num), val))
            else:
                answers.append(part)
        workflows[name] = answers


def get_ints(bnds, name):
    if name == "R":
        return 0
    if name == "A":
        prod = 1
        for k in bnds:
            mn, mx = bnds[k]
            prod *= max(0, mx-mn+1)
        return prod
    print(name, bnds)
    ans = 0
    for entry in workflows[name]:
        if type(entry) == str:
            ans += get_ints(bnds, entry)
        elif entry[0] == "<":
            nbnds = bnds.copy()
            nbnds[entry[1]] = (bnds[entry[1]][0], min(entry[2]-1, bnds[entry[1]][1]))
            ans += get_ints(nbnds, entry[3])
            bnds = bnds.copy()
            bnds[entry[1]] = (max(entry[2], bnds[entry[1]][0]), bnds[entry[1]][1])
        elif entry[0] == ">":
            nbnds = bnds.copy()
            nbnds[entry[1]] = (max(entry[2]+1, bnds[entry[1]][0]), bnds[entry[1]][1])
            ans += get_ints(nbnds, entry[3])
            bnds = bnds.copy()
            bnds[entry[1]] = (bnds[entry[1]][0], min(entry[2], bnds[entry[1]][1]))
    return ans

print(get_ints({"m": (1, 4000), "s": (1, 4000), "a": (1, 4000), "x": (1, 4000)}, "in"))
