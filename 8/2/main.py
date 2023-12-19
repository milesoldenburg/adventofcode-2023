import math
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

starting_nodes = [x for x in networks if x.endswith('A')]
node_steps = []

for n in starting_nodes:
    steps = 0
    node = n
    while not node.endswith('Z'):
        for c in instructions:
            if c == 'L':
                node = networks[node][0]
                steps += 1
                if node.endswith('Z'):
                    break
            elif c == 'R':
                node = networks[node][1]
                steps += 1
                if node.endswith('Z'):
                    break
    node_steps.append(steps)

print(math.lcm(*node_steps))
