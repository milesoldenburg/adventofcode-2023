def is_step_zeros(step):
    for x in step:
        if x != 0:
            return False
    return True


extrapolated_sum = 0
for line in open('../input.txt'):
    history = []
    step = [int(x) for x in line.split()]
    history.append(step)

    while not is_step_zeros(step):
        step = [step[i] - step[i - 1] for i in range(len(step) - 1, 0, -1)]
        step.reverse()
        history.append(step)
    history.reverse()

    for i in range(0, len(history) - 1):
        extrapolated_value = history[i][-1] + history[i + 1][-1]
        history[i + 1].append(extrapolated_value)
    extrapolated_sum += history[-1][-1]
print(extrapolated_sum)
