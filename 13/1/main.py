import functools


def find_mirror_point(pattern):
    potential_mirror_points = []
    for i, block in enumerate(pattern):
        if i > 0:
            if block == pattern[i - 1]:
                print(f'Potential mirror between block {i - 1} and {i}')
                print(block)
                potential_mirror_points.append(i - 1)

    for potential_mirror_point in potential_mirror_points:
        if potential_mirror_point == 0:
            print('Confirmed mirror point between block 0 and 1')
            print()
            return potential_mirror_point
        elif potential_mirror_point == len(pattern) - 2:
            print(f'Confirmed mirror point between block {len(pattern) - 2} and {len(pattern) - 1}')
            print()
            return potential_mirror_point
        else:
            blocks_match = True
            for i in range(potential_mirror_point - 1, -1, -1):
                compared_blocki = potential_mirror_point + 1 + potential_mirror_point - i
                print(f'Comparing block {i} and {compared_blocki}')
                if compared_blocki < len(pattern) and pattern[i] != pattern[compared_blocki]:
                    blocks_match = False
                    break
            if blocks_match:
                print(f'Confirmed mirror point between block {potential_mirror_point} and {potential_mirror_point + 1}')
                print()
                return potential_mirror_point
            else:
                print('No mirror points in block')

    return None


with open('../input.txt') as f:
    data = f.read()
    patterns = [x.splitlines() for x in data.split('\n\n')]

summary = 0
for pattern in patterns:
    print('Checking rows...')
    row_mirror_point = find_mirror_point(pattern)

    if row_mirror_point is not None:
        summary += (row_mirror_point + 1) * 100
    else:
        print('Checking columns...')
        columns = [functools.reduce(lambda x, y: x + y[i], pattern, '') for i in range(len(pattern[0]))]
        column_mirror_point = find_mirror_point(columns)
        summary += column_mirror_point + 1

print(summary)
