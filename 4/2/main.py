import re

pattern = re.compile(r'^Card\s+\d+:\s+(.*)\s\|\s+(.*)$')

total_instances = 0
cards = []

for line in open('input.txt'):
    m = re.match(pattern, line)
    winning_numbers = m.group(1).split()
    draws = m.group(2).split()
    matches = 0
    for draw in draws:
        if draw in winning_numbers:
            matches += 1
    cards.append({
        'matches': matches,
        'instances': 1
    })

for i, card in enumerate(cards):
    for n in range(1, card['matches'] + 1):
        cards[i + n]['instances'] += card['instances']

total_instances = sum([x['instances'] for x in cards])

print(total_instances)
