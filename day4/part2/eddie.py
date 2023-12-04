def get_lines():
    import sys
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    return lines


def get_num_games(lines):
    return len(lines)


def init_num_cards_per_game(lines):
    num_games = get_num_games(lines)
    num_cards_per_game = [1]*num_games
    return num_cards_per_game


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


def get_num_winners(line):
    my_numbers = get_my_numbers(line)
    winning_numbers = get_winning_numbers(line)

    num_winners = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            num_winners += 1
    return num_winners


if __name__ == '__main__':
    lines = get_lines()

    num_games = get_num_games(lines)
    num_cards_per_game = init_num_cards_per_game(lines)
    for i, line in enumerate(lines):
        num_winners = get_num_winners(line)
        for j in range(1, num_winners+1):
            num_cards_per_game[i+j] += num_cards_per_game[i]

    num_cards = sum(num_cards_per_game)
    print(num_cards)
