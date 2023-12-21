with open("./Day19/Day19_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n\n')

workflows, parts = file_parse[0].split('\n'), file_parse[1].split('\n')
workflows = {w.split('{')[0]:w.split('{')[1].strip('}').split(',') for w in workflows}
workflows['A'] = True
workflows['R'] = True

output = 0
x, m, a, s = 0, 0, 0, 0
for part in parts:
    ratings = part.strip('{').strip('}').split(',')
    for rating in ratings: exec(rating)

    workflow = 'in'
    while workflow not in {'A', 'R'}:
        for flow in workflows[workflow]:
            if flow in workflows:
                workflow = flow
                break
            comparison, new_flow = flow.split(':')
            if eval(comparison):
                workflow = new_flow
                break

    output = output + x + m + a + s if workflow == 'A' else output

print(output)
