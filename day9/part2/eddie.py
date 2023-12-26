def parse_history(line):
    history = [int(num) for num in line.split()]
    return history


def get_lines():
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    return lines


def get_histories(lines):
    histories = []
    for line in lines:
        history = parse_history(line)
        histories.append(history)
    return histories


def all_zero(A):
    return all(elem == 0 for elem in A)


def get_differences(A):
    n = len(A)
    m = n-1
    differences = [0]*m
    for i in range(m):
        differences[i] = A[i+1] - A[i]
    return differences


def get_next_value(differences):
    """

    [0, 3, 6, 9, 12, 15]

    """
    if all_zero(differences):
        return 0
    else:
        next_differences = get_differences(differences)
        next_value = get_next_value(next_differences)
        return differences[0] - next_value


if __name__ == '__main__':
    lines = get_lines()
    histories = get_histories(lines)

    next_value_sum = 0
    for history in histories:
        next_value = get_next_value(history)
        next_value_sum += next_value

    print(next_value_sum)
