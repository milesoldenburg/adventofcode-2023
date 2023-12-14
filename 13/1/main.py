with open('../test.txt') as f:
    data = f.read()
    patterns = [x.splitlines() for x in data.split('\n\n')]

for pattern in patterns:
    row_mirror_point = None
    for rowi, row in enumerate(pattern):
        if rowi > 0:
            if row == pattern[rowi - 1]:
                # Found a potential mirror point
                print(f'Potential mirror between row {rowi - 1} and {rowi}')
                print(row)
                row_mirror_point = rowi - 1
                break

    if row_mirror_point is not None:
        if row_mirror_point == 0:
            print('Confirmed mirror point between row 0 and 1')
            print()
            continue
        elif row_mirror_point == len(pattern) - 2:
            print(f'Confirmed mirror point between row {len(pattern) - 2} and {len(pattern) - 1}')
            print()
            continue
        else:
            rows_match = True
            for i in range(row_mirror_point - 1, -1, -1):
                compared_rowi = row_mirror_point + 1 + row_mirror_point - i
                if compared_rowi < len(pattern) and pattern[i] != pattern[compared_rowi]:
                    rows_match = False
                    break
            if rows_match:
                print(f'Confirmed mirror point between row {row_mirror_point} and {row_mirror_point + 1}')
                print()
                continue
            else:
                print('No mirror points in rows')
    else:
        print('No mirror points in rows')

    print('Need to check for vertical now')
    print()
