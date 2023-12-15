def get_lines():
    import sys
    lines = [line.strip() for line in sys.stdin.readlines()]
    return lines


def parse_section(lines, i):
    """
    seed-to-soil map:
    50 98 2
    52 50 48

    """
    name_str = lines[i]
    name, _ = name_str.split(' ')
    i += 1

    ranges = []
    n = len(lines)
    while i < n and lines[i] != '':
        range = [int(num) for num in lines[i].split(' ')]
        ranges.append(range)
        i += 1
    i += 1
    def map(x):
        for [dest, start, range_length] in ranges:
            if start <= x <= start + range_length:
                offset = x - start
                y = dest + offset
                return y
        y = x
        return y
    return map, i


def parse_seeds(lines, i):
    """
    seeds: 79 14 55 13

    """
    _, seeds_str = lines[i].split(':')
    seeds_str = seeds_str.strip()
    seeds = [int(num) for num in seeds_str.split()]
    i += 1
    i += 1

    return seeds, i


def parse_lines(lines):
    i = 0
    seed_line = lines[i]
    seeds, i = parse_seeds(lines, i)
    
    seed_to_soil_map, i = parse_section(lines, i)
    soil_to_fertilizer_map, i = parse_section(lines, i)
    fertilizer_to_water_map, i = parse_section(lines, i)
    water_to_light_map, i = parse_section(lines, i)
    light_to_temperature_map, i = parse_section(lines, i)
    temperature_to_humidity_map, i = parse_section(lines, i)
    humidity_to_location_map, i = parse_section(lines, i)

    return seeds, [
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    ]


def get_location(seed, maps):
    y = seed
    for map in maps:
        y = map(y)
    return y


def compute_min(x, y):
    if y == -1: # starting value
        return x
    else:
        return min(x, y)


if __name__ == '__main__':
    lines = get_lines()
    seeds, maps = parse_lines(lines)

    min_location = -1
    for seed in seeds:
        location = get_location(seed, maps)
        min_location = compute_min(location, min_location)
    print(min_location)

