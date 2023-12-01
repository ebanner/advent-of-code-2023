def get_lines():
    with open('input', 'r') as file:
        lines = file.readlines()
    return lines


DIGITS = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six', 
    'seven',
    'eight',
    'nine'
]

DIGIT_TO_NUM = dict(zip(DIGITS, range(1, 10)))

NUM_TO_DIGIT = dict(zip(range(1, 10), DIGITS))


def is_digit(line, i):
    for digit in DIGITS:
        j = len(digit)
        sub_string = line[i:i+j]
        if sub_string == digit:
            return True
    return False


def get_digit(line, i):
    for digit in DIGITS:
        j = len(digit)
        sub_string = line[i:i+j]
        if sub_string == digit:
            return digit



def get_first_digit(line):
    """returns like 'one' or 'two'"""
    for i in range(len(line)):
        if line[i].isdigit():
            return NUM_TO_DIGIT[int(line[i])]

        if is_digit(line, i):
            digit = get_digit(line, i)
            return digit


def get_last_digit(line):
    """returns like 'one' or 'two'"""
    i = len(line) - 1
    while 0 <= i:
        if line[i].isdigit():
            return NUM_TO_DIGIT[int(line[i])]

        if is_digit(line, i):
            digit = get_digit(line, i)
            return digit
        i -= 1


def combine(l, r):
    return str(DIGIT_TO_NUM[l]) + str(DIGIT_TO_NUM[r])


if __name__ == '__main__':
    lines = get_lines()

    sum = 0
    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        combined = combine(first_digit, last_digit)
        sum += int(combined)

    print(sum)
