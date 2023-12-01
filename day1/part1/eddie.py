def get_lines():
    with open('input', 'r') as file:
        lines = file.readlines()
    return lines


def get_first_digit(line):
    for char in line:
        if char.isdigit():
            return char


def get_last_digit(line):
    i = len(line) - 1
    while 0 <= i:
        char = line[i]
        if char.isdigit():
            return char
        i -= 1


def combine(l, r):
    return l + r


if __name__ == '__main__':
    lines = get_lines()

    sum = 0
    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        combined = combine(first_digit, last_digit)
        sum += int(combined)

    print(sum)
