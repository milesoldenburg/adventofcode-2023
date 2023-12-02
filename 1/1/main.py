import re

pattern = re.compile(r'\d')

calibrations = 0
for line in open('input.txt'):
    matches = re.findall(pattern, line)
    if matches:
        calibrations += int(matches[0] + matches[-1])

print(calibrations)
