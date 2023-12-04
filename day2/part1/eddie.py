import sys


def get_lines():
    lines = sys.stdin.readlines()
    return lines


def get_id(line):
    """

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    """
    game_str, _ = line.split(':')
    game, id = game_str.split()
    return int(id)


def parse_set(set_str):
    """

    input

    3 blue, 4 red

    output

    {
        'red': 4,
        'green': 0,
        'blue': 3
    }

    """
    counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for pick_str in set_str.split(','):
        pick_str = pick_str.strip()
        num, color = pick_str.split(' ')
        counts[color] += int(num)
    return counts


def get_sets(line):
    game, sets_str = line.split(':')
    sets_str = sets_str.strip()
    sets = []
    for set_str in sets_str.split(';'):
        set_str = set_str.strip()
        set = parse_set(set_str)
        sets.append(set)
    return sets


def is_valid_game(line):
    for set in get_sets(line):
        if set['red'] > 12 or set['green'] > 13 or set['blue'] > 14:
            return False
    return True


if __name__ == '__main__':
    valid_id_sum = 0

    lines = get_lines()
    for line in lines:
        if is_valid_game(line):
            id = get_id(line)
            valid_id_sum += id

    print(valid_id_sum)
