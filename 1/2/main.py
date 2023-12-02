import re

pattern = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')
pattern2 = re.compile(r'^.*(one|two|three|four|five|six|seven|eight|nine|\d).*$')
replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

calibrations = 0
for line in open('input.txt'):
    first_match = re.search(pattern, line)
    first_match = first_match.group(0)

    last_match = re.search(pattern2, line)
    last_match = last_match.group(1)

    if first_match in replacements:
        c1 = replacements.get(first_match)
    else:
        c1 = first_match

    if last_match in replacements:
        c2 = replacements.get(last_match)
    else:
        c2 = last_match

    calibrations += int(c1 + c2)

print(calibrations)
