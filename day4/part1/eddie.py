def get_lines():
    import sys
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_my_numbers(line):
    """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"""

    _, nums = line.split(':')
    nums = nums.strip()
    _, my_nums_str = nums.split('|')
    my_nums_str = my_nums_str.strip()
    my_nums = [int(num_str) for num_str in my_nums_str.split()]
    return my_nums


def get_winning_numbers(line):
    """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"""

    _, nums = line.split(':')
    nums = nums.strip()
    winning_nums_str, _ = nums.split('|')
    winning_nums_str = winning_nums_str.strip()
    winning_nums = [int(num_str) for num_str in winning_nums_str.split()]
    return winning_nums


if __name__ == '__main__':
    lines = get_lines()
    total_points = 0
    for line in lines:
        my_numbers = get_my_numbers(line)
        winning_numbers = get_winning_numbers(line)

        card_points = 0
        for my_number in my_numbers:
            if my_number in winning_numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2

        total_points += card_points

    print(total_points)

