import re

workflow_pattern = re.compile(r'(\w+){(.*)}')

for line in open('../test_a.txt'):
    m = re.match(workflow_pattern, line)
    title, flows_text = m.groups()
    print(title)
    flows = flows_text.split(',')
    print(flows[0:-1])
    otherwise = flows[-1]
    print(otherwise)
