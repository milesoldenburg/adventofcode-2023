import re

instruction_pattern = re.compile(r'([RL]+)\n\n', flags=re.MULTILINE)
node_pattern = re.compile(r'(\w{3}) = \((\w{3}), (\w{3})\)')

with open('../input.txt') as f:
    data = f.read()

m = re.match(instruction_pattern, data)
instructions = m.group(1)
network_text = re.sub(instruction_pattern, '', data)

networks = {}
for n in network_text.splitlines():
    m = re.match(node_pattern, n)
    node, left_node, right_node = m.groups()
    networks[node] = (left_node, right_node)

steps = 0
node = 'AAA'
while node != 'ZZZ':
    for c in instructions:
        if c == 'L':
            node = networks[node][0]
            steps += 1
            if node == 'ZZZ':
                break
        elif c == 'R':
            node = networks[node][1]
            steps += 1
            if node == 'ZZZ':
                break

print(steps)
