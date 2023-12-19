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

steps = 0
all_nodes_match = False
while not all_nodes_match:
    for c in instructions:
        checking_nodes = []
        for n in starting_nodes:
            if c == 'L':
                checking_nodes.append(networks[n][0])
            elif c == 'R':
                checking_nodes.append(networks[n][1])
        steps += 1
        all_nodes_match = True
        for checking_node in checking_nodes:
            if not checking_node.endswith('Z'):
                all_nodes_match = False
                break
        if all_nodes_match:
            break
        starting_nodes = checking_nodes

print(steps)
