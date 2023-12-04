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


def get_min_cubes(line):
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in get_sets(line):
        max_red = max(max_red, set['red'])
        max_green = max(max_green, set['green'])
        max_blue = max(max_blue, set['blue'])
    return max_red, max_green, max_blue


def get_power(cubes):
    prod = 1
    for cube in cubes:
        prod *= cube
    return prod


if __name__ == '__main__':
    power_sum = 0

    lines = get_lines()
    for line in lines:
        min_cubes = get_min_cubes(line)
        power = get_power(min_cubes)
        power_sum += power

    print(power_sum)
