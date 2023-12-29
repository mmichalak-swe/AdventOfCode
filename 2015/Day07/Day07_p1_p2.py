with open("./Day07/Day07_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

calc = {}
results = {}

for command in file_parse:
    (ops, res) = command.split(' -> ')
    calc[res] = ops.split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
                res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
                res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
                res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
                res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
                res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

print(calculate('a'))
# change b to 16076 in input for part 2
