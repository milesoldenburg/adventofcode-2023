import re

workflows_pattern = re.compile(r'(\w+){(.*)}')
workflow_pattern = re.compile(r'([xmas])([<>])(\d+):(\w+)')
xmas_pattern = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')

workflows = {}
for line in open('../input_a.txt'):
    m = re.match(workflows_pattern, line)
    title, flows_text = m.groups()
    flows = flows_text.split(',')
    otherwise = flows[-1]
    rules = []
    for f in flows[0:-1]:
        m = re.match(workflow_pattern, f)
        part, comparator, value, w = m.groups()
        value = int(value)
        rules.append((part, comparator, value, w))
    workflows[title] = {
        'rules': rules,
        'otherwise': otherwise
    }

accepted_parts_total = 0
for line in open('../input_b.txt'):
    match = re.match(xmas_pattern, line)
    x, m, a, s = match.groups()
    x = int(x)
    m = int(m)
    a = int(a)
    s = int(s)
    a_or_r = False
    workflow_name = 'in'
    while not a_or_r:
        workflow = workflows[workflow_name]
        rule_satisfied = False
        for rule in workflow.get('rules'):
            part = x
            if rule[0] == 'm':
                part = m
            elif rule[0] == 'a':
                part = a
            elif rule[0] == 's':
                part = s
            if rule[1] == '<':
                rule_satisfied = part < rule[2]
                if rule_satisfied:
                    if rule[3] == 'A':
                        a_or_r = True
                        accepted_parts_total += x + m + a + s
                    elif rule[3] == 'R':
                        a_or_r = True
                    else:
                        workflow_name = rule[3]
                    break
            elif rule[1] == '>':
                rule_satisfied = part > rule[2]
                if rule_satisfied:
                    if rule[3] == 'A':
                        a_or_r = True
                        accepted_parts_total += x + m + a + s
                    elif rule[3] == 'R':
                        a_or_r = True
                    else:
                        workflow_name = rule[3]
                    break
        if not rule_satisfied:
            otherwise = workflow.get('otherwise')
            if otherwise == 'A':
                a_or_r = True
                accepted_parts_total += x + m + a + s
            elif otherwise == 'R':
                a_or_r = True
            else:
                workflow_name = otherwise

print(accepted_parts_total)
